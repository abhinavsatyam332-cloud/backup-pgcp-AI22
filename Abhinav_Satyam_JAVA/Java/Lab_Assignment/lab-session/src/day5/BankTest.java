package day5;

import java.time.LocalTime;
import java.util.Date;

public class BankTest {
    public static void main(String[] args) {

        long i = System.currentTimeMillis();
        System.out.println(i);
        BankOperation bop = new BankOperation();

        bop.accountCreate("Savings",1000,"ram",10.0,0);
        bop.accountCreate("Current",2000,"sham",10.0,200);
        bop.accountCreate("Current",2000,"anita",10.0,200);

        try {
            bop.deposit(102,100);
            bop.withdraw(103, 20);
            bop.withdraw(101, 90);
            bop.printAllAccounts();

            Thread.sleep(100);

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        System.out.println("Execution time: "+(System.currentTimeMillis()- i)+" mili sec");
    }
    }
