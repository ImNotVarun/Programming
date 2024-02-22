package Project_File_Java.Simple_java;

import java.util.Scanner;

public class factorial {
    public static void main(String[] args) {
        try(Scanner a = new Scanner(System.in)){
            System.out.println("enter the number");
            int n = a.nextInt();
            int mul=1;
            for(int i=n;i>0;i=i-1){
                mul =mul*i;
            }
            System.out.println("Factorial of the number "+n+ " is " +mul);

        }
    }
}
