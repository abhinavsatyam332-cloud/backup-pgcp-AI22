package day5;

public class CurrentAccount extends BankAccount{
    private int overdraft;

    CurrentAccount(){}
    CurrentAccount(int Account , int Balance , String holderName, int overdraft){
        super( Account , Balance , holderName);
        this.overdraft = overdraft;
    }

    public int getOverdraft() {
        return overdraft;
    }

    public void withdraw(int amt){

            if(getBalance() - amt <= overdraft){
            System.out.println("Cant withdraw balance insufficient");
        }
        this.setBalance( getBalance() - amt );
        System.out.println(amt+" withdraw for "+getHolderName());
    }
}
