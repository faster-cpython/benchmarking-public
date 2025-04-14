# Results vs. 3.13.0

- fork: mdboom
- ref: msvc_musttail_aa
- machine: windows-amd64
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.301x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 309 ms: 1.44x slower                                                    |
| docutils       | 1.53 sec                                                    | 2.31 sec: 1.51x slower                                                  |
| html5lib       | 38.2 ms                                                     | 52.5 ms: 1.38x slower                                                   |
| sphinx         | 617 ms                                                      | 933 ms: 1.51x slower                                                    |
| Geometric mean | (ref)                                                       | 1.46x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 304 ms: 1.08x slower                                                    |
| asyncio_websockets         | 300 ms                                                      | 330 ms: 1.10x slower                                                    |
| async_tree_io              | 513 ms                                                      | 570 ms: 1.11x slower                                                    |
| async_tree_io_tg           | 497 ms                                                      | 576 ms: 1.16x slower                                                    |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 444 ms: 1.16x slower                                                    |
| async_tree_memoization     | 265 ms                                                      | 313 ms: 1.18x slower                                                    |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 455 ms: 1.20x slower                                                    |
| async_tree_none_tg         | 200 ms                                                      | 243 ms: 1.22x slower                                                    |
| async_tree_none            | 219 ms                                                      | 267 ms: 1.22x slower                                                    |
| async_generators           | 223 ms                                                      | 348 ms: 1.56x slower                                                    |
| coroutines                 | 12.5 ms                                                     | 22.4 ms: 1.79x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.24x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 156 ms: 1.07x slower                                                    |
| float          | 50.8 ms                                                     | 78.0 ms: 1.53x slower                                                   |
| nbody          | 66.3 ms                                                     | 103 ms: 1.56x slower                                                    |
| Geometric mean | (ref)                                                       | 1.37x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 17.5 ms: 1.36x faster                                                   |
| regex_dna      | 115 ms                                                      | 123 ms: 1.07x slower                                                    |
| regex_effbot   | 1.69 ms                                                     | 1.87 ms: 1.10x slower                                                   |
| regex_compile  | 80.7 ms                                                     | 130 ms: 1.61x slower                                                    |
| Geometric mean | (ref)                                                       | 1.09x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 112 ms: 1.22x slower                                                    |
| tomli_loads          | 1.37 sec                                                    | 2.07 sec: 1.51x slower                                                  |
| json_dumps           | 6.19 ms                                                     | 9.44 ms: 1.53x slower                                                   |
| json_loads           | 15.1 us                                                     | 23.3 us: 1.54x slower                                                   |
| xml_etree_iterparse  | 60.5 ms                                                     | 94.3 ms: 1.56x slower                                                   |
| xml_etree_generate   | 53.5 ms                                                     | 92.6 ms: 1.73x slower                                                   |
| xml_etree_process    | 36.5 ms                                                     | 66.9 ms: 1.83x slower                                                   |
| pickle_pure_python   | 186 us                                                      | 364 us: 1.96x slower                                                    |
| unpickle_pure_python | 130 us                                                      | 284 us: 2.18x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.65x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 29.5 ms: 1.21x slower                                                   |
| python_startup_no_site | 16.9 ms                                                     | 22.0 ms: 1.30x slower                                                   |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 50.4 ms: 1.49x slower                                                   |
| genshi_text     | 15.2 ms                                                     | 23.9 ms: 1.57x slower                                                   |
| mako            | 6.56 ms                                                     | 12.1 ms: 1.84x slower                                                   |
| django_template | 20.3 ms                                                     | 38.0 ms: 1.87x slower                                                   |
| Geometric mean  | (ref)                                                       | 1.68x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 710 us: 11.92x faster                                                   |
| pathlib                    | 75.3 ms                                                     | 37.5 ms: 2.01x faster                                                   |
| regex_v8                   | 23.8 ms                                                     | 17.5 ms: 1.36x faster                                                   |
| pidigits                   | 146 ms                                                      | 156 ms: 1.07x slower                                                    |
| regex_dna                  | 115 ms                                                      | 123 ms: 1.07x slower                                                    |
| async_tree_memoization_tg  | 281 ms                                                      | 304 ms: 1.08x slower                                                    |
| asyncio_websockets         | 300 ms                                                      | 330 ms: 1.10x slower                                                    |
| regex_effbot               | 1.69 ms                                                     | 1.87 ms: 1.10x slower                                                   |
| async_tree_io              | 513 ms                                                      | 570 ms: 1.11x slower                                                    |
| async_tree_io_tg           | 497 ms                                                      | 576 ms: 1.16x slower                                                    |
| create_gc_cycles           | 1.22 ms                                                     | 1.42 ms: 1.16x slower                                                   |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 444 ms: 1.16x slower                                                    |
| async_tree_memoization     | 265 ms                                                      | 313 ms: 1.18x slower                                                    |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 455 ms: 1.20x slower                                                    |
| bench_mp_pool              | 84.2 ms                                                     | 101 ms: 1.20x slower                                                    |
| python_startup             | 24.4 ms                                                     | 29.5 ms: 1.21x slower                                                   |
| async_tree_none_tg         | 200 ms                                                      | 243 ms: 1.22x slower                                                    |
| async_tree_none            | 219 ms                                                      | 267 ms: 1.22x slower                                                    |
| xml_etree_parse            | 92.2 ms                                                     | 112 ms: 1.22x slower                                                    |
| shortest_path              | 355 ms                                                      | 437 ms: 1.23x slower                                                    |
| sqlite_synth               | 1.59 us                                                     | 1.96 us: 1.23x slower                                                   |
| json                       | 3.30 ms                                                     | 4.07 ms: 1.23x slower                                                   |
| connected_components       | 320 ms                                                      | 395 ms: 1.23x slower                                                    |
| deepcopy                   | 223 us                                                      | 278 us: 1.24x slower                                                    |
| k_core                     | 1.70 sec                                                    | 2.18 sec: 1.28x slower                                                  |
| python_startup_no_site     | 16.9 ms                                                     | 22.0 ms: 1.30x slower                                                   |
| dulwich_log                | 40.1 ms                                                     | 52.4 ms: 1.31x slower                                                   |
| pylint                     | 205 ms                                                      | 269 ms: 1.31x slower                                                    |
| mdp                        | 1.43 sec                                                    | 1.89 sec: 1.32x slower                                                  |
| telco                      | 4.85 ms                                                     | 6.56 ms: 1.35x slower                                                   |
| html5lib                   | 38.2 ms                                                     | 52.5 ms: 1.38x slower                                                   |
| meteor_contest             | 72.0 ms                                                     | 99.5 ms: 1.38x slower                                                   |
| coverage                   | 45.3 ms                                                     | 63.7 ms: 1.41x slower                                                   |
| deepcopy_reduce            | 2.02 us                                                     | 2.86 us: 1.42x slower                                                   |
| 2to3                       | 215 ms                                                      | 309 ms: 1.44x slower                                                    |
| sympy_sum                  | 85.2 ms                                                     | 123 ms: 1.45x slower                                                    |
| pycparser                  | 695 ms                                                      | 1.01 sec: 1.46x slower                                                  |
| sympy_expand               | 286 ms                                                      | 419 ms: 1.47x slower                                                    |
| deepcopy_memo              | 23.1 us                                                     | 34.0 us: 1.47x slower                                                   |
| sympy_str                  | 167 ms                                                      | 247 ms: 1.48x slower                                                    |
| genshi_xml                 | 33.9 ms                                                     | 50.4 ms: 1.49x slower                                                   |
| sympy_integrate            | 12.3 ms                                                     | 18.4 ms: 1.49x slower                                                   |
| typing_runtime_protocols   | 103 us                                                      | 154 us: 1.49x slower                                                    |
| docutils                   | 1.53 sec                                                    | 2.31 sec: 1.51x slower                                                  |
| tomli_loads                | 1.37 sec                                                    | 2.07 sec: 1.51x slower                                                  |
| sphinx                     | 617 ms                                                      | 933 ms: 1.51x slower                                                    |
| json_dumps                 | 6.19 ms                                                     | 9.44 ms: 1.53x slower                                                   |
| float                      | 50.8 ms                                                     | 78.0 ms: 1.53x slower                                                   |
| json_loads                 | 15.1 us                                                     | 23.3 us: 1.54x slower                                                   |
| bpe_tokeniser              | 2.87 sec                                                    | 4.45 sec: 1.55x slower                                                  |
| many_optionals             | 361 us                                                      | 559 us: 1.55x slower                                                    |
| xml_etree_iterparse        | 60.5 ms                                                     | 94.3 ms: 1.56x slower                                                   |
| nbody                      | 66.3 ms                                                     | 103 ms: 1.56x slower                                                    |
| async_generators           | 223 ms                                                      | 348 ms: 1.56x slower                                                    |
| genshi_text                | 15.2 ms                                                     | 23.9 ms: 1.57x slower                                                   |
| bench_thread_pool          | 810 us                                                      | 1.28 ms: 1.57x slower                                                   |
| scimark_fft                | 175 ms                                                      | 276 ms: 1.58x slower                                                    |
| spectral_norm              | 63.4 ms                                                     | 102 ms: 1.60x slower                                                    |
| logging_format             | 6.18 us                                                     | 9.92 us: 1.61x slower                                                   |
| regex_compile              | 80.7 ms                                                     | 130 ms: 1.61x slower                                                    |
| logging_simple             | 5.77 us                                                     | 9.30 us: 1.61x slower                                                   |
| gc_traversal               | 1.96 ms                                                     | 3.25 ms: 1.66x slower                                                   |
| go                         | 84.7 ms                                                     | 140 ms: 1.66x slower                                                    |
| fannkuch                   | 252 ms                                                      | 418 ms: 1.66x slower                                                    |
| pyflate                    | 283 ms                                                      | 477 ms: 1.69x slower                                                    |
| pprint_pformat             | 977 ms                                                      | 1.66 sec: 1.70x slower                                                  |
| pprint_safe_repr           | 485 ms                                                      | 825 ms: 1.70x slower                                                    |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 4.43 ms: 1.70x slower                                                   |
| nqueens                    | 56.1 ms                                                     | 96.9 ms: 1.73x slower                                                   |
| xml_etree_generate         | 53.5 ms                                                     | 92.6 ms: 1.73x slower                                                   |
| crypto_pyaes               | 45.6 ms                                                     | 80.1 ms: 1.76x slower                                                   |
| coroutines                 | 12.5 ms                                                     | 22.4 ms: 1.79x slower                                                   |
| scimark_sor                | 76.2 ms                                                     | 139 ms: 1.82x slower                                                    |
| chaos                      | 37.9 ms                                                     | 69.3 ms: 1.83x slower                                                   |
| xml_etree_process          | 36.5 ms                                                     | 66.9 ms: 1.83x slower                                                   |
| mako                       | 6.56 ms                                                     | 12.1 ms: 1.84x slower                                                   |
| scimark_monte_carlo        | 40.7 ms                                                     | 75.8 ms: 1.86x slower                                                   |
| django_template            | 20.3 ms                                                     | 38.0 ms: 1.87x slower                                                   |
| generators                 | 19.0 ms                                                     | 35.6 ms: 1.87x slower                                                   |
| hexiom                     | 3.84 ms                                                     | 7.44 ms: 1.94x slower                                                   |
| comprehensions             | 10.4 us                                                     | 20.1 us: 1.94x slower                                                   |
| pickle_pure_python         | 186 us                                                      | 364 us: 1.96x slower                                                    |
| subparsers                 | 10.9 ms                                                     | 21.5 ms: 1.98x slower                                                   |
| raytrace                   | 153 ms                                                      | 313 ms: 2.04x slower                                                    |
| scimark_lu                 | 56.7 ms                                                     | 119 ms: 2.11x slower                                                    |
| unpickle_pure_python       | 130 us                                                      | 284 us: 2.18x slower                                                    |
| deltablue                  | 1.89 ms                                                     | 4.22 ms: 2.23x slower                                                   |
| richards                   | 26.3 ms                                                     | 59.0 ms: 2.25x slower                                                   |
| richards_super             | 29.8 ms                                                     | 67.7 ms: 2.27x slower                                                   |
| logging_silent             | 54.6 ns                                                     | 124 ns: 2.28x slower                                                    |
| Geometric mean             | (ref)                                                       | 1.44x slower                                                            |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250310-3.14.0a5+-90d131f/bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.301x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.43x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.35x

# Memory
- memory change: unknown