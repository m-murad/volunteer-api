from endpoints.apiserving import _ApiServer
import ndb
from utils import *


__all__ = [ndb]

__all__ += utils.__all__

# Monkey patch the ProtoJson instance to be used
# for parsing requests.
_ApiServer._ApiServer__PROTOJSON = utils._EPDProtoJson()
