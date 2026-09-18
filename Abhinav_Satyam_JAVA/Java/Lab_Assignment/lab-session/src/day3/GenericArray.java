package day3;

import day2.Employee;

import java.util.Objects;

public class GenericArray {

    public static void main(String[] args) {
        Object[] objects = new Object[2];
        Employee e1 = new Employee(1,"ram");
        Employee e2 = new Employee(1,"ram");
        objects[0] = e1;
        objects[1] = new String("akash");
    }
}
