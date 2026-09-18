package classAssignment2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Test {
    public static void main(String[] args) {
        Engineer e= new Engineer(15,"Demo","Tech",50);
        Manager e1= new Manager(2,"Manager","Tech","Demo");
        List<Employee> list = new ArrayList<>();
        list.add(e);
        list.add(e1);
        for(Employee emp:list) {
            System.out.println(emp);
            System.out.println("--------------------------------------");
        }
        Collections.sort(list);
        for(Employee emp:list){
            System.out.println(emp);
            System.out.println("--------------------------------------");
        }



    }


}
