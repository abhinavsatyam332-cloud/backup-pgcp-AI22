package ClassAssignment3.Classes;

import java.time.LocalDate;

public class Test {
    public static void main(String[] args) {
        Library library = new Library();


        try {

            Book b1 = new Book("1","Wings of fire", LocalDate.of(2026,05,3));
            Book b2 = new Book("2","java", LocalDate.of(2026,8,5));
            Book b3 = new Book("3","python", LocalDate.of(2026,8,5));
            Book b4 = new Book("4","ai", LocalDate.of(2026,8,5));
            Book b5 = new Book("5","dsa", LocalDate.of(2026,8,5));
            Book b6 = new Book("6","dsa", LocalDate.of(2026,10,5));
            Book b7 = new Book("7","dsa", LocalDate.of(2026,10,5));

            library.addBook(b1);
            library.addBook(b2);
            library.addBook(b3);
            library.addBook(b4);
            library.addBook(b5);
            library.addBook(b6);
            library.addBook(b7);

            library.returnBook("5");

            library.getOverdueBooks(LocalDate.of(2026,9,10));
        }catch (Exception e){
            System.out.println(e.getMessage());
        }


    }
}
