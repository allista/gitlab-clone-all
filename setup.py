from distutils.core import setup

setup(
        name='gitlab-clone-all',
        version='1.0',
        packages=[''],
        url='',
        license='MIT',
        author='Evgeny Taranov',
        author_email='evgeny.taranov@gmail.com',
        description='Clone all repositories from a gitlab server available to user',
        scripts=['gitlab-clone-all', 'git-fetch-all'],
)
