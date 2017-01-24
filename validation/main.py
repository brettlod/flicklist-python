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

def valid_month(user_month):
    return True

def valid_day(user_day):
    return True

def valid_year(user_year):
    return True

form="""
<form method="post">
    What is your birthday?
    <br>
    <label>
        Month
        <input type="text" name="month" value="%(month)s"></label>
    <label>
        Day
        <input type="text" name="day" value="%(day)s"></label>
    <label>
        Year
        <input type="text" name="year" value="%(year)s"></label>
    <div style="color: red">%(error)s</div>
    <br>
    <br>
    <input type = "submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error": error,
                                        "month": month,
                                        "day": day,
                                        "year": year})

    def get(self):
        self.write_form

    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))

        if not (user_month and user_day and user_year):
            self.write_form("That doesn't look valid to me, friend.")
        else:
            self.response.out.write("Thanks! That's a valid day.")

app = webapp2.WSGIApplication([('/', MainPage)],
                    debug=True)
