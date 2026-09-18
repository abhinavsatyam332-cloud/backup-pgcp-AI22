package day5;

public class SavingAccount extends BankAccount{
    private Double interest;

    SavingAccount(){}
    SavingAccount(int Account , int Balance , String holderName, Double interest){
        super(Account,Balance,holderName);
        this.interest = interest;
    }

    public void setInterest(Double interest) {
        this.interest = interest;
    }

    double getInterest(){
        return getBalance() * interest /100;
    }

    public void deposit(int amt){
        if(getBalance() < amt){
            System.out.println("Cant withdraw balance insufficient");
        }
      this.setBalance( getBalance() - amt );
        System.out.println(amt+" withdraw for "+getHolderName());
    }

}
