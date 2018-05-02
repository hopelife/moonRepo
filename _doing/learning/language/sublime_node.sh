#!/bin/sh
osascript -e '
  on run parameters
    tell application "terminal"
      activate
      do script with command "node " & parameters
    end tell
  end run
' $@
