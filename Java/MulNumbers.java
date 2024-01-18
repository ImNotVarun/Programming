package Java;

import java.util.Scanner;

public class MulNumbers { 
    public static void main(String[] args) {
        try(Scanner scanner = new Scanner(System.in)){
            System.out.println("Enter first number: ");
            int num1 = scanner.nextInt();
            System.out.println("Enter second number: ");
            int num2 = scanner.nextInt();

            int mul = num1 * num2;
        System.out.println("Multiplication of these numbers: "+mul);
    }
    
}

}