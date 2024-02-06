package com.example.java;

import java.util.Scanner;
                                                                   /* calculator without using any if-else statements */

// public class java {
//     static Scanner sc = new Scanner(System.in);

//     public static void main(String[] args) {
//         System.out.print("Enter the first number ");
//         int n = sc.nextInt();
//         System.out.print("Enter the second number ");
//         int m = sc.nextInt();
//         System.out.print("Sum of two numbers = "+(n+m));
//         System.out.print("Sub of two numbers = "+(n-m));
//         System.out.print("Multipilcation of two numbers = "+(n*m));
//         System.out.print("Division of two numbers = "+(n/m));
//         System.out.print("Modulus of two numbers = "+(n%m));
//     }
// }


                                                        /* calculator in float form */

// public class java {
//     static Scanner sc = new Scanner(System.in);
//     public static void main(String[] args) {
//         System.out.println("Enter the first number ");
//         float a = sc.nextFloat();
//         System.out.println("Enter the second number ");
//         float b = sc.nextFloat();
//         System.out.println("addition of numbers is = "+(a+b));
//         System.out.println("subtraction of numbers is = "+(a-b));
//         System.out.println("multiplication of numbers is = "+(a*b));
//         System.out.println("division of numbers is = "+(a/b));
//         System.out.println("modulus of numbers is = "+(a%b));
//     }}

                                                    /* printing sunday if day 7 is sunday */
public class java {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println("Enter the day number ");
        int a = sc.nextInt();
        if (a==7){
            System.out.println("Sunday");
        }
        else{
            System.out.println("Not Sunday");
        }
    }
}