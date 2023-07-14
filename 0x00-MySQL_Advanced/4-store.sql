-- Create trigger to decrease item quantity after adding a new order
DROP TRIGGER IF EXISTS decrease_quantity;
DELIMITER $$
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
        SET quantity = quantity - NEW.quantity
        WHERE name = NEW.item_name;
END $$
DELIMITER ;
