#!/bin/sh
osascript -e '
tell application "iTerm2"
  set newWindow to (create window with default profile)
  tell current session of newWindow
    write text "echo it works!"
  end tell
end tell
' $@