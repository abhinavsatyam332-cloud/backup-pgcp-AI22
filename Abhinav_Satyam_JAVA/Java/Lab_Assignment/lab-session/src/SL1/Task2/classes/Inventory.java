package SL1.Task2.classes;

import java.util.*;

public class Inventory {

    Map<Integer,Items> map = new HashMap<>();

    // add items in inventory
    void addItem(Items item){
        map.put(item.getId(),item);
    }

    //get data from inventory
    Items getItem(int id){
        return map.get(id);
    }

    // get all data
    Collection<Items> allItems(){
        return map.values();
    }

}
