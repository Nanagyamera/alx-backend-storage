-- Create stored procedure ComputeAverageWeightedScoreForUsers
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Declare variables
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE avg_weighted_score FLOAT;
    
    -- Declare cursor for iterating through users
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    -- Open cursor and start iterating through users
    OPEN cur;
    read_loop: LOOP
        -- Fetch next user_id from the cursor
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        -- Compute the average weighted score for the user
        SELECT AVG(score * weight) INTO avg_weighted_score
        FROM corrections
        WHERE user_id = user_id;
        
        -- Update the average_weighted_score column for the user in the users table
        UPDATE users
        SET average_weighted_score = avg_weighted_score
        WHERE id = user_id;
    END LOOP;
    
    -- Close the cursor
    CLOSE cur;
