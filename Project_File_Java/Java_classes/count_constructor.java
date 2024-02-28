package Project_File_Java.Java_classes;

public class count_constructor {
    private static final String Varun = "default value";
    private String name;
    private int age;

    public count_constructor(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public count_constructor(String name) {
        this(Varun, 20);
        this.name = name;
    }
    static int count = 0; 
    {
        count++;
    }

    public static void main(String[] args) {
        count_constructor name1 = new count_constructor("Varun", 20);
        count_constructor name2 = new count_constructor("Vishal",20);
        count_constructor name3 = new count_constructor("Rohan",20);
        count_constructor name4 = new count_constructor("Abhishek",20);
        count_constructor name5 = new count_constructor("Harsh",20);
        count_constructor name6 = new count_constructor("Jigyasu",20);

        System.out.println("1: "+ name1.name +  + name1.age);
        System.out.println("2: "+ name2.name + + name2.age);
        System.out.println("3: "+ name3.name + + name2.age);
        System.out.println("4: "+ name4.name + + name4.age);
        System.err.println("5: "+ name5.name + + name5.age);
        System.out.println("6: "+ name6.name + + name6.age);
        System.out.println("The total Number of constructors is : "+count);
    }
}
