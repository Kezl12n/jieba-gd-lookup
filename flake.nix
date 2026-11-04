{
  description = "Building a devenv (jieba-gd-lookup) script into a pure flake package";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    devenv.url = "github:cachix/devenv";
  };

  outputs = inputs@{ flake-parts, nixpkgs, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      imports = [ inputs.devenv.flakeModule ]; # Loads devenv internals into the flake

      systems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];

      perSystem = { config, pkgs, ... }: {
        devenv.shells.default = {
          imports = [ ./devenv.nix ];
        };

        # Extract the exact script from the compiled devenv shell into a pure package output
        packages.default = config.devenv.shells.default.config.scripts.jieba-gd-lookup.package;
      };
    };
}
