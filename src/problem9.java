
public class problem9 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int[] abc = find1000Triplet();
		int product = abc[0] * abc[1] * abc[2];
		System.out.println(product);

	}
	
	//brute force function to find the triplet a^2 + b^2 + c^2 = 1000
	public static int[] find1000Triplet(){
		int a = 1;
		int b = 1;
		int c = 1;
		boolean finished = false;
	
		
		for (int i = 0;  i<1000; i++ ){
			for (int j = 0; j <1000; j++){
				for (int k = 0; (a + b + c)<= 1000; k++){
					//System.out.println("current: " + a + " "+  b + " "+ c);
					if (is1000Triplet(a , b , c)){
						return new int[]{a,b,c};
					}
					c++;   //heyoooooooo
				}
				c = b;
				b++;
			}
			c = a;
			b = a;
			a++;
		}
		System.out.println(a + " " + b + " " + c);
	 return  new int[]{a,b,c};
		
	}
	
	public static boolean is1000Triplet(int a, int b, int c){
		if ((Math.pow(a, 2) + Math.pow(b, 2)) == Math.pow(c, 2)){
			//System.out.println("answer!:"+ a + " " + b + " " + c);
			if(a+b+c == 1000){
				System.out.println("answer!:"+ a + " " + b + " " + c);
				return true;
			}
		}

			return false;
		

		
	}

}
