from django.conf import settings
import pandas as pd


class SoftwareListboardView:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            data_workstation_installed_software=self.frd,
            frd=self.frd,
            list_workstation=self.workstation_list,
            list_server=self.server_list,
            data_server_installed_software=self.get_data_server_installed_software,
            no_server=self.get_server_installed_software,
            no_workstation=self.get_workstation_installed_software,
            total_server_server=self.get_total_server_installed_software,
            total_software_server=self.get_total_workstation_installed_software,
            total_installed_software=len(self.software_inst_svr_wks),
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
            workstation_difference=len(self.get_list_vs_workstation_installed_software),
            new_workstation_software=self.get_update_data_workstation_software,
            new_server_software=self.get_update_data_server_software,
            new_workstation_app=self.get_new_workstation_app,
            no_svr_not_manage_sccm=len(self.svr_not_manage_sccm)
        )
        return context

    @property
    def get_server_all(self):
        df1 = pd.read_sql("select * from list_of_servers", settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['computer_name'])
        return df11.to_dict('records')

    @property
    def get_workstation_all(self):
        df1 = pd.read_sql("select * from list_of_workstations", settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['computer_name'])
        return df11.to_dict('records')

    def get_server(self, name):
        df1 = pd.read_sql(f"select * from list_of_servers where computer_name='{name}'",
                          settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['computer_name'])
        return df11.to_dict('records')

    def get_workstation(self, name):
        df1 = pd.read_sql(f"select * from list_of_workstations where computer_name='{name}'",
                          settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['computer_name'])
        return df11.to_dict('records')

    def get_server_app(self, name):
        df1 = pd.read_sql(f"select * from software_server_new where computer_name='{name}'",
                          settings.SOMANS_ENGINE)
        # df11 = df1.drop_duplicates(['computer_name'])
        return df1.to_dict('records')

    def get_workstation_app(self, name):
        df1 = pd.read_sql(
            f"select * from software_workstation_new where computer_name='{name}'",
            settings.SOMANS_ENGINE)
        # df11 = df1.drop_duplicates(['computer_name'])
        return df1.to_dict('records')

    def get_server_new(self, name):
        df1 = pd.read_sql(f"select * from software_server_new where computer_name='{name}'",
                          settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['product_name'])
        return df11.to_dict('records')

    def get_workstation_new(self, name):
        df1 = pd.read_sql(
            f"select * from software_workstation_new where computer_name='{name}'",
            settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['product_name'])
        return df11.to_dict('records')

    def get_server_old(self, name):
        df1 = pd.read_sql(f"select * from software_server where computer_name='{name}'",
                          settings.SOMANS_ENGINE)
        # df11 = df1.drop_duplicates(['computer_name'])
        return df1

    def frd(self):
        df1 = pd.read_sql('select * from software_workstation_new', settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['computer_name'])
        return df11.to_dict('records')

    @property
    def workstation_list(self):
        df1 = self.get_data_workstation_installed_software
        df11 = self.get_workstation_list_data
        df_all = df1.merge(df11.drop_duplicates(), on=['computer_name', 'computer_name'],
                           how='left', indicator=True)
        df_all_1 = df_all[
            ['computer_name', 'computer_manufacturer', 'computer_model', 'user_name',
             'user_email',
             'operating_system', 'os_version', 'os_build_version', 'computer_ip_address',
             'managed_in_sccm']]
        df_all_2 = df_all_1.fillna('')
        return df_all_2.to_dict('records')

    @property
    def new_workstation_software_list(self):
        df1 = self.get_new_workstation_app
        df11 = self.get_workstation_list_data
        df_all = df1.merge(df11.drop_duplicates(), on=['computer_name', 'computer_name'],
                           how='left', indicator=True)
        df_all_1 = df_all[
            ['computer_name', 'computer_manufacturer', 'computer_model', 'product_name',
             'user_name', 'user_email',
             'operating_system', 'os_version', 'os_build_version', 'computer_ip_address',
             'managed_in_sccm']]
        df_all_2 = df_all_1.fillna('')
        return df_all_2.to_dict('records')

    @property
    def server_list(self):
        df2 = self.get_data_server_installed_software
        df22 = self.get_server_list_data
        df_all = df2.merge(df22.drop_duplicates(), on=['computer_name', 'computer_name'],
                           how='left', indicator=True)
        df_all_1 = df_all[
            ['computer_name', 'computer_manufacturer', 'computer_model', 'user_name',
             'operating_system', 'os_version', 'computer_ip_address', 'managed_in_sccm']]
        df_all_2 = df_all_1.fillna('')
        return df_all_2.to_dict('records')

    @property
    def new_server_software_list(self):
        df2 = self.get_new_server_app
        df22 = self.get_server_list_data
        df_all = df2.merge(df22.drop_duplicates(), on=['computer_name', 'computer_name'],
                           how='left', indicator=True)
        df_all_1 = df_all[
            ['computer_name', 'computer_manufacturer', 'computer_model', 'user_name',
             'product_name',
             'operating_system', 'os_version', 'computer_ip_address', 'managed_in_sccm']]
        df_all_2 = df_all_1.fillna('')
        return df_all_2.to_dict('records')

    def new_app_server(self, name):
        df4 = self.get_server_new(name)
        df5 = self.get_server_new(name)
        df44 = df4[
            ['computer_name', 'computer_manufacturer', 'computer_model', 'product_name']]
        df55 = df5[
            ['computer_name', 'computer_manufacturer', 'computer_model', 'product_name']]
        print(len(df44))
        print(len(df55))
        df555 = pd.concat([df44, df55]).drop_duplicates(keep=False)
        return df555.to_dict('records')

    @property
    def get_data_workstation_installed_software(self):
        df1 = pd.read_sql('select * from software_workstation_new', settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['computer_name'])
        return df11

    @property
    def get_update_data_workstation_installed_software(self):
        df1 = pd.read_sql('select * from software_workstation', settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['computer_name'])
        return df11

    @property
    def get_update_data_workstation_software(self):
        num = self.get_total_workstation_installed_software - self.get_total_update_workstation_installed_software
        return num

    @property
    def get_data_server_installed_software(self):
        df2 = pd.read_sql('select * from software_server_new', settings.SOMANS_ENGINE)
        df22 = df2.drop_duplicates(['computer_name'])
        return df22

    @property
    def get_update_data_server_installed_software(self):
        df2 = pd.read_sql('select * from software_server', settings.SOMANS_ENGINE)
        df22 = df2.drop_duplicates(['computer_name'])
        return df22

    @property
    def get_workstation_list_data(self):
        df1 = pd.read_sql('select * from list_of_workstations', settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['computer_name'])
        return df11

    @property
    def get_server_list_data(self):
        df1 = pd.read_sql('select * from list_of_servers', settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['computer_name'])
        return df11

    @property
    def get_update_data_server_software(self):
        num = self.get_total_server_installed_software - self.get_total_update_server_installed_software
        return num

    @property
    def get_update_data_server_installed_software(self):
        df2 = pd.read_sql('select * from software_server', settings.SOMANS_ENGINE)
        df22 = df2.drop_duplicates(['computer_name'])
        return df22

    @property
    def get_data_headcount(self):
        df2 = pd.read_sql('select * from headcount', settings.SOMANS_ENGINE)
        df22 = df2.drop_duplicates(['personnel_number'])
        return len(df22.index)

    @property
    def headcount_data(self):
        df2 = pd.read_sql('select * from headcount', settings.SOMANS_ENGINE)
        df22 = df2.drop_duplicates(['personnel_number'])
        return df22.to_dict('records')

    @property
    def get_data_workstation_list(self):
        df1 = pd.read_sql('select * from list_of_workstations', settings.SOMANS_ENGINE)
        return len(df1.index)

    @property
    def get_workstation_list_all(self):
        df1 = pd.read_sql('select * from list_of_workstations', settings.SOMANS_ENGINE)
        return df1

    @property
    def get_server_list_all(self):
        df1 = pd.read_sql('select * from list_of_servers', settings.SOMANS_ENGINE)
        return df1

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
    def get_new_workstation_app(self):
        df111 = self.get_total_installed_software_workstation
        df222 = self.get_total_update_installed_software_workstation
        df44 = df111[
            ['computer_name', 'computer_manufacturer', 'computer_model', 'product_name']]
        df55 = df222[
            ['computer_name', 'computer_manufacturer', 'computer_model', 'product_name']]
        return pd.concat([df44, df55]).drop_duplicates(keep=False)

    @property
    def get_new_server_app(self):
        df4 = self.get_total_installed_software_server
        df5 = self.get_total_update_installed_software_server
        df44 = df4[
            ['computer_name', 'computer_manufacturer', 'computer_model', 'product_name']]
        df55 = df5[
            ['computer_name', 'computer_manufacturer', 'computer_model', 'product_name']]
        return pd.concat([df44, df55]).drop_duplicates(keep=False)

    @property
    def get_total_workstation_installed_software(self):
        df1 = pd.read_sql('select * from software_workstation_new', settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['product_name'])
        return len(df11.index)

    @property
    def get_total_update_workstation_installed_software(self):
        df1 = pd.read_sql('select * from software_workstation', settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['product_name'])
        return len(df11.index)

    @property
    def get_total_installed_software_workstation(self):
        df1 = pd.read_sql('select * from software_workstation_new', settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['product_name'])
        return df11

    @property
    def get_total_update_installed_software_workstation(self):
        df1 = pd.read_sql('select * from software_workstation', settings.SOMANS_ENGINE)
        df11 = df1.drop_duplicates(['product_name'])
        return df11

    @property
    def get_total_server_installed_software(self):
        df2 = pd.read_sql('select * from software_server_new', settings.SOMANS_ENGINE)
        df22 = df2.drop_duplicates(['product_name'])
        return len(df22.index)

    @property
    def get_total_update_server_installed_software(self):
        df2 = pd.read_sql('select * from software_server', settings.SOMANS_ENGINE)
        df22 = df2.drop_duplicates(['product_name'])
        return len(df22.index)

    @property
    def get_total_installed_software_server(self):
        df2 = pd.read_sql('select * from software_server_new', settings.SOMANS_ENGINE)
        df22 = df2.drop_duplicates(['product_name'])
        return df22

    @property
    def get_total_update_installed_software_server(self):
        df6 = pd.read_sql('select * from software_server', settings.SOMANS_ENGINE)
        df66 = df6.drop_duplicates(['product_name'])
        return df66

    @property
    def get_total_installed_software(self):
        total = self.get_total_workstation_installed_software + self.get_total_server_installed_software
        return total

    @property
    def get_server_installed_software(self):
        return len(self.get_data_server_installed_software.index)

    @property
    def get_server_update_installed_software(self):
        return len(self.get_update_data_server_installed_software.index)

    @property
    def get_workstation_installed_software(self):
        return len(self.get_data_workstation_installed_software.index)

    @property
    def get_workstation_update_installed_software(self):
        return len(self.get_update_data_workstation_installed_software.index)

    @property
    def get_list_vs_server_installed_software(self):
        df1 = self.get_server_list_data
        df2 = self.get_data_server_installed_software
        df11 = df1[['computer_name']]
        df22 = df2[['computer_name']]
        df = pd.concat([df11, df22]).drop_duplicates(keep=False)
        return df.to_dict('records')

    @property
    def get_list_vs_workstation_installed_software(self):
        df1 = self.get_workstation_list_data
        df2 = self.get_data_workstation_installed_software
        df11 = df1[['computer_name']].drop_duplicates()
        df22 = df2[['computer_name']].drop_duplicates()
        df = pd.concat([df11, df22]).drop_duplicates(keep=False)
        return df.to_dict('records')

    @property
    def get_duplicate_workstation_list(self):
        df = self.get_workstation_list_all
        df1 = df[['computer_name']]
        df11 = df1[df1.duplicated(keep=False)].drop_duplicates()

        df2 = pd.read_sql('select computer_name,computer_ip_address,managed_in_sccm, '
                          'user_name, user_last_logon_time_stamp, count(*) as occurrence from '
                          'list_of_workstations group by computer_name, computer_ip_address,user_name, managed_in_sccm, user_last_logon_time_stamp having count(*) > 1;',
                          settings.SOMANS_ENGINE)
        return df2.to_dict('records')

    @property
    def get_duplicate_server_list(self):
        df = self.get_server_list_all
        df1 = df[['computer_name']]
        df11 = df1[df1.duplicated(keep=False)].drop_duplicates()

        df2 = pd.read_sql('select computer_name,computer_ip_address,managed_in_sccm, '
                          'count(*) as occurrence from list_of_servers group by computer_name having count(*) > 1;',
                          settings.SOMANS_ENGINE)
        return df2.to_dict('records')

    def get_workstation_duplicate(self, name):
        df1 = pd.read_sql(f"select * from list_of_workstations where computer_name='{name}'",
                          settings.SOMANS_ENGINE)
        return df1.to_dict('records')

    def get_server_duplicate(self, name):
        df1 = pd.read_sql(f"select * from list_of_servers where computer_name='{name}'",
                          settings.SOMANS_ENGINE)
        return df1.to_dict('records')

    @property
    def removed_software_server(self):
        df = pd.read_sql(
            "select a.* from  software_server a left join software_server_new b on a.product_name = b.product_name where b.product_name is null",
            settings.SOMANS_ENGINE)
        return df

    @property
    def removed_sft_server(self):
        df2 = self.removed_software_server
        df22 = self.get_server_list_data
        df_all = df2.merge(df22.drop_duplicates(), on=['computer_name', 'computer_name'],
                           how='left', indicator=True)
        df_all_1 = df_all[
            ['computer_name', 'computer_manufacturer', 'computer_model', 'user_name',
             'product_name',
             'operating_system', 'os_version', 'computer_ip_address', 'managed_in_sccm']]
        df_all_2 = df_all_1.fillna('')
        return df_all_2.to_dict('records')

    @property
    def no_removed_sft_server(self):
        df2 = self.removed_software_server
        df22 = df2.drop_duplicates('product_name')
        return len(df22)

    @property
    def new_software_server(self):
        df = pd.read_sql(
            "select a.* from  software_server_new a left join software_server b on a.product_name = b.product_name where b.product_name is null",
            settings.SOMANS_ENGINE)
        return df

    @property
    def new_software_server_app(self):
        df = pd.read_sql(
            "select a.* from  software_server_new a left join software_server b on a.product_name = b.product_name where b.product_name is null",
            settings.SOMANS_ENGINE)
        df2 = df.drop_duplicates('product_name')
        return df2.to_dict('records')

    @property
    def new_sft_server_dup(self):
        df2 = self.new_software_server_app_dup
        df22 = self.get_server_list_data
        df_all = df2.merge(df22.drop_duplicates(), on=['computer_name', 'computer_name'],
                           how='left', indicator=True)
        df_all_1 = df_all[
            ['computer_name', 'computer_manufacturer', 'computer_model', 'user_name',
             'product_name',
             'operating_system', 'os_version', 'computer_ip_address', 'managed_in_sccm']]
        df_all_2 = df_all_1.fillna('')
        return df_all_2.to_dict('records')

    @property
    def new_software_server_app_dup(self):
        df = pd.read_sql(
            "select a.* from  software_server_new a left join software_server b on a.product_name = b.product_name where b.product_name is null",
            settings.SOMANS_ENGINE)
        # df2 = df.drop_duplicates('product_name')
        return df

    @property
    def new_software_workstation_app_dup(self):
        df = pd.read_sql(
            "select a.* from  software_workstation_new a left join software_workstation b on a.product_name = b.product_name where b.product_name is null",
            settings.SOMANS_ENGINE)
        # df2 = df.drop_duplicates('product_name')
        return df

    @property
    def new_sft_workstation_dup(self):
        df2 = self.new_software_workstation_app_dup
        df22 = self.get_workstation_list_data
        df_all = df2.merge(df22.drop_duplicates(), on=['computer_name', 'computer_name'],
                           how='left', indicator=True)
        df_all_1 = df_all[
            ['computer_name', 'computer_manufacturer', 'computer_model', 'user_name',
             'product_name',
             'operating_system', 'os_version', 'computer_ip_address', 'managed_in_sccm']]
        df_all_2 = df_all_1.fillna('')
        return df_all_2.to_dict('records')


    def get_new_software_server_app(self, name):
        df = pd.read_sql(
            f"select a.* from  software_server_new a where a.product_name ='{name}'",
            settings.SOMANS_ENGINE)
        return df

    # @property
    # def new_sft_server(self):
    #     df2 = self.new_software_server
    #     df22 = self.get_server_list_data
    #     df_all = df2.merge(df22.drop_duplicates(), on=['computer_name', 'computer_name'],
    #                        how='left', indicator=True)
    #     df_all_1 = df_all[
    #         ['computer_name', 'computer_manufacturer', 'computer_model', 'user_name',
    #          'product_name',
    #          'operating_system', 'os_version', 'computer_ip_address', 'managed_in_sccm']]
    #     df_all_2 = df_all_1.fillna('')
    #     return df_all_2.to_dict('records')


    def new_sft_server(self , name):
        df2 = self.get_new_software_server_app(name)
        df22 = self.get_server_list_data
        df_all = df2.merge(df22.drop_duplicates(), on=['computer_name', 'computer_name'],
                           how='left', indicator=True)
        df_all_1 = df_all[
            ['computer_name', 'computer_manufacturer', 'computer_model', 'user_name',
             'product_name',
             'operating_system', 'os_version', 'computer_ip_address', 'managed_in_sccm']]
        df_all_2 = df_all_1.fillna('')
        return df_all_2.to_dict('records')

    @property
    def no_new_sft_server(self):
        df2 = self.new_software_server
        df22 = df2.drop_duplicates('product_name')
        return len(df22)

    @property
    def removed_software_workstation(self):
        df = pd.read_sql(
            "select a.* from  software_workstation a left join software_workstation_new b on a.product_name = b.product_name where b.product_name is null",
            settings.SOMANS_ENGINE)
        return df

    @property
    def removed_sft_workstation(self):
        df2 = self.removed_software_workstation
        df22 = self.get_workstation_list_data
        df_all = df2.merge(df22.drop_duplicates(), on=['computer_name', 'computer_name'],
                           how='left', indicator=True)
        df_all_1 = df_all[
            ['computer_name', 'computer_manufacturer', 'computer_model', 'user_name',
             'product_name',
             'operating_system', 'os_version', 'computer_ip_address', 'managed_in_sccm']]
        df_all_2 = df_all_1.fillna('')
        return df_all_2.to_dict('records')

    @property
    def no_removed_sft_workstation(self):
        df2 = self.removed_software_workstation
        df22 = df2.drop_duplicates('product_name')
        return len(df22)

    @property
    def new_software_workstation(self):
        df = pd.read_sql(
            "select a.* from  software_workstation_new a left join software_workstation b on a.product_name = b.product_name where b.product_name is null",
            settings.SOMANS_ENGINE)
        return df

    @property
    def new_software_workstation_app(self):
        df = pd.read_sql(
            "select a.* from  software_workstation_new a left join software_workstation b on a.product_name = b.product_name where b.product_name is null",
            settings.SOMANS_ENGINE)
        df2 = df.drop_duplicates('product_name')
        return df2.to_dict('records')

    def get_new_software_workstation_app(self, name):
        df = pd.read_sql(f"select a.* from  software_workstation_new a where a.product_name = '{name}'", settings.SOMANS_ENGINE)
        df2 = df.drop_duplicates('product_name')
        return df2

    # @property
    # def new_sft_workstation(self):
    #     df2 = self.new_software_workstation
    #     df22 = self.get_workstation_list_data
    #     df_all = df2.merge(df22.drop_duplicates(), on=['computer_name', 'computer_name'],
    #                        how='left', indicator=True)
    #     df_all_1 = df_all[
    #         ['computer_name', 'computer_manufacturer', 'computer_model', 'user_name',
    #          'product_name',
    #          'operating_system', 'os_version', 'computer_ip_address', 'managed_in_sccm']]
    #     df_all_2 = df_all_1.fillna('')
    #     return df_all_2.to_dict('records')

    def new_sft_workstation(self, name):
        df2 = self.get_new_software_workstation_app(name)
        df22 = self.get_workstation_list_data
        df_all = df2.merge(df22.drop_duplicates(), on=['computer_name', 'computer_name'],
                           how='left', indicator=True)
        df_all_1 = df_all[
            ['computer_name', 'computer_manufacturer', 'computer_model', 'user_name',
             'product_name',
             'operating_system', 'os_version', 'computer_ip_address', 'managed_in_sccm']]
        df_all_2 = df_all_1.fillna('')
        return df_all_2.to_dict('records')

    @property
    def no_new_sft_workstation(self):
        df2 = self.new_software_workstation
        df22 = df2.drop_duplicates('product_name')
        return len(df22)

    @property
    def software_ls_nt_inst_server(self):
        df = pd.read_sql(
            "select a.* from  list_of_servers a left join software_server_new b on a.computer_name = b.computer_name where b.computer_name is null",
            settings.SOMANS_ENGINE)
        return df

    @property
    def software_ls_nt_inst_server_dt(self):
        df2 = self.software_ls_nt_inst_server
        df22 = df2.drop_duplicates('computer_name')
        return df22.to_dict('records')

    @property
    def software_inst_ls_nt_ls_server(self):
        df = pd.read_sql(
            "select a.* from  software_server_new a left join list_of_servers b on a.computer_name = b.computer_name where b.computer_name is null",
            settings.SOMANS_ENGINE)
        return df

    @property
    def software_inst_ls_nt_ls_server_dt(self):
        df2 = self.software_inst_ls_nt_ls_server
        df22 = df2.drop_duplicates('computer_name')
        return df22.to_dict('records')

    @property
    def software_ls_nt_inst_workstation(self):
        df = pd.read_sql(
            "select a.* from  list_of_workstations a left join software_workstation_new b on a.computer_name = b.computer_name where b.computer_name is null",
            settings.SOMANS_ENGINE)
        return df

    @property
    def software_ls_nt_inst_workstation_dt(self):
        df2 = self.software_ls_nt_inst_workstation
        df22 = df2.drop_duplicates('computer_name')
        return df22.to_dict('records')

    @property
    def software_inst_ls_nt_ls_workstation(self):
        df = pd.read_sql(
            "select a.* from  software_workstation_new a left join list_of_workstations b on a.computer_name = b.computer_name where b.computer_name is null",
            settings.SOMANS_ENGINE)
        return df

    @property
    def software_inst_ls_nt_ls_workstation_dt(self):
        df2 = self.software_inst_ls_nt_ls_workstation
        df22 = df2.drop_duplicates('computer_name')
        return df22.to_dict('records')

    @property
    def software_inst_svr_wks(self):
        df = pd.read_sql(
            "select distinct (product_name) from software_server_new union select distinct ("
            "product_name) from software_workstation_new",
            settings.SOMANS_ENGINE)
        return df

    @property
    def get_software_inst_svr_wks(self):
        df = self.software_inst_svr_wks
        return df.to_dict('records')

    @property
    def svr_incomplete_details(self):
        df = pd.read_sql(
            "select * from list_of_servers where operating_system is null or os_version is "
            "null or days_computer_last_comms is null or managed_in_sccm is null",
            settings.SOMANS_ENGINE)
        return df

    @property
    def get_svr_incomplete_details(self):
        df = self.svr_incomplete_details
        return df.to_dict('records')

    @property
    def wks_incomplete_details(self):
        df = pd.read_sql(
            "select * from list_of_workstations where operating_system is null or os_version is null  or days_computer_last_comms is null or managed_in_sccm is null or user_name is null or user_email is null or  user_last_logon_time_stamp is null or last_hardware_inventory is null",
            settings.SOMANS_ENGINE)
        return df

    @property
    def get_wks_incomplete_details(self):
        df = self.wks_incomplete_details
        return df.to_dict('records')


    def svr_wks_app_data(self, app):
        df = pd.read_sql(
            f"select * from software_server_new where product_name = '{app}' union select * from software_workstation_new where product_name = '{app}'",
            settings.SOMANS_ENGINE)
        return df

    @property
    def svr_wks_list(self):
        df = pd.read_sql(
            f"select computer_name, user_name, operating_system, os_version, computer_ip_address, managed_in_sccm from list_of_servers union select computer_name, user_name, operating_system,os_version, computer_ip_address, managed_in_sccm from list_of_workstations", settings.SOMANS_ENGINE)
        return df

    def svr_wks_list_data(self, app):
        df1 = self.svr_wks_app_data(app)
        df2 = self.svr_wks_list
        df = df1.merge(df2.drop_duplicates(), on=['computer_name', 'computer_name'], how='left', indicator=True)
        return df.to_dict('records')

    @property
    def svr_not_manage_sccm(self):
        df = pd.read_sql(
            "select * from list_of_servers where managed_in_sccm is null or managed_in_sccm = 'No'",
            settings.SOMANS_ENGINE)
        return df.to_dict('records')

    @property
    def wks_not_manage_sccm(self):
        df = pd.read_sql(
            "select * from list_of_workstations where managed_in_sccm is null or managed_in_sccm = 'No'",
            settings.SOMANS_ENGINE)
        return df.to_dict('records')
