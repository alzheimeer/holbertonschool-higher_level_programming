#include "lists.h"
/**
 * is_palindrome - check if is palindrome
 * @head: list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux1 = *head, *aux2 = *head;
	int c = 0, n = 0, i = 0, j = 0;

	if (head == NULL && *head == NULL)
		return (1);
	while (aux2->next)
	{
		aux2 = aux2->next;
		c++;
	}
	n = (c + 1) / 2;
	for (i = 0; i < n; i++)
	{
		j = 0;
		if (aux1->n != aux2->n)
			return (0);
		aux2 = *head;
		aux1 = aux1->next;
		c--;
		while (j < c)
		{
			aux2 = aux2->next;
			j++;
		}
	}
	return (1);
}
