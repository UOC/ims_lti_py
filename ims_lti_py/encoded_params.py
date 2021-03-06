import base64

# List of the launch parameters for an LTI launch not encoded in Base 64
EXCLUDED_BASE64_PARAMETERS = [
    'lti_version',
    'lti_message_type',
    'tool_consumer_instance_name',
    'tool_consumer_instance_description',
    'tool_consumer_instance_guid',
    'oauth_consumer_key',
    'custom_lti_message_encoded_base64',
    'oauth_nonce',
    'oauth_version',
    'oauth_callback',
    'oauth_timestamp',
    'basiclti_submit',
    'oauth_signature_method',
    'oauth_signature',
    'custom_lti_message_encoded_utf8',
    'custom_lti_message_encoded_iso',
    'ext_ims_lis_memberships_url',
    'ext_ims_lis_memberships_id',
    'ext_ims_lis_basic_outcome_url',
    'ext_ims_lti_tool_setting_url',
    'ext_basiclti_submit',
    'launch_presentation_return_url'
]

class EncodedParamsMixin(object):
    def decode_params(self, params={}):
        decoded_params = params.copy()
        if params['custom_lti_message_encoded_base64'] == '1':
            for param in params:
                if not param in EXCLUDED_BASE64_PARAMETERS:
                    decoded_params[param] = base64.b64decode(params[param]).decode()
        return decoded_params