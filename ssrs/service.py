import datetime
import sspyrs  # pip install sspyrs  (https://pypi.python.org/pypi/sspyrs/0.3)


class RdSsrs:
    def execute_report(self):
        base_execution_path = 'http://callwebprod.netwasatch.com/ReportServer/Pages/ReportViewer.aspx?'
        user = 'NETWASATCH\\RDReports'
        password = '*** The pw is found in 1Password ***'
        ssrs_directory = 'RentDynamicsReports'

        # A sample report that doesn't require inputs
        ssrs_report_name = 'ContactOutcome'
        parameters = None
        rpt = sspyrs.report('{0}%2f{1}%2f{2}&rs:Command=Render'.format(base_execution_path, ssrs_directory,
                                                                       ssrs_report_name),
                            user, password, parameters=parameters)
        download_filename = '{0}-{1}'.format(ssrs_report_name, datetime.date.today())
        rpt.directdown(download_filename, 'PDF')
        rpt.directdown(download_filename, 'EXCEL')

        # A sample report that requires inputs
        ssrs_report_name = 'CallCenterFollowUp'
        parameters = {'startDateTime': '2018-04-05', 'endDateTime': '2018-04-06'}
        rpt = sspyrs.report('{0}%2f{1}%2f{2}&rs:Command=Render'.format(base_execution_path, ssrs_directory,
                                                                       ssrs_report_name),
                            user, password, parameters=parameters)
        download_filename = '{0}-{1}'.format(ssrs_report_name, datetime.date.today())
        rpt.directdown(download_filename, 'PDF')
        rpt.directdown(download_filename, 'EXCEL')
