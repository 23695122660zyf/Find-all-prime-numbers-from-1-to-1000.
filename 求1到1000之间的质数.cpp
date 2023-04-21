#include <iostream>
using namespace std;

int main(){
	for (short i = 2;i<1000;i++){
		bool flag = true;
		for (short j = 2;j<i;j++){
			if (i % j == 0){
				flag = false;
				break;
			}
		}
		if (flag){
			cout << i << endl;
		}
	}
}
