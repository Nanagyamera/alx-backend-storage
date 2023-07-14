-- Create stored procedure AddBonus
CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score FLOAT
)
BEGIN
    DECLARE project_id INT;
    
    -- Check if project already exists in the projects table
    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name;
    
    -- If project doesn't exist, create a new entry in the projects table
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;
    
    -- Add the correction for the student
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
END;
