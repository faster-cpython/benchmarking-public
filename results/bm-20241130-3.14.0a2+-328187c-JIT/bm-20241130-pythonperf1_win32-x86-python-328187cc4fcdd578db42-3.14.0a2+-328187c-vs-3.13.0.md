# Results vs. 3.13.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: windows-x86
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.054x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 268 ms: 1.05x slower                                                            |
| docutils       | 1.80 sec                                                        | 2.02 sec: 1.12x slower                                                          |
| html5lib       | 47.1 ms                                                         | 49.4 ms: 1.05x slower                                                           |
| sphinx         | 729 ms                                                          | 829 ms: 1.14x slower                                                            |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 266 ms: 1.08x faster                                                            |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 497 ms: 1.01x slower                                                            |
| coroutines                | 16.1 ms                                                         | 16.4 ms: 1.02x slower                                                           |
| asyncio_websockets        | 352 ms                                                          | 372 ms: 1.06x slower                                                            |
| async_tree_io             | 530 ms                                                          | 576 ms: 1.09x slower                                                            |
| async_tree_io_tg          | 499 ms                                                          | 549 ms: 1.10x slower                                                            |
| async_generators          | 267 ms                                                          | 329 ms: 1.23x slower                                                            |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                                    |

Benchmark hidden because not significant (4): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 202 ms: 1.01x faster                                                            |
| nbody          | 81.4 ms                                                         | 102 ms: 1.25x slower                                                            |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.55 ms: 1.18x faster                                                           |
| regex_v8       | 15.5 ms                                                         | 15.7 ms: 1.02x slower                                                           |
| regex_dna      | 112 ms                                                          | 119 ms: 1.06x slower                                                            |
| regex_compile  | 101 ms                                                          | 117 ms: 1.16x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.8 us: 1.04x faster                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.87 sec: 1.07x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 111 ms: 1.09x slower                                                            |
| xml_etree_iterparse  | 61.3 ms                                                         | 68.1 ms: 1.11x slower                                                           |
| json_dumps           | 7.53 ms                                                         | 9.05 ms: 1.20x slower                                                           |
| xml_etree_generate   | 61.9 ms                                                         | 74.5 ms: 1.20x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 295 us: 1.23x slower                                                            |
| xml_etree_process    | 44.6 ms                                                         | 55.5 ms: 1.25x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 206 us: 1.27x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.15x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                           |
| python_startup_no_site | 20.2 ms                                                         | 19.4 ms: 1.04x faster                                                           |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 7.33 ms: 1.04x slower                                                           |
| genshi_xml      | 49.0 ms                                                         | 55.0 ms: 1.12x slower                                                           |
| django_template | 32.0 ms                                                         | 36.9 ms: 1.15x slower                                                           |
| genshi_text     | 21.7 ms                                                         | 25.9 ms: 1.19x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.13x slower                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 783 us: 13.10x faster                                                           |
| coverage                  | 326 ms                                                          | 52.6 ms: 6.20x faster                                                           |
| sqlglot_normalize         | 223 ms                                                          | 112 ms: 1.99x faster                                                            |
| regex_effbot              | 1.82 ms                                                         | 1.55 ms: 1.18x faster                                                           |
| deepcopy_memo             | 26.2 us                                                         | 23.0 us: 1.14x faster                                                           |
| python_startup            | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                           |
| deepcopy                  | 311 us                                                          | 282 us: 1.10x faster                                                            |
| pathlib                   | 89.1 ms                                                         | 82.1 ms: 1.09x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 266 ms: 1.08x faster                                                            |
| bench_mp_pool             | 93.6 ms                                                         | 86.8 ms: 1.08x faster                                                           |
| deepcopy_reduce           | 2.94 us                                                         | 2.81 us: 1.05x faster                                                           |
| json_loads                | 21.7 us                                                         | 20.8 us: 1.04x faster                                                           |
| python_startup_no_site    | 20.2 ms                                                         | 19.4 ms: 1.04x faster                                                           |
| dulwich_log               | 50.2 ms                                                         | 49.4 ms: 1.02x faster                                                           |
| gc_traversal              | 1.76 ms                                                         | 1.74 ms: 1.01x faster                                                           |
| pidigits                  | 204 ms                                                          | 202 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 497 ms: 1.01x slower                                                            |
| regex_v8                  | 15.5 ms                                                         | 15.7 ms: 1.02x slower                                                           |
| coroutines                | 16.1 ms                                                         | 16.4 ms: 1.02x slower                                                           |
| json                      | 4.40 ms                                                         | 4.50 ms: 1.02x slower                                                           |
| mako                      | 7.02 ms                                                         | 7.33 ms: 1.04x slower                                                           |
| create_gc_cycles          | 1.08 ms                                                         | 1.13 ms: 1.05x slower                                                           |
| 2to3                      | 255 ms                                                          | 268 ms: 1.05x slower                                                            |
| html5lib                  | 47.1 ms                                                         | 49.4 ms: 1.05x slower                                                           |
| pylint                    | 225 ms                                                          | 237 ms: 1.05x slower                                                            |
| asyncio_websockets        | 352 ms                                                          | 372 ms: 1.06x slower                                                            |
| regex_dna                 | 112 ms                                                          | 119 ms: 1.06x slower                                                            |
| pycparser                 | 869 ms                                                          | 929 ms: 1.07x slower                                                            |
| tomli_loads               | 1.74 sec                                                        | 1.87 sec: 1.07x slower                                                          |
| logging_format            | 8.59 us                                                         | 9.22 us: 1.07x slower                                                           |
| logging_simple            | 7.89 us                                                         | 8.49 us: 1.08x slower                                                           |
| connected_components      | 266 ms                                                          | 288 ms: 1.08x slower                                                            |
| shortest_path             | 298 ms                                                          | 322 ms: 1.08x slower                                                            |
| async_tree_io             | 530 ms                                                          | 576 ms: 1.09x slower                                                            |
| xml_etree_parse           | 102 ms                                                          | 111 ms: 1.09x slower                                                            |
| mdp                       | 1.70 sec                                                        | 1.85 sec: 1.09x slower                                                          |
| sympy_sum                 | 108 ms                                                          | 118 ms: 1.09x slower                                                            |
| async_tree_io_tg          | 499 ms                                                          | 549 ms: 1.10x slower                                                            |
| spectral_norm             | 70.0 ms                                                         | 77.5 ms: 1.11x slower                                                           |
| scimark_sparse_mat_mult   | 2.88 ms                                                         | 3.20 ms: 1.11x slower                                                           |
| xml_etree_iterparse       | 61.3 ms                                                         | 68.1 ms: 1.11x slower                                                           |
| sympy_expand              | 377 ms                                                          | 421 ms: 1.12x slower                                                            |
| bpe_tokeniser             | 3.49 sec                                                        | 3.90 sec: 1.12x slower                                                          |
| docutils                  | 1.80 sec                                                        | 2.02 sec: 1.12x slower                                                          |
| genshi_xml                | 49.0 ms                                                         | 55.0 ms: 1.12x slower                                                           |
| sympy_str                 | 214 ms                                                          | 241 ms: 1.13x slower                                                            |
| meteor_contest            | 78.1 ms                                                         | 88.1 ms: 1.13x slower                                                           |
| pprint_safe_repr          | 658 ms                                                          | 745 ms: 1.13x slower                                                            |
| sphinx                    | 729 ms                                                          | 829 ms: 1.14x slower                                                            |
| telco                     | 6.27 ms                                                         | 7.13 ms: 1.14x slower                                                           |
| go                        | 111 ms                                                          | 127 ms: 1.15x slower                                                            |
| django_template           | 32.0 ms                                                         | 36.9 ms: 1.15x slower                                                           |
| regex_compile             | 101 ms                                                          | 117 ms: 1.16x slower                                                            |
| pprint_pformat            | 1.32 sec                                                        | 1.54 sec: 1.17x slower                                                          |
| crypto_pyaes              | 56.6 ms                                                         | 66.0 ms: 1.17x slower                                                           |
| sqlglot_parse             | 1.02 ms                                                         | 1.19 ms: 1.17x slower                                                           |
| sympy_integrate           | 15.2 ms                                                         | 17.9 ms: 1.18x slower                                                           |
| sqlglot_transpile         | 1.26 ms                                                         | 1.49 ms: 1.18x slower                                                           |
| typing_runtime_protocols  | 141 us                                                          | 167 us: 1.18x slower                                                            |
| fannkuch                  | 288 ms                                                          | 343 ms: 1.19x slower                                                            |
| genshi_text               | 21.7 ms                                                         | 25.9 ms: 1.19x slower                                                           |
| k_core                    | 1.43 sec                                                        | 1.72 sec: 1.20x slower                                                          |
| json_dumps                | 7.53 ms                                                         | 9.05 ms: 1.20x slower                                                           |
| xml_etree_generate        | 61.9 ms                                                         | 74.5 ms: 1.20x slower                                                           |
| scimark_fft               | 204 ms                                                          | 248 ms: 1.22x slower                                                            |
| scimark_sor               | 85.8 ms                                                         | 106 ms: 1.23x slower                                                            |
| async_generators          | 267 ms                                                          | 329 ms: 1.23x slower                                                            |
| pickle_pure_python        | 239 us                                                          | 295 us: 1.23x slower                                                            |
| sqlglot_optimize          | 42.4 ms                                                         | 52.7 ms: 1.24x slower                                                           |
| xml_etree_process         | 44.6 ms                                                         | 55.5 ms: 1.25x slower                                                           |
| nbody                     | 81.4 ms                                                         | 102 ms: 1.25x slower                                                            |
| pyflate                   | 322 ms                                                          | 405 ms: 1.26x slower                                                            |
| scimark_lu                | 60.7 ms                                                         | 76.6 ms: 1.26x slower                                                           |
| unpickle_pure_python      | 162 us                                                          | 206 us: 1.27x slower                                                            |
| logging_silent            | 62.4 ns                                                         | 79.6 ns: 1.28x slower                                                           |
| scimark_monte_carlo       | 48.7 ms                                                         | 62.3 ms: 1.28x slower                                                           |
| richards                  | 33.4 ms                                                         | 44.0 ms: 1.32x slower                                                           |
| nqueens                   | 75.1 ms                                                         | 99.2 ms: 1.32x slower                                                           |
| chaos                     | 49.4 ms                                                         | 65.6 ms: 1.33x slower                                                           |
| richards_super            | 37.0 ms                                                         | 49.8 ms: 1.34x slower                                                           |
| deltablue                 | 2.35 ms                                                         | 3.26 ms: 1.39x slower                                                           |
| comprehensions            | 13.1 us                                                         | 18.6 us: 1.41x slower                                                           |
| hexiom                    | 4.60 ms                                                         | 7.18 ms: 1.56x slower                                                           |
| raytrace                  | 203 ms                                                          | 327 ms: 1.61x slower                                                            |
| generators                | 21.5 ms                                                         | 36.2 ms: 1.68x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.06x slower                                                                    |

Benchmark hidden because not significant (6): async_tree_none, async_tree_cpu_io_mixed_tg, float, async_tree_none_tg, async_tree_memoization, bench_thread_pool
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (3) of results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.054x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown