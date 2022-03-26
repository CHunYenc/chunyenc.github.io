<%@ Page Language="C#" AutoEventWireup="true" CodeFile="hwk4_3.cs" Inherits="_Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div class="Input">
            <p>
                輸入 4 個點：</p>
            <p>
                1. (
                <asp:TextBox ID="TextBox1" runat="server" Width="70px"></asp:TextBox>
                ,<asp:TextBox ID="TextBox2" runat="server" Width="70px"></asp:TextBox>
                ),</p>
            <p>
                2.&nbsp; (<asp:TextBox ID="TextBox3" runat="server" Width="70px"></asp:TextBox>
                ,<asp:TextBox ID="TextBox4" runat="server" Width="70px"></asp:TextBox>
                ),</p>
            <p>
                3.&nbsp; (<asp:TextBox ID="TextBox5" runat="server" Width="70px"></asp:TextBox>
                ,<asp:TextBox ID="TextBox6" runat="server" Width="70px"></asp:TextBox>
                ),</p>
            <p>
                4.&nbsp; (<asp:TextBox ID="TextBox7" runat="server" Width="70px"></asp:TextBox>
                ,<asp:TextBox ID="TextBox8" runat="server" Width="70px"></asp:TextBox>
                )</p>
            <p>
                <asp:Button ID="Button1" runat="server" Text="送出" OnClick="Button1_Click" />
            </p>
        </div>
        <asp:Label ID="Label1" runat="server"></asp:Label>
        <br />
        <asp:Label ID="Label2" runat="server"></asp:Label>
        <br />
        <asp:Label ID="Label3" runat="server"></asp:Label>
    </form>
</body>
</html>
