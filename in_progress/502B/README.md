# NEU 502B lab code and exercises

Jupyter notebooks and materials for in-class lab demonstrations and exercises.

## Setting up your computing environment

We recommend setting up a dedicated computing environment for this class using [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). You can set up this conda environment locally or on the PNI server (i.e. scotty). To log onto the PNI server, connect to the Princeton VPN and use `ssh` from the command line with your username/password; e.g. `ssh username@scotty.pni.princeton.edu` (let the instructor know if you've never done this before). In the first step, we'll install [miniconda](https://docs.conda.io/en/latest/miniconda.html) in your home directory. If you already have a working conda installation, you can skip this step.

If you're on a Windows machine, use [PowerShell](https://docs.microsoft.com/en-us/powershell/), [Cygwin](https://www.cygwin.com/), [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), or [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to log onto the PNI server, then proceed to the following Linux instructions.

If you're on a Linux machine (e.g. the PNI server), use the following:

```
cd ~
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

If you're on an Apple Silicon (M-series) Mac, use the following instead:

```
cd ~
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
bash Miniconda3-latest-MacOSX-arm64.sh
```

Next, we'll create a conda environment for the class and activate that environment.

```
conda create --name neu502b
conda activate neu502b
```

Now we'll install some necessary packages (and their dependencies) into our conda environment.

```
conda install -c conda-forge python=3.12 jupyterlab scipy matplotlib seaborn git gh
```

Next, we'll install some neuroscience-specific packages via `pip`.

```
pip install nilearn psyneulink
```

Later in the course, we'll install some additional packages—but don't worry about this for now.

```
conda install -c conda-forge mne-base
conda install pytorch
```

Create a GitHub account at https://github.com if you don't already have one. Next, in the terminal configure git with a username and email.
```
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
```

Begin authenticating with GitHub from git.
```
gh auth login
```

Select `GitHub.com`, `HTTPS`,  `Yes` and `Paste an authentication token`. Then, navigate to https://github.com/settings/tokens in a browser. Click _Generate new token_ and enter a nickname of your computer in the _Note_ field (e.g. _macbook_, _scotty_). Set the expiration to _No expiration_. Click _repo_, _read:org_, and _user_; then, click _Generate token_. Copy the token and paste it into `Paste your authentication token` on the command line.

## Forking and cloning the repository

On the GitHub repository page (https://github.com/NEU502B/neu502b-2025), click the _Fork_ button at top right. Click _Create fork_ to create a copy of the repository on your own GitHub account.

Back to the terminal: If you don't already have a directory for this class, make one (`mkdir neu502b`) and navigate into it (`cd neu502b`).

Now, you'll clone your own fork of the repository (specify your GitHub username below) into your class directory:

```
git clone https://github.com/username/neu502b-2025
cd neu502b-2025
```

## Running the notebooks

You can pull and run the notebooks on your local computer, on the PNI server, or run them on the cloud using Colab. To run the notebooks locally, navigate your terminal to your `neu502b` directory and run `jupyter lab`.

To run the notebooks on the server, we'll use port forwarding with an SSH tunnel to render the remote notebook in your local browser. First, log onto the server (e.g. `ssh username@scotty.pni.princeton.edu`). We recommend starting a persistent `tmux` session on the server (you can learn more about `tmux` [here](https://brainhack-princeton.github.io/handbook/content_pages/hack_pages/tmux.html)):

```
tmux new -s neu502b
```

You'll need to (re)activate the conda environment again inside the tmux session. Now, we'll start running Jupyter in the `tmux` session on the remote server (without a browser):

```
jupyter lab --no-browser
```

Next, copy the full URL output by the `jupyter lab` command on the server (including the authentication token); e.g. `http://localhost:8888/?token=abcdefghijklmnopqrstuv0123456789abcdefghijklmnop`

Now, open a local terminal and set up an SSH tunnel using the remote port (`8888` in the above example):

```
ssh -NL 8888:localhost:8888 username@scotty.pni.princeton.edu
```

Finally, open a browser and copy the full URL output by the `jupyter lab` command into the browser's URL bar. This should render the remote Jupyter session in your local browser, allowing you to efficiently interact with notebooks on the server.

This workflow follows best practices described in the [Princeton Handbook for Reproducible Neuroimaging](https://brainhack-princeton.github.io/handbook/index.html), and more details as well as other useful tips can be found there.
