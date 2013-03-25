//If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

//Find the sum of all the multiples of 3 or 5 below 1000.

#include <iostream>

int main() {
	size_t sum = 0;
	size_t N=1000;
	for(int i=3; i<N; i+=3) {
		sum += i;
	}

	size_t sum2 = 0;
	for(int i=5; i<N; i+=5) {
		if(i%3 !=0)
						sum2 += i;
	}
	std::cout << "Sum = " << sum << "\n";
	std::cout << "Sum = " << sum2 << "\n";
	std::cout << "result = " << sum+sum2 << "\n";
}

