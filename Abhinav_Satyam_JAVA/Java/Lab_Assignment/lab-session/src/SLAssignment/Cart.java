package SLAssignment;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class Cart {
//    Inventory invent;
//    Cart(){
//
//    }
//    Cart(Inventory inventory){
//        this. invent=inventory;
//    }


    List<Item> list = new ArrayList<>();

    //Add Item in cart
    public void addItem(Item item){

        list.add(item);
    }

    // Getting items in cart
    public List<Item> getItem(){
        return list;
    }

}
