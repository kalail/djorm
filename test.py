from djorm import setup_database, models, table, run_query


# Setup database settings
setup_database(name='simple.db', engine='sqlite')


# Declare model
class Message(models.Model):
    subject = models.TextField()

    @table('messages')
    class Meta:
        pass


# Create table
run_query('create_table.sql')

# Create rows
create_row = lambda: Message.objects.create(subject='haha')
repeat = lambda func, n: (func() for i in range(n))
list(repeat(create_row, 10))

# Fetch rows
msgs = Message.objects.filter(subject='haha')
assert len(msgs) == 10
to_is_correct = lambda msg: msg.subject == 'haha'
assert all(map(to_is_correct, msgs))

# Empty table
run_query('delete_rows.sql')

# Check rows
assert Message.objects.count() == 0
