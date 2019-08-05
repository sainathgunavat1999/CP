#include<stdio.h>
void printArray();
int f;
void main(){
int a[100][100];
int n;
int i,j;
int rowI[100];
int colI[100];
int value[100];
int count = 0;
printf("Enter size of Matrix:\n");
scanf("%d",&n);
printf("Enter Element of Sparse maTrix:\n");
for(i=0;i<n;i++){
    for(j=0;j<n;j++){
scanf("%d",&a[i][j]);
    }
}

for(i=0;i<n;i++){
    for(j=0;j<n;j++){
     if(a[i][j] != 0){
    rowI[count] = i;
    colI[count] = j;
    value[count] = a[i][j];
    count = count + 1;
     }
    }
}


printf("Index of ROW where NoN Zero element is LOCATED:\n");
printArray(rowI,count);
printf("Index of column where NoN Zero element is LOCATED:\n");
printArray(colI,count);
printf("Non Zero Value:\n");
printArray(value,count);



}

void printArray(int a[100],int c){

for(f=0;f<c;f++){
printf("%d\n",a[f]);
}

}