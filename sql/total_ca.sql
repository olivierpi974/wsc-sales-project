SELECT SUM(p.prix*v.quantite) AS chiffre_affaire_total
FROM vente AS v
LEFT JOIN produit AS p ON v.id_reference_produit=p.id_reference_produit



