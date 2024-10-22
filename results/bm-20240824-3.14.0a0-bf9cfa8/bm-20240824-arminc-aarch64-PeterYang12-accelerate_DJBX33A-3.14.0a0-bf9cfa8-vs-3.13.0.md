# Results vs. 3.13.0

- fork: PeterYang12
- ref: accelerate_DJBX33A
- machine: linux-aarch64
- commit hash: bf9cfa8
- commit date: 2024-08-24
- overall geometric mean: 1.01x faster
- HPT reliability: 99.55%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 294 ms: 1.04x faster                                                       |
| docutils       | 2.91 sec                                                 | 3.09 sec: 1.06x slower                                                     |
| html5lib       | 64.3 ms                                                  | 65.9 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                    | 1.00x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|---------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 551 ms: 1.18x faster                                                       |
| async_tree_none           | 493 ms                                                   | 433 ms: 1.14x faster                                                       |
| async_tree_none_tg        | 467 ms                                                   | 421 ms: 1.11x faster                                                       |
| async_tree_memoization    | 626 ms                                                   | 563 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 733 ms: 1.04x faster                                                       |
| async_generators          | 496 ms                                                   | 483 ms: 1.03x faster                                                       |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.24 sec: 1.03x slower                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                     |
| async_tree_io_tg          | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                     |
| Geometric mean            | (ref)                                                    | 1.03x faster                                                               |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, asyncio_websockets, asyncio_tcp, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.04x faster                                                       |
| float          | 94.4 ms                                                  | 91.2 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                    | 1.03x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.0 ms: 1.05x faster                                                      |
| regex_dna      | 246 ms                                                   | 252 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                    | 1.01x faster                                                               |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|--------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps         | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                      |
| xml_etree_parse    | 188 ms                                                   | 189 ms: 1.01x slower                                                       |
| pickle_pure_python | 359 us                                                   | 365 us: 1.02x slower                                                       |
| tomli_loads        | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                     |
| json_loads         | 31.4 us                                                  | 32.8 us: 1.04x slower                                                      |
| Geometric mean     | (ref)                                                    | 1.00x slower                                                               |

Benchmark hidden because not significant (4): xml_etree_generate, unpickle_pure_python, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                    | 1.01x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text    | 27.7 ms                                                  | 27.3 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                    | 1.01x faster                                                               |

Benchmark hidden because not significant (3): django_template, genshi_xml, mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|---------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy                  | 451 us                                                   | 335 us: 1.35x faster                                                       |
| deepcopy_memo             | 51.0 us                                                  | 38.2 us: 1.34x faster                                                      |
| async_tree_memoization_tg | 649 ms                                                   | 551 ms: 1.18x faster                                                       |
| deepcopy_reduce           | 4.07 us                                                  | 3.57 us: 1.14x faster                                                      |
| async_tree_none           | 493 ms                                                   | 433 ms: 1.14x faster                                                       |
| async_tree_none_tg        | 467 ms                                                   | 421 ms: 1.11x faster                                                       |
| async_tree_memoization    | 626 ms                                                   | 563 ms: 1.11x faster                                                       |
| generators                | 37.8 ms                                                  | 34.9 ms: 1.08x faster                                                      |
| pathlib                   | 22.4 ms                                                  | 21.2 ms: 1.06x faster                                                      |
| regex_v8                  | 31.5 ms                                                  | 30.0 ms: 1.05x faster                                                      |
| bench_mp_pool             | 7.30 ms                                                  | 6.96 ms: 1.05x faster                                                      |
| nbody                     | 114 ms                                                   | 109 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 733 ms: 1.04x faster                                                       |
| 2to3                      | 306 ms                                                   | 294 ms: 1.04x faster                                                       |
| logging_silent            | 135 ns                                                   | 131 ns: 1.04x faster                                                       |
| float                     | 94.4 ms                                                  | 91.2 ms: 1.03x faster                                                      |
| bench_thread_pool         | 1.28 ms                                                  | 1.24 ms: 1.03x faster                                                      |
| meteor_contest            | 113 ms                                                   | 110 ms: 1.03x faster                                                       |
| async_generators          | 496 ms                                                   | 483 ms: 1.03x faster                                                       |
| scimark_lu                | 139 ms                                                   | 136 ms: 1.03x faster                                                       |
| pycparser                 | 1.26 sec                                                 | 1.23 sec: 1.03x faster                                                     |
| python_startup            | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                      |
| hexiom                    | 7.13 ms                                                  | 6.97 ms: 1.02x faster                                                      |
| scimark_monte_carlo       | 83.8 ms                                                  | 82.0 ms: 1.02x faster                                                      |
| scimark_sor               | 159 ms                                                   | 156 ms: 1.02x faster                                                       |
| sqlglot_normalize         | 128 ms                                                   | 126 ms: 1.02x faster                                                       |
| logging_format            | 7.83 us                                                  | 7.68 us: 1.02x faster                                                      |
| richards_super            | 60.3 ms                                                  | 59.2 ms: 1.02x faster                                                      |
| json_dumps                | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.48 ms: 1.02x faster                                                      |
| genshi_text               | 27.7 ms                                                  | 27.3 ms: 1.01x faster                                                      |
| richards                  | 53.5 ms                                                  | 52.8 ms: 1.01x faster                                                      |
| bpe_tokeniser             | 5.90 sec                                                 | 5.83 sec: 1.01x faster                                                     |
| pprint_pformat            | 1.90 sec                                                 | 1.88 sec: 1.01x faster                                                     |
| logging_simple            | 7.04 us                                                  | 6.98 us: 1.01x faster                                                      |
| xml_etree_parse           | 188 ms                                                   | 189 ms: 1.01x slower                                                       |
| sympy_expand              | 455 ms                                                   | 458 ms: 1.01x slower                                                       |
| sqlglot_parse             | 1.38 ms                                                  | 1.40 ms: 1.01x slower                                                      |
| nqueens                   | 98.7 ms                                                  | 99.9 ms: 1.01x slower                                                      |
| comprehensions            | 20.4 us                                                  | 20.7 us: 1.01x slower                                                      |
| raytrace                  | 298 ms                                                   | 303 ms: 1.02x slower                                                       |
| json                      | 5.61 ms                                                  | 5.70 ms: 1.02x slower                                                      |
| pickle_pure_python        | 359 us                                                   | 365 us: 1.02x slower                                                       |
| fannkuch                  | 452 ms                                                   | 460 ms: 1.02x slower                                                       |
| deltablue                 | 3.85 ms                                                  | 3.93 ms: 1.02x slower                                                      |
| regex_dna                 | 246 ms                                                   | 252 ms: 1.02x slower                                                       |
| telco                     | 9.73 ms                                                  | 9.97 ms: 1.02x slower                                                      |
| html5lib                  | 64.3 ms                                                  | 65.9 ms: 1.03x slower                                                      |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.24 sec: 1.03x slower                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                     |
| tomli_loads               | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                     |
| json_loads                | 31.4 us                                                  | 32.8 us: 1.04x slower                                                      |
| docutils                  | 2.91 sec                                                 | 3.09 sec: 1.06x slower                                                     |
| create_gc_cycles          | 2.12 ms                                                  | 2.26 ms: 1.07x slower                                                      |
| async_tree_io_tg          | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                     |
| gc_traversal              | 4.53 ms                                                  | 4.98 ms: 1.10x slower                                                      |
| go                        | 163 ms                                                   | 191 ms: 1.18x slower                                                       |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                               |

Benchmark hidden because not significant (32): tornado_http, xml_etree_generate, sympy_sum, sympy_integrate, django_template, sqlglot_transpile, unpickle_pure_python, async_tree_cpu_io_mixed_tg, regex_compile, sqlglot_optimize, xml_etree_process, thrift, mdp, scimark_fft, xml_etree_iterparse, spectral_norm, genshi_xml, crypto_pyaes, python_startup_no_site, chaos, pidigits, pprint_safe_repr, asyncio_websockets, mako, regex_effbot, sympy_str, pyflate, coverage, typing_runtime_protocols, asyncio_tcp, coroutines, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.55% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x