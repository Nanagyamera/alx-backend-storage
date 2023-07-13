SQL SCRIPTS AND STORED PROCEDURES

This repository contains a collection of SQL scripts and stored procedures to perform various tasks and computations on database tables. Each script is designed to meet specific requirements and can be executed on any compatible database system.

TABLE OF CONTENTS

AddBonus

ComputeAverageScoreForUser

ComputeAverageWeightedScoreForUser

ComputeAverageWeightedScoreForUsers

CreateTableUsers

CreateTriggerDecreaseQuantity

CreateTriggerResetValidEmail

CreateViewNeedMeeting

CreateIndexIdxNameFirst

CreateIndexIdxNameFirstScore

FunctionSafeDiv

AddBonus

Description: This SQL script creates a stored procedure named AddBonus that adds a new correction for a student. It takes three inputs: user_id, project_name, and score. If the project name does not exist in the table, it creates a new entry. The script assumes the existence of an projects table and an items table.

ComputeAverageScoreForUser

Description: This SQL script creates a stored procedure named ComputeAverageScoreForUser that computes and stores the average score for a student. It takes one input: user_id. The script assumes the existence of a corrections table and an users table.

ComputeAverageWeightedScoreForUser

Description: This SQL script creates a stored procedure named ComputeAverageWeightedScoreForUser that computes and stores the average weighted score for a student. It takes one input: user_id. The script assumes the existence of a corrections table and an users table.

ComputeAverageWeightedScoreForUsers

Description: This SQL script creates a stored procedure named ComputeAverageWeightedScoreForUsers that computes and stores the average weighted score for all students. The script assumes the existence of a corrections table and an users table.

CreateTableUsers

Description: This SQL script creates a table named users with specified attributes (id, email, name, country). If the table already exists, the script does not fail.

CreateTriggerDecreaseQuantity

Description: This SQL script creates a trigger named decrease_quantity_trigger that decreases the quantity of an item after adding a new order. The script assumes the existence of orders and items tables.

CreateTriggerResetValidEmail

Description: This SQL script creates a trigger named reset_valid_email_trigger that resets the valid_email attribute only when the email has been changed. The script assumes the existence of an users table.

CreateViewNeedMeeting

Description: This SQL script creates a view named need_meeting that lists all students with a score under 80 (strict) and either no last_meeting date or a last_meeting date that is more than one month ago. The script assumes the existence of a students table.

CreateIndexIdxNameFirst

Description: This SQL script creates an index named idx_name_first on the table names for the first letter of the name column. The script assumes the existence of a names table.

CreateIndexIdxNameFirstScore

Description: This SQL script creates an index named idx_name_first_score on the table names for the first letter of the name column and the score column. The script assumes the existence of a names table.

FunctionSafeDiv

Description: This SQL script creates a function named SafeDiv that divides two numbers and returns the result. If the second number is 0, it returns 0. The script assumes the existence of a corrections table.

Please refer to the individual SQL script files for detailed code and usage instructions.
