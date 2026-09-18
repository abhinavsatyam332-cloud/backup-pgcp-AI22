package Assignment3.Task4;

/*
Goal: create your first custom exception and use throw with it inside validation logic.
    1. Create a class InvalidQuantityException that extends RuntimeException, with a constructor that accepts a String message and passes it to super(message).
    2. Write a method void validateQuantity(int qty) that throws a new InvalidQuantityException (using throw) with a descriptive message whenever qty <= 0 or qty > 100.
    3. In an OrderValidatorTest class, call validateQuantity() with at least 4 values: one that's negative,
    one that's zero, one that's above 100, and one that's valid — wrap each call in its own try-catch for InvalidQuantityException and print the outcome.
#/
 */

public class InvalidQuantityException extends RuntimeException{
    InvalidQuantityException(String message){
        super(message);
    }


}
