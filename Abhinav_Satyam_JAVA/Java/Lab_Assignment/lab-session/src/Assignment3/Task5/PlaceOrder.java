package Assignment3.Task5;
public class PlaceOrder {
    static void placeOrder(String item, int qty, int stockAvailable) throws OutOfStockException{
        try {
            if(qty>stockAvailable){
                throw new InvalidQuantityException("");
            }
            ValidQuantity.validateQuantity(qty);
            CheckStock.checkStock(item,stockAvailable);
        } catch (InvalidQuantityException e) {
            System.out.println("Invalid Quantity: "+e.getMessage());
        } catch (OutOfStockException e) {
            System.out.println("Stock unavailable: "+e.getMessage());
        }finally {
            System.out.println("Order attempted for: "+item);
            System.out.println("------------------------------------------------");
        }

    }
}
