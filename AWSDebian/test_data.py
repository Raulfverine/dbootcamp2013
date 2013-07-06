test_data1 = """Delivered-To: rauf.ridzuan@gmail.com
Received: by 10.49.101.17 with SMTP id fc17csp172504qeb;
        Fri, 5 Jul 2013 20:06:52 -0700 (PDT)
X-Received: by 10.68.213.231 with SMTP id nv7mr12270168pbc.70.1373080012241;
        Fri, 05 Jul 2013 20:06:52 -0700 (PDT)
Return-Path: <subscriptions_255_1194344@weblite.my>
Received: from mta008.weblite.my (mta008.weblite.my. [183.78.170.216])
        by mx.google.com with ESMTP id p7si6635205pac.252.2013.07.05.20.06.51
        for <rauf.ridzuan@gmail.com>;
        Fri, 05 Jul 2013 20:06:52 -0700 (PDT)
Received-SPF: pass (google.com: domain of subscriptions_255_1194344@weblite.my designates 183.78.170.216 as permitted sender) client-ip=183.78.170.216;
Authentication-Results: mx.google.com;
       spf=pass (google.com: domain of subscriptions_255_1194344@weblite.my designates 183.78.170.216 as permitted sender) smtp.mail=subscriptions_255_1194344@weblite.my;
       dkim=policy (weak key) header.i=subscriptions_255_1194344@weblite.my
DKIM-Signature: v=1; a=rsa-sha1; c=relaxed/relaxed; s=dkim; d=weblite.my;
 h=MIME-Version:From:Sender:To:Reply-To:Date:Subject:Content-Type:Content-Transfer-Encoding:Message-ID; i=subscriptions_255_1194344@weblite.my;
 bh=mh1IOptEFNq6QGixFX11CitlSSM=;
 b=GGXRO0yydo4CI/v1SEkvPmThKYL2YRN+zP7rkcVjunxXzm/Hb8cg9/ArICkDcT2jJBiM0VE7seOM
   P0yFvWyeKg==
DomainKey-Signature: a=rsa-sha1; c=nofws; q=dns; s=dkim; d=weblite.my;
 b=ZbFKVySHc+vFBTZvlhsQcyp0K9HpIJeH/ixeZDJnH8PM69YzKvaTj+YEjOOTAJIuUQqKG2kQ5cy9
   7F9T1ci2Eg==;
Received: from Websvr-DC-001 (183.78.170.188) by mta008.weblite.my id hqu4sa1gno8h for <rauf.ridzuan@gmail.com>; Sat, 6 Jul 2013 11:04:51 +0800 (envelope-from <subscriptions_255_1194344@weblite.my>)
Precedence: bulk
X-Mailer: WebLITE
X-Mailer-Version: V4.5
X-Report-Abuse-At: abuse@weblite.com.my
X-Report-Abuse-Info: It is important to include full email headers in the report
X-Complaints-To: abuse@weblite.com.my
X-Unsubscribe: http://www.borders.com.my/campaignmgmt/campaign_unsubscribe.aspx?ID=5/vt0t2tAx2EmCIukJ8jMA==&Type=all&Mem=2lzCuxBfxKcp4pC2M2JMzA==
MIME-Version: 1.0
From: BORDERS <marketing@borders.com.my>
Sender: subscriptions_255_1194344@weblite.my
To: rauf.ridzuan@gmail.com
Reply-To: BORDERS <marketing@borders.com.my>
Date: 6 Jul 2013 11:05:03 +0800
Subject: Redeem your BCard points at Borders!
Content-Type: text/html; charset=us-ascii
Content-Transfer-Encoding: quoted-printable
Message-ID: <0.0.9.6BC.1CE79F59555B942.0@mta008.weblite.my>"""

test_data2 = """Delivered-To: xgn.firahz@gmail.com
Received: by 10.49.71.36 with SMTP id r4csp124829qeu;
        Tue, 4 Jun 2013 16:10:17 -0700 (PDT)
X-Received: by 10.60.125.5 with SMTP id mm5mr13106560oeb.81.1370387417284;
        Tue, 04 Jun 2013 16:10:17 -0700 (PDT)
Return-Path: <zharif+caf_=xgn.firahz=gmail.com@siswa.um.edu.my>
Received: from mail-oa0-x22f.google.com (mail-oa0-x22f.google.com [2607:f8b0:4003:c02::22f])
        by mx.google.com with ESMTPS id a3si29087451obt.43.2013.06.04.16.10.17
        for <xgn.firahz@gmail.com>
        (version=TLSv1 cipher=ECDHE-RSA-RC4-SHA bits=128/128);
        Tue, 04 Jun 2013 16:10:17 -0700 (PDT)
Received-SPF: neutral (google.com: 2607:f8b0:4003:c02::22f is neither permitted nor denied by best guess record for domain of zharif+caf_=xgn.firahz=gmail.com@siswa.um.edu.my) client-ip=2607:f8b0:4003:c02::22f;
Authentication-Results: mx.google.com;
       spf=neutral (google.com: 2607:f8b0:4003:c02::22f is neither permitted nor denied by best guess record for domain of zharif+caf_=xgn.firahz=gmail.com@siswa.um.edu.my) smtp.mail=zharif+caf_=xgn.firahz=gmail.com@siswa.um.edu.my
Received: by mail-oa0-x22f.google.com with SMTP id m1so616761oag.20
        for <xgn.firahz@gmail.com>; Tue, 04 Jun 2013 16:10:17 -0700 (PDT)
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=google.com; s=20120113;
        h=x-forwarded-to:x-forwarded-for:delivered-to:x-beenthere
         :mime-version:date:message-id:subject:from:to:cc:x-original-sender
         :x-original-authentication-results:reply-to:precedence:mailing-list
         :list-id:x-google-group-id:list-post:list-help:list-archive
         :list-unsubscribe:content-type:x-gm-message-state;
        bh=IZth1mkL81TExT1bg1dy6p2dGrbEmmWPw38SI5bvqzk=;
        b=nWo7bfAjK6sMA7Fyam7vVJ5XWVzME83MAm5H0o0cTWuhPTR8CDoWxyaOrO/fSldJi4
         fqpY7BZKkzOlbNsWIBkUg+QSKJKmUIC/Tyoh8aTNa8JENyPSDaKwXJkMEiMC7bsavBFk
         6J+UJb33QKaXIk6pmAv/uxHEAWGSR5N1r+xJzq2PmsVgmnOXfixoXftrNbqnL+sa/nmL
         hHDD7iHyVhsG+9KS9Xszg+6WKB0GRsptCWfG9b03VDh7ND5TZMSlP3FmwoPocHh+HZAX
         4Pzsg2Ww4WvIeuEneC6ILjxCGZJL/5970sTpppW5bU4LT+XPUWn0QycDJnqPddIx2f/9
         MoCA==
X-Received: by 10.182.153.5 with SMTP id vc5mr13297597obb.32.1370387416821;
        Tue, 04 Jun 2013 16:10:16 -0700 (PDT)
X-Forwarded-To: xgn.firahz@hotmail.com, xgn.firahz@gmail.com
X-Forwarded-For: zharif@siswa.um.edu.my xgn.firahz@hotmail.com, xgn.firahz@gmail.com
Delivered-To: zharif@siswa.um.edu.my
Received: by 10.182.142.193 with SMTP id ry1csp58815obb;
        Tue, 4 Jun 2013 16:10:15 -0700 (PDT)
X-Received: by 10.14.180.4 with SMTP id i4mr8517549eem.63.1370387415154;
        Tue, 04 Jun 2013 16:10:15 -0700 (PDT)
Return-Path: <student_info-list+bncBDL4RR6QWIDBBTHHXGGQKGQEYEVMDYI@siswa.um.edu.my>
Received: from mail-ea0-x245.google.com (mail-ea0-x245.google.com [2a00:1450:4013:c01::245])
        by mx.google.com with ESMTPS id q6si48399989eew.204.2013.06.04.16.10.14
        for <zharif@siswa.um.edu.my>
        (version=TLSv1 cipher=ECDHE-RSA-RC4-SHA bits=128/128);
        Tue, 04 Jun 2013 16:10:15 -0700 (PDT)
Received-SPF: pass (google.com: domain of student_info-list+bncBDL4RR6QWIDBBTHHXGGQKGQEYEVMDYI@siswa.um.edu.my designates 2a00:1450:4013:c01::245 as permitted sender)
Received: by mail-ea0-x245.google.com with SMTP id z7sf783552eaf.0
        for <zharif@siswa.um.edu.my>; Tue, 04 Jun 2013 16:10:14 -0700 (PDT)
X-Received: by 10.180.21.173 with SMTP id w13mr923896wie.4.1370387413569;
        Tue, 04 Jun 2013 16:10:13 -0700 (PDT)
X-BeenThere: student_info-list@siswa.um.edu.my
Received: by 10.180.105.228 with SMTP id gp4ls1453498wib.51.canary; Tue, 04
 Jun 2013 16:09:14 -0700 (PDT)
X-Received: by 10.180.210.161 with SMTP id mv1mr1566504wic.1.1370387354943;
        Tue, 04 Jun 2013 16:09:14 -0700 (PDT)
Received: by 10.194.6.194 with SMTP id d2mswja;
        Mon, 3 Jun 2013 23:16:43 -0700 (PDT)
X-Received: by 10.60.92.230 with SMTP id cp6mr11500215oeb.91.1370326552161;
        Mon, 03 Jun 2013 23:15:52 -0700 (PDT)
Received: from mail-ie0-x234.google.com (mail-ie0-x234.google.com [2607:f8b0:4001:c03::234])
        by mx.google.com with ESMTPS id wq7si28297603obb.181.2013.06.03.23.15.51
        for <student_info-list@siswa.um.edu.my>
        (version=TLSv1 cipher=ECDHE-RSA-RC4-SHA bits=128/128);
        Mon, 03 Jun 2013 23:15:52 -0700 (PDT)
Received-SPF: pass (google.com: domain of suren@um.edu.my designates 2607:f8b0:4001:c03::234 as permitted sender) client-ip=2607:f8b0:4001:c03::234;
Received: by mail-ie0-f180.google.com with SMTP id b11so12871681iee.39
        for <student_info-list@siswa.um.edu.my>; Mon, 03 Jun 2013 23:15:51 -0700 (PDT)
MIME-Version: 1.0
X-Received: by 10.43.115.2 with SMTP id fc2mr12194700icc.27.1370326551608;
 Mon, 03 Jun 2013 23:15:51 -0700 (PDT)
Received: by 10.64.65.226 with HTTP; Mon, 3 Jun 2013 23:15:51 -0700 (PDT)
Date: Tue, 4 Jun 2013 14:15:51 +0800
Message-ID: <CAGzUdaOk457xHj8CBpb8EOm4tERYtPudxOMK1ciyaGO8=0tr7w@mail.gmail.com>
Subject: [student_info] Bloomberg Aptitude Test (BAT) in Kuala Lumpur
From: SURENTHIRAN PILLAI VENAYAGAM PILLAI Staff <suren@um.edu.my>
To: student_info-list@siswa.um.edu.my, student_ips-list@siswa.um.edu.my
Cc: HALIMATON BINTI ATTAN <halimatt@um.edu.my>
X-Original-Sender: suren@um.edu.my
X-Original-Authentication-Results: mx.google.com;       spf=pass (google.com:
 domain of suren@um.edu.my designates 2607:f8b0:4001:c03::234 as permitted
 sender) smtp.mail=suren@um.edu.my
Reply-To: suren@um.edu.my
Precedence: list
Mailing-list: list student_info-list@siswa.um.edu.my; contact student_info-list+owners@siswa.um.edu.my
List-ID: <student_info-list.siswa.um.edu.my>
X-Google-Group-Id: 162770263519
List-Post: <http://groups.google.com/a/siswa.um.edu.my/group/student_info-list/post?hl=en_US>,
 <mailto:student_info-list@siswa.um.edu.my>
List-Help: <http://support.google.com/a/siswa.um.edu.my/bin/topic.py?hl=en_US&topic=25838>,
 <mailto:student_info-list+help@siswa.um.edu.my>
List-Archive: <http://groups.google.com/a/siswa.um.edu.my/group/student_info-list/?hl=en_US>
List-Unsubscribe: <http://groups.google.com/a/siswa.um.edu.my/group/student_info-list/subscribe?hl=en_US>,
 <mailto:googlegroups-manage+162770263519+unsubscribe@googlegroups.com>
Content-Type: multipart/related; boundary=bcaec51718fb55ca8d04de4e0378
X-Gm-Message-State: ALoCoQmQxFkA0oH5FDHW9RHgKFMaKEMo6qmAiqiO+Itulg4LcuwJGXBRsCcyMKPqCUYaWUYeT3dU

--bcaec51718fb55ca8d04de4e0378
Content-Type: multipart/alternative; boundary=bcaec51718fb55ca8a04de4e0377

--bcaec51718fb55ca8a04de4e0377
Content-Type: text/plain; charset=windows-1252
Content-Transfer-Encoding: quoted-printable"""

test_data3 = """Delivered-To: rauf.ridzuan@gmail.com
Received: by 10.49.101.17 with SMTP id fc17csp172504qeb;
        Fri, 5 Jul 2013 20:06:52 -0700 (PDT)
X-Received: by 10.68.213.231 with SMTP id nv7mr12270168pbc.70.1373080012241;
        Fri, 05 Jul 2013 20:06:52 -0700 (PDT)
Return-Path: <subscriptions_255_1194344@weblite.my>
Received: from mta008.weblite.my (mta008.weblite.my. [183.78.170.216])
        by mx.google.com with ESMTP id p7si6635205pac.252.2013.07.05.20.06.51
        for <rauf.ridzuan@gmail.com>;
        Fri, 05 Jul 2013 20:06:52 -0700 (PDT)
Received-SPF: pass (google.com: domain of subscriptions_255_1194344@weblite.my designates 183.78.170.216 as permitted sender) client-ip=183.78.170.216;
Authentication-Results: mx.google.com;
       spf=pass (google.com: domain of subscriptions_255_1194344@weblite.my designates 183.78.170.216 as permitted sender) smtp.mail=subscriptions_255_1194344@weblite.my;
       dkim=policy (weak key) header.i=subscriptions_255_1194344@weblite.my
DKIM-Signature: v=1; a=rsa-sha1; c=relaxed/relaxed; s=dkim; d=weblite.my;
 h=MIME-Version:From:Sender:To:Reply-To:Date:Subject:Content-Type:Content-Transfer-Encoding:Message-ID; i=subscriptions_255_1194344@weblite.my;
 bh=mh1IOptEFNq6QGixFX11CitlSSM=;
 b=GGXRO0yydo4CI/v1SEkvPmThKYL2YRN+zP7rkcVjunxXzm/Hb8cg9/ArICkDcT2jJBiM0VE7seOM
   P0yFvWyeKg==
DomainKey-Signature: a=rsa-sha1; c=nofws; q=dns; s=dkim; d=weblite.my;
 b=ZbFKVySHc+vFBTZvlhsQcyp0K9HpIJeH/ixeZDJnH8PM69YzKvaTj+YEjOOTAJIuUQqKG2kQ5cy9
   7F9T1ci2Eg==;
Received: from Websvr-DC-001 (183.78.170.188) by mta008.weblite.my id hqu4sa1gno8h for <rauf.ridzuan@gmail.com>; Sat, 6 Jul 2013 11:04:51 +0800 (envelope-from <subscriptions_255_1194344@weblite.my>)
Precedence: bulk
X-Mailer: WebLITE
X-Mailer-Version: V4.5
X-Report-Abuse-At: abuse@weblite.com.my
X-Report-Abuse-Info: It is important to include full email headers in the report
X-Complaints-To: abuse@weblite.com.my
X-Unsubscribe: http://www.borders.com.my/campaignmgmt/campaign_unsubscribe.aspx?ID=5/vt0t2tAx2EmCIukJ8jMA==&Type=all&Mem=2lzCuxBfxKcp4pC2M2JMzA==
MIME-Version: 1.0
From: BORDERS <marketing@borders.com.my>
Sender: subscriptions_255_1194344@weblite.my
To: rauf.ridzuan@gmail.com
Reply-To: BORDERS <marketing@borders.com.my>
Date: 6 Jul 2013 11:05:03 +0800
Subject: Redeem your BCard points at Borders!
Content-Type: text/html; charset=us-ascii
Content-Transfer-Encoding: quoted-printable
Message-ID: <0.0.9.6BC.1CE79F59555B942.0@mta008.weblite.my>

<TABLE WIDTH=3D"645" ALIGN=3D"center" BORDER=3D"0" cellspacing=3D"0" CELLPADDING=3D"0"><tr><td=
 width=3D"645"><table border=3D"0" width=3D"100%" cellspacing=3D"5" CELLPADDING=3D"0"><tr><td><FONT=
 face=3Dverdana size=3D1> If you cannot view this email properly, please=
 <A href=3Dhttp://www.borders.com.my/campaignmgmt/campaign_previewInBrowser.aspx?IDStr=3DgP4Ku9PyEfFTtSm+samrzA=3D=3D&MStr=3D2lzCuxBfxKcp4pC2M2JMzA=3D=3D&TIDStr=3D5/vt0t2tAx2EmCIukJ8jMA=3D=3D&CStr=3DFbYl2M3jFjVXmu4cA1/hug=3D=3D&UStr=3DFalse=
 target=3D_blank> click here. </A></FONT></td><td><p align=3Dright><FONT=
 face=3Dverdana size=3D1><img src=3Dhttp://www.borders.com.my/WebLite/Applications/campaignmgmt/images/email.gif>&nbsp;<a=
 href=3Dhttp://www.borders.com.my/campaignmgmt/campaign_forward.aspx?IDStr=3DgP4Ku9PyEfFTtSm+samrzA=3D=3D&TIDStr=3D5/vt0t2tAx2EmCIukJ8jMA=3D=3D&MStr=3D2lzCuxBfxKcp4pC2M2JMzA=3D=3D&CStr=3DFbYl2M3jFjVXmu4cA1/hug=3D=3D>Forward=
 to a friend!</a></FONT></p></td></tr></table></td> </tr><tr><td width=3D"645"=
 bgcolor=3D""><table bgcolor=3D"" cellspacing=3D"5" CELLPADDING=3D"0" border=3D"0"=
 width=3D"645"><tr><td colspan=3D"2" width=3D"645"><img src=3D"http://www.borders.com.my/WebLITE/Applications/campaignmgmt/uploaded/pics/promotion/BCard%20Redemption.jpg"=
 style=3D"width: 640px; height: 893px; " alt=3D"Borders" border=3D"0"></td></tr><tr><td=
 colspan=3D"2" width=3D"645">&nbsp;</td></tr></table></td></tr><tr><td width=3D"645"><table=
 cellspacing=3D"5" CELLPADDING=3D"0" border=3D"0" width=3D"645"><tr><td=
 colspan=3D"2" width=3D"645"><p><FONT face=3Dverdana size=3D1>This email=
 was sent to: </FONT><FONT face=3Dverdana size=3D1 style=3D"font-weight:=
 bold;">rauf.ridzuan@gmail.com</FONT></p></td></tr><tr><td colspan=3D"2"=
 width=3D"645"><p><FONT face=3Dverdana size=3D1>To ensure undisrupted delivery=
 of our E-Newsletters, please add </FONT><FONT face=3Dverdana size=3D1 style=3D"font-weight:=
 bold;">marketing@borders.com.my</FONT><FONT face=3Dverdana size=3D1> to=
 your list of safe senders.</FONT></p></td></tr><tr><td width=3D"566"><p><FONT=
 face=3Dverdana size=3D1>We support responsible and ethical email marketing=
 practices. Removal from this email distribution list is automatically enforced=
 by our email delivery system. <a  href=3Dhttp://www.borders.com.my/campaignmgmt/campaign_PrivacyPolicy.aspx?CStr=3DFbYl2M3jFjVXmu4cA1/hug=3D=3D=
  target=3D_blank title=3DPrivacy><font face=3Dverdana size=3D1>Privacy=
 Policy</font></a><br>* To unsubscribe from this newsletter please <A href=3Dhttp://www.borders.com.my/campaignmgmt/campaign_unsubscribe.aspx?ID=3D5/vt0t2tAx2EmCIukJ8jMA=3D=3D&Type=3Dcamp&Mem=3D2lzCuxBfxKcp4pC2M2JMzA=3D=3D=
 target=3D_blank> click here </A><br>* To unsubscribe from all future newsletters=
 please <A href=3Dhttp://www.borders.com.my/campaignmgmt/campaign_unsubscribe.aspx?ID=3D5/vt0t2tAx2EmCIukJ8jMA=3D=3D&Type=3Dall&Mem=3D2lzCuxBfxKcp4pC2M2JMzA=3D=3D=
 target=3D_blank> click here </A></FONT></p></td><td align=3Dright><A HREF=3Dhttp://www.borders.com.my/campaignmgmt/campaign_ClickThru.aspx?CampID=3D5/vt0t2tAx2EmCIukJ8jMA=3D=3D&URL=3Dhttp://campaign.weblite.com.my&Type=3DTest><img=
 id=3DimgLogo VSPACE=3D"0"  height=3D"29" valign=3Dtop align=3Dright width=3D"79"=
 HSPACE=3D"0" BORDER=3D"0" ALT=3D"" src=3Dhttp://www.borders.com.my/WebLite/Applications/campaignmgmt/images/1194344.aspx></a></td></tr><tr><td=
 colspan=3D"2" width=3D"645"></td></tr><tr align=3D"right"><td colspan=3D"2"=
 width=3D"645"><p><FONT face=3Dverdana size=3D1 style=3D"font-weight: bold;">Berjaya=
 Books Sdn Bhd</FONT><br><FONT face=3Dverdana size=3D1>No. 3 Jalan PJU 3/48,&nbsp;Sunway=
 Damansara Technology Park, Sunway Damansara&nbsp;47810&nbsp;Petaling Jaya,&nbsp;Selangor,&nbsp;Malaysia<br>Tel:=
 +60 3 7803 9000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fax: +60 3 7803 9200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;URL:=
 <A href=3Dhttp://www.borders.com.my target=3D_blank>www.borders.com.my=
 </A></FONT></p></td></tr></table></td></tr></TABLE>"""