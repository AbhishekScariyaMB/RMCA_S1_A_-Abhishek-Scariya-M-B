//This program has been written and submitted by 
//Abhishek Scariya M B [MCA-A]
#include<stdio.h>
#include<stdlib.h>
struct node
{
 int data;
 struct node *next;
 struct node *prev;
 }*head=NULL,*temp;
typedef struct node NODE; 
void Ins(int item)
{
 NODE* newnode=(NODE*)malloc(sizeof(NODE));
 newnode->data=item;
 newnode->next=head;
 newnode->prev=NULL;
 if(head!=NULL)
 head->prev=newnode;
 head=newnode;	
 }
void InsE(int item)
{  
 NODE *newnode=(NODE*)malloc(sizeof(NODE));
 newnode->data=item;
 newnode->next=NULL;
 temp=head;
 if(head!=NULL)
 {  	
  while(temp->next!=NULL)
  {
   temp=temp->next;
   }
   temp->next=newnode;
   newnode->prev=temp;
  }
 else
  {
   head=newnode;
   newnode->prev=NULL;	
  } 	 
 } 
 void InsB(int item,int key)
 {
  NODE *newnode=(NODE*)malloc(sizeof(NODE));
  newnode->data=item;
  if(head==NULL)
  {
   newnode->next=NULL;
   newnode->prev=NULL;
   head=newnode;
   return;
   }
   temp=head;
  while(temp->next!=NULL)
  {
   if(temp->data==key)
   {break;}	
   temp=temp->next;	
   }  
   if(temp->data!=key)
  {
   printf("\n\nNo such node exists! Insertion failed!");
   return;	
   }  
  newnode->next=temp;
  newnode->prev= temp->prev;
  temp->prev->next=newnode;
  temp->prev=newnode;
  } 
void InsA(int item,int key)
 {
  NODE *newnode=(NODE*)malloc(sizeof(NODE));
  newnode->data=item;
  if(head==NULL)
  {
   newnode->next=NULL;
   newnode->prev=NULL;
   head=newnode;
   return;
   }
   temp=head;
  while(temp->next!=NULL)
  {
   if(temp->data==key)
   break;	
   temp=temp->next;	
   } 
  if(temp->data!=key)
  {
   printf("\n\nNo such node exists! Insertion failed!");
   return;	
   } 
  newnode->next=temp->next;
  newnode->prev=temp;
  temp->next->prev=newnode;
  temp->next=newnode;
  }
void del()
{
 if(head==NULL)
 {
  printf("\n\nUNDERFLOW...!");
  return;	
  }
 temp=head; 
 if(temp->next!=NULL)
 {  
  head->next->prev=NULL;
  }
 head=head->next;
 printf("\n%d deleted!",temp->data);
 free(temp);  	
 }
void delE()
{
if(head==NULL)
 {
  printf("\n\nUNDERFLOW...!");
  return;	
  }
  temp=head;
  while(temp->next!=NULL)
  {
   temp=temp->next;
    }
  if(head->next!=NULL)
  temp->prev->next=NULL;
 printf("\n%d deleted!",temp->data);
 free(temp);  
 } 
void delS(int key)
{
 if(head==NULL)
 {
  printf("\n\nUNDERFLOW...!");
  return;	
  }
 temp=head;
 while(temp->next!=NULL)
 {
  if(temp->data==key)
  {
   break;	
   }
  temp=temp->next; 	
  }
 if(temp->data==key)
 {
  if(temp->next!=NULL)
   temp->next->prev=temp->prev;
   if(temp->prev!=NULL)
   temp->prev->next=temp->next;	
   printf("\n%d deleted!",temp->data);
   free(temp);
   return;	
  } 
 printf("\n\nNode not found, deletion failed!");  	
 }
void search(int key)
{
  if(head==NULL)
  printf("\nList Empty...!"); 
   int c=1; 
   temp=head;
  while(temp->next!=NULL)
  {
   if(temp->data==key)
   {
   	break;
    }	
   temp=temp->next;
   c++;	
   }
  if(temp->data==key) 
  {printf("\n%d found at node %d",key,c);
  return; } 
   printf("\n\nNo such node exists! Search failed!");
   return;	
   	
 }    
void display()
{
 if(head==NULL)
 {
  printf("\n\nList is empty!");
  return;	
  }
 temp=head;
 printf("\n\n");
 while(temp!=NULL)
  {
   printf("%d ->",temp->data);	
   temp=temp->next;
   } 	
 }  
void main()
{
 int ch,item,key;
 while(1)
 {
  printf("\n\n\nEnter choice to perform the following operations:-");
  printf("\n1.Insert at the beginning\t\t2.Insert at the end\n");
  printf("3.Insert before a node\t\t\t4.Insert after a node \n");
  printf("5.Delete first node\t\t\t6.Delete last node\n7.Delete specific node");
  printf("\t\t\t8.Search\n9.Display\t\t\t\t10.Exit\n\n");
  printf("Enter choice: ");  
  scanf("%d",&ch);
  switch(ch)
  {
   case 1: printf("\nEnter item to insert: ");
   		   scanf("%d",&item);	 
           Ins(item); 
   	       break;
   case 2: printf("\nEnter item to insert: ");
   		   scanf("%d",&item);	 
           InsE(item); 
   	       break;
   case 3: printf("\nEnter item to insert: ");
           scanf("%d",&item);
		   printf("\nEnter reference node value: ");
		   scanf("%d",&key);	       
		   InsB(item,key);
		   break;
   case 4: printf("\nEnter item to insert: ");
           scanf("%d",&item);
		   printf("\nEnter reference node value: ");
		   scanf("%d",&key);	       
		   InsA(item,key);
		   break;
   case 5: del();
           break;
   case 6: delE();
           break;		    		   
   case	7: printf("\nEnter node to be deleted: ");
           scanf("%d",&key);
		   delS(key);    
		   break;
   case 8: printf("\nEnter node to be searched: ");
           scanf("%d",&key);
		   search(key);    
		   break;		   
   case 9: display();
           break;
   case 10: printf("\n\nExit success!");
           exit(0);
   default:printf("\nInvalid choice !");             	 	   	    	 	   
   };
  }	
 }
