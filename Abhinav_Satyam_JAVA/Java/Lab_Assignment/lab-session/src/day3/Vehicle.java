package day3;

public class Vehicle {
    private int id;
    final protected int noOfTyres = 4;
    protected int speed;
    protected String name;

    public Vehicle( int speed,String name){

        this.speed = speed;
        this.name = name;
    }
    final void doFinal(){ }

    public void honk(){
        System.out.println("Honkkkkkk....");
    }

    public static final void doNothing(){
        System.out.println("Kuch nahi bye.");
    }
}
