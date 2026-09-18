package ClassAssignment3.Classes;

import java.time.LocalDate;

public class Book implements Comparable {

    private String isbn;
    private String name;
    private LocalDate date;

    Book(String isbn, String name, LocalDate date){
        this.date=date;
        this.isbn=isbn;
        this.name=name;
    }

    public String getName() {
        return name;
    }

    public LocalDate getDate() {
        return date;
    }

    public String getIsbn() {
        return isbn;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    @Override
    public int compareTo(Object o) {
        Book book = (Book) o;
        if(this.date.isAfter(book.getDate())){
            return 1;
        }else if(this.date.isEqual(book.getDate())){
            return this.isbn.compareTo(book.isbn);
        }
        return -1;
    }

    @Override
    public String toString() {
        return "Book{" +
                "isbn='" + isbn + '\'' +
                ", name='" + name + '\'' +
                ", date=" + date +
                '}';
    }
}
