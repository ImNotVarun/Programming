package Javaa;

import java.util.Scanner;
import javax.swing.JOptionPane;

@SuppressWarnings("unused")
public class Main {
    // public static void main(String[] args) {
    // int x = 123; // declaration and assinement
    // System.out.println("the value of x is :" + x);
    // long y = 234235345343L;
    // System.out.println("The value of y is :" + y);
    // double z = 1233.34353;
    // System.out.println(z);
    // boolean a = true; // they only hold true and false
    // System.out.println(a);
    // char symbol = '#';
    // System.out.println(symbol);
    // String b = "hello world";
    // System.out.println(b);

    // }
    // }

    // public static void main(String[] args) {
    // int a = 10;
    // int b = 20;
    // int temp;
    // temp = a;
    // a = b;
    // b = temp;
    // System.out.println(a);
    // System.out.println(b);
    // }
    // }

    // public static void main(String[] args) {
    // try (Scanner a = new Scanner(System.in)) {
    // System.out.println("what is your name");
    // String name = a.nextLine();
    // System.out.println("What is your age :");
    // int age = a.nextInt();
    // a.nextLine();
    // System.out.println("What is your favorite food");
    // String food = a.nextLine();

    // System.out.println("You name is :" + name);
    // System.out.println("You age is :" + age);
    // System.out.println("You Favorite food is :" + food);
    // }
    // }
    // }

    // public static void main(String[] args) {
    // int f = 10;
    // f++;
    // System.out.println(f);
    // }
    // }

    // GUI application
    // public static void main(String[] args) {
    // String name = JOptionPane.showInputDialog("enter your name ");

    // }
    // }

    // public static void main(String[] args) {
    // double a = 1.46;
    // double b = 9;
    // double z = Math.max(a, b);
    // double v = Math.min(a, b);
    // double c = Math.abs(b);
    // double s = Math.sqrt(b);
    // System.out.println(z);
    // System.out.println(v);
    // System.out.println(c);
    // System.out.println(s);
    // }
    // }
    // triangle
    // public static void main(String[] args) {
    // try (Scanner a = new Scanner(System.in)) {
    // System.out.println("Enter the base of the trianle");
    // int base = a.nextInt();
    // System.out.println("enter the height");
    // int height = a.nextInt();
    // double hy = Math.sqrt(((base * base) + (height * height)));
    // System.out.println("The hypotinius of the triangle will be :" + hy);
    // }

    // }
    // }

    public static void main(String[] args) {
        String day = "Pizza";
        switch (day) {
            case "sunday":
                System.out.println("it is sunday");
                break;
            case "monday":
                System.out.println("it is monday");
                break;
            case "tueday":
                System.out.println("It is tuesday");
                break;
            case "Friday":
                System.out.println("it is friday");
                break;
            default:
                System.out.println("that is not a day");
        }
    }
}