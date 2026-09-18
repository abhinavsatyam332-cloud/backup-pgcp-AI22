package day1.OnGoingPracticals;

public class TestScope {

    static int i_global=20;
    int i_ns_global=100;

    public void doSomething(){
        System.out.println(i_ns_global);
        System.out.println(i_global);
    }
    public static void main(String[] args){
        int i_main = 10;

        System.out.println(i_global);
        System.out.println(i_main);
//        System.out.println(i_ns_global);           //  from static method we can access non static members like this.

        TestScope testScope = new TestScope();
        System.out.println(testScope.i_ns_global);

        testScope.doSomething();
    }
}
