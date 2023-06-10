/*
 * File: 13-is_palindrome.c
  */

#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL;

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *mid = NULL;
	int isPalindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (isPalindrome);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	prev->next = NULL;
	reverse_listint(&slow);

	while (slow != NULL)
	{
		if (slow->n != (*head)->n)
		{
			isPalindrome = 0;
			break;
		}

		slow = slow->next;
		*head = (*head)->next;
	}

	reverse_listint(&mid);
	if (mid != NULL)
		prev->next = mid;
	else
		prev->next = slow;
	return (isPalindrome);
}
