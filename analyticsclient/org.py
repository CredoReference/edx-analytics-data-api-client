import analyticsclient.constants.data_format as DF


class Org(object):
    """ Org-related analytics. """

    def __init__(self, client, org_id):
        """
        Initialize the Org client.

        Arguments:

            client (analyticsclient.client.Client): The client to use to access remote resources.
            org_id (str): String identifying the org

        """
        self.client = client
        self.org_id = unicode(org_id)

    def problems_and_tags(self, data_format=DF.JSON):
        """
        Get the courses and the problems for the org with assigned tags.

        Arguments:
            data_format (str): Format in which data should be returned
        """
        path = 'orgs/{0}/problems_and_tags/'.format(self.org_id)
        return self.client.get(path, data_format=data_format)
