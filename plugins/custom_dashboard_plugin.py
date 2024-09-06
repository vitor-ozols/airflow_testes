from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint, render_template
from flask_admin.base import MenuLink

# Crie um blueprint Flask para a nova página
custom_page = Blueprint("custom_page", __name__,
                        template_folder='templates',
                        static_folder='static')

# Defina a rota para a página personalizada
@custom_page.route("/stream")
def custom_dashboard():
    return render_template("custom_dashboard.html")

# Defina um menu link para aparecer na UI do Airflow
custom_menu_link = MenuLink(
    category='Custom Dashboard',
    name="View Custom Dashboard",
    url="/custom_dashboard"
)

# Crie o plugin do Airflow
class CustomDashboardPlugin(AirflowPlugin):
    name = "custom_dashboard_plugin"
    flask_blueprints = [custom_page]
    menu_links = [custom_menu_link]
