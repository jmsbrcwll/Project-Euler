import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Collections;


public class problem3 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		BigInteger a = new BigInteger("600851475143");
		BigInteger divider = new BigInteger("2");
		ArrayList<BigInteger> primeFactors = new ArrayList<BigInteger>();
		boolean finished = false;
		do{
			//if we find a factor, check if it's prime
			if (a.remainder(divider) == BigInteger.ZERO){
			   //check if the result is also prime. If so,
			   //	then we are done
				if (a.divide(divider).isProbablePrime(100)){
					primeFactors.add(a.divide(divider));
					finished = true;
					
				}
				a = a.divide(divider);
				divider = new BigInteger("2");

			}
			else{
				
				do{
					
					divider = divider.add(BigInteger.ONE);
				}while(!divider.isProbablePrime(100));
			}

		}while(finished == false);
		
		Collections.sort(primeFactors);
		System.out.println(primeFactors.get(primeFactors.size()-1).toString());
		
	}
	
	


}
