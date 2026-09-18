package day6;

import java.util.*;

public class ListDemo {
    public static void main(String[] args) {
        List<Employee> list = new ArrayList<>();
        for (int i = 0; i < 5; i++) {

            list.add(new Employee(i, "Default"));
        }


        Employee e1 = new Employee(2, "satyam");
        Employee e2 = new Employee(8, "ram");
        Employee ee[] = {e1, e2};
        List<Employee> eee = new ArrayList<>();
        eee.add(e1);
        eee.add(e2);

        list.addAll(eee);
        list.set(2, e1);
//        list.remove(300);

        list.add(2, list.remove(3));
        Iterator<Employee> iterator = list.iterator();
        while (iterator.hasNext()) {
            Employee e = iterator.next();
            System.out.printf(e.getId() + " ");
            System.out.println(e.getName());
            iterator.remove();
        }
        System.out.println(eee);

        List<Integer> lst = new LinkedList<>();
        List<Integer> lst2 = new ArrayList<>();

        for (int i = 0; i < 5; i++) {
            lst.add(i);
        }

//        lst.remove(0);
//
        lst2.add(2);
        lst2.add(3);
//        lst.removeAll(lst2);

        lst.retainAll(lst2);
        System.out.println(lst);

        Map<Integer, Integer> mp = new HashMap<>();
        mp.put(1, 1);
        mp.put(2, 2);
        mp.put(3, 3);
        Iterator<Integer> itt = mp.keySet().iterator();
    }
}
