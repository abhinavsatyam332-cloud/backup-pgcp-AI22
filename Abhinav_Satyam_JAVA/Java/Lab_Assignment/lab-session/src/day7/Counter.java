package day7;

public class Counter implements Runnable{
    private int count = 0;

      void increment(){
        count++;
    }

      int getCount() {
        return count;
    }

    @Override
    public void run() {
        increment();
        System.out.println(getCount());
    }
}
