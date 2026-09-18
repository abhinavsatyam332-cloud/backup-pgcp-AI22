package SL1.Task2.classes;

import java.util.HashMap;
import java.util.Map;

public class Cart {

    Map<Integer, Items> cart = new HashMap<>();
    Process process;

    public Cart(Process process) {
        this.process = process;
    }

    // Add in cart
    void addCart(int id, int quantity) {
        if (cart.containsKey(id)) {

            Items storeItem = process.inventory.getItem(id);
            Items existingItem = cart.get(id);


            process.addInCart(id, quantity);
            existingItem.setQuantity(existingItem.getQuantity() + quantity);
        } else {
            Items newItem = process.addInCart(id, quantity);
            cart.put(id, newItem);
        }
    }

    void removeCart(int id, int quantity) {
        if (cart.containsKey(id)) {
            Items cartItem = cart.get(id);
            if (quantity > cartItem.getQuantity()) {
                System.out.println("Cannot remove more than what is in the cart!");
                return;
            }

            cartItem.setQuantity(cartItem.getQuantity() - quantity);
            process.addInInventory(id, quantity);

            // Remove item from map if quantity drops to 0
            if (cartItem.getQuantity() == 0) {
                cart.remove(id);
            }
            System.out.println("Item removed successfully!");
        } else {
            System.out.println("Please enter a valid cart item ID.");
        }
    }

    // View items in cart
    Map<Integer, Items> showCart() {
                return cart;
    }

    // cart total
    int totalAmount(){
        int total=0;
        for(Items item:cart.values()){
            total= total + (item.getPrice()* item.getQuantity());
        }
    return total;
    }
}