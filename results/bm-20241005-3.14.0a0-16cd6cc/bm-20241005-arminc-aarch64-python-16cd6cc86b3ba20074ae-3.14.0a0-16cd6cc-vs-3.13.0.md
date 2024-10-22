# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-aarch64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.05x slower
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 294 ms: 1.04x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 552 ms: 1.18x faster                                                    |
| async_tree_none            | 493 ms                                                   | 424 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 412 ms: 1.14x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 555 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 728 ms: 1.05x faster                                                    |
| async_generators           | 496 ms                                                   | 476 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 721 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.17 sec: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): asyncio_tcp, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| float          | 94.4 ms                                                  | 93.0 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.7 ms: 1.03x faster                                                   |
| regex_compile  | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| regex_effbot   | 4.87 ms                                                  | 4.99 ms: 1.03x slower                                                   |
| regex_dna      | 246 ms                                                   | 259 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle        | 20.2 us                                                  | 19.5 us: 1.03x faster                                                   |
| pickle_dict     | 38.1 us                                                  | 37.4 us: 1.02x faster                                                   |
| pickle_list     | 5.34 us                                                  | 5.27 us: 1.01x faster                                                   |
| xml_etree_parse | 188 ms                                                   | 186 ms: 1.01x faster                                                    |
| pickle          | 13.5 us                                                  | 13.7 us: 1.02x slower                                                   |
| tomli_loads     | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (8): json_dumps, unpickle_list, json_loads, xml_etree_generate, unpickle_pure_python, xml_etree_process, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| python_startup_no_site | 8.75 ms                                                  | 8.61 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.02x faster                                                            |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, django_template, genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 335 us: 1.35x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 38.1 us: 1.34x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 552 ms: 1.18x faster                                                    |
| go                         | 163 ms                                                   | 138 ms: 1.17x faster                                                    |
| async_tree_none            | 493 ms                                                   | 424 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.52 us: 1.15x faster                                                   |
| async_tree_none_tg         | 467 ms                                                   | 412 ms: 1.14x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 555 ms: 1.13x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.7 ms: 1.09x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 21.2 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 728 ms: 1.05x faster                                                    |
| scimark_fft                | 447 ms                                                   | 427 ms: 1.05x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 133 ms: 1.05x faster                                                    |
| async_generators           | 496 ms                                                   | 476 ms: 1.04x faster                                                    |
| logging_silent             | 135 ns                                                   | 130 ns: 1.04x faster                                                    |
| 2to3                       | 306 ms                                                   | 294 ms: 1.04x faster                                                    |
| nbody                      | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| unpickle                   | 20.2 us                                                  | 19.5 us: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.37 ms: 1.03x faster                                                   |
| telco                      | 9.73 ms                                                  | 9.45 ms: 1.03x faster                                                   |
| thrift                     | 946 us                                                   | 920 us: 1.03x faster                                                    |
| python_startup             | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| regex_v8                   | 31.5 ms                                                  | 30.7 ms: 1.03x faster                                                   |
| sympy_sum                  | 143 ms                                                   | 140 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                 | 1.23 sec: 1.02x faster                                                  |
| pprint_safe_repr           | 926 ms                                                   | 907 ms: 1.02x faster                                                    |
| pickle_dict                | 38.1 us                                                  | 37.4 us: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 721 ms: 1.02x faster                                                    |
| regex_compile              | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| richards_super             | 60.3 ms                                                  | 59.3 ms: 1.02x faster                                                   |
| python_startup_no_site     | 8.75 ms                                                  | 8.61 ms: 1.02x faster                                                   |
| json                       | 5.61 ms                                                  | 5.53 ms: 1.01x faster                                                   |
| float                      | 94.4 ms                                                  | 93.0 ms: 1.01x faster                                                   |
| pickle_list                | 5.34 us                                                  | 5.27 us: 1.01x faster                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.8 ms: 1.01x faster                                                   |
| mdp                        | 3.36 sec                                                 | 3.33 sec: 1.01x faster                                                  |
| xml_etree_parse            | 188 ms                                                   | 186 ms: 1.01x faster                                                    |
| bpe_tokeniser              | 5.90 sec                                                 | 5.85 sec: 1.01x faster                                                  |
| pprint_pformat             | 1.90 sec                                                 | 1.89 sec: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                                   |
| comprehensions             | 20.4 us                                                  | 20.6 us: 1.01x slower                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.30 ms: 1.02x slower                                                   |
| deltablue                  | 3.85 ms                                                  | 3.92 ms: 1.02x slower                                                   |
| pickle                     | 13.5 us                                                  | 13.7 us: 1.02x slower                                                   |
| raytrace                   | 298 ms                                                   | 305 ms: 1.02x slower                                                    |
| regex_effbot               | 4.87 ms                                                  | 4.99 ms: 1.03x slower                                                   |
| fannkuch                   | 452 ms                                                   | 468 ms: 1.04x slower                                                    |
| docutils                   | 2.91 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| sqlglot_parse              | 1.38 ms                                                  | 1.43 ms: 1.04x slower                                                   |
| pyflate                    | 556 ms                                                   | 579 ms: 1.04x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| tomli_loads                | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| regex_dna                  | 246 ms                                                   | 259 ms: 1.05x slower                                                    |
| create_gc_cycles           | 2.12 ms                                                  | 2.28 ms: 1.07x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.17 sec: 1.08x slower                                                  |
| gc_traversal               | 4.53 ms                                                  | 5.02 ms: 1.11x slower                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 4.42 sec: 606.12x slower                                                |
| Geometric mean             | (ref)                                                    | 1.05x slower                                                            |

Benchmark hidden because not significant (38): tornado_http, asyncio_tcp, logging_format, meteor_contest, json_dumps, scimark_sor, richards, unpickle_list, crypto_pyaes, sqlite_synth, json_loads, sqlglot_normalize, nqueens, xml_etree_generate, genshi_text, unpickle_pure_python, hexiom, django_template, unpack_sequence, sympy_integrate, sympy_str, sqlglot_transpile, xml_etree_process, pidigits, sympy_expand, asyncio_websockets, html5lib, pickle_pure_python, typing_runtime_protocols, genshi_xml, coverage, chaos, sqlglot_optimize, spectral_norm, logging_simple, xml_etree_iterparse, pylint, mako
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: dulwich_log

# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x