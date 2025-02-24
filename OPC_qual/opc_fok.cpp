#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    int N; // Number of trade orders
    cin >> N;

    // Order books: Buy side and Sell side
    map<int, int, greater<int>> buySide; // Price -> Quantity
    map<int, int> sellSide; // Price -> Quantity

    // Total traded volume
    long long totalTradedVolume = 0;

    // Process each order
    for (int i = 0; i < N; ++i) {
        string side, type;
        int price, quantity;
        cin >> side >> type >> price >> quantity;

        // Process GTC orders
        if (type == "GTC") {
            if (side == "BUY") {
                // Match BUY order with SELL side
                auto it = sellSide.begin(); // Start with the lowest sell price
                while (it != sellSide.end() && quantity > 0 && price >= it->first) {
                    int tradeQty = min(quantity, it->second); // Match the minimum quantity
                    totalTradedVolume += tradeQty;
                    quantity -= tradeQty;
                    it->second -= tradeQty;

                    // Remove the sell order if fully filled
                    if (it->second == 0) {
                        it = sellSide.erase(it);
                    } else {
                        ++it;
                    }
                }

                // If any quantity is left, add to BUY side
                if (quantity > 0) {
                    buySide[price] += quantity;
                }
            } else if (side == "SELL") {
                // Match SELL order with BUY side
                auto it = buySide.begin(); // Start with the highest buy price
                while (it != buySide.end() && quantity > 0 && price <= it->first) {
                    int tradeQty = min(quantity, it->second); // Match the minimum quantity
                    totalTradedVolume += tradeQty;
                    quantity -= tradeQty;
                    it->second -= tradeQty;

                    // Remove the buy order if fully filled
                    if (it->second == 0) {
                        it = buySide.erase(it);
                    } else {
                        ++it;
                    }
                }

                // If any quantity is left, add to SELL side
                if (quantity > 0) {
                    sellSide[price] += quantity;
                }
            }
        } else if (type == "IOC") {
            // Immediate Or Cancel: Execute as much as possible, discard the rest
            if (side == "BUY") {
                auto it = sellSide.begin();
                while (it != sellSide.end() && quantity > 0 && price >= it->first) {
                    int tradeQty = min(quantity, it->second);
                    totalTradedVolume += tradeQty;
                    quantity -= tradeQty;
                    it->second -= tradeQty;

                    if (it->second == 0) {
                        it = sellSide.erase(it);
                    } else {
                        ++it;
                    }
                }
                // Remaining quantity is discarded
            } else if (side == "SELL") {
                auto it = buySide.begin();
                while (it != buySide.end() && quantity > 0 && price <= it->first) {
                    int tradeQty = min(quantity, it->second);
                    totalTradedVolume += tradeQty;
                    quantity -= tradeQty;
                    it->second -= tradeQty;

                    if (it->second == 0) {
                        it = buySide.erase(it);
                    } else {
                        ++it;
                    }
                }
                // Remaining quantity is discarded
            }
        } else if (type == "FOK") {
            // Fill Or Kill: Execute fully or discard entirely
            bool canBeFilled = true;
            int tempQty = quantity;

            if (side == "BUY") {
                auto it = sellSide.begin();
                while (it != sellSide.end() && tempQty > 0 && price >= it->first) {
                    tempQty -= it->second;
                    ++it;
                }
                if (tempQty > 0) canBeFilled = false;

                // If fully fillable, execute the order
                if (canBeFilled) {
                    auto it = sellSide.begin();
                    while (it != sellSide.end() && quantity > 0 && price >= it->first) {
                        int tradeQty = min(quantity, it->second);
                        totalTradedVolume += tradeQty;
                        quantity -= tradeQty;
                        it->second -= tradeQty;

                        if (it->second == 0) {
                            it = sellSide.erase(it);
                        } else {
                            ++it;
                        }
                    }
                }
            } else if (side == "SELL") {
                auto it = buySide.begin();
                while (it != buySide.end() && tempQty > 0 && price <= it->first) {
                    tempQty -= it->second;
                    ++it;
                }
                if (tempQty > 0) canBeFilled = false;

                // If fully fillable, execute the order
                if (canBeFilled) {
                    auto it = buySide.begin();
                    while (it != buySide.end() && quantity > 0 && price <= it->first) {
                        int tradeQty = min(quantity, it->second);
                        totalTradedVolume += tradeQty;
                        quantity -= tradeQty;
                        it->second -= tradeQty;

                        if (it->second == 0) {
                            it = buySide.erase(it);
                        } else {
                            ++it;
                        }
                    }
                }
            }
        }
    }

    // Output the total traded volume
    cout << totalTradedVolume << endl;

    return 0;
}
