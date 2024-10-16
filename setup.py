from distutils.core import setup
setup(
  name = 'bubble_sort',         # How you named your package folder (MyLib)
  packages = ['bubble_sort'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here:
  description = 'Turtorial for package, bubble sort',   # Give a short description about your library
  author = 'Xinxin',                   # Type in your name
  author_email = 'x57yu@uwaterloo.ca',      # Type in your E-Mail
  url = 'https://github.com/XinxinTree/turtorial_bubble',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/XinxinTree/turtorial_bubble/archive/refs/tags/v_01_bubb.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy'
          
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
