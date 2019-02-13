This instruction works for Linux Mint 18.1 (and probably for most Debian-based Linuxes)

Development environment
=======================

#. Install prerequisites::

    apt update
    apt install git
    wget https://github.com/jgm/pandoc/releases/download/2.6/pandoc-2.6-1-amd64.deb
    sudo dpkg -i pandoc-2.6-1-amd64.deb

#. Fork `<https://github.com/dmugtasimov/containers-micro-optimizations>`_ repository

#. Clone forked repository (replace <username> with your github account name)::

    git clone git@github.com:<username>/containers-micro-optimizations.git
    cd containers-micro-optimizations

#. Configure git user name and email if you have not done it yet::

    git config user.name 'Firstname Lastname'
    git config user.email 'youremail@youremail_domain.com'

#. Install and configure `pyenv` according to https://github.com/pyenv/pyenv#basic-github-checkout
#. Install Python 3.7.2::

    pyenv install 3.7.2

#. Install `pipenv`::

    pip install --user pipenv==2018.11.26

#. Create virtualenv with all required dependencies::

    pipenv install --dev

#. Switch to virtualenv::

    pipenv shell

#. Install Containers Micro-optimizations in development mode::

    pip install -e .

#. Build the blogpost::

    make
