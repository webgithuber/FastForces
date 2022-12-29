import java.util.*;
public class comp {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		for(int t=sc.nextInt();t-->0;) {
			int n=sc.nextInt(),a[]=new int[n],max=0,max2=1;
			for(int i=0;i<n;i++)
				if((a[i]=sc.nextInt())>=a[max])max=i;
			max2=max==1?0:1;
			for(int i=0;i<n;i++)if(i!=max&&a[i]>=a[max2])max2=i;
			for(int i=0;i<n;i++)
				System.out.print((a[max]==a[i]?a[i]-a[max2]:a[i]-a[max])+" ");
			System.out.println();
			
		}
		sc.close();

	}

}
