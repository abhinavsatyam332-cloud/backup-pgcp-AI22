package Assignment3.Task3;

public class RunTask {
    static void runTask(int value) throws Exception{
        SimulatedResource sr = new SimulatedResource();
        sr.open();
        try {
            sr.process(value);
        } finally {
            sr.close();

        }
    }
}
