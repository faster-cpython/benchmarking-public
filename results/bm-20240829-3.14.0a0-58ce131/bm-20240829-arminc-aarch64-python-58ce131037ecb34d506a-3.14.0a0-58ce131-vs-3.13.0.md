# Results vs. 3.13.0

- fork: python
- ref: 58ce131037ecb34d506a
- machine: linux-aarch64
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.02x faster
- HPT reliability: 99.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 297 ms: 1.03x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| html5lib       | 64.3 ms                                                  | 63.5 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 552 ms: 1.18x faster                                                    |
| async_tree_none           | 493 ms                                                   | 424 ms: 1.16x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 413 ms: 1.13x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 555 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 731 ms: 1.04x faster                                                    |
| async_generators          | 496 ms                                                   | 482 ms: 1.03x faster                                                    |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                                  |
| coroutines                | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                                   |
| async_tree_io             | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| async_tree_io_tg          | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                                  |
| Geometric mean            | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, asyncio_tcp, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| float          | 94.4 ms                                                  | 92.6 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| regex_compile  | 128 ms                                                   | 125 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python  | 359 us                                                   | 363 us: 1.01x slower                                                    |
| xml_etree_iterparse | 147 ms                                                   | 149 ms: 1.02x slower                                                    |
| json_loads          | 31.4 us                                                  | 32.6 us: 1.04x slower                                                   |
| tomli_loads         | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| Geometric mean      | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (5): unpickle_pure_python, xml_etree_process, xml_etree_generate, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.3 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                  | 451 us                                                   | 334 us: 1.35x faster                                                    |
| deepcopy_memo             | 51.0 us                                                  | 38.1 us: 1.34x faster                                                   |
| go                        | 163 ms                                                   | 137 ms: 1.19x faster                                                    |
| async_tree_memoization_tg | 649 ms                                                   | 552 ms: 1.18x faster                                                    |
| async_tree_none           | 493 ms                                                   | 424 ms: 1.16x faster                                                    |
| deepcopy_reduce           | 4.07 us                                                  | 3.56 us: 1.14x faster                                                   |
| async_tree_none_tg        | 467 ms                                                   | 413 ms: 1.13x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 555 ms: 1.13x faster                                                    |
| generators                | 37.8 ms                                                  | 34.8 ms: 1.09x faster                                                   |
| pathlib                   | 22.4 ms                                                  | 21.1 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 731 ms: 1.04x faster                                                    |
| scimark_lu                | 139 ms                                                   | 134 ms: 1.04x faster                                                    |
| nbody                     | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| regex_v8                  | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.33 ms: 1.04x faster                                                   |
| pycparser                 | 1.26 sec                                                 | 1.22 sec: 1.04x faster                                                  |
| bench_mp_pool             | 7.30 ms                                                  | 7.04 ms: 1.04x faster                                                   |
| 2to3                      | 306 ms                                                   | 297 ms: 1.03x faster                                                    |
| async_generators          | 496 ms                                                   | 482 ms: 1.03x faster                                                    |
| scimark_monte_carlo       | 83.8 ms                                                  | 81.4 ms: 1.03x faster                                                   |
| regex_compile             | 128 ms                                                   | 125 ms: 1.03x faster                                                    |
| bench_thread_pool         | 1.28 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| logging_silent            | 135 ns                                                   | 132 ns: 1.02x faster                                                    |
| sqlglot_normalize         | 128 ms                                                   | 125 ms: 1.02x faster                                                    |
| logging_format            | 7.83 us                                                  | 7.66 us: 1.02x faster                                                   |
| float                     | 94.4 ms                                                  | 92.6 ms: 1.02x faster                                                   |
| meteor_contest            | 113 ms                                                   | 112 ms: 1.02x faster                                                    |
| hexiom                    | 7.13 ms                                                  | 7.02 ms: 1.02x faster                                                   |
| scimark_fft               | 447 ms                                                   | 440 ms: 1.02x faster                                                    |
| html5lib                  | 64.3 ms                                                  | 63.5 ms: 1.01x faster                                                   |
| mdp                       | 3.36 sec                                                 | 3.34 sec: 1.01x faster                                                  |
| bpe_tokeniser             | 5.90 sec                                                 | 5.85 sec: 1.01x faster                                                  |
| pyflate                   | 556 ms                                                   | 560 ms: 1.01x slower                                                    |
| pprint_pformat            | 1.90 sec                                                 | 1.91 sec: 1.01x slower                                                  |
| pickle_pure_python        | 359 us                                                   | 363 us: 1.01x slower                                                    |
| sympy_expand              | 455 ms                                                   | 459 ms: 1.01x slower                                                    |
| mako                      | 13.3 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| raytrace                  | 298 ms                                                   | 301 ms: 1.01x slower                                                    |
| typing_runtime_protocols  | 192 us                                                   | 194 us: 1.01x slower                                                    |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                                  |
| coroutines                | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                                   |
| pprint_safe_repr          | 926 ms                                                   | 942 ms: 1.02x slower                                                    |
| xml_etree_iterparse       | 147 ms                                                   | 149 ms: 1.02x slower                                                    |
| fannkuch                  | 452 ms                                                   | 460 ms: 1.02x slower                                                    |
| nqueens                   | 98.7 ms                                                  | 101 ms: 1.02x slower                                                    |
| sqlglot_parse             | 1.38 ms                                                  | 1.42 ms: 1.03x slower                                                   |
| docutils                  | 2.91 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| telco                     | 9.73 ms                                                  | 10.1 ms: 1.04x slower                                                   |
| async_tree_io             | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| json_loads                | 31.4 us                                                  | 32.6 us: 1.04x slower                                                   |
| tomli_loads               | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| gc_traversal              | 4.53 ms                                                  | 4.84 ms: 1.07x slower                                                   |
| async_tree_io_tg          | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                                  |
| create_gc_cycles          | 2.12 ms                                                  | 2.29 ms: 1.08x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (35): tornado_http, sympy_sum, richards_super, scimark_sor, async_tree_cpu_io_mixed_tg, python_startup, asyncio_tcp, sqlglot_optimize, chaos, sympy_integrate, regex_effbot, unpickle_pure_python, crypto_pyaes, sqlglot_transpile, xml_etree_process, xml_etree_generate, genshi_text, comprehensions, pidigits, spectral_norm, richards, coverage, logging_simple, regex_dna, asyncio_websockets, xml_etree_parse, sympy_str, python_startup_no_site, thrift, django_template, json, json_dumps, deltablue, genshi_xml, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.52% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x