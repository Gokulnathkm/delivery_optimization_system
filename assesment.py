import pandas as pd
import random

try:
    df = pd.read_csv("olist_customers_dataset.csv")
except FileNotFoundError:
    print("Error: Dataset file not found.")
    exit()
df=df.head(150)

new_data=[]

for i, row in df.iterrows():
    Location_id = row['customer_id']
    Distance = random.randint(5, 50)
    Priority = random.choice(["High", "Medium", "Low"])
    new_data.append([Location_id, Distance, Priority])

new_df = pd.DataFrame(new_data, columns=['Location_id', 'Distance', 'Priority'])

new_df.to_csv("delivery_dataset.csv", index=False)

print("created Dataset")

priority_map = {"High": 1, "Medium": 2, "Low": 3}
df = pd.read_csv("delivery_dataset.csv")
df['priority_num'] = df['Priority'].map(priority_map)

df = df.sort_values(by=['priority_num', 'Distance'])
agents = {
    "Agent_1": {"tasks": [], "total_distance": 0},
    "Agent_2": {"tasks": [], "total_distance": 0},
    "Agent_3": {"tasks": [], "total_distance": 0}
}
for i, row in df.iterrows():
    min_agent = min(agents, key=lambda x: agents[x]['total_distance'])
    
    agents[min_agent]['tasks'].append({
        "Location_ID": row['Location_id'],
        "Distance": row['Distance'],
        "Priority": row['Priority']
    })
    
    agents[min_agent]['total_distance'] += row['Distance']

for agent, data in agents.items():
    print(f"{agent}:")
    print(" Locations:", data['tasks'])
    print(" Total Distance:", data['total_distance'])
    print()

output = []

for agent, data in agents.items():
    for task in data['tasks']:
        output.append([
            agent,
            task['Location_ID'],
            task['Distance'],
            task['Priority'],
            data['total_distance']
        ])

output_df = pd.DataFrame(output, columns=[
    "Agent", "Location_ID", "Distance", "Priority", "Total_Distance"
])

output_df.to_csv("delivery_plan.csv", index=False)




    