CREATE TABLE IF NOT EXISTS produit (
  id_reference_produit TEXT,
  nom TEXT,
  prix NUMERIC,
  stock INT, 
    PRIMARY KEY(id_reference_produit)
);


CREATE TABLE IF NOT EXISTS magasin(
    id_magasin TEXT,
    ville TEXT,
    nombre_de_salaries INT,
    PRIMARY KEY(id_magasin)
);


CREATE TABLE IF NOT EXISTS vente(
    date TEXT, 
    id_reference_produit TEXT , 
    quantite INT,
    id_magasin TEXT, 
    PRIMARY KEY(date,id_reference_produit,id_magasin),
    FOREIGN KEY (id_reference_produit)REFERENCES produit(id_reference_produit),
    FOREIGN KEY (id_magasin) REFERENCES magasin(id_magasin)
);


CREATE TABLE IF NOT EXISTS vente_par_region(
    region TEXT, 
    vente_total_region INT
);


CREATE TABLE IF NOT EXISTS vente_par_produit(
    id_reference_produit TEXT, 
    quantite_total INT,
    prix_unitaire NUMERIC,
    prix_total NUMERIC
);

CREATE TABLE IF NOT EXISTS chiffre_affaire(
    chiffre_affaire_total NUMERIC
    );
