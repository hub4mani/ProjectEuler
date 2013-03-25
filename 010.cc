#include <iostream>
#include <vector>
#include <complex>

using namespace std;

int main() {
  const size_t LIMIT = 2000000;
  vector<int> primes(LIMIT,-1);
  primes[0] = 0;
  primes[1] = 1;

  unsigned long long sum=0;
  for(size_t i=2; i<=LIMIT; ++i) {
    if(primes[i] == -1) { 
      primes[i] = 1;
      cout << i << "\n";
      sum += i;
      for(size_t j=2; j*i<LIMIT; ++j) {
        primes[j*i] = 0;
      }
    }
  }
  cout << "sum = " << sum << "\n";
}

