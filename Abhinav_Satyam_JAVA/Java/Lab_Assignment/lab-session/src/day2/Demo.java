package day2;

import java.util.Arrays;

public class Demo {
    public static void main(String[] args) {
        int arr[] = {12,23,3};
//        int[] arrcpy ;
        int[] arrcpy = Arrays.copyOf(arr,8);
        System.out.println(Arrays.toString(arrcpy));
        Arrays.sort(arrcpy);
        System.out.println(Arrays.binarySearch(arrcpy,12));
    }
}
