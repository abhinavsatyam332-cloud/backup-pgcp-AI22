package SL2.Task4.Classes;

import SL2.Task4.Exceptions.DuplicateEnrollmentException;
import SL2.Task4.Exceptions.InvalidGpaException;

import java.util.*;

public class ClassRoom {

    Map<Integer,Student> map = new HashMap<>();
    Student s= null;

    //add student
    public void addStudent(int id,float gpa, int grade) {
       s = new Student(id, gpa, grade);
       try {
           if(!map.containsKey(id)){
               if(s.getGpa()>0.0 && s.getGpa()<10.0) {
                   map.put(id, s);
               }
               else{
                   throw new InvalidGpaException("GPA must be between 0-10");
               }
           }
           else {
               throw new DuplicateEnrollmentException("ID already exists!!!!!!!!");
           }
       }catch (DuplicateEnrollmentException e){
           System.out.println(e.getMessage());
       }catch (InvalidGpaException e){
           System.out.println(e.getMessage());

       }
    }

    //Student list

    public Collection<Student> list(){
        return map.values();
    }

    public void showStats() {
        Collection<Student> lst = map.values();

        lst.stream().sorted(
                (o1, o2) ->
                        (int)Float.compare(o2.getGpa() , o1.getGpa()))
                .forEach(System.out::println);
    }


    //Student rank





}
