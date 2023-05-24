import re
from datetime import datetime, timedelta
from typing import List, Match, Optional, Tuple

from dateutil.relativedelta import relativedelta

# Necessary for OpenBB keywords
MONTHS_VALUE = {
    "JANUARY": 1,
    "FEBRUARY": 2,
    "MARCH": 3,
    "APRIL": 4,
    "MAY": 5,
    "JUNE": 6,
    "JULY": 7,
    "AUGUST": 8,
    "SEPTEMBER": 9,
    "OCTOBER": 10,
    "NOVEMBER": 11,
    "DECEMBER": 12,
}

WEEKDAY_VALUE = {
    "MONDAY": 0,
    "TUESDAY": 1,
    "WEDNESDAY": 2,
    "THURSDAY": 3,
    "FRIDAY": 4,
    "SATURDAY": 5,
    "SUNDAY": 6,
}


def match_and_return_openbb_keyword_date(keyword: str) -> str:
    """Return OpenBB keyword into date

    Parameters
    ----------
    keyword : str
        String with potential OpenBB keyword (e.g. 1MONTHAGO,LASTFRIDAY,3YEARSFROMNOW,NEXTTUESDAY)

    Returns
    ----------
        str: Date with format YYYY-MM-DD
    """
    match = re.match(r"^\$(\d+)([A-Z]+)AGO$", keyword)
    now = datetime.now()
    if match:
        integer_value = int(match.group(1))
        time_unit = match.group(2)
        if time_unit == "DAYS":
            return (now - timedelta(days=integer_value)).strftime("%Y-%m-%d")
        if time_unit == "MONTHS":
            return (now - relativedelta(months=integer_value)).strftime("%Y-%m-%d")
        if time_unit == "YEARS":
            return (now - relativedelta(years=integer_value)).strftime("%Y-%m-%d")

    match = re.match(r"^\$(\d+)([A-Z]+)FROMNOW$", keyword)
    if match:
        integer_value = int(match.group(1))
        time_unit = match.group(2)
        if time_unit == "DAYS":
            return (now + timedelta(days=integer_value)).strftime("%Y-%m-%d")
        if time_unit == "MONTHS":
            return (now + relativedelta(months=integer_value)).strftime("%Y-%m-%d")
        if time_unit == "YEARS":
            return (now + relativedelta(years=integer_value)).strftime("%Y-%m-%d")

    match = re.search(r"\$LAST(\w+)", keyword)
    if match:
        time_unit = match.group(1)
        # Check if it corresponds to a month
        if time_unit in list(MONTHS_VALUE.keys()):
            # Calculate the year and month for last month date
            if now.month > MONTHS_VALUE[time_unit]:
                # If the current month is greater than the last date month, it means it is this year
                return datetime(now.year, MONTHS_VALUE[time_unit], 1).strftime(
                    "%Y-%m-%d"
                )

            return datetime(now.year - 1, MONTHS_VALUE[time_unit], 1).strftime(
                "%Y-%m-%d"
            )

        # Check if it corresponds to a week day
        if time_unit in list(WEEKDAY_VALUE.keys()):
            if datetime.weekday(now) > WEEKDAY_VALUE[time_unit]:
                return (
                    now
                    - timedelta(datetime.weekday(now))
                    + timedelta(WEEKDAY_VALUE[time_unit])
                ).strftime("%Y-%m-%d")
            return (
                now
                - timedelta(7)
                - timedelta(datetime.weekday(now))
                + timedelta(WEEKDAY_VALUE[time_unit])
            ).strftime("%Y-%m-%d")

    match = re.search(r"\$NEXT(\w+)", keyword)
    if match:
        time_unit = match.group(1)
        # Check if it corresponds to a month
        if time_unit in list(MONTHS_VALUE.keys()):
            # Calculate the year and month for next month date
            if now.month < MONTHS_VALUE[time_unit]:
                # If the current month is greater than the last date month, it means it is this year
                return datetime(now.year, MONTHS_VALUE[time_unit], 1).strftime(
                    "%Y-%m-%d"
                )

            return datetime(now.year + 1, MONTHS_VALUE[time_unit], 1).strftime(
                "%Y-%m-%d"
            )

        # Check if it corresponds to a week day
        if time_unit in list(WEEKDAY_VALUE.keys()):
            if datetime.weekday(now) < WEEKDAY_VALUE[time_unit]:
                return (
                    now
                    - timedelta(datetime.weekday(now))
                    + timedelta(WEEKDAY_VALUE[time_unit])
                ).strftime("%Y-%m-%d")
            return (
                now
                + timedelta(7)
                - timedelta(datetime.weekday(now))
                + timedelta(WEEKDAY_VALUE[time_unit])
            ).strftime("%Y-%m-%d")

    return ""


def parse_openbb_script(
    raw_lines: List[str],
    script_inputs: List[str] = None,
) -> Tuple[str, List[str]]:
    """
    Parse .openbb script

    Parameters
    ----------
    raw_lines : List[str]
        Lines from .openbb script
    script_inputs: str, optional
        Inputs to the script that come externally

    Returns
    -------
    str
        Error that occurred - if empty means no error
    List[str]
        Processed lines from .openbb script that can be run by the OpenBB Terminal
    """
    ROUTINE_VARS = dict()
    if script_inputs:
        ROUTINE_VARS["$ARGV"] = script_inputs

    ## LOOK FOR NEW VARIABLES BEING DECLARED FROM USERS
    lines_without_declarations = list()
    for line in raw_lines:
        # Check if this line has a variable attribution
        # This currently allows user to override ARGV parameter
        if "$" in line and "=" in line:
            match = re.search(r"\$(\w+)\s*=\s*([\d,-.\s]+)", line)
            if match:
                VAR_NAME = match.group(1)
                VAR_VALUES = match.group(2)
                ROUTINE_VARS["$" + VAR_NAME] = (
                    VAR_VALUES if "," not in VAR_VALUES else VAR_VALUES.split(",")
                )
            else:
                lines_without_declarations.append(line)
        else:
            lines_without_declarations.append(line)

    # At this stage our ROUTINE_VARS should be completed coming from external AND from internal
    # Now we want to replace the ROUTINE_VARS to where applicable throughout the .openbb script
    # Due to this implementation, a variable declared at the end will still be effective

    lines_with_vars_replaced = list()
    foreach_loop_found = False
    for line in lines_without_declarations:
        # Save temporary line to ensure that all vars get replaced by correct vars
        templine = line

        # Found 'end' keyword which means that a loop has terminated
        if re.match(r"^\s*end\s*$", line, re.IGNORECASE):
            # Check whether the foreach loop has started or not
            if not foreach_loop_found:
                return (
                    "[red]The script has a foreach loop that terminates before it gets started."
                    "Add the keyword 'foreach' to explicitly start loop[/red]",
                    [],
                )
            foreach_loop_found = False

        else:
            # Found 'foreach' keyword which means there needs to be a matching 'end'
            if re.search(r"foreach", line, re.IGNORECASE):
                foreach_loop_found = True

            # Regular expression pattern to match variables starting with $
            pattern = r"(?<!\$)(\$(\w+)(\[[^]]*\])?)(?![^\[]*\])"

            # Find all matches of the pattern in the line
            matches: Optional[List[Match[str]]] = re.findall(pattern, line)

            if matches:
                for match in matches:
                    if match:
                        VAR_NAME = "$" + match[1]
                        VAR_SLICE = match[2][1:-1] if match[2] else ""

                        # Within a list refers to a single element
                        if VAR_SLICE.isdigit():
                            # This is an edge case for when the user has a variable such as $DATE = 2022-01-01
                            # We want the user to be able to access it with $DATE or $DATE[0] and the latest
                            # in python will only take the first '2'
                            if VAR_SLICE == "0":
                                if VAR_NAME in ROUTINE_VARS:
                                    values = eval(f'ROUTINE_VARS["{VAR_NAME}"]')
                                    if isinstance(values, list):
                                        templine = templine.replace(
                                            match[0],
                                            eval(f"values[{VAR_SLICE}]"),
                                        )
                                    else:
                                        templine = templine.replace(match[0], values)
                                else:
                                    return (
                                        f"[red]Variable {VAR_NAME} not given "
                                        "for current routine script.[/red]",
                                        [],
                                    )

                            # Only enters here when any other index from 0 is used
                            else:
                                if VAR_NAME in ROUTINE_VARS:
                                    variable = eval(f'ROUTINE_VARS["{VAR_NAME}"]')
                                    length_variable = (
                                        len(variable)
                                        if isinstance(variable, list)
                                        else 1
                                    )

                                    # We use <= because we are using 0 index based lists
                                    if length_variable <= int(VAR_SLICE):
                                        return (
                                            f"[red]Variable {VAR_NAME} only has "
                                            f"{length_variable} elements and there "
                                            f"was an attempt to access it with index {VAR_SLICE}.[/red]",
                                            [],
                                        )
                                    else:
                                        templine = templine.replace(
                                            match[0],
                                            variable[int(VAR_SLICE)],
                                        )
                                else:
                                    return (
                                        f"[red]Variable {VAR_NAME} not given "
                                        "for current routine script.[/red]",
                                        [],
                                    )

                        # Involves slicing which is a bit more tricky to use eval on
                        elif (
                            ":" in VAR_SLICE
                            and len(VAR_SLICE.split(":")) == 2
                            and (
                                VAR_SLICE.split(":")[0].isdigit()
                                or VAR_SLICE.split(":")[1].isdigit()
                            )
                        ):
                            slicing_tuple = "slice("
                            slicing_tuple += (
                                VAR_SLICE.split(":")[0]
                                if VAR_SLICE.split(":")[0].isdigit()
                                else "None"
                            )
                            slicing_tuple += ","
                            slicing_tuple += (
                                VAR_SLICE.split(":")[1]
                                if VAR_SLICE.split(":")[1].isdigit()
                                else "None"
                            )
                            slicing_tuple += ")"

                            templine = templine.replace(
                                match[0],
                                ",".join(
                                    eval(f'ROUTINE_VARS["{VAR_NAME}"][{slicing_tuple}]')
                                ),
                            )

                        # Just replace value without slicing or list
                        else:
                            if VAR_SLICE and int(VAR_SLICE) < 0:
                                return (
                                    f"[red]Negative index on {VAR_NAME} is not allowed[/red]",
                                    [],
                                )
                            if VAR_NAME in ROUTINE_VARS:
                                templine = templine.replace(
                                    match[0],
                                    eval(f'ROUTINE_VARS["{VAR_NAME}"]'),
                                )
                            else:
                                # Check if this is an OpenBB keyword variable like
                                # 1MONTHAGO,LASTFRIDAY,3YEARSFROMNOW,NEXTTUESDAY
                                # and decode it into the right date if it exists
                                potential_date_match = (
                                    match_and_return_openbb_keyword_date(VAR_NAME)
                                )
                                if potential_date_match:
                                    templine = templine.replace(
                                        match[0], potential_date_match
                                    )
                                else:
                                    return (
                                        f"[red]Variable {VAR_NAME} not given for "
                                        "current routine script.[/red]",
                                        [],
                                    )

        lines_with_vars_replaced.append(templine)

    # If this flags ends in True it means that the script routine has a foreach loop that never terminates
    if foreach_loop_found:
        return (
            "[red]The script has a foreach loop that doesn't terminate. "
            "Add the keyword 'end' to explicitly terminate loop[/red]",
            [],
        )

    # Finally the only remaining thing to address are the foreach loops. For that we'll go through
    # those lines and unroll the arguments that will be iterated by.
    # Note that the fact that we checked before that the amount of foreach and end matches allow us
    # to be confident that the script has no clear issues.

    within_foreach = False
    foreach_lines_loop: List[str] = list()

    final_lines = list()
    for line in lines_with_vars_replaced:
        # Found 'foreach' header associated with loop
        match = re.search(r"(?<=foreach \$\$VAR in )([A-Z,]+)", line, re.IGNORECASE)
        if match:
            foreach_loop = match.group(1).split(",")
            within_foreach = True

        # We are inside a loop and this is a line that we will want to replicate,
        # so we need to temporarily store it until we reach the end
        elif within_foreach:
            # Found 'end' keyword which means that the foreach loop has reached the end
            if re.match(r"^\s*end\s*$", line, re.IGNORECASE):
                # Now we want to process what we were waiting for before

                # Iterate through main foreach header
                for var in foreach_loop:
                    # Iterate through all lines within foreach and end loop
                    for foreach_line_loop in foreach_lines_loop:
                        final_lines.append(
                            foreach_line_loop.replace("$$VAR", var).strip()
                        )

                # Since this has been processed we reset the foreach loop lines
                within_foreach = False
                foreach_lines_loop = list()

            else:
                foreach_lines_loop.append(line)

        else:
            final_lines.append(line)
    print(final_lines)
    return "", final_lines
