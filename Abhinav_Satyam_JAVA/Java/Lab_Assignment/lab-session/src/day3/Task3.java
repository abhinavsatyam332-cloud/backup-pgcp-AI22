package day3;
/**
 * Goal: practice String immutability, common String methods, and StringBuilder for efficient building.
 * Write a class TextUtils in com.lab.core with the following static methods:
 *     • String reverse(String input) — reverse a string using StringBuilder (not manual char-swapping).
 *     • boolean isPalindrome(String input) — case-insensitive, ignoring spaces (use toLowerCase(), replace(), and your reverse() method).
 *     • String initials(String fullName) — turn "John Ronald Tolkien" into "JRT" using split() and a StringBuilder loop.
 *     • String maskEmail(String email) — turn "john.doe@email.com" into "jo******@email.com", keeping the domain and the first 2 characters of the local part.
 * In a TextUtilsTest class, call every method with at least 2 different inputs each (including one edge case, like an empty string or a single-word name) and print the results.
 **/
public class Task3 {

    String reverse(String input){
        StringBuilder sb = new StringBuilder(input);
        sb.reverse();
        return  sb.toString();
    }
    boolean isPalindrome(String input){
        String rev = reverse(input);
        return  rev.equals(input);
    }

    String initials(String fullName){
        String arr[] = fullName.split(" ");
        StringBuilder sb = new StringBuilder();

        for(String str:arr){
           sb.append(Character.toUpperCase(str.charAt(0)));
        }
        return sb.toString();
    }

    String maskEmail(String email){
            if(email.length() <8){
                return "Invalid email";
            }

            StringBuilder sb = new StringBuilder(email);
            for (int i=2;i<email.length();i++){
                if(sb.charAt(i) == '@'){
                    break;
                }
                sb.setCharAt(i,'*');
            }
            return  sb.toString();
    }
    public static void main(String[] args) {
        Task3 task3 = new Task3();

        String str = "ramesh is good boy";

        System.out.println("Reverse of string is: "+task3.reverse(str));
        System.out.println("Is palindrome: "+task3.isPalindrome(str));
        System.out.println("Initials: "+task3.initials("John Ronald Tolkien"));
        System.out.println("Masked mail: "+task3.maskEmail("john.doe@email.com"));
    }
}
