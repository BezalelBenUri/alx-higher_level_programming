#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr, *fast_ptr, *prev_slow_ptr;
	listint_t *second_half, *mid_node;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);

	slow_ptr = *head;
	fast_ptr = *head;
	prev_slow_ptr = *head;
	mid_node = NULL;

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		prev_slow_ptr = slow_ptr;
		slow_ptr = slow_ptr->next;
	}

	if (fast_ptr != NULL)
	{
		mid_node = slow_ptr;
		slow_ptr = slow_ptr->next;
	}

	second_half = slow_ptr;
	prev_slow_ptr->next = NULL;
	reverse_list(&second_half);
	is_palindrome = compare_lists(*head, second_half);
	reverse_list(&second_half);

	if (mid_node != NULL)
	{
		prev_slow_ptr->next = mid_node;
		mid_node->next = second_half;
	}
	else
		prev_slow_ptr->next = second_half;
	return (is_palindrome);
}

/**
 * reverse_list - reverses a singly linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev_node, *current_node, *next_node;

	prev_node = NULL;
	current_node = *head;

	while (current_node != NULL)
	{
		next_node = current_node->next;
		current_node->next = prev_node;
		prev_node = current_node;
		current_node = next_node;
	}

	*head = prev_node;

	return (*head);
}

/**
 * compare_lists - compares two singly linked lists for equality
 * @list1: pointer to the head of the first list
 * @list2: pointer to the head of the second list
 * Return: 0 if not equal, 1 if equal
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);

		list1 = list1->next;
		list2 = list2->next;
	}
	if (list1 == NULL && list2 == NULL)
		return (1);
	else
		return (0);
}
