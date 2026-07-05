import pandas as pd
import sqlite3
import requests
from sqlite3 import OperationalError
from io import StringIO

##1.definition des fonctions

#fonction execution sql script from files
def connect_db(db_path):
    """Cette fonction permet de créer un fichier .db 
    s'il n'existe pas et de retourner la connexion à la base de donnée
    db_path: chemin du ficher.db
    """
    conn=sqlite3.connect(db_path)
    #modificaiton de la forme des resultats
    conn.row_factory = lambda cursor, row: {col[0] : row[i] for i,col in enumerate(cursor.description)}
    return conn


def execute_script_from_file(conn,file_path):
    """Cette fonction permet de lire un fichier .sql et 
    d'executer les script SQL dans la base de donnée à partir
    de la connexion.
    conn: connexion à la base de donnée
    file_path: chemin d'accès des fichier sql"""
    #crée un cursor à partir de la connexion 
    c=conn.cursor()
    
    #Ouvre le script SQL et le lit
    fd= open(file_path,'r')
    sqlFile=fd.read()
    fd.close()

    #séparation du script 
    sqlcommand=sqlFile.split(';')
    # execution de chaque requête
    for command in sqlcommand:
        try:
            c.execute(command)
    
        except OperationalError as msg:
            print("Command skipped",msg)
    conn.commit()

def get_csv(url):
    
    response=requests.get(url=url)
    response.encoding = 'utf-8'
    if response.status_code != 200:
        print('Error')
        return None
    
    result=response.text
    
    df=pd.read_csv(StringIO(result))
    return df

# fonction transformation des noms de colonnes
def transform_column(df):
    df.columns=df.columns.str.strip()
    df.columns=df.columns.str.lower().str.replace(" ", "_")
    df.columns=df.columns.str.lower().str.replace("é", "e")
    
    return df

# fonction Ingestion des données
def load_data(df,conn, table_name, truncate=False,INSERT_OR_IGNORE=False):
    """Cette fonction  permet de charger les données
    dans la base de donnée """
    if truncate==True:
        sql_state=f"DELETE FROM {table_name}"
        conn.execute(sql_state)
        conn.commit()
    if INSERT_OR_IGNORE==True:
        columns = ', '.join(df.columns)
        placeholders = ', '.join(['?' for _ in df.columns])
        for _, row in df.iterrows():
            conn.execute(f"""
                INSERT OR IGNORE INTO {table_name}({columns})
                VALUES ({placeholders})
            """, (tuple(row.values)))
        conn.commit()
            
    else:
        df.to_sql(f'{table_name}',conn,if_exists="append",index=False)

    
    print(f'{table_name} chargée')

## 2.Utilisation des fonctions 

#excution du script
#ingestion


if __name__ == '__main__':
    db_path='./db/wsc.db'
    sql_script='./sql/create_table.sql'
    url= "https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=0&single=true&output=csv"
    url_2='https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=714623615&single=true&output=csv'
    url_3='https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=760830694&single=true&output=csv'

    #Connexion à la DB
    conn=connect_db(db_path)
    #Création des tables
    execute_script_from_file(conn,sql_script)
    #Récupération des CSV
    produit=get_csv(url)
    magasin=get_csv(url_2)
    vente=get_csv(url_3)
    #Transformation des colonnes
   
    produit=transform_column(produit)
    magasin=transform_column(magasin)
    vente=transform_column(vente)
    
    #Ingestion des données
    load_data(produit, conn, 'produit',truncate=True)
    load_data(magasin,conn,'magasin',truncate=True)
    load_data(vente,conn,'vente',INSERT_OR_IGNORE=True)
