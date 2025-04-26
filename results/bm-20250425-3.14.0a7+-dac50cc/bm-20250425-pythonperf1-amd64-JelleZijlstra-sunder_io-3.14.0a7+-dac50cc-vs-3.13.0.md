# Results vs. 3.13.0

- fork: JelleZijlstra
- ref: sunder_io
- machine: windows-amd64
- commit hash: dac50cc
- commit date: 2025-04-25
- overall geometric mean: 1.024x faster
- HPT reliability: 97.82%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                    |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                  |
| sphinx         | 617 ms                                                      | 644 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                       | 1.04x slower                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                    |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.33x faster                                                    |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                    |
| async_tree_io_tg           | 497 ms                                                      | 395 ms: 1.26x faster                                                    |
| async_tree_io              | 513 ms                                                      | 413 ms: 1.24x faster                                                    |
| async_tree_none            | 219 ms                                                      | 183 ms: 1.20x faster                                                    |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.17x faster                                                    |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                    |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 338 ms: 1.13x faster                                                    |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                                    |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 42.8 ms: 1.19x faster                                                   |
| nbody          | 66.3 ms                                                     | 63.0 ms: 1.05x faster                                                   |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                       | 1.07x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.9 ms: 1.71x faster                                                   |
| regex_effbot   | 1.69 ms                                                     | 1.43 ms: 1.18x faster                                                   |
| regex_compile  | 80.7 ms                                                     | 81.5 ms: 1.01x slower                                                   |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                       | 1.19x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.9 ms: 1.04x faster                                                   |
| json_loads           | 15.1 us                                                     | 15.4 us: 1.02x slower                                                   |
| tomli_loads          | 1.37 sec                                                    | 1.42 sec: 1.03x slower                                                  |
| xml_etree_generate   | 53.5 ms                                                     | 55.6 ms: 1.04x slower                                                   |
| unpickle_pure_python | 130 us                                                      | 135 us: 1.04x slower                                                    |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.3 ms: 1.06x slower                                                   |
| xml_etree_process    | 36.5 ms                                                     | 40.0 ms: 1.10x slower                                                   |
| json_dumps           | 6.19 ms                                                     | 6.90 ms: 1.11x slower                                                   |
| pickle_pure_python   | 186 us                                                      | 210 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                   |
| python_startup_no_site | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.68 ms: 1.02x slower                                                   |
| genshi_text     | 15.2 ms                                                     | 15.6 ms: 1.02x slower                                                   |
| django_template | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                   |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.5 ms: 2.31x faster                                                   |
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                    |
| mdp                        | 1.43 sec                                                    | 789 ms: 1.81x faster                                                    |
| regex_v8                   | 23.8 ms                                                     | 13.9 ms: 1.71x faster                                                   |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.33x faster                                                    |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                    |
| deepcopy                   | 223 us                                                      | 175 us: 1.27x faster                                                    |
| async_tree_io_tg           | 497 ms                                                      | 395 ms: 1.26x faster                                                    |
| deepcopy_memo              | 23.1 us                                                     | 18.6 us: 1.24x faster                                                   |
| async_tree_io              | 513 ms                                                      | 413 ms: 1.24x faster                                                    |
| async_tree_none            | 219 ms                                                      | 183 ms: 1.20x faster                                                    |
| float                      | 50.8 ms                                                     | 42.8 ms: 1.19x faster                                                   |
| regex_effbot               | 1.69 ms                                                     | 1.43 ms: 1.18x faster                                                   |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.17x faster                                                    |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                    |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 338 ms: 1.13x faster                                                    |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.12x faster                                                   |
| spectral_norm              | 63.4 ms                                                     | 57.8 ms: 1.10x faster                                                   |
| json                       | 3.30 ms                                                     | 3.06 ms: 1.08x faster                                                   |
| go                         | 84.7 ms                                                     | 79.0 ms: 1.07x faster                                                   |
| telco                      | 4.85 ms                                                     | 4.60 ms: 1.05x faster                                                   |
| nbody                      | 66.3 ms                                                     | 63.0 ms: 1.05x faster                                                   |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.49 ms: 1.05x faster                                                   |
| xml_etree_parse            | 92.2 ms                                                     | 88.9 ms: 1.04x faster                                                   |
| bpe_tokeniser              | 2.87 sec                                                    | 2.84 sec: 1.01x faster                                                  |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.3 ms: 1.01x faster                                                   |
| scimark_fft                | 175 ms                                                      | 176 ms: 1.01x slower                                                    |
| pyflate                    | 283 ms                                                      | 285 ms: 1.01x slower                                                    |
| generators                 | 19.0 ms                                                     | 19.1 ms: 1.01x slower                                                   |
| logging_silent             | 54.6 ns                                                     | 55.1 ns: 1.01x slower                                                   |
| regex_compile              | 80.7 ms                                                     | 81.5 ms: 1.01x slower                                                   |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                    |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.01x slower                                                    |
| create_gc_cycles           | 1.22 ms                                                     | 1.24 ms: 1.01x slower                                                   |
| fannkuch                   | 252 ms                                                      | 255 ms: 1.02x slower                                                    |
| json_loads                 | 15.1 us                                                     | 15.4 us: 1.02x slower                                                   |
| mako                       | 6.56 ms                                                     | 6.68 ms: 1.02x slower                                                   |
| chaos                      | 37.9 ms                                                     | 38.6 ms: 1.02x slower                                                   |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.02x slower                                                   |
| genshi_text                | 15.2 ms                                                     | 15.6 ms: 1.02x slower                                                   |
| shortest_path              | 355 ms                                                      | 364 ms: 1.02x slower                                                    |
| scimark_sor                | 76.2 ms                                                     | 78.1 ms: 1.03x slower                                                   |
| pprint_safe_repr           | 485 ms                                                      | 499 ms: 1.03x slower                                                    |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                    |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                    |
| meteor_contest             | 72.0 ms                                                     | 74.1 ms: 1.03x slower                                                   |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                                    |
| sympy_expand               | 286 ms                                                      | 295 ms: 1.03x slower                                                    |
| pprint_pformat             | 977 ms                                                      | 1.01 sec: 1.03x slower                                                  |
| tomli_loads                | 1.37 sec                                                    | 1.42 sec: 1.03x slower                                                  |
| typing_runtime_protocols   | 103 us                                                      | 107 us: 1.04x slower                                                    |
| sympy_sum                  | 85.2 ms                                                     | 88.3 ms: 1.04x slower                                                   |
| xml_etree_generate         | 53.5 ms                                                     | 55.6 ms: 1.04x slower                                                   |
| unpickle_pure_python       | 130 us                                                      | 135 us: 1.04x slower                                                    |
| scimark_lu                 | 56.7 ms                                                     | 59.1 ms: 1.04x slower                                                   |
| connected_components       | 320 ms                                                      | 334 ms: 1.04x slower                                                    |
| sphinx                     | 617 ms                                                      | 644 ms: 1.04x slower                                                    |
| crypto_pyaes               | 45.6 ms                                                     | 47.7 ms: 1.05x slower                                                   |
| gc_traversal               | 1.96 ms                                                     | 2.07 ms: 1.05x slower                                                   |
| richards                   | 26.3 ms                                                     | 27.7 ms: 1.05x slower                                                   |
| richards_super             | 29.8 ms                                                     | 31.5 ms: 1.06x slower                                                   |
| bench_mp_pool              | 84.2 ms                                                     | 89.4 ms: 1.06x slower                                                   |
| dulwich_log                | 40.1 ms                                                     | 42.6 ms: 1.06x slower                                                   |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.3 ms: 1.06x slower                                                   |
| hexiom                     | 3.84 ms                                                     | 4.13 ms: 1.08x slower                                                   |
| comprehensions             | 10.4 us                                                     | 11.2 us: 1.08x slower                                                   |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                  |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                   |
| python_startup             | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                   |
| logging_simple             | 5.77 us                                                     | 6.32 us: 1.09x slower                                                   |
| nqueens                    | 56.1 ms                                                     | 61.5 ms: 1.10x slower                                                   |
| xml_etree_process          | 36.5 ms                                                     | 40.0 ms: 1.10x slower                                                   |
| logging_format             | 6.18 us                                                     | 6.81 us: 1.10x slower                                                   |
| bench_thread_pool          | 810 us                                                      | 894 us: 1.10x slower                                                    |
| json_dumps                 | 6.19 ms                                                     | 6.90 ms: 1.11x slower                                                   |
| pickle_pure_python         | 186 us                                                      | 210 us: 1.13x slower                                                    |
| coverage                   | 45.3 ms                                                     | 51.5 ms: 1.14x slower                                                   |
| raytrace                   | 153 ms                                                      | 175 ms: 1.14x slower                                                    |
| python_startup_no_site     | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                   |
| deltablue                  | 1.89 ms                                                     | 2.19 ms: 1.16x slower                                                   |
| django_template            | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                   |
| many_optionals             | 361 us                                                      | 430 us: 1.19x slower                                                    |
| subparsers                 | 10.9 ms                                                     | 16.1 ms: 1.48x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                            |

Benchmark hidden because not significant (6): pylint, sqlite_synth, html5lib, k_core, genshi_xml, pycparser
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250425-3.14.0a7+-dac50cc/bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.024x faster

# HPT report

- Reliability score: 97.82% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown