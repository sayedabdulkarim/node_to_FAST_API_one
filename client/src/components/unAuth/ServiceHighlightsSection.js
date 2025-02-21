import React from "react";

const ServiceHighlights = () => {
  return (
    <div className="tracking_section">
      <div className="trackingBody">
        <div className="items">
          <div className="trackImg">
            <img
              className="photo"
              width="105"
              height="199"
              src="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_210,h_398/4x_-_No_min_order_x0bxuf"
              alt="facilities_one_image"
            />
          </div>
          <div className="trackHead">No Minimum Order</div>
          <div className="trackPara">
            Order in for yourself or for the group, with no restrictions on
            order value
          </div>
        </div>
        <div className="items">
          <div className="trackImg">
            <img
              className="photo"
              width="112"
              height="206"
              src="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_224,h_412/4x_Live_order_zzotwy"
              alt="facilities_one_image"
            />
          </div>
          <div className="trackHead">Live Order Tracking</div>
          <div className="trackPara">
            Know where your order is at all times, from the restaurant to your
            doorstep
          </div>
        </div>
        <div className="items">
          <div className="trackImg">
            <img
              className="photo"
              width="124"
              height="188"
              src="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_248,h_376/4x_-_Super_fast_delivery_awv7sn"
              alt="facilities_one_image"
            />
          </div>
          <div className="trackHead">Lightning-Fast Delivery</div>
          <div className="trackPara">
            Experience Swiggy's superfast delivery for food delivered fresh
            &amp; on time
          </div>
        </div>
      </div>
    </div>
  );
};
export default ServiceHighlights;
