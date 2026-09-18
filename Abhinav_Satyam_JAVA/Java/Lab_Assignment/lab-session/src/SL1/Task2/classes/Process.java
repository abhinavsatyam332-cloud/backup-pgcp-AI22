package SL1.Task2.classes;

import SL1.Task2.Exception.ProductNotFound;
import SL1Assignment.InventoryException;

public class Process {
    Inventory inventory;
    Process(Inventory inventory){
        this.inventory=inventory;
    }

    // add item in cart
    Items addInCart(int id, int quantity) throws InventoryException {
        Items i = inventory.getItem(id);
        if (i == null) {
            throw new ProductNotFound("Product with ID " + id + " not found!");
        }
        if (quantity > i.getQuantity()) {
            throw new InventoryException("Required Quantity is not available");
        }

        Items c = new Items(i.getId(), i.getName(), i.getPrice(), quantity);
        i.setQuantity(i.getQuantity() - quantity);
        return c;
    }

    void addInInventory(int id, int quantity) {
        Items i = inventory.getItem(id);
        if (i != null) {
            i.setQuantity(i.getQuantity() + quantity);
        }
    }


}
