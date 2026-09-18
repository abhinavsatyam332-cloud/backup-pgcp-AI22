package ClassAssignment3.Classes;

import java.util.Comparator;

public class BookComparator implements Comparator {

    @Override
    public int compare(Object o1, Object o2) {
        Book b1 = (Book) o1;
        Book b2 = (Book) o2;

        if(b1.getDate().isAfter(b2.getDate())){
            return 1;
        }else if(b1.getDate().isEqual(b2.getDate())){
            return b1.getDate().compareTo(b2.getDate());
        }
        return -1;
    }
}
