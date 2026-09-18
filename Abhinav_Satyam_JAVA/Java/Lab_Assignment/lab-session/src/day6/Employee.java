package day6;

import java.util.Objects;

public class Employee   {

    private int id;
    private String name;
    public Employee(String name){
        this.name = name;
    }
    public Employee(int id, String name){

        this.id=id;
        this.name=name;

    }

    public int getId(){
        return id;
    }
    public String getName(){
        return name;
    }

    @Override
    public boolean equals(Object o) {

        if(! (o instanceof Employee)){
            return false;
        }

        Employee ee = (Employee) o;
        if(this == (Employee) o){
            return true;
        }

        if(this.id == ee.getId() ){
            return true;
        }
        return false;
    }

    @Override
    public int hashCode() {
        System.out.println("Hash code");
        return this.getName().hashCode();
    }
}
