# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [df93f5d](https://github.com/python/cpython/commit/df93f5d)
- commit date: 2024-05-29T18:51:13+01:00
- commit merge base: [fcca08ec2f48f4ba5ba1d4690fb39b1efe630944](https://github.com/python/cpython/commit/fcca08ec2f48f4ba5ba1d4690fb39b1efe630944)
- ref: main

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9290852101)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240529-linux-x86_64-python-main-3.14.0a0-df93f5d.json)

### vs. 3.10.4

- Geometric mean: not sig (HPT: reliability of 84.13%, 1.00x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: 2to3, aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, asyncio_websockets, bench_mp_pool, bench_thread_pool, chameleon, chaos, comprehensions, coroutines, coverage, create_gc_cycles, crypto_pyaes, dask, deepcopy, deepcopy_memo, deepcopy_reduce, deltablue, django_template, djangocms, docutils, dulwich_log, fannkuch, flaskblogging, float, gc_traversal, generators, genshi_text, genshi_xml, go, gunicorn, html5lib, json, json_dumps, json_loads, logging_format, logging_silent, logging_simple, mako, mdp, meteor_contest, mypy2, nbody, nqueens, pathlib, pickle, pickle_dict, pickle_list, pickle_pure_python, pidigits, pprint_pformat, pprint_safe_repr, pycparser, pyflate, pylint, python_startup, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, spectral_norm, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sqlite_synth, sympy_expand, sympy_integrate, sympy_str, sympy_sum, telco, thrift, tomli_loads, tornado_http, typing_runtime_protocols, unpack_sequence, unpickle, unpickle_list, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [📄table](bm-20240529-linux-x86_64-python-main-3.14.0a0-df93f5d-vs-3.10.4.md)
- [📈time plot](bm-20240529-linux-x86_64-python-main-3.14.0a0-df93f5d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: not sig (HPT: reliability of 84.13%, 1.00x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: 2to3, aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, asyncio_websockets, bench_mp_pool, bench_thread_pool, chameleon, chaos, comprehensions, coroutines, coverage, create_gc_cycles, crypto_pyaes, dask, deepcopy, deepcopy_memo, deepcopy_reduce, deltablue, django_template, docutils, dulwich_log, fannkuch, float, gc_traversal, generators, go, gunicorn, json, json_dumps, json_loads, logging_format, logging_silent, logging_simple, mako, mdp, meteor_contest, mypy2, nbody, nqueens, pathlib, pickle, pickle_dict, pickle_list, pickle_pure_python, pidigits, pprint_pformat, pprint_safe_repr, pycparser, pyflate, python_startup, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, spectral_norm, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sqlite_synth, sympy_expand, sympy_integrate, sympy_str, sympy_sum, telco, tomli_loads, tornado_http, typing_runtime_protocols, unpack_sequence, unpickle, unpickle_list, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [📄table](bm-20240529-linux-x86_64-python-main-3.14.0a0-df93f5d-vs-3.12.0.md)
- [📈time plot](bm-20240529-linux-x86_64-python-main-3.14.0a0-df93f5d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: not sig (HPT: reliability of 84.13%, 1.00x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: 2to3, aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, asyncio_websockets, bench_mp_pool, bench_thread_pool, bpe_tokeniser, chameleon, chaos, comprehensions, coroutines, coverage, create_gc_cycles, crypto_pyaes, dask, deepcopy, deepcopy_memo, deepcopy_reduce, deltablue, django_template, djangocms, docutils, dulwich_log, fannkuch, flaskblogging, float, gc_traversal, generators, genshi_text, genshi_xml, go, gunicorn, html5lib, json, json_dumps, json_loads, logging_format, logging_silent, logging_simple, mako, mdp, meteor_contest, mypy2, nbody, nqueens, pathlib, pickle, pickle_dict, pickle_list, pickle_pure_python, pidigits, pprint_pformat, pprint_safe_repr, pycparser, pyflate, pylint, python_startup, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, spectral_norm, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sqlite_synth, sympy_expand, sympy_integrate, sympy_str, sympy_sum, telco, thrift, tomli_loads, tornado_http, typing_runtime_protocols, unpickle, unpickle_list, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [📄table](bm-20240529-linux-x86_64-python-main-3.14.0a0-df93f5d-vs-3.13.0b2.md)
- [📈time plot](bm-20240529-linux-x86_64-python-main-3.14.0a0-df93f5d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: not sig (HPT: reliability of 84.13%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [🧠memory plot](bm-20240529-linux-x86_64-python-main-3.14.0a0-df93f5d-vs-base-mem.svg)
- [📄table](bm-20240529-linux-x86_64-python-main-3.14.0a0-df93f5d-vs-base.md)
- [📈time plot](bm-20240529-linux-x86_64-python-main-3.14.0a0-df93f5d-vs-base.svg)

