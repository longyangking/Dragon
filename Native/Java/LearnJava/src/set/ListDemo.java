package set;
import java.util.Random;
import java.util.List;
import java.util.ArrayList;

public class ListDemo {
	public static void main(String[] args){
		int M = 5, N = 5, L = 5;
		List<int[][]> list =  new ArrayList<int[][]>();
		//ArrayList<int[][]> list =  new ArrayList<int[][]>();
		for(int i=0;i<L;i++){
			list.add(randomdata(M,N));
		}
		System.out.println("The Size of set is "+list.size());
		for(int[][] a:list){
			System.out.println("Element:");
			for(int i = 0; i<M; i++){
				for(int j = 0; j<N; j++){
					System.out.print(a[i][j]+" ");
				}
			}
			System.out.println();
		}
	}
	public static int[][] randomdata(int m, int n){
		int[][] data = new int[m][n];
		Random rand = new Random();
		for(int i = 0; i<m; i++){
			for(int j = 0; j<n; j++){
				data[i][j] = rand.nextInt(100);
			}
		}
		return data;
	}
}
