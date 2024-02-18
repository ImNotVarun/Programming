package Project_File_Java;
import java.util.Scanner;

public class sum_nth_number {
    public static void main(String[] args) {
        try(Scanner a = new Scanner(System.in)){
            System.out.println("Enter the number");
            int n = a.nextInt();
            int sum=0;
            for (int i=0;i<=n;i=i+1){
                sum=sum+i;
            }
            System.out.println("Sum of all number up to " +n+" is "+sum);



        }
    }}