
public class problem4 {

	public static void main(String[] args) {
		int highest = 0;
		for (int i = 100; i <= 999; i++){
			for (int j = 100; j <= 999; j++){
				int product = i*j;
				if (isPalindrome(Integer.toString(product))){
					if (product > highest ){
						highest = product;
					}
					
					
				}
				
			}
			
		}
		System.out.println("highest product: " + highest);

	}
	
	//takes in a string and returns true if it is a palindrome
	public static boolean isPalindrome(String a){
		String reverse = new StringBuffer(a).reverse().toString();
		if (a.equals(reverse)){
			return true;
		}
		else{
			return false;
		}
		
	}

}
