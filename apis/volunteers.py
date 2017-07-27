import endpoints
from protorpc import remote

from models import UnconfirmedVolunteer


@endpoints.api(name="volunteer", version="v1", description="Volunteer API")
class VolunteersApi(remote.Service):
    @UnconfirmedVolunteer.method(user_required=True, path="volunteer/apply", name="apply")
    def applyVolunteer(self, volunteer):
        """Method for new volunteers to apply to org."""
        user = endpoints.get_current_user()
        volunteer.email = user.email()
        volunteer.name = user.nickname()
        volunteer.put()
        return volunteer
