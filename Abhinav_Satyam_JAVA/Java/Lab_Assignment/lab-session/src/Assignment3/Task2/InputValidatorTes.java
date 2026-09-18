package Assignment3.Task2;

public class InputValidatorTes {

    public static void main(String[] args) {
        InputValidator validator= new InputValidator();
        String [] arr= {"s","a","0", "5" };
        validator.processEntry(arr,3);
        validator.processEntry(arr,1);
        validator.processEntry(arr,2);
        validator.processEntry(arr,0);
    }

}
