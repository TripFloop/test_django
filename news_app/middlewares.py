class EditHTMLMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        response = self._get_response(request)
        index = response.content.find(b"</header>")
        # response.content is bytestring, so to concatenate we need to decode it
        content_decoded = response.content.decode()
        new_content = content_decoded[:index] + "<! - HelloWorld >" + content_decoded[index:]
        # after need to encode it back
        content_decoded = response.content.decode()
        new_content = content_decoded[:index] + "<! - HelloWorld >" + content_decoded[index:]
        response.content = new_content.encode("utf-8")
        return response
