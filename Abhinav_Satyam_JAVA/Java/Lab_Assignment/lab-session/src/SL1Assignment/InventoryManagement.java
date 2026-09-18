package SL1Assignment;

public class InventoryManagement {
    public static void main(String[] args) {
        Processing processing = new Processing();

        Inventory inventory = new Inventory();
        inventory.addItem(new Item(1,"Milk",80,10));
        inventory.addItem(new Item(2,"Butter",280,10));
        inventory.addItem(new Item(3,"kurkure",5,10));
        inventory.addItem(new Item(4,"biscuit",20,10));

        processing.addInventory(inventory);

        processing.addCartItem(new Item("Milk",5));
        processing.addCartItem(new Item("Butter",5));


        processing.showCart();
        processing.showInventory();

        processing.checkOut();
        processing.showInventory();
    }
}
