package day1.other;


import day1.OnGoingPracticals.Parent;

public class NewClass extends Parent {
    Parent p = new Parent();
    public void doSomething(){
        System.out.println(p.publicInt);
//        System.out.println(p.protectedInt);
    }
}
