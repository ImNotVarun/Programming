                                         // WAP to perform Java Program to Demonstrate Primitive Data Type
package Project_File_Java.Simple_java;

import java.util.Scanner;

public class primitive_datatype {
    public static void main(String[] args) {
        try(Scanner a = new Scanner(System.in)){
            System.out.println("Enter the int value ");
            int a1 = a.nextInt();
            System.out.println("The Entered  int value is "+a1);

            System.out.println("Enter the Boolean value");
            boolean b1 =a.nextBoolean();
            System.out.println("The Entered  Boolean value is "+b1);

            System.out.println("enter the char value");
            char c1 =a.next().charAt(0);
            System.out.println("The Entered  char value is "+c1);

            System.out.println("enter the float value");
            float f1 = a.nextFloat();
            System.out.println(" The Entered  float value is"+f1);

            System.out.println("enter the double value");
            double d1 =a.nextDouble();
            System.out.println("The Entered value of double is"+d1);


            System.out.println("enter the short value");
            short s1 = a.nextShort();
            System.out.println("The Entered  short value is"+s1);


            System.out.println("enter the long value");
            long l1 = a.nextLong();
            System.out.println("The Entered long value is"+l1);

            System.out.println("enter the string value");
            String S1 = a.next();
            System.out.println("The Entered string value is "+S1);


            System.out.println("enter the byte value");
            byte b2 = a.nextByte();
            System.out.println("The Entered byte value is "+b2);

        }
    }
}
