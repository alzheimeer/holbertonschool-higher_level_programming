int check_cycle(listint_t *list)
{
	listint_t *lento = list, *rap = list;

	if (list == NULL)
		return (0);
	while (lento && rap && rap->next)
	{
		lento = lento->next;
		rap = rap->next->next;

		if (lento == rap)
		{
			while (1)
			{
				lento = rap;
				while (rap->next != lento && rap->next != list)
					rap = rap->next;
				if (rap->next == list)
					break;
				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
