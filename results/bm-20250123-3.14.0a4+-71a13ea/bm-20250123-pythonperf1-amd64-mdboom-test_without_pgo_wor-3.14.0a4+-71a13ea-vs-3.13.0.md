# Results vs. 3.13.0

- fork: mdboom
- ref: test_without_pgo_wor
- machine: windows-amd64
- commit hash: 71a13ea
- commit date: 2025-01-23
- overall geometric mean: 1.039x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 235 ms: 1.09x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.1 ms: 1.05x slower                                                       |
| sphinx         | 617 ms                                                      | 666 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.31x faster                                                        |
| async_tree_io              | 513 ms                                                      | 419 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 410 ms: 1.21x faster                                                        |
| async_tree_none            | 219 ms                                                      | 189 ms: 1.16x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 230 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 176 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 348 ms: 1.09x faster                                                        |
| async_generators           | 223 ms                                                      | 231 ms: 1.03x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 315 ms: 1.05x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 15.1 ms: 1.21x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 147 ms: 1.00x slower                                                        |
| float          | 50.8 ms                                                     | 52.4 ms: 1.03x slower                                                       |
| nbody          | 66.3 ms                                                     | 77.5 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 15.1 ms: 1.58x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.50 ms: 1.13x faster                                                       |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                        |
| regex_compile  | 80.7 ms                                                     | 89.6 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 89.7 ms: 1.03x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.9 ms: 1.07x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.83 ms: 1.10x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 59.9 ms: 1.12x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 43.6 ms: 1.19x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 165 us: 1.27x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 244 us: 1.31x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.9 ms                                                     | 18.1 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 36.0 ms: 1.06x slower                                                       |
| mako            | 6.56 ms                                                     | 7.07 ms: 1.08x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.8 ms: 1.11x slower                                                       |
| django_template | 20.3 ms                                                     | 26.1 ms: 1.29x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 546 us: 15.50x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 15.1 ms: 1.58x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.31x faster                                                        |
| async_tree_io              | 513 ms                                                      | 419 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 410 ms: 1.21x faster                                                        |
| deepcopy                   | 223 us                                                      | 192 us: 1.16x faster                                                        |
| async_tree_none            | 219 ms                                                      | 189 ms: 1.16x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 230 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 176 ms: 1.14x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.50 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                        |
| json                       | 3.30 ms                                                     | 3.01 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 348 ms: 1.09x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 21.7 us: 1.06x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.95 us: 1.04x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.19 ms: 1.03x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.7 ms: 1.03x faster                                                       |
| shortest_path              | 355 ms                                                      | 352 ms: 1.01x faster                                                        |
| connected_components       | 320 ms                                                      | 317 ms: 1.01x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.81 ms: 1.01x faster                                                       |
| pidigits                   | 146 ms                                                      | 147 ms: 1.00x slower                                                        |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                                        |
| spectral_norm              | 63.4 ms                                                     | 64.5 ms: 1.02x slower                                                       |
| k_core                     | 1.70 sec                                                    | 1.73 sec: 1.02x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.67 ms: 1.02x slower                                                       |
| float                      | 50.8 ms                                                     | 52.4 ms: 1.03x slower                                                       |
| async_generators           | 223 ms                                                      | 231 ms: 1.03x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 41.5 ms: 1.04x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 840 us: 1.04x slower                                                        |
| pathlib                    | 75.3 ms                                                     | 78.4 ms: 1.04x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.01 sec: 1.05x slower                                                      |
| asyncio_websockets         | 300 ms                                                      | 315 ms: 1.05x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 40.1 ms: 1.05x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 88.6 ms: 1.05x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 36.0 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.9 ms: 1.07x slower                                                       |
| pycparser                  | 695 ms                                                      | 746 ms: 1.07x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 18.1 ms: 1.07x slower                                                       |
| mako                       | 6.56 ms                                                     | 7.07 ms: 1.08x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 91.7 ms: 1.08x slower                                                       |
| sphinx                     | 617 ms                                                      | 666 ms: 1.08x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 49.3 ms: 1.08x slower                                                       |
| sympy_expand               | 286 ms                                                      | 310 ms: 1.08x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 78.0 ms: 1.08x slower                                                       |
| sympy_str                  | 167 ms                                                      | 181 ms: 1.09x slower                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.72 us: 1.09x slower                                                       |
| 2to3                       | 215 ms                                                      | 235 ms: 1.09x slower                                                        |
| json_dumps                 | 6.19 ms                                                     | 6.83 ms: 1.10x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 16.8 ms: 1.11x slower                                                       |
| go                         | 84.7 ms                                                     | 93.9 ms: 1.11x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 89.6 ms: 1.11x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 115 us: 1.11x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 13.7 ms: 1.11x slower                                                       |
| coverage                   | 45.3 ms                                                     | 50.4 ms: 1.11x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                                      |
| scimark_fft                | 175 ms                                                      | 195 ms: 1.12x slower                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 59.9 ms: 1.12x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.62 sec: 1.13x slower                                                      |
| sqlglot_optimize           | 32.5 ms                                                     | 36.8 ms: 1.13x slower                                                       |
| logging_format             | 6.18 us                                                     | 7.00 us: 1.13x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.58 us: 1.14x slower                                                       |
| pyflate                    | 283 ms                                                      | 323 ms: 1.14x slower                                                        |
| fannkuch                   | 252 ms                                                      | 290 ms: 1.15x slower                                                        |
| chaos                      | 37.9 ms                                                     | 43.7 ms: 1.15x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 65.2 ms: 1.16x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 566 ms: 1.17x slower                                                        |
| nbody                      | 66.3 ms                                                     | 77.5 ms: 1.17x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.14 sec: 1.17x slower                                                      |
| sqlglot_normalize          | 172 ms                                                      | 202 ms: 1.18x slower                                                        |
| generators                 | 19.0 ms                                                     | 22.4 ms: 1.18x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.13 ms: 1.18x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 909 us: 1.19x slower                                                        |
| xml_etree_process          | 36.5 ms                                                     | 43.6 ms: 1.19x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 15.1 ms: 1.21x slower                                                       |
| many_optionals             | 361 us                                                      | 440 us: 1.22x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 69.4 ms: 1.22x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.72 ms: 1.23x slower                                                       |
| comprehensions             | 10.4 us                                                     | 12.7 us: 1.23x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 50.9 ms: 1.25x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 95.4 ms: 1.25x slower                                                       |
| richards_super             | 29.8 ms                                                     | 37.4 ms: 1.26x slower                                                       |
| richards                   | 26.3 ms                                                     | 33.3 ms: 1.27x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 165 us: 1.27x slower                                                        |
| django_template            | 20.3 ms                                                     | 26.1 ms: 1.29x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.43 ms: 1.29x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 244 us: 1.31x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 73.0 ns: 1.34x slower                                                       |
| raytrace                   | 153 ms                                                      | 210 ms: 1.37x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.2 ms: 1.49x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (3): pylint, python_startup, gc_traversal
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.039x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown