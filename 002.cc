#include <iostream>

int main() {
	size_t a=1,b=2;
	size_t sum=0;
	size_t LIMIT = 4000000;
	while(b<LIMIT) {
		if(b%2==0)
			sum += b;
		std::cout << "sum = " << sum << " a = " << a << " b = " << b << "\n";
		size_t tmp = a;
		a = b;
		b = a + tmp;
	}
	std::cout << sum << std::endl;
}

