# coding: utf-8

"""
    Python API wrapper for Jellyfish Media Server

    The version of the OpenAPI document: 0.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint


class ComponentOptionsRTSP(BaseModel):
    """
    Options specific to the RTSP component
    """

    keep_alive_interval: Optional[conint(strict=True, ge=0)] = Field(
        15000,
        alias="keepAliveInterval",
        description="Interval (in ms) in which keep-alive RTSP messages will be sent to the remote stream source",
    )
    pierce_nat: Optional[StrictBool] = Field(
        True,
        alias="pierceNat",
        description="Whether to attempt to create client-side NAT binding by sending an empty datagram from client to source, after the completion of RTSP setup",
    )
    reconnect_delay: Optional[conint(strict=True, ge=0)] = Field(
        15000,
        alias="reconnectDelay",
        description="Delay (in ms) between successive reconnect attempts",
    )
    rtp_port: Optional[conint(strict=True, le=65535, ge=1)] = Field(
        20000, alias="rtpPort", description="Local port RTP stream will be received at"
    )
    source_uri: StrictStr = Field(
        ..., alias="sourceUri", description="URI of RTSP source stream"
    )
    __properties = [
        "keepAliveInterval",
        "pierceNat",
        "reconnectDelay",
        "rtpPort",
        "sourceUri",
    ]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ComponentOptionsRTSP:
        """Create an instance of ComponentOptionsRTSP from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ComponentOptionsRTSP:
        """Create an instance of ComponentOptionsRTSP from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComponentOptionsRTSP.parse_obj(obj)

        _obj = ComponentOptionsRTSP.parse_obj(
            {
                "keep_alive_interval": obj.get("keepAliveInterval")
                if obj.get("keepAliveInterval") is not None
                else 15000,
                "pierce_nat": obj.get("pierceNat")
                if obj.get("pierceNat") is not None
                else True,
                "reconnect_delay": obj.get("reconnectDelay")
                if obj.get("reconnectDelay") is not None
                else 15000,
                "rtp_port": obj.get("rtpPort")
                if obj.get("rtpPort") is not None
                else 20000,
                "source_uri": obj.get("sourceUri"),
            }
        )
        return _obj
