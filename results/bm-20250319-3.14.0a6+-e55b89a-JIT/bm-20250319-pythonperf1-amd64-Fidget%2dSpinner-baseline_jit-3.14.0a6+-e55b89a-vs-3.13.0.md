# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: baseline_jit
- machine: windows-amd64
- commit hash: e55b89a
- commit date: 2025-03-19
- overall geometric mean: 1.015x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 231 ms: 1.07x slower                                                          |
| docutils       | 1.53 sec                                                    | 1.74 sec: 1.14x slower                                                        |
| html5lib       | 38.2 ms                                                     | 41.6 ms: 1.09x slower                                                         |
| sphinx         | 617 ms                                                      | 675 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                       | 1.10x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.29x faster                                                          |
| async_tree_io_tg           | 497 ms                                                      | 420 ms: 1.18x faster                                                          |
| async_tree_io              | 513 ms                                                      | 435 ms: 1.18x faster                                                          |
| async_tree_memoization     | 265 ms                                                      | 227 ms: 1.17x faster                                                          |
| async_tree_none            | 219 ms                                                      | 193 ms: 1.14x faster                                                          |
| async_tree_none_tg         | 200 ms                                                      | 179 ms: 1.12x faster                                                          |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                          |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 348 ms: 1.09x faster                                                          |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.12x slower                                                         |
| async_generators           | 223 ms                                                      | 254 ms: 1.14x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 57.9 ms: 1.14x faster                                                         |
| float          | 50.8 ms                                                     | 47.6 ms: 1.07x faster                                                         |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                         |
| regex_effbot   | 1.69 ms                                                     | 1.48 ms: 1.15x faster                                                         |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                                          |
| regex_compile  | 80.7 ms                                                     | 88.3 ms: 1.09x slower                                                         |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                        |
| xml_etree_parse      | 92.2 ms                                                     | 90.2 ms: 1.02x faster                                                         |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                         |
| xml_etree_generate   | 53.5 ms                                                     | 59.7 ms: 1.12x slower                                                         |
| json_dumps           | 6.19 ms                                                     | 7.01 ms: 1.13x slower                                                         |
| xml_etree_process    | 36.5 ms                                                     | 43.0 ms: 1.18x slower                                                         |
| unpickle_pure_python | 130 us                                                      | 157 us: 1.21x slower                                                          |
| pickle_pure_python   | 186 us                                                      | 228 us: 1.23x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                  |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                         |
| python_startup_no_site | 16.9 ms                                                     | 20.8 ms: 1.23x slower                                                         |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 7.06 ms: 1.08x slower                                                         |
| genshi_text     | 15.2 ms                                                     | 17.1 ms: 1.12x slower                                                         |
| genshi_xml      | 33.9 ms                                                     | 38.4 ms: 1.13x slower                                                         |
| django_template | 20.3 ms                                                     | 26.1 ms: 1.29x slower                                                         |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 522 us: 16.23x faster                                                         |
| pathlib                    | 75.3 ms                                                     | 32.5 ms: 2.32x faster                                                         |
| regex_v8                   | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                         |
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.29x faster                                                          |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.09 ms: 1.24x faster                                                         |
| async_tree_io_tg           | 497 ms                                                      | 420 ms: 1.18x faster                                                          |
| async_tree_io              | 513 ms                                                      | 435 ms: 1.18x faster                                                          |
| async_tree_memoization     | 265 ms                                                      | 227 ms: 1.17x faster                                                          |
| regex_effbot               | 1.69 ms                                                     | 1.48 ms: 1.15x faster                                                         |
| nbody                      | 66.3 ms                                                     | 57.9 ms: 1.14x faster                                                         |
| async_tree_none            | 219 ms                                                      | 193 ms: 1.14x faster                                                          |
| async_tree_none_tg         | 200 ms                                                      | 179 ms: 1.12x faster                                                          |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                          |
| scimark_fft                | 175 ms                                                      | 159 ms: 1.10x faster                                                          |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 348 ms: 1.09x faster                                                          |
| tomli_loads                | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                        |
| float                      | 50.8 ms                                                     | 47.6 ms: 1.07x faster                                                         |
| json                       | 3.30 ms                                                     | 3.10 ms: 1.06x faster                                                         |
| deepcopy                   | 223 us                                                      | 211 us: 1.06x faster                                                          |
| deepcopy_memo              | 23.1 us                                                     | 22.0 us: 1.05x faster                                                         |
| spectral_norm              | 63.4 ms                                                     | 60.8 ms: 1.04x faster                                                         |
| xml_etree_parse            | 92.2 ms                                                     | 90.2 ms: 1.02x faster                                                         |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                          |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.01x slower                                                          |
| shortest_path              | 355 ms                                                      | 361 ms: 1.02x slower                                                          |
| connected_components       | 320 ms                                                      | 331 ms: 1.03x slower                                                          |
| deepcopy_reduce            | 2.02 us                                                     | 2.10 us: 1.04x slower                                                         |
| create_gc_cycles           | 1.22 ms                                                     | 1.27 ms: 1.04x slower                                                         |
| gc_traversal               | 1.96 ms                                                     | 2.04 ms: 1.04x slower                                                         |
| telco                      | 4.85 ms                                                     | 5.05 ms: 1.04x slower                                                         |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                         |
| fannkuch                   | 252 ms                                                      | 265 ms: 1.05x slower                                                          |
| meteor_contest             | 72.0 ms                                                     | 76.3 ms: 1.06x slower                                                         |
| bench_mp_pool              | 84.2 ms                                                     | 89.4 ms: 1.06x slower                                                         |
| scimark_sor                | 76.2 ms                                                     | 81.3 ms: 1.07x slower                                                         |
| 2to3                       | 215 ms                                                      | 231 ms: 1.07x slower                                                          |
| mako                       | 6.56 ms                                                     | 7.06 ms: 1.08x slower                                                         |
| scimark_lu                 | 56.7 ms                                                     | 61.2 ms: 1.08x slower                                                         |
| sympy_sum                  | 85.2 ms                                                     | 92.4 ms: 1.08x slower                                                         |
| bench_thread_pool          | 810 us                                                      | 879 us: 1.09x slower                                                          |
| go                         | 84.7 ms                                                     | 92.3 ms: 1.09x slower                                                         |
| pycparser                  | 695 ms                                                      | 758 ms: 1.09x slower                                                          |
| python_startup             | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                         |
| html5lib                   | 38.2 ms                                                     | 41.6 ms: 1.09x slower                                                         |
| bpe_tokeniser              | 2.87 sec                                                    | 3.14 sec: 1.09x slower                                                        |
| sympy_str                  | 167 ms                                                      | 182 ms: 1.09x slower                                                          |
| sphinx                     | 617 ms                                                      | 675 ms: 1.09x slower                                                          |
| regex_compile              | 80.7 ms                                                     | 88.3 ms: 1.09x slower                                                         |
| generators                 | 19.0 ms                                                     | 20.8 ms: 1.09x slower                                                         |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.6 ms: 1.09x slower                                                         |
| logging_silent             | 54.6 ns                                                     | 59.7 ns: 1.09x slower                                                         |
| dulwich_log                | 40.1 ms                                                     | 44.0 ms: 1.10x slower                                                         |
| sqlite_synth               | 1.59 us                                                     | 1.74 us: 1.10x slower                                                         |
| coverage                   | 45.3 ms                                                     | 49.8 ms: 1.10x slower                                                         |
| mdp                        | 1.43 sec                                                    | 1.58 sec: 1.10x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 13.6 ms: 1.10x slower                                                         |
| sympy_expand               | 286 ms                                                      | 318 ms: 1.11x slower                                                          |
| xml_etree_generate         | 53.5 ms                                                     | 59.7 ms: 1.12x slower                                                         |
| genshi_text                | 15.2 ms                                                     | 17.1 ms: 1.12x slower                                                         |
| pyflate                    | 283 ms                                                      | 318 ms: 1.12x slower                                                          |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.12x slower                                                         |
| json_dumps                 | 6.19 ms                                                     | 7.01 ms: 1.13x slower                                                         |
| logging_simple             | 5.77 us                                                     | 6.55 us: 1.13x slower                                                         |
| genshi_xml                 | 33.9 ms                                                     | 38.4 ms: 1.13x slower                                                         |
| docutils                   | 1.53 sec                                                    | 1.74 sec: 1.14x slower                                                        |
| richards                   | 26.3 ms                                                     | 29.9 ms: 1.14x slower                                                         |
| async_generators           | 223 ms                                                      | 254 ms: 1.14x slower                                                          |
| richards_super             | 29.8 ms                                                     | 34.1 ms: 1.14x slower                                                         |
| nqueens                    | 56.1 ms                                                     | 64.8 ms: 1.15x slower                                                         |
| logging_format             | 6.18 us                                                     | 7.14 us: 1.16x slower                                                         |
| pprint_safe_repr           | 485 ms                                                      | 562 ms: 1.16x slower                                                          |
| typing_runtime_protocols   | 103 us                                                      | 120 us: 1.16x slower                                                          |
| pprint_pformat             | 977 ms                                                      | 1.14 sec: 1.17x slower                                                        |
| xml_etree_process          | 36.5 ms                                                     | 43.0 ms: 1.18x slower                                                         |
| chaos                      | 37.9 ms                                                     | 45.2 ms: 1.19x slower                                                         |
| unpickle_pure_python       | 130 us                                                      | 157 us: 1.21x slower                                                          |
| crypto_pyaes               | 45.6 ms                                                     | 55.9 ms: 1.23x slower                                                         |
| pickle_pure_python         | 186 us                                                      | 228 us: 1.23x slower                                                          |
| python_startup_no_site     | 16.9 ms                                                     | 20.8 ms: 1.23x slower                                                         |
| deltablue                  | 1.89 ms                                                     | 2.37 ms: 1.25x slower                                                         |
| many_optionals             | 361 us                                                      | 453 us: 1.26x slower                                                          |
| raytrace                   | 153 ms                                                      | 196 ms: 1.28x slower                                                          |
| django_template            | 20.3 ms                                                     | 26.1 ms: 1.29x slower                                                         |
| hexiom                     | 3.84 ms                                                     | 5.39 ms: 1.40x slower                                                         |
| comprehensions             | 10.4 us                                                     | 15.5 us: 1.49x slower                                                         |
| subparsers                 | 10.9 ms                                                     | 16.9 ms: 1.56x slower                                                         |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                  |

Benchmark hidden because not significant (4): json_loads, pylint, asyncio_websockets, k_core
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250319-3.14.0a6+-e55b89a-JIT/bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.015x slower

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown