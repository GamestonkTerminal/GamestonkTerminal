from typing import Callable, Any, Optional, List, Dict
from inspect import signature
import importlib
import json
import os
import yaml

from openbb_terminal.api import functions


class Item:
    def __init__(self, name: str, ref: str):
        self.name = name
        self.ref = ref

    def __hash__(self):
        return hash((self.name, self.ref))

    def __eq__(self, other):
        return (self.name, self.ref) == (other.name, other.ref)

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return f"{self.name}"


def employee_representer(dumper: yaml.SafeDumper, item: Item) -> yaml.nodes.MappingNode:
    """Represent an employee instance as a YAML mapping node."""
    return dumper.represent_mapping(
        f"{item.name}",
        {
            "name": item.name,
            "ref": item.ref,
        },
    )


def get_dumper():
    """Add representers to a YAML seriailizer."""
    safe_dumper = yaml.SafeDumper
    safe_dumper.add_representer(Item, employee_representer)
    return safe_dumper


def all_functions() -> List[Tuple[str, str, Callable[..., Any]]]:
    """Uses the base api functions dictionary to get a list of all functions we have linked
    in our API.

    Returns
    ----------
    func_list: List[Tuple[str, str, Callable[..., Any]]]
        A list of functions organized as (path_to_func, view/model, the_function)
    """
    func_list = []
    for key, sub_dict in functions.items():
        for sub_key, item_path in sub_dict.items():
            full_path = item_path.split(".")
            module_path = ".".join(full_path[:-1])
            module = importlib.import_module(module_path)
            target_function = getattr(module, full_path[-1])
            func_list.append((key, sub_key, target_function))
    return func_list


def groupby(orig_list: List[Any], index: int) -> dict[Any, Any]:
    """Groups a list of iterable by the index provided

    Parameters
    ----------
    orig_list: List[Any]
        A list of iterables
    index: int
        The index to groupby

    Returns
    ----------
    grouped: dict[Any, Any]
        Group information where keys are the groupby item and values are the iterables
    """
    grouped: Dict[Any, Any] = {}
    for item in orig_list:
        if item[index] in grouped:
            grouped[item[index]].append(item)
        else:
            grouped[item[index]] = [item]
    return grouped


def generate_documentation(
    base: str, key: str, value: List[Tuple[str, str, Callable[..., Any]]]
):
    models = list(filter(lambda x: x[1] == "model", value))
    views = list(filter(lambda x: x[1] == "view", value))
    model_type = Optional[Tuple[str, str, Callable[..., Any]]]
    model: model_type = models[0] if models else None
    view: model_type = views[0] if views else None
    for end in key.split("."):
        base += f"/{end}"
        if not os.path.isdir(base):
            os.mkdir(base)
    with open(f"{base}/_index.md", "w") as f:
        f.write(f"# {key}\n\n")
        if view:
            f.write(
                "To obtain charts, make sure to add `chart=True` as the last parameter\n\n"
            )
        if model:
            f.write(f"## Get underlying data \n###{key}{signature(model[2])}\n\n")
            m_docs = str(model[2].__doc__)[:-5]
            f.write(f"{m_docs}\n")
        if view:
            if model:
                f.write("\n")
            v_docs = str(view[2].__doc__)[:-5]
            temp = str(signature(view[2]))
            # TODO: This breaks if there is a ')' inside the function arguments
            idx = temp.find(")")
            new_signature = temp[:idx] + ", chart=True" + temp[idx:]
            f.write(f"## Getting charts \n###{key}{new_signature}\n\n")
            f.write(f"{v_docs}\n")


def generate_dict(values: list[tuple[str, str, Callable[..., Any]]]):
    final_dict: dict[Item, Any] = {}
    for func_path, _, _ in values:
        whole_path = func_path.split(".")
        first = whole_path[0]
        partial_p_str = whole_path[whole_path.index(first) - 1]
        partial_path = partial_p_str.split(".")
        first_obj = Item(first, "api/" + "/".join(partial_path))
        if first not in final_dict:
            final_dict[first_obj] = {}
        temp_ref = final_dict[first_obj]
        for item in whole_path[1:]:
            partial_p_str = whole_path[whole_path.index(item) - 1]
            partial_path = partial_p_str.split(".")
            item_object = Item(item, "api/" + "/".join(partial_path))
            if item_object not in temp_ref:
                temp_ref[item_object] = {}
            temp_ref = temp_ref[item_object]
        temp_ref["ref"] = "api/" + "/".join(whole_path)

    return final_dict


def generate_output(the_dict: dict[str, Any]):
    for key, value in the_dict.items():
        print(key)
        print(value)


if __name__ == "__main__":
    folder_path = os.path.realpath("./website/content/api")
    main_path = os.path.realpath("./website/data/menu/main.yml")
    funcs = all_functions()
    grouped_funcs = groupby(funcs, 0)
    for k, v in grouped_funcs.items():
        # generate_documentation(folder_path, k, v)
        pass
    func_dict = generate_dict(funcs)
    with open(r'test.yaml', 'w') as file:
        documents = yaml.dump(func_dict, file)
    print(func_dict)
    # print(yaml.dump(func_dict))
    with open(main_path) as f:
        dataMap = yaml.safe_load(f)
    # print(json.dumps(dataMap, sort_keys=True, indent=4, separators=(",", ": ")))
    # print(yaml.dump(func_dict, Dumper=get_dumper()))
    # generate_output(func_dict)
