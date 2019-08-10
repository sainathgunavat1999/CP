import java.util.Scanner;
public class CP8{
	public static void main(String[] args) {
		int height=1;
		Scanner in = new Scanner(System.in);
		int n=in.nextInt();
		for (int i=1;i<=n ;i++ ) {
			if (i%2==0) {
				height++;
			}else{
				height=height*2;
			}
		}
		System.out.println(height);
	}
}