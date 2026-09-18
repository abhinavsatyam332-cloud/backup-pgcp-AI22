package Assignment3.Task3;

public class ResourceTest {
    public static void main(String[] args) {
        // Case 1--> pass riskyValue(5)

        try {
            RunTask.runTask(5);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        // case 2 -> fail

        try {
            RunTask.runTask(-5);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }



    }
}
