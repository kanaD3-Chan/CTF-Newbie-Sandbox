public class FlagChecker {
    public static boolean check(String input) {
        if (input.length() != 30) return false;

        int[] enc = {
            0x44, 0x4e, 0x43, 0x45, 0x59, 0x48, 0x16, 0x54,
            0x16, 0x7d, 0x40, 0x5b, 0x56, 0x11, 0x41, 0x12,
            0x46, 0x11, 0x7d, 0x46, 0x11, 0x41, 0x12, 0x4f,
            0x52, 0x13, 0x4e, 0x11, 0x50, 0x5f,
        };

        for (int i = 0; i < 30; i++) {
            if ((input.charAt(i) ^ 0x22) != enc[i])
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java FlagChecker <flag>");
            return;
        }
        if (check(args[0]))
            System.out.println("Correct!");
        else
            System.out.println("Wrong!");
    }
}
