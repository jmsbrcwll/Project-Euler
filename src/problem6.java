
public class problem6 {


	public static void main(String[] args) {
		
       System.out.println(sumOfSquaresAndSquaresOfSumsDiff(1,100));
	}
	
	
	//finds the sum of squares from a to b
	public static int sumOfSquaresAndSquaresOfSumsDiff(int a, int b){
		int sumOfSquares = 0;
		int sum = 0;
		for (int i = a; i <= b; i++){
	
			sumOfSquares += Math.pow(i,2);		
			sum += i;
		}
		int squareOfSums = (int)Math.pow(sum, 2);
		
		return squareOfSums - sumOfSquares;
	}

}
