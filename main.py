#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi

mainform = """
    <form method="post">
        <h2>Web Caesar</h2>
        <p>Rotate by: <input type="number" name="rotation" value="%(rotation)s"/></p>
        <br>
        <p>Type a message: <textarea name="text">%(text)s</textarea></p>
        <input type="submit" />
        <br>
    </form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = mainform%{"text":"", "rotation":13}
        self.response.write(content)

    def post(self):
        message = self.request.get("text")
        str_rotation = self.request.get("rotation")
        if str_rotation.isdigit():
            rotation = int(str_rotation)
        else:
            rotation = 13
        encrypted_message = cgi.escape(caesar.encrypt(message, rotation), quote=True)
        content = mainform%{"text":encrypted_message, "rotation":rotation}
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
