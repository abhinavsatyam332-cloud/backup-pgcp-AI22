package classAssignment;


public class Employee   {

    private String name;
    private String department;
    public Employee (String name,String department){
        this.department=department;
        this.name=name;

    }

    public String getName() {
        return name;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Name: "+this.name+" Department: "+this.department;
    }
}
