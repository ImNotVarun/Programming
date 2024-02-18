package Project_File_Java;
import java.util.Scanner;
public class sum_of_even_odd_nth_number_seprately {
    public static void main(String[] args) {
        try(Scanner a = new Scanner(System.in)){
            System.out.println("Enter the Number");
            int n = a.nextInt();
            int sum=0;
            int sum2=0;
            
            for (int i=0;i<=n;i=i+1)
            {
                if(i%2==0)
                {
                sum=sum+i;
                }
                else
                {
                    sum2=sum2+i;
                }
            }
               System.out.println("sum of even number to the "+n+" term is "+sum);
               System.out.println("Sum of odd numbers to the "+n+" term is "+sum2);
        }
    }
}