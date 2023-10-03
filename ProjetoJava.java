import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class IconeFlutuanteApp {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Aplicativo de Ícones Flutuantes");
            frame.setSize(800, 600);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            GradientBackgroundPanel gradientPanel = new GradientBackgroundPanel();
            frame.add(gradientPanel);

            addButton("Home", 100, 100, "Texto do Home", gradientPanel);
            addButton("Test", 300, 300, "Texto do Test", gradientPanel);
            addButton("About", 500, 500, "Texto do About", gradientPanel);

            frame.setVisible(true);
        });
    }

    private static void addButton(String label, int x, int y, String description, JPanel panel) {
        JButton button = new JButton(label);
        button.setBounds(x, y, 80, 30);

        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.out.println("Clicou em " + label);
                System.out.println(description);
            }
        });

        panel.add(button);
    }
}

class GradientBackgroundPanel extends JPanel {
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        drawGradientBackground(g);
    }

    private void drawGradientBackground(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;
        GradientPaint gradient = new GradientPaint(0, 0, new Color(0.2f, 0.4f, 0.8f), 0, 600, new Color(0.4f, 0.7f, 0.9f));
        g2d.setPaint(gradient);
        g2d.fillRect(0, 0, getWidth(), getHeight());
    }
}
