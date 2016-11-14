package algorithms;
import java.util.Arrays;

public class QuickSortDemo {
	public static void main(String[] args){
		System.out.println("-----------------Quick Sort--------------");
		int N = 100;
		int[] target = new int[N];
		for(int i = 0; i<N; i++){
			target[i] = (int)(1000*Math.random());
		}
		int[] backup = target.clone();
		quickSort(target,0,target.length-1);
		/*
		for(int i = 0; i<N; i++){
			System.out.println(i+1 + "th: "+target[i]);
		}
		*/
		Arrays.sort(backup);
		for(int i = 0; i<N; i++){
			if (target[i] != backup[i]){
				System.out.println("Not Work normally!");
				break;
			}
		} 
		System.out.println("Work well!");
	}
	public static void quickSort(int[] nums, int start, int end){
		int i = start, j = end;
		if ((nums == null)||(nums.length == 0)){
			return;
		}
		while(i<j){
			while((i<j)&&(nums[i]<=nums[j])) j--;
			if (i<j){
				int temp = nums[i];
				nums[i] = nums[j];
				nums[j] = temp;
			}
			while ((i<j)&&(nums[i]<nums[j])) i++;
			if (i<j){
				int temp = nums[i];
				nums[i] = nums[j];
				nums[j] = temp;
			}
		}
		if (i - start > 1){
			quickSort(nums,start,i-1);
		}
		if (end - j > 1){
			quickSort(nums,j+1,end);
		}
	}
}
