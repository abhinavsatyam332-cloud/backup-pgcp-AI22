package Assignment3.Task5;

public class OrderProcessorTest {
    public static void main(String[] args) {

        try {
//            PlaceOrder.placeOrder("Milk",9,2);
            PlaceOrder.placeOrder("Milk",9,10);
            PlaceOrder.placeOrder("Milk",1,0);
            PlaceOrder.placeOrder("Milk",5,100);

        } catch (OutOfStockException e) {
            throw new RuntimeException(e);
        }

    }
}
