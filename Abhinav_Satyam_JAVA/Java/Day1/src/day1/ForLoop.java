package day1;

public class ForLoop {
    public static void main(String[] args){

        for(int i=0;i<10;i++){
            System.out.println(i);
        }

        int i=1;
        while (i<10){
            System.out.println(" In while "+i);
            i+=1;
        }

        i=0;
        do{
            System.out.println(" In do while "+i);

        }while (i<0);


    }
}
