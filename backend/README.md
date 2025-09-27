## 📂 Backend Structure

<pre> 
backend/
└─ src/
   ├─ main.py                       # FastAPI app entrypoint / app factory
   ├─ routes.py                     # Root router includes
   │
   ├─ core/                         # Core config & security
   │  ├─ config.py                  # Loads environment variables
   │  └─ security.py                # Password hashing, JWT utils
   │
   ├─ api/
   │  └─ v1/
   │     ├─ auth/                   # Auth endpoints
   │     │  └─ routes.py            # Signup / login routes
   │     └─ home/                   # (Future public routes)
   │        └─ routes.py
   │
   ├─ crud/                         # Low-level DB CRUD operations
   │  └─ crud_user.py               # User CRUD functions
   │
   ├─ db/                           # Database config & init
   │  ├─ session.py                 # Async engine & session maker
   │  └─ init_db.py                 # One-time DB init script
   │
   ├─ models/                       # SQLAlchemy ORM models
   │  └─ user.py                    # User table definition
   │
   ├─ schemas/                      # Pydantic schemas
   │  └─ auth.py                    # User input/output models
   │
   ├─ services/                     # Business logic / orchestration
   │  └─ user_service.py            # User registration service
   │
   └─ utils/                        # (optional future utilities)
</pre>
