// Write a program that takes a list of integers as input and prints the sum of all the integers in the list.
package Java;

import java.util.Scanner;

// Main class
class NumbersSUM {
    // Main method
    public static void main(String[] args) {// Create a scanner object
        try (Scanner sc = new Scanner(System.in)) {
            // Get the number of elements from the user
            System.out.println("Enter the number of elements: ");
            int n = sc.nextInt();

            // Create an array to store the elements
            int[] arr = new int[n];

            // Get the elements from the user
            System.out.println("Enter the elements: ");
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            // Calculate the sum of the elements
            int sum = 0;
            for (int i = 0; i < n; i++) {
                sum += arr[i];
            }

            // Print the sum of the elements
            System.out.println("Sum of the elements: " + sum);
        }
    }
}
