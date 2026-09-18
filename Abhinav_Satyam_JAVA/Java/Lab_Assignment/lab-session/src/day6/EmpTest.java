package day6;

import java.util.HashMap;
import java.util.Map;

public class EmpTest {
    public static void main(String[] args) {
//        Map<Integer, Employee> mp = new HashMap<>();
//        mp.put(1,new Employee(1,"ram"));
//        mp.put(3,new Employee(3,"abhinav"));
//        mp.put(2,new Employee(2,"satyam"));
//
//        for(int i=0;i<mp.size();i++){
//
//            System.out.println(mp.get(i).getName());
//        }

//        EmpOperation op = new EmpOperation();
//        Employee e = new Employee(1,"ram");
//        op.addEmployee(e);
//        op.addEmployee(e);
//        op.addEmployee(new Employee(2,"nam"));
//        op.addEmployee(new Employee(3,"kam"));
//        op.addEmployee(new Employee(4,"kam"));
//        op.addEmployee(new Employee(4,"kam"));
//        op.printAll();
//        System.out.println("After deletion");
////        op.removeEmployee(e);
////        op.removeEmployee(2);
//
//        op.printAll();


        EmpOperation op = new EmpOperation();
        Employee e = new Employee("ram");
        op.addEmployee(e);
        op.addEmployee(e);
        op.addEmployee(new Employee("nam"));
        op.addEmployee(new Employee("kam"));
        op.addEmployee(new Employee("kam"));
        op.addEmployee(new Employee("kam"));
        op.printAll();
        System.out.println("After deletion");
    }
}
