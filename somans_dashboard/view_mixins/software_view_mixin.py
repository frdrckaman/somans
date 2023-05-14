from django.conf import settings
import pandas as pd


class SoftwareListboardView:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            no_server=self.get_server_installed_software,
            no_workstation=self.get_workstation_installed_software,
            total_server_server=self.get_total_server_installed_software,
            total_software_server=self.get_total_workstation_installed_software,
            total_installed_software=self.get_total_installed_software,
            headcount=self.get_data_headcount,
            computer_manufacturer=self.get_computer_manufacturer,
            count_brand=self.get_count_brand,
            workstation_list=self.get_data_workstation_list,
            workstation_list_unique=self.get_data_workstation_list_unique,
            server_list=self.get_data_server_list,
            server_list_unique=self.get_data_server_list_unique,
            duplicate_server_name=self.get_data_server_list - self.get_data_server_list_unique,
            duplicate_workstation_name=self.get_data_workstation_list -
                                       self.get_data_workstation_list_unique,
            server_difference=abs(self.get_server_installed_software -
                                  self.get_data_server_list_unique),
            workstation_difference=abs(self.get_workstation_installed_software -
                                       self.get_data_workstation_list_unique),
        )
        return context

    @property
    def get_data_workstation_installed_software(self):
        df1 = pd.read_sql('select * from software_workstation', settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['computer_name'])
        return df11

    @property
    def get_data_server_installed_software(self):
        df2 = pd.read_sql('select * from software_server', settings.SOMANS_ENGINE)
        df22 = df2.drop_duplicates(['computer_name'])
        return df22

    @property
    def get_data_headcount(self):
        df2 = pd.read_sql('select * from headcount', settings.SOMANS_ENGINE)
        df22 = df2.drop_duplicates(['personnel_number'])
        return len(df22.index)

    @property
    def get_data_workstation_list(self):
        df1 = pd.read_sql('select * from list_of_workstations', settings.SOMANS_ENGINE)
        return len(df1.index)

    @property
    def get_data_workstation_list_unique(self):
        df1 = pd.read_sql('select * from list_of_workstations', settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['computer_name'])
        return len(df11.index)

    @property
    def get_data_server_list(self):
        df2 = pd.read_sql('select * from list_of_servers', settings.SOMANS_ENGINE)
        return len(df2.index)

    @property
    def get_data_server_list_unique(self):
        df2 = pd.read_sql('select * from list_of_servers', settings.SOMANS_ENGINE)
        df22 = df2.drop_duplicates(['computer_name'])
        return len(df22.index)

    @property
    def get_computer_manufacturer(self):
        data = []
        servers = self.get_data_server_installed_software
        workstations = self.get_data_workstation_installed_software
        workstation = workstations.drop_duplicates(['computer_manufacturer'])
        server = servers.drop_duplicates(['computer_manufacturer'])
        svr = server['computer_manufacturer'].values.tolist()
        wks = workstation['computer_manufacturer'].values.tolist()

        for s in svr:
            data.append(s)
        for w in wks:
            data.append(w)

        return pd.unique(data).tolist()

    @property
    def get_count_brand(self):
        count = []
        server = self.get_data_server_installed_software
        workstation = self.get_data_workstation_installed_software
        for brand in self.get_computer_manufacturer:
            wks = workstation.loc[workstation['computer_manufacturer'] == brand,
            'computer_manufacturer']
            svr = server.loc[server['computer_manufacturer'] == brand,
            'computer_manufacturer']
            count.append(len(wks) + len(svr))
        return count
    @property
    def get_total_workstation_installed_software(self):
        df1 = pd.read_sql('select * from software_workstation', settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['product_name'])
        return len(df11.index)

    @property
    def get_total_server_installed_software(self):
        df2 = pd.read_sql('select * from software_server', settings.SOMANS_ENGINE)
        df22 = df2.drop_duplicates(['product_name'])
        return len(df22.index)

    @property
    def get_total_installed_software(self):
        total = self.get_total_workstation_installed_software + self.get_total_server_installed_software
        return total
    @property
    def get_server_installed_software(self):
        return len(self.get_data_server_installed_software.index)

    @property
    def get_workstation_installed_software(self):
        return len(self.get_data_workstation_installed_software.index)

