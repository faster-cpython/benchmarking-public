# Results vs. 3.13.0

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-aarch64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.01x faster
- HPT reliability: 68.16%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 293 ms: 1.04x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.09 sec: 1.06x slower                                                  |
| html5lib       | 64.3 ms                                                  | 65.0 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 541 ms: 1.20x faster                                                    |
| async_tree_none           | 493 ms                                                   | 426 ms: 1.16x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 423 ms: 1.10x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 575 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 733 ms: 1.04x faster                                                    |
| asyncio_websockets        | 656 ms                                                   | 661 ms: 1.01x slower                                                    |
| coroutines                | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                                   |
| asyncio_tcp               | 568 ms                                                   | 582 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.24 sec: 1.03x slower                                                  |
| async_tree_io_tg          | 1.09 sec                                                 | 1.14 sec: 1.05x slower                                                  |
| async_tree_io             | 1.11 sec                                                 | 1.20 sec: 1.09x slower                                                  |
| Geometric mean            | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): async_generators, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| float          | 94.4 ms                                                  | 91.1 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                   | 127 ms: 1.01x faster                                                    |
| regex_v8       | 31.5 ms                                                  | 31.2 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps          | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| pickle_pure_python  | 359 us                                                   | 355 us: 1.01x faster                                                    |
| xml_etree_iterparse | 147 ms                                                   | 148 ms: 1.01x slower                                                    |
| xml_etree_parse     | 188 ms                                                   | 191 ms: 1.02x slower                                                    |
| json_loads          | 31.4 us                                                  | 32.9 us: 1.05x slower                                                   |
| tomli_loads         | 2.53 sec                                                 | 2.64 sec: 1.05x slower                                                  |
| Geometric mean      | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_generate, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.3 ms                                                  | 13.4 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 37.9 us: 1.35x faster                                                   |
| deepcopy                  | 451 us                                                   | 338 us: 1.34x faster                                                    |
| async_tree_memoization_tg | 649 ms                                                   | 541 ms: 1.20x faster                                                    |
| async_tree_none           | 493 ms                                                   | 426 ms: 1.16x faster                                                    |
| deepcopy_reduce           | 4.07 us                                                  | 3.53 us: 1.15x faster                                                   |
| async_tree_none_tg        | 467 ms                                                   | 423 ms: 1.10x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 575 ms: 1.09x faster                                                    |
| generators                | 37.8 ms                                                  | 34.8 ms: 1.09x faster                                                   |
| pathlib                   | 22.4 ms                                                  | 21.2 ms: 1.06x faster                                                   |
| 2to3                      | 306 ms                                                   | 293 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 733 ms: 1.04x faster                                                    |
| nbody                     | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| float                     | 94.4 ms                                                  | 91.1 ms: 1.04x faster                                                   |
| bench_thread_pool         | 1.28 ms                                                  | 1.23 ms: 1.03x faster                                                   |
| scimark_lu                | 139 ms                                                   | 135 ms: 1.03x faster                                                    |
| pycparser                 | 1.26 sec                                                 | 1.22 sec: 1.03x faster                                                  |
| thrift                    | 946 us                                                   | 918 us: 1.03x faster                                                    |
| bench_mp_pool             | 7.30 ms                                                  | 7.11 ms: 1.03x faster                                                   |
| scimark_monte_carlo       | 83.8 ms                                                  | 81.9 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.44 ms: 1.02x faster                                                   |
| json_dumps                | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| python_startup            | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| logging_silent            | 135 ns                                                   | 133 ns: 1.02x faster                                                    |
| scimark_sor               | 159 ms                                                   | 157 ms: 1.01x faster                                                    |
| regex_compile             | 128 ms                                                   | 127 ms: 1.01x faster                                                    |
| crypto_pyaes              | 82.7 ms                                                  | 81.7 ms: 1.01x faster                                                   |
| pickle_pure_python        | 359 us                                                   | 355 us: 1.01x faster                                                    |
| regex_v8                  | 31.5 ms                                                  | 31.2 ms: 1.01x faster                                                   |
| bpe_tokeniser             | 5.90 sec                                                 | 5.87 sec: 1.00x faster                                                  |
| mako                      | 13.3 ms                                                  | 13.4 ms: 1.00x slower                                                   |
| xml_etree_iterparse       | 147 ms                                                   | 148 ms: 1.01x slower                                                    |
| asyncio_websockets        | 656 ms                                                   | 661 ms: 1.01x slower                                                    |
| pprint_pformat            | 1.90 sec                                                 | 1.91 sec: 1.01x slower                                                  |
| html5lib                  | 64.3 ms                                                  | 65.0 ms: 1.01x slower                                                   |
| sympy_str                 | 264 ms                                                   | 267 ms: 1.01x slower                                                    |
| raytrace                  | 298 ms                                                   | 302 ms: 1.01x slower                                                    |
| logging_simple            | 7.04 us                                                  | 7.13 us: 1.01x slower                                                   |
| typing_runtime_protocols  | 192 us                                                   | 195 us: 1.01x slower                                                    |
| coroutines                | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                                   |
| xml_etree_parse           | 188 ms                                                   | 191 ms: 1.02x slower                                                    |
| sympy_expand              | 455 ms                                                   | 463 ms: 1.02x slower                                                    |
| fannkuch                  | 452 ms                                                   | 462 ms: 1.02x slower                                                    |
| asyncio_tcp               | 568 ms                                                   | 582 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.24 sec: 1.03x slower                                                  |
| telco                     | 9.73 ms                                                  | 10.0 ms: 1.03x slower                                                   |
| json                      | 5.61 ms                                                  | 5.79 ms: 1.03x slower                                                   |
| json_loads                | 31.4 us                                                  | 32.9 us: 1.05x slower                                                   |
| tomli_loads               | 2.53 sec                                                 | 2.64 sec: 1.05x slower                                                  |
| async_tree_io_tg          | 1.09 sec                                                 | 1.14 sec: 1.05x slower                                                  |
| sqlglot_parse             | 1.38 ms                                                  | 1.45 ms: 1.05x slower                                                   |
| docutils                  | 2.91 sec                                                 | 3.09 sec: 1.06x slower                                                  |
| pyflate                   | 556 ms                                                   | 593 ms: 1.07x slower                                                    |
| create_gc_cycles          | 2.12 ms                                                  | 2.29 ms: 1.08x slower                                                   |
| async_tree_io             | 1.11 sec                                                 | 1.20 sec: 1.09x slower                                                  |
| gc_traversal              | 4.53 ms                                                  | 4.96 ms: 1.09x slower                                                   |
| go                        | 163 ms                                                   | 191 ms: 1.18x slower                                                    |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (33): tornado_http, meteor_contest, sqlglot_normalize, sympy_sum, xml_etree_generate, sympy_integrate, scimark_fft, async_generators, async_tree_cpu_io_mixed_tg, logging_format, unpickle_pure_python, hexiom, regex_effbot, chaos, django_template, pprint_safe_repr, xml_etree_process, coverage, richards_super, mdp, nqueens, spectral_norm, pidigits, sqlglot_transpile, genshi_text, regex_dna, genshi_xml, python_startup_no_site, richards, comprehensions, sqlglot_optimize, deltablue, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 68.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x