package day7;

public class test {
    public static void main(String[] args) {
//        Counter counter = new Counter();

        Runnable counter1 = new Counter();
        Runnable counter2 = new Counter();

        Thread t1=new Thread(counter1);
        Thread t2 = new Thread(counter1);

        try{
            t1.start();
//            Thread.sleep(100);
            t2.start();

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }


//        Counter cc = (Counter) counter;
//
//        System.out.println(cc.getCount());

    }
}
