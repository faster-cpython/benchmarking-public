# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-aarch64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.02x faster
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 295 ms: 1.03x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.01 sec: 1.03x slower                                                  |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 555 ms: 1.17x faster                                                    |
| async_tree_none            | 493 ms                                                   | 424 ms: 1.16x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 558 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 422 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 737 ms: 1.04x faster                                                    |
| async_generators           | 496 ms                                                   | 483 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 728 ms: 1.01x faster                                                    |
| coroutines                 | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.19 sec: 1.09x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.03x faster                                                    |
| float          | 94.4 ms                                                  | 92.7 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| regex_compile  | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| regex_dna      | 246 ms                                                   | 249 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle            | 20.2 us                                                  | 19.4 us: 1.04x faster                                                   |
| unpickle_list       | 6.65 us                                                  | 6.41 us: 1.04x faster                                                   |
| pickle_list         | 5.34 us                                                  | 5.19 us: 1.03x faster                                                   |
| json_loads          | 31.4 us                                                  | 31.8 us: 1.01x slower                                                   |
| xml_etree_iterparse | 147 ms                                                   | 149 ms: 1.01x slower                                                    |
| tomli_loads         | 2.53 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| Geometric mean      | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (8): pickle_dict, xml_etree_generate, json_dumps, unpickle_pure_python, xml_etree_process, pickle, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| python_startup_no_site | 8.75 ms                                                  | 8.62 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.02x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.3 ms                                                  | 13.5 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 37.7 us: 1.35x faster                                                   |
| deepcopy                   | 451 us                                                   | 334 us: 1.35x faster                                                    |
| go                         | 163 ms                                                   | 139 ms: 1.17x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 555 ms: 1.17x faster                                                    |
| async_tree_none            | 493 ms                                                   | 424 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.52 us: 1.16x faster                                                   |
| async_tree_memoization     | 626 ms                                                   | 558 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 422 ms: 1.11x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.7 ms: 1.09x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 20.7 ms: 1.08x faster                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 7.01 ms: 1.04x faster                                                   |
| unpickle                   | 20.2 us                                                  | 19.4 us: 1.04x faster                                                   |
| regex_v8                   | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.22 sec: 1.04x faster                                                  |
| unpickle_list              | 6.65 us                                                  | 6.41 us: 1.04x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 737 ms: 1.04x faster                                                    |
| bench_thread_pool          | 1.28 ms                                                  | 1.23 ms: 1.03x faster                                                   |
| 2to3                       | 306 ms                                                   | 295 ms: 1.03x faster                                                    |
| nbody                      | 114 ms                                                   | 110 ms: 1.03x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 135 ms: 1.03x faster                                                    |
| pickle_list                | 5.34 us                                                  | 5.19 us: 1.03x faster                                                   |
| async_generators           | 496 ms                                                   | 483 ms: 1.03x faster                                                    |
| python_startup             | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| logging_format             | 7.83 us                                                  | 7.63 us: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.42 ms: 1.03x faster                                                   |
| logging_silent             | 135 ns                                                   | 133 ns: 1.02x faster                                                    |
| meteor_contest             | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| float                      | 94.4 ms                                                  | 92.7 ms: 1.02x faster                                                   |
| regex_compile              | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 81.3 ms: 1.02x faster                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.5 ms: 1.02x faster                                                   |
| thrift                     | 946 us                                                   | 931 us: 1.02x faster                                                    |
| richards_super             | 60.3 ms                                                  | 59.4 ms: 1.02x faster                                                   |
| richards                   | 53.5 ms                                                  | 52.7 ms: 1.02x faster                                                   |
| python_startup_no_site     | 8.75 ms                                                  | 8.62 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 728 ms: 1.01x faster                                                    |
| scimark_fft                | 447 ms                                                   | 442 ms: 1.01x faster                                                    |
| mdp                        | 3.36 sec                                                 | 3.33 sec: 1.01x faster                                                  |
| bpe_tokeniser              | 5.90 sec                                                 | 5.86 sec: 1.01x faster                                                  |
| pprint_pformat             | 1.90 sec                                                 | 1.91 sec: 1.00x slower                                                  |
| json_loads                 | 31.4 us                                                  | 31.8 us: 1.01x slower                                                   |
| regex_dna                  | 246 ms                                                   | 249 ms: 1.01x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.40 ms: 1.01x slower                                                   |
| pyflate                    | 556 ms                                                   | 562 ms: 1.01x slower                                                    |
| telco                      | 9.73 ms                                                  | 9.86 ms: 1.01x slower                                                   |
| sympy_expand               | 455 ms                                                   | 460 ms: 1.01x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                   | 149 ms: 1.01x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                                   |
| mako                       | 13.3 ms                                                  | 13.5 ms: 1.02x slower                                                   |
| raytrace                   | 298 ms                                                   | 303 ms: 1.02x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 3.92 ms: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                                  |
| fannkuch                   | 452 ms                                                   | 460 ms: 1.02x slower                                                    |
| nqueens                    | 98.7 ms                                                  | 101 ms: 1.02x slower                                                    |
| unpack_sequence            | 57.2 ns                                                  | 59.0 ns: 1.03x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| docutils                   | 2.91 sec                                                 | 3.01 sec: 1.03x slower                                                  |
| tomli_loads                | 2.53 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.19 sec: 1.09x slower                                                  |
| create_gc_cycles           | 2.12 ms                                                  | 2.33 ms: 1.10x slower                                                   |
| gc_traversal               | 4.53 ms                                                  | 5.18 ms: 1.14x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (35): tornado_http, pickle_dict, sympy_sum, django_template, xml_etree_generate, scimark_sor, coverage, sqlite_synth, json, spectral_norm, json_dumps, unpickle_pure_python, sqlglot_normalize, sympy_integrate, xml_etree_process, genshi_text, logging_simple, hexiom, pprint_safe_repr, sqlglot_optimize, pidigits, sympy_str, chaos, genshi_xml, typing_runtime_protocols, pickle, sqlglot_transpile, xml_etree_parse, pickle_pure_python, comprehensions, asyncio_websockets, regex_effbot, asyncio_tcp, html5lib, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: dulwich_log

# HPT report

- Reliability score: 99.79% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x