package Project_File_Java;
import java.util.Scanner;

public class positive_negative {
    public static void main(String[] args) {
        try (Scanner a = new Scanner(System.in)) {
        System.out.println("Enter the number");
        int num = a.nextInt();
        if (num>=0){
            System.out.println("It is a positive integer");
        }
        else{
            System.out.println("It is a negative integer");
        }

    }
}}
