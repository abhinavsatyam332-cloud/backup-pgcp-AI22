package day2;

public class Wrapper {
    public static void main(String[] args) {
            Integer i=5;
            Integer i1= new Integer(5);

//        System.out.println(i==i1);

        Integer i2 = Integer.valueOf("7");
        int i3 = Integer.parseInt("7");

        System.out.println("i = " +i);
        System.out.println("i1 = " +i1);
        System.out.println("i2 = " +i2);
        System.out.println("i3 = " +i3);


        System.out.println(i==i1);
        System.out.println(i.equals(i1));

        System.out.println(i2==i3);
        System.out.println(i2.equals(i3));

    }
}


