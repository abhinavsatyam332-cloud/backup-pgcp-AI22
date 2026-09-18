package Assignment3.Task2;

public class InputValidator {

    public void processEntry(String[] data, int index){

        int i=index;
        try {
            System.out.println(data[i]);
            int a= Integer.parseInt(data[i]);
            a=100/a;
            } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("ArrayIndexOutOfBoundsException");
            } catch (NumberFormatException e) {
            System.out.println(e.getMessage());
            }
            catch (ArithmeticException e){
                System.out.println(e.getMessage());
            } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }


}
