# Results vs. 3.13.0

- fork: python
- ref: c6b1a073438d93d4e629
- machine: windows-amd64
- commit hash: c6b1a07
- commit date: 2025-03-29
- overall geometric mean: 1.180x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 204 ms: 1.05x faster                                                        |
| docutils       | 1.53 sec                                                    | 1.54 sec: 1.00x slower                                                      |
| html5lib       | 38.2 ms                                                     | 36.0 ms: 1.06x faster                                                       |
| sphinx         | 617 ms                                                      | 598 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                        |
| async_tree_io              | 513 ms                                                      | 349 ms: 1.47x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 348 ms: 1.43x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 199 ms: 1.41x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 190 ms: 1.40x faster                                                        |
| async_tree_none            | 219 ms                                                      | 158 ms: 1.38x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 151 ms: 1.33x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 312 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 316 ms: 1.21x faster                                                        |
| async_generators           | 223 ms                                                      | 188 ms: 1.19x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 10.9 ms: 1.15x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 47.7 ms: 1.39x faster                                                       |
| float          | 50.8 ms                                                     | 37.1 ms: 1.37x faster                                                       |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.24x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.3 ms: 1.80x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 69.1 ms: 1.17x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.66 ms: 1.02x faster                                                       |
| regex_dna      | 115 ms                                                      | 124 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 105 us: 1.24x faster                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 47.6 ms: 1.12x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.68 ms: 1.09x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 33.5 ms: 1.09x faster                                                       |
| pickle_pure_python   | 186 us                                                      | 175 us: 1.06x faster                                                        |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 88.2 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.0 ms: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.7 ms: 1.10x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 21.0 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text    | 15.2 ms                                                     | 12.0 ms: 1.27x faster                                                       |
| genshi_xml     | 33.9 ms                                                     | 28.7 ms: 1.18x faster                                                       |
| mako           | 6.56 ms                                                     | 5.78 ms: 1.14x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 30.6 ms: 2.46x faster                                                       |
| mdp                        | 1.43 sec                                                    | 684 ms: 2.09x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.3 ms: 1.80x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 14.0 us: 1.65x faster                                                       |
| deepcopy                   | 223 us                                                      | 142 us: 1.57x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 49.2 ms: 1.55x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 42.9 ms: 1.48x faster                                                       |
| async_tree_io              | 513 ms                                                      | 349 ms: 1.47x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 348 ms: 1.43x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 199 ms: 1.41x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 190 ms: 1.40x faster                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 29.3 ms: 1.39x faster                                                       |
| nbody                      | 66.3 ms                                                     | 47.7 ms: 1.39x faster                                                       |
| async_tree_none            | 219 ms                                                      | 158 ms: 1.38x faster                                                        |
| float                      | 50.8 ms                                                     | 37.1 ms: 1.37x faster                                                       |
| go                         | 84.7 ms                                                     | 62.2 ms: 1.36x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 151 ms: 1.33x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.54 us: 1.31x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 1.99 ms: 1.31x faster                                                       |
| logging_silent             | 54.6 ns                                                     | 41.8 ns: 1.31x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 43.5 ms: 1.30x faster                                                       |
| hexiom                     | 3.84 ms                                                     | 2.96 ms: 1.30x faster                                                       |
| fannkuch                   | 252 ms                                                      | 197 ms: 1.28x faster                                                        |
| genshi_text                | 15.2 ms                                                     | 12.0 ms: 1.27x faster                                                       |
| generators                 | 19.0 ms                                                     | 15.0 ms: 1.27x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 105 us: 1.24x faster                                                        |
| pyflate                    | 283 ms                                                      | 230 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 312 ms: 1.22x faster                                                        |
| scimark_fft                | 175 ms                                                      | 144 ms: 1.22x faster                                                        |
| comprehensions             | 10.4 us                                                     | 8.54 us: 1.21x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 316 ms: 1.21x faster                                                        |
| chaos                      | 37.9 ms                                                     | 31.4 ms: 1.21x faster                                                       |
| typing_runtime_protocols   | 103 us                                                      | 86.5 us: 1.19x faster                                                       |
| deltablue                  | 1.89 ms                                                     | 1.59 ms: 1.19x faster                                                       |
| async_generators           | 223 ms                                                      | 188 ms: 1.19x faster                                                        |
| genshi_xml                 | 33.9 ms                                                     | 28.7 ms: 1.18x faster                                                       |
| richards                   | 26.3 ms                                                     | 22.2 ms: 1.18x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 411 ms: 1.18x faster                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 38.8 ms: 1.18x faster                                                       |
| richards_super             | 29.8 ms                                                     | 25.4 ms: 1.17x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 834 ms: 1.17x faster                                                        |
| regex_compile              | 80.7 ms                                                     | 69.1 ms: 1.17x faster                                                       |
| json                       | 3.30 ms                                                     | 2.83 ms: 1.16x faster                                                       |
| nqueens                    | 56.1 ms                                                     | 48.5 ms: 1.16x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.48 sec: 1.16x faster                                                      |
| coverage                   | 45.3 ms                                                     | 39.3 ms: 1.15x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 10.9 ms: 1.15x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.23 ms: 1.15x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.78 ms: 1.14x faster                                                       |
| sympy_str                  | 167 ms                                                      | 148 ms: 1.13x faster                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 47.6 ms: 1.12x faster                                                       |
| sympy_expand               | 286 ms                                                      | 255 ms: 1.12x faster                                                        |
| pylint                     | 205 ms                                                      | 185 ms: 1.11x faster                                                        |
| sympy_integrate            | 12.3 ms                                                     | 11.3 ms: 1.09x faster                                                       |
| raytrace                   | 153 ms                                                      | 140 ms: 1.09x faster                                                        |
| sympy_sum                  | 85.2 ms                                                     | 78.1 ms: 1.09x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.68 ms: 1.09x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 33.5 ms: 1.09x faster                                                       |
| meteor_contest             | 72.0 ms                                                     | 66.6 ms: 1.08x faster                                                       |
| pycparser                  | 695 ms                                                      | 648 ms: 1.07x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.48 us: 1.07x faster                                                       |
| pickle_pure_python         | 186 us                                                      | 175 us: 1.06x faster                                                        |
| dulwich_log                | 40.1 ms                                                     | 37.8 ms: 1.06x faster                                                       |
| html5lib                   | 38.2 ms                                                     | 36.0 ms: 1.06x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                       |
| 2to3                       | 215 ms                                                      | 204 ms: 1.05x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 88.2 ms: 1.05x faster                                                       |
| logging_format             | 6.18 us                                                     | 5.94 us: 1.04x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.64 sec: 1.04x faster                                                      |
| sphinx                     | 617 ms                                                      | 598 ms: 1.03x faster                                                        |
| logging_simple             | 5.77 us                                                     | 5.60 us: 1.03x faster                                                       |
| shortest_path              | 355 ms                                                      | 345 ms: 1.03x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.66 ms: 1.02x faster                                                       |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                        |
| docutils                   | 1.53 sec                                                    | 1.54 sec: 1.00x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.0 ms: 1.01x slower                                                       |
| connected_components       | 320 ms                                                      | 327 ms: 1.02x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 88.7 ms: 1.05x slower                                                       |
| regex_dna                  | 115 ms                                                      | 124 ms: 1.08x slower                                                        |
| python_startup             | 24.4 ms                                                     | 26.7 ms: 1.10x slower                                                       |
| many_optionals             | 361 us                                                      | 396 us: 1.10x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.34 ms: 1.10x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 21.0 ms: 1.24x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 14.6 ms: 1.35x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.74 ms: 1.40x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (2): django_template, bench_thread_pool
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250329-3.14.0a6+-c6b1a07-CLANG/bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.180x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown