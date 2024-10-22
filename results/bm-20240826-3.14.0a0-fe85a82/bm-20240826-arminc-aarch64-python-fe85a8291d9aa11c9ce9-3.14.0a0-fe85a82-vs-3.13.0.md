# Results vs. 3.13.0

- fork: python
- ref: fe85a8291d9aa11c9ce9
- machine: linux-aarch64
- commit hash: fe85a82
- commit date: 2024-08-26
- overall geometric mean: 1.01x faster
- HPT reliability: 99.20%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 296 ms: 1.03x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.09 sec: 1.06x slower                                                  |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 546 ms: 1.19x faster                                                    |
| async_tree_none           | 493 ms                                                   | 420 ms: 1.17x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 551 ms: 1.13x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 416 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 723 ms: 1.06x faster                                                    |
| async_generators          | 496 ms                                                   | 488 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                  |
| async_tree_io             | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| async_tree_io_tg          | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| Geometric mean            | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (4): asyncio_tcp, async_tree_cpu_io_mixed_tg, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| float          | 94.4 ms                                                  | 91.6 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| regex_v8       | 31.5 ms                                                  | 31.1 ms: 1.02x faster                                                   |
| regex_dna      | 246 ms                                                   | 245 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps          | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| xml_etree_parse     | 188 ms                                                   | 190 ms: 1.01x slower                                                    |
| xml_etree_iterparse | 147 ms                                                   | 151 ms: 1.03x slower                                                    |
| json_loads          | 31.4 us                                                  | 32.5 us: 1.03x slower                                                   |
| tomli_loads         | 2.53 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| Geometric mean      | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (4): pickle_pure_python, unpickle_pure_python, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.1 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 38.0 us: 1.34x faster                                                   |
| deepcopy                  | 451 us                                                   | 338 us: 1.34x faster                                                    |
| async_tree_memoization_tg | 649 ms                                                   | 546 ms: 1.19x faster                                                    |
| async_tree_none           | 493 ms                                                   | 420 ms: 1.17x faster                                                    |
| deepcopy_reduce           | 4.07 us                                                  | 3.52 us: 1.16x faster                                                   |
| async_tree_memoization    | 626 ms                                                   | 551 ms: 1.13x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 416 ms: 1.12x faster                                                    |
| generators                | 37.8 ms                                                  | 35.0 ms: 1.08x faster                                                   |
| pathlib                   | 22.4 ms                                                  | 20.8 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 723 ms: 1.06x faster                                                    |
| nbody                     | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| bench_thread_pool         | 1.28 ms                                                  | 1.23 ms: 1.04x faster                                                   |
| pycparser                 | 1.26 sec                                                 | 1.22 sec: 1.04x faster                                                  |
| scimark_lu                | 139 ms                                                   | 135 ms: 1.03x faster                                                    |
| 2to3                      | 306 ms                                                   | 296 ms: 1.03x faster                                                    |
| bench_mp_pool             | 7.30 ms                                                  | 7.08 ms: 1.03x faster                                                   |
| float                     | 94.4 ms                                                  | 91.6 ms: 1.03x faster                                                   |
| logging_silent            | 135 ns                                                   | 132 ns: 1.03x faster                                                    |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.43 ms: 1.02x faster                                                   |
| thrift                    | 946 us                                                   | 927 us: 1.02x faster                                                    |
| json_dumps                | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| scimark_fft               | 447 ms                                                   | 440 ms: 1.02x faster                                                    |
| async_generators          | 496 ms                                                   | 488 ms: 1.02x faster                                                    |
| regex_compile             | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| regex_v8                  | 31.5 ms                                                  | 31.1 ms: 1.02x faster                                                   |
| python_startup            | 13.3 ms                                                  | 13.1 ms: 1.01x faster                                                   |
| sqlglot_normalize         | 128 ms                                                   | 127 ms: 1.01x faster                                                    |
| logging_simple            | 7.04 us                                                  | 6.95 us: 1.01x faster                                                   |
| richards_super            | 60.3 ms                                                  | 59.6 ms: 1.01x faster                                                   |
| scimark_monte_carlo       | 83.8 ms                                                  | 82.8 ms: 1.01x faster                                                   |
| pprint_safe_repr          | 926 ms                                                   | 918 ms: 1.01x faster                                                    |
| mdp                       | 3.36 sec                                                 | 3.34 sec: 1.01x faster                                                  |
| pprint_pformat            | 1.90 sec                                                 | 1.89 sec: 1.01x faster                                                  |
| bpe_tokeniser             | 5.90 sec                                                 | 5.87 sec: 1.00x faster                                                  |
| regex_dna                 | 246 ms                                                   | 245 ms: 1.00x faster                                                    |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                  |
| sympy_expand              | 455 ms                                                   | 460 ms: 1.01x slower                                                    |
| pyflate                   | 556 ms                                                   | 563 ms: 1.01x slower                                                    |
| xml_etree_parse           | 188 ms                                                   | 190 ms: 1.01x slower                                                    |
| typing_runtime_protocols  | 192 us                                                   | 195 us: 1.01x slower                                                    |
| raytrace                  | 298 ms                                                   | 302 ms: 1.02x slower                                                    |
| json                      | 5.61 ms                                                  | 5.71 ms: 1.02x slower                                                   |
| fannkuch                  | 452 ms                                                   | 464 ms: 1.03x slower                                                    |
| xml_etree_iterparse       | 147 ms                                                   | 151 ms: 1.03x slower                                                    |
| sqlglot_parse             | 1.38 ms                                                  | 1.43 ms: 1.03x slower                                                   |
| json_loads                | 31.4 us                                                  | 32.5 us: 1.03x slower                                                   |
| async_tree_io             | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| tomli_loads               | 2.53 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| docutils                  | 2.91 sec                                                 | 3.09 sec: 1.06x slower                                                  |
| gc_traversal              | 4.53 ms                                                  | 4.83 ms: 1.06x slower                                                   |
| create_gc_cycles          | 2.12 ms                                                  | 2.28 ms: 1.08x slower                                                   |
| async_tree_io_tg          | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| go                        | 163 ms                                                   | 193 ms: 1.19x slower                                                    |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (36): tornado_http, logging_format, asyncio_tcp, meteor_contest, sympy_sum, async_tree_cpu_io_mixed_tg, sympy_integrate, scimark_sor, coverage, telco, pickle_pure_python, regex_effbot, sympy_str, genshi_text, unpickle_pure_python, richards, genshi_xml, chaos, python_startup_no_site, sqlglot_optimize, xml_etree_generate, xml_etree_process, mako, spectral_norm, hexiom, sqlglot_transpile, crypto_pyaes, asyncio_websockets, pidigits, nqueens, django_template, coroutines, comprehensions, deltablue, html5lib, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.20% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x