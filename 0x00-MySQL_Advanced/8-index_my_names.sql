-- Create index idx_name_first on the first letter of name
CREATE INDEX idx_name_first ON names (SUBSTR(name, 1, 1));