package day3;


public class Employee   {

    private int id;
    private String name;

    public Employee (int id, String name){

        this.id=id;
        this.name=name;

    }

    public int getId(){
        return id;
    }
    public String getName(){
        return name;
    }

    public void setName(String nm){
        this.name = nm;
    }

    @Override
    public String toString(){
        return  "Id: "+id+ ", Name: " +name;
    }


}
