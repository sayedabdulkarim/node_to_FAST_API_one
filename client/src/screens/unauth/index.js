import React, { useCallback, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import UnAuthMobileScreen from "./mobile";
import UnAuthWebScreen from "./web";
import { isMobile } from "../../utils/unauthHelper";
import { useTextCycle } from "../../hooks/useTextCycle";
import {
  useLoginMutation,
  useRegisterUserMutation,
} from "../../apiSlices/userApiSlice";
import { setCredentials } from "../../slices/authSlice";
import { handleShowAlert } from "../../utils/commonHelper";

const Index = () => {
  //misc
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const texts = ["Hungry?", "Unexpected guests?", "Cooking gone wrong?"];
  const currentText = useTextCycle(texts, 3000); // 1000ms = 1 second
  //misc
  //useState
  const [open, setOpen] = useState(false);
  const [isOtp, setIsOtp] = useState(false);
  const [user, setUser] = useState(null);
  const [isLoginActive, setIsLoginActive] = useState(true);
  const [signupFormData, setSignUpFormData] = useState({
    phone: "",
    name: "",
    email: "",
  });
  const [loginFormData, setLoginFormData] = useState({
    phone: "",
    otp: "",
  });
  //loader cond
  const [isLoadingOtp, setIsLoadingOtp] = useState(false);

  //queries n mutation
  const [registerUser, { isLoading: registerLoading, error: registerError }] =
    useRegisterUserMutation();

  const [login, { isLoading: loginLoading, error: loginError }] =
    useLoginMutation();
  //

  //func
  const showDrawer = useCallback((isTrue) => {
    setOpen(true);
    setIsLoginActive(isTrue);
  }, []);
  const onClose = useCallback(() => {
    setOpen(false);
  }, []);
  // signup
  const handleSingUpForm = (e) => {
    setSignUpFormData({
      ...signupFormData,
      [e.target.name]: e.target.value,
    });
  };
  const handleSignUpSubmit = async (e) => {
    e.preventDefault();
    const { phone, email, name } = signupFormData;
    const formattedNumber = `+91${phone}`;

    try {
      const res = await registerUser({
        name,
        email,
        phone: formattedNumber,
      }).unwrap();
      console.log(res, " resss");
      handleShowAlert(dispatch, "success", res?.message);
      localStorage.setItem("jwtToken", res.token);
      dispatch(setCredentials({ ...res }));
      navigate("/");
    } catch (err) {
      handleShowAlert(dispatch, "error", err?.data?.message);
      console.log(err, " errr");
    }
    console.log(signupFormData, " signupFormData");
  };

  ///login
  const handleLogInForm = (e) => {
    setLoginFormData({
      ...loginFormData,
      [e.target.name]: e.target.value,
    });
  };

  // Remove Firebase related states and add dummy OTP
  const [dummyOTP] = useState("123456"); // Hardcoded dummy OTP

  // Replace the sendOtp function
  const sendOtp = async () => {
    setIsLoadingOtp(true);
    try {
      const { phone } = loginFormData;
      // Simulate API delay
      await new Promise((resolve) => setTimeout(resolve, 1000));

      handleShowAlert(
        dispatch,
        "success",
        `Please use OTP: ${dummyOTP} (This is a dummy OTP)`
      );
      setIsOtp(true);
      setIsLoadingOtp(false);
    } catch (error) {
      handleShowAlert(
        dispatch,
        "error",
        "Something went wrong. Please try after sometime."
      );
      setIsLoadingOtp(false);
    }
  };

  // Replace the handleVerifyOtp function
  const handleVerifyOtp = async (e) => {
    e.preventDefault();
    setIsLoadingOtp(true);

    try {
      const { otp, phone } = loginFormData;

      if (otp === dummyOTP) {
        // If OTP matches, proceed with login
        const formattedNumber = `+91${phone}`;
        await handleLogInSubmit(formattedNumber);
      } else {
        handleShowAlert(dispatch, "error", "Invalid OTP");
        setIsLoadingOtp(false);
      }
    } catch (error) {
      setIsLoadingOtp(false);
      handleShowAlert(dispatch, "error", "OTP verification failed");
    }
  };

  const handleLogInContinue = (e) => {
    e.preventDefault();
    console.log(loginFormData, " loginFormData");
    sendOtp();
  };

  const handleLogInSubmit = async (phone) => {
    try {
      const res = await login({ phone }).unwrap();
      dispatch(setCredentials({ ...res }));
      setIsOtp(false);
      setIsLoadingOtp(false);
      localStorage.setItem("jwtToken", res.token);
      handleShowAlert(dispatch, "success", res?.message);
      console.log(res, " ressssss");
    } catch (err) {
      setIsLoadingOtp(false);
      handleShowAlert(dispatch, "error", err?.message);
      console.log(err.data.message, " errrrrrrrr from login");
    }
  };
  // console.log(open, " opennnnn");
  return (
    <div>
      {/* <button onClick={() => console.log({ userInfo, name })}>CLick</button> */}
      <div id="recaptcha"></div>
      {isMobile() ? (
        <UnAuthMobileScreen
          loginFormData={loginFormData}
          handleLogInForm={handleLogInForm}
          isOtp={isOtp}
          handleLogInContinue={handleLogInContinue}
          handleVerifyOtp={handleVerifyOtp}
          handleLogInSubmit={handleLogInSubmit}
        />
      ) : (
        <UnAuthWebScreen
          currentText={currentText}
          open={open}
          //drawer
          showDrawer={showDrawer}
          onClose={onClose}
          isLoginActive={isLoginActive}
          //form
          registerLoading={registerLoading}
          signupFormData={signupFormData}
          handleSingUpForm={handleSingUpForm}
          handleSignUpSubmit={handleSignUpSubmit}
          //
          isLoadingOtp={isLoadingOtp}
          loginLoading={loginLoading}
          loginFormData={loginFormData}
          handleLogInForm={handleLogInForm}
          handleLogInContinue={handleLogInContinue}
          handleVerifyOtp={handleVerifyOtp}
          handleLogInSubmit={handleLogInSubmit}
          isOtp={isOtp}
        />
      )}
    </div>
  );
};

export default Index;
