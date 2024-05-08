#include <iostream>
#include <iomanip>
using namespace std;
// 0 -> empty
// 1 -> 1 coin
// 2 -> 2 coins (pair)
void initC(int coins[], int n)
{
	for (int i = 0; i < n; i++)
	{
		coins[i] = 1;
	}
}
void pairCoins(int coins[], int n)
{
	if (n % 4 != 0)
	{
		cout << "Invalid number of coins.\n The number of coins must be divisible by 4."<< endl;
			return;
	}
	int moves = 0;
	int i = 1;
	for (int j = n - 1; j >= 0; j--)
	{
		if (i <= (n / 4) - 1)
		{
			if (coins[j] == 1)
			{
				int idx = j - 1;
				int count = 0;
				while (count != i && idx >= 0)
				{
					if (coins[idx] == 1)
					{
						count++;
						idx--;
					}
					if (coins[idx] == 2)
					{
						count = count + 2;
						idx--;
					}
					if (coins[idx] == 0)
					{
						idx--;
					}
				}
				cout << "move coin " << idx + 1 << " over coin " << j + 1 << " to form a pair." << endl;
					coins[idx] = 0;
				coins[j] = 2;
				moves++;
				for (int k = 0; k < n; k++)
				{
					cout << setw(3) << coins[k];
				}
				cout << endl;
				i++;
			}
		}
		else break;
	}
	for (int j = 0; j < n; j++)
	{
		if (i <= n / 2)
		{
			if (coins[j] == 1)
			{
				int idx = j + 1;
				int count = 0;
				while (count != i && idx < n - 1)
				{
					if (coins[idx] == 1)
					{
						count++;
						idx++;
					}
					if (coins[idx] == 2)
					{
						count = count + 2;
						idx++;
					}
					if (coins[idx] == 0)
					{
						idx++;
					}
				}
				cout << "move coin " << idx + 1 << " over coin " << j + 1 << " to form a pair." << endl;
					coins[idx] = 2;
				coins[j] = 0;
				moves++;
				for (int k = 0; k < n; k++)
				{
					cout << setw(3) << coins[k];
				}
				cout << endl;
				i++;
			}
		}
		else break;
	}
	cout << "\nThe number of moves executed is " << moves << " moves." << endl;
}
int main()
{
	int n;
	cout << "Insert the number of coins: " << endl;
	cin >> n;

	// Check if the input is positive
	if (n <= 0) {
		cout << "Invalid input. The number of coins must be a positive integer." << endl;
		return 1; // Exit the program with an error code
	}

	// Check if the input is even but not divisible by 4
	if (n % 2 == 0 && n % 4 != 0) {
		cout << "Invalid input. The number of coins must be divisible by 4." << endl;
		return 1; 
	}

	// Check if the input is odd
	if (n % 2 != 0) {
		cout << "Invalid input. The number of coins must be an even number." << endl;
		return 1;
	}

	int* coins = new int[n];
	initC(coins, n);
	cout << "The array before pairing the coins: " << endl;
	for (int i = 0; i < n; i++)
	{
		cout << setw(3) << coins[i];
	}
	cout << endl;
	pairCoins(coins, n);
	cout << "\nThe array after pairing the coins: " << endl;
	for (int i = 0; i < n; i++)
	{
		cout << setw(3) << coins[i];
	}
	delete[] coins;

	return 0; 
}