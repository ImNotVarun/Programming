//Java Program to Find Sum of Digits of a Number
package Project_File_Java.Simple_java;

import java.util.Scanner;

public class sum_digits {
    public static void main(String[] args) {
        try(Scanner a = new Scanner(System.in)){
            System.out.println("Enter the Value ");
            String b = a.nextLine();
            int sum = 0;
            for (int i = 0; i < b.length(); i++) {
                sum += b.charAt(i) - '0';
            }
            System.out.println("Sum of Digits is : " + sum);


        }
    }
    
}
