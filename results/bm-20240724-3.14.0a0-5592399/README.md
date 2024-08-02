# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [5592399](https://github.com/python/cpython/commit/5592399)
- commit date: 2024-07-24T10:58:28-07:00
- commit merge base: [9ac606080a0074cdf7589d9b7c9413a73e0ddf37](https://github.com/python/cpython/commit/9ac606080a0074cdf7589d9b7c9413a73e0ddf37)
- ref: 5592399313c963c11028

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10095495155)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240724-linux-x86_64-python-5592399313c963c11028-3.14.0a0-5592399.json)

### vs. 3.10.4

- Geometric mean: not sig (HPT: reliability of 84.13%, 1.00x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: 2to3, aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, asyncio_websockets, bench_mp_pool, bench_thread_pool, chameleon, chaos, comprehensions, coroutines, coverage, create_gc_cycles, crypto_pyaes, dask, deepcopy, deepcopy_memo, deepcopy_reduce, deltablue, django_template, djangocms, docutils, dulwich_log, fannkuch, flaskblogging, float, gc_traversal, generators, genshi_text, genshi_xml, go, gunicorn, hexiom, html5lib, json, json_dumps, json_loads, logging_format, logging_silent, logging_simple, mako, mdp, meteor_contest, mypy2, nbody, nqueens, pathlib, pickle, pickle_dict, pickle_list, pickle_pure_python, pidigits, pprint_pformat, pprint_safe_repr, pycparser, pyflate, pylint, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, spectral_norm, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sqlite_synth, sympy_expand, sympy_integrate, sympy_str, sympy_sum, telco, thrift, tomli_loads, tornado_http, typing_runtime_protocols, unpack_sequence, unpickle, unpickle_list, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [📄table](bm-20240724-linux-x86_64-python-5592399313c963c11028-3.14.0a0-5592399-vs-3.10.4.md)
- [📈time plot](bm-20240724-linux-x86_64-python-5592399313c963c11028-3.14.0a0-5592399-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: not sig (HPT: reliability of 84.13%, 1.00x slower at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: 2to3, aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, asyncio_websockets, bench_mp_pool, bench_thread_pool, chameleon, chaos, comprehensions, coroutines, coverage, create_gc_cycles, crypto_pyaes, dask, deepcopy, deepcopy_memo, deepcopy_reduce, deltablue, django_template, docutils, dulwich_log, fannkuch, float, gc_traversal, generators, go, gunicorn, hexiom, json, json_dumps, json_loads, logging_format, logging_silent, logging_simple, mako, mdp, meteor_contest, mypy2, nbody, nqueens, pathlib, pickle, pickle_dict, pickle_list, pickle_pure_python, pidigits, pprint_pformat, pprint_safe_repr, pycparser, pyflate, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, spectral_norm, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sqlite_synth, sympy_expand, sympy_integrate, sympy_str, sympy_sum, telco, tomli_loads, tornado_http, typing_runtime_protocols, unpack_sequence, unpickle, unpickle_list, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [📄table](bm-20240724-linux-x86_64-python-5592399313c963c11028-3.14.0a0-5592399-vs-3.12.0.md)
- [📈time plot](bm-20240724-linux-x86_64-python-5592399313c963c11028-3.14.0a0-5592399-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: not sig (HPT: reliability of 84.13%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 2to3, aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, asyncio_websockets, bench_mp_pool, bench_thread_pool, bpe_tokeniser, chameleon, chaos, comprehensions, coroutines, coverage, create_gc_cycles, crypto_pyaes, dask, deepcopy, deepcopy_memo, deepcopy_reduce, deltablue, django_template, djangocms, docutils, dulwich_log, fannkuch, flaskblogging, float, gc_traversal, generators, genshi_text, genshi_xml, go, gunicorn, hexiom, html5lib, json, json_dumps, json_loads, logging_format, logging_silent, logging_simple, mako, mdp, meteor_contest, mypy2, nbody, nqueens, pathlib, pickle, pickle_dict, pickle_list, pickle_pure_python, pidigits, pprint_pformat, pprint_safe_repr, pycparser, pyflate, pylint, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, spectral_norm, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sqlite_synth, sympy_expand, sympy_integrate, sympy_str, sympy_sum, telco, thrift, tomli_loads, tornado_http, typing_runtime_protocols, unpickle, unpickle_list, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [📄table](bm-20240724-linux-x86_64-python-5592399313c963c11028-3.14.0a0-5592399-vs-3.13.0b2.md)
- [📈time plot](bm-20240724-linux-x86_64-python-5592399313c963c11028-3.14.0a0-5592399-vs-3.13.0b2.svg)

