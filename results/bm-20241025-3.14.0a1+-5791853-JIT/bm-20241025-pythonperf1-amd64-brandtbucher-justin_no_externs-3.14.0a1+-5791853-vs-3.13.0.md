# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-amd64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.023x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 253 ms: 1.15x slower                                                           |
| docutils       | 1.57 sec                                                    | 1.94 sec: 1.23x slower                                                         |
| html5lib       | 38.9 ms                                                     | 40.6 ms: 1.04x slower                                                          |
| sphinx         | 633 ms                                                      | 784 ms: 1.24x slower                                                           |
| tornado_http   | 93.0 ms                                                     | 98.6 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                       | 1.14x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 262 ms: 1.10x faster                                                           |
| async_tree_none            | 226 ms                                                      | 219 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 390 ms: 1.02x slower                                                           |
| async_tree_none_tg         | 209 ms                                                      | 215 ms: 1.03x slower                                                           |
| async_tree_io              | 521 ms                                                      | 550 ms: 1.06x slower                                                           |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 407 ms: 1.08x slower                                                           |
| coroutines                 | 12.8 ms                                                     | 14.4 ms: 1.13x slower                                                          |
| async_generators           | 223 ms                                                      | 267 ms: 1.20x slower                                                           |
| async_tree_io_tg           | 518 ms                                                      | 643 ms: 1.24x slower                                                           |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                                   |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 51.9 ms: 1.32x faster                                                          |
| float          | 49.9 ms                                                     | 48.1 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.4 ms: 1.39x faster                                                          |
| regex_effbot   | 1.58 ms                                                     | 1.63 ms: 1.03x slower                                                          |
| regex_dna      | 115 ms                                                      | 122 ms: 1.05x slower                                                           |
| regex_compile  | 80.5 ms                                                     | 92.7 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.31 sec: 1.06x faster                                                         |
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                          |
| xml_etree_generate   | 54.0 ms                                                     | 51.2 ms: 1.05x faster                                                          |
| xml_etree_process    | 37.0 ms                                                     | 36.5 ms: 1.01x faster                                                          |
| xml_etree_parse      | 93.6 ms                                                     | 95.7 ms: 1.02x slower                                                          |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.3 ms: 1.02x slower                                                          |
| pickle_pure_python   | 190 us                                                      | 199 us: 1.05x slower                                                           |
| unpickle_pure_python | 133 us                                                      | 145 us: 1.09x slower                                                           |
| json_dumps           | 5.92 ms                                                     | 6.47 ms: 1.09x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 24.2 ms: 1.05x faster                                                          |
| python_startup_no_site | 18.1 ms                                                     | 18.4 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.20 ms: 1.22x faster                                                          |
| django_template | 22.4 ms                                                     | 27.0 ms: 1.21x slower                                                          |
| genshi_text     | 15.6 ms                                                     | 20.0 ms: 1.28x slower                                                          |
| genshi_xml      | 35.5 ms                                                     | 49.1 ms: 1.38x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 521 us: 16.87x faster                                                          |
| regex_v8                   | 21.4 ms                                                     | 15.4 ms: 1.39x faster                                                          |
| deepcopy_memo              | 23.3 us                                                     | 16.9 us: 1.38x faster                                                          |
| nbody                      | 68.4 ms                                                     | 51.9 ms: 1.32x faster                                                          |
| mako                       | 6.35 ms                                                     | 5.20 ms: 1.22x faster                                                          |
| spectral_norm              | 62.8 ms                                                     | 53.9 ms: 1.17x faster                                                          |
| deepcopy                   | 226 us                                                      | 195 us: 1.16x faster                                                           |
| scimark_sor                | 76.2 ms                                                     | 67.0 ms: 1.14x faster                                                          |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.20 ms: 1.12x faster                                                          |
| async_tree_memoization_tg  | 288 ms                                                      | 262 ms: 1.10x faster                                                           |
| deepcopy_reduce            | 2.06 us                                                     | 1.87 us: 1.10x faster                                                          |
| scimark_monte_carlo        | 40.8 ms                                                     | 38.0 ms: 1.07x faster                                                          |
| scimark_fft                | 172 ms                                                      | 161 ms: 1.07x faster                                                           |
| crypto_pyaes               | 45.4 ms                                                     | 42.5 ms: 1.07x faster                                                          |
| pprint_pformat             | 999 ms                                                      | 941 ms: 1.06x faster                                                           |
| tomli_loads                | 1.39 sec                                                    | 1.31 sec: 1.06x faster                                                         |
| json                       | 3.19 ms                                                     | 3.01 ms: 1.06x faster                                                          |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                          |
| xml_etree_generate         | 54.0 ms                                                     | 51.2 ms: 1.05x faster                                                          |
| python_startup             | 25.4 ms                                                     | 24.2 ms: 1.05x faster                                                          |
| pprint_safe_repr           | 494 ms                                                      | 470 ms: 1.05x faster                                                           |
| float                      | 49.9 ms                                                     | 48.1 ms: 1.04x faster                                                          |
| async_tree_none            | 226 ms                                                      | 219 ms: 1.03x faster                                                           |
| fannkuch                   | 253 ms                                                      | 248 ms: 1.02x faster                                                           |
| telco                      | 4.79 ms                                                     | 4.72 ms: 1.01x faster                                                          |
| xml_etree_process          | 37.0 ms                                                     | 36.5 ms: 1.01x faster                                                          |
| dulwich_log                | 40.8 ms                                                     | 41.3 ms: 1.01x slower                                                          |
| python_startup_no_site     | 18.1 ms                                                     | 18.4 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 390 ms: 1.02x slower                                                           |
| xml_etree_parse            | 93.6 ms                                                     | 95.7 ms: 1.02x slower                                                          |
| xml_etree_iterparse        | 61.8 ms                                                     | 63.3 ms: 1.02x slower                                                          |
| logging_simple             | 5.96 us                                                     | 6.12 us: 1.03x slower                                                          |
| async_tree_none_tg         | 209 ms                                                      | 215 ms: 1.03x slower                                                           |
| regex_effbot               | 1.58 ms                                                     | 1.63 ms: 1.03x slower                                                          |
| logging_silent             | 54.6 ns                                                     | 56.4 ns: 1.03x slower                                                          |
| bench_mp_pool              | 86.4 ms                                                     | 89.9 ms: 1.04x slower                                                          |
| html5lib                   | 38.9 ms                                                     | 40.6 ms: 1.04x slower                                                          |
| coverage                   | 45.6 ms                                                     | 47.7 ms: 1.05x slower                                                          |
| pickle_pure_python         | 190 us                                                      | 199 us: 1.05x slower                                                           |
| logging_format             | 6.26 us                                                     | 6.59 us: 1.05x slower                                                          |
| meteor_contest             | 73.5 ms                                                     | 77.5 ms: 1.05x slower                                                          |
| regex_dna                  | 115 ms                                                      | 122 ms: 1.05x slower                                                           |
| async_tree_io              | 521 ms                                                      | 550 ms: 1.06x slower                                                           |
| tornado_http               | 93.0 ms                                                     | 98.6 ms: 1.06x slower                                                          |
| pyflate                    | 283 ms                                                      | 303 ms: 1.07x slower                                                           |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 407 ms: 1.08x slower                                                           |
| go                         | 87.0 ms                                                     | 94.0 ms: 1.08x slower                                                          |
| unpickle_pure_python       | 133 us                                                      | 145 us: 1.09x slower                                                           |
| pycparser                  | 683 ms                                                      | 744 ms: 1.09x slower                                                           |
| json_dumps                 | 5.92 ms                                                     | 6.47 ms: 1.09x slower                                                          |
| mdp                        | 1.39 sec                                                    | 1.54 sec: 1.11x slower                                                         |
| create_gc_cycles           | 1.26 ms                                                     | 1.40 ms: 1.11x slower                                                          |
| scimark_lu                 | 53.0 ms                                                     | 59.0 ms: 1.11x slower                                                          |
| typing_runtime_protocols   | 105 us                                                      | 118 us: 1.12x slower                                                           |
| chaos                      | 38.5 ms                                                     | 43.3 ms: 1.12x slower                                                          |
| coroutines                 | 12.8 ms                                                     | 14.4 ms: 1.13x slower                                                          |
| sympy_expand               | 291 ms                                                      | 330 ms: 1.13x slower                                                           |
| nqueens                    | 56.7 ms                                                     | 64.7 ms: 1.14x slower                                                          |
| 2to3                       | 221 ms                                                      | 253 ms: 1.15x slower                                                           |
| regex_compile              | 80.5 ms                                                     | 92.7 ms: 1.15x slower                                                          |
| generators                 | 19.5 ms                                                     | 22.5 ms: 1.15x slower                                                          |
| sympy_str                  | 169 ms                                                      | 195 ms: 1.16x slower                                                           |
| comprehensions             | 10.3 us                                                     | 12.1 us: 1.18x slower                                                          |
| async_generators           | 223 ms                                                      | 267 ms: 1.20x slower                                                           |
| sqlglot_normalize          | 175 ms                                                      | 210 ms: 1.20x slower                                                           |
| sqlglot_parse              | 771 us                                                      | 931 us: 1.21x slower                                                           |
| django_template            | 22.4 ms                                                     | 27.0 ms: 1.21x slower                                                          |
| sympy_sum                  | 86.9 ms                                                     | 106 ms: 1.22x slower                                                           |
| docutils                   | 1.57 sec                                                    | 1.94 sec: 1.23x slower                                                         |
| sphinx                     | 633 ms                                                      | 784 ms: 1.24x slower                                                           |
| deltablue                  | 1.92 ms                                                     | 2.38 ms: 1.24x slower                                                          |
| async_tree_io_tg           | 518 ms                                                      | 643 ms: 1.24x slower                                                           |
| sympy_integrate            | 12.5 ms                                                     | 15.8 ms: 1.27x slower                                                          |
| sqlglot_transpile          | 956 us                                                      | 1.21 ms: 1.27x slower                                                          |
| richards_super             | 30.9 ms                                                     | 39.5 ms: 1.28x slower                                                          |
| genshi_text                | 15.6 ms                                                     | 20.0 ms: 1.28x slower                                                          |
| richards                   | 27.3 ms                                                     | 35.5 ms: 1.30x slower                                                          |
| raytrace                   | 160 ms                                                      | 208 ms: 1.30x slower                                                           |
| sqlglot_optimize           | 32.9 ms                                                     | 43.9 ms: 1.33x slower                                                          |
| pylint                     | 211 ms                                                      | 284 ms: 1.35x slower                                                           |
| genshi_xml                 | 35.5 ms                                                     | 49.1 ms: 1.38x slower                                                          |
| hexiom                     | 3.89 ms                                                     | 5.43 ms: 1.39x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                   |

Benchmark hidden because not significant (5): bench_thread_pool, gc_traversal, pathlib, pidigits, async_tree_memoization
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.023x slower
# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown