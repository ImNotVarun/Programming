package Project_File_Java.Simple_java;
import java.util.Scanner;

public class greatest {
    public static void main(String[] args) {
        try (Scanner a = new Scanner(System.in)) {
        System.out.println("Enter the first number");
        int num = a.nextInt();
        System.out.println("Enter the second number");
        int num2 = a.nextInt();
        System.out.println("Enter the third number");
        int num3 = a.nextInt();

        if (num>num2 && num>num3){
            System.out.println(+num+" is the largest number");}
        else if (num2>num && num2>num3){
            System.out.println(+num2+" is the largest number");
        }
        else{
            System.out.println(+num3+ " is the largest number");
        }
        
    }
    
}}
