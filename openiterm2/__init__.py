from fman import DirectoryPaneCommand, show_alert, load_json, DATA_DIRECTORY
import os

class OpenIterm2(DirectoryPaneCommand):
    def __call__(self):
        currentDirName = self.pane.get_path()
        os.system("/usr/bin/osascript '" + DATA_DIRECTORY + "/Plugins/OpeniTerm2/OpeniTerm2.scpt' '" + currentDirName + "'")
