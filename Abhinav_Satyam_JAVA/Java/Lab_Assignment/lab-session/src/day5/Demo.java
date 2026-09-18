package day5;

public class Demo {


    Demo(){
        System.out.println("No args");
    }

    Demo(String hello){
        System.out.println("Contructor: "+ hello);
    }

    {
        System.out.println("Genric block");
    }

    static {

        System.out.println("Static block");
    }

    public static void main(String[] args) {
        Demo demo = new Demo("S");
        System.out.println("--------------------------");
        Demo demo1 = new Demo();
    }

}
