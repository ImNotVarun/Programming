// Find Area of Rectangle
package Java;

import java.util.Scanner;

public class AreaOfRectangle {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            System.out.println("Area Of reectangle");
                    System.out.println("Enter Length : ");
                    float Length = sc.nextFloat();
                    System.out.println("Enter Width : ");
                    float Width = sc.nextFloat();
                    float result = (float) (Length * Width);

            System.out.println("Result : " + result);

            System.out.println("Enter C to Continue and Q to Quit");
            char ch = sc.next().charAt(0);
            if (ch == 'C') {
                main(args);
            } else {
                System.out.println("Thank You");
            }
        }
    }
}