import java.util.Scanner;
public class PCMB_PCMC_percentage{
    public static void main(){   
        int num1, num2, num3, num4;
        Scanner sc=new Scanner(System.in);
        System.out.print("\u000c");
        System.out.println("Please choose PCMC or PCMB and enter it(In capitals)");
        String subject=sc.next();
        if (subject.equals("PCMC")){
            System.out.println("Enter how much each subject is out of :");
            float total=(sc.nextFloat())*4; 
            System.out.println("Enter physics marks");
            float phy=sc.nextFloat();        
            System.out.println("Enter chemistry marks");
            float chem=sc.nextFloat();
            System.out.println("Enter mathematics marks");
            float math=sc.nextFloat();
            System.out.println("Enter computer marks");
            float comp=sc.nextFloat();  
            System.out.println("\u000c");
            Percentage a = new Percentage();
            double percentage = a.get_per((float)phy,(float)chem,(float)math,(float)comp,(float)total);
            System.out.print("PCMC : ");
            System.out.printf("%.2f",percentage);
            System.out.print("%");
        }
        else if (subject.equals("PCMB")){
            System.out.println("Enter how much each subject is out of :");
            float total=(sc.nextFloat())*4;
            System.out.println("Enter physics marks");
            float phy=sc.nextFloat();        
            System.out.println("Enter chemistry marks");
            float chem=sc.nextFloat();
            System.out.println("Enter mathematics marks");
            float math=sc.nextFloat();
            System.out.println("Enter biology marks");
            float bio=sc.nextFloat();    
            System.out.println("\u000c");
            Percentage a = new Percentage();
            double percentage = a.get_per((float)phy,(float)chem,(float)math,(float)bio,(float)total);
            System.out.print("PCMB : ");
            System.out.printf("%.2f",percentage);
            System.out.print("%");
        }
    }
}