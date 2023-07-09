
# Results vs. base

- fork: brandtbucher
- ref: un_materialize
- machine: linux-x86_64
- commit hash: 0ab8274
- commit date: 2023-07-06
- overall geometric mean: not sig

| Benchmark | bm-20230706-linux-x86_64-python-67a798888dcde13bbb1e-3.13.0a0-67a7988 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|-----------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mypy2     | 336 ms                                                                | 455 ms: 1.35x slower                                                  |
Ignored benchmarks (81) of results/bm-20230706-3.13.0a0-67a7988/bm-20230706-linux-x86_64-python-67a798888dcde13bbb1e-3.13.0a0-67a7988.json: async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chaos, comprehensions, coroutines, coverage, create_gc_cycles, crypto_pyaes, dask, deepcopy, deepcopy_memo, deepcopy_reduce, deltablue, docutils, dulwich_log, fannkuch, float, gc_traversal, generators, go, hexiom, json, json_dumps, json_loads, logging_format, logging_silent, logging_simple, mako, mdp, meteor_contest, nbody, nqueens, pathlib, pickle, pickle_dict, pickle_list, pickle_pure_python, pidigits, pprint_pformat, pprint_safe_repr, pycparser, pyflate, python_startup, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, spectral_norm, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sqlite_synth, telco, tomli_loads, tornado_http, typing_runtime_protocols, unpack_sequence, unpickle, unpickle_list, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
