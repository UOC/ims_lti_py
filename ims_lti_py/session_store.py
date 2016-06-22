import pickle


class SessionStoreMixin(object):
    """
    A 'mixin' for LTI session storage
    """

    def save_context(self, request, context):
        """
        This must be implemented for the framework you're using

        Saves LTI context into session
        """
        raise NotImplemented

    def load_context(self, request):
        """
        This must be implemented for the framework you're using

        Retrieve LTI context into session
        """
        raise NotImplemented


class TornadoSessionStoreMixin(SessionStoreMixin):

    """
    A 'mixin' for LTI session storage using Tornado
    """

    COOKIE_NAME = "LTI Context"

    def save_context(self, request, context):
        request.set_secure_cookie(self.COOKIE_NAME, pickle.dumps(context), 1)

    def load_context(self, request):
        context_as_string = request.get_secure_cookie(self.COOKIE_NAME)
        if context_as_string:
            return pickle.loads(context_as_string)

        return None
