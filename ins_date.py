import sublime, sublime_plugin, time, datetime

'''
  simple date insertion
'''
date_format = "%Y-%m-%d"            # 2013-10-02
class InsertDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
      self.view.insert(edit, self.view.sel()[0].begin(),
                        time.strftime(date_format));

'''
  panel popup taken from https://gist.github.com/robmccormack/6040840
  I customized the output
'''
class InsertDatePanelCommand(sublime_plugin.TextCommand):

    def on_done(self, index):
        if index == -1:
          return

        # if user picks from list, return the entry
        self.view.run_command(
            "insert_my_text", {"args":
            {'text': self.list[index]}})

    def run(self, edit):
        #  Set formats
        d1 = str(datetime.date.today().strftime("%Y-%m-%d"))
        d2 = str(datetime.date.today().strftime("%B %d, %Y"))
        d3 = datetime.date.today().strftime("%b-%d-%Y")
        d4 = datetime.date.today().strftime("%m/%d/%Y")
        self.list = [d1, d2, d3, d4]

        self.view.window().show_quick_panel(self.list, self.on_done,0,1)


class InsertMyText(sublime_plugin.TextCommand):

    def run(self, edit, args):
        self.view.insert(edit, self.view.sel()[0].begin(), args['text'])