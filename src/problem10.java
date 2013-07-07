import java.math.BigInteger;


public class problem10 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		long sum = 0;
        for(int i = 1; i < 2000000; i++){
        	BigInteger tmp = new BigInteger(Integer.toString(i));
			if (tmp.isProbablePrime(1000000)){
				sum += (long)tmp.intValue();
			}
        }

		
		System.out.println(sum);

	}

}
