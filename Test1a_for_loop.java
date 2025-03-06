import java.util.Scanner;

public class Test1a_for_loop {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Using for loops : ");
        for ( int i = 24; i >= -6; i -= 6) {

            if ( i != -6) {
                System.out.print(i + ","); 
            } else {
                System.out.print(i);
            } 
        }
    }    
}
