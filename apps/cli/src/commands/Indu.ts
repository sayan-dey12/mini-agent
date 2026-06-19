import chalk from "chalk";
import boxen from "boxen";
import figlet from "figlet";
import gradient from "gradient-string";

export class InduCommand {
  execute(): void {
    console.clear();

    // Big Banner
    console.log(
      gradient.atlas.multiline(
        figlet.textSync("Hello Pomi!!", {
          font: "ANSI Shadow",
          horizontalLayout: "default",
        })
      )
    );

    console.log();

    // Main Message
    console.log(
      boxen(
        `${chalk.bold.yellowBright("💙 Taratari thik hoye jao 💙")}

${chalk.white(
  "On the behalf of my boss, I am praying for your better health 🙏🙏"
)}

${chalk.white("Take care and get well soon! 🌸")}`,
        {
          padding: 1,
          margin: 1,
          borderStyle: "round",
          borderColor: "blue",
          title: " GET WELL SOON ",
          titleAlignment: "center",
        }
      )
    );

    console.log();

    console.log(
      chalk.blueBright.bold(
        "══════════════════════════════════════════════════════════════"
      )
    );

    console.log(
      chalk.cyanBright(
        "               Wishing you a speedy recovery ❤️"
      )
    );

    console.log(
      chalk.blueBright.bold(
        "══════════════════════════════════════════════════════════════"
      )
    );

    console.log();
  }
}