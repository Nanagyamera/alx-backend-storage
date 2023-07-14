-- List bands with Glam rock as their main style, ranked by longevity
SELECT band_name, 
       (CASE
            WHEN split IS NULL THEN YEAR('2022-01-01') - formed
            ELSE split - formed
        END) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
