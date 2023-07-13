-- Create trigger to decrease item quantity after adding a new order
CREATE TRIGGER IF NOT EXIST decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
        SET quantity = quantity - NEW.number
        WHERE name = NEW.item_name;
END;
