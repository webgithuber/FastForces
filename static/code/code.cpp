#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin>>t;
	while(t--){
	int n;
	cin>>n;
	int a[n],b[n];
	for (int i =0;i<n;i++){
		cin>>a[i];
		b[i]=a[i];
	}
	sort(b,b+n);
	for (int j=0;j<n;j++){
		if (a[j]!=b[n-1]) cout<<(a[j]-b[n-1])<<" ";
		else cout<<(a[j]-b[n-2])<<" ";
	}
	cout<<endl;
}
	return 0;
}