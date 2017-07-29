import endpoints
from google.appengine.api import oauth
from protorpc import remote

from models import Volunteer

OAUTH_SCOPES = (
    'https://www.googleapis.com/auth/userinfo.email',
)


@endpoints.api(name="volunteer", version="v1", description="Volunteer API")
class VolunteersApi(remote.Service):
    @Volunteer.query_method(user_required=True, path="volunteer/get/all", name="get_all",
                            query_fields=("limit", "order", "pageToken"))
    def getAllVolunteers(self, query):
        return query

    @Volunteer.method(user_required=True, path="volunteer/apply", name="apply")
    def applyVolunteer(self, volunteer):
        """Method for new volunteers to apply to org."""
        user = endpoints.get_current_user()
        volunteer.confirmed = False
        volunteer.email = user.email()
        volunteer.name = user.nickname()
        volunteer.put()
        return volunteer

    @Volunteer.method(request_fields=("id",), path="volunteer/confirm/{id}",
                      http_method="POST", name="confirm")
    def confirmVolunteer(self, volunteer):
        """Method for admins to confirm a volunteers."""
        user = endpoints.get_current_user()
        is_admin = oauth.is_current_user_admin(_format_oauth_scopes(OAUTH_SCOPES))
        if not is_admin:
            raise endpoints.UnauthorizedException("You are not allowed to make this request.")
        volunteer.confirmed = True
        volunteer.confirmed_by = user
        return volunteer


def _format_oauth_scopes(oauth_scopes):
    if hasattr(oauth_scopes, '__iter__'):
        oauth_scopes = ' '.join(oauth_scopes)
    return oauth_scopes
