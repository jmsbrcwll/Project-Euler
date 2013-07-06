
public class problem2 {


	public static void main(String[] args) {
		int sum = 0;
		//we know 1 is not an even fibonnacci, so no need to start at 1
		for (int i = 2; i <= 4000000; i++){
			
			if (checkEven(i) && checkFib(i)){
				sum += i;
			}
			
		}
		System.out.println(sum);

	}
	
	
	//checks if the number is a member of the fibonacci sequence
	public static boolean checkFib(int a){
		int first = 1;
		int second = 2;
		int tmp;
		if ((a == 1) || (a == 2)){
			return true;
		}
		
		do{
			tmp = first + second;
			first = second;
			second = tmp;
			
			if (second == a){
				return true;
			}
			if (second > a ){
				return false;
			}
									
		}while(true);
		
		
		
		
	}
	
	//checks if the input is even
	public static boolean checkEven(int a){
		if (a % 2 == 0){
			return true;
		}
		else{
			return false;
		}
		
	}

}
