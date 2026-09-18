package classAssignment;

import java.util.ArrayList;
import java.util.List;

public class TestingEmployees {
    public static void main(String[] args) {
        Engineer engineer = new Engineer("ramesh","IT",1000);
        Manager manager = new Manager("satyam","IT","demo");


        List<Employee> lst = new ArrayList<>();
        lst.add(engineer);
        lst.add(manager);

        for(Employee e:lst){
            if(e instanceof Manager){
                Employee ee = (Manager) e;
                System.out.println(ee);
            }


            if(e instanceof Engineer){
                Engineer ee = (Engineer) e;
                System.out.println(ee);
            }
        }
    }
}
