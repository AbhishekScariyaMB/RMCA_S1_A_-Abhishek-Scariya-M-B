#include<stdio.h>
int main()
{
   int a[20],b[20],c[40],i,j,k,m,n;
   printf("enter how many value in A List\n");
   scanf("%d",&m);
   printf("Enter %d value in sorted order \n",m);
   for(i=0;i<m;i++)
scanf("%d",&a[i]);
   printf("enter how many value in B List\n");
   scanf("%d",&n);
   printf("Enter %d value in sorted order \n",n);
   for(i=0;i<n;i++)
scanf("%d",&b[i]);
 
   /* Merge sort logic */
   i=j=k=0;
   /* Compare  A and B List */
   while(i<m&&j<n)
   if(a[i]>=b[j])
      c[k++]= b[j++];
   else
      c[k++]=a[i++];
   /* Remaining Element of A List */
   while(i<m)
      c[k++]=a[i++];
  /* Remaining Element of b List */
   while(j<n)
      c[k++]= b[j++];
   printf("\nA list is :\n");
   for(i=0;i<m;i++)
     printf("%5d",a[i]);
   printf("\nB list is :\n");
   for(i=0;i<n;i++)
     printf("%5d",b[i]);
   printf("\nC list is :\n");
   for(i=0;i<m+n;i++)
     printf("%5d",c[i]);
     
 return 0;
}
