package classAssignment2;

public class Manager extends Employee{
    private String project;
    Manager(int id, String name, String department, String project) {
        super(id, name, department);
        this.project=project;

    }
    @Override
    public String toString() {
        return "Employee id: "+getId()
                +"\nName: "+getName()
                +"\nDepartment: "+getDepartment()
                +"\nProject: "+project;
    }
}
