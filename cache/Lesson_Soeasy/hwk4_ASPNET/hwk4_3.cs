using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class _Default : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {

    }

    protected void Button1_Click(object sender, EventArgs e)
    {
        double a = Convert.ToDouble(TextBox1.Text),
            b = Convert.ToDouble(TextBox2.Text),
            c = Convert.ToDouble(TextBox3.Text),
            d = Convert.ToDouble(TextBox4.Text),
            // 以上為 第 1 , 2 線。
            // 以下為 第 3 , 4 線
            l = Convert.ToDouble(TextBox5.Text), //a
            f = Convert.ToDouble(TextBox6.Text), //b
            g = Convert.ToDouble(TextBox7.Text), //c
            h = Convert.ToDouble(TextBox8.Text); //d

        double x1 = b - d, y1 = c - a, ans1 = b * c - a * d,
               x2 = f - h, y2 = g - l, ans2 = f * g - l * h;
        Label1.Text = "第一線與第二線的直線方程式：" + x1 + "x + " + y1 + "y = " + ans1;
        Label2.Text = "第三線與第四線的直線方程式：" + x2 + "x * " + y2 + "y = " + ans2;
        Label3.Text = "直線交點：" + "(" + (ans1 * y2 - y1 * ans2) / (x1 * y2 - y1 * x2) + "," + (x1 * ans2 - ans1 * x2) / (x1 * y2 - y1 * x2) + ")";
    }                                      

}