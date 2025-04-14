# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: windows-amd64
- commit hash: d270553
- commit date: 2025-02-20
- overall geometric mean: 1.052x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 231 ms: 1.07x slower                                                           |
| docutils       | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                                         |
| html5lib       | 38.2 ms                                                     | 41.2 ms: 1.08x slower                                                          |
| sphinx         | 617 ms                                                      | 670 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 228 ms: 1.23x faster                                                           |
| async_tree_io              | 513 ms                                                      | 444 ms: 1.16x faster                                                           |
| async_tree_memoization     | 265 ms                                                      | 234 ms: 1.13x faster                                                           |
| async_tree_io_tg           | 497 ms                                                      | 444 ms: 1.12x faster                                                           |
| async_tree_none            | 219 ms                                                      | 199 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 350 ms: 1.09x faster                                                           |
| async_tree_none_tg         | 200 ms                                                      | 186 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 355 ms: 1.07x faster                                                           |
| asyncio_websockets         | 300 ms                                                      | 308 ms: 1.03x slower                                                           |
| async_generators           | 223 ms                                                      | 236 ms: 1.06x slower                                                           |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 51.5 ms: 1.01x slower                                                          |
| pidigits       | 146 ms                                                      | 151 ms: 1.03x slower                                                           |
| nbody          | 66.3 ms                                                     | 78.4 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 15.2 ms: 1.57x faster                                                          |
| regex_effbot   | 1.69 ms                                                     | 1.49 ms: 1.14x faster                                                          |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                                           |
| regex_compile  | 80.7 ms                                                     | 92.9 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 91.2 ms: 1.01x faster                                                          |
| xml_etree_iterparse  | 60.5 ms                                                     | 65.7 ms: 1.09x slower                                                          |
| xml_etree_generate   | 53.5 ms                                                     | 61.2 ms: 1.14x slower                                                          |
| json_dumps           | 6.19 ms                                                     | 7.11 ms: 1.15x slower                                                          |
| tomli_loads          | 1.37 sec                                                    | 1.62 sec: 1.18x slower                                                         |
| xml_etree_process    | 36.5 ms                                                     | 44.2 ms: 1.21x slower                                                          |
| unpickle_pure_python | 130 us                                                      | 170 us: 1.30x slower                                                           |
| pickle_pure_python   | 186 us                                                      | 244 us: 1.31x slower                                                           |
| Geometric mean       | (ref)                                                       | 1.15x slower                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                          |
| python_startup_no_site | 16.9 ms                                                     | 19.1 ms: 1.13x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 17.6 ms: 1.16x slower                                                          |
| genshi_xml      | 33.9 ms                                                     | 39.5 ms: 1.17x slower                                                          |
| mako            | 6.56 ms                                                     | 8.26 ms: 1.26x slower                                                          |
| django_template | 20.3 ms                                                     | 27.3 ms: 1.34x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.23x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 539 us: 15.71x faster                                                          |
| pathlib                    | 75.3 ms                                                     | 30.0 ms: 2.51x faster                                                          |
| regex_v8                   | 23.8 ms                                                     | 15.2 ms: 1.57x faster                                                          |
| async_tree_memoization_tg  | 281 ms                                                      | 228 ms: 1.23x faster                                                           |
| async_tree_io              | 513 ms                                                      | 444 ms: 1.16x faster                                                           |
| regex_effbot               | 1.69 ms                                                     | 1.49 ms: 1.14x faster                                                          |
| deepcopy                   | 223 us                                                      | 198 us: 1.13x faster                                                           |
| async_tree_memoization     | 265 ms                                                      | 234 ms: 1.13x faster                                                           |
| async_tree_io_tg           | 497 ms                                                      | 444 ms: 1.12x faster                                                           |
| async_tree_none            | 219 ms                                                      | 199 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 350 ms: 1.09x faster                                                           |
| async_tree_none_tg         | 200 ms                                                      | 186 ms: 1.07x faster                                                           |
| json                       | 3.30 ms                                                     | 3.08 ms: 1.07x faster                                                          |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 355 ms: 1.07x faster                                                           |
| deepcopy_memo              | 23.1 us                                                     | 22.4 us: 1.03x faster                                                          |
| xml_etree_parse            | 92.2 ms                                                     | 91.2 ms: 1.01x faster                                                          |
| sqlite_synth               | 1.59 us                                                     | 1.60 us: 1.01x slower                                                          |
| float                      | 50.8 ms                                                     | 51.5 ms: 1.01x slower                                                          |
| bench_mp_pool              | 84.2 ms                                                     | 85.5 ms: 1.01x slower                                                          |
| shortest_path              | 355 ms                                                      | 362 ms: 1.02x slower                                                           |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.03x slower                                                           |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                                          |
| asyncio_websockets         | 300 ms                                                      | 308 ms: 1.03x slower                                                           |
| gc_traversal               | 1.96 ms                                                     | 2.02 ms: 1.03x slower                                                          |
| k_core                     | 1.70 sec                                                    | 1.75 sec: 1.03x slower                                                         |
| pidigits                   | 146 ms                                                      | 151 ms: 1.03x slower                                                           |
| telco                      | 4.85 ms                                                     | 5.01 ms: 1.03x slower                                                          |
| deepcopy_reduce            | 2.02 us                                                     | 2.09 us: 1.03x slower                                                          |
| python_startup             | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                          |
| connected_components       | 320 ms                                                      | 334 ms: 1.04x slower                                                           |
| dulwich_log                | 40.1 ms                                                     | 42.1 ms: 1.05x slower                                                          |
| spectral_norm              | 63.4 ms                                                     | 66.7 ms: 1.05x slower                                                          |
| async_generators           | 223 ms                                                      | 236 ms: 1.06x slower                                                           |
| coverage                   | 45.3 ms                                                     | 48.3 ms: 1.07x slower                                                          |
| bench_thread_pool          | 810 us                                                      | 869 us: 1.07x slower                                                           |
| 2to3                       | 215 ms                                                      | 231 ms: 1.07x slower                                                           |
| bpe_tokeniser              | 2.87 sec                                                    | 3.09 sec: 1.08x slower                                                         |
| html5lib                   | 38.2 ms                                                     | 41.2 ms: 1.08x slower                                                          |
| sphinx                     | 617 ms                                                      | 670 ms: 1.08x slower                                                           |
| xml_etree_iterparse        | 60.5 ms                                                     | 65.7 ms: 1.09x slower                                                          |
| sympy_str                  | 167 ms                                                      | 182 ms: 1.09x slower                                                           |
| sympy_sum                  | 85.2 ms                                                     | 92.8 ms: 1.09x slower                                                          |
| sympy_expand               | 286 ms                                                      | 311 ms: 1.09x slower                                                           |
| meteor_contest             | 72.0 ms                                                     | 78.7 ms: 1.09x slower                                                          |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.91 ms: 1.12x slower                                                          |
| docutils                   | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                                         |
| sympy_integrate            | 12.3 ms                                                     | 13.8 ms: 1.12x slower                                                          |
| typing_runtime_protocols   | 103 us                                                      | 115 us: 1.12x slower                                                           |
| go                         | 84.7 ms                                                     | 94.8 ms: 1.12x slower                                                          |
| mdp                        | 1.43 sec                                                    | 1.62 sec: 1.13x slower                                                         |
| python_startup_no_site     | 16.9 ms                                                     | 19.1 ms: 1.13x slower                                                          |
| pycparser                  | 695 ms                                                      | 786 ms: 1.13x slower                                                           |
| sqlglot_optimize           | 32.5 ms                                                     | 37.2 ms: 1.14x slower                                                          |
| xml_etree_generate         | 53.5 ms                                                     | 61.2 ms: 1.14x slower                                                          |
| json_dumps                 | 6.19 ms                                                     | 7.11 ms: 1.15x slower                                                          |
| regex_compile              | 80.7 ms                                                     | 92.9 ms: 1.15x slower                                                          |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                          |
| genshi_text                | 15.2 ms                                                     | 17.6 ms: 1.16x slower                                                          |
| genshi_xml                 | 33.9 ms                                                     | 39.5 ms: 1.17x slower                                                          |
| sqlglot_normalize          | 172 ms                                                      | 203 ms: 1.18x slower                                                           |
| tomli_loads                | 1.37 sec                                                    | 1.62 sec: 1.18x slower                                                         |
| nbody                      | 66.3 ms                                                     | 78.4 ms: 1.18x slower                                                          |
| scimark_fft                | 175 ms                                                      | 210 ms: 1.20x slower                                                           |
| logging_format             | 6.18 us                                                     | 7.43 us: 1.20x slower                                                          |
| logging_simple             | 5.77 us                                                     | 6.95 us: 1.20x slower                                                          |
| chaos                      | 37.9 ms                                                     | 45.9 ms: 1.21x slower                                                          |
| xml_etree_process          | 36.5 ms                                                     | 44.2 ms: 1.21x slower                                                          |
| pyflate                    | 283 ms                                                      | 344 ms: 1.22x slower                                                           |
| many_optionals             | 361 us                                                      | 441 us: 1.22x slower                                                           |
| scimark_sor                | 76.2 ms                                                     | 93.3 ms: 1.22x slower                                                          |
| sqlglot_transpile          | 953 us                                                      | 1.17 ms: 1.23x slower                                                          |
| pprint_safe_repr           | 485 ms                                                      | 596 ms: 1.23x slower                                                           |
| pprint_pformat             | 977 ms                                                      | 1.20 sec: 1.23x slower                                                         |
| hexiom                     | 3.84 ms                                                     | 4.75 ms: 1.24x slower                                                          |
| scimark_monte_carlo        | 40.7 ms                                                     | 50.5 ms: 1.24x slower                                                          |
| crypto_pyaes               | 45.6 ms                                                     | 56.6 ms: 1.24x slower                                                          |
| sqlglot_parse              | 764 us                                                      | 954 us: 1.25x slower                                                           |
| comprehensions             | 10.4 us                                                     | 13.0 us: 1.26x slower                                                          |
| mako                       | 6.56 ms                                                     | 8.26 ms: 1.26x slower                                                          |
| fannkuch                   | 252 ms                                                      | 317 ms: 1.26x slower                                                           |
| deltablue                  | 1.89 ms                                                     | 2.39 ms: 1.26x slower                                                          |
| richards_super             | 29.8 ms                                                     | 37.8 ms: 1.27x slower                                                          |
| richards                   | 26.3 ms                                                     | 33.4 ms: 1.27x slower                                                          |
| logging_silent             | 54.6 ns                                                     | 69.6 ns: 1.28x slower                                                          |
| nqueens                    | 56.1 ms                                                     | 71.8 ms: 1.28x slower                                                          |
| raytrace                   | 153 ms                                                      | 197 ms: 1.28x slower                                                           |
| scimark_lu                 | 56.7 ms                                                     | 73.9 ms: 1.30x slower                                                          |
| unpickle_pure_python       | 130 us                                                      | 170 us: 1.30x slower                                                           |
| pickle_pure_python         | 186 us                                                      | 244 us: 1.31x slower                                                           |
| django_template            | 20.3 ms                                                     | 27.3 ms: 1.34x slower                                                          |
| subparsers                 | 10.9 ms                                                     | 16.9 ms: 1.56x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                                   |

Benchmark hidden because not significant (3): pylint, json_loads, create_gc_cycles
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.052x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown