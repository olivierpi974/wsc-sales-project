from main import connect_db
import sqlite3
import pandas as pd
from main import load_data

def analysis(conn,file_path):
    """Cette fonction permet d'éxecuter uner requête SQL à partir d'un fichier dans la base de donnée
    elle retourne un dataframe
    """

    #création du cursor
    c=conn.cursor()
    # Lecture du fichier
    fd=open(file_path,'r')
    query=fd.read()
    fd.close()
    # execution de la requête
    res=c.execute(query)
    #resultat à partir du cursor avec fetchall
    result=res.fetchall()
    #transformation du resultat en dataframe
    
    df=pd.DataFrame(result)
    

    return df

if __name__ == '__main__':
    #connexion à la base de donnée
    conn=connect_db('./db/wsc.db')
    total_ca_path='./sql/total_ca.sql'
    vente_produit_path='./sql/vente_produit.sql'
    vente_region_path='./sql/vente_region.sql'

    #creation des datframes
    total_ca= analysis(conn, total_ca_path )
    vente_produit=analysis(conn, vente_produit_path)
    vente_region=analysis(conn,vente_region_path)

    print(vente_produit.columns.tolist())
    #ingestion dans la base de donnée

    load_data(df=total_ca,conn=conn,table_name='chiffre_affaire')
    load_data(df=vente_produit,conn=conn,table_name='vente_par_produit')
    load_data(df=vente_region,conn=conn,table_name='vente_par_region')