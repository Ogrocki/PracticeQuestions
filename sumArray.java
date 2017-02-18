//Build a function that takes in a array and int and output
//a new array that is the sum of array based the int

import java.util.*;

public class sumArray {

public static void main(String[] args) {
	int[] num = {-1,2,3,4};
	int[] b=sumA(num, 2);
	for(int xx=0; xx<b.length; xx++){
			System.out.println(b[xx]);
	}
    }
public static int[] sumA(int[] a, int i){
	int[] temp = new int[a.length-(i-1)];
	int sum=0;
	for(int iii=0; iii<i; iii++){
		sum+=a[iii];
	}
	temp[0]=sum;

	for(int ii=i; ii<a.length; ii++){
		sum-=a[ii-i];
		sum+=a[ii];
		temp[ii-i+1]=sum;
	}
	return temp;
	}
}
