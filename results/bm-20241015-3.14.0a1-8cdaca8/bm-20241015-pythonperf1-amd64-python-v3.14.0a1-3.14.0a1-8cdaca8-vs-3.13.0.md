# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: windows-amd64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.042x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 231 ms: 1.05x slower                                            |
| docutils       | 1.57 sec                                                    | 1.72 sec: 1.10x slower                                          |
| html5lib       | 38.9 ms                                                     | 40.8 ms: 1.05x slower                                           |
| sphinx         | 633 ms                                                      | 682 ms: 1.08x slower                                            |
| Geometric mean | (ref)                                                       | 1.06x slower                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 266 ms: 1.09x faster                                            |
| async_tree_none_tg         | 209 ms                                                      | 215 ms: 1.03x slower                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 407 ms: 1.08x slower                                            |
| coroutines                 | 12.8 ms                                                     | 13.9 ms: 1.09x slower                                           |
| async_tree_io              | 521 ms                                                      | 574 ms: 1.10x slower                                            |
| async_generators           | 223 ms                                                      | 249 ms: 1.11x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 645 ms: 1.24x slower                                            |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                    |

Benchmark hidden because not significant (3): async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 49.9 ms                                                     | 55.6 ms: 1.11x slower                                           |
| nbody          | 68.4 ms                                                     | 79.3 ms: 1.16x slower                                           |
| Geometric mean | (ref)                                                       | 1.09x slower                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 16.5 ms: 1.30x faster                                           |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                            |
| regex_effbot   | 1.58 ms                                                     | 1.59 ms: 1.01x slower                                           |
| regex_compile  | 80.5 ms                                                     | 91.1 ms: 1.13x slower                                           |
| Geometric mean | (ref)                                                       | 1.03x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_parse      | 93.6 ms                                                     | 95.4 ms: 1.02x slower                                           |
| xml_etree_iterparse  | 61.8 ms                                                     | 66.3 ms: 1.07x slower                                           |
| xml_etree_generate   | 54.0 ms                                                     | 59.3 ms: 1.10x slower                                           |
| xml_etree_process    | 37.0 ms                                                     | 41.7 ms: 1.13x slower                                           |
| unpickle_pure_python | 133 us                                                      | 151 us: 1.13x slower                                            |
| pickle_pure_python   | 190 us                                                      | 217 us: 1.15x slower                                            |
| tomli_loads          | 1.39 sec                                                    | 1.61 sec: 1.16x slower                                          |
| json_dumps           | 5.92 ms                                                     | 6.93 ms: 1.17x slower                                           |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                    |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 24.6 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 6.73 ms: 1.06x slower                                           |
| genshi_xml      | 35.5 ms                                                     | 39.6 ms: 1.12x slower                                           |
| genshi_text     | 15.6 ms                                                     | 17.5 ms: 1.12x slower                                           |
| django_template | 22.4 ms                                                     | 25.9 ms: 1.16x slower                                           |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 539 us: 16.33x faster                                           |
| regex_v8                   | 21.4 ms                                                     | 16.5 ms: 1.30x faster                                           |
| deepcopy                   | 226 us                                                      | 194 us: 1.17x faster                                            |
| deepcopy_memo              | 23.3 us                                                     | 20.4 us: 1.14x faster                                           |
| async_tree_memoization_tg  | 288 ms                                                      | 266 ms: 1.09x faster                                            |
| python_startup             | 25.4 ms                                                     | 24.6 ms: 1.03x faster                                           |
| bench_mp_pool              | 86.4 ms                                                     | 84.0 ms: 1.03x faster                                           |
| deepcopy_reduce            | 2.06 us                                                     | 2.02 us: 1.02x faster                                           |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                            |
| regex_effbot               | 1.58 ms                                                     | 1.59 ms: 1.01x slower                                           |
| go                         | 87.0 ms                                                     | 88.5 ms: 1.02x slower                                           |
| xml_etree_parse            | 93.6 ms                                                     | 95.4 ms: 1.02x slower                                           |
| telco                      | 4.79 ms                                                     | 4.89 ms: 1.02x slower                                           |
| async_tree_none_tg         | 209 ms                                                      | 215 ms: 1.03x slower                                            |
| sympy_sum                  | 86.9 ms                                                     | 90.9 ms: 1.05x slower                                           |
| 2to3                       | 221 ms                                                      | 231 ms: 1.05x slower                                            |
| meteor_contest             | 73.5 ms                                                     | 77.0 ms: 1.05x slower                                           |
| html5lib                   | 38.9 ms                                                     | 40.8 ms: 1.05x slower                                           |
| mako                       | 6.35 ms                                                     | 6.73 ms: 1.06x slower                                           |
| typing_runtime_protocols   | 105 us                                                      | 112 us: 1.07x slower                                            |
| dulwich_log                | 40.8 ms                                                     | 43.6 ms: 1.07x slower                                           |
| sympy_str                  | 169 ms                                                      | 181 ms: 1.07x slower                                            |
| sympy_expand               | 291 ms                                                      | 312 ms: 1.07x slower                                            |
| xml_etree_iterparse        | 61.8 ms                                                     | 66.3 ms: 1.07x slower                                           |
| coverage                   | 45.6 ms                                                     | 49.0 ms: 1.08x slower                                           |
| logging_simple             | 5.96 us                                                     | 6.42 us: 1.08x slower                                           |
| sphinx                     | 633 ms                                                      | 682 ms: 1.08x slower                                            |
| mdp                        | 1.39 sec                                                    | 1.50 sec: 1.08x slower                                          |
| sympy_integrate            | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                           |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 407 ms: 1.08x slower                                            |
| pylint                     | 211 ms                                                      | 229 ms: 1.09x slower                                            |
| coroutines                 | 12.8 ms                                                     | 13.9 ms: 1.09x slower                                           |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.68 ms: 1.09x slower                                           |
| logging_format             | 6.26 us                                                     | 6.85 us: 1.09x slower                                           |
| docutils                   | 1.57 sec                                                    | 1.72 sec: 1.10x slower                                          |
| xml_etree_generate         | 54.0 ms                                                     | 59.3 ms: 1.10x slower                                           |
| async_tree_io              | 521 ms                                                      | 574 ms: 1.10x slower                                            |
| pycparser                  | 683 ms                                                      | 756 ms: 1.11x slower                                            |
| crypto_pyaes               | 45.4 ms                                                     | 50.3 ms: 1.11x slower                                           |
| float                      | 49.9 ms                                                     | 55.6 ms: 1.11x slower                                           |
| async_generators           | 223 ms                                                      | 249 ms: 1.11x slower                                            |
| genshi_xml                 | 35.5 ms                                                     | 39.6 ms: 1.12x slower                                           |
| genshi_text                | 15.6 ms                                                     | 17.5 ms: 1.12x slower                                           |
| create_gc_cycles           | 1.26 ms                                                     | 1.41 ms: 1.12x slower                                           |
| xml_etree_process          | 37.0 ms                                                     | 41.7 ms: 1.13x slower                                           |
| nqueens                    | 56.7 ms                                                     | 63.9 ms: 1.13x slower                                           |
| fannkuch                   | 253 ms                                                      | 286 ms: 1.13x slower                                            |
| sqlglot_optimize           | 32.9 ms                                                     | 37.2 ms: 1.13x slower                                           |
| regex_compile              | 80.5 ms                                                     | 91.1 ms: 1.13x slower                                           |
| generators                 | 19.5 ms                                                     | 22.1 ms: 1.13x slower                                           |
| unpickle_pure_python       | 133 us                                                      | 151 us: 1.13x slower                                            |
| sqlglot_normalize          | 175 ms                                                      | 199 ms: 1.14x slower                                            |
| pprint_safe_repr           | 494 ms                                                      | 565 ms: 1.14x slower                                            |
| pprint_pformat             | 999 ms                                                      | 1.14 sec: 1.14x slower                                          |
| pickle_pure_python         | 190 us                                                      | 217 us: 1.15x slower                                            |
| hexiom                     | 3.89 ms                                                     | 4.46 ms: 1.15x slower                                           |
| logging_silent             | 54.6 ns                                                     | 62.9 ns: 1.15x slower                                           |
| pyflate                    | 283 ms                                                      | 327 ms: 1.15x slower                                            |
| comprehensions             | 10.3 us                                                     | 11.9 us: 1.16x slower                                           |
| chaos                      | 38.5 ms                                                     | 44.6 ms: 1.16x slower                                           |
| tomli_loads                | 1.39 sec                                                    | 1.61 sec: 1.16x slower                                          |
| nbody                      | 68.4 ms                                                     | 79.3 ms: 1.16x slower                                           |
| django_template            | 22.4 ms                                                     | 25.9 ms: 1.16x slower                                           |
| spectral_norm              | 62.8 ms                                                     | 72.9 ms: 1.16x slower                                           |
| json_dumps                 | 5.92 ms                                                     | 6.93 ms: 1.17x slower                                           |
| scimark_fft                | 172 ms                                                      | 202 ms: 1.17x slower                                            |
| scimark_monte_carlo        | 40.8 ms                                                     | 48.2 ms: 1.18x slower                                           |
| richards                   | 27.3 ms                                                     | 32.3 ms: 1.18x slower                                           |
| deltablue                  | 1.92 ms                                                     | 2.29 ms: 1.19x slower                                           |
| scimark_lu                 | 53.0 ms                                                     | 63.2 ms: 1.19x slower                                           |
| sqlglot_transpile          | 956 us                                                      | 1.14 ms: 1.19x slower                                           |
| richards_super             | 30.9 ms                                                     | 36.8 ms: 1.19x slower                                           |
| sqlglot_parse              | 771 us                                                      | 921 us: 1.20x slower                                            |
| scimark_sor                | 76.2 ms                                                     | 93.2 ms: 1.22x slower                                           |
| raytrace                   | 160 ms                                                      | 198 ms: 1.24x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 645 ms: 1.24x slower                                            |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                    |

Benchmark hidden because not significant (11): bench_thread_pool, json, pathlib, gc_traversal, async_tree_none, pidigits, python_startup_no_site, async_tree_cpu_io_mixed, tornado_http, async_tree_memoization, json_loads
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.042x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown