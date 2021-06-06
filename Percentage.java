public class Percentage

{
    public float sub1, sub2, sub3, sub4,total;
    public Percentage()    // constructor
    {
        sub1 = 0; 
        sub2 = 0;
        sub3 = 0;
        sub4 = 0;
        total= 0;
    }

    public double get_per( float sub1, float sub2,float sub3,float sub4,float total)
    {
        double per = ((sub1+sub2+sub3+sub4)/total)*100;
        return per;
    }
}