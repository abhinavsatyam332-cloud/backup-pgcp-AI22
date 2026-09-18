package Assignment3.Task3;

public class SimulatedResource   {

    public void open(){
        System.out.println("Open");
    }
    public void process(int riskyValue) throws RuntimeException{

            if(riskyValue<0){
                throw new RuntimeException("Processing failed");
            }
        System.out.println("-> Resource: Processed value " + riskyValue + " successfully.");

        }

    public void close(){
        System.out.println("Close");
        System.out.println("----------------------------------");
    }



}
