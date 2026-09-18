package SL1Assignment;

import java.util.ArrayList;
import java.util.List;

public class Cart {
    List<Item> cart = null;
    int totalAmount ;
    Cart(){
        cart = new ArrayList<>();
        totalAmount = 0;
    }

    void addItem(Item item){

        cart.add(item);

    }
    List<Item> getCartItems(){
        return this.cart;
    }
    void addMultipleItems(List<Item> items){
        cart.addAll(items);
        System.out.println("Multiple items added");
    }
    int getTotalAmount(){
        for(Item item:cart){
            if (item==null){
                break;
            }
            totalAmount += item.getAmount();
        }
        return totalAmount;
    }

    void printCartItems(){
        System.out.println("---------------------------------------");
        System.out.println("------------- Cart Items --------------");
        System.out.println("---------------------------------------");
        System.out.println("Name \t Quantity \t price  ");
        for(Item item:cart){
            if (item==null){
                break;
            }
            System.out.println(item.getItemName() +" \t "+item.getQuantity()+" \t\t\t "+item.getPrice() +" \t ");
        }

        System.out.println("Total amount: "+getTotalAmount());
        totalAmount=0;
        System.out.println("----------- Cart List End --------------\n");
    }
}
