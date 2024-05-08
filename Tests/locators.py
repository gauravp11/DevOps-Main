class LoginPageLocators:
    USERNAME_INPUT = "//input[@type='text' and @name='username']"
    PASSWORD_INPUT = "//input[@type='password' and @name='password']"
    LOGIN_BUTTON = "//div[contains(@class,'submit')]//input[@value='Log in']"

class CommonLocators:
    CheckUserName = "//div[@id='header']//div[@id='user-tools']/strong[.='admindocker']"
    clickSave = "//div[@class='submit-row']//input[@value='Save']"
    CheckBrandingName = "//div[@id='branding']//h1/a/span"

class HomePageLocators:
    CreatePatner = "//a[.='Partners']//ancestor::table//tr[@class='model-partner']//th/a"
    CreateTask = "//a[.='Tasks']//ancestor::table//tr[@class='model-task']//th/a"
    CreatThemes = "//a[.='Themes']//ancestor::table//tr[@class='model-theme']//th/a"
    CreateGroup = "//a[.='Groups']//ancestor::table//tr[@class='model-group']//th/a"
    CreateUser = "//a[.='Users']//ancestor::table//tr[@class='model-user']//th/a"
    CreateTicket = "//a[.='Internal Tickets']//ancestor::table//tr[@class='model-ticket']//th/a"
    
class TaskPageLocators:
    addTaskButtonClick = "//div[@id='content-main']//ul//a[@class='addlink']"
    addTitle = "//div[contains(@class,'container')]//input[@name='title']"
    assignedtoClick = "//span[contains(@class,'select2') and @role='combobox' and contains(@aria-labelledby,'id_user')]"
    selectUserAssign = "//li[@role='option' and .='admindocker']"
    partnerToclick = "//span[contains(@class,'select2') and @role='combobox' and contains(@aria-labelledby,'id_partner')]"
    selectOptionPart = "//li[@role='option' and .='TestPartner']"
    deadlineInput = "//input[@name='deadline']"
    selectPriority = "//select[@name='priority']"
    inputPrioriy = "//select[@name='priority']//option[.='High']"
    inputDecs = "//textarea[@name='description']"
    checkTitle = "//table[@id='result_list']//tbody//td[@class='field-title']"

class PartnerPageLocators:
    addButtonClick = "//div[@id='content-main']//ul//a[@class='addlink']"
    addName = "//div[contains(@class,'field-name')]//input[@name='name']"
    addEmail = "//div[contains(@class,'field-name')]//input[@name='email']"
    addPhone = "//div[contains(@class,'field-phone')]//input[@name='phone']"
    addNotes = "//div[contains(@class,'field-comment')]//textarea[@name='comment']"
    clickIsCompany = "//div[contains(@class,'field-is_company')]//select[@name='is_company']"
    selectIsCompany = "//div[contains(@class,'field-is_company')]//select[@name='is_company']//option[.='Yes']"
    CheckForName = "//table[@id='result_list']//tbody//td[@class='field-name']"

class ThemePagelocators:
    addThemeButtonClick = "//div[@id='content-main']//ul//a[@class='addlink']"
    addThemeName = "//label[@for='id_name']//ancestor::div[@class='flex-container']//input"
    addEnvName = "//input[@name='env_name']"
    addTitleName = "//input[@name='title']"
    CheckThemeName = "//table[@id='result_list']//tbody//th[@class='field-name']"

class UserPageLocators:
    addUserClick = "//div[@id='content-main']//ul//a[@class='addlink']"
    inputUserName = "//input[@name='username']"
    inputPassword = "//input[@name='password1' and@type='password']"
    confirmPassword = "//input[@name='password2' and@type='password']"
    
    #After user creation 
    inputFirstName = "//input[@name='first_name']"
    inputLastName = "//input[@name='last_name']"
    
    # Grant
    isStaffTrue = "//input[@name='is_staff']"
    addInternalTicket = "//option[contains(@title,'add Internal Ticket')]"
    
    checkUser = "//table[@id='result_list']//tbody//th[@class='field-username']"
    
class TicketPageLocators:
    addTicketButtonClick = "//div[@id='content-main']//ul//a[@class='addlink']"
    addTitle = "//input[@name='title']"
    selectPriority = "//select[@name='priority']"
    inputPrioriy = "//select[@name='priority']//option[.='High']"
    clickassignedTo = "//select[@id='id_assigned_to']"
    inputTO = "//select[@id='id_assigned_to']//option[.='admindocker']"
    checkTicket = "//table[@id='result_list']//tbody//th[@class='field-title']"
    
    
