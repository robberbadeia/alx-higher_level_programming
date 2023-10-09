#include "lists.h"
/**
 *is_palindrom: Function to Check weather the list is palindrom 
 * or not
 * @head: input
 * 
 *Return: 1 if palindrom 0 else 
*/
int is_palindrome(listint_t **head)
{
	int c = 0;
	int i = 0, j;
	listint_t *tmp, *f, *r;

	if (!head)
		return (0);
	if (!*head)
		return (0);
	
	tmp = *head;
	while (tmp)
	{
		tmp = tmp->next;
		c++;
	}
	if (c % 2 == 0)
	{
		/**
		 *Even Case
		 */
		for (j = 0; j <= (c / 2) - 1; j++)
		{
			r = r->next;
			f = f->next;
		}
		r = r->next;
		if (f->n != r->n)
		{
			return (0);
		}
		else
		{
			i = 0;
			while (i < (c / 2) - 1)
			{
				for (j = 0; j < i; j++)
				{
					f = f->next;
				}
				for (j = 0; j < c - (1 + i); j++)
				{
					r = r->next;
				}
				if (f->n != r->n)
				{
					return (0);
				}
				else
				{
					i++;
				}
			}
		}

	}
	if (c % 2 != 0)
	{
		/**
		 *Odd Case
		 */
		while (i != c / 2)
		{
			f = r = *head;
			for (j = 0; j < i; j++)
			{
				f = f->next;
			}
			for (j = 0; j < c - (i + 1); j++)
			{
				r = r->next;
			}
			if (f->n != r->n)
			{
				return (0);
			}
			else
			{
				i++;
			}
		}
		return (1);
	}
}
