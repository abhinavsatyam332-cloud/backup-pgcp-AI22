package Assignment3.Task5;

public class CheckStock {

    static void checkStock(String item, int available) throws OutOfStockException{

        if(available<=0){
            throw new OutOfStockException(item+"Not available");
        }
        System.out.println("Available stock of "+item+"-->"+available);
    }
}
