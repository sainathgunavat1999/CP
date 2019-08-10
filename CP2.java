import java.util.Scanner;
public class CP2{
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String string=in.nextLine();
		String[] arr = string.split(" ");
		int maxLength=0;
		String temp="";
		for (String a : arr){
			if (a.length() > maxLength) {
				maxLength=a.length();
				temp=a;
			}
		}
		int maxFrequency = findFrequency(arr, temp);
		System.out.printf("\n{%d, %d}",maxLength,maxFrequency);
	}
	public static int findFrequency(String[] arr, String temp){
		int counter=0;
		for (String a: arr ) {
			if(a==temp){
				counter++;
			}			
		}
		return counter;
	}
}
/*Database management system is the set of programs to manage the database and to perform various operations on the database.*/