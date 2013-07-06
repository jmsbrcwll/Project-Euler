
public class problem5 {

	
	public static void main(String[] args) {
		//answer can't be less than 21, so start with 21
		int a = 21;
		
		do{
			a++;
			
		}while(!isDivisibleBy1to20(a));
		
		System.out.println(a);

	}
	
	public static boolean isDivisibleBy1to20(int a){
		
		for (int i = 1; i <=20; i++){
			//if not evenly divisible, return false

			if (a % i != 0){
				return false;
			}
			
		}
		return true;
		
	}

}
