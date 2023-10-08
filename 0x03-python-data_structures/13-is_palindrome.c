#include "lists.h"

/**
 * move - move pointers to position
 * @len: length
 * @forward: pointer
 * @backward: pointer
 */

void move(int len, listint_t **forward, listint_t **backward)
{
	int i;

	for (i = 1; i < (len / 2); i++)
	{
		*forward = (*forward)->next;
		*backward = (*backward)->next;
	}
	if (len % 2 == 0)
		*forward = (*forward)->next;
	else
		*forward = (*forward)->next->next;
}
/**
 * is_palindrome - Checks if a linkedlist is a palindrome
 * @head: entry point to the linkedlist
 *
 * Return: 0 if false, 1 if true
 */

int is_palindrome(listint_t **head)
{
	int len = 0, i, mid;
	listint_t *forward, *backward, *ptr;

	if (!head)
		return (0);
	if (!(*head))
		return (1);

	ptr = *head;

	while (ptr)
	{
		len += 1;
		ptr = ptr->next;
	}
	mid = len / 2;

	if (len == 1)
		return (1);
	forward = *head;
	backward = *head;

	move(len, &forward, &backward);

	while (mid > 0)
	{
		if (forward->n != backward->n)
			return (0);
		mid--;
		if (forward->next)
		{
			forward = forward->next;
			backward = *head;
			for (i = 1; i < mid; i++)
				backward = backward->next;
		}
	}
	return (1);
}
