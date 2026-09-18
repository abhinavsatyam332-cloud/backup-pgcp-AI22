package SL2.Task4.Classes;

public class User {
    public static void main(String[] args) {
        ClassRoom c=new ClassRoom();
        c.addStudent(1,8,5);
        c.addStudent(10,7.4f,5);
        c.addStudent(11,6.5f,5);
        c.addStudent(12,5.5f,5);
        c.addStudent(13,4.5f,5);
        c.addStudent(14,8,5);
        c.addStudent(15,6,5);
        c.addStudent(3,12,5);
        c.addStudent(4,0,5);

        System.out.println(c.list());

        System.out.println("Rankwise student list: ");
        c.showStats();
    }
}
