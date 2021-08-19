using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 傻吊
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            this.StartPosition = FormStartPosition.CenterScreen;
            InitializeComponent();
        }

        private void button1_MouseEnter(object sender, EventArgs e)
        {
            button1.Text = "是";
            button2.Text = "不是";
        }

        private void button2_MouseEnter(object sender, EventArgs e)
        {
            button2.Text = "是";
            button1.Text = "不是";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("你不用这么认真啦。。。");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            MessageBox.Show("行行行我知道啦！");
        }

        private void button4_MouseEnter(object sender, EventArgs e)
        {
            button4.Text = "我才是傻逼呢";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            MessageBox.Show("好有道理哦。。。");
        }

        private void button4_MouseLeave(object sender, EventArgs e)
        {
            button4.Text = "你才是傻逼呢";
        }

        private void button5_MouseEnter(object sender, EventArgs e)
        {
            Random random = new Random();
            int x = random.Next(0, base.Size.Width - this.button5.Size.Width);
            int y = random.Next(0, base.ClientSize.Height - this.button5.Size.Height);
            Point location = new Point(x, y);
            this.button5.Location = location;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            MessageBox.Show("看来你真的是个傻逼。。。");
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            DialogResult dialogResult = MessageBox.Show("你真的觉得自己是个傻逼吗。。？", "人生的抉择", MessageBoxButtons.YesNo);
            if (dialogResult == DialogResult.No)
            {
                e.Cancel = true;
            }
            else
            {
                MessageBox.Show("你终于说实话啦=w=");
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            MessageBox.Show("你点你妈呢");
        }
    }
}
