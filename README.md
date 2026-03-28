# 📦 Delivery Optimization System

This project was developed as part of an assessment task.

## 📌 Overview

This project focuses on solving a **logistics delivery optimization problem**.
The goal is to assign delivery locations to multiple agents such that:

* Workload is **balanced across agents**
* High-priority deliveries are handled first
* Total travel distance is **optimized efficiently**


## 📊 Dataset

The dataset is derived from the **Olist Brazilian E-Commerce dataset (Kaggle)**.
Relevant features were extracted and transformed to fit the problem.

### Data Preparation:

* `customer_id` → used as **Location_ID**
* **Distance** → randomly generated (5–50 units) to simulate delivery distance
* **Priority** → randomly assigned (`High`, `Medium`, `Low`) to simulate real-world urgency independent of distance

### Final Dataset Columns:

* Location_ID
* Distance
* Priority


## 🧠 Approach

### 1. Sorting

Deliveries are sorted based on:

1. **Priority** (High → Medium → Low)
2. **Distance** (ascending order)

This ensures:

* Urgent deliveries are handled first
* Shorter routes are prioritized within each priority level


### 2. Algorithm Used – Greedy Approach

A **greedy algorithm** is used to assign deliveries efficiently.

#### Logic:

* Initialize 3 delivery agents
* Iterate through sorted deliveries
* Assign each delivery to the agent with the **least total distance**

#### Why Greedy?

* Simple and efficient
* Produces **near-optimal load balancing**
* Suitable for real-time logistics systems


### 3. Load Balancing

The system ensures:

* Each agent gets a **nearly equal total delivery distance**
* No agent is overloaded
* Efficient distribution of tasks


## 📁 Project Structure

```
Digitivity/
│── assesment.py
│── olist_customers_dataset.csv
│── delivery_dataset.csv
│── delivery_plan.csv
│── README.md
```


## ▶️ How to Run

1. Navigate to the project folder:

```bash
cd Digitivity
```

2. Activate virtual environment:

```bash
source venv/bin/activate
```

3. Run the program:

```bash
python assesment.py
```


## 📤 Output

### 1. delivery_dataset.csv

Processed dataset containing:

* Location_ID
* Distance
* Priority


### 2. delivery_plan.csv

Final optimized delivery assignment:

| Agent | Location_ID | Distance | Priority | Total_Distance |
| ----- | ----------- | -------- | -------- | -------------- |

Each row represents:

* Assigned agent
* Delivery location
* Distance of that delivery
* Priority level
* Total distance handled by that agent


## ✅ Results

* Deliveries are distributed across 3 agents
* Total distance per agent is **balanced**
* Priority-based sorting ensures urgent deliveries are handled first
* The system scales well with larger datasets



## 🚀 Conclusion

This project demonstrates how a **greedy algorithm** can effectively solve a delivery optimization problem by:

* Prioritizing tasks
* Balancing workloads
* Maintaining efficiency without complex computations



## 🔧 Future Improvements

* Use real geographic coordinates to calculate actual distances
* Implement route optimization (e.g., shortest path algorithms)
* Handle larger datasets for scalability analysis
* Add visualization (maps or dashboards)


## 📎 Note

The dataset is inspired by Kaggle (Olist dataset) and has been **preprocessed and enhanced** with additional features (distance and priority) to simulate a real-world delivery optimization scenario.
