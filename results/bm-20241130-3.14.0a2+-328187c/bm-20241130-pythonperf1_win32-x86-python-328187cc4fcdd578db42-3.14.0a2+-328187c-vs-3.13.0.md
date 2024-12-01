# Results vs. 3.13.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: windows-x86
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.039x faster
- HPT reliability: 86.99%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 241 ms: 1.06x faster                                                            |
| docutils       | 1.80 sec                                                        | 1.81 sec: 1.01x slower                                                          |
| html5lib       | 47.1 ms                                                         | 45.1 ms: 1.04x faster                                                           |
| sphinx         | 729 ms                                                          | 743 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 248 ms: 1.15x faster                                                            |
| async_tree_none            | 245 ms                                                          | 215 ms: 1.14x faster                                                            |
| async_tree_memoization     | 302 ms                                                          | 273 ms: 1.10x faster                                                            |
| async_tree_none_tg         | 216 ms                                                          | 203 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 479 ms: 1.02x faster                                                            |
| coroutines                 | 16.1 ms                                                         | 16.3 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 475 ms: 1.01x slower                                                            |
| async_tree_io_tg           | 499 ms                                                          | 523 ms: 1.05x slower                                                            |
| async_generators           | 267 ms                                                          | 298 ms: 1.11x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 83.6 ms: 1.03x slower                                                           |
| float          | 56.4 ms                                                         | 60.2 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.55 ms: 1.17x faster                                                           |
| regex_compile  | 101 ms                                                          | 107 ms: 1.05x slower                                                            |
| regex_dna      | 112 ms                                                          | 119 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.8 us: 1.04x faster                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.77 sec: 1.02x slower                                                          |
| xml_etree_generate   | 61.9 ms                                                         | 66.3 ms: 1.07x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 173 us: 1.07x slower                                                            |
| xml_etree_parse      | 102 ms                                                          | 110 ms: 1.07x slower                                                            |
| pickle_pure_python   | 239 us                                                          | 257 us: 1.08x slower                                                            |
| xml_etree_process    | 44.6 ms                                                         | 47.9 ms: 1.08x slower                                                           |
| xml_etree_iterparse  | 61.3 ms                                                         | 67.6 ms: 1.10x slower                                                           |
| json_dumps           | 7.53 ms                                                         | 8.64 ms: 1.15x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 26.7 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 46.2 ms: 1.06x faster                                                           |
| genshi_text     | 21.7 ms                                                         | 21.6 ms: 1.01x faster                                                           |
| django_template | 32.0 ms                                                         | 32.6 ms: 1.02x slower                                                           |
| mako            | 7.02 ms                                                         | 7.49 ms: 1.07x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.00x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 744 us: 13.78x faster                                                           |
| coverage                   | 326 ms                                                          | 54.1 ms: 6.03x faster                                                           |
| deepcopy                   | 311 us                                                          | 245 us: 1.27x faster                                                            |
| deepcopy_memo              | 26.2 us                                                         | 21.2 us: 1.24x faster                                                           |
| regex_effbot               | 1.82 ms                                                         | 1.55 ms: 1.17x faster                                                           |
| deepcopy_reduce            | 2.94 us                                                         | 2.53 us: 1.16x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 248 ms: 1.15x faster                                                            |
| async_tree_none            | 245 ms                                                          | 215 ms: 1.14x faster                                                            |
| async_tree_memoization     | 302 ms                                                          | 273 ms: 1.10x faster                                                            |
| pathlib                    | 89.1 ms                                                         | 81.7 ms: 1.09x faster                                                           |
| go                         | 111 ms                                                          | 102 ms: 1.08x faster                                                            |
| pycparser                  | 869 ms                                                          | 812 ms: 1.07x faster                                                            |
| pylint                     | 225 ms                                                          | 210 ms: 1.07x faster                                                            |
| async_tree_none_tg         | 216 ms                                                          | 203 ms: 1.06x faster                                                            |
| python_startup             | 28.3 ms                                                         | 26.7 ms: 1.06x faster                                                           |
| genshi_xml                 | 49.0 ms                                                         | 46.2 ms: 1.06x faster                                                           |
| 2to3                       | 255 ms                                                          | 241 ms: 1.06x faster                                                            |
| html5lib                   | 47.1 ms                                                         | 45.1 ms: 1.04x faster                                                           |
| json_loads                 | 21.7 us                                                         | 20.8 us: 1.04x faster                                                           |
| shortest_path              | 298 ms                                                          | 286 ms: 1.04x faster                                                            |
| json                       | 4.40 ms                                                         | 4.25 ms: 1.04x faster                                                           |
| sympy_sum                  | 108 ms                                                          | 105 ms: 1.03x faster                                                            |
| connected_components       | 266 ms                                                          | 259 ms: 1.03x faster                                                            |
| pprint_safe_repr           | 658 ms                                                          | 639 ms: 1.03x faster                                                            |
| gc_traversal               | 1.76 ms                                                         | 1.72 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 479 ms: 1.02x faster                                                            |
| sympy_expand               | 377 ms                                                          | 369 ms: 1.02x faster                                                            |
| logging_simple             | 7.89 us                                                         | 7.75 us: 1.02x faster                                                           |
| sympy_str                  | 214 ms                                                          | 210 ms: 1.02x faster                                                            |
| bench_mp_pool              | 93.6 ms                                                         | 92.1 ms: 1.02x faster                                                           |
| nqueens                    | 75.1 ms                                                         | 74.0 ms: 1.02x faster                                                           |
| logging_format             | 8.59 us                                                         | 8.46 us: 1.02x faster                                                           |
| sqlglot_normalize          | 223 ms                                                          | 220 ms: 1.01x faster                                                            |
| sympy_integrate            | 15.2 ms                                                         | 15.1 ms: 1.01x faster                                                           |
| genshi_text                | 21.7 ms                                                         | 21.6 ms: 1.01x faster                                                           |
| bpe_tokeniser              | 3.49 sec                                                        | 3.47 sec: 1.01x faster                                                          |
| dulwich_log                | 50.2 ms                                                         | 50.4 ms: 1.00x slower                                                           |
| docutils                   | 1.80 sec                                                        | 1.81 sec: 1.01x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 16.3 ms: 1.01x slower                                                           |
| sqlglot_optimize           | 42.4 ms                                                         | 42.8 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 475 ms: 1.01x slower                                                            |
| pprint_pformat             | 1.32 sec                                                        | 1.34 sec: 1.01x slower                                                          |
| typing_runtime_protocols   | 141 us                                                          | 143 us: 1.01x slower                                                            |
| tomli_loads                | 1.74 sec                                                        | 1.77 sec: 1.02x slower                                                          |
| django_template            | 32.0 ms                                                         | 32.6 ms: 1.02x slower                                                           |
| meteor_contest             | 78.1 ms                                                         | 79.5 ms: 1.02x slower                                                           |
| comprehensions             | 13.1 us                                                         | 13.4 us: 1.02x slower                                                           |
| sphinx                     | 729 ms                                                          | 743 ms: 1.02x slower                                                            |
| spectral_norm              | 70.0 ms                                                         | 71.4 ms: 1.02x slower                                                           |
| sqlglot_transpile          | 1.26 ms                                                         | 1.29 ms: 1.02x slower                                                           |
| sqlglot_parse              | 1.02 ms                                                         | 1.04 ms: 1.02x slower                                                           |
| nbody                      | 81.4 ms                                                         | 83.6 ms: 1.03x slower                                                           |
| mdp                        | 1.70 sec                                                        | 1.75 sec: 1.03x slower                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 1.12 ms: 1.03x slower                                                           |
| crypto_pyaes               | 56.6 ms                                                         | 58.4 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 523 ms: 1.05x slower                                                            |
| hexiom                     | 4.60 ms                                                         | 4.81 ms: 1.05x slower                                                           |
| regex_compile              | 101 ms                                                          | 107 ms: 1.05x slower                                                            |
| regex_dna                  | 112 ms                                                          | 119 ms: 1.06x slower                                                            |
| fannkuch                   | 288 ms                                                          | 305 ms: 1.06x slower                                                            |
| float                      | 56.4 ms                                                         | 60.2 ms: 1.07x slower                                                           |
| mako                       | 7.02 ms                                                         | 7.49 ms: 1.07x slower                                                           |
| xml_etree_generate         | 61.9 ms                                                         | 66.3 ms: 1.07x slower                                                           |
| unpickle_pure_python       | 162 us                                                          | 173 us: 1.07x slower                                                            |
| xml_etree_parse            | 102 ms                                                          | 110 ms: 1.07x slower                                                            |
| pickle_pure_python         | 239 us                                                          | 257 us: 1.08x slower                                                            |
| xml_etree_process          | 44.6 ms                                                         | 47.9 ms: 1.08x slower                                                           |
| scimark_lu                 | 60.7 ms                                                         | 66.0 ms: 1.09x slower                                                           |
| telco                      | 6.27 ms                                                         | 6.87 ms: 1.10x slower                                                           |
| chaos                      | 49.4 ms                                                         | 54.1 ms: 1.10x slower                                                           |
| pyflate                    | 322 ms                                                          | 353 ms: 1.10x slower                                                            |
| scimark_monte_carlo        | 48.7 ms                                                         | 53.7 ms: 1.10x slower                                                           |
| xml_etree_iterparse        | 61.3 ms                                                         | 67.6 ms: 1.10x slower                                                           |
| deltablue                  | 2.35 ms                                                         | 2.59 ms: 1.10x slower                                                           |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.20 ms: 1.11x slower                                                           |
| generators                 | 21.5 ms                                                         | 24.0 ms: 1.11x slower                                                           |
| async_generators           | 267 ms                                                          | 298 ms: 1.11x slower                                                            |
| scimark_fft                | 204 ms                                                          | 230 ms: 1.13x slower                                                            |
| logging_silent             | 62.4 ns                                                         | 71.0 ns: 1.14x slower                                                           |
| richards                   | 33.4 ms                                                         | 38.2 ms: 1.14x slower                                                           |
| json_dumps                 | 7.53 ms                                                         | 8.64 ms: 1.15x slower                                                           |
| scimark_sor                | 85.8 ms                                                         | 99.1 ms: 1.16x slower                                                           |
| richards_super             | 37.0 ms                                                         | 42.9 ms: 1.16x slower                                                           |
| k_core                     | 1.43 sec                                                        | 1.67 sec: 1.16x slower                                                          |
| raytrace                   | 203 ms                                                          | 244 ms: 1.20x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (6): bench_thread_pool, python_startup_no_site, pidigits, regex_v8, asyncio_websockets, async_tree_io
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (3) of results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 86.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown