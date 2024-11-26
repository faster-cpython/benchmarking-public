# Results vs. 3.13.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: windows-amd64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.003x slower
- HPT reliability: 97.97%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 251 ms: 1.14x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.88 sec: 1.20x slower                                                      |
| sphinx         | 633 ms                                                      | 762 ms: 1.20x slower                                                        |
| Geometric mean | (ref)                                                       | 1.13x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 261 ms: 1.11x faster                                                        |
| async_tree_none            | 226 ms                                                      | 210 ms: 1.08x faster                                                        |
| async_tree_memoization     | 276 ms                                                      | 262 ms: 1.05x faster                                                        |
| asyncio_websockets         | 318 ms                                                      | 309 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 391 ms: 1.02x slower                                                        |
| async_tree_none_tg         | 209 ms                                                      | 218 ms: 1.05x slower                                                        |
| async_tree_io              | 521 ms                                                      | 546 ms: 1.05x slower                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 403 ms: 1.07x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.7 ms: 1.07x slower                                                       |
| async_generators           | 223 ms                                                      | 259 ms: 1.16x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 627 ms: 1.21x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 53.2 ms: 1.29x faster                                                       |
| float          | 49.9 ms                                                     | 47.4 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.5 ms: 1.38x faster                                                       |
| regex_effbot   | 1.58 ms                                                     | 1.61 ms: 1.02x slower                                                       |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| regex_compile  | 80.5 ms                                                     | 90.9 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.27 sec: 1.10x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                       |
| xml_etree_generate   | 54.0 ms                                                     | 51.0 ms: 1.06x faster                                                       |
| xml_etree_process    | 37.0 ms                                                     | 36.0 ms: 1.03x faster                                                       |
| xml_etree_parse      | 93.6 ms                                                     | 94.4 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.2 ms: 1.02x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 144 us: 1.08x slower                                                        |
| json_dumps           | 5.92 ms                                                     | 6.42 ms: 1.09x slower                                                       |
| pickle_pure_python   | 190 us                                                      | 207 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 24.9 ms: 1.02x faster                                                       |
| python_startup_no_site | 18.1 ms                                                     | 18.8 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.04 ms: 1.26x faster                                                       |
| django_template | 22.4 ms                                                     | 26.7 ms: 1.19x slower                                                       |
| genshi_text     | 15.6 ms                                                     | 19.2 ms: 1.23x slower                                                       |
| genshi_xml      | 35.5 ms                                                     | 45.5 ms: 1.28x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 524 us: 16.79x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 16.6 us: 1.41x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 15.5 ms: 1.38x faster                                                       |
| nbody                      | 68.4 ms                                                     | 53.2 ms: 1.29x faster                                                       |
| mako                       | 6.35 ms                                                     | 5.04 ms: 1.26x faster                                                       |
| deepcopy                   | 226 us                                                      | 188 us: 1.21x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 64.3 ms: 1.18x faster                                                       |
| spectral_norm              | 62.8 ms                                                     | 54.9 ms: 1.14x faster                                                       |
| crypto_pyaes               | 45.4 ms                                                     | 39.9 ms: 1.14x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.81 us: 1.14x faster                                                       |
| scimark_fft                | 172 ms                                                      | 153 ms: 1.13x faster                                                        |
| telco                      | 4.79 ms                                                     | 4.29 ms: 1.12x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 261 ms: 1.11x faster                                                        |
| tomli_loads                | 1.39 sec                                                    | 1.27 sec: 1.10x faster                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 37.4 ms: 1.09x faster                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.25 ms: 1.09x faster                                                       |
| pprint_safe_repr           | 494 ms                                                      | 453 ms: 1.09x faster                                                        |
| pprint_pformat             | 999 ms                                                      | 918 ms: 1.09x faster                                                        |
| json                       | 3.19 ms                                                     | 2.93 ms: 1.09x faster                                                       |
| bpe_tokeniser              | 2.91 sec                                                    | 2.70 sec: 1.08x faster                                                      |
| async_tree_none            | 226 ms                                                      | 210 ms: 1.08x faster                                                        |
| connected_components       | 332 ms                                                      | 311 ms: 1.07x faster                                                        |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 51.0 ms: 1.06x faster                                                       |
| float                      | 49.9 ms                                                     | 47.4 ms: 1.05x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 262 ms: 1.05x faster                                                        |
| shortest_path              | 362 ms                                                      | 345 ms: 1.05x faster                                                        |
| fannkuch                   | 253 ms                                                      | 242 ms: 1.05x faster                                                        |
| dulwich_log                | 40.8 ms                                                     | 39.6 ms: 1.03x faster                                                       |
| xml_etree_process          | 37.0 ms                                                     | 36.0 ms: 1.03x faster                                                       |
| asyncio_websockets         | 318 ms                                                      | 309 ms: 1.03x faster                                                        |
| pathlib                    | 80.9 ms                                                     | 79.0 ms: 1.02x faster                                                       |
| python_startup             | 25.4 ms                                                     | 24.9 ms: 1.02x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.93 ms: 1.02x faster                                                       |
| xml_etree_parse            | 93.6 ms                                                     | 94.4 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 391 ms: 1.02x slower                                                        |
| regex_effbot               | 1.58 ms                                                     | 1.61 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 63.2 ms: 1.02x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 56.3 ns: 1.03x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 54.7 ms: 1.03x slower                                                       |
| python_startup_no_site     | 18.1 ms                                                     | 18.8 ms: 1.04x slower                                                       |
| coverage                   | 45.6 ms                                                     | 47.4 ms: 1.04x slower                                                       |
| go                         | 87.0 ms                                                     | 90.7 ms: 1.04x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.22 us: 1.04x slower                                                       |
| async_tree_none_tg         | 209 ms                                                      | 218 ms: 1.05x slower                                                        |
| pyflate                    | 283 ms                                                      | 296 ms: 1.05x slower                                                        |
| async_tree_io              | 521 ms                                                      | 546 ms: 1.05x slower                                                        |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| pycparser                  | 683 ms                                                      | 721 ms: 1.06x slower                                                        |
| logging_format             | 6.26 us                                                     | 6.66 us: 1.06x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 403 ms: 1.07x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.7 ms: 1.07x slower                                                       |
| chaos                      | 38.5 ms                                                     | 41.2 ms: 1.07x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 144 us: 1.08x slower                                                        |
| bench_mp_pool              | 86.4 ms                                                     | 93.3 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 105 us                                                      | 114 us: 1.08x slower                                                        |
| json_dumps                 | 5.92 ms                                                     | 6.42 ms: 1.09x slower                                                       |
| create_gc_cycles           | 1.26 ms                                                     | 1.37 ms: 1.09x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 207 us: 1.09x slower                                                        |
| sympy_expand               | 291 ms                                                      | 321 ms: 1.10x slower                                                        |
| mdp                        | 1.39 sec                                                    | 1.53 sec: 1.11x slower                                                      |
| sympy_str                  | 169 ms                                                      | 190 ms: 1.13x slower                                                        |
| regex_compile              | 80.5 ms                                                     | 90.9 ms: 1.13x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 64.3 ms: 1.13x slower                                                       |
| 2to3                       | 221 ms                                                      | 251 ms: 1.14x slower                                                        |
| comprehensions             | 10.3 us                                                     | 11.7 us: 1.14x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 880 us: 1.14x slower                                                        |
| pylint                     | 211 ms                                                      | 243 ms: 1.15x slower                                                        |
| generators                 | 19.5 ms                                                     | 22.5 ms: 1.15x slower                                                       |
| async_generators           | 223 ms                                                      | 259 ms: 1.16x slower                                                        |
| sympy_sum                  | 86.9 ms                                                     | 101 ms: 1.16x slower                                                        |
| sqlglot_normalize          | 175 ms                                                      | 208 ms: 1.19x slower                                                        |
| django_template            | 22.4 ms                                                     | 26.7 ms: 1.19x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.88 sec: 1.20x slower                                                      |
| sphinx                     | 633 ms                                                      | 762 ms: 1.20x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 627 ms: 1.21x slower                                                        |
| deltablue                  | 1.92 ms                                                     | 2.33 ms: 1.22x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.17 ms: 1.22x slower                                                       |
| genshi_text                | 15.6 ms                                                     | 19.2 ms: 1.23x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 15.6 ms: 1.25x slower                                                       |
| richards_super             | 30.9 ms                                                     | 39.0 ms: 1.26x slower                                                       |
| richards                   | 27.3 ms                                                     | 34.9 ms: 1.28x slower                                                       |
| genshi_xml                 | 35.5 ms                                                     | 45.5 ms: 1.28x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 42.6 ms: 1.29x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 5.16 ms: 1.33x slower                                                       |
| raytrace                   | 160 ms                                                      | 222 ms: 1.39x slower                                                        |
| k_core                     | 1.74 sec                                                    | 2.43 sec: 1.40x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (4): bench_thread_pool, pidigits, html5lib, meteor_contest
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: sqlite_synth

- Geometric mean (including insignificant results): 1.003x slower
# HPT report

- Reliability score: 97.97% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown