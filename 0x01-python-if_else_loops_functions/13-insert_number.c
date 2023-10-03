#include "lists.h"
/**
 *insert_node - Function
 *
 *@head: input
 *@number: input
 *Return: listint_t
 */
listint_t *insert_node(listint_t *head, int number)
{
	listint_t *tmp, *new, *node;

	tmp = *head;
	new = malloc(sizeof(listint_t))
	if (!new)
	{
		return (NULL);
	}
	new->n = number;
	if (tmp == NULL || tmp->n > number)
	{
		new->next = tmp;
		tmp = new;
	}
	else
	{
		while (tmp->next && tmp->next->n < number)
		{
			tmp = tmp->next;
		}
		node = tmp->next;
		tmp->next = new;
		new->next = node;
	}
	return (*head);
}
