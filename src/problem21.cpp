#include <iostream>
#include <unordered_map>
using namespace std;

bool areAmicable(int a, int b);
int properDivisorSum(int a);
int calcProperDivisorSum(int a);

std::unordered_map<int,int> cache;

int main()
{

	int total = 0;
	for(int i = 1; i < 10000; i++){		

		cout<<"current:"<<i<<"\n";

		for(int j = 1; j < 10000; j++){
			if (areAmicable(i,j) & (i != j))
				total += i;		
		}
		
	}
	cout<<"total: "<<total<<"\n";  		

}

bool areAmicable(int a, int b)
{
	return ((properDivisorSum(a) == b) & (a == properDivisorSum(b)));
	
}

int properDivisorSum(int a)
{
	if (cache.find(a) == cache.end()) {
		int sum = calcProperDivisorSum(a);
		cache.insert(std::pair<int,int>(a,sum));
		return sum;

	} else {
		return cache.at(a);
	}
	
}

int calcProperDivisorSum(int a)
{	
	int total = 0;
	for(int i = a-1; i > 0; i--){
		if (a%i == 0){
			total += i;
		}
	}
	return total;
}
