package day2;

public class TestStringBuilder {
    public static void main(String[] args) {
        String s1 = "Abhinav-satyam";

        StringBuilder sb = new StringBuilder(s1);
        sb.reverse();
        System.out.println(sb);
        sb.reverse();
        sb.delete(0,8);
        System.out.println(sb);

    }
}
