    node *cursor = list;
    while (cursor != NULL)
    {
        node *next = ptr->next;
        free(cursor);
        cursor = next;
    }
