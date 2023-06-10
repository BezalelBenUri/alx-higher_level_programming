#include "lists.h"

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Double pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *mid = find_middle(*head);
	listint_t *second_half = reverse_list(mid);
	int is_palindrome = compare_lists(*head, second_half);

	reverse_list(second_half);

	return (is_palindrome);
}

/**
 * find_middle - Finds the middle node of a linked list
 * @head: Pointer to the head of the list
 *
 * Return: Pointer to the middle node
 */
listint_t *find_middle(listint_t *head)
{
	listint_t *slow = head;
	listint_t *fast = head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	return (slow);
}

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to the head of the list
 *
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * compare_lists - Compares two linked lists for equality
 * @list1: Pointer to the head of the first list
 * @list2: Pointer to the head of the second list
 *
 * Return: 1 if the lists are equal, 0 otherwise
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

