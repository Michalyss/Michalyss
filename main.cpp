#include <iostream>
#include <limits> // For std::numeric_limits

using namespace std;

/*
int is a number without decimal point.
float is a number with a decimal point.
double is a float with double precision.
bool is a variable which has only two states: true or false.
char is a one character in single quotation marks.
string is everything inside double quotation marks.
*/

int main() {
    float num1, num2;

    // Read and validate the first number
    cout << "Enter a number: ";
    while (!(cin >> num1)) {
        cout << "Enter a valid number: ";
        cin.clear(); // Clear the error state
        cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Ignore the invalid input
    }

    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clear the buffer before taking second input

    // Read and validate the second number
    cout << "Enter another number: ";
    while (!(cin >> num2)) {
        cout << "Enter a valid number: ";
        cin.clear(); // Clear the error state
        cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Ignore the invalid input
    }

    // Calculate the sum
    float sum = num1 + num2;

    // Display the result
    cout << "The sum is " << sum << endl;

    return 0;
}