# Results vs. base

- fork: Fidget-Spinner
- ref: baseline_jit
- machine: windows-amd64
- commit hash: e55b89a
- commit date: 2025-03-19
- overall geometric mean: 1.034x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 227 ms                                                                      | 231 ms: 1.02x slower                                                          |
| docutils       | 1.75 sec                                                                    | 1.74 sec: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                  |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| asyncio_websockets         | 307 ms                                                                      | 302 ms: 1.02x faster                                                          |
| coroutines                 | 14.1 ms                                                                     | 14.1 ms: 1.00x faster                                                         |
| async_tree_cpu_io_mixed_tg | 338 ms                                                                      | 344 ms: 1.02x slower                                                          |
| async_tree_io_tg           | 411 ms                                                                      | 420 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed    | 341 ms                                                                      | 348 ms: 1.02x slower                                                          |
| async_tree_none_tg         | 175 ms                                                                      | 179 ms: 1.03x slower                                                          |
| async_tree_memoization     | 221 ms                                                                      | 227 ms: 1.03x slower                                                          |
| async_generators           | 246 ms                                                                      | 254 ms: 1.03x slower                                                          |
| async_tree_none            | 186 ms                                                                      | 193 ms: 1.03x slower                                                          |
| async_tree_io              | 418 ms                                                                      | 435 ms: 1.04x slower                                                          |
| Geometric mean             | (ref)                                                                       | 1.02x slower                                                                  |

Benchmark hidden because not significant (1): async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 58.6 ms                                                                     | 57.9 ms: 1.01x faster                                                         |
| float          | 47.3 ms                                                                     | 47.6 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 1.45 ms                                                                     | 1.48 ms: 1.02x slower                                                         |
| regex_compile  | 86.2 ms                                                                     | 88.3 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                  |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_loads           | 15.3 us                                                                     | 15.1 us: 1.01x faster                                                         |
| xml_etree_iterparse  | 63.1 ms                                                                     | 63.6 ms: 1.01x slower                                                         |
| xml_etree_parse      | 87.6 ms                                                                     | 90.2 ms: 1.03x slower                                                         |
| pickle_pure_python   | 222 us                                                                      | 228 us: 1.03x slower                                                          |
| tomli_loads          | 1.22 sec                                                                    | 1.28 sec: 1.04x slower                                                        |
| xml_etree_process    | 38.9 ms                                                                     | 43.0 ms: 1.11x slower                                                         |
| xml_etree_generate   | 53.0 ms                                                                     | 59.7 ms: 1.13x slower                                                         |
| unpickle_pure_python | 126 us                                                                      | 157 us: 1.25x slower                                                          |
| Geometric mean       | (ref)                                                                       | 1.06x slower                                                                  |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup | 25.8 ms                                                                     | 26.6 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                  |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text    | 16.9 ms                                                                     | 17.1 ms: 1.01x slower                                                         |
| mako           | 5.81 ms                                                                     | 7.06 ms: 1.21x slower                                                         |
| Geometric mean | (ref)                                                                       | 1.05x slower                                                                  |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| scimark_sparse_mat_mult    | 2.27 ms                                                                     | 2.09 ms: 1.09x faster                                                         |
| thrift                     | 537 us                                                                      | 522 us: 1.03x faster                                                          |
| json                       | 3.16 ms                                                                     | 3.10 ms: 1.02x faster                                                         |
| scimark_lu                 | 62.3 ms                                                                     | 61.2 ms: 1.02x faster                                                         |
| asyncio_websockets         | 307 ms                                                                      | 302 ms: 1.02x faster                                                          |
| nbody                      | 58.6 ms                                                                     | 57.9 ms: 1.01x faster                                                         |
| deltablue                  | 2.40 ms                                                                     | 2.37 ms: 1.01x faster                                                         |
| logging_simple             | 6.63 us                                                                     | 6.55 us: 1.01x faster                                                         |
| json_loads                 | 15.3 us                                                                     | 15.1 us: 1.01x faster                                                         |
| many_optionals             | 457 us                                                                      | 453 us: 1.01x faster                                                          |
| docutils                   | 1.75 sec                                                                    | 1.74 sec: 1.01x faster                                                        |
| scimark_sor                | 81.8 ms                                                                     | 81.3 ms: 1.01x faster                                                         |
| mdp                        | 1.58 sec                                                                    | 1.58 sec: 1.00x faster                                                        |
| coroutines                 | 14.1 ms                                                                     | 14.1 ms: 1.00x faster                                                         |
| logging_silent             | 59.5 ns                                                                     | 59.7 ns: 1.00x slower                                                         |
| meteor_contest             | 75.9 ms                                                                     | 76.3 ms: 1.01x slower                                                         |
| float                      | 47.3 ms                                                                     | 47.6 ms: 1.01x slower                                                         |
| xml_etree_iterparse        | 63.1 ms                                                                     | 63.6 ms: 1.01x slower                                                         |
| sympy_sum                  | 91.7 ms                                                                     | 92.4 ms: 1.01x slower                                                         |
| scimark_fft                | 158 ms                                                                      | 159 ms: 1.01x slower                                                          |
| sympy_integrate            | 13.5 ms                                                                     | 13.6 ms: 1.01x slower                                                         |
| sympy_expand               | 315 ms                                                                      | 318 ms: 1.01x slower                                                          |
| generators                 | 20.6 ms                                                                     | 20.8 ms: 1.01x slower                                                         |
| genshi_text                | 16.9 ms                                                                     | 17.1 ms: 1.01x slower                                                         |
| dulwich_log                | 43.5 ms                                                                     | 44.0 ms: 1.01x slower                                                         |
| scimark_monte_carlo        | 44.1 ms                                                                     | 44.6 ms: 1.01x slower                                                         |
| sympy_str                  | 180 ms                                                                      | 182 ms: 1.01x slower                                                          |
| connected_components       | 326 ms                                                                      | 331 ms: 1.01x slower                                                          |
| create_gc_cycles           | 1.25 ms                                                                     | 1.27 ms: 1.01x slower                                                         |
| richards                   | 29.4 ms                                                                     | 29.9 ms: 1.02x slower                                                         |
| shortest_path              | 355 ms                                                                      | 361 ms: 1.02x slower                                                          |
| regex_effbot               | 1.45 ms                                                                     | 1.48 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 338 ms                                                                      | 344 ms: 1.02x slower                                                          |
| 2to3                       | 227 ms                                                                      | 231 ms: 1.02x slower                                                          |
| async_tree_io_tg           | 411 ms                                                                      | 420 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed    | 341 ms                                                                      | 348 ms: 1.02x slower                                                          |
| subparsers                 | 16.6 ms                                                                     | 16.9 ms: 1.02x slower                                                         |
| regex_compile              | 86.2 ms                                                                     | 88.3 ms: 1.02x slower                                                         |
| chaos                      | 44.1 ms                                                                     | 45.2 ms: 1.03x slower                                                         |
| async_tree_none_tg         | 175 ms                                                                      | 179 ms: 1.03x slower                                                          |
| async_tree_memoization     | 221 ms                                                                      | 227 ms: 1.03x slower                                                          |
| sqlglot_v2_normalize       | 75.4 ms                                                                     | 77.5 ms: 1.03x slower                                                         |
| sqlglot_v2_optimize        | 36.9 ms                                                                     | 38.0 ms: 1.03x slower                                                         |
| xml_etree_parse            | 87.6 ms                                                                     | 90.2 ms: 1.03x slower                                                         |
| k_core                     | 1.67 sec                                                                    | 1.72 sec: 1.03x slower                                                        |
| pickle_pure_python         | 222 us                                                                      | 228 us: 1.03x slower                                                          |
| python_startup             | 25.8 ms                                                                     | 26.6 ms: 1.03x slower                                                         |
| richards_super             | 33.0 ms                                                                     | 34.1 ms: 1.03x slower                                                         |
| async_generators           | 246 ms                                                                      | 254 ms: 1.03x slower                                                          |
| deepcopy_reduce            | 2.03 us                                                                     | 2.10 us: 1.03x slower                                                         |
| async_tree_none            | 186 ms                                                                      | 193 ms: 1.03x slower                                                          |
| spectral_norm              | 58.8 ms                                                                     | 60.8 ms: 1.03x slower                                                         |
| pprint_pformat             | 1.10 sec                                                                    | 1.14 sec: 1.04x slower                                                        |
| async_tree_io              | 418 ms                                                                      | 435 ms: 1.04x slower                                                          |
| go                         | 88.7 ms                                                                     | 92.3 ms: 1.04x slower                                                         |
| tomli_loads                | 1.22 sec                                                                    | 1.28 sec: 1.04x slower                                                        |
| coverage                   | 47.4 ms                                                                     | 49.8 ms: 1.05x slower                                                         |
| nqueens                    | 61.6 ms                                                                     | 64.8 ms: 1.05x slower                                                         |
| typing_runtime_protocols   | 112 us                                                                      | 120 us: 1.07x slower                                                          |
| sqlglot_v2_transpile       | 1.10 ms                                                                     | 1.18 ms: 1.07x slower                                                         |
| fannkuch                   | 246 ms                                                                      | 265 ms: 1.07x slower                                                          |
| pprint_safe_repr           | 519 ms                                                                      | 562 ms: 1.08x slower                                                          |
| deepcopy                   | 193 us                                                                      | 211 us: 1.10x slower                                                          |
| telco                      | 4.58 ms                                                                     | 5.05 ms: 1.10x slower                                                         |
| xml_etree_process          | 38.9 ms                                                                     | 43.0 ms: 1.11x slower                                                         |
| sqlglot_v2_parse           | 866 us                                                                      | 964 us: 1.11x slower                                                          |
| crypto_pyaes               | 50.1 ms                                                                     | 55.9 ms: 1.11x slower                                                         |
| pyflate                    | 283 ms                                                                      | 318 ms: 1.12x slower                                                          |
| xml_etree_generate         | 53.0 ms                                                                     | 59.7 ms: 1.13x slower                                                         |
| sqlite_synth               | 1.53 us                                                                     | 1.74 us: 1.14x slower                                                         |
| bpe_tokeniser              | 2.74 sec                                                                    | 3.14 sec: 1.14x slower                                                        |
| hexiom                     | 4.53 ms                                                                     | 5.39 ms: 1.19x slower                                                         |
| mako                       | 5.81 ms                                                                     | 7.06 ms: 1.21x slower                                                         |
| deepcopy_memo              | 18.0 us                                                                     | 22.0 us: 1.22x slower                                                         |
| unpickle_pure_python       | 126 us                                                                      | 157 us: 1.25x slower                                                          |
| comprehensions             | 11.7 us                                                                     | 15.5 us: 1.32x slower                                                         |
| Geometric mean             | (ref)                                                                       | 1.03x slower                                                                  |

Benchmark hidden because not significant (18): regex_v8, pathlib, django_template, logging_format, pidigits, regex_dna, gc_traversal, bench_mp_pool, genshi_xml, json_dumps, pylint, sphinx, bench_thread_pool, async_tree_memoization_tg, html5lib, python_startup_no_site, raytrace, pycparser

- Geometric mean (including insignificant results): 1.034x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown