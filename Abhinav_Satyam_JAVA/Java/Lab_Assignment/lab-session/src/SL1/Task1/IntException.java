package SL1.Task1;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class IntException {
    public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);
        Set<Integer> set = new HashSet<>();
        System.out.println("Enter 5 values");
        int i=0,a=0;

        while(i<5){
            try {
                a=sc.nextInt();
                if (set.contains(a)) {
                    throw new DuplicateValue("Value already exists! Please enter a different number.");
                }

                set.add(a);
                i++;
            }catch (DuplicateValue e){
                System.out.println(e.getMessage());
            }
        }
    }
}
