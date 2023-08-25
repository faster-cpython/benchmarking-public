# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [0ab8274](https://github.com/brandtbucher/cpython/commit/0ab8274)
- commit date: 2023-07-06T16:01:44-07:00
- commit merge base: [67a798888dcde13bbb1e17cfcc3c742c94e67a07](https://github.com/brandtbucher/cpython/commit/67a798888dcde13bbb1e17cfcc3c742c94e67a07)
- ref: un_materialize

## linux x86_64 (azure)

- [pystats raw](bm-20230706-azure-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-pystats.json)
- [pystats table](bm-20230706-azure-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-pystats.md)

### vs. base

- [pystats diff](bm-20230706-azure-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5489501342)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274.json)

### vs. 3.10.4

- Geometric mean: not sig (HPT: reliability of 84.13%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, chaos, comprehensions, coroutines, coverage, create_gc_cycles, crypto_pyaes, dask, deepcopy, deepcopy_memo, deepcopy_reduce, deltablue, django_template, djangocms, docutils, dulwich_log, fannkuch, flaskblogging, float, gc_traversal, generators, genshi_text, genshi_xml, go, gunicorn, hexiom, html5lib, json, json_dumps, json_loads, logging_format, logging_silent, logging_simple, mako, mdp, meteor_contest, nbody, nqueens, pathlib, pickle, pickle_dict, pickle_list, pickle_pure_python, pidigits, pprint_pformat, pprint_safe_repr, pycparser, pyflate, pylint, python_startup, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, spectral_norm, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sqlite_synth, sympy_expand, sympy_integrate, sympy_str, sympy_sum, telco, thrift, tomli_loads, tornado_http, typing_runtime_protocols, unpack_sequence, unpickle, unpickle_list, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [table](bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-vs-3.10.4.md)
- [plot](bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: not sig (HPT: reliability of 84.13%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, chaos, comprehensions, coroutines, coverage, create_gc_cycles, crypto_pyaes, dask, deepcopy, deepcopy_memo, deepcopy_reduce, deltablue, django_template, djangocms, docutils, dulwich_log, fannkuch, flaskblogging, float, gc_traversal, generators, genshi_text, genshi_xml, go, gunicorn, hexiom, html5lib, json, json_dumps, json_loads, logging_format, logging_silent, logging_simple, mako, mdp, meteor_contest, nbody, nqueens, pathlib, pickle, pickle_dict, pickle_list, pickle_pure_python, pidigits, pprint_pformat, pprint_safe_repr, pycparser, pyflate, pylint, python_startup, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, spectral_norm, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sqlite_synth, sympy_expand, sympy_integrate, sympy_str, sympy_sum, telco, thrift, tomli_loads, tornado_http, typing_runtime_protocols, unpack_sequence, unpickle, unpickle_list, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [table](bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-vs-3.11.0.md)
- [plot](bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-vs-3.11.0.png)

### vs. base

- Geometric mean: not sig (HPT: reliability of 84.13%, 1.00x slower at 99th %ile)
- missing benchmarks: 🔴 async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chaos, comprehensions, coroutines, coverage, create_gc_cycles, crypto_pyaes, dask, deepcopy, deepcopy_memo, deepcopy_reduce, deltablue, docutils, dulwich_log, fannkuch, float, gc_traversal, generators, go, hexiom, json, json_dumps, json_loads, logging_format, logging_silent, logging_simple, mako, mdp, meteor_contest, nbody, nqueens, pathlib, pickle, pickle_dict, pickle_list, pickle_pure_python, pidigits, pprint_pformat, pprint_safe_repr, pycparser, pyflate, python_startup, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, spectral_norm, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sqlite_synth, telco, tomli_loads, tornado_http, typing_runtime_protocols, unpack_sequence, unpickle, unpickle_list, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [table](bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-vs-base.md)
- [plot](bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-vs-base.png)

