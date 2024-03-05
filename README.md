# Raspberry Pi Home Assistant Setup

## Setup Instructions:

1. **Hardware Setup:**
   - Obtain a Raspberry Pi, preferably a Raspberry Pi 5.
   - Acquire a micro SD card suitable for the Raspberry Pi.
   - Insert the micro SD card into the Raspberry Pi.

2. **Software Installation:**
   - Connect the Raspberry Pi to a computer.
   - Download and install the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) on the computer.
   - Run the Raspberry Pi Imager software.
   - Insert the micro SD card into the computer.

3. **Operating System Installation:**
   - In the Raspberry Pi Imager, select the option to install an operating system.
   - Choose the appropriate Raspberry Pi model.
   - Select **Other specific-purpose OS** > **Home assistants and home automation** > **Home Assistant**.
   - Continue with the installation.

4. **Pi 5 Compatibility Issues:**
   - If the installed Home Assistant version is not compatible with Raspberry Pi 5:
     - Download the necessary files from [GitHub](https://github.com/home-assistant/operating-system/releases/download/11.4/haos_rpi5-64-11.4.img.xz).
     - Manually install the Home Assistant operating system from the downloaded files.
     - Attach the custom file on the operating system Dropbox in the Raspberry Imager.

5. **Completion:**
   - Once the installation process is complete, eject the micro SD card from the computer.
   - Insert the micro SD card into the Raspberry Pi.
   - Power on the Raspberry Pi to start using Home Assistant.

## Configuration and Connection:

1. **Initial Setup:**
   - Wait until the Raspberry Pi completes processing configuration files and displays the "Home Assistant" logo with an IP address.
   - Do not interact with the system until you see the "Home Assistant" logo and the IP address.

2. **Network Configuration:**
   - Connect a keyboard to the Raspberry Pi.
   - Type `login` and press enter.
   - Then, type `nmcli device connect`.
   - Select the desired network for connection, in my case, my personal mobile hotspot.
   - Type `nmcli device connect [network name] password [actual network password]`.
   - Wait for the confirmation message indicating successful connection.

3. **Access Home Assistant:**
   - Find the IP address displayed on the Raspberry Pi, under the Home Assisant logo.
   - On another computer connected to the same network as the Raspberry Pi, open a web browser.
   - Type the IP address provided by the Raspberry Pi into the web browser's address bar.
   - Follow the on-screen instructions to pair up and create a user account for Home Assistant.

4. **Extras**
   - Make sure the Raspberry Pi with Home Assistant remains powered on and connected to the network.
   - Home Assistant can be managed entirely from an external device, even if the Raspberry Pi operates headlessly.
