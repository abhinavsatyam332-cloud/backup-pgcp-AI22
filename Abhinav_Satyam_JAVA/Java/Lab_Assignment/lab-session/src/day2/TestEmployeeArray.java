package day2;

public class TestEmployeeArray {
    public static void main(String[] args) {
        EmployeeArray emparr = new EmployeeArray();
        emparr.populateEmp();

        emparr.displayEmployee();
        emparr.sort();
        emparr.displayEmployee();
    }
}
