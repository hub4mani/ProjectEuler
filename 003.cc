#include <iostream>
#include <vector>
#include <complex>

using namespace std;

int main() {
  unsigned long long N = 600851475143;

  const size_t LIMIT = std::sqrt(N);
  vector<int> primes(LIMIT,-1);
  primes[0] = 0;
  primes[1] = 1;

  size_t last_prime=1;
  for(size_t i=2; i<=LIMIT; ++i) {
    if(primes[i] == -1) { 
      primes[i] = 1;
      cout << i << "\n";
      for(size_t j=2; j*i<LIMIT; ++j) {
        primes[j*i] = 0;
      }
      if(N%i == 0) {
        last_prime = i;
        cout << "last prime = " << i << "\n";
        while(N%i == 0) N/=i;
      }
      if(N<LIMIT && primes[N] == 1)
        break;
    }
  }
  if(last_prime != 1)
    cout << last_prime << "\n";
  else
    cout << "original number" << "\n";
}

