package SL1Assignment;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Inventory {
    Map<Integer, Item > inventory = new HashMap<>();

    int invId;
    Inventory(){
        this.invId = 0;
    }

    void addItem(Item item){
        inventory.put(invId++,item);
        System.out.println("Item added: "+item.getItemName());
    }

    void addMultipleItems(List<Item> items){
        for(Item ii: items){
            if (ii==null){
                break;
            }
            inventory.put(invId++,ii);
        }
        System.out.println("All Items added ");
    }
    boolean updateInventoryAsPerCart(Cart c){

        for (Item i:c.getCartItems()) {
            if (i == null) {
                break;
            }
            Item invItem = getItemByName(i.getItemName());

            if(invItem.getItemName().equals(i.getItemName())){

                invItem.setQuantity( invItem.getQuantity() - i.getQuantity() );
            }
        }
        return true;
    }
    Item getItemByName(String name){
        for (Item i:inventory.values()){
            if(i==null){
                break;
            }
            if(i.getItemName().equals(name)){
                return i;
            }
        }
        return null;
    }
    Item getItemById(Integer id){
        if(id > invId){
            throw new InventoryException("Item not found");
        }
        return inventory.get(id);
    }
    boolean validateCartItems(Cart c){
         for(Item i: c.getCartItems()){
              if(i.getQuantity() > getItemByName(i.getItemName()).getQuantity()){
                  return false;
              }
         }
         return true;
    }

    public int getPrice(Item item) {
        for (Item i: inventory.values()){
            if (i==null){
                break;
            }

            String str1 = i.getItemName(), str2 = item.getItemName();
            if(str1.equals(str2)){
                return i.getPrice();
            }
        }
        return 0;
    }

    void printInventoryItems(){
        System.out.println("-------------------------------------------");
        System.out.println("------------- Inventory Items --------------");
        System.out.println("--------------------------------------------");
        System.out.println("Name \t\t Quantity \t\t price ");

        for(Item item:inventory.values()){
            if (item==null){
                break;
            }
            StringBuilder sb = new StringBuilder(item.getItemName());
            int i=0;
            for(i=0;i<10;i++){
                if(i < item.getItemName().length()){

                }
                else {
                    sb.append(" ");
                }
            }

            System.out.println(sb.toString() +" \t "+item.getQuantity()+" \t\t\t "+item.getPrice() );
        }
        System.out.println("------------ Inventory List End ------------\n");
    }
}
