# quick-dd
A simple Python program to run dd quicker.

![quick-dd example](/docs/images/example.gif)

## Done
- :heavy_check_mark: Basic functionality
- :heavy_check_mark: Check if selected drive exists

## To-do list
- :x: Put ls output in array
- :x: Print numbered array contents
- :x: Pull image name from array with number
- :x: The ability to manage pools with quick-dd
- :x: Escape special characters from `image`

## Make runable with qdd
1. store the file in safe location where you can't accidentally delete it.
2. Make file executable with `chmod +x quick-dd.py`.
3. Make an alias by adding `alias qdd='python /location/of/file'` to the .bashrc under `# User specific aliases and functions` in your home directory.

Now the tool can be run with the `qdd` command from the commandline.

## Default pools
- 'os' pointing to /mnt/sdb1/OS
- 'down' pointing to ~/Downloads

To make a custom pool edit the selectPool and ddRun functions.  
