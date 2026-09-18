package day6;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class EmpOperation2 {
    Set<Employee> set = new HashSet<>();

    public void addEmployee(Employee e){

        set.add(e);

    }

    public void removeEmployee(Object e){
        Employee obj = (Employee) e;
        if(set.contains(e)){
            set.remove(e);
            System.out.println("Employee " +obj.getName()+" deleted");
        }
        System.out.println("Emp not found");

    }

    void printAll(){
        for(Employee e:set) {

            System.out.println("Id: "+e.getId()+ " Name: "+e.getName()+"\n");
        }
    }



}
