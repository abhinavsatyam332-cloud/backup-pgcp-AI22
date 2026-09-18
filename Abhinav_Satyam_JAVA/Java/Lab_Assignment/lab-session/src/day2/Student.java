package day2;

public class Student {
    private String sname;
    private int rno;

    public Student(int rno,String sname){
        this.sname = sname;
        this.rno = rno;
    }

    public String getSname(){
        return this.sname;
    }
    public int getRno(){
        return this.rno;
    }

    @Override
    public String toString() {
        return sname+", "+rno;
    }
}
