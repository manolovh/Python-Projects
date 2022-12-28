#include <iostream>
using namespace std;

int main() {
  int smallest, number;

  cout << "Enter a number (or '.' to finish): ";
  cin >> number;
  smallest = number;

  while (cin >> number) {
    if (number < smallest) {
      smallest = number;
    }
  }

  cout << "The smallest number is: " << smallest << endl;

  return 0;
}
