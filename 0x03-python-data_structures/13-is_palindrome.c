#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome-function in C that checks if a singly linked list is a palindrome.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * @head:pointer to a head
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	listint_t *middle = slow;
	listint_t *current = middle->next;
	listint_t *prev = NULL;
	while (current != NULL)
	{
		listint_t *next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	listint_t *second_half = prev;
	listint_t *node1 = *head;
	listint_t *node2 = second_half;
	while (node1 != middle && node2 != NULL)
	{
		if (node1->n != node2->n)
		{
			return (0);
		}
		node1 = node1->next;
		node2 = node2->next;
	}
	return (1);
}
