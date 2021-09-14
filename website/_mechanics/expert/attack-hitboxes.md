---
name: Attack Hitboxes
techgroup: expert
---

[![All Dustforce character hitboxes overlapped](https://i.imgur.com/grO8PaH.png "Click here to open album")](https://imgur.com/a/jtzG0)

**Click image to view full album on Imgur**

```
ah_ = attack heavy
al_ = attack light
_f = front
_u = up
_b = back
_ah = aerial front
_au = aerial up
_ad = aerial down
_of = offset relative to bottom center of character

Dustman

      //heavy
      ah_f.left = 0; ah_f.right = 285; ah_f.top = -48; ah_f.bottom = 48; ah_f_of.x = -10; ah_f_of.y = -48;        //DONE
      ah_u.left = -70; ah_u.right = 70; ah_u.top = -230; ah_u.bottom = 0; ah_u_of.x = 60; ah_u_of.y = -50;        //DONE
      ah_d.left = -70; ah_d.right = 70; ah_d.top = 0; ah_d.bottom = 225; ah_d_of.x = 70; ah_d_of.y = -220;        //DONE
      //air
      ah_af.left = 0; ah_af.right = 285; ah_af.top = -48; ah_af.bottom = 48; ah_af_of.x = -10; ah_af_of.y = -48;      //DONE
      ah_au.left = -75; ah_au.right = 75; ah_au.top = -205; ah_au.bottom = 0; ah_au_of.x = 65; ah_au_of.y = -70;      //DONE
      ah_ad.left = -80; ah_ad.right = 80; ah_ad.top = 0; ah_ad.bottom = 270; ah_ad_of.x = 80; ah_ad_of.y = -200;      //DONE

      ////light
      al_f.left = 0; al_f.right = 170; al_f.top = -65; al_f.bottom = 65; al_f_of.x = -10; al_f_of.y = -65;        //DONE
      al_u.left = -55; al_u.right = 55; al_u.top = -170; al_u.bottom = 0;  al_u_of.x = 45; al_u_of.y = -50;        //DONE
      al_d.left = -82; al_d.right = 82; al_d.top = 0; al_d.bottom = 136; al_d_of.x = 74; al_d_of.y = -131;        //DONE
      //air
      al_af.left = 0; al_af.right = 170; al_af.top = -65; al_af.bottom = 65; al_af_of.x = -10; al_af_of.y = -65;          //DONE
      al_au.left = -55; al_au.right = 55; al_au.top = -170; al_au.bottom = 0; al_au_of.x = 45; al_au_of.y = -50;      //DONE
      al_ad.left = -50; al_ad.right = 50; al_ad.top = 0; al_ad.bottom = 110;  al_ad_of.x = 40; al_ad_of.y = -55;      //done

Dustgirl

  dm.ah_f.left = 0; dm.ah_f.right = 285; dm.ah_f.top = -60;
  dm.ah_f.bottom = 60; dm.ah_f_of.x = -10; dm.ah_f_of.y = -60;        //DONE

  dm.ah_u.left = -70; dm.ah_u.right = 70; dm.ah_u.top = -205;
  dm.ah_u.bottom = 0; dm.ah_u_of.x = 70; dm.ah_u_of.y = -80;        //DONE

  dm.ah_d.left = -80; dm.ah_d.right = 80; dm.ah_d.top = 0;dm.ah_d.bottom = 225;dm.ah_d_of.x = 70;dm.ah_d_of.y = -220;        //DONE
  //air
 dm.ah_af.left = 0;dm.ah_af.right = 285;dm.ah_af.top = -60;dm.ah_af.bottom = 60;dm.ah_af_of.x = -10;dm.ah_af_of.y = -60;      //
 dm.ah_au.left = -70;dm.ah_au.right = 70;dm.ah_au.top = -205;dm.ah_au.bottom = 0;dm.ah_au_of.x = 70;dm.ah_au_of.y = -80;      //
 dm.ah_ad.left = -80;dm.ah_ad.right = 80;dm.ah_ad.top = 0;dm.ah_ad.bottom = 270;dm.ah_ad_of.x = 80;dm.ah_ad_of.y = -200;      //DONE
 

  ////light
  dm.al_f.left = 0; dm.al_f.right = 170; dm.al_f.top = -50; dm.al_f.bottom = 50; dm.al_f_of.x = -10; dm.al_f_of.y = -50;        //DONE
  dm.al_u.left = -60; dm.al_u.right = 60; dm.al_u.top = -150; dm.al_u.bottom = 0;  dm.al_u_of.x = 45; dm.al_u_of.y = -60;        //DONE
  dm.al_d.left = -82; dm.al_d.right = 82; dm.al_d.top = 0; dm.al_d.bottom = 136; dm.al_d_of.x = 74; dm.al_d_of.y = -131;        //DONE
  //air
  dm.al_af.left = 0; dm.al_af.right = 170; dm.al_af.top = -50; dm.al_af.bottom = 50; dm.al_af_of.x = -10; dm.al_af_of.y = -50;          //DONE
  dm.al_au.left = -60; dm.al_au.right = 60; dm.al_au.top = -150; dm.al_au.bottom = 0; dm.al_au_of.x = 45; dm.al_au_of.y = -60;      //DONe
  dm.al_ad.left = -55; dm.al_ad.right = 55; dm.al_ad.top = 0; dm.al_ad.bottom = 120;  dm.al_ad_of.x = 32; dm.al_ad_of.y = -65;      //DONE


Dustkid

  dm.ah_f.left = 0;dm.ah_f.right = 195;dm.ah_f.top = -55;dm.ah_f.bottom = 55;dm.ah_f_of.x = -10;dm.ah_f_of.y = -55;        //DONE
 dm.ah_u.left = -60;dm.ah_u.right = 60;dm.ah_u.top = -195;dm.ah_u.bottom = 0;dm.ah_u_of.x = 40;dm.ah_u_of.y = -30;        //DONE
 dm.ah_d.left = -65;dm.ah_d.right = 65;dm.ah_d.top = 0;dm.ah_d.bottom = 185;dm.ah_d_of.x = 57;dm.ah_d_of.y = -180;        //DONE
  //air
 dm.ah_af.left = 0;dm.ah_af.right = 195;dm.ah_af.top = -55;dm.ah_af.bottom = 55;dm.ah_af_of.x = -10;dm.ah_af_of.y = -55;      //
 dm.ah_au.left = -60;dm.ah_au.right = 60;dm.ah_au.top = -195;dm.ah_au.bottom = 0;dm.ah_au_of.x = 40;dm.ah_au_of.y = -30;      //
 dm.ah_ad.left = -65;dm.ah_ad.right = 65;dm.ah_ad.top = 0;dm.ah_ad.bottom = 185;dm.ah_ad_of.x = 57;dm.ah_ad_of.y = -180;      //

  ////light
  dm.al_f.left = 0; dm.al_f.right = 150; dm.al_f.top = -45; dm.al_f.bottom = 45; dm.al_f_of.x = -10; dm.al_f_of.y = -45;        //DONE
  dm.al_u.left = -50; dm.al_u.right = 50; dm.al_u.top = -130; dm.al_u.bottom = 0;  dm.al_u_of.x = 40; dm.al_u_of.y = -60;        //DONE
  dm.al_d.left = -75; dm.al_d.right = 75; dm.al_d.top = 0; dm.al_d.bottom = 126; dm.al_d_of.x = 55; dm.al_d_of.y = -121;        //DONE
  //air
  dm.al_af.left = 0; dm.al_af.right = 150; dm.al_af.top = -45; dm.al_af.bottom = 45; dm.al_af_of.x = -10; dm.al_af_of.y = -45;          //DONE
  dm.al_au.left = -50; dm.al_au.right = 50; dm.al_au.top = -130; dm.al_au.bottom = 0; dm.al_au_of.x = 40; dm.al_au_of.y = -60;      //DONE
  dm.al_ad.left = -75; dm.al_ad.right = 75; dm.al_ad.top = 0; dm.al_ad.bottom = 135;  dm.al_ad_of.x = 55; dm.al_ad_of.y = -121;      //DONE

Dustworth
  //heavy
 dm.ah_f.left = 0;dm.ah_f.right = 295;dm.ah_f.top = -70;dm.ah_f.bottom = 70;dm.ah_f_of.x = -10;dm.ah_f_of.y = -70;        //DONE
 dm.ah_u.left = -80;dm.ah_u.right = 80;dm.ah_u.top = -230;dm.ah_u.bottom = 0;dm.ah_u_of.x = 80;dm.ah_u_of.y = -70;        //DONE
 dm.ah_d.left = -110;dm.ah_d.right = 110;dm.ah_d.top = 0;dm.ah_d.bottom = 165;dm.ah_d_of.x = 100;dm.ah_d_of.y = -130;        //DONE
  //air
 dm.ah_af.left = 0;dm.ah_af.right = 295;dm.ah_af.top = -70;dm.ah_af.bottom = 70;dm.ah_af_of.x = -10;dm.ah_af_of.y = -70;      //DONE
 dm.ah_au.left = -85;dm.ah_au.right = 85;dm.ah_au.top = -230;dm.ah_au.bottom = 0;dm.ah_au_of.x = 75;dm.ah_au_of.y = -70;      //DONE
 dm.ah_ad.left = -80;dm.ah_ad.right = 80;dm.ah_ad.top = 0;dm.ah_ad.bottom = 200;dm.ah_ad_of.x = 60;dm.ah_ad_of.y = -100;      //

  ////light
  dm.al_f.left = 0; dm.al_f.right = 235; dm.al_f.top = -70; dm.al_f.bottom = 70; dm.al_f_of.x = -10; dm.al_f_of.y = -70;        //DONE
  dm.al_u.left = -75; dm.al_u.right = 75; dm.al_u.top = -200; dm.al_u.bottom = 0;  dm.al_u_of.x = 50; dm.al_u_of.y = -70;        //
  dm.al_d.left = -100; dm.al_d.right = 100; dm.al_d.top = 0; dm.al_d.bottom = 120; dm.al_d_of.x = 90; dm.al_d_of.y = -111;        //DONE

  //air
  dm.al_af.left = 0; dm.al_af.right = 235; dm.al_af.top = -70; dm.al_af.bottom = 70; dm.al_af_of.x = -10; dm.al_af_of.y = -70;          //DONE
  dm.al_au.left = -75; dm.al_au.right = 75; dm.al_au.top = -200; dm.al_au.bottom = 0; dm.al_au_of.x = 50; dm.al_au_of.y = -70;      //
dm.al_ad.left = -70; dm.al_ad.right = 70; dm.al_ad.top = 0; dm.al_ad.bottom = 160; dm.al_ad_of.x = 30; dm.al_ad_of.y = -111; //
```

Code source: [gist.github.com](https://gist.github.com/msg555/75c618f0a65f95aa97bf92387d4bbcac) (pinned in #tasforce on Discord server)
