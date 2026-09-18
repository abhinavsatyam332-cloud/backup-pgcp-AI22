package day5;

public class SingleTon {
    private static SingleTon singleTon=null;
    private static int count = 0;
    private String name ;

    private SingleTon(){  }

    public static SingleTon getInstance(){
        if(singleTon==null){
            singleTon = new SingleTon();

        }
        count=count+1;
        if(count>1){
            System.out.println("Jo object create kiya hai wohi use kr");
        }
        System.out.println("Ye le object");
        return singleTon;
    }
    void getCount(){
        System.out.println(count);
    }
    void setName(String nm){
        this.name = nm;
    }

    String getName(){
        return  this.name;
    }

}
