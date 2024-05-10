#include <iostream>
using namespace std;

int towerOfHanoiDynamic(int n) {
    // Initialize a 2D array to store the number of moves for each number of disks and pegs
    const int DISKS = 8; //  number of disks
    const int PEGS = 4;  //  number of pegs
    int dp[PEGS][DISKS + 1];

    // Base cases: 0 moves for 0 disks, 1 move for 1 disk
    for (int peg = 0; peg < PEGS; peg++) {
        dp[peg][0] = 0;
        dp[peg][1] = 1;
    }

    // Fill the dp table using dynamic programming
    for (int disks = 2; disks <= n; disks++) {
        for (int peg = 0; peg < PEGS; peg++) {
            int min_moves = dp[peg][disks - 1] * 2 + 1;
            for (int prev_peg = 0; prev_peg < PEGS; prev_peg++) {
                if (prev_peg != peg) {
                    min_moves = min(min_moves, dp[prev_peg][disks - 1] * 2 + 1);
                }
            }
            dp[peg][disks] = min_moves;
        }
    }

    return dp[PEGS - 1][n]; // Return the minimum moves required for all disks on the last peg
}

int main() {
    int N = 8; // Number of disks

    // Calculate the minimum moves using dynamic programming
    int min_moves = towerOfHanoiDynamic(N);

    cout << "Minimum Moves Required with Dynamic Programming: " << min_moves << endl;

    return 0;
}



