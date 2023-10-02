#include "lists.h"

/**
 * check_cycle - checks if there's a cycle in a linked list
 * @list: list to check
 *
 * Return: 0 if no cycle, 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	if (!list)
		return (0);

	fast = list;
	slow = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
			return (1);
	}
	return (0);
}
