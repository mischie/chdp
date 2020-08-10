import setuptools

setuptools.setup(
    name = 'chdp',
    version = '4.0.0',
    description = 'Command Handler for Discord.Py',
    author = 'kiki7000',
    author_email = 'devkiki7000@gmail.com',
    url = 'https://github.com/kiki7000/chdp',
    packages = setuptools.find_packages(),
    keywords = ['discord', 'discord.py', 'commandhandler', 'chdp', 'handler', 'command', 'kiki'],
    python_requires = '>=3.7',
    install_requires = ['discord.py'],
    zip_save = False,
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
)
