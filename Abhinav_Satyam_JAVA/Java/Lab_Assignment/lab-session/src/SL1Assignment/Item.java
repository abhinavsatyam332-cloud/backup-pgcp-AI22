package SL1Assignment;

public class Item {
    private String itemName;
    private int id;
    private int price;
    private int quantity;
    private int amount;
    Item(int id,String itemName, int price,int quantity,int amount){
        this.id = id;
        this.itemName = itemName;
        this.price = price;
        this.quantity = quantity;
        this.amount = amount;
    }

    Item(int id,String itemName, int price,int quantity){
        this.id = id;
        this.itemName = itemName;
        this.price = price;
        this.quantity = quantity;
        this.amount =0;
    }

    Item(String itemName, int quantity){
        this.itemName = itemName;
        this.quantity = quantity;
        this.amount =0;

    }

    String getItemName(){
        return this.itemName;
    }
    int getPrice(){
        return this.price;
    }
    void setPrice(int price){
        this.price = price;
    }
    int getQuantity(){
        return  this.quantity;
    }
    int getAmount(){
        return this.amount;
    }

    boolean setQuantity(int quantity){
        this.quantity = quantity;
        return true;
    }
    boolean setAmount(int amount){
        this.amount = amount;
        return true;
    }
}
