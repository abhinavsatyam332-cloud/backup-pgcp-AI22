package day5;

public class BankOperation {
    BankAccount bankAccounts[] = new BankAccount[5];
    static int accountNo;
    static int i ;
    static {
        accountNo =101;
        i=0;
    }
    public void accountCreate(String type, int balance,String holderName,Double interest ,int overdraft) {
        if(i+1 > 5){
            System.out.println("Max accounts created cant create new");
        }else{
            if(type.equals("Savings")){
                bankAccounts[i++] = new SavingAccount(accountNo++,balance,holderName,interest);
            }else if(type.equals("Current")){
                bankAccounts[i++] = new CurrentAccount(accountNo++,balance,holderName,overdraft);
            }
            System.out.println("Account for user: "+ holderName+" created successfully");
        }
    }

    public BankAccount getAccount(int accountNo){
        for(int i =0;i<5;i++){
            if(bankAccounts[i].getAccount() == accountNo){
                return bankAccounts[i];
            }
        }
        throw new AccountNotFound("Account not found for "+accountNo);
    }

    public void withdraw( int accountNo, int amount){
        try {
            BankAccount acc = getAccount(accountNo);
            acc.withdraw(amount);

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }public void deposit( int accountNo, int amount){
        try {
            BankAccount acc = getAccount(accountNo);
            acc.deposit(amount);

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public void printAllAccounts(){
        if(i==0){
            System.out.println("No accounts were found");
        }
        for(BankAccount acc:bankAccounts){
            if(acc==null){
                throw new AccountNotFound("lIST ENDED");
            }
            System.out.println(acc);
            if(acc instanceof SavingAccount){
                System.out.println("Total interest: "+((SavingAccount) acc).getInterest());
            }
            if(acc instanceof CurrentAccount){
                System.out.println("Overdraft limit: "+((CurrentAccount) acc).getOverdraft());
            }
            System.out.println();
        }
    }


}
