#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a new node into a sotred linked list
 *
 * @head: the address to the head of the linked list
 *
 * @number: the number that the new node would hold
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *first, *new, *prev, *next;

	if (!head)
		return (NULL);
	first = *head;
	prev = NULL;
	next = first;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	while (next)
	{
		if (next->n >= number)
			break;
		prev = next;
		next = next->next;
	}
	if (prev)
	{
		prev->next = new;
		new->next = next;
	}
	else
	{
		*head = new;
		new->next = first;
	}
	return (new);
}
