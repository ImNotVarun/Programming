package Project_File_Java.Simple_java;

import java.util.Scanner;

public class even_odd_sum {
    public static void main(String[] args) {
        try(Scanner a = new Scanner(System.in))
        {
            System.out.println("Enter the number");
            int n = a.nextInt();
            int sum=0;
            int i =0;
            int m=0;
            System.out.println("Even Numbers are");

            for(i=0;i<=n;i=i+1)
            {
                if (i%2==0) 
                {
                    System.out.println(+i); 
                } 
                else{}
                
                
            }
            System.out.println("Odd Numbers are");

            for(m=0;m<=n;m=m+1)
            {
                sum=sum+m;
            
                if (m%2!=0) 
                {
                    System.out.println(+m);
                }
                else if(m%1==0){


                }
                
            }
            System.out.println("The Sum of these are \n"+sum);
        }
    }
}
