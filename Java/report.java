package Java;
import java.util.Scanner;

public class report {

    public static void main(String[] args) {
        System.out.println("Repots Card of the student");
        try (Scanner scr = new Scanner(System.in)) {
            System.out.println("Maths :");
            int a = scr.nextInt();
            System.out.println("Computer Netework :");
            int CN = scr.nextInt();
            System.out.println("Cloud Computing :");
            int CC = scr.nextInt();
            System.out.println("Linux :");
            int L = scr.nextInt();
            System.out.println("Java :");
            int J = scr.nextInt();
            int per=((a+CN+CC+L+J)*100)/500;
            System.out.println("The percentage of the student is :"+per);
        }
        }
        }
