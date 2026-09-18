package Assignment3.Task4;

public class ValidQuantity {
    static void validateQuantity(int qty)throws InvalidQuantityException{
        if(qty<=0 || qty>100){
            System.out.println("Invalid Quantity->"+qty);
        }
        else {
            System.out.println("Quantity Available->"+qty);
        }
    }
}
