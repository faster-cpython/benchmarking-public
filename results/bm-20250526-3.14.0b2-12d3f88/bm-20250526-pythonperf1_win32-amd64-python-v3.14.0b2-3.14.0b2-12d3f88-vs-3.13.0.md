# Results vs. 3.13.0

- fork: python
- ref: v3.14.0b2
- machine: windows-amd64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.217x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 224 ms: 1.11x faster                                                  |
| docutils       | 1.78 sec                                                        | 1.64 sec: 1.08x faster                                                |
| html5lib       | 47.5 ms                                                         | 38.4 ms: 1.24x faster                                                 |
| sphinx         | 719 ms                                                          | 648 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                           | 1.13x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 159 ms: 2.29x faster                                                  |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 330 ms: 1.47x faster                                                  |
| async_tree_none            | 245 ms                                                          | 175 ms: 1.40x faster                                                  |
| async_tree_memoization     | 297 ms                                                          | 212 ms: 1.40x faster                                                  |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 341 ms: 1.34x faster                                                  |
| async_tree_memoization_tg  | 282 ms                                                          | 212 ms: 1.33x faster                                                  |
| async_tree_io              | 526 ms                                                          | 408 ms: 1.29x faster                                                  |
| async_tree_none_tg         | 214 ms                                                          | 174 ms: 1.23x faster                                                  |
| async_tree_io_tg           | 494 ms                                                          | 409 ms: 1.21x faster                                                  |
| async_generators           | 270 ms                                                          | 230 ms: 1.17x faster                                                  |
| coroutines                 | 16.2 ms                                                         | 13.9 ms: 1.17x faster                                                 |
| Geometric mean             | (ref)                                                           | 1.37x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 149 ms: 1.35x faster                                                  |
| nbody          | 80.0 ms                                                         | 64.3 ms: 1.24x faster                                                 |
| float          | 54.6 ms                                                         | 44.5 ms: 1.23x faster                                                 |
| Geometric mean | (ref)                                                           | 1.27x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 82.5 ms: 1.22x faster                                                 |
| regex_effbot   | 1.80 ms                                                         | 1.53 ms: 1.18x faster                                                 |
| regex_v8       | 16.8 ms                                                         | 14.5 ms: 1.16x faster                                                 |
| regex_dna      | 114 ms                                                          | 119 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                           | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 14.7 us: 1.47x faster                                                 |
| xml_etree_parse      | 107 ms                                                          | 89.1 ms: 1.21x faster                                                 |
| unpickle_pure_python | 160 us                                                          | 135 us: 1.19x faster                                                  |
| tomli_loads          | 1.71 sec                                                        | 1.44 sec: 1.19x faster                                                |
| json_dumps           | 7.30 ms                                                         | 6.27 ms: 1.16x faster                                                 |
| xml_etree_process    | 44.2 ms                                                         | 39.7 ms: 1.11x faster                                                 |
| pickle_pure_python   | 231 us                                                          | 212 us: 1.09x faster                                                  |
| xml_etree_generate   | 61.4 ms                                                         | 56.9 ms: 1.08x faster                                                 |
| xml_etree_iterparse  | 62.6 ms                                                         | 65.0 ms: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                           | 1.16x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 26.2 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                           | 1.04x faster                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.4 ms: 1.46x faster                                                 |
| genshi_text     | 21.5 ms                                                         | 15.6 ms: 1.38x faster                                                 |
| django_template | 29.8 ms                                                         | 25.4 ms: 1.17x faster                                                 |
| mako            | 7.09 ms                                                         | 6.68 ms: 1.06x faster                                                 |
| Geometric mean  | (ref)                                                           | 1.26x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coverage                   | 324 ms                                                          | 51.2 ms: 6.32x faster                                                 |
| pathlib                    | 82.9 ms                                                         | 32.2 ms: 2.58x faster                                                 |
| asyncio_websockets         | 363 ms                                                          | 159 ms: 2.29x faster                                                  |
| mdp                        | 1.62 sec                                                        | 818 ms: 1.99x faster                                                  |
| deepcopy                   | 314 us                                                          | 171 us: 1.83x faster                                                  |
| deepcopy_reduce            | 2.92 us                                                         | 1.83 us: 1.59x faster                                                 |
| telco                      | 6.96 ms                                                         | 4.66 ms: 1.49x faster                                                 |
| json_loads                 | 21.6 us                                                         | 14.7 us: 1.47x faster                                                 |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 330 ms: 1.47x faster                                                  |
| genshi_xml                 | 50.1 ms                                                         | 34.4 ms: 1.46x faster                                                 |
| json                       | 4.27 ms                                                         | 2.98 ms: 1.43x faster                                                 |
| async_tree_none            | 245 ms                                                          | 175 ms: 1.40x faster                                                  |
| async_tree_memoization     | 297 ms                                                          | 212 ms: 1.40x faster                                                  |
| go                         | 109 ms                                                          | 78.6 ms: 1.38x faster                                                 |
| genshi_text                | 21.5 ms                                                         | 15.6 ms: 1.38x faster                                                 |
| deepcopy_memo              | 25.4 us                                                         | 18.5 us: 1.37x faster                                                 |
| pidigits                   | 201 ms                                                          | 149 ms: 1.35x faster                                                  |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 341 ms: 1.34x faster                                                  |
| async_tree_memoization_tg  | 282 ms                                                          | 212 ms: 1.33x faster                                                  |
| pprint_pformat             | 1.33 sec                                                        | 1.03 sec: 1.29x faster                                                |
| async_tree_io              | 526 ms                                                          | 408 ms: 1.29x faster                                                  |
| typing_runtime_protocols   | 138 us                                                          | 107 us: 1.28x faster                                                  |
| logging_format             | 8.72 us                                                         | 6.81 us: 1.28x faster                                                 |
| pprint_safe_repr           | 648 ms                                                          | 508 ms: 1.28x faster                                                  |
| sympy_expand               | 373 ms                                                          | 293 ms: 1.27x faster                                                  |
| chaos                      | 50.2 ms                                                         | 39.5 ms: 1.27x faster                                                 |
| logging_simple             | 7.99 us                                                         | 6.38 us: 1.25x faster                                                 |
| nbody                      | 80.0 ms                                                         | 64.3 ms: 1.24x faster                                                 |
| sympy_str                  | 212 ms                                                          | 171 ms: 1.24x faster                                                  |
| html5lib                   | 47.5 ms                                                         | 38.4 ms: 1.24x faster                                                 |
| async_tree_none_tg         | 214 ms                                                          | 174 ms: 1.23x faster                                                  |
| float                      | 54.6 ms                                                         | 44.5 ms: 1.23x faster                                                 |
| regex_compile              | 101 ms                                                          | 82.5 ms: 1.22x faster                                                 |
| sqlite_synth               | 1.95 us                                                         | 1.61 us: 1.22x faster                                                 |
| crypto_pyaes               | 56.9 ms                                                         | 46.9 ms: 1.21x faster                                                 |
| async_tree_io_tg           | 494 ms                                                          | 409 ms: 1.21x faster                                                  |
| xml_etree_parse            | 107 ms                                                          | 89.1 ms: 1.21x faster                                                 |
| sympy_integrate            | 15.0 ms                                                         | 12.5 ms: 1.20x faster                                                 |
| pycparser                  | 872 ms                                                          | 727 ms: 1.20x faster                                                  |
| unpickle_pure_python       | 160 us                                                          | 135 us: 1.19x faster                                                  |
| tomli_loads                | 1.71 sec                                                        | 1.44 sec: 1.19x faster                                                |
| sympy_sum                  | 106 ms                                                          | 89.1 ms: 1.19x faster                                                 |
| regex_effbot               | 1.80 ms                                                         | 1.53 ms: 1.18x faster                                                 |
| django_template            | 29.8 ms                                                         | 25.4 ms: 1.17x faster                                                 |
| async_generators           | 270 ms                                                          | 230 ms: 1.17x faster                                                  |
| coroutines                 | 16.2 ms                                                         | 13.9 ms: 1.17x faster                                                 |
| bpe_tokeniser              | 3.46 sec                                                        | 2.96 sec: 1.17x faster                                                |
| richards                   | 32.7 ms                                                         | 28.0 ms: 1.17x faster                                                 |
| json_dumps                 | 7.30 ms                                                         | 6.27 ms: 1.16x faster                                                 |
| dulwich_log                | 48.8 ms                                                         | 41.9 ms: 1.16x faster                                                 |
| regex_v8                   | 16.8 ms                                                         | 14.5 ms: 1.16x faster                                                 |
| fannkuch                   | 299 ms                                                          | 258 ms: 1.16x faster                                                  |
| scimark_fft                | 205 ms                                                          | 177 ms: 1.16x faster                                                  |
| spectral_norm              | 69.4 ms                                                         | 60.1 ms: 1.16x faster                                                 |
| scimark_monte_carlo        | 47.7 ms                                                         | 41.4 ms: 1.15x faster                                                 |
| richards_super             | 36.7 ms                                                         | 32.0 ms: 1.15x faster                                                 |
| pylint                     | 227 ms                                                          | 198 ms: 1.14x faster                                                  |
| nqueens                    | 72.1 ms                                                         | 63.8 ms: 1.13x faster                                                 |
| pyflate                    | 320 ms                                                          | 284 ms: 1.13x faster                                                  |
| scimark_sor                | 85.9 ms                                                         | 76.7 ms: 1.12x faster                                                 |
| 2to3                       | 250 ms                                                          | 224 ms: 1.11x faster                                                  |
| xml_etree_process          | 44.2 ms                                                         | 39.7 ms: 1.11x faster                                                 |
| sphinx                     | 719 ms                                                          | 648 ms: 1.11x faster                                                  |
| generators                 | 21.8 ms                                                         | 19.8 ms: 1.10x faster                                                 |
| raytrace                   | 201 ms                                                          | 183 ms: 1.10x faster                                                  |
| pickle_pure_python         | 231 us                                                          | 212 us: 1.09x faster                                                  |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.62 ms: 1.09x faster                                                 |
| docutils                   | 1.78 sec                                                        | 1.64 sec: 1.08x faster                                                |
| xml_etree_generate         | 61.4 ms                                                         | 56.9 ms: 1.08x faster                                                 |
| python_startup             | 28.3 ms                                                         | 26.2 ms: 1.08x faster                                                 |
| deltablue                  | 2.33 ms                                                         | 2.18 ms: 1.07x faster                                                 |
| comprehensions             | 12.5 us                                                         | 11.7 us: 1.07x faster                                                 |
| mako                       | 7.09 ms                                                         | 6.68 ms: 1.06x faster                                                 |
| hexiom                     | 4.44 ms                                                         | 4.24 ms: 1.05x faster                                                 |
| scimark_lu                 | 60.2 ms                                                         | 58.5 ms: 1.03x faster                                                 |
| meteor_contest             | 74.6 ms                                                         | 73.7 ms: 1.01x faster                                                 |
| many_optionals             | 436 us                                                          | 440 us: 1.01x slower                                                  |
| xml_etree_iterparse        | 62.6 ms                                                         | 65.0 ms: 1.04x slower                                                 |
| regex_dna                  | 114 ms                                                          | 119 ms: 1.05x slower                                                  |
| subparsers                 | 14.8 ms                                                         | 17.3 ms: 1.17x slower                                                 |
| gc_traversal               | 1.75 ms                                                         | 2.14 ms: 1.22x slower                                                 |
| shortest_path              | 290 ms                                                          | 357 ms: 1.23x slower                                                  |
| connected_components       | 267 ms                                                          | 330 ms: 1.24x slower                                                  |
| create_gc_cycles           | 1.06 ms                                                         | 1.31 ms: 1.24x slower                                                 |
| k_core                     | 1.38 sec                                                        | 1.71 sec: 1.24x slower                                                |
| logging_silent             | 60.3 ns                                                         | 328 ns: 5.43x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.19x faster                                                          |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-pythonperf1_win32-amd64-python-v3.14.0b2-3.14.0b2-12d3f88.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.217x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown