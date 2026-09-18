package day2;

public class Employee implements Comparable<Employee> {

    private int id;
    private String name;

    public Employee (int id, String name){

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
    public String toString(){
        return  "Id: "+id+ ", Name: " +name;
    }

    public int compareTo(Employee e){
//        return name.length() < e.getName().length();
            return  Integer.compare(this.name.length(), e.getName().length());
    }
}
