#include "lists.h"
#include <stdlib.h>
/**
 *insert_node-inserts a number into a sorted singly linked list
 *@number:numer to be added
 *@head:pointer to head
 *Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;
	if (current == NULL || number < current->n)
	{
		new_node->next = current;
		*head = new_node;
	}
	while (current->next != NULL && number > current->next->n)
	{
		current = current->next;
	}
	new_node->next  = current->next;
	current->next = new_node;
	return (new_node);
}
