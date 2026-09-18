package SLAssignment;

import day3.Car;

import java.util.Scanner;

public class User {

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        Item item = new Item(1,"Milk", 50,30);
        Item item1 = new Item(2,"Bread", 10,50);
        Item item2 = new Item(3,"Coke", 30,70);
        Item item3 = new Item(4,"Chocolate", 55,110);
        Item item4 = new Item(5,"Water", 50,20);
        Inventory inventory = new Inventory();
        inventory.add(item);
        inventory.add(item1);
        inventory.add(item2);
        inventory.add(item3);
        inventory.add(item4);
        System.out.println("Items available in store");
        System.out.println(inventory.getAll());
        System.out.println("Please enter the product id");
        int id= sc.nextInt();
        System.out.println("Enter quantity");
        int quantity= sc.nextInt();
        System.out.println();
        Process process=new Process(inventory);
        process.addInCart(id,quantity);
        Cart cart = new Cart();
        System.out.println("-----------Cart----------");
        System.out.println(cart.getItem());
        System.out.println("Items available in store");
        System.out.println(inventory.getAll());
    }

}
