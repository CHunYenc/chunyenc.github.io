using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class hwk4_5 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        Label7.Text = "訂單確認：";
        Label8.Text = "訂單編號：" + "000001";
        Label9.Text = "顧客資料：";
        Label10.Text = "姓名：" + TextBox1.Text;
        Label11.Text = "地址：" + TextBox3.Text + TextBox2.Text;
        Label12.Text = "付款方式：" + RadioButtonList1.Text;
        Label13.Text = "費用：" + "$" + Convert.ToInt32(TextBox5.Text) * 3 + Convert.ToInt32(TextBox6.Text) * 3.5 + Convert.ToInt32(TextBox7.Text) * 4.5 + Convert.ToInt32(TextBox8.Text) * 5 + "元";


    }
    protected void reset(object sender, EventArgs e)
    {
        TextBox1.Text = "";
        TextBox2.Text = "";
        TextBox3.Text = "";
        TextBox4.Text = "";
        TextBox5.Text = "";
        TextBox6.Text = "";
        TextBox7.Text = "";
        TextBox8.Text = "";
    }
}