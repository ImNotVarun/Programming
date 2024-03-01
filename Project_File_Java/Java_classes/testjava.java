package Project_File_Java.Java_classes;
import java.util.Scanner;

public class testjava {
    private static final String Varun = "default value";
    private String name;
    private int age;

    public testjava(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public testjava(String name) {
        this(Varun, 20);
        this.name = name;
    }

    static int count = 0;
    {
        count++;
    }

    public static void main(String[] args) {
        try (Scanner a = new Scanner(System.in)) {
            System.out.println("Enter the name : ");
            String name = a.nextLine();
            count_constructor name1 = new count_constructor(name);
            String nameValue = new String(name);
            count_constructor name2 = new count_constructor(nameValue);

            System.out.println("1: " + name1.name + " " + name1.age);
            System.out.println("2: " + name2.name + " " + name2.age);
            System.out.println("The total Number of constructors is : " + count);
        }
    }
}