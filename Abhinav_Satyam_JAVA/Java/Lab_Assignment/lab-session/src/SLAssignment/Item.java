package SLAssignment;

public class Item {
    private int id;
    private String name;
    private int quantity;
    private int price;

    Item(int id, String name, int quantity, int price){
        this.id=id;
        this.name=name;
        this.quantity=quantity;
        this.price=price;
    }

    public int getId() {
        return id;
    }

    public int getPrice() {
        return price;
    }

    public String getName() {
        return name;
    }

    public int getQuantity() {
        return quantity;
    }


    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    @Override
    public String toString() {
        return id+" "+name+" "+quantity+" "+price+"\n" ;
    }
}
