package SL1.Task2.classes;

import SL1Assignment.InventoryException;
import SL1.Task2.Exception.InvalidQuantity;
import SL1.Task2.Exception.ProductNotFound;

import java.util.Scanner;

public class User {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Items item = new Items(1, "Milk", 30, 50);
        Items item1 = new Items(2, "Bread", 50, 10);
        Items item2 = new Items(3, "Coke", 70, 30);
        Items item3 = new Items(4, "Chocolate", 110, 55);
        Items item4 = new Items(5, "Water", 20, 20);

        Inventory inventory = new Inventory();
        inventory.addItem(item);
        inventory.addItem(item1);
        inventory.addItem(item2);
        inventory.addItem(item3);
        inventory.addItem(item4);

        Process process = new Process(inventory);
        Cart cart = new Cart(process);

        int choice = 0;


        while (choice != 6) {
            System.out.println("\n------------------- MENU --------------------\n" +
                    "1. Check available items in store\n" +
                    "2. Add item to cart\n" +
                    "3. Remove item from cart\n" +
                    "4. Open cart\n" +
                    "5. Total amount\n"+
                    "6. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            System.out.println();

            switch (choice) {
                case 1: {
                    System.out.println("--- Items available in store ---");
                    System.out.println(inventory.allItems());
                    break;
                }
                case 2: {
                    System.out.println("Please enter the product id:");
                    int id = sc.nextInt();
                    System.out.println("Enter quantity:");
                    int quantity = sc.nextInt();

                    try {
                        cart.addCart(id, quantity);
                        System.out.println("Item added successfully!");
                    } catch (ProductNotFound | InventoryException | InvalidQuantity e) {
                        System.out.println("Error: " + e.getMessage());
                    }
                    break;
                }
                case 3: {

                    try {
                        System.out.println("Please enter the product id:");
                        int id = sc.nextInt();
                        System.out.println("Enter quantity:");
                        int quantity = sc.nextInt();
                        cart.removeCart(id, quantity);

                    }catch (ProductNotFound p ){
                        throw new ProductNotFound(p.getMessage());
                    }
                    break;
                }
                case 4: {
                    System.out.println("----------- Cart -----------");
                    System.out.println(cart.showCart());
                    break;
                }
                case 5: {
                    System.out.println(cart.totalAmount());
                    break;
                }case 6: {
                    System.out.println("Thank you for shopping with us!");
                    break;
                }
                default: {
                    System.out.println("Invalid choice! Please choose between 1 and 5.");
                }
            }
        }
        sc.close();
    }
}