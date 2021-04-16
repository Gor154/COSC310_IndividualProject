from google.cloud import translate_v2 as translate

def translate_text(target, text):
    import six
    translate_client = translate.Client.from_service_account_json('/Users/gor154/Downloads/qualified-cedar-310923-828fa7355ae7.json')

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    result = translate_client.translate(text, target_language=target)

    return result["translatedText"]

def detect_language(text):

    translate_client = translate.Client.from_service_account_json('/Users/gor154/Downloads/qualified-cedar-310923-828fa7355ae7.json')

    result = translate_client.detect_language(text)

    return result["language"]
