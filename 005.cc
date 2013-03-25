#include <iostream>

using namespace std;

size_t gcd(size_t n1, size_t n2) {
  if(n2 == 0)
    return n1;
  return gcd(n2, n1%n2);
}

int main() {
  size_t result = 20*19;
  for (size_t i=18; i>=11; --i) {
    size_t g =  gcd(result,i);
      result = (result * i)/g;
  }
  cout << result << endl;
}

