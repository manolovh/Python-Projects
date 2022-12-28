#include <iostream>
using namespace std;

int main() {
  int sum = 0; 
  int count = 0; 
  int num; 

  cout << "Enter numbers (0 to terminate): ";
  cin >> num;
  while (num != 0) {
    sum += num; 
    count++;
    cin >> num;
  }

  if (count > 0) {
    double average = static_cast<double>(sum) / count;
    cout << "Average: " << average << endl;
  } else {
    cout << "No numbers were entered." << endl;
  }

  cout << "Sum: " << sum << endl;

  return 0;
}