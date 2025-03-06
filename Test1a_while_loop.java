public class Test1a_while_loop {
    public static void main(String[] args) {
        System.out.println("Using while Loops : ");
        
        int i = 24;

        while (i >= -6) {
            if ( i != -6)  {
                System.out.print(i + ",");
            } else {
                System.out.print(i);
            }
            i -= 6;
        }
    }
    
}
