package day5;

public class TestSingleTon {
    public static void main(String[] args) {

        SingleTon s1 = SingleTon.getInstance();
        SingleTon s2 = SingleTon.getInstance();
        s1.setName("ram");
        s2.setName("kam");
s1.getCount();
s2.getCount();
        System.out.println(s1.getName());
        System.out.println(s2.getName());
    }
}
