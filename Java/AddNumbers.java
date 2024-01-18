package Java;

import java.util.Scanner;

public class AddNumbers {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Enter two numbers:");
            int num1 = scanner.nextInt();
            int num2 = scanner.nextInt();

            int sum = num1 + num2;

            System.out.println("The sum of the two numbers is " + sum);
        }
    }
}
