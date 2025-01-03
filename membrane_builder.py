import argparse
if __name__=="__main__":
        parser = argparse.ArgumentParser(formatter_class= argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument("--x_in",type = float, help ="input width of inner membrane")
        parser.add_argument("--y_in",type = float, help ="input length of inner membrane")
        parser.add_argument("--z_in", type = float, help = "input depth of inner membrane")
        parser.add_argument("--x_out",type = float, help ="input width of outer membrane")
        parser.add_argument("--y_out",type = float, help ="input length of outer membrane")
        parser.add_argument("--z_out", type = float, help = "input depth of outer membrane")
        args = parser.parse_args()
        class Volume():
                def __init__(self, x_in, y_in, x_out, y_out,z_in,z_out):
                        self.x_in = args.x_in
                        self.y_in = args.y_in
                        self.z_in = args.z_in
                        self.x_out = args.x_out
                        self.y_out = args.y_out
                        self.z_out = args.z_out
                def calculate_outer_volume():
                        return args.x_out*args.y_out*args.z_out
                def calculate_inner_volume():
                        return args.x_in*args.y_in*args.z_in
out_vol=Volume.calculate_outer_volume()
in_vol=Volume.calculate_inner_volume()
print(f"Outer volume is: {out_vol}")
print(f"Inner volume is: {in_vol}")

