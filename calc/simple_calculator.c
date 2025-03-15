#include <gtk/gtk.h>

static void calculate(GtkWidget *widget, gpointer data) {
    GtkEntry *entry1 = GTK_ENTRY(g_object_get_data(G_OBJECT(widget), "entry1"));
    GtkEntry *entry2 = GTK_ENTRY(g_object_get_data(G_OBJECT(widget), "entry2"));
    GtkLabel *result_label = GTK_LABEL(g_object_get_data(G_OBJECT(widget), "result_label"));

    const gchar *num1_text = gtk_entry_get_text(entry1);
    const gchar *num2_text = gtk_entry_get_text(entry2);

    int num1 = atoi(num1_text);
    int num2 = atoi(num2_text);
    int result = num1 + num2;

    gchar result_text[100];
    snprintf(result_text, sizeof(result_text), "%d + %d = %d", num1, num2, result);

    gtk_label_set_text(result_label, result_text);
}

int main(int argc, char *argv[]) {
    GtkBuilder *builder;
    GtkWidget *window;
    GtkWidget *calculate_button;
    GtkEntry *entry1, *entry2;
    GtkLabel *result_label;

    gtk_init(&argc, &argv);

    builder = gtk_builder_new_from_file("simple_calculator.glade");

    window = GTK_WIDGET(gtk_builder_get_object(builder, "window"));
    calculate_button = GTK_WIDGET(gtk_builder_get_object(builder, "calculate_button"));
    entry1 = GTK_ENTRY(gtk_builder_get_object(builder, "entry1"));
    entry2 = GTK_ENTRY(gtk_builder_get_object(builder, "entry2"));
    result_label = GTK_LABEL(gtk_builder_get_object(builder, "result_label"));

    g_object_set_data(G_OBJECT(calculate_button), "entry1", entry1);
    g_object_set_data(G_OBJECT(calculate_button), "entry2", entry2);
    g_object_set_data(G_OBJECT(calculate_button), "result_label", result_label);

    g_signal_connect(calculate_button, "clicked", G_CALLBACK(calculate), NULL);
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    gtk_widget_show_all(window);
    gtk_main();

    return 0;
}