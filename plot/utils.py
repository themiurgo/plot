def common_settings(args, plt):
    # Common options
    if args['--title']:
        plt.title(args['--title'])
    plt.ylabel(args['--ylabel'])
    plt.xlabel(args['--xlabel'])
    if args['--xlog']:
        plt.xscale('log')
    if args['--ylog']:
        plt.yscale('log')
