#include <iostream> 
#include <iomanip> 
#include <vector> 
using namespace std; 

// Function to initialize the coins array with 1s (representing single coins) 
void initCoins(vector<int>& coins, int n) { 
    coins.assign(n, 1); 
} 

// Function to find and print the moves to pair coins 
void pairCoins(int n) { 
    vector<int> coins; 
    initCoins(coins, n); // Initialize the coins array 
    int moves = 0; // Counter for moves 
    cout << "The array before pairing the coins:" << endl; 
    for (int i = 0; i < n; ++i) { 
        cout << setw(3) << coins[i]; 
    } 
    cout << endl; 

    // Pairing coins using brute force approach 
    for (int i = 0; i < n / 2; ++i) { 
        for (int j = n - 1; j > i; --j) { 
            if (coins[i] == 1 && coins[j] == 1) { 
                cout << "move coin " << j + 1 << " over coin " << n - i << " to form a pair." << endl; 
                coins[i] = 0; // Pair formed, so set coins[i] to 0 
                coins[j] = 2; // Pair formed, so set coins[j] to 2 
                moves++; // Increment moves counter 

                // Display the array after each move 
                for (int k = 0; k < n; ++k) { 
                    cout << setw(3) << coins[k]; 
                } 
                cout << endl; 
                break; // Move to the next i 
            } 
        } 
    } 
    cout << "\nThe number of moves executed is " << moves << " moves." << endl; 
    cout << "The array after pairing the coins:" << endl; 
    for (int i = 0; i < n; ++i) { 
        cout << setw(3) << coins[i]; 
    } 
    cout << endl; 
} 

int main() { 
    int n; 
    cout << "Insert the number of coins: "; 
    cin >> n; 
    // Check if the input is valid 
    if (n <= 0 || n % 2 != 0) { 
        cout << "Invalid input. The number of coins must be a positive even integer." << endl; 
        return 1; // Exit the program with an error code 
    } 
    pairCoins(n); // Pair the coins 
    return 0; 
}