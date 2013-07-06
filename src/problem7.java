import java.math.BigInteger;
import java.util.ArrayList;


public class problem7 {


	public static void main(String[] args) {
		ArrayList<String> primes = new ArrayList<String>();
		BigInteger i = new BigInteger("1");
		do{
			if (i.isProbablePrime(100)){
				primes.add(i.toString());
			}
			i =  i.add(BigInteger.ONE);
			
			
		}while (primes.size() < 10001);

		System.out.println(primes.get(10000));
	}

}
