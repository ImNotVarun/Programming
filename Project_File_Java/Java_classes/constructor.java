package Project_File_Java.Java_classes;

public class constructor {
    private static final String Varun = "default value";
    private String name;
    private int age;

    public constructor(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public constructor(String name) {
        this(Varun, 20);
        this.name = name;
    }

    public static void main(String[] args) {
        constructor name1 = new constructor("Varun", 20);
        constructor name2 = new constructor("Vishal",20);

        System.out.println("Name: " + name1.name +  "\nAge: " + name1.age);
        System.out.println("Name: " + name2.name + "\nAge: " + name2.age);
    }
}
