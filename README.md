# Extract, Transform, Load (ETL) Project

This project is focused on the implementation of an ETL pipeline. The pipeline involves selecting a dataset, creating a data model, loading the data into a relational database, extracting it to a storage system, performing an ETL job, loading the data into a data warehouse, and finally fetching it to a dashboard from the warehouse.

## Technologies Used

- **Python**: The main programming language used for data manipulation and analysis.
- **Jupyter Notebook**: An open-source web application that allows creation and sharing of documents that contain live code, equations, visualizations and narrative text.
- **PostgreSQL**: An open-source relational database management system used for creating a data model.
- **Snowflake**: A cloud-based data warehousing platform used for storing and analyzing data.
- **PowerBI**: A business analytics tool developed by Microsoft. It provides interactive visualizations and business intelligence capabilities with an interface that is easy to use for creating reports and dashboards.

## Author

Eero Kuosmanen - [Github](https://github.com/eeroak)

## Project Status

Project finished at 26.3.2024.

## License

Distributed under the MIT License. See LICENSE for more information.

## Acknowledgements
<details>
<summary>Click to expand</summary>
<br>
<h4>Notes</h4>
<ul>
    <li>My first project, some practical work with data loading, transforming and extracting.</li>
    <li>I found the project very interesting and engaging, but i will use a more challenging dataset next time for sure for more challenge and so i can create better datamodels.</li>
    <li>Main challenges were with data-loading and extracting from snowflake and to PowerBI, since they are new technologies for me. I really liked snowflake tho, i can see myself using it in the future.</li> 
</ul>
<img src="img\\snowflake_db.png" title="Data succesfully loaded in to snowflake database">
<img src="img\\warehouse_activity.png" title="Succesful warehouse activity">
<img src="models\\model.png" title="Data model created in PostgreSQL">
<img src="img\\data_in_powerbi.png" title="A figure representing the average MSRP per year loaded from Snowflake to PowerBI">
</details>
