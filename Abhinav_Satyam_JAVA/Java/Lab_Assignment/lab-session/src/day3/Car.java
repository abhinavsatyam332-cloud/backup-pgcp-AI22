package day3;

public class Car extends Vehicle{
    public Car(int speed,String nm){
        super( speed,nm);
    }

    public Car(int speed){
//        super(speed,  "default car");
        this(speed,  "default car");

    }
    public void honk(){
        System.out.println("pom pom");
    }
    public void engine(){
        System.out.println("Starting engine");
    }
}
