import java.util.Scanner;

public class Test2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the N number to find their sum and average: ");
        double number = sc.nextDouble();
        
        if (number <= 0) {
            System.out.println("Please enter a positive number.");
        } else {
            double sum = 0.0;

            for (int i = 1; i <= number; i++) {
                sum += i;
            }
            System.out.println("Sum of first " + number + " numbers is : " + sum);
            System.out.println("Average of first " + number + " numbers is : " + (sum / number));
        
        sc.close();
    }
}