# Pelion-Python-Test-1
Repeatedly get resource value.

# Prerequisite

You should use Python 2.7.x, not 3.x. Check your Python version by `python --version`

Run the firmware of [Quick Connect](https://cloud.mbed.com/quick-start) on your target board. Get your device ID (Endpoint Name, at the last line in the example output below).

```
Starting Simple Mbed Cloud Client example
Connecting to the network using Ethernet...
Connected to the network successfully. IP address: 10.128.4.85
[Simple Cloud Client] Autoformatting the storage.
[Simple Cloud Client] Reset storage to an empty state.
[Simple Cloud Client] Starting developer flow
Initialized Mbed Cloud Client. Registering...
Connected to Mbed Cloud. Endpoint Name: 0165885edb66000000000001001002ef
```

# Setup

## Install SDK

`$ pip install mbed-cloud-sdk`

## Download Project

`$ git clone https://github.com/coisme/Pelion-Python-Test-1.git`

## API Key

Create a configuration file in your `$HOME` or project directory (`.mbed_cloud_config.json`):
```
{
    "api_key": "your_api_key_here"
}
```
# Run

In the project directory, run the following command. Make sure you use python 2.7.x.

`$ python pull-notification.py`
