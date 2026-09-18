package day1.OnGoingPracticals;

public class TestConstructor {

    int i=10;

    TestConstructor(){
        System.out.println("Base");
    }
//    Constructor overloading
    TestConstructor(int i){
        System.out.println("Param Constructor = " + i);
        this.i = i;
    }

    public static void main(String[] args) {
        TestConstructor tc = new TestConstructor();
        TestConstructor tc1 = new TestConstructor(5);
        System.out.println(tc1.i);
        System.out.println(tc.i);
    }
}
