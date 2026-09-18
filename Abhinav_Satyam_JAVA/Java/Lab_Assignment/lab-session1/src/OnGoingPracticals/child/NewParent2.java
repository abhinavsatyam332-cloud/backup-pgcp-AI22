package OnGoingPracticals.child;

import OnGoingPracticals.Parent;

public class NewParent2 {
    Parent p = new Parent();
    public void doSomething(){
        System.out.println(p.publicInt);
//        System.out.println(p.protectedInt);
//        System.out.println(privateInt);
//        System.out.println(defaultInt);
    }
}
