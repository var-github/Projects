import java.util.Scanner;
public class Boxes
{
    public static void main(){
       Scanner x=new Scanner (System.in);
       System.out.println("\u000c");
       int b=3;
       String design="[_]";
       System.out.println("[_][_][_]");
       for(int c=1;c!=2;){
           System.out.println("Do you want to add or remove");
           System.out.println("Type ''dsn'' to change design");
           System.out.println("Type ''exit'' to exit");
           String h=x.next();
           if(h.equals("exit")){
              c=c+1;
           }
           if(h.equals("dsn")){
              System.out.println("Choose a design and type 1,2,3 or 4");
              System.out.println("1) [_]");
              System.out.println("2) |_|");
              System.out.println("3) {_}");              
              System.out.println("4) Custom design");
              int ch=x.nextInt();
              if(ch==1){
                 design="[_]";
              }
              if(ch==2){
                 design="|_|";
              }
              if(ch==3){
                 design="{_}";
              }              
              if(ch==4){
                 System.out.println("Enter your design");
                 design=x.next();
              }
           }
           if(h.equals("add")){
              System.out.println("How many more do you want to add");           
              int i=x.nextInt();                       
              b=b+i;
           }
           if(h.equals("remove")){
              System.out.println("How many do you want to remove");           
              int i=x.nextInt();                       
              b=b-i;
           }
           System.out.println("\u000c");
           for(int d=1;d<=(b-1);d++){
              System.out.print(design);            
           }
           System.out.println(design);
       }
       System.out.println("\u000c");
       System.out.println("You may exit the program now");     
    }
}