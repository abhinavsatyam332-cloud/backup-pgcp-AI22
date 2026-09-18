package day7;
@FunctionalInterface
interface calculate{
    int operate(int a,int b);
}

public class Lamba {
    public static void main(String[] args) {

        String s = "fd";

//        System.out::println("as");
//        Consumer<String> printAction=(s)->System.out.println("s");
//        printAction.accept(s);
        int a=6;
        int b=9;

        calculate add= (x,y) -> x+y;

        System.out.println(add.operate(a,b));
    }
}
