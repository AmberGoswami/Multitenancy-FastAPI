# Multitenancy-FastAPI

•FastAPI Multi-tenant architecture<br>
•ORM: SqlAlchemy<br>
•Migration: Alembic<br>
•Database: PostgreSQL<br>
•Data Validation: Pydantic<br>
<br>

Schema based muliti-tenancy, Each tenant can have different schema in the database containing tables with same entities. Every tenant get's assigned a unique SqlAlchemy Class through which data can be accessed. Tenant specific crud operatrion APIs being developed. Proper JWT authentication and API authorization with tenant specific login API.  
