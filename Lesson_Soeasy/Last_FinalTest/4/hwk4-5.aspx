<%@ Page Language="C#" AutoEventWireup="true" CodeFile="hwk4-5.aspx.cs" Inherits="hwk4_5" %>

<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta charset="utf-8" />
    <title></title>    
    <style type="text/css">
        table, th, td {
         border: 1px solid black;
        }   
    </style>
    </head>
<body>
    <form id="form1" runat="server">   
        歡迎來到雋諺賣冰廠<br />
        <br />
        <asp:Label ID="Label2" runat="server" Text="名字 : "></asp:Label>
        <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
        <br />
        <asp:Label ID="Label3" runat="server" Text="街道 : "></asp:Label>
        <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
        <br />
        <asp:Label ID="Label4" runat="server" Text="都市 : "></asp:Label>
        <asp:TextBox ID="TextBox3" runat="server"></asp:TextBox>
        <br />
        <asp:Label ID="Label5" runat="server" Text="電話 : "></asp:Label>
        <asp:TextBox ID="TextBox4" runat="server"></asp:TextBox>
        <br />
        <br />
        <table class="order">
          <tr>
            <td class="product">Product</td>
            <td class="price">Price</td> 
            <td>Quantity</td>
          </tr>
          <tr>
            <td class="product_1">1號冰</td>
            <td class="price_1">$3.00</td> 
            <td>
                <asp:TextBox ID="TextBox5" runat="server" Width="53px"></asp:TextBox>
              </td>
          </tr>
          <tr>
            <td class="product_2">2號冰</td>
            <td class="price_2">$3.50</td> 
            <td class="auto-style1">
                <asp:TextBox ID="TextBox6" runat="server" Width="53px"></asp:TextBox>
              </td>
          </tr>
            <tr>
            <td class="product_3">3號冰</td>
            <td class="price_3">$4.50</td> 
            <td>
                <asp:TextBox ID="TextBox7" runat="server" Width="53px"></asp:TextBox>
                </td>
          </tr>
            <tr>
            <td class="product_4">4號冰</td>
            <td class="price_4">$5.00</td> 
            <td>
                <asp:TextBox ID="TextBox8" runat="server" Width="53px"></asp:TextBox>
            </tr>
          </tr>
        </table>
        <br />
        <asp:Label ID="Label6" runat="server" Text="付款方式"></asp:Label>
        <br />
        <asp:RadioButtonList ID="RadioButtonList1" runat="server" Height="57px" Width ="255px">
            <asp:ListItem>Visa</asp:ListItem>
            <asp:ListItem>Master Card</asp:ListItem>
            <asp:ListItem>現金</asp:ListItem>
        </asp:RadioButtonList>
        <br />
        <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="送出" style="height: 21px" />
&nbsp;<asp:Button ID="Button2" runat="server" Text="清除" OnClick="reset" />
        <br />
        <br />
        <asp:Label ID="Label7" runat="server"></asp:Label>
        <br />
        <asp:Label ID="Label8" runat="server"></asp:Label>
        <br />
        <asp:Label ID="Label9" runat="server"></asp:Label>
        <br />
        <br />
        <asp:Label ID="Label10" runat="server"></asp:Label>
        <br />
        <asp:Label ID="Label11" runat="server"></asp:Label>
        <br />
        <asp:Label ID="Label12" runat="server"></asp:Label>
        <br />
        <asp:Label ID="Label13" runat="server"></asp:Label>
        <br />
    </form>
</body>
</html>

