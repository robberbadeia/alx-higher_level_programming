#include "lists.h"
/**
 *check_cycle - Function
 *
 *@list: input
 *
 *Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_p, *fast_p;

	if (!list)
		return (0);

	slow_p = fast_p = list;
	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;

		if (slow_p == fast_p)
			return (1);
	}
	return (0);
}
