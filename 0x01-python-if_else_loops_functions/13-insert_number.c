#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a note in a sorted linked list
 * @head: pointer to the head of the linked list
 * @number: number to insert
 *
 * Return: address of new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	current = *head;

	if (current == NULL)
		current = new;
	else
	{
		while(current)
		{
			if (current->n <= number && (current->next->n > number || current->next == NULL))
			{
				new->next = current->next;
				current->next = new;
				break;
			}
			current = current->next;
		}
	}
	return (new);
}
