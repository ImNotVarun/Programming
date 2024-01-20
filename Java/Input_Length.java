// Write a program that takes a string as input from user and prints its length to the console.
package Java;

public class Input_Length {
    public static void main(String[] args) {
        try (java.util.Scanner sc = new java.util.Scanner(System.in)) {
            System.out.print("Enter a string: ");
            String str = sc.nextLine();
            System.out.println("Length of the string is: " + str.length());
        }

    }
}
