package classAssignment2;

public class Employee implements Comparable<Employee>{
    private int id;
    private String name;
    private String department;

    Employee(int id, String name,String department ){
        this.department=department;
        this.id=id;
        this.name=name;
    }

    public String getDepartment() {
        return department;
    }

    public String getName() {
        return name;
    }

    public int getId() {
        return id;
    }

    @Override
    public String toString() {
        return super.toString();
    }

    @Override
    public int compareTo(Employee o) {
        return this.id-o.id;
    }



}
