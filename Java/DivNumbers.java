package Java;

import java.util.Scanner;

public class DivNumbers { 
    public static void main(String[] args) {
        try(Scanner scanner = new Scanner(System.in)){
            System.out.println("Enter first number: ");
            float num1 = scanner.nextInt();
            System.out.println("Enter second number: ");
            float num2 = scanner.nextInt();

            Float Div = num1 / num2;
        System.out.println("Divition of these numbers: "+Div);
    }
    
}

}