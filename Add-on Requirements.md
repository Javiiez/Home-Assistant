## Instructions:

1. Access the external interface of the Home Assistant web server.
2. Navigate to **Settings** and click on **Add-ons**.
3. At the bottom right corner, click on **Add-on Store**.
4. Download the following add-ons: **Mosquitto broker** and **File editor**.
5. Once installed, open the **File editor** and click on **Show in sidebar**.
6. Now, access **Mosquitto broker** and navigate to the **Configuration** tab.
7. Ensure to create a login user for this usage. In the login section, specify the following:
   - Username: mqtt-user (can be anything for identification)
   - Password: [anything you desire]
8. In the **Customize** area, input the following:
   - Active: true
   - Folder: mosquitto
   - Certfile: fullchain.pem
   - Keyfile: privkey.pem
   - Require_certificate: false

This setup configures Mosquitto to access the Home Assistant's configuration files, which is necessary for linking with other clients, such as sensors later on.
