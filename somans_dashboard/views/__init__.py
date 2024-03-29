from .software_dashboard_view import SoftwareDashboardView
from .server_dashboard_view import ServerDashboardView
from .workstation_dashboard_view import WorkstationDashboardView
from .new_software_workstation import NewWorkstationSoftwareView
from .new_software_server import NewServerSoftwareView
from .server_details_view import ServerDetailsView
from .workstation_details import WorkstationDetailsView
from .list_of_server import ListOfServerView
from .list_of_workstation import ListOfWorkstationView
from .server_list_vs_installed import ServerListVsInstalledView
from .workstation_list_vs_installed import WorkstationListVsInstalledView
from .list_workstation_duplicate import ListOfWorkstationDuplicateView
from .list_server_duplicate import ListOfServerDuplicateView
from .ls_wks_dup_details import ListWorkstationDuplicateDetailsView
from .ls_svr_dup_details import ListServerDuplicateDetailsView
from .headcount_view import HeadcountView
from .removed_sft_svr import RemovedSoftwareServerView
from .removed_sft_wks import RemovedSoftwareWorkstationView
from .nw_app_ls_svr import NewAppListServerView
from .nw_app_ls_wks import NewAppListWorkstationView
from .server_installed_vs_list import ServerInstalledVsListView
from .workstation_installed_vs_list import WorkstationInstalledVsListView
from .software_list import InstalledSoftwareView
from .svr_incomplete_dtls import IncompleteServerDetailsView
from .wks_incomplete_dtls import IncompleteWorkstationDetailsView
from .svr_wks_app_data import ServerSoftwareAppView
from .new_sft_dtls_svr import NewSoftwareServerDetailsView
from .new_sft_dtls_wks import NewSoftwareWorkstationDetailsView
from .svr_not_manage_sccm import ServerNotManageSccm
from .wks_not_manage_sccm import WorkstationNotManageSccm
from .grp_software_list import GroupSoftwareList
from .approve_software import ApproveSoftwareView
from .approve_new_software import ApproveSoftwareSvrWksView
from .theme_view import change_theme
from .error_404_view import handle_not_found, handle_server_error
from .welcome_view import WelcomeView


