package Assignment3.Task5;
public class ValidQuantity {
    static void validateQuantity(int qty)throws InvalidQuantityException {

                if(qty<=0 || qty>100){
            throw new InvalidQuantityException("qty <= 0 or qty > 100");
        }
        else {
            System.out.println("Required Quantity->"+qty);
        }
    }
}
