import React from "react";
const AppDownloadSection = () => {
  return (
    <div className="download_section">
      <div className="downloadBody">
        <div className="downloadPocket">Restaurants in your pocket</div>
        <div className="downloadPara">
          Order from your favorite restaurants &amp; track on the go, with the
          all-new Swiggy app.
        </div>
        <div>
          <a
            href="https://play.google.com/store/apps/details?id=in.swiggy.android"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img
              alt=""
              className="downloadGoogle"
              height="54"
              src="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_108/play_ip0jfp"
            />
          </a>
          <a
            href="https://itunes.apple.com/in/app/swiggy-food-order-delivery/id989540920"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img
              alt=""
              className="downloadApple"
              height="54"
              src="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_108/iOS_ajgrty"
            />
          </a>
        </div>
        <img
          alt=""
          className="downloadZone"
          width="384"
          height="489"
          src="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_768,h_978/pixel_wbdy4n"
        />
        <img
          alt=""
          className="downloadHub"
          width="384"
          height="489"
          src="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_768,h_978/iPhone_wgconp_j0d1fn"
        />
      </div>
    </div>
  );
};
export default AppDownloadSection;
