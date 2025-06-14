def fun(arg1,**kwgs):
    for k, val in kwgs.items():
        print("%s==%s"%(k,val))

fun("hi",s1="the",s2="heart",s4="break",s3="kid")
