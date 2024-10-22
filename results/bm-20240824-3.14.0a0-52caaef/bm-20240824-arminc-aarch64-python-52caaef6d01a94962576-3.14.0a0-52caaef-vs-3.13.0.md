# Results vs. 3.13.0

- fork: python
- ref: 52caaef6d01a94962576
- machine: linux-aarch64
- commit hash: 52caaef
- commit date: 2024-08-24
- overall geometric mean: 1.02x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 297 ms: 1.03x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.09 sec: 1.06x slower                                                  |
| html5lib       | 64.3 ms                                                  | 67.8 ms: 1.05x slower                                                   |
| tornado_http   | 131 ms                                                   | 125 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 550 ms: 1.18x faster                                                    |
| async_tree_none           | 493 ms                                                   | 423 ms: 1.17x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 557 ms: 1.12x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 419 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 727 ms: 1.05x faster                                                    |
| async_generators          | 496 ms                                                   | 485 ms: 1.02x faster                                                    |
| asyncio_websockets        | 656 ms                                                   | 660 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.21 sec: 1.02x slower                                                  |
| async_tree_io             | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| async_tree_io_tg          | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                                  |
| Geometric mean            | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (3): asyncio_tcp, async_tree_cpu_io_mixed_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 108 ms: 1.06x faster                                                    |
| float          | 94.4 ms                                                  | 91.2 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                   | 123 ms: 1.04x faster                                                    |
| regex_v8       | 31.5 ms                                                  | 30.5 ms: 1.03x faster                                                   |
| regex_dna      | 246 ms                                                   | 252 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|--------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps         | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| pickle_pure_python | 359 us                                                   | 356 us: 1.01x faster                                                    |
| tomli_loads        | 2.53 sec                                                 | 2.62 sec: 1.04x slower                                                  |
| json_loads         | 31.4 us                                                  | 32.6 us: 1.04x slower                                                   |
| Geometric mean     | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_process, unpickle_pure_python, xml_etree_generate, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, genshi_text, mako, django_template

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                  | 451 us                                                   | 336 us: 1.34x faster                                                    |
| deepcopy_memo             | 51.0 us                                                  | 38.0 us: 1.34x faster                                                   |
| async_tree_memoization_tg | 649 ms                                                   | 550 ms: 1.18x faster                                                    |
| async_tree_none           | 493 ms                                                   | 423 ms: 1.17x faster                                                    |
| deepcopy_reduce           | 4.07 us                                                  | 3.50 us: 1.16x faster                                                   |
| async_tree_memoization    | 626 ms                                                   | 557 ms: 1.12x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 419 ms: 1.12x faster                                                    |
| generators                | 37.8 ms                                                  | 35.0 ms: 1.08x faster                                                   |
| nbody                     | 114 ms                                                   | 108 ms: 1.06x faster                                                    |
| pathlib                   | 22.4 ms                                                  | 21.2 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 727 ms: 1.05x faster                                                    |
| tornado_http              | 131 ms                                                   | 125 ms: 1.05x faster                                                    |
| bench_mp_pool             | 7.30 ms                                                  | 6.99 ms: 1.04x faster                                                   |
| regex_compile             | 128 ms                                                   | 123 ms: 1.04x faster                                                    |
| scimark_lu                | 139 ms                                                   | 134 ms: 1.04x faster                                                    |
| pycparser                 | 1.26 sec                                                 | 1.22 sec: 1.04x faster                                                  |
| bench_thread_pool         | 1.28 ms                                                  | 1.23 ms: 1.04x faster                                                   |
| float                     | 94.4 ms                                                  | 91.2 ms: 1.03x faster                                                   |
| regex_v8                  | 31.5 ms                                                  | 30.5 ms: 1.03x faster                                                   |
| 2to3                      | 306 ms                                                   | 297 ms: 1.03x faster                                                    |
| scimark_monte_carlo       | 83.8 ms                                                  | 81.5 ms: 1.03x faster                                                   |
| logging_format            | 7.83 us                                                  | 7.61 us: 1.03x faster                                                   |
| logging_silent            | 135 ns                                                   | 132 ns: 1.03x faster                                                    |
| thrift                    | 946 us                                                   | 921 us: 1.03x faster                                                    |
| richards_super            | 60.3 ms                                                  | 59.0 ms: 1.02x faster                                                   |
| async_generators          | 496 ms                                                   | 485 ms: 1.02x faster                                                    |
| json_dumps                | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| logging_simple            | 7.04 us                                                  | 6.90 us: 1.02x faster                                                   |
| meteor_contest            | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| python_startup            | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| pprint_safe_repr          | 926 ms                                                   | 909 ms: 1.02x faster                                                    |
| sympy_integrate           | 21.0 ms                                                  | 20.6 ms: 1.02x faster                                                   |
| pprint_pformat            | 1.90 sec                                                 | 1.87 sec: 1.02x faster                                                  |
| hexiom                    | 7.13 ms                                                  | 7.02 ms: 1.02x faster                                                   |
| sympy_sum                 | 143 ms                                                   | 141 ms: 1.01x faster                                                    |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.49 ms: 1.01x faster                                                   |
| scimark_fft               | 447 ms                                                   | 443 ms: 1.01x faster                                                    |
| pickle_pure_python        | 359 us                                                   | 356 us: 1.01x faster                                                    |
| bpe_tokeniser             | 5.90 sec                                                 | 5.84 sec: 1.01x faster                                                  |
| asyncio_websockets        | 656 ms                                                   | 660 ms: 1.01x slower                                                    |
| sympy_expand              | 455 ms                                                   | 459 ms: 1.01x slower                                                    |
| fannkuch                  | 452 ms                                                   | 458 ms: 1.01x slower                                                    |
| comprehensions            | 20.4 us                                                  | 20.7 us: 1.02x slower                                                   |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.21 sec: 1.02x slower                                                  |
| raytrace                  | 298 ms                                                   | 303 ms: 1.02x slower                                                    |
| regex_dna                 | 246 ms                                                   | 252 ms: 1.02x slower                                                    |
| sqlglot_parse             | 1.38 ms                                                  | 1.42 ms: 1.03x slower                                                   |
| async_tree_io             | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| tomli_loads               | 2.53 sec                                                 | 2.62 sec: 1.04x slower                                                  |
| json_loads                | 31.4 us                                                  | 32.6 us: 1.04x slower                                                   |
| html5lib                  | 64.3 ms                                                  | 67.8 ms: 1.05x slower                                                   |
| docutils                  | 2.91 sec                                                 | 3.09 sec: 1.06x slower                                                  |
| async_tree_io_tg          | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                                  |
| gc_traversal              | 4.53 ms                                                  | 4.91 ms: 1.08x slower                                                   |
| create_gc_cycles          | 2.12 ms                                                  | 2.31 ms: 1.09x slower                                                   |
| go                        | 163 ms                                                   | 193 ms: 1.19x slower                                                    |
| Geometric mean            | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (33): xml_etree_process, sqlglot_transpile, richards, scimark_sor, unpickle_pure_python, crypto_pyaes, asyncio_tcp, chaos, genshi_xml, genshi_text, async_tree_cpu_io_mixed_tg, spectral_norm, xml_etree_generate, nqueens, pyflate, sqlglot_optimize, mako, typing_runtime_protocols, coverage, pidigits, python_startup_no_site, mdp, regex_effbot, sqlglot_normalize, django_template, telco, xml_etree_parse, coroutines, sympy_str, json, deltablue, xml_etree_iterparse, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x