# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-amd64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.019x slower
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 248 ms: 1.12x slower                                                           |
| docutils       | 1.57 sec                                                    | 1.93 sec: 1.23x slower                                                         |
| html5lib       | 38.9 ms                                                     | 39.8 ms: 1.02x slower                                                          |
| sphinx         | 633 ms                                                      | 781 ms: 1.23x slower                                                           |
| tornado_http   | 93.0 ms                                                     | 99.0 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                       | 1.13x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 260 ms: 1.11x faster                                                           |
| async_tree_none            | 226 ms                                                      | 216 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 399 ms: 1.06x slower                                                           |
| async_tree_io              | 521 ms                                                      | 553 ms: 1.06x slower                                                           |
| coroutines                 | 12.8 ms                                                     | 14.0 ms: 1.10x slower                                                          |
| async_generators           | 223 ms                                                      | 270 ms: 1.21x slower                                                           |
| async_tree_io_tg           | 518 ms                                                      | 640 ms: 1.24x slower                                                           |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                                   |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 56.2 ms: 1.22x faster                                                          |
| float          | 49.9 ms                                                     | 48.3 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.7 ms: 1.46x faster                                                          |
| regex_effbot   | 1.58 ms                                                     | 1.56 ms: 1.01x faster                                                          |
| regex_compile  | 80.5 ms                                                     | 92.5 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.30 sec: 1.07x faster                                                         |
| xml_etree_generate   | 54.0 ms                                                     | 51.7 ms: 1.04x faster                                                          |
| json_loads           | 15.1 us                                                     | 14.6 us: 1.03x faster                                                          |
| xml_etree_process    | 37.0 ms                                                     | 36.7 ms: 1.01x faster                                                          |
| xml_etree_parse      | 93.6 ms                                                     | 95.8 ms: 1.02x slower                                                          |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.8 ms: 1.03x slower                                                          |
| pickle_pure_python   | 190 us                                                      | 204 us: 1.08x slower                                                           |
| unpickle_pure_python | 133 us                                                      | 147 us: 1.10x slower                                                           |
| json_dumps           | 5.92 ms                                                     | 6.62 ms: 1.12x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 24.4 ms: 1.04x faster                                                          |
| python_startup_no_site | 18.1 ms                                                     | 18.4 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.14 ms: 1.24x faster                                                          |
| django_template | 22.4 ms                                                     | 27.0 ms: 1.21x slower                                                          |
| genshi_text     | 15.6 ms                                                     | 19.6 ms: 1.26x slower                                                          |
| genshi_xml      | 35.5 ms                                                     | 46.8 ms: 1.32x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 525 us: 16.76x faster                                                          |
| regex_v8                   | 21.4 ms                                                     | 14.7 ms: 1.46x faster                                                          |
| deepcopy_memo              | 23.3 us                                                     | 17.0 us: 1.37x faster                                                          |
| mako                       | 6.35 ms                                                     | 5.14 ms: 1.24x faster                                                          |
| nbody                      | 68.4 ms                                                     | 56.2 ms: 1.22x faster                                                          |
| spectral_norm              | 62.8 ms                                                     | 53.6 ms: 1.17x faster                                                          |
| deepcopy                   | 226 us                                                      | 196 us: 1.15x faster                                                           |
| scimark_sor                | 76.2 ms                                                     | 67.9 ms: 1.12x faster                                                          |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.20 ms: 1.12x faster                                                          |
| async_tree_memoization_tg  | 288 ms                                                      | 260 ms: 1.11x faster                                                           |
| pprint_safe_repr           | 494 ms                                                      | 453 ms: 1.09x faster                                                           |
| fannkuch                   | 253 ms                                                      | 234 ms: 1.08x faster                                                           |
| deepcopy_reduce            | 2.06 us                                                     | 1.92 us: 1.07x faster                                                          |
| tomli_loads                | 1.39 sec                                                    | 1.30 sec: 1.07x faster                                                         |
| crypto_pyaes               | 45.4 ms                                                     | 42.8 ms: 1.06x faster                                                          |
| json                       | 3.19 ms                                                     | 3.01 ms: 1.06x faster                                                          |
| pprint_pformat             | 999 ms                                                      | 945 ms: 1.06x faster                                                           |
| scimark_fft                | 172 ms                                                      | 163 ms: 1.05x faster                                                           |
| async_tree_none            | 226 ms                                                      | 216 ms: 1.04x faster                                                           |
| xml_etree_generate         | 54.0 ms                                                     | 51.7 ms: 1.04x faster                                                          |
| python_startup             | 25.4 ms                                                     | 24.4 ms: 1.04x faster                                                          |
| scimark_monte_carlo        | 40.8 ms                                                     | 39.4 ms: 1.04x faster                                                          |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.03x faster                                                          |
| float                      | 49.9 ms                                                     | 48.3 ms: 1.03x faster                                                          |
| xml_etree_process          | 37.0 ms                                                     | 36.7 ms: 1.01x faster                                                          |
| regex_effbot               | 1.58 ms                                                     | 1.56 ms: 1.01x faster                                                          |
| python_startup_no_site     | 18.1 ms                                                     | 18.4 ms: 1.01x slower                                                          |
| html5lib                   | 38.9 ms                                                     | 39.8 ms: 1.02x slower                                                          |
| xml_etree_parse            | 93.6 ms                                                     | 95.8 ms: 1.02x slower                                                          |
| meteor_contest             | 73.5 ms                                                     | 75.7 ms: 1.03x slower                                                          |
| xml_etree_iterparse        | 61.8 ms                                                     | 63.8 ms: 1.03x slower                                                          |
| coverage                   | 45.6 ms                                                     | 47.2 ms: 1.04x slower                                                          |
| bench_mp_pool              | 86.4 ms                                                     | 89.6 ms: 1.04x slower                                                          |
| logging_simple             | 5.96 us                                                     | 6.22 us: 1.04x slower                                                          |
| logging_silent             | 54.6 ns                                                     | 57.6 ns: 1.05x slower                                                          |
| pycparser                  | 683 ms                                                      | 722 ms: 1.06x slower                                                           |
| pyflate                    | 283 ms                                                      | 300 ms: 1.06x slower                                                           |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 399 ms: 1.06x slower                                                           |
| async_tree_io              | 521 ms                                                      | 553 ms: 1.06x slower                                                           |
| tornado_http               | 93.0 ms                                                     | 99.0 ms: 1.06x slower                                                          |
| logging_format             | 6.26 us                                                     | 6.73 us: 1.07x slower                                                          |
| pickle_pure_python         | 190 us                                                      | 204 us: 1.08x slower                                                           |
| go                         | 87.0 ms                                                     | 94.0 ms: 1.08x slower                                                          |
| coroutines                 | 12.8 ms                                                     | 14.0 ms: 1.10x slower                                                          |
| create_gc_cycles           | 1.26 ms                                                     | 1.39 ms: 1.10x slower                                                          |
| unpickle_pure_python       | 133 us                                                      | 147 us: 1.10x slower                                                           |
| scimark_lu                 | 53.0 ms                                                     | 58.4 ms: 1.10x slower                                                          |
| sympy_expand               | 291 ms                                                      | 325 ms: 1.12x slower                                                           |
| json_dumps                 | 5.92 ms                                                     | 6.62 ms: 1.12x slower                                                          |
| 2to3                       | 221 ms                                                      | 248 ms: 1.12x slower                                                           |
| chaos                      | 38.5 ms                                                     | 43.2 ms: 1.12x slower                                                          |
| nqueens                    | 56.7 ms                                                     | 63.7 ms: 1.12x slower                                                          |
| typing_runtime_protocols   | 105 us                                                      | 119 us: 1.13x slower                                                           |
| comprehensions             | 10.3 us                                                     | 11.8 us: 1.15x slower                                                          |
| regex_compile              | 80.5 ms                                                     | 92.5 ms: 1.15x slower                                                          |
| sympy_str                  | 169 ms                                                      | 194 ms: 1.15x slower                                                           |
| mdp                        | 1.39 sec                                                    | 1.62 sec: 1.17x slower                                                         |
| sqlglot_parse              | 771 us                                                      | 908 us: 1.18x slower                                                           |
| generators                 | 19.5 ms                                                     | 23.0 ms: 1.18x slower                                                          |
| sympy_sum                  | 86.9 ms                                                     | 104 ms: 1.20x slower                                                           |
| sqlglot_normalize          | 175 ms                                                      | 211 ms: 1.21x slower                                                           |
| django_template            | 22.4 ms                                                     | 27.0 ms: 1.21x slower                                                          |
| async_generators           | 223 ms                                                      | 270 ms: 1.21x slower                                                           |
| deltablue                  | 1.92 ms                                                     | 2.35 ms: 1.22x slower                                                          |
| docutils                   | 1.57 sec                                                    | 1.93 sec: 1.23x slower                                                         |
| sphinx                     | 633 ms                                                      | 781 ms: 1.23x slower                                                           |
| async_tree_io_tg           | 518 ms                                                      | 640 ms: 1.24x slower                                                           |
| richards_super             | 30.9 ms                                                     | 38.3 ms: 1.24x slower                                                          |
| sympy_integrate            | 12.5 ms                                                     | 15.7 ms: 1.25x slower                                                          |
| richards                   | 27.3 ms                                                     | 34.2 ms: 1.25x slower                                                          |
| sqlglot_transpile          | 956 us                                                      | 1.20 ms: 1.25x slower                                                          |
| genshi_text                | 15.6 ms                                                     | 19.6 ms: 1.26x slower                                                          |
| raytrace                   | 160 ms                                                      | 207 ms: 1.29x slower                                                           |
| genshi_xml                 | 35.5 ms                                                     | 46.8 ms: 1.32x slower                                                          |
| sqlglot_optimize           | 32.9 ms                                                     | 43.7 ms: 1.33x slower                                                          |
| pylint                     | 211 ms                                                      | 283 ms: 1.34x slower                                                           |
| hexiom                     | 3.89 ms                                                     | 5.33 ms: 1.37x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                   |

Benchmark hidden because not significant (10): dulwich_log, telco, regex_dna, pathlib, gc_traversal, async_tree_cpu_io_mixed, bench_thread_pool, pidigits, async_tree_none_tg, async_tree_memoization
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.019x slower
# HPT report

- Reliability score: 99.83% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown