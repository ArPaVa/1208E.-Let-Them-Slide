#include <iostream>
#include <deque>

long long n, w, length, blank, k, r, l;
const long long N = 1e6 + 6;

long long results[N], row[N];

int main() {
    std::cin >> n >> w;
    
    for (long long i = 0; i < n; i++) {
        
        std::cin >> length;

        for (long long j = 1; j <= length; j++) {
            std::cin >> row[j];
        }

        blank = w - length;
        k = length - blank;

        std::deque<int> q;
        q.push_back(0);

		row[length + 1] = 0;

        int l = 1, r = 1;

        for (r = 1; r <= w; r++) {
            if (r <= length + 1) {
                while (!q.empty() && row[q.back()] <= row[r]) {
                    q.pop_back();
                }
                q.push_back(r);
            }

            if (r - blank > q.front()) {
                q.pop_front();
            }

            int max = row[q.front()];
            results[r] += max;

			if (w > length*2 && r == length+1) {
				results[blank+1] -= max;
                r = blank;
            }
			else results[r+1] -= max;
        }
    }

    for (int i = 1; i <= w; i++) {
        printf("%lld ", results[i] += results[i-1]);
    }

    return 0;
}