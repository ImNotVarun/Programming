package Project_File_Java.Java_number;
import java.util.Scanner;

public class armstrong {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
        int n = 0 ,a,b,c;
        System.out.println("Enter the number");
        n=sc.nextInt();
        a=n%10;
        b=n/10;
        c=b%10;
        b=b/10;
        if(a*a*a+b*b*b+c*c*c==n)
        {
            System.out.println("The number is armstrong");
        }
        else
        {
            System.out.println("The number is not armstrong");
        }
        
    }
    }
}
