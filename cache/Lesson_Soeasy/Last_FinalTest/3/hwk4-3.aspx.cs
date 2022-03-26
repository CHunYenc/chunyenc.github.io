using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class _Default : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        double
            a = Convert.ToDouble(TextBox1.Text),
            b = Convert.ToDouble(TextBox2.Text),
            // 以上為 第 1 , 2 線。
            // 以下為 第 3 , 4 線
            c = Convert.ToDouble(TextBox3.Text), 
            d = Convert.ToDouble(TextBox4.Text);

        double 
            x = (d - b) , y = (c - a)  , z = (a*d) - (b*c) , abs = Math.Abs((x*0) + (y*0) -z),sqrt = (x*x)+(y*y);
        Label1.Text = "第一線與第二線的直線方程式：" + x + "x +" + y + "y = " + z;
        Label2.Text = "三角形面積：" + (z*z)/(2*x*y) ;
        Label3.Text = "直線到遠點的距離："+ abs/Math.Sqrt(sqrt);
    }                                      
}