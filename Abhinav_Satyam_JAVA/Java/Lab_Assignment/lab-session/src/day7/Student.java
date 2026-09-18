package day7;

public class Student  implements Comparable<Student>{
    String name;
    int height;
    int rollNo;
    Student(String name, int height, int rollNo){
        this.name = name;
        this.height = height;
        this.rollNo = rollNo;
    }


    @Override
    public int compareTo(Student o) {
        return this.height - o.height;
    }

    @Override
    public String toString() {
        return "{" +
                "name='" + name + '\'' +
                ", height=" + height +
                ", rollNo=" + rollNo +
                '}';
    }
}
