from fastapi import FastAPI, Depends, HTTPException, status

blogs = {
    "1": "FastAPI Pre-Req",
    "2": "Building APIs with FastAPI",
    "3": "Background Tasks | Celery x FastAPI",
}

users = {
    "8":"James",
    "9":"Michael",
}

app = FastAPI(title="Dependency Injection")

def get_blog_name_or_404(id: str):
    blog = blogs.get(id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog {id} not found",
        )
    return blog

class GetObjectOr404:
    ''' Parameterized dependency to make dependency injection more generalized '''
    def __init__(self, model: dict) -> None:
        self.model = model

    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Object with {id} not found",
            )
        return obj

blog_dependency = Depends(GetObjectOr404(blogs))
@app.get("/blog/{id}")
def get_blog(blog_name:str = blog_dependency):
    return blog_name

user_dependency = Depends(GetObjectOr404(users))
@app.get("/user/{id}")
def get_blog(user_name:str = user_dependency):
    return user_name