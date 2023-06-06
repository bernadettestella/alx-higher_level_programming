#include "lists.h"

/**
  * check_cycle - checks if a list contains a cycle
  * @list: the singly list to be checked
  *
  * Return: returns 1 if there is a cycle else 0
  */

int check_cycle(listint_t *list)
{
	listint_t *birds = list;
	listint_t *bees = list;

	if (!list)
		return (0);

	while (birds && bees && bees->next)
	{
		birds = birds->next;
		bees = bees->next->next;
		if (birds == bees)
			return (1);
	}

	return (0);
}
