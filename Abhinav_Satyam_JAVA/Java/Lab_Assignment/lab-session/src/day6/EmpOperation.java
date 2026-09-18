package day6;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class EmpOperation {
    Map<Integer, Employee> mp = new HashMap<>();
    Set<Employee> set = new HashSet<>();

    public void addEmployee(Employee e){

        mp.put(e.getId(),e);

    }

    public void removeEmployee(Object e){

        if(e instanceof Integer){
            Integer ee = (Integer) e;

            for(Integer i:mp.keySet()) {
                if(i==ee){
                    mp.remove(i);
                    System.out.println("Employee deleted");
                    return;
                }
            }
        }else {
            Employee ee = (Employee) e;
            for(Integer i:mp.keySet()){
                if(ee.getId() == mp.get(i).getId() ){
                    mp.remove(i);
                    System.out.println("Employee deleted with id "+i);
                    return;
                }
            }

        }
        System.out.println("Emp not found");

    }

    void printAll(){
        for(Integer i:mp.keySet()) {
            Employee e = mp.get(i);
            System.out.println("Id: "+e.getId()+ " Name: "+e.getName()+"\n");
        }
    }



}
