package SL1Assignment;

import day3.Car;

import java.util.*;

public class Processing {
    Cart cart;
    Inventory inventory;
    Map<Item,Integer> statistics;

    Processing(){
        inventory = new Inventory();
        cart = new Cart();
        statistics = new HashMap<>();
    }

    public void addInventory(Inventory inventory){
        this.inventory = inventory;
    }

    public void addInventoryItem(Item item){
        inventory.addItem(item);
    }

    public void addCartItem(Item item){
        int price = inventory.getPrice(item);
        item.setPrice(price);
        item.setAmount( price * item.getQuantity() );

        cart.addItem(item);
        System.out.println("Item added: "+item.getItemName());
    }
    void addToStatistics(Cart c,int noSoldItems){
        for (Item i:c.getCartItems()){
            if(i==null){
                break;
            }
            statistics.put(i,noSoldItems);
        }
    }
    void getStatistics(){
      // will avail soon
//        statistics.


    }
    public void checkOut(){
        if(inventory.validateCartItems(cart)){
            System.out.println("Please pay: "+ cart.getTotalAmount());
            int pay= new Scanner(System.in).nextInt();
            if(pay < cart.totalAmount){
                throw new PaymentException("PaymentException");
            }
            System.out.println("Rs. "+pay+" Payment successfull..");
            System.out.println("Shipping your product..");



            if(!inventory.updateInventoryAsPerCart(cart)){
                throw new InventoryException("Inventory update exception");
            }
        }else{
            throw new InventoryException("Inventory exception");
        }
    }

    public void showCart(){
        cart.printCartItems();
    }

    public void showInventory(){
        inventory.printInventoryItems();
    }

}
