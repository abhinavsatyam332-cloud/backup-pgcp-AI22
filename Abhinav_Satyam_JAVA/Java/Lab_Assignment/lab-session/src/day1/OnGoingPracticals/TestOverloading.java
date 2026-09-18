package day1.OnGoingPracticals;

public class TestOverloading {
    public void doSomething(double i ){
        System.out.println("double "+i);
    }
    public void doSomething(int i){
        System.out.println("int "+i);

    }

    public static void main(String[] args) {
        TestOverloading to = new TestOverloading();
        to.doSomething(126.4);
    }
}
