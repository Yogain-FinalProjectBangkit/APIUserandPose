import io
import base64
import sqlalchemy as sqlx

from flask import Blueprint, request, jsonify
from schema.meta import engine, meta
from sqlx import sqlx_easy_orm
from utils import get_images_url_from_column_images, run_query

pose_bp = Blueprint("pose", __name__, url_prefix="/")


@pose_bp.route("/pose/", methods=["GET"])
def pose_detail():

    p = sqlx_easy_orm(engine, meta.tables.get("pose"))
    row = p.get(
        [
            "pose.id",
            "pose.title",
            "pose.images",
            "pose.description"
        ],        
    )

    if row is not None:

        pose = row.pose

        if pose is not None:
            data = {}
            data["id"] = pose.id
            data["title"] = pose.title
            data["images"] = get_images_url_from_column_images(pose.images)
            data["description"] = pose.description
    
            return jsonify({ "message": "success, pose found", "data": data }), 200

    return jsonify({ "message": "error, pose unknown" }), 400


@pose_bp.route("/posecoba/", methods=["GET"])
def pose_yoga():
    
    data = []
    ps_yg = run_query(f"SELECT*FROM pose")
                
    images = get_images_url_from_column_images(ps_yg[0]["images"])
    req = {
                "id": ps_yg["id"],
                "title": ps_yg[0]["title"],
                "images": images[0] if len(images) > 0 else "",
                "description": ps_yg[0]["description"]
                }
    data.append(req)
    return jsonify({ "data": data, "message": "success, cart found" }), 200
