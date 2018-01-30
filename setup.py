from distutils.core import setup

setup(
        name='gitlab-clone-all',
        version='1.1',
        packages=[''],
        url='',
        license='MIT',
        author='Evgeny Taranov',
        author_email='evgeny.taranov@gmail.com',
        description='Tool to work with multi-repo projects '
                    'based on git and gitlab',
        scripts=['gitlab-clone-all',
                 'git-fetch-all',
                 'git-set-author-all',
                 'git-checkout-all',
                 'git-replace-remote-all']
)
