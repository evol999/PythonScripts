import pyperclip
import datetime

StepName = None

def get_step_name():
    global StepName
    if StepName is None:
        StepName = input("Enter STEP name:\n")
    return StepName

def gen_func_prot():
    StepName = get_step_name()
    string = "bool Pre_STEP_{step}(void);\nint Post_STEP_{step}(char *Result);".format(step = StepName)
    pyperclip.copy(string)
    print("Funtion prototypes copied to clipboard")

def gen_step_list_items():
    StepName = get_step_name()
    string = "\t{{ STEP_{step},				INPUT_NONE,			0,			0,				0,				NULL,						Pre_STEP_{step},					Post_STEP_{step} }},".format(step = StepName)
    pyperclip.copy(string)
    print("Step list items copied to clipboard")

def gen_step_skeleton_definitions():
    StepName = get_step_name()
    now = datetime.datetime.now()
    string = """/** --------------------------------------------------------------
 * Functcion Name:	Pre_STEP_{step}
 * Autor:           @carodriguez
 * Date:            {day}/{month}/{year}
 * Description:
 * Parameters:
 * - none
 * Return:
 * - none
 * Notes:
 */
bool Pre_STEP_{step}(void)
{{
	return TRUE;

LBL_FALSE:
	return FALSE;
}}

/** ------------------------------------------------------------------------------
 * Function Name:	Post_STEP_{step}
 * Author:			@carodriguez 
 * Date:		 	{day}/{month}/{year}
 * Description:		Shows menu for preauthorization transaction.
 * Parameters:
 *  - none
 * Return:
 *  - none
 * Notes:
 */
int Post_STEP_{step}(char *Result)
{{
	return STM_RET_NEXT;
LBL_ERROR:
	return STM_RET_CANCEL;
}}""".format(step = StepName, day = now.day, month = now.month, year = now.year)
    pyperclip.copy(string)
    print("Step list items copied to clipboard")

ans = True
while ans:
    print ("""
    1. STEP function prototypes
    2. STEP list items.
    3. STEP skeleton definitions
    4. Exit/Quit
    """)
    selection = input("What would you like to do? ") 
    if selection=="1":
        gen_func_prot()
    elif selection=="2":
        gen_step_list_items()
    elif selection=="3":
        gen_step_skeleton_definitions()
    elif selection=="4":
      print("\n Goodbye")
      ans = False
    elif selection !="":
      print("\n Not Valid Choice Try again") 
