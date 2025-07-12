# PySpark Data Processing Project

A PySpark application for processing orders and customers data with filtering, joining, and aggregation operations.

## Overview

This project demonstrates basic PySpark operations including:
- Reading data from multiple sources (orders and customers)
- Filtering data based on conditions
- Joining datasets
- Performing aggregations
- Logging operations

## Datasets Used

This project utilizes sample retail data consisting of orders and customers information for comprehensive data analysis and processing.

### Dataset Details
- **Format**: CSV files
- **Records**: 
  - Customers: 10,000+ records
  - Orders: 65,000+ records
- **Location**: The datasets are stored in the `data/` directory of this project
- **Files**:
  - `data/customers.csv` - Customer information and demographics
  - `data/orders.csv` - Order transactions and details

### Accessing the Dataset

You can access the datasets in the following ways:

**GitHub Repository**: [Access the complete dataset here](https://github.com/shubhambhargava55/RetailProject/tree/main/data)

## Features

- **Data Reading**: Reads orders and customers data from configurable sources
- **Data Filtering**: Filters orders to include only closed orders
- **Data Joining**: Joins orders and customers data for comprehensive analysis
- **Data Aggregation**: Counts orders by state
- **Environment Configuration**: Supports multiple environments (dev, prod, etc.)
- **Logging**: Comprehensive logging using Log4j

## Prerequisites

- Python 3.7+
- Apache Spark 3.0+
- PySpark
- Java 8 or 11

## Project Structure

```
retail-project/
├── configs/
│   ├── application.conf    # Application configuration (file paths)
│   └── pyspark.conf       # PySpark configuration (cluster settings)
├── lib/
│   ├── ConfigReader.py    # Configuration management utilities
│   ├── DataManipulation.py # Data processing functions
│   ├── DataReader.py      # Data reading utilities
│   └── Utils.py           # Spark session utilities
├── data/
│   ├── customers.csv      # Customer data
│   └── orders.csv         # Order data
├── application_main.py    # Main application entry point
└── README.md
```

### Running the Application

Clone the repository:
```bash
git clone https://github.com/shubhambhargava55/RetailProject.git
cd <project-directory>
```

Execute the main application with environment parameter:

```bash
# Local environment
python application_main.py LOCAL

# Test environment
python application_main.py TEST

# Production environment
python application_main.py PROD
```

## Configuration

The application uses environment-based configuration. Make sure to set up your environment-specific configurations in the `Utils.get_spark_session()` method.

## Data Pipeline

The application follows this data processing pipeline:

1. **Initialize Spark Session**: Creates a Spark session based on the specified environment
2. **Read Orders Data**: Loads orders dataset using `DataReader.read_orders()`
3. **Filter Orders**: Filters to include only closed orders using `DataManipulation.filter_closed_orders()`
4. **Read Customers Data**: Loads customers dataset using `DataReader.read_customers()`
5. **Join Data**: Joins filtered orders with customers data using `DataManipulation.join_orders_customers()`
6. **Aggregate Results**: Counts orders by state using `DataManipulation.count_orders_state()`
7. **Display Results**: Shows the final aggregated results

## Library Modules

### DataReader
Contains functions for reading data from various sources:
- `read_orders()`: Reads orders data
- `read_customers()`: Reads customers data

### DataManipulation
Contains data processing functions:
- `filter_closed_orders()`: Filters orders with 'CLOSED' status
- `join_orders_customers()`: Joins orders and customers datasets
- `count_orders_state()`: Aggregates order counts by state

### Utils
Utility functions for:
- `get_spark_session()`: Creates and configures Spark session

### Logger
Logging configuration using Log4j for Spark applications.

## Output

The application displays the final results showing order counts grouped by state.

## Error Handling

- Validates command-line arguments
- Exits gracefully if environment parameter is not provided
- Includes comprehensive logging for debugging

## Troubleshooting

### Common Issues

1. **Missing Environment Parameter**
   ```
   Error: Please specify the environment
   Solution: Run with environment parameter (LOCAL/TEST/PROD)
   ```

2. **Configuration File Not Found**
   ```
   Check: Ensure configs/ directory exists with proper .conf files
   ```

3. **Data Files Not Found**
   ```
   Check: Verify data/ directory contains customers.csv and orders.csv
   ```
