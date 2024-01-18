package Java;

import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        try(Scanner scanner = new Scanner(System.in)){
            System.out.println("Enter first number: ");
            float num1 = scanner.nextInt();
            System.out.println("Enter second number: ");
            float num2 = scanner.nextInt();
            System.out.println("Enter operator: ");
            char operator = scanner.next().charAt(0);

            float result = 0;

            switch (operator) {
                case '+':
                    result = num1 + num2;
                    break;
                case '-':
                    result = num1 - num2;
                    break;
                case '*':
                    result = num1 * num2;
                    break;
                case '/':
                    result = num1 / num2;
                    break;
                default:
                    System.out.println("Invalid operator");
            }

            System.out.println("Result: " + result);
        }
    }
    
}
