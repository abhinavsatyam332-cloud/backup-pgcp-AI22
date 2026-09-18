package SL2.Task4.Classes;

public class Student implements Comparable{
    private int id;
    private float Gpa;
    private int grade;

    Student(){}
    Student(int id, float Gpa,int grade){
        this.id=id;
        this.Gpa=Gpa;
        this.grade=grade;
    }

    public float getGpa() {
        return Gpa;
    }

    public int getid() {
        return id;
    }

    public int getGrade() {
        return grade;
    }

    public void setGpa(float gpa) {
        Gpa = gpa;
    }

    public void setGrade(int grade) {
        this.grade = grade;
    }

    public void setid(int id) {
        this.id = id;
    }

    @Override
    public String toString() {
        return "ID: "+id+", Class: "+grade+", Gpa: "+Gpa+"\n";
    }



    @Override
    public int compareTo(Object o) {
        Student ss = (Student) o;
        return (int)(this.getGpa()-ss.getGpa());
    }
}
