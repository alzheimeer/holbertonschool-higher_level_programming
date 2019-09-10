#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - find the loop
 * @list: first element a list
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
  listint_t *slow = list, *fast = list;

  if (list == NULL)
    return (0);

  while (slow && fast && fast->next)
    {
      slow = slow->next;
      fast = fast->next->next;

      if (slow == fast)
	{
	  return (1);
	}

    }
  return (0);

}
