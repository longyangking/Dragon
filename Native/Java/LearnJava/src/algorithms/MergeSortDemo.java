package algorithms;

import java.util.Arrays;

public class MergeSortDemo {
	public static void main(String[] args){
		System.out.println("-----------------Merge Sort--------------");
		int N = 100;
		int[] target = new int[N];
		for(int i = 0; i<N; i++){
			target[i] = (int)(1000*Math.random());
		}
		int[] backup = target.clone();
		mergeSort(target,0,target.length-1);
		Arrays.sort(backup);
		for(int i = 0; i<N; i++){
			if (target[i] != backup[i]){
				System.out.println("Not Work normally!");
				break;
			}
		} 
		System.out.println("Work well!");
	}
	public static int[] mergeSort(int[] nums, int low, int high){
		int mid = (low + high)/2;
		if (low < high){
			mergeSort(nums,low,mid);
			mergeSort(nums,mid + 1, high);
			merge(nums,low,mid,high);
		}
		return nums;
	}
	public static void merge(int[] nums, int low, int mid, int high){
		int[] temp = new int[high - low + 1];
		int i = low, j = mid + 1, k = 0;
		while ((i<=mid)&&(j<=high)){
			if (nums[i] < nums[j]){
				temp[k++] = nums[i++];
			}else {
				temp[k++] = nums[j++];
			}
		}
		while (i<= mid) temp[k++] = nums[i++];
		while (j<= high) temp[k++] = nums[j++];
		for (int k2 = 0; k2 < temp.length; k2++) nums[k2 + low] = temp[k2];
	}
}
