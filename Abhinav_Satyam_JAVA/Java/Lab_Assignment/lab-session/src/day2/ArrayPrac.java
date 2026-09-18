package day2;

import java.util.Arrays;

public class ArrayPrac {
    int add(int a,int b){
        return  a+b;
    }
    public static void main(String[] args){
        int [] arr = new int[5];

    for(int i=0;i<5;i++){

        arr[i]=i;

        }

    for(int i=0;i<5;i++){
        System.out.println(arr[i]);
    }

    int op=0;
    op = Arrays.stream(arr).reduce(0,(a,b)->a+b);
    System.out.println("add "+op);
    }
}
