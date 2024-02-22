package Project_File_Java.Simple_java;
import java.util.Scanner;

public class advance_calculator {
    public static void main(String[] args) {
        try(Scanner a = new Scanner(System.in)){
            System.out.println("Welcome to the advance calculator");
            System.out.println("Enter the number");
            float num1 = a.nextInt();
            System.out.println("enter the second number");
            float num2 = a.nextInt();
            System.out.println("Enter the oprator you want to use for thr opreation \n Addition(+)\n Substraction(-)\n Multiplication(*)\n division(/)\n modulation(%)");
            String op = a.next();
            switch (op) {
                case "+":
                    System.out.println("Addition of the two input is " +(num1+num2));
                    break;
                case "-":
                    System.out.println("Substraction of the two number is " +(num1-num2));
                    break;
                case "*":
                    System.out.println("Multiplication if the two numbers is" +(num1*num2));
                    break;
                case "/":
                    System.out.println("Division of the two numbers is " +(num1/num2));
                    break;
                case "%":
                    System.out.println("Modulation of the two numbers is" +(num1%num2));
                    break;
                default:
                    System.out.println("Invalid Input");
                    break;
            }


        }
    }
    
}
