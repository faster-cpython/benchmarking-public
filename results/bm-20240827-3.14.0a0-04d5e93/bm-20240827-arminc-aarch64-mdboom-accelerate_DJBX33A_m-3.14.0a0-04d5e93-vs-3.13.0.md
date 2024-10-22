# Results vs. 3.13.0

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: linux-aarch64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 294 ms: 1.04x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.07 sec: 1.06x slower                                                  |
| html5lib       | 64.3 ms                                                  | 64.7 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 551 ms: 1.18x faster                                                    |
| async_tree_none            | 493 ms                                                   | 426 ms: 1.16x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 556 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 417 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 727 ms: 1.05x faster                                                    |
| async_generators           | 496 ms                                                   | 485 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 726 ms: 1.01x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.13 sec: 1.02x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 583 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| float          | 94.4 ms                                                  | 92.6 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                   | 125 ms: 1.03x faster                                                    |
| regex_v8       | 31.5 ms                                                  | 30.7 ms: 1.03x faster                                                   |
| regex_effbot   | 4.87 ms                                                  | 4.81 ms: 1.01x faster                                                   |
| regex_dna      | 246 ms                                                   | 245 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_process   | 80.1 ms                                                  | 77.5 ms: 1.03x faster                                                   |
| xml_etree_iterparse | 147 ms                                                   | 146 ms: 1.01x faster                                                    |
| pickle_pure_python  | 359 us                                                   | 357 us: 1.01x faster                                                    |
| tomli_loads         | 2.53 sec                                                 | 2.55 sec: 1.01x slower                                                  |
| json_loads          | 31.4 us                                                  | 32.2 us: 1.03x slower                                                   |
| Geometric mean      | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (4): json_dumps, unpickle_pure_python, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 60.2 ms                                                  | 59.1 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (3): genshi_text, django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 329 us: 1.37x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 37.6 us: 1.36x faster                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 3.45 us: 1.18x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 551 ms: 1.18x faster                                                    |
| async_tree_none            | 493 ms                                                   | 426 ms: 1.16x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 556 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 417 ms: 1.12x faster                                                    |
| generators                 | 37.8 ms                                                  | 35.1 ms: 1.08x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 21.3 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 727 ms: 1.05x faster                                                    |
| nbody                      | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| bench_mp_pool              | 7.30 ms                                                  | 6.98 ms: 1.05x faster                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.22 ms: 1.04x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                    |
| 2to3                       | 306 ms                                                   | 294 ms: 1.04x faster                                                    |
| xml_etree_process          | 80.1 ms                                                  | 77.5 ms: 1.03x faster                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 81.2 ms: 1.03x faster                                                   |
| pprint_safe_repr           | 926 ms                                                   | 898 ms: 1.03x faster                                                    |
| regex_compile              | 128 ms                                                   | 125 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                 | 1.23 sec: 1.03x faster                                                  |
| logging_silent             | 135 ns                                                   | 132 ns: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.41 ms: 1.03x faster                                                   |
| regex_v8                   | 31.5 ms                                                  | 30.7 ms: 1.03x faster                                                   |
| sqlglot_optimize           | 62.4 ms                                                  | 61.0 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.90 sec                                                 | 1.85 sec: 1.02x faster                                                  |
| async_generators           | 496 ms                                                   | 485 ms: 1.02x faster                                                    |
| sympy_sum                  | 143 ms                                                   | 141 ms: 1.02x faster                                                    |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| hexiom                     | 7.13 ms                                                  | 7.00 ms: 1.02x faster                                                   |
| thrift                     | 946 us                                                   | 928 us: 1.02x faster                                                    |
| float                      | 94.4 ms                                                  | 92.6 ms: 1.02x faster                                                   |
| genshi_xml                 | 60.2 ms                                                  | 59.1 ms: 1.02x faster                                                   |
| scimark_fft                | 447 ms                                                   | 440 ms: 1.02x faster                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 1.70 ms: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                   | 112 ms: 1.02x faster                                                    |
| coverage                   | 98.5 ms                                                  | 96.9 ms: 1.02x faster                                                   |
| sympy_integrate            | 21.0 ms                                                  | 20.6 ms: 1.02x faster                                                   |
| logging_simple             | 7.04 us                                                  | 6.93 us: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 726 ms: 1.01x faster                                                    |
| richards_super             | 60.3 ms                                                  | 59.6 ms: 1.01x faster                                                   |
| regex_effbot               | 4.87 ms                                                  | 4.81 ms: 1.01x faster                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 5.83 sec: 1.01x faster                                                  |
| mdp                        | 3.36 sec                                                 | 3.33 sec: 1.01x faster                                                  |
| richards                   | 53.5 ms                                                  | 53.1 ms: 1.01x faster                                                   |
| xml_etree_iterparse        | 147 ms                                                   | 146 ms: 1.01x faster                                                    |
| regex_dna                  | 246 ms                                                   | 245 ms: 1.01x faster                                                    |
| pickle_pure_python         | 359 us                                                   | 357 us: 1.01x faster                                                    |
| html5lib                   | 64.3 ms                                                  | 64.7 ms: 1.01x slower                                                   |
| tomli_loads                | 2.53 sec                                                 | 2.55 sec: 1.01x slower                                                  |
| raytrace                   | 298 ms                                                   | 300 ms: 1.01x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.13 sec: 1.02x slower                                                  |
| json_loads                 | 31.4 us                                                  | 32.2 us: 1.03x slower                                                   |
| asyncio_tcp                | 568 ms                                                   | 583 ms: 1.03x slower                                                    |
| telco                      | 9.73 ms                                                  | 10.0 ms: 1.03x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                  |
| fannkuch                   | 452 ms                                                   | 467 ms: 1.03x slower                                                    |
| pyflate                    | 556 ms                                                   | 579 ms: 1.04x slower                                                    |
| docutils                   | 2.91 sec                                                 | 3.07 sec: 1.06x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| create_gc_cycles           | 2.12 ms                                                  | 2.31 ms: 1.09x slower                                                   |
| gc_traversal               | 4.53 ms                                                  | 4.98 ms: 1.10x slower                                                   |
| go                         | 163 ms                                                   | 190 ms: 1.17x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (27): tornado_http, logging_format, json_dumps, genshi_text, scimark_sor, unpickle_pure_python, nqueens, sympy_str, django_template, chaos, typing_runtime_protocols, crypto_pyaes, sqlglot_normalize, json, comprehensions, sympy_expand, pidigits, spectral_norm, xml_etree_generate, python_startup_no_site, xml_etree_parse, asyncio_websockets, coroutines, sqlglot_parse, deltablue, mako, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x