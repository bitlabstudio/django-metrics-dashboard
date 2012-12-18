"""Custom admin command that updates the data for all registered widgets."""
from django.core.management.base import BaseCommand

from metrics_dashboard.widget_pool import dashboard_widget_pool


class Command(BaseCommand):
    help = 'Updates the data for all registered widgets.'

    def handle(self, *args, **options):
        for widget_name, widget in dashboard_widget_pool.get_widgets().items():
            widget.update_widget_data()
            self.stdout.write('Successfully updated {0}\n'.format(
                widget.get_name()))
