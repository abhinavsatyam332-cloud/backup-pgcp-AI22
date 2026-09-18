package SLAssignment;

public class Process {


    Inventory inventory;
    Cart cart;

    Process(Inventory inventory){
        this.inventory=inventory;
        this.cart=new Cart();
    }


    void addInCart(int id, int quantity){
        Item i = inventory.get(id);
        Item c= new Item(i.getId(),i.getName(),quantity,i.getPrice());
        cart.addItem(c);
        inventory.get(id).setQuantity(inventory.get(id).getQuantity()-quantity);
    }
}
