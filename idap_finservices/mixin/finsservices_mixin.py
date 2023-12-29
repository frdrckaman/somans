from django.conf import settings
from django.views.generic import TemplateView
from idap_finservices.models import FinServicesProd, FinServicesUat


class FinServicesAdmin(TemplateView):
    txt_file = settings.FIN_SERVICE_FILE
    service_title = settings.FIN_SERVICE_NAME
    file_data = []
    service_start = settings.FIN_START_RANGE
    service_end = settings.FIN_END_RANGE
    fin_service = []
    fin_service_status = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.read_log_file()
        self.get_fin_services_status()
        fins_status_node1 = []
        fins_status_node2 = []
        for status1 in FinServicesProd.objects.filter(node=1).values():
            fins_status_node1 = [*status1.values()]
        for status2 in FinServicesProd.objects.filter(node=2).values():
            fins_status_node2 = [*status2.values()]
        context.update(
            s_status_node1=fins_status_node1,
            s_status_node2=fins_status_node2,
            service_title=self.service_title,
            service_time=self.show_service_time,
            fin_service_name=self.fin_service,
            fin_services_status=self.fin_service_status,
        )
        return context

    def read_log_file(self):
        with open(self.txt_file, 'r') as file:
            for file_line in file.readlines():
                self.file_data.append(file_line.replace(" ", ""))

    @property
    def get_file_data(self):
        return self.file_data

    @property
    def get_service_title(self):
        return self.service_title

    @property
    def get_service_status_time(self):
        service_log = self.get_file_data[2].split('|')
        return service_log[1].replace('FinacleServicesAdministration', '')

    @property
    def show_service_time(self):
        return f'{self.get_service_status_time[:3]} {self.get_service_status_time[3:6]}' \
               f' {self.get_service_status_time[6:8]} {self.get_service_status_time[8:16]} ' \
               f'{self.get_service_status_time[16:19]} {self.get_service_status_time[19:]}'

    def get_fin_services_status(self):
        self.fin_service = []
        self.fin_service_status = []
        # work on this to display service status for node1 and node2
        for fin in range(self.service_start, self.service_end):
            self.fin_service.append(self.fin_service_name(self.file_data[fin]))
            self.fin_service_status.append(self.fin_services_status(self.file_data[fin]))

    def fin_service_name(self, service_list):
        service = service_list.split('|')
        service_name = service[1].split('1m')
        return service_name[1]

    def fin_services_status(self, service_status):
        service = service_status.split('|')
        service_stat = service[3].split(';')
        return service_stat[1].replace('1m', '')
