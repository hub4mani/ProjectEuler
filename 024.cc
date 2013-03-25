// next_permutation
#include <iostream>
#include <algorithm>
using namespace std;

int main () {
  //int myints[] = {2,6,7,1,9,8,5,4,3,0};
  int myints[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

  for(size_t i=0;i<10; ++i)
    cout << myints[i];
  cout << "\n";

  size_t count=1;
  while ( count < 1000000) {
    next_permutation (myints,myints+10) ;
    ++count;
  }
  for(size_t i=0;i<10; ++i)
    cout << myints[i];
  cout << "\n";

  return 0;
}
