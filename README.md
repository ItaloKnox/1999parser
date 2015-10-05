# 1999parser
Tool to compile data about 1999.co.jp products. Built for gundam plastic models.

# Image format:
For all images: http://www.1999.co.jp/eng/image/[product_code][A-Z]/[10-90]/[1-10]

For [box covers](http://www.1999.co.jp/eng/image/10334864p/10/1): /[product_code]p/10/1 

For [completed model photos](http://www.1999.co.jp/eng/image/10334864a/20/1): /[product_code]a/20/1 (>> /[product_code]a[2-99]/20/[2-99])

# Code
```
form
    div .whole
        div .right
            table #masterBody_tblItemHeader -> MOBILE SUIT NAME
            table #masterBody_tblItemImg
                table #masterBody_tblItemInfo
                    tr #masterBody_trMaker -> MANUFACTURE
                    tr #masterBody_trScale -> SCALE
                    tr #masterBody_trSeries -> SERIES
                    tr #masterBody_trSerieshin -> TV SHOW
                    tr #masterBody_trSalseDate -> RELEASE DATE
                    tr #masterBody_trSalseDate -> PRICE
            div #masterBody_pnlImgCa
                td #gazotitle_box -> TYPE OF PHOTO
```
