public prime_number{
public static void main(String arg[])
{
int num=5;
boolean prime=true;
if (num<=1){
System.out.println("enter the valid number");
}
else{
for (i=2;i<=Math.squrt(num);i++){
prime=false;
break;
}
}
if(prime)
System.out.println("num is prime");
else
System.out.println("num is not prime");
}

}
