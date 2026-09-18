package day6;

public class EnumDemo {
    enum status{
        YES(1),NO(2);
        int level;
        status(int i){
            this.level= i;
        }
        status(String m){

        }
        int getLevel(){
            return  this.level;
        }
    }

    EnumDemo(int a){}
    public static void main(String[] args) {
        System.out.println(status.YES.getClass());
        System.out.println(Integer.MAX_VALUE);
        System.out.println(Integer.MIN_VALUE) ;
        System.currentTimeMillis();
    }
}
