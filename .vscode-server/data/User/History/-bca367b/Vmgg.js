import React from "react";

export const Box = () => {
  return (
    <div className="relative w-[1440px] h-[594px]">
      <div className="fixed w-[1440px] h-[594px] top-0 left-0 bg-black">
        <div className="absolute w-[1126px] h-[32px] top-[58px] left-[160px]">
          <div className="absolute w-[108px] top-0 left-0 [font-family:'Roboto-Regular',Helvetica] font-normal text-beige text-[24px] tracking-[0] leading-[normal] whitespace-nowrap">
            MeetHub
          </div>
          <div className="absolute w-[70px] top-[5px] left-[1047px] [font-family:'Roboto-Regular',Helvetica] font-normal text-beige text-[18px] tracking-[0] leading-[normal]">
            Account
          </div>
          <div className="absolute w-[138px] top-[5px] left-[855px] [font-family:'Roboto-Regular',Helvetica] font-normal text-beige text-[18px] tracking-[0] leading-[normal]">
            List a space
          </div>
          <img className="w-[1120px] h-px top-[31px] left-0 absolute object-cover" alt="Line" src="line-1.svg" />
        </div>
        <div className="absolute w-[1120px] h-[72px] top-[465px] left-[160px] bg-[#f6f4f0] rounded-[100px]">
          <div className="absolute w-[60px] h-[60px] top-[6px] left-[1053px] bg-beige rounded-[30px]">
            <img className="absolute w-[37px] h-[34px] top-[14px] left-[14px]" alt="Image" src="image-1.png" />
          </div>
          <div className="absolute w-[168px] h-[42px] top-[15px] left-[33px]">
            <div className="absolute w-[65px] top-0 left-0 [font-family:'Roboto-Regular',Helvetica] font-normal text-[#000000] text-[16px] tracking-[0] leading-[normal]">
              Where
            </div>
            <div className="w-[164px] absolute top-[21px] left-0 [font-family:'Roboto-Regular',Helvetica] font-normal text-searchbar text-[18px] tracking-[0] leading-[normal]">
              Enter location
            </div>
          </div>
          <div className="absolute w-[155px] h-[42px] top-[15px] left-[568px]">
            <div className="absolute w-[48px] top-0 left-0 [font-family:'Roboto-Regular',Helvetica] font-normal text-[#000000] text-[16px] tracking-[0] leading-[normal]">
              Date
            </div>
            <div className="w-[151px] absolute top-[21px] left-0 [font-family:'Roboto-Regular',Helvetica] font-normal text-[#919191] text-[18px] tracking-[0] leading-[normal]">
              Enter date
            </div>
          </div>
          <div className="absolute w-[162px] h-[42px] top-[15px] left-[854px]">
            <div className="absolute w-[50px] top-0 left-0 [font-family:'Roboto-Regular',Helvetica] font-normal text-[#000000] text-[16px] tracking-[0] leading-[normal]">
              Who
            </div>
            <div className="absolute w-[158px] top-[21px] left-0 [font-family:'Roboto-Regular',Helvetica] font-normal text-[#919191] text-[18px] tracking-[0] leading-[normal]">
              Number of people
            </div>
          </div>
          <img className="w-px h-[39px] top-[18px] left-[833px] absolute object-cover" alt="Line" src="line-3.svg" />
          <img className="w-px h-[39px] top-[18px] left-[551px] absolute object-cover" alt="Line" src="line-2.svg" />
        </div>
        <div className="absolute w-[1122px] h-[291px] top-[120px] left-[160px]">
          <img
            className="absolute w-[645px] h-[291px] top-0 left-[475px] object-cover"
            alt="Foto s"
            src="foto-s-kantoorruimtes.png"
          />
          <p className="absolute w-[455px] top-[8px] left-0 [font-family:'Roboto-Regular',Helvetica] font-normal text-beige text-[64px] tracking-[0] leading-[normal]">
            <span className="[font-family:'Roboto-Regular',Helvetica] font-normal text-[#f3ddc4] text-[64px] tracking-[0]">
              Meetings for everyone
              <br />
            </span>
            <span className="text-[24px]">
              <br />
              Find Your Ideal Meeting Space: Effortless Booking, Infinite Possibilities.
              <br />
              <br />
            </span>
          </p>
        </div>
      </div>
    </div>
  );
};
