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
        constructor name3 = new constructor("Rohan",20);
        constructor name4 = new constructor("Abhishek",20);
        constructor name5 = new constructor("Harsh",20);
        constructor name6 = new constructor("Jigyasu",20);

        System.out.println("Name: " + name1.name +  "\nAge: " + name1.age);
        System.out.println("Name: " + name2.name + "\nAge: " + name2.age);
        System.out.println("Name: " + name3.name + "\nAge: " + name3.age);
        System.out.println("Name: " + name4.name + "\nAge: " + name4.age);
        System.out.println("Name: " + name5.name + "\nAge: " + name5.age);
        System.out.println("Name: " + name6.name + "\nAge: " + name6.age);
    }
}
