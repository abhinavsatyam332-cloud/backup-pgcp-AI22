package SL1.Task2.Exception;

public class InvalidQuantity extends RuntimeException {
    public InvalidQuantity(String message) {
        super(message);
    }
}
