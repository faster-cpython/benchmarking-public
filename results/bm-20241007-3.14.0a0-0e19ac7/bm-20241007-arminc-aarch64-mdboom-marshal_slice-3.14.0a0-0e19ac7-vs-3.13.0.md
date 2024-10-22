# Results vs. 3.13.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-aarch64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.05x slower
- HPT reliability: 99.41%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 296 ms: 1.03x faster                                             |
| docutils       | 2.91 sec                                                 | 3.01 sec: 1.04x slower                                           |
| html5lib       | 64.3 ms                                                  | 63.1 ms: 1.02x faster                                            |
| tornado_http   | 131 ms                                                   | 126 ms: 1.05x faster                                             |
| Geometric mean | (ref)                                                    | 1.02x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 550 ms: 1.18x faster                                             |
| async_tree_none            | 493 ms                                                   | 429 ms: 1.15x faster                                             |
| async_tree_memoization     | 626 ms                                                   | 553 ms: 1.13x faster                                             |
| async_tree_none_tg         | 467 ms                                                   | 421 ms: 1.11x faster                                             |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 714 ms: 1.07x faster                                             |
| async_generators           | 496 ms                                                   | 475 ms: 1.05x faster                                             |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 705 ms: 1.04x faster                                             |
| coroutines                 | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                            |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                           |
| async_tree_io              | 1.11 sec                                                 | 1.17 sec: 1.06x slower                                           |
| async_tree_io_tg           | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                           |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                     |

Benchmark hidden because not significant (2): asyncio_tcp, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                    | 1.01x faster                                                     |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 128 ms                                                   | 125 ms: 1.02x faster                                             |
| regex_v8       | 31.5 ms                                                  | 30.8 ms: 1.02x faster                                            |
| regex_effbot   | 4.87 ms                                                  | 4.99 ms: 1.02x slower                                            |
| regex_dna      | 246 ms                                                   | 254 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                    | 1.00x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|---------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle            | 20.2 us                                                  | 19.5 us: 1.03x faster                                            |
| pickle_list         | 5.34 us                                                  | 5.23 us: 1.02x faster                                            |
| json_loads          | 31.4 us                                                  | 31.1 us: 1.01x faster                                            |
| pickle_pure_python  | 359 us                                                   | 366 us: 1.02x slower                                             |
| xml_etree_parse     | 188 ms                                                   | 193 ms: 1.03x slower                                             |
| pickle              | 13.5 us                                                  | 13.9 us: 1.03x slower                                            |
| xml_etree_iterparse | 147 ms                                                   | 152 ms: 1.04x slower                                             |
| tomli_loads         | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                           |
| Geometric mean      | (ref)                                                    | 1.01x slower                                                     |

Benchmark hidden because not significant (6): json_dumps, xml_etree_generate, unpickle_list, pickle_dict, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                            |
| Geometric mean | (ref)                                                    | 1.01x faster                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text    | 27.7 ms                                                  | 27.2 ms: 1.02x faster                                            |
| Geometric mean | (ref)                                                    | 1.00x faster                                                     |

Benchmark hidden because not significant (3): django_template, mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 331 us: 1.36x faster                                             |
| deepcopy_memo              | 51.0 us                                                  | 37.9 us: 1.35x faster                                            |
| async_tree_memoization_tg  | 649 ms                                                   | 550 ms: 1.18x faster                                             |
| deepcopy_reduce            | 4.07 us                                                  | 3.45 us: 1.18x faster                                            |
| go                         | 163 ms                                                   | 138 ms: 1.18x faster                                             |
| async_tree_none            | 493 ms                                                   | 429 ms: 1.15x faster                                             |
| async_tree_memoization     | 626 ms                                                   | 553 ms: 1.13x faster                                             |
| async_tree_none_tg         | 467 ms                                                   | 421 ms: 1.11x faster                                             |
| generators                 | 37.8 ms                                                  | 35.2 ms: 1.08x faster                                            |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 714 ms: 1.07x faster                                             |
| scimark_lu                 | 139 ms                                                   | 132 ms: 1.06x faster                                             |
| telco                      | 9.73 ms                                                  | 9.25 ms: 1.05x faster                                            |
| scimark_fft                | 447 ms                                                   | 426 ms: 1.05x faster                                             |
| tornado_http               | 131 ms                                                   | 126 ms: 1.05x faster                                             |
| async_generators           | 496 ms                                                   | 475 ms: 1.05x faster                                             |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 705 ms: 1.04x faster                                             |
| unpack_sequence            | 57.2 ns                                                  | 54.8 ns: 1.04x faster                                            |
| pathlib                    | 22.4 ms                                                  | 21.5 ms: 1.04x faster                                            |
| nbody                      | 114 ms                                                   | 110 ms: 1.04x faster                                             |
| unpickle                   | 20.2 us                                                  | 19.5 us: 1.03x faster                                            |
| 2to3                       | 306 ms                                                   | 296 ms: 1.03x faster                                             |
| bpe_tokeniser              | 5.90 sec                                                 | 5.72 sec: 1.03x faster                                           |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.39 ms: 1.03x faster                                            |
| logging_silent             | 135 ns                                                   | 132 ns: 1.03x faster                                             |
| pprint_safe_repr           | 926 ms                                                   | 904 ms: 1.02x faster                                             |
| regex_compile              | 128 ms                                                   | 125 ms: 1.02x faster                                             |
| meteor_contest             | 113 ms                                                   | 111 ms: 1.02x faster                                             |
| regex_v8                   | 31.5 ms                                                  | 30.8 ms: 1.02x faster                                            |
| sympy_sum                  | 143 ms                                                   | 140 ms: 1.02x faster                                             |
| json                       | 5.61 ms                                                  | 5.50 ms: 1.02x faster                                            |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                            |
| pprint_pformat             | 1.90 sec                                                 | 1.86 sec: 1.02x faster                                           |
| pickle_list                | 5.34 us                                                  | 5.23 us: 1.02x faster                                            |
| html5lib                   | 64.3 ms                                                  | 63.1 ms: 1.02x faster                                            |
| pycparser                  | 1.26 sec                                                 | 1.24 sec: 1.02x faster                                           |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.4 ms: 1.02x faster                                            |
| genshi_text                | 27.7 ms                                                  | 27.2 ms: 1.02x faster                                            |
| scimark_sor                | 159 ms                                                   | 157 ms: 1.01x faster                                             |
| richards                   | 53.5 ms                                                  | 52.7 ms: 1.01x faster                                            |
| hexiom                     | 7.13 ms                                                  | 7.03 ms: 1.01x faster                                            |
| json_loads                 | 31.4 us                                                  | 31.1 us: 1.01x faster                                            |
| mdp                        | 3.36 sec                                                 | 3.34 sec: 1.01x faster                                           |
| logging_simple             | 7.04 us                                                  | 7.11 us: 1.01x slower                                            |
| sympy_expand               | 455 ms                                                   | 459 ms: 1.01x slower                                             |
| chaos                      | 68.8 ms                                                  | 69.7 ms: 1.01x slower                                            |
| coroutines                 | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                            |
| thrift                     | 946 us                                                   | 962 us: 1.02x slower                                             |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                           |
| pickle_pure_python         | 359 us                                                   | 366 us: 1.02x slower                                             |
| deltablue                  | 3.85 ms                                                  | 3.93 ms: 1.02x slower                                            |
| raytrace                   | 298 ms                                                   | 304 ms: 1.02x slower                                             |
| regex_effbot               | 4.87 ms                                                  | 4.99 ms: 1.02x slower                                            |
| xml_etree_parse            | 188 ms                                                   | 193 ms: 1.03x slower                                             |
| pickle                     | 13.5 us                                                  | 13.9 us: 1.03x slower                                            |
| regex_dna                  | 246 ms                                                   | 254 ms: 1.03x slower                                             |
| sqlglot_parse              | 1.38 ms                                                  | 1.43 ms: 1.03x slower                                            |
| docutils                   | 2.91 sec                                                 | 3.01 sec: 1.04x slower                                           |
| xml_etree_iterparse        | 147 ms                                                   | 152 ms: 1.04x slower                                             |
| fannkuch                   | 452 ms                                                   | 471 ms: 1.04x slower                                             |
| tomli_loads                | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                           |
| pyflate                    | 556 ms                                                   | 583 ms: 1.05x slower                                             |
| async_tree_io              | 1.11 sec                                                 | 1.17 sec: 1.06x slower                                           |
| async_tree_io_tg           | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                           |
| create_gc_cycles           | 2.12 ms                                                  | 2.35 ms: 1.11x slower                                            |
| gc_traversal               | 4.53 ms                                                  | 5.07 ms: 1.12x slower                                            |
| bench_mp_pool              | 7.30 ms                                                  | 5.20 sec: 712.83x slower                                         |
| Geometric mean             | (ref)                                                    | 1.05x slower                                                     |

Benchmark hidden because not significant (30): asyncio_tcp, richards_super, sqlglot_normalize, crypto_pyaes, json_dumps, python_startup_no_site, sqlglot_optimize, sqlite_synth, django_template, xml_etree_generate, logging_format, nqueens, bench_thread_pool, unpickle_list, pickle_dict, pidigits, unpickle_pure_python, float, mako, xml_etree_process, spectral_norm, genshi_xml, comprehensions, asyncio_websockets, coverage, sympy_str, sympy_integrate, sqlglot_transpile, typing_runtime_protocols, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: dulwich_log

# HPT report

- Reliability score: 99.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x