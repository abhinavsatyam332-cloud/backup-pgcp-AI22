package classAssignment;

public class Manager extends Employee {
    String project;

    Manager(String name,String department,String project){
        super( name, department);
        this.project = project;
    }
    public void setProject(String project) {
        this.project = project;
    }

    public String getProject() {
        return project;
    }

    @Override
    public String toString() {
        return "Name: "+getName()+" Department: "+getDepartment()+" Project: "+project;

    }
}
