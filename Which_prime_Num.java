import java.util.*;
import java.util.Scanner;
public class Which_prime_Num
{
    public static void main(){
        Scanner x = new Scanner (System.in);
        System.out.println("\u000c");
        int primeTest = 0;
        System.out.println("Which prime number do you want ? (For example when 4 is entered the program will tell the 4th prime number )");
        int n = x.nextInt();
        long startTime = System.currentTimeMillis();;
        List<Integer> prime = new ArrayList<Integer>();
        prime.add(2);
        prime.add(3);
        prime.add(5);        
        for (int i = 7; n > prime.size();i++){            
            for(int y = 0; prime.get(y)<(Math.sqrt(i)+1);y++){
                if(i % prime.get(y) == 0){
                    primeTest = 1;
                    break;
                }                                
            }
            if(primeTest == 0){
                prime.add(i);                
            }
            primeTest=0;
            i+=1;            
        }        
        System.out.println("The "+n+"th prime number is "+prime.get(n-1));
        double sec = (System.currentTimeMillis()-startTime);
        System.out.println("It took "+(sec/1000)+" seconds");  
    }
}
