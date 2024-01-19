// Find Area of circle and Circumference
package Java;

import java.util.Scanner;

public class AreaofCircle {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)) {
            System.out.println("Area or Cirm ");
            char operator = sc.next().charAt(0);

            float result = 0;

            switch (operator) {
                case 'A':
                    System.out.println("Enter Radius ");
                    float radius = sc.nextFloat();
                    result = (float) (3.14 * radius * radius);
                    break;
                case 'C':
                    System.out.println("Enter Radius ");
                    float radius1 = sc.nextFloat();
                    result = (float) (2 * 3.14 * radius1);
                    break;
                default:
                    System.out.println("Invalid Operator");
                    break;
            }
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