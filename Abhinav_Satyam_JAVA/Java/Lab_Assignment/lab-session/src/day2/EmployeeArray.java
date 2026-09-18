package day2;

import org.w3c.dom.ls.LSOutput;

import java.util.Arrays;
import java.util.Scanner;

public class EmployeeArray {


    private Employee [] emp = new Employee[2];

    private Scanner sc = new Scanner(System.in);

    void populateEmp(){
        for(int i=0;i<emp.length;i++){

            int id = sc.nextInt();
            String name = sc.next();

            Employee employee = new Employee(id,name);
            emp[i] = employee;
        }
    }

    void displayEmployee(){
        for(Employee e:emp){
//            System.out.println("Id : "+e.getId());
//            System.out.println("Name : "+e.getName()+"\n");
            System.out.println(e);
        }
    }

    void sort(){
        Arrays.sort(emp);
    }





}
