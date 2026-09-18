package day3;


import java.util.Arrays;

public class TestPassingData {
    static void tryToChange(Integer ii){
        ii = new Integer(99);
    }

    static void addItem(){

    }
    static void updateItem(Employee e){
        e.setName("Ramesh");
    }
    static void updateArray(String[] strings){
        strings[0] = "Aa";
        strings[1] = "Na Na";
    }

    public static void main(String[] args) {

        int a = 10;
        Integer ii = new Integer(a);
        tryToChange(ii);
        System.out.println(ii);

        Employee e = new Employee(1,"akash");
        updateItem(e);
        System.out.println(e.getName());

        String[] strings = {"ramesh","anita","kamal"};
        updateArray(strings);
        System.out.println(Arrays.toString(strings));
    }
}
