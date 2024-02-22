package Project_File_Java.Simple_java;
import java.util.Scanner;

public class even_odd {
    public static void main(String[] args) {
        try (Scanner a = new Scanner(System.in)) {
        System.out.println("Enter a number");
        int num = a.nextInt();
        if (num%2==0){
            System.out.println("It is an even number");
        }
        else {
            System.out.println("It is an odd number");
        }

    }
}
}
