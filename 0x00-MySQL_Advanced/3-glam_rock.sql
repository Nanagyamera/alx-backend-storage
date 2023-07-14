-- Create a temporary table to store the computed lifespan for each band
CREATE TEMPORARY TABLE temp_band_lifespan AS
SELECT
    band_name,
    CASE
        WHEN split IS NULL THEN 2022 - formed
        ELSE split - formed
    END AS lifespan
FROM
    bands
WHERE
    style LIKE '%Glam rock%';

-- Rank the bands by their longevity
SELECT
    band_name,
    lifespan
FROM
    temp_band_lifespan
ORDER BY
    lifespan DESC;
