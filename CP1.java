import java.util.Scanner;
public class CP1{
	public static void main(String[] args) {
		Scanner in= new Scanner(System.in);
		System.out.println("Enter number");
		int n=in.nextInt();
		System.out.printf("%d ",n);
		while(n!=1){
			if (n%2==0) {
				n=n/2;
				System.out.printf("%d ",n);
			}
			else{
				n=n*3+1;
				System.out.printf("%d ",n);
			}
		}
	}
}