# Results vs. 3.13.0

- fork: faster-cpython
- ref: c_recursion_limit
- machine: windows-amd64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.021x faster
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                               |
| docutils       | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                             |
| html5lib       | 38.2 ms                                                     | 39.9 ms: 1.05x slower                                                              |
| sphinx         | 617 ms                                                      | 643 ms: 1.04x slower                                                               |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.29x faster                                                               |
| async_tree_io              | 513 ms                                                      | 411 ms: 1.25x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 407 ms: 1.22x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                               |
| async_tree_none            | 219 ms                                                      | 188 ms: 1.17x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 176 ms: 1.14x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 344 ms: 1.11x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                               |
| async_generators           | 223 ms                                                      | 218 ms: 1.02x faster                                                               |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.3 ms: 1.12x faster                                                              |
| pidigits       | 146 ms                                                      | 150 ms: 1.03x slower                                                               |
| nbody          | 66.3 ms                                                     | 71.2 ms: 1.07x slower                                                              |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.4 ms: 1.66x faster                                                              |
| regex_effbot   | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                              |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                               |
| regex_compile  | 80.7 ms                                                     | 85.1 ms: 1.05x slower                                                              |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                              |
| xml_etree_parse      | 92.2 ms                                                     | 91.1 ms: 1.01x faster                                                              |
| tomli_loads          | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                             |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.2 ms: 1.04x slower                                                              |
| xml_etree_generate   | 53.5 ms                                                     | 56.5 ms: 1.06x slower                                                              |
| json_dumps           | 6.19 ms                                                     | 6.64 ms: 1.07x slower                                                              |
| xml_etree_process    | 36.5 ms                                                     | 40.5 ms: 1.11x slower                                                              |
| unpickle_pure_python | 130 us                                                      | 145 us: 1.11x slower                                                               |
| pickle_pure_python   | 186 us                                                      | 219 us: 1.18x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 24.8 ms: 1.02x slower                                                              |
| python_startup_no_site | 16.9 ms                                                     | 18.6 ms: 1.10x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.66 ms: 1.01x slower                                                              |
| genshi_xml      | 33.9 ms                                                     | 35.3 ms: 1.04x slower                                                              |
| genshi_text     | 15.2 ms                                                     | 16.5 ms: 1.08x slower                                                              |
| django_template | 20.3 ms                                                     | 25.5 ms: 1.26x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 514 us: 16.49x faster                                                              |
| pathlib                    | 75.3 ms                                                     | 29.1 ms: 2.59x faster                                                              |
| regex_v8                   | 23.8 ms                                                     | 14.4 ms: 1.66x faster                                                              |
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.29x faster                                                               |
| async_tree_io              | 513 ms                                                      | 411 ms: 1.25x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 407 ms: 1.22x faster                                                               |
| deepcopy                   | 223 us                                                      | 184 us: 1.21x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                               |
| deepcopy_memo              | 23.1 us                                                     | 19.7 us: 1.17x faster                                                              |
| regex_effbot               | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                              |
| async_tree_none            | 219 ms                                                      | 188 ms: 1.17x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 176 ms: 1.14x faster                                                               |
| json                       | 3.30 ms                                                     | 2.91 ms: 1.13x faster                                                              |
| float                      | 50.8 ms                                                     | 45.3 ms: 1.12x faster                                                              |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 344 ms: 1.11x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                               |
| spectral_norm              | 63.4 ms                                                     | 57.6 ms: 1.10x faster                                                              |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                              |
| deepcopy_reduce            | 2.02 us                                                     | 1.91 us: 1.06x faster                                                              |
| telco                      | 4.85 ms                                                     | 4.71 ms: 1.03x faster                                                              |
| bpe_tokeniser              | 2.87 sec                                                    | 2.80 sec: 1.03x faster                                                             |
| async_generators           | 223 ms                                                      | 218 ms: 1.02x faster                                                               |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.01x faster                                                              |
| xml_etree_parse            | 92.2 ms                                                     | 91.1 ms: 1.01x faster                                                              |
| shortest_path              | 355 ms                                                      | 351 ms: 1.01x faster                                                               |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                               |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.59 ms: 1.01x faster                                                              |
| coverage                   | 45.3 ms                                                     | 45.2 ms: 1.00x faster                                                              |
| connected_components       | 320 ms                                                      | 322 ms: 1.01x slower                                                               |
| mdp                        | 1.43 sec                                                    | 1.44 sec: 1.01x slower                                                             |
| mako                       | 6.56 ms                                                     | 6.66 ms: 1.01x slower                                                              |
| python_startup             | 24.4 ms                                                     | 24.8 ms: 1.02x slower                                                              |
| tomli_loads                | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                             |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                              |
| dulwich_log                | 40.1 ms                                                     | 41.1 ms: 1.02x slower                                                              |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                               |
| pidigits                   | 146 ms                                                      | 150 ms: 1.03x slower                                                               |
| sympy_sum                  | 85.2 ms                                                     | 88.2 ms: 1.04x slower                                                              |
| typing_runtime_protocols   | 103 us                                                      | 107 us: 1.04x slower                                                               |
| sympy_str                  | 167 ms                                                      | 173 ms: 1.04x slower                                                               |
| sympy_expand               | 286 ms                                                      | 296 ms: 1.04x slower                                                               |
| sphinx                     | 617 ms                                                      | 643 ms: 1.04x slower                                                               |
| scimark_fft                | 175 ms                                                      | 182 ms: 1.04x slower                                                               |
| genshi_xml                 | 33.9 ms                                                     | 35.3 ms: 1.04x slower                                                              |
| pycparser                  | 695 ms                                                      | 726 ms: 1.04x slower                                                               |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.2 ms: 1.04x slower                                                              |
| html5lib                   | 38.2 ms                                                     | 39.9 ms: 1.05x slower                                                              |
| bench_thread_pool          | 810 us                                                      | 853 us: 1.05x slower                                                               |
| regex_compile              | 80.7 ms                                                     | 85.1 ms: 1.05x slower                                                              |
| xml_etree_generate         | 53.5 ms                                                     | 56.5 ms: 1.06x slower                                                              |
| meteor_contest             | 72.0 ms                                                     | 76.4 ms: 1.06x slower                                                              |
| crypto_pyaes               | 45.6 ms                                                     | 48.5 ms: 1.06x slower                                                              |
| scimark_lu                 | 56.7 ms                                                     | 60.3 ms: 1.06x slower                                                              |
| comprehensions             | 10.4 us                                                     | 11.0 us: 1.06x slower                                                              |
| sympy_integrate            | 12.3 ms                                                     | 13.2 ms: 1.07x slower                                                              |
| docutils                   | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                             |
| json_dumps                 | 6.19 ms                                                     | 6.64 ms: 1.07x slower                                                              |
| nbody                      | 66.3 ms                                                     | 71.2 ms: 1.07x slower                                                              |
| logging_silent             | 54.6 ns                                                     | 58.8 ns: 1.08x slower                                                              |
| sqlglot_optimize           | 32.5 ms                                                     | 35.0 ms: 1.08x slower                                                              |
| pyflate                    | 283 ms                                                      | 305 ms: 1.08x slower                                                               |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.0 ms: 1.08x slower                                                              |
| genshi_text                | 15.2 ms                                                     | 16.5 ms: 1.08x slower                                                              |
| scimark_sor                | 76.2 ms                                                     | 83.3 ms: 1.09x slower                                                              |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                              |
| chaos                      | 37.9 ms                                                     | 41.5 ms: 1.10x slower                                                              |
| hexiom                     | 3.84 ms                                                     | 4.22 ms: 1.10x slower                                                              |
| logging_simple             | 5.77 us                                                     | 6.35 us: 1.10x slower                                                              |
| logging_format             | 6.18 us                                                     | 6.81 us: 1.10x slower                                                              |
| python_startup_no_site     | 16.9 ms                                                     | 18.6 ms: 1.10x slower                                                              |
| fannkuch                   | 252 ms                                                      | 278 ms: 1.11x slower                                                               |
| pprint_pformat             | 977 ms                                                      | 1.08 sec: 1.11x slower                                                             |
| nqueens                    | 56.1 ms                                                     | 62.3 ms: 1.11x slower                                                              |
| xml_etree_process          | 36.5 ms                                                     | 40.5 ms: 1.11x slower                                                              |
| pprint_safe_repr           | 485 ms                                                      | 539 ms: 1.11x slower                                                               |
| richards                   | 26.3 ms                                                     | 29.2 ms: 1.11x slower                                                              |
| unpickle_pure_python       | 130 us                                                      | 145 us: 1.11x slower                                                               |
| sqlglot_normalize          | 172 ms                                                      | 193 ms: 1.12x slower                                                               |
| richards_super             | 29.8 ms                                                     | 33.6 ms: 1.13x slower                                                              |
| sqlglot_transpile          | 953 us                                                      | 1.08 ms: 1.13x slower                                                              |
| deltablue                  | 1.89 ms                                                     | 2.14 ms: 1.13x slower                                                              |
| sqlglot_parse              | 764 us                                                      | 873 us: 1.14x slower                                                               |
| pickle_pure_python         | 186 us                                                      | 219 us: 1.18x slower                                                               |
| many_optionals             | 361 us                                                      | 428 us: 1.19x slower                                                               |
| django_template            | 20.3 ms                                                     | 25.5 ms: 1.26x slower                                                              |
| raytrace                   | 153 ms                                                      | 194 ms: 1.26x slower                                                               |
| subparsers                 | 10.9 ms                                                     | 16.0 ms: 1.47x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                       |

Benchmark hidden because not significant (7): pylint, create_gc_cycles, bench_mp_pool, go, asyncio_websockets, k_core, gc_traversal
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.021x faster

# HPT report

- Reliability score: 99.76% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown