package ClassAssignment3.Classes;

import ClassAssignment3.Exceptions.BookNotFound;
import ClassAssignment3.Exceptions.DuplicateBookException;

import java.time.LocalDate;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Library {

    Map<String, Book> lib;
    Library(){
        lib = new HashMap<String, Book>();
    }

    void addBook(Book book) throws DuplicateBookException {
        String isbn = book.getIsbn();
        if(lib.keySet().contains(isbn)){
            throw new DuplicateBookException(book.getName()+" already in library");
        }else {
            lib.put(isbn,book);
            System.out.println(book.getName()+" added");
        }
    }
    void showBook(){
        System.out.println(lib);
    }
    void returnBook(String isbn) {
        if(lib.keySet().contains(isbn)){
            if (lib.get(isbn).getDate() == null){
                throw new BookNotFound("Book with id: "+isbn+" Already returned");
            }
            lib.get(isbn).setDate(null);
            System.out.println(lib.get(isbn).getName()+": Book returned ");
        }else {
            throw new BookNotFound("Book with id: "+isbn+"not found");
        }
    }

    void getOverdueBooks(LocalDate date){
        Map<String,Book> mp = new HashMap<>();

        for(String id:lib.keySet()){
            Book book  = lib.get(id);
            LocalDate overdue = book.getDate();
            if(overdue==null){
                continue;
            }

            if(date.isEqual(overdue)){
                continue;
            }else if(date.isAfter(overdue)){
                mp.put( book.getIsbn(),book );
            }
        }

        System.out.println("\n\n");

        mp.values().stream()
                .sorted()
                .forEach(System.out::println);
    }

}
