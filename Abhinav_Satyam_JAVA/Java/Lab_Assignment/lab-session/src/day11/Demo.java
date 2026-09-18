package day11;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;

public class Demo {
    public static void main(String[] args) {
        try {

            Class<?> clazz = Class.forName("day11.MyClass");

            Constructor<?> constructor = clazz.getDeclaredConstructor();
            Object instance = constructor.newInstance();

            Method setMethod = clazz.getDeclaredMethod("setI", int.class);
            setMethod.invoke(instance, 1); // Pass 1 as argument

            Method getMethod = clazz.getDeclaredMethod("getI");
            int i = (int) getMethod.invoke(instance);

            System.out.println("Retrieved value of i: " + i);

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}