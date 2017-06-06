import sublime, sublime_plugin
import subprocess

# Command: replace_with_shell_result
# Replaces all highlighted regions with the Shell interpretation.
#
# Example:
#   `pwd` -> `~/code/project`
class ReplaceWithShellResultCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for i, region in enumerate(self.view.sel()):
      if not region.empty():
        txt = self.view.substr(region)
        try:
          proc = subprocess.Popen(
              txt, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
          new_txt = '\n'.join(line.decode('utf-8')
                              for line in proc.stdout.readlines())
          print(type(new_txt))
          proc.wait()
          self.view.replace(edit, region, new_txt)
        except Exception as e:
          print('Could not replace: %s' % e)
