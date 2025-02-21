import React from "react";
const Index = () => {
  return (
    <div className="footerContainer">
      <div className="foodBody">
        {/* near me links */}
        <div id="near-me-links" className="footerPart1">
          <h4 className="baseFooter">Explore Every Restaurants Near Me</h4>
          <div className="pageFooter">
            <ul className="groundLink">
              <li className="explore">
                <a className="exploreLink top" href="/restaurants-near-me">
                  explore restaurants near me
                </a>
              </li>
            </ul>
            <ul className="bottomLink">
              <li className="related">
                <a className="near top" href="/best-restaurants-near-me">
                  explore top rated restaurants near me
                </a>
              </li>
            </ul>
          </div>
        </div>
        {/* copyrights */}
        <div className="footerPart2">
          <div className="top">
            <a href="/">
              <img
                className=""
                imageurl="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_284/Logo_f5xzza"
                width="142"
                imageid=""
                alt="img renderer"
                src="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_284/Logo_f5xzza"
              />
            </a>
          </div>
          <div className="middle">© 2023 Swiggy</div>
          <div className="bottom">
            <a
              className="footIcons"
              href="https://www.facebook.com/swiggy.in"
              rel="nofollow noopener noreferrer"
              alt="facebook"
              target="_blank"
            >
              <img
                className=""
                imageurl="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_48,h_48/icon-facebook_tfqsuc"
                width="24"
                height="24"
                imageid=""
                alt="img renderer"
                src="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_48,h_48/icon-facebook_tfqsuc"
              />
            </a>
            <a
              className="footIcons"
              href="https://pinterest.com/swiggyindia"
              rel="nofollow noopener noreferrer"
              alt="pintrest"
              target="_blank"
            >
              <img
                className=""
                imageurl="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_48,h_48/icon-pinterest_kmz2wd"
                width="24"
                height="24"
                imageid=""
                alt="img renderer"
                src="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_48,h_48/icon-pinterest_kmz2wd"
              />
            </a>
            <a
              className="footIcons"
              href="https://instagram.com/swiggyindia/"
              rel="nofollow noopener noreferrer"
              alt="instagram"
              target="_blank"
            >
              <img
                className=""
                imageurl="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_48,h_48/icon-instagram_b7nubh"
                width="24"
                height="24"
                imageid=""
                alt="img renderer"
                src="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_48,h_48/icon-instagram_b7nubh"
              />
            </a>
            <a
              className="footIcons"
              href="https://twitter.com/swiggy"
              rel="nofollow noopener noreferrer"
              alt="twitter"
              target="_blank"
            >
              <img
                className=""
                imageurl="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_48,h_48/icon-twitter_gtq8dv"
                width="24"
                height="24"
                imageid=""
                alt="img renderer"
                src="https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_48,h_48/icon-twitter_gtq8dv"
              />
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Index;
