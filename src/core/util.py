def populate_pydantic_base_model_from_dict(class_value, dict_value, upper_keys=False):
    return class_value(
        **{
            key: dict_value[key.upper() if upper_keys else key]
            for key in [key for key in class_value.model_fields.keys()]
        }
    )
