#include <iostream>
#include <cstdio>

int main() {
  for (int i = 1; i <= 5000; ++i) {
    char buffer[5];
    sprintf(buffer, "%04d", i);

    int first_two = (buffer[0] - '0') * 10 + (buffer[1] - '0');
    int last_two = (buffer[2] - '0') * 10 + (buffer[3] - '0');

    if (first_two == last_two) {
      std::cout << i << std::endl;
    }
  }

  return 0;
}
