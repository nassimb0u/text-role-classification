utils_config = {
    "data_dir": {
        "ICPR2022Real": "/kaggle/working/ICPR2022Real.tar.gz",
        "CHIME-R": "/text-role-classification/datasets/CHIME-R.tar.gz",
        "EconBiz": "/text-role-classification/datasets/EconBiz.tar.gz",
    },
    "column_names": {
        "image": "image",
        "text": "words",
        "boxes": "bboxes",
        "label": "labels",
    },
    "pretrained_model": "microsoft/layoutlmv3-base",
    "label_list": [
        "CHART_TITLE",
        "LEGEND_TITLE",
        "LEGEND_LABEL",
        "AXIS_TITLE",
        "TICK_LABEL",
        "TICK_GROUPING",
        "MARK_LABEL",
        "VALUE_LABEL",
        "OTHER",
    ],
    "return_entity_level_metrics": False,
}
