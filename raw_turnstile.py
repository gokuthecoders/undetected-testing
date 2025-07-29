from seleniumbase import SB

with SB(uc=True, test=True) as sb:
    url = "https://new21.gdtot.dad/file/1023867990"
    sb.uc_open_with_reconnect(url)
    sb.uc_gui_click_captcha()
    sb.assert_element("img#captcha-success", timeout=3)
    sb.set_messenger_theme(location="top_left")
    sb.post_message("SeleniumBase wasn't detected", duration=3)
    sb.save_screenshot_to_logs()
