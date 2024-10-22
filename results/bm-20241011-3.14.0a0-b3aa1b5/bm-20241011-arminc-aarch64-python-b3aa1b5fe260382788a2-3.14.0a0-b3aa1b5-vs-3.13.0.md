# Results vs. 3.13.0

- fork: python
- ref: b3aa1b5fe260382788a2
- machine: linux-aarch64
- commit hash: b3aa1b5
- commit date: 2024-10-11
- overall geometric mean: 1.05x slower
- HPT reliability: 96.43%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 293 ms: 1.05x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.03 sec: 1.04x slower                                                  |
| tornado_http   | 131 ms                                                   | 126 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 545 ms: 1.19x faster                                                    |
| async_tree_none            | 493 ms                                                   | 428 ms: 1.15x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 550 ms: 1.14x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 420 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 722 ms: 1.06x faster                                                    |
| async_generators           | 496 ms                                                   | 475 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 708 ms: 1.04x faster                                                    |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.15 sec: 1.05x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.16 sec: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (2): asyncio_tcp, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                   | 124 ms: 1.04x faster                                                    |
| regex_v8       | 31.5 ms                                                  | 31.0 ms: 1.02x faster                                                   |
| regex_effbot   | 4.87 ms                                                  | 5.01 ms: 1.03x slower                                                   |
| regex_dna      | 246 ms                                                   | 260 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle            | 20.2 us                                                  | 19.2 us: 1.05x faster                                                   |
| pickle_list         | 5.34 us                                                  | 5.17 us: 1.03x faster                                                   |
| unpickle_list       | 6.65 us                                                  | 6.53 us: 1.02x faster                                                   |
| pickle_pure_python  | 359 us                                                   | 364 us: 1.01x slower                                                    |
| pickle              | 13.5 us                                                  | 13.9 us: 1.03x slower                                                   |
| xml_etree_iterparse | 147 ms                                                   | 153 ms: 1.04x slower                                                    |
| tomli_loads         | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                                  |
| xml_etree_parse     | 188 ms                                                   | 198 ms: 1.06x slower                                                    |
| json_dumps          | 13.4 ms                                                  | 14.6 ms: 1.09x slower                                                   |
| Geometric mean      | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (5): pickle_dict, xml_etree_generate, json_loads, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.7 ms                                                  | 27.1 ms: 1.02x faster                                                   |
| mako           | 13.3 ms                                                  | 13.6 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 332 us: 1.36x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 37.8 us: 1.35x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 545 ms: 1.19x faster                                                    |
| go                         | 163 ms                                                   | 137 ms: 1.19x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.51 us: 1.16x faster                                                   |
| async_tree_none            | 493 ms                                                   | 428 ms: 1.15x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 550 ms: 1.14x faster                                                    |
| unpack_sequence            | 57.2 ns                                                  | 51.2 ns: 1.12x faster                                                   |
| async_tree_none_tg         | 467 ms                                                   | 420 ms: 1.11x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.7 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 722 ms: 1.06x faster                                                    |
| pathlib                    | 22.4 ms                                                  | 21.2 ms: 1.05x faster                                                   |
| unpickle                   | 20.2 us                                                  | 19.2 us: 1.05x faster                                                   |
| 2to3                       | 306 ms                                                   | 293 ms: 1.05x faster                                                    |
| telco                      | 9.73 ms                                                  | 9.31 ms: 1.05x faster                                                   |
| async_generators           | 496 ms                                                   | 475 ms: 1.04x faster                                                    |
| tornado_http               | 131 ms                                                   | 126 ms: 1.04x faster                                                    |
| logging_silent             | 135 ns                                                   | 130 ns: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 708 ms: 1.04x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                    |
| regex_compile              | 128 ms                                                   | 124 ms: 1.04x faster                                                    |
| logging_format             | 7.83 us                                                  | 7.55 us: 1.04x faster                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 5.70 sec: 1.04x faster                                                  |
| pickle_list                | 5.34 us                                                  | 5.17 us: 1.03x faster                                                   |
| meteor_contest             | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| genshi_text                | 27.7 ms                                                  | 27.1 ms: 1.02x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.24 sec: 1.02x faster                                                  |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| unpickle_list              | 6.65 us                                                  | 6.53 us: 1.02x faster                                                   |
| sqlglot_normalize          | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 926 ms                                                   | 911 ms: 1.02x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 31.0 ms: 1.02x faster                                                   |
| thrift                     | 946 us                                                   | 931 us: 1.02x faster                                                    |
| scimark_fft                | 447 ms                                                   | 441 ms: 1.02x faster                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 81.5 ms: 1.01x faster                                                   |
| richards                   | 53.5 ms                                                  | 52.9 ms: 1.01x faster                                                   |
| mdp                        | 3.36 sec                                                 | 3.33 sec: 1.01x faster                                                  |
| logging_simple             | 7.04 us                                                  | 6.96 us: 1.01x faster                                                   |
| pprint_pformat             | 1.90 sec                                                 | 1.89 sec: 1.01x faster                                                  |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                                   |
| nqueens                    | 98.7 ms                                                  | 100.0 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                                  |
| scimark_sor                | 159 ms                                                   | 161 ms: 1.01x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 364 us: 1.01x slower                                                    |
| comprehensions             | 20.4 us                                                  | 20.7 us: 1.02x slower                                                   |
| sqlite_synth               | 3.84 us                                                  | 3.90 us: 1.02x slower                                                   |
| mako                       | 13.3 ms                                                  | 13.6 ms: 1.02x slower                                                   |
| deltablue                  | 3.85 ms                                                  | 3.92 ms: 1.02x slower                                                   |
| typing_runtime_protocols   | 192 us                                                   | 196 us: 1.02x slower                                                    |
| chaos                      | 68.8 ms                                                  | 70.5 ms: 1.02x slower                                                   |
| regex_effbot               | 4.87 ms                                                  | 5.01 ms: 1.03x slower                                                   |
| pickle                     | 13.5 us                                                  | 13.9 us: 1.03x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.42 ms: 1.03x slower                                                   |
| raytrace                   | 298 ms                                                   | 310 ms: 1.04x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                   | 153 ms: 1.04x slower                                                    |
| docutils                   | 2.91 sec                                                 | 3.03 sec: 1.04x slower                                                  |
| fannkuch                   | 452 ms                                                   | 471 ms: 1.04x slower                                                    |
| pyflate                    | 556 ms                                                   | 582 ms: 1.05x slower                                                    |
| tomli_loads                | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.15 sec: 1.05x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.16 sec: 1.05x slower                                                  |
| xml_etree_parse            | 188 ms                                                   | 198 ms: 1.06x slower                                                    |
| regex_dna                  | 246 ms                                                   | 260 ms: 1.06x slower                                                    |
| json_dumps                 | 13.4 ms                                                  | 14.6 ms: 1.09x slower                                                   |
| create_gc_cycles           | 2.12 ms                                                  | 2.37 ms: 1.12x slower                                                   |
| gc_traversal               | 4.53 ms                                                  | 5.09 ms: 1.12x slower                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 5.11 sec: 700.45x slower                                                |
| Geometric mean             | (ref)                                                    | 1.05x slower                                                            |

Benchmark hidden because not significant (29): pickle_dict, sympy_sum, xml_etree_generate, spectral_norm, asyncio_tcp, python_startup_no_site, json, genshi_xml, richards_super, coverage, json_loads, hexiom, html5lib, xml_etree_process, sqlglot_optimize, bench_thread_pool, sympy_str, pidigits, unpickle_pure_python, asyncio_websockets, float, scimark_sparse_mat_mult, sympy_expand, django_template, nbody, sqlglot_transpile, sympy_integrate, scimark_monte_carlo, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241011-3.14.0a0-b3aa1b5/bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json: dulwich_log

# HPT report

- Reliability score: 96.43% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x