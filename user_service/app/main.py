from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from .db_handler.connection import engine, Base, check_db_connection, get_db, text
from sqlalchemy.ext.asyncio import AsyncSession

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        yield
    finally:
        await engine.dispose()


def create_applicaiton() -> FastAPI:
    app = FastAPI(title="User Microservice",
    lifespan=lifespan,
    docs_url="/api/docs",
    redoc_url="/api/redoc")

    app.add_middleware(CORSMiddleware, allow_headers = ["*"])

    @app.get("/")
    async def health():
        await check_db_connection()
        
        return "user microservice is up"

    @app.get("/debug/schema")
    async def schema(db: AsyncSession = Depends(get_db)):
        result = await db.execute(text("""
            SELECT table_name, column_name, data_type, is_nullable
            FROM information_schema.columns
            WHERE table_schema = 'public'
            ORDER BY table_name, ordinal_position
        """))
        tables: dict[str, list] = {}
        for table_name, column_name, data_type, is_nullable in result:
            tables.setdefault(table_name, []).append(
                {"column": column_name, "type": data_type, "nullable": is_nullable == "YES"}
            )
        return tables
    
    return app

app = create_applicaiton()




