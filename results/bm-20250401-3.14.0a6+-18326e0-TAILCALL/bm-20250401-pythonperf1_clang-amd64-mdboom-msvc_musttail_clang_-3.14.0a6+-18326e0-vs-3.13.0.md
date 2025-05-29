# Results vs. 3.13.0

- fork: mdboom
- ref: msvc_musttail_clang_
- machine: windows-amd64
- commit hash: 18326e0
- commit date: 2025-04-01
- overall geometric mean: 1.171x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 207 ms: 1.04x faster                                                        |
| docutils       | 1.53 sec                                                    | 1.56 sec: 1.02x slower                                                      |
| html5lib       | 38.2 ms                                                     | 34.9 ms: 1.09x faster                                                       |
| sphinx         | 617 ms                                                      | 603 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                        |
| async_tree_io              | 513 ms                                                      | 353 ms: 1.45x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 197 ms: 1.43x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 351 ms: 1.42x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 187 ms: 1.41x faster                                                        |
| async_tree_none            | 219 ms                                                      | 159 ms: 1.38x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 150 ms: 1.33x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 313 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 316 ms: 1.21x faster                                                        |
| async_generators           | 223 ms                                                      | 187 ms: 1.19x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 10.7 ms: 1.16x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 36.9 ms: 1.38x faster                                                       |
| nbody          | 66.3 ms                                                     | 49.1 ms: 1.35x faster                                                       |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.0 ms: 1.84x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 69.8 ms: 1.16x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 107 us: 1.21x faster                                                        |
| json_dumps           | 6.19 ms                                                     | 5.66 ms: 1.09x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 49.1 ms: 1.09x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 34.0 ms: 1.07x faster                                                       |
| pickle_pure_python   | 186 us                                                      | 173 us: 1.07x faster                                                        |
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 89.4 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.5 ms: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.9 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 11.9 ms: 1.28x faster                                                       |
| genshi_xml      | 33.9 ms                                                     | 29.0 ms: 1.17x faster                                                       |
| mako            | 6.56 ms                                                     | 5.83 ms: 1.13x faster                                                       |
| django_template | 20.3 ms                                                     | 21.3 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 30.7 ms: 2.45x faster                                                       |
| mdp                        | 1.43 sec                                                    | 682 ms: 2.10x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.0 ms: 1.84x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 14.0 us: 1.65x faster                                                       |
| deepcopy                   | 223 us                                                      | 144 us: 1.55x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 49.3 ms: 1.55x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 42.8 ms: 1.48x faster                                                       |
| async_tree_io              | 513 ms                                                      | 353 ms: 1.45x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 197 ms: 1.43x faster                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 28.6 ms: 1.42x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 351 ms: 1.42x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 187 ms: 1.41x faster                                                        |
| async_tree_none            | 219 ms                                                      | 159 ms: 1.38x faster                                                        |
| float                      | 50.8 ms                                                     | 36.9 ms: 1.38x faster                                                       |
| go                         | 84.7 ms                                                     | 61.5 ms: 1.38x faster                                                       |
| nbody                      | 66.3 ms                                                     | 49.1 ms: 1.35x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.52 us: 1.33x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 150 ms: 1.33x faster                                                        |
| logging_silent             | 54.6 ns                                                     | 41.1 ns: 1.33x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 1.99 ms: 1.31x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 43.5 ms: 1.30x faster                                                       |
| hexiom                     | 3.84 ms                                                     | 2.98 ms: 1.29x faster                                                       |
| generators                 | 19.0 ms                                                     | 14.8 ms: 1.29x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 11.9 ms: 1.28x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                      |
| scimark_fft                | 175 ms                                                      | 139 ms: 1.25x faster                                                        |
| fannkuch                   | 252 ms                                                      | 207 ms: 1.22x faster                                                        |
| unpickle_pure_python       | 130 us                                                      | 107 us: 1.21x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 313 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 316 ms: 1.21x faster                                                        |
| pyflate                    | 283 ms                                                      | 234 ms: 1.21x faster                                                        |
| chaos                      | 37.9 ms                                                     | 31.4 ms: 1.21x faster                                                       |
| comprehensions             | 10.4 us                                                     | 8.64 us: 1.20x faster                                                       |
| async_generators           | 223 ms                                                      | 187 ms: 1.19x faster                                                        |
| typing_runtime_protocols   | 103 us                                                      | 87.6 us: 1.18x faster                                                       |
| json                       | 3.30 ms                                                     | 2.81 ms: 1.17x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 835 ms: 1.17x faster                                                        |
| pprint_safe_repr           | 485 ms                                                      | 415 ms: 1.17x faster                                                        |
| genshi_xml                 | 33.9 ms                                                     | 29.0 ms: 1.17x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 10.7 ms: 1.16x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 69.8 ms: 1.16x faster                                                       |
| deltablue                  | 1.89 ms                                                     | 1.64 ms: 1.15x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 39.9 ms: 1.14x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.25 ms: 1.14x faster                                                       |
| coverage                   | 45.3 ms                                                     | 39.8 ms: 1.14x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.55 sec: 1.13x faster                                                      |
| nqueens                    | 56.1 ms                                                     | 49.8 ms: 1.13x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.83 ms: 1.13x faster                                                       |
| sympy_str                  | 167 ms                                                      | 149 ms: 1.12x faster                                                        |
| sympy_expand               | 286 ms                                                      | 256 ms: 1.12x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                       |
| sympy_integrate            | 12.3 ms                                                     | 11.2 ms: 1.10x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.66 ms: 1.09x faster                                                       |
| pylint                     | 205 ms                                                      | 188 ms: 1.09x faster                                                        |
| html5lib                   | 38.2 ms                                                     | 34.9 ms: 1.09x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 49.1 ms: 1.09x faster                                                       |
| raytrace                   | 153 ms                                                      | 142 ms: 1.08x faster                                                        |
| meteor_contest             | 72.0 ms                                                     | 66.8 ms: 1.08x faster                                                       |
| sympy_sum                  | 85.2 ms                                                     | 79.2 ms: 1.08x faster                                                       |
| pycparser                  | 695 ms                                                      | 647 ms: 1.08x faster                                                        |
| xml_etree_process          | 36.5 ms                                                     | 34.0 ms: 1.07x faster                                                       |
| pickle_pure_python         | 186 us                                                      | 173 us: 1.07x faster                                                        |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 38.0 ms: 1.05x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.51 us: 1.05x faster                                                       |
| logging_simple             | 5.77 us                                                     | 5.55 us: 1.04x faster                                                       |
| 2to3                       | 215 ms                                                      | 207 ms: 1.04x faster                                                        |
| logging_format             | 6.18 us                                                     | 5.96 us: 1.04x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.4 ms: 1.03x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.66 sec: 1.02x faster                                                      |
| sphinx                     | 617 ms                                                      | 603 ms: 1.02x faster                                                        |
| shortest_path              | 355 ms                                                      | 351 ms: 1.01x faster                                                        |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                        |
| richards_super             | 29.8 ms                                                     | 30.2 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.5 ms: 1.02x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.56 sec: 1.02x slower                                                      |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| connected_components       | 320 ms                                                      | 329 ms: 1.03x slower                                                        |
| django_template            | 20.3 ms                                                     | 21.3 ms: 1.05x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 88.6 ms: 1.05x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.36 ms: 1.11x slower                                                       |
| many_optionals             | 361 us                                                      | 409 us: 1.13x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 20.9 ms: 1.24x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.76 ms: 1.40x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 15.3 ms: 1.41x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.17x faster                                                                |

Benchmark hidden because not significant (2): richards, bench_thread_pool
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250401-3.14.0a6+-18326e0-CLANG/bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.171x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown