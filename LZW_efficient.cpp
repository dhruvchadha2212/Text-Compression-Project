#include<bits/stdc++.h>
using namespace std;
struct node {
	char symbol;
	int dict_index;
	node* children[256];
};
vector<node*> root;
int main() {
	for(int i = 0; i < 256; i++) {
		node *temp = new node;
		temp->symbol = i;
		temp->dict_index = i;
		for(int j = 0; j < 256; j++) {
			temp->children[j] = NULL;
		}
		root.push_back(temp);
	}
	
	fstream readfile, writefile;
	writefile.open("write.bin", ios::binary|ios::out);
	readfile.open("medium.txt", ios::in);
	readfile>>noskipws;
	char a;
	node *currentnode;
	int nextindex = 256;
	if(readfile>>a) {
		currentnode = root[(int)a];
	}
	while(readfile>>a) {
		if(currentnode->children[(int)a])
			currentnode = currentnode->children[(int)a];
		else {
			node *temp = new node;
			temp->symbol = a;
			temp->dict_index = nextindex++;
			for(int j = 0; j < 256; j++) {
				temp->children[j] = NULL;
			}
			currentnode->children[(int)a] = temp;
			short int toprint = currentnode->dict_index;
			writefile.write((char*)&toprint, sizeof(toprint));
			currentnode = root[(int)a];
		}
	}
	short int toprint = currentnode->dict_index;
	writefile.write((char*)&toprint, sizeof(toprint));
	readfile.close();
	writefile.close();
}
