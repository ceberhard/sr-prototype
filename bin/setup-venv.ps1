$scriptpath = split-path -parent $MyInvocation.MyCommand.Definition

$venvpath = $scriptpath + '\..\venv'

# echo $venvpath

if (test-path $venvpath) {
    remove-item $venvpath -recurse -force
}

C:\Python34\python -m venv $venvpath

# cd $venvpath\Scripts\
# $installcmd = $venvpath + '\Scripts\pip3 install biopython'
# Invoke-Expression $installcmd

echo ""
echo "---------------------------------------------------------------------------------"
echo "Virtual Environment installed... to activate the environment in your shell run:"
echo "---------------------------------------------------------------------------------"
echo ".\venv\Scripts\Activate.ps1"
echo ""
