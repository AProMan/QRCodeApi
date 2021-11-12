# api_app.py
from flasgger import Swagger

# API可视化管理
swagger_config = Swagger.DEFAULT_CONFIG

# 标题
swagger_config['title'] = config.SWAGGER_TITLE
# 描述信息
swagger_config['description'] = config.SWAGGER_DESC
# Host
swagger_config['host'] = config.SWAGGER_HOST

# 实例化
swagger = Swagger(app, config=swagger_config)
