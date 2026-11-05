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

        packages.default = pkgs.python3Packages.buildPythonApplication {
          pname = "jieba-gd-lookup";
	        version = "0.1.1";
	        src = ./.;
	
	        pyproject = true;
	
	        build-system = [
	          pkgs.python3Packages.setuptools
            pkgs.python3Packages.uv-build
	        ];

	        dependencies = [ 
            pkgs.python3Packages.jieba 
          ];
        };         
      };
    };
}
