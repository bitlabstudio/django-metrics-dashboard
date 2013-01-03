"""Custom admin command that updates the data for all registered widgets."""
from django.core.management.base import BaseCommand

from django_libs.decorators import lockfile

from metrics_dashboard.widget_pool import dashboard_widget_pool


class Command(BaseCommand):
    help = 'Updates the data for all registered widgets.'

    @lockfile('update_widget_data')
    def handle(self, *args, **options):
        for widget_name, widget in dashboard_widget_pool.get_widgets().items():
            if widget.should_update():
                widget.update_widget_data()
                widget.set_last_update()
                message = 'Successfully updated {0}\n'
            else:
                message = 'No update needed for {0}\n'
            self.stdout.write(message.format(widget.get_name()))
