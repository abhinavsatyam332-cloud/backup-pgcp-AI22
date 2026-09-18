package SLAssignment;


import SLAssignment.Exceptions.InventoryException;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class Inventory {
    Map<Integer, Item> map = new HashMap<Integer,Item>();

    //Remove and add to cart
    public void remove(Item item){
        map.remove(item.getId());
    }

    //Updating the quantity in inventory
    public void update(int id, int quantity){
        if(map.containsKey(id)){
            int a=map.get(id).getQuantity();
            map.get(id).setQuantity(a-quantity);
        }
    }

    //Add to inventory and remove from cart
    public void add(Item item){
        map.put(item.getId(), item);
    }

    // Getting values by itd
    public Item get(int id){
        try {
            Item i = map.get(id);
            return i;
        }catch (InventoryException e){
            System.out.println("Not in stock, available stock: "+ map.get(id).getQuantity() );
        }

        return null;

    }

    public Collection<Item> getAll(){

        return map.values();

    }







}
