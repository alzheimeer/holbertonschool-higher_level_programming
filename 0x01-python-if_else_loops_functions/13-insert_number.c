#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert
 * Return: If fails - NULL Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *head2;

	head2 = *head;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->n = number;

	if (head2->n > newnode->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	else if (*head == NULL)
	{
		newnode->next = NULL;
		*head = newnode;
		return (newnode);
	}
	while (head2->next != NULL)
	{
		if (head2->next->n > newnode->n || head2->n  == newnode->n)
		{
			newnode->next = head2->next;
			head2->next = newnode;
			return (newnode);
		}
		head2 = head2->next;
	}
	newnode->next = head2->next;
	head2->next = newnode;
	return (newnode);
}
