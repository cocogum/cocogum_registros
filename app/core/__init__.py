from app.auth.dependencies import (
    get_current_active_admin,
    get_current_active_user,
    get_current_user,
)

# Prueba rápida para verificar importaciones
print(get_current_active_admin)
print(get_current_active_user)
print(get_current_user)
