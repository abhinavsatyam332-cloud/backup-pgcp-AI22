package day7;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class TestStudent {
    public static void main(String[] args) {
        List<Student> lst = new ArrayList<Student>();

        lst.add(new Student("abhinav",23,20));
        lst.add(new Student("ram",2,12));
        lst.add(new Student("rakesh",10,3));
        System.out.println(lst);
//        Collections.sort(lst);

//        Collections.sort(lst,new StudentComparator());

        Collections.sort(lst, new Comparator<Student>() {
            @Override
            public int compare(Student o1, Student o2) {
                return o1.rollNo - o2.rollNo;
            }
        });

        Collections.sort(lst, (Student o1, Student o2) ->{
            return o1.rollNo - o2.rollNo;
        });

        Collections.sort(lst, (Student o1, Student o2)  -> o1.rollNo - o2.rollNo);


        System.out.println(lst);

    }
}
