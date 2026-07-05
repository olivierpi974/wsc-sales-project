WITH vente_ville AS(
SELECT m.ville, SUM(v.quantite*p.prix) AS vente_total
FROM vente AS v
LEFT JOIN produit AS p 
ON v.id_reference_produit=p.id_reference_produit
LEFT JOIN magasin as m
ON v.id_magasin=m.id_magasin
GROUP BY m.ville)

SELECT CASE ville
    WHEN 'Paris' THEN 'Ile de france'
    WHEN 'Marseille'THEN 'Bouche du rhone'
    WHEN 'Lyon' THEN 'Auvergne rhone alpe'
    WHEN 'Bordeaux' THEN 'Aquitaine'
    WHEN 'Lille' THEN 'Haut de france'
    WHEN 'Nantes' THEN 'Pays de la loire'
    WHEN 'Strasbourg' THEN 'Alsace'
    END AS region,
    SUM(vente_total) AS vente_total_region
FROM vente_ville
GROUP BY ville