#include <iostream> 
#include <iomanip> 
#include <vector> 
using namespace std; 

// Function to initialize the coins array with 1s (representing single coins) 
void initCoins(vector<int>& coins, int n) { 
    coins.assign(n, 1); 
} 

// Function to check if the given coin can be paired with any other coin 
bool canPair(int index, const vector<int>& coins) { 
    // Look for a 1 to pair with 
    for (int i = index + 1; i < coins.size(); ++i) { 
        if (coins[i] == 1) { 
            return true; 
        } 
    } 
    return false; 
} 

// Function to find and print the moves to pair coins using backtracking 
void pairCoinsBacktrack(vector<int>& coins, int index, int& moves) { 
    // Base case: If all coins are paired, return 
    if (index == coins.size()) { 
        return; 
    } 

    // If the coin at the current index is already paired, move to the next coin 
    if (coins[index] == 2) { 
        pairCoinsBacktrack(coins, index + 1, moves); 
        return; 
    } 
 
    // If the coin at the current index can be paired with any other coin, pair it 
    if (coins[index] == 1 && canPair(index, coins)) { 
        for (int i = index + 1; i < coins.size(); ++i) { 
            if (coins[i] == 1) { 
                cout << "move coin " << i + 1 << " over coin " << index + 1 << " to form a pair." << endl; 
                coins[i] = 2; 
                coins[index] = 0; 
                moves++; 
 
                // Print the array after each move 
                cout << " "; 
                for (int j = 0; j < coins.size(); ++j) { 
                    cout << setw(2) << coins[j]; 
                } 
                cout << endl; 
                break; 
            } 
        } 
    } 

    // Recur for the next coin 
    pairCoinsBacktrack(coins, index + 1, moves); 
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

    vector<int> coins; 
    initCoins(coins, n); // Initialize the coins array 
    int moves = 0; // Counter for moves 
    cout << "The array before pairing the coins:" << endl; 
    for (int i = 0; i < n; ++i) { 
        cout << setw(2) << coins[i]; 
    } 
    cout << endl; 

    // Pair the coins using backtracking 
    pairCoinsBacktrack(coins, 0, moves); 
    cout << "\nThe number of moves executed is " << moves << " moves." << endl; 
    cout << "The array after pairing the coins:" << endl; 
    for (int i = 0; i < n; ++i) { 
        cout << setw(2) << coins[i]; 
    } 
    cout << endl; 
    return 0; 
}