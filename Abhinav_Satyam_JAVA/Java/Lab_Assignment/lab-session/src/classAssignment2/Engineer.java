package classAssignment2;

public class Engineer extends Employee{
    private int incentive;

    Engineer(int id, String name, String department, int incentive) {
        super(id, name, department);
        this.incentive=incentive;
    }

    @Override
    public String toString() {
        return "Employee id: "+getId()
                +"\nName: "+getName()
                +"\nDepartment: "+getDepartment()
                +"\nIncentive: "+incentive;
    }
}
