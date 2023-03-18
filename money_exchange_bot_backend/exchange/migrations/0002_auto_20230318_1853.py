from django.db import migrations


class Migration(migrations.Migration):

    def default_banned_user(self, schema_editor):
        """Create default banned user"""
        banned_user = self.get_model('exchange', 'User')
        banned_user.objects.create(
            id=0,
            username='Banned',
            role='Banned',
        )

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(default_banned_user),
    ]
