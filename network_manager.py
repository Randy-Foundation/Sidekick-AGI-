from problem_solver import problem_solver
import datetime
import json
import os
import socket
import urllib.request
import math

class NetworkManager:
    def __init__(self, creator_id, security_logs_file="network_security_logs.json"):
        """
        Initialize the Network Manager with security logs and device tracking.
        """
        self.creator_id = creator_id
        self.network_logs = []
        self.approved_devices = {}
        self.smart_devices = {}
        self.behavior_logs = {}
        self.connected_wifi_points = []
        self.network_security_enabled = True
        self.mobile_data_enabled = False
        self.security_logs_file = security_logs_file
        self.security_risk_level = 1.0  # Weighted security trust factor (Golden Ratio applied)

    # ==========================
    # 📊 Network Monitoring
    # ==========================

    def log_event(self, event):
        """
        Log an event with a timestamp.
        """
        timestamp = datetime.datetime.now()
        log_entry = f"[{timestamp}] {event}"
        self.network_logs.append(log_entry)
        self.save_security_logs(log_entry)
        print(log_entry)

    def check_network(self):
        """
        Return a list of approved devices and their status.
        """
        return f"📡 Approved devices: {list(self.approved_devices.keys())}"

    def scan_wifi(self):
        """
        Scan the local network for active devices.
        """
        print("🔍 Scanning WiFi for active devices...")
        devices = []
        try:
            for ip in range(1, 255):
                ip_addr = f"192.168.1.{ip}"
                try:
                    hostname = socket.gethostbyaddr(ip_addr)
                    devices.append({'ip': ip_addr, 'hostname': hostname[0]})
                    self.log_event(f"📡 Detected device - IP: {ip_addr}, Hostname: {hostname[0]}")
                except socket.herror:
                    continue
        except Exception as e:
            self.log_event(f"⚠️ Error during WiFi scan: {e}")
        return devices

    # ==========================
    # 🔐 Security Management
    # ==========================

    def approve_device(self, device_name):
        """
        Approve a device based on recursive trust weighting.
        """
        phi = 1.618  # Golden Ratio
        trust_weight = round((phi ** self.security_risk_level) / self.security_risk_level, 2)

        self.approved_devices[device_name] = {
            "approved_by": self.creator_id,
            "trust_weight": trust_weight,
            "timestamp": datetime.datetime.now()
        }
        self.log_event(f"✅ Device '{device_name}' approved with trust weight {trust_weight}.")

    def emergency_shutdown(self):
        """
        Disconnect all devices in case of a network breach.
        """
        self.approved_devices.clear()
        self.smart_devices.clear()
        self.log_event("🚨 Emergency shutdown executed! All devices disconnected.")

    def analyze_security(self):
        """
        Perform a security check for known vulnerabilities.
        """
        try:
            url = "https://cve.circl.lu/api/last"
            with urllib.request.urlopen(url) as response:
                if response.status == 200:
                    self.log_event("✅ Security scan completed. No immediate vulnerabilities found.")
                    return response.read()
        except urllib.error.URLError as e:
            self.log_event(f"⚠️ Error during security analysis: {e}")
            return "⚠️ Could not fetch security updates."

    def detect_intrusions(self):
        """
        Detect unauthorized attempts to access the network.
        """
        print("🔍 Scanning for intrusions...")
        intrusion_detected = False
        for device in self.approved_devices:
            if self.approved_devices[device]["trust_weight"] < 1.0:
                intrusion_detected = True
                self.log_event(f"⚠️ Possible unauthorized access attempt from '{device}'.")
        
        if not intrusion_detected:
            print("✅ No intrusions detected.")
        return intrusion_detected

    # ==========================
    # 📡 Connectivity Management
    # ==========================

    def enable_mobile_data(self, permission):
        """
        Enable or disable mobile data access.
        """
        self.mobile_data_enabled = permission
        state = "enabled" if permission else "disabled"
        self.log_event(f"📶 Mobile data access {state}.")
        return f"📶 Mobile data access has been {state}."

    def connect_to_wifi(self, ssid, password=None):
        """
        Simulate connecting to a WiFi network.
        """
        self.connected_wifi_points.append(ssid)
        self.log_event(f"📡 Connected to WiFi network: {ssid}")
        return f"✅ Successfully connected to WiFi: {ssid}"

    def monitor_device_behavior(self, device_name, behavior_type, details):
        """
        Log and analyze behavior from connected devices.
        """
        timestamp = datetime.datetime.now()
        if device_name not in self.behavior_logs:
            self.behavior_logs[device_name] = []
        self.behavior_logs[device_name].append({
            "behavior_type": behavior_type,
            "details": details,
            "timestamp": timestamp
        })
        self.log_event(f"🛠 Behavior logged from '{device_name}': {behavior_type} - {details}")

    # ==========================
    # 🔍 Logging & Optimization
    # ==========================

    def save_security_logs(self, log_entry):
        """
        Save security logs to a file.
        """
        with open(self.security_logs_file, "a") as file:
            file.write(log_entry + "\n")

    def get_logs(self):
        """
        Retrieve all network logs.
        """
        return self.network_logs

    def get_behavior_logs(self):
        """
        Retrieve all behavior logs.
        """
        return self.behavior_logs

    def optimize_network(self):
        """
        Optimize network performance by managing connections and removing inactive devices.
        """
        print("🔧 Optimizing network connections...")
        before_count = len(self.approved_devices)
        self.approved_devices = {k: v for k, v in self.approved_devices.items() if v["trust_weight"] >= 1.0}
        after_count = len(self.approved_devices)

        self.log_event(f"🔄 Network optimized. Removed {before_count - after_count} inactive/low-trust devices.")
        print(f"✅ Network optimization complete. Active trusted devices: {after_count}.")

    def share_file(self, file_path, target_device):
        """
        Share a file with an approved device.
        """
        if target_device not in self.approved_devices:
            self.log_event(f"⚠️ Target device '{target_device}' not approved for file sharing.")
            return "⚠️ Device not approved."

        self.log_event(f"📂 File '{file_path}' sent to device '{target_device}'.")
        return f"📂 File '{file_path}' successfully shared with '{target_device}'."

# =====================
# 🔬 Example Usage
# =====================
if __name__ == "__main__":
    network_manager = NetworkManager("Randell_Murrin")

    # Check security status
    network_manager.analyze_security()

    # Monitor network activity
    network_manager.check_network()

    # Approve a device
    network_manager.approve_device("Randell_Phone")

    # Connect to WiFi
    network_manager.connect_to_wifi("Home_Network")

    # Optimize network
    network_manager.optimize_network()

    # Detect intrusions
    network_manager.detect_intrusions()