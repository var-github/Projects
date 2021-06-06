import java.util.*;
import java.util.Scanner;
public class Prime_uptill
{
    public static void main(){
        Scanner x = new Scanner (System.in);
        System.out.println("\u000c");
        int primeTest = 0;
        System.out.println("Find prime numbers uptil ?");
        int n = x.nextInt();
        long startTime = System.currentTimeMillis();;
        List<Integer> prime = new ArrayList<Integer>();
        prime.add(2);
        prime.add(3);
        prime.add(5);
        for (int i = 7; i < (n+1);i++){            
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
        System.out.println(prime.toString());
        double sec = (System.currentTimeMillis()-startTime);
        System.out.println("It took "+(sec/1000)+" seconds");  
    }
}