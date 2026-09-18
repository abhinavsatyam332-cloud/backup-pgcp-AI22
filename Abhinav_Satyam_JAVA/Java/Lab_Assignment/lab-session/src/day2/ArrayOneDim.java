package day2;

import java.util.Scanner;

public class ArrayOneDim {
    public static void main(String[] args) {
        int arr[] = new int[5];
        Scanner sc = new Scanner(System.in);
        for (int i=0;i<arr.length;i++){
//            arr[i] = i*2;
            arr[i] = sc.nextInt();
        }
        for (int i=0;i<arr.length;i++) {
            System.out.println("arr["+i+"] => "+ arr[i]);
        }

    }
}
