package SL1.Task2.classes;

public class Items {
    private int id;
    private String name;
    private int price;
    private int quantity;

    Items(int id,String name,int price,int quantity){
        this.id=id;
        this.name=name;
        this.price=price;
        this.quantity=quantity;

    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getQuantity() {
        return quantity;
    }

    public int getPrice() {
        return price;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    @Override
    public String toString() {

        return "id : "+id+", " +
                "Name : "+name+", " +
                "Quantity : "+quantity+", " +
                "Price : "+price+"\n" ;
    }
}
