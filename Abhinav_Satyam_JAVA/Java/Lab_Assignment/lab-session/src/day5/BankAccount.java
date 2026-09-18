package day5;

public class BankAccount {
    private int Account;
    private int balance;
    private String holderName;

    BankAccount(){
    this(1,500,"Unknown Name");

    }

    BankAccount(int Account, int balance, String holderName){

        this.Account=Account;
        this.balance=balance;
        this.holderName=holderName;
    }

    public int getAccount() {
        return Account;
    }

    public int getBalance() {
        return balance;
    }

    public void setBalance(int balance) {
        this.balance = balance;
    }

    public void withdraw(int amt){
        balance -=amt;
        System.out.println(amt + " withdraw for "+holderName);
    };
    public void deposit(int amt){ balance = balance+amt; };

    public String getHolderName() {
        return holderName;
    }

    @Override
    public String toString() {
        return "BankAccount{" +
                "Account=" + Account +
                ", balance=" + balance +
                ", holderName='" + holderName + '\'' +
                '}';
    }
}
