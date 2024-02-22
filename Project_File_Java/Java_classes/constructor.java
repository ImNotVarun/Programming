package Project_File_Java.Java_classes;

public class constructor {
    private static final String Varun = "default value";
    @SuppressWarnings("unused")
    private String name;
    @SuppressWarnings("unused")
    private int age;

    public constructor(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public constructor(String name) {
        this(Varun, 20);
        this.name = name;
    }
}
