from nicegui import ui

def set_cafe(config):
    with ui.row():
        ui.link_target("CAFE")
        ui.label(config.get_text("task_cafe")).style('font-size: x-large')
    
    
    # 收集
    with ui.row():
        ui.checkbox(config.get_text("cafe_collect_desc")).bind_value(config.userconfigdict, "CAFE_COLLECT")
    
    # 摸头
    with ui.row():
        ui.checkbox(config.get_text("cafe_touch_desc")).bind_value(config.userconfigdict, "CAFE_TOUCH")
        ui.checkbox(config.get_text("enable_diff_touch")).bind_value(config.userconfigdict, "CAFE_TOUCH_WAY_DIFF").bind_visibility_from(config.userconfigdict, "CAFE_TOUCH")
        
    # 一号咖啡馆邀请
    ui.number("1" + config.get_text("cafe_invite_desc"), min=0, max=5, precision=0, step=1).bind_value(config.userconfigdict, "CAFE1_INVITE_SEQ", forward=lambda x:int(x), backward=lambda x: int(x)).bind_visibility_from(config.userconfigdict, "CAFE_TOUCH").style("width: 300px;")
    # 二号咖啡馆邀请
    ui.number("2" + config.get_text("cafe_invite_desc"), min=0, max=5, precision=0, step=1).bind_value(config.userconfigdict, "CAFE2_INVITE_SEQ", forward=lambda x:int(x), backward=lambda x: int(x)).bind_visibility_from(config.userconfigdict, "CAFE_TOUCH").style("width: 300px;")

    ui.checkbox(config.get_text("config_cafe_samename_defer")).bind_value(config.userconfigdict, "CAFE_INVITE_SAME_NAME_DELAY")
    


    # 关于视角的提示
    ui.label(config.get_text("config_cafe_attention"))
    full_camera = ui.checkbox(config.get_text("config_camera_full")).bind_value(config.userconfigdict, "CAFE_CAMERA_FULL").bind_visibility_from(config.userconfigdict, "CAFE_TOUCH")
    full_camera.set_value(True)
    full_camera.set_enabled(False)