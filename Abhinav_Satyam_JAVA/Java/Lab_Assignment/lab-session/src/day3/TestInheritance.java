package day3;

public class TestInheritance {
    public static void main(String[] args) {
        Vehicle v1 = new Car(1,"Hector");

        Vehicle v2 = new Car(2,"Hector");

//        Car c = new Car()
        Car.doNothing();
        Vehicle.doNothing();

        v1.honk();
//        v1.engine(); cant be called

        Car c1 = (Car) v1;
        c1.engine();
    }
}
