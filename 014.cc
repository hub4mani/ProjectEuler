#include <iostream>
#include <map>

using namespace std;

size_t get_next_num(size_t n) {
  if(n%2) {
    return 3*n+1;
  }
  return n/2;
}
int main() {
  int N=13;
  while((N=get_next_num(N)) != 1) {
    cout << N << " ";
  }
  cout << endl;
}

