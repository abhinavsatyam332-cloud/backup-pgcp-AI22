package day2;

import java.util.Scanner;

public class StudentArray {

    Student [] students = new Student[2];
    Scanner sc = new Scanner(System.in);
    public void populate(){
        System.out.println("Enter student roll number and name ");

        for(int i=0;i<students.length;i++){
            students[i] = new Student(sc.nextInt(), sc.next());
        }
    }

    public void display(){
        for (Student student: students) {
            System.out.println(student);
        }
    }

}
