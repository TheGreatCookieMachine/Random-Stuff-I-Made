#include <iostream>

int main() {
    for( int n = 1; n < 101; n = n + 1 ) {
        if( n % 5 == 0 and n % 3 == 0 ) {
            std::cout << "Fizz Buzz";
        }
        else if( n % 5 == 0 ) {
            std::cout << "Buzz";
        }
        else if( n % 3 == 0) {
            std::cout << "Fizz";
        }
        else {
            std::cout << n;
        }
        std::cout << std::endl;
    }
}
