A lot of good work here. I like how you're separating out the classes into different files.

* Get in the habit of using the `if __name__ == '__main__':` for your main scripts, rather than having code sitting out by itself. It'll come in handy later
* In CoursesLoop, you `import datetime` in the `'__main__'` code. Typically those go at the top of the file (which you do elsewhere).
