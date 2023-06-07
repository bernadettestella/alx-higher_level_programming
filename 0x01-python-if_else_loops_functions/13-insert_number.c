#include "lists.h"

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: the head of the linked list
 * @number: data in the new node
 * Return: address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *beginning;

	beginning = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || beginning->n > new->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (beginning->next != NULL)
	{
		if ((beginning->next->n > new->n && beginning->n < new->n)
			|| new->n == beginning->n)
		{
			new->next = beginning->next;
			beginning->next = new;
			return (new);
		}
		beginning = beginning->next;
	}
	new->next = beginning->next;
	beginning->next = new;
	return (new);
}
