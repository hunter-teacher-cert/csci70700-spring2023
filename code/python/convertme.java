  import java.io.*;
  import java.util.*;
  
  public class Recursion {
  
   public static void main(String[] args) {
    System.out.println("Good News Everyone!");
    System.out.printf("1! = %d\n", factorial(1) );
    System.out.printf("fib(1) = %d\n", fib(1) );
   }
  
   public static int factorial(int n) {
       int prod = 1;
       int i;
       for (i=n;i>1;i--){
           prod = prod * i;
       }
        return prod;
   }
   public static int fib(int n) {
       if (n<2){
           return 1;
       } else {
           return fib(n-1)+fib(n-2);
       }
  
   }
  }
