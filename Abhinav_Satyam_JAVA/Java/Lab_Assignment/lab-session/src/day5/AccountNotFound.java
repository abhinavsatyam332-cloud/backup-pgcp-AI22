package day5;

public class AccountNotFound extends  RuntimeException{
    AccountNotFound(String msg){
        super(msg);
    }
}
