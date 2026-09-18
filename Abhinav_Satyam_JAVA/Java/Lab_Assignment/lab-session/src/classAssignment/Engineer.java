package classAssignment;

public class Engineer extends Employee{
    int incentive;
    Engineer(String name,String department,int incentive){
        super( name, department);
        this.incentive = incentive;
    }

    public void setIncentive(int incentive) {
        this.incentive = incentive;
    }

    public int getIncentive() {
        return incentive;
    }

    @Override
    public String toString() {
        return "Name: "+getName()+" Department: "+getDepartment()+" Incentive: "+incentive;

    }
}
