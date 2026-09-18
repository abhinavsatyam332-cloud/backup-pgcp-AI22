package day2;

public class TestString {
    public static void main(String[] args) {
        String s1 = "ram";
        String s2 = "ram";


        String s3 = new String("ram");
        String s4 = new String("ram");

//        System.out.println(s1==s2);
//        System.out.println(s1.equals(s2));
//
//        System.out.println(s3==s4);
//        System.out.println(s3.equals(s4));

        if(s1==s2){
            System.out.println("s1==s2 -> True" );
        }else{
            System.out.println("s1==s2 -> False" );
        }

        if(s3==s4){
            System.out.println("s3==s4 -> True" );
        }else{
            System.out.println("s3==s4 -> False" );
        }

        if(s3.equals(s4)){
            System.out.println("s3.equals(s4) -> True" );
        }else{
            System.out.println("s3.equals(s4) -> False" );
        }

        s3 = s1;
        if(s3==s1){
            System.out.println("s3==s1 -> True" );
        }else{
            System.out.println("s3==s1 -> False" );
        }

    }
}
