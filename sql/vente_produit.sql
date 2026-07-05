SELECT v.id_reference_produit,SUM(v.quantite) AS quantite_total,p.prix AS prix_unitaire,SUM(p.prix*quantite) AS prix_total
FROM vente AS v
LEFT JOIN produit AS p 
ON v.id_reference_produit=p.id_reference_produit
GROUP BY v.id_reference_produit
