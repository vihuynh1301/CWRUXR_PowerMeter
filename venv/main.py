import asyncio
from kasa import SmartPlug
import random
from cwruxr_sdk.common import *
from cwruxr_sdk.client import *
from cwruxr_sdk.object_message import *

ENDPOINT = "https://cwruxrstudents.azurewebsites.net/api/v2/"
ROOM_ID = "VI"
ANCHOR_ID = "v2"
API_KEY = "[yourapikey]"



cwruxrClient = Client(ENDPOINT, ROOM_ID, ANCHOR_ID, API_KEY)

# Initialize visual elements for power usage
power_bar = PrimitiveMessage(
    id="power_bar",
    source=PRIMITIVE_CUBE,
    pose=Pose(Vector3(0, 0.1, 0), scale=Vector3(0.2, 0.2, 0.2)),
    materialID="Lit:Green",
    isManipulationOn=False
)
cwruxrClient.PostObject(power_bar)

power_text = TextMessage(
    id="power_text",
    pose=Pose(Vector3(0, 0.5, 0), scale=Vector3(1, 1, 1)),
    parameters=TextParameters(text="Power: 0W"),
    isManipulationOn=False
)
cwruxrClient.PostObject(power_text)

# Function to update power usage visualization
def update_power_visual(power_value):
    # Scale the power value for visualization
    scaled_height = power_value / 100  # Example scaling
    scaled_height = min(max(scaled_height, 0.1), 1)  # Clamp the value between 0.1 and 1

    # Update power bar
    power_bar.pose.scale.y = scaled_height
    power_bar.pose.position.y = scaled_height / 2  # Adjust position based on height
    cwruxrClient.PostObject(power_bar)

    # Update power text
    power_text.parameters.text = f"Power: {power_value}W"
    cwruxrClient.PostObject(power_text)

# # Async function to fetch power data and update visualization using given func from kasa doc
# async def power_monitor():
#     PLUG_IP = "192.168.x.x"  # Replace with the actual IP of the smart plug
#     plug = SmartPlug(PLUG_IP)

#     while True:
#         await plug.update()
#         power_data = plug.emeter_realtime["power"]
#         update_power_visual(power_data)
#         await asyncio.sleep(1)  # Update every second

# # Start the asyncio loop
# asyncio.run(power_monitor())
#####

async def power_monitor_simulation(iterations=60):
    for _ in range(iterations):
    #while True:
        # Generate a random power value for simulation (e.g., between 0 and 100 watts)
        simulated_power_data = random.uniform(0, 100)

        # Update the visualization with the simulated data
        update_power_visual(simulated_power_data)

        await asyncio.sleep(0.01)  # Update every second

# Start the asyncio loop with the simulation function
asyncio.run(power_monitor_simulation())
