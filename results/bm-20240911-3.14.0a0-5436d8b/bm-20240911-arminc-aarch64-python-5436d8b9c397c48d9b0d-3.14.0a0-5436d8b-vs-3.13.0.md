# Results vs. 3.13.0

- fork: python
- ref: 5436d8b9c397c48d9b0d
- machine: linux-aarch64
- commit hash: 5436d8b
- commit date: 2024-09-11
- overall geometric mean: 1.02x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 295 ms: 1.04x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.02 sec: 1.04x slower                                                  |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 553 ms: 1.17x faster                                                    |
| async_tree_none           | 493 ms                                                   | 425 ms: 1.16x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 560 ms: 1.12x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 422 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 725 ms: 1.05x faster                                                    |
| asyncio_tcp               | 568 ms                                                   | 551 ms: 1.03x faster                                                    |
| coroutines                | 28.2 ms                                                  | 28.4 ms: 1.00x slower                                                   |
| asyncio_websockets        | 656 ms                                                   | 663 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.21 sec: 1.02x slower                                                  |
| async_tree_io             | 1.11 sec                                                 | 1.17 sec: 1.06x slower                                                  |
| async_tree_io_tg          | 1.09 sec                                                 | 1.18 sec: 1.09x slower                                                  |
| Geometric mean            | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): async_generators, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| float          | 94.4 ms                                                  | 91.8 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| regex_v8       | 31.5 ms                                                  | 31.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|--------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_list      | 6.65 us                                                  | 6.38 us: 1.04x faster                                                   |
| unpickle           | 20.2 us                                                  | 19.4 us: 1.04x faster                                                   |
| pickle_list        | 5.34 us                                                  | 5.23 us: 1.02x faster                                                   |
| xml_etree_parse    | 188 ms                                                   | 185 ms: 1.01x faster                                                    |
| pickle             | 13.5 us                                                  | 13.7 us: 1.02x slower                                                   |
| pickle_pure_python | 359 us                                                   | 368 us: 1.02x slower                                                    |
| tomli_loads        | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| Geometric mean     | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (7): xml_etree_process, pickle_dict, xml_etree_generate, unpickle_pure_python, xml_etree_iterparse, json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| python_startup_no_site | 8.75 ms                                                  | 8.58 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.02x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                  | 41.4 ms: 1.02x faster                                                   |
| mako            | 13.3 ms                                                  | 13.3 ms: 1.00x faster                                                   |
| Geometric mean  | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                  | 451 us                                                   | 331 us: 1.36x faster                                                    |
| deepcopy_memo             | 51.0 us                                                  | 37.6 us: 1.36x faster                                                   |
| go                        | 163 ms                                                   | 138 ms: 1.18x faster                                                    |
| async_tree_memoization_tg | 649 ms                                                   | 553 ms: 1.17x faster                                                    |
| async_tree_none           | 493 ms                                                   | 425 ms: 1.16x faster                                                    |
| deepcopy_reduce           | 4.07 us                                                  | 3.54 us: 1.15x faster                                                   |
| async_tree_memoization    | 626 ms                                                   | 560 ms: 1.12x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 422 ms: 1.11x faster                                                    |
| generators                | 37.8 ms                                                  | 34.7 ms: 1.09x faster                                                   |
| pathlib                   | 22.4 ms                                                  | 20.9 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 725 ms: 1.05x faster                                                    |
| unpickle_list             | 6.65 us                                                  | 6.38 us: 1.04x faster                                                   |
| pycparser                 | 1.26 sec                                                 | 1.21 sec: 1.04x faster                                                  |
| unpickle                  | 20.2 us                                                  | 19.4 us: 1.04x faster                                                   |
| bench_thread_pool         | 1.28 ms                                                  | 1.23 ms: 1.04x faster                                                   |
| nbody                     | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| bench_mp_pool             | 7.30 ms                                                  | 7.03 ms: 1.04x faster                                                   |
| 2to3                      | 306 ms                                                   | 295 ms: 1.04x faster                                                    |
| asyncio_tcp               | 568 ms                                                   | 551 ms: 1.03x faster                                                    |
| float                     | 94.4 ms                                                  | 91.8 ms: 1.03x faster                                                   |
| scimark_lu                | 139 ms                                                   | 136 ms: 1.02x faster                                                    |
| python_startup            | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| thrift                    | 946 us                                                   | 924 us: 1.02x faster                                                    |
| logging_silent            | 135 ns                                                   | 132 ns: 1.02x faster                                                    |
| django_template           | 42.3 ms                                                  | 41.4 ms: 1.02x faster                                                   |
| scimark_monte_carlo       | 83.8 ms                                                  | 82.1 ms: 1.02x faster                                                   |
| pickle_list               | 5.34 us                                                  | 5.23 us: 1.02x faster                                                   |
| regex_compile             | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| python_startup_no_site    | 8.75 ms                                                  | 8.58 ms: 1.02x faster                                                   |
| sympy_integrate           | 21.0 ms                                                  | 20.6 ms: 1.02x faster                                                   |
| pprint_safe_repr          | 926 ms                                                   | 911 ms: 1.02x faster                                                    |
| regex_v8                  | 31.5 ms                                                  | 31.0 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.49 ms: 1.01x faster                                                   |
| xml_etree_parse           | 188 ms                                                   | 185 ms: 1.01x faster                                                    |
| scimark_sor               | 159 ms                                                   | 157 ms: 1.01x faster                                                    |
| richards                  | 53.5 ms                                                  | 52.9 ms: 1.01x faster                                                   |
| pprint_pformat            | 1.90 sec                                                 | 1.88 sec: 1.01x faster                                                  |
| bpe_tokeniser             | 5.90 sec                                                 | 5.85 sec: 1.01x faster                                                  |
| mdp                       | 3.36 sec                                                 | 3.34 sec: 1.01x faster                                                  |
| mako                      | 13.3 ms                                                  | 13.3 ms: 1.00x faster                                                   |
| coroutines                | 28.2 ms                                                  | 28.4 ms: 1.00x slower                                                   |
| asyncio_websockets        | 656 ms                                                   | 663 ms: 1.01x slower                                                    |
| spectral_norm             | 141 ms                                                   | 143 ms: 1.01x slower                                                    |
| raytrace                  | 298 ms                                                   | 302 ms: 1.01x slower                                                    |
| nqueens                   | 98.7 ms                                                  | 100 ms: 1.01x slower                                                    |
| sympy_expand              | 455 ms                                                   | 462 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.21 sec: 1.02x slower                                                  |
| pickle                    | 13.5 us                                                  | 13.7 us: 1.02x slower                                                   |
| fannkuch                  | 452 ms                                                   | 459 ms: 1.02x slower                                                    |
| sqlglot_parse             | 1.38 ms                                                  | 1.41 ms: 1.02x slower                                                   |
| sqlite_synth              | 3.84 us                                                  | 3.93 us: 1.02x slower                                                   |
| pickle_pure_python        | 359 us                                                   | 368 us: 1.02x slower                                                    |
| unpack_sequence           | 57.2 ns                                                  | 58.9 ns: 1.03x slower                                                   |
| docutils                  | 2.91 sec                                                 | 3.02 sec: 1.04x slower                                                  |
| tomli_loads               | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| telco                     | 9.73 ms                                                  | 10.2 ms: 1.05x slower                                                   |
| scimark_fft               | 447 ms                                                   | 471 ms: 1.05x slower                                                    |
| async_tree_io             | 1.11 sec                                                 | 1.17 sec: 1.06x slower                                                  |
| create_gc_cycles          | 2.12 ms                                                  | 2.28 ms: 1.07x slower                                                   |
| async_tree_io_tg          | 1.09 sec                                                 | 1.18 sec: 1.09x slower                                                  |
| gc_traversal              | 4.53 ms                                                  | 5.12 ms: 1.13x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (35): tornado_http, logging_format, async_generators, genshi_text, sqlglot_normalize, xml_etree_process, richards_super, crypto_pyaes, meteor_contest, json, sympy_sum, async_tree_cpu_io_mixed_tg, coverage, pickle_dict, comprehensions, hexiom, xml_etree_generate, sqlglot_transpile, chaos, unpickle_pure_python, xml_etree_iterparse, sympy_str, sqlglot_optimize, pidigits, typing_runtime_protocols, pyflate, logging_simple, regex_effbot, regex_dna, json_loads, json_dumps, deltablue, genshi_xml, html5lib, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240911-3.14.0a0-5436d8b/bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json: dulwich_log

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x