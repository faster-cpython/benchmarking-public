# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: windows-amd64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.011x faster
- HPT reliability: 74.82%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 210 ms: 1.05x faster                                            |
| chameleon      | 4.82 ms                                                     | 4.91 ms: 1.02x slower                                           |
| docutils       | 1.57 sec                                                    | 1.53 sec: 1.02x faster                                          |
| html5lib       | 38.9 ms                                                     | 35.9 ms: 1.08x faster                                           |
| tornado_http   | 93.0 ms                                                     | 85.5 ms: 1.09x faster                                           |
| Geometric mean | (ref)                                                       | 1.04x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| coroutines                 | 12.8 ms                                                     | 13.0 ms: 1.02x slower                                           |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                            |
| async_tree_none            | 226 ms                                                      | 263 ms: 1.17x slower                                            |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 448 ms: 1.17x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 349 ms: 1.21x slower                                            |
| async_tree_memoization     | 276 ms                                                      | 341 ms: 1.23x slower                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 465 ms: 1.24x slower                                            |
| async_tree_none_tg         | 209 ms                                                      | 270 ms: 1.29x slower                                            |
| async_tree_io              | 521 ms                                                      | 724 ms: 1.39x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 750 ms: 1.45x slower                                            |
| Geometric mean             | (ref)                                                       | 1.21x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 49.9 ms                                                     | 52.5 ms: 1.05x slower                                           |
| nbody          | 68.4 ms                                                     | 74.1 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                       | 1.04x slower                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.3 ms: 1.40x faster                                           |
| regex_compile  | 80.5 ms                                                     | 77.7 ms: 1.04x faster                                           |
| regex_effbot   | 1.58 ms                                                     | 1.59 ms: 1.01x slower                                           |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                       | 1.08x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 13.7 us: 1.11x faster                                           |
| json_dumps           | 5.92 ms                                                     | 5.54 ms: 1.07x faster                                           |
| pickle_pure_python   | 190 us                                                      | 179 us: 1.06x faster                                            |
| unpickle_pure_python | 133 us                                                      | 128 us: 1.04x faster                                            |
| xml_etree_process    | 37.0 ms                                                     | 36.4 ms: 1.02x faster                                           |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.5 ms: 1.03x slower                                           |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                    |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 20.1 ms: 1.27x faster                                           |
| python_startup_no_site | 18.1 ms                                                     | 17.9 ms: 1.01x faster                                           |
| Geometric mean         | (ref)                                                       | 1.13x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 22.4 ms                                                     | 21.4 ms: 1.05x faster                                           |
| genshi_text     | 15.6 ms                                                     | 16.1 ms: 1.03x slower                                           |
| mako            | 6.35 ms                                                     | 6.57 ms: 1.03x slower                                           |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| create_gc_cycles           | 1.26 ms                                                     | 732 us: 1.72x faster                                            |
| mypy2                      | 679 ms                                                      | 409 ms: 1.66x faster                                            |
| typing_runtime_protocols   | 105 us                                                      | 70.5 us: 1.50x faster                                           |
| regex_v8                   | 21.4 ms                                                     | 15.3 ms: 1.40x faster                                           |
| bench_mp_pool              | 86.4 ms                                                     | 66.6 ms: 1.30x faster                                           |
| gc_traversal               | 1.97 ms                                                     | 1.52 ms: 1.30x faster                                           |
| python_startup             | 25.4 ms                                                     | 20.1 ms: 1.27x faster                                           |
| json_loads                 | 15.1 us                                                     | 13.7 us: 1.11x faster                                           |
| json                       | 3.19 ms                                                     | 2.88 ms: 1.11x faster                                           |
| sympy_expand               | 291 ms                                                      | 268 ms: 1.09x faster                                            |
| tornado_http               | 93.0 ms                                                     | 85.5 ms: 1.09x faster                                           |
| html5lib                   | 38.9 ms                                                     | 35.9 ms: 1.08x faster                                           |
| sympy_str                  | 169 ms                                                      | 156 ms: 1.08x faster                                            |
| deepcopy_reduce            | 2.06 us                                                     | 1.93 us: 1.07x faster                                           |
| json_dumps                 | 5.92 ms                                                     | 5.54 ms: 1.07x faster                                           |
| crypto_pyaes               | 45.4 ms                                                     | 42.8 ms: 1.06x faster                                           |
| pickle_pure_python         | 190 us                                                      | 179 us: 1.06x faster                                            |
| thrift                     | 8.80 ms                                                     | 8.32 ms: 1.06x faster                                           |
| 2to3                       | 221 ms                                                      | 210 ms: 1.05x faster                                            |
| sympy_sum                  | 86.9 ms                                                     | 82.6 ms: 1.05x faster                                           |
| deepcopy_memo              | 23.3 us                                                     | 22.2 us: 1.05x faster                                           |
| django_template            | 22.4 ms                                                     | 21.4 ms: 1.05x faster                                           |
| unpickle_pure_python       | 133 us                                                      | 128 us: 1.04x faster                                            |
| regex_compile              | 80.5 ms                                                     | 77.7 ms: 1.04x faster                                           |
| fannkuch                   | 253 ms                                                      | 245 ms: 1.03x faster                                            |
| coverage                   | 45.6 ms                                                     | 44.3 ms: 1.03x faster                                           |
| docutils                   | 1.57 sec                                                    | 1.53 sec: 1.02x faster                                          |
| go                         | 87.0 ms                                                     | 84.9 ms: 1.02x faster                                           |
| scimark_monte_carlo        | 40.8 ms                                                     | 39.9 ms: 1.02x faster                                           |
| meteor_contest             | 73.5 ms                                                     | 71.9 ms: 1.02x faster                                           |
| pathlib                    | 80.9 ms                                                     | 79.3 ms: 1.02x faster                                           |
| sympy_integrate            | 12.5 ms                                                     | 12.3 ms: 1.02x faster                                           |
| hexiom                     | 3.89 ms                                                     | 3.82 ms: 1.02x faster                                           |
| spectral_norm              | 62.8 ms                                                     | 61.6 ms: 1.02x faster                                           |
| xml_etree_process          | 37.0 ms                                                     | 36.4 ms: 1.02x faster                                           |
| deepcopy                   | 226 us                                                      | 223 us: 1.02x faster                                            |
| sqlglot_parse              | 771 us                                                      | 761 us: 1.01x faster                                            |
| python_startup_no_site     | 18.1 ms                                                     | 17.9 ms: 1.01x faster                                           |
| logging_silent             | 54.6 ns                                                     | 54.1 ns: 1.01x faster                                           |
| pprint_safe_repr           | 494 ms                                                      | 491 ms: 1.01x faster                                            |
| telco                      | 4.79 ms                                                     | 4.77 ms: 1.00x faster                                           |
| sqlglot_normalize          | 175 ms                                                      | 175 ms: 1.00x slower                                            |
| raytrace                   | 160 ms                                                      | 161 ms: 1.00x slower                                            |
| pprint_pformat             | 999 ms                                                      | 1.00 sec: 1.01x slower                                          |
| regex_effbot               | 1.58 ms                                                     | 1.59 ms: 1.01x slower                                           |
| dulwich_log                | 40.8 ms                                                     | 41.1 ms: 1.01x slower                                           |
| mdp                        | 1.39 sec                                                    | 1.40 sec: 1.01x slower                                          |
| logging_simple             | 5.96 us                                                     | 6.04 us: 1.01x slower                                           |
| coroutines                 | 12.8 ms                                                     | 13.0 ms: 1.02x slower                                           |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                            |
| pyflate                    | 283 ms                                                      | 288 ms: 1.02x slower                                            |
| chameleon                  | 4.82 ms                                                     | 4.91 ms: 1.02x slower                                           |
| scimark_sor                | 76.2 ms                                                     | 78.0 ms: 1.02x slower                                           |
| chaos                      | 38.5 ms                                                     | 39.5 ms: 1.03x slower                                           |
| sqlglot_transpile          | 956 us                                                      | 981 us: 1.03x slower                                            |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.52 ms: 1.03x slower                                           |
| xml_etree_iterparse        | 61.8 ms                                                     | 63.5 ms: 1.03x slower                                           |
| deltablue                  | 1.92 ms                                                     | 1.97 ms: 1.03x slower                                           |
| genshi_text                | 15.6 ms                                                     | 16.1 ms: 1.03x slower                                           |
| logging_format             | 6.26 us                                                     | 6.47 us: 1.03x slower                                           |
| mako                       | 6.35 ms                                                     | 6.57 ms: 1.03x slower                                           |
| scimark_fft                | 172 ms                                                      | 178 ms: 1.03x slower                                            |
| scimark_lu                 | 53.0 ms                                                     | 54.9 ms: 1.04x slower                                           |
| nqueens                    | 56.7 ms                                                     | 59.3 ms: 1.05x slower                                           |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                            |
| float                      | 49.9 ms                                                     | 52.5 ms: 1.05x slower                                           |
| nbody                      | 68.4 ms                                                     | 74.1 ms: 1.08x slower                                           |
| generators                 | 19.5 ms                                                     | 22.1 ms: 1.14x slower                                           |
| async_tree_none            | 226 ms                                                      | 263 ms: 1.17x slower                                            |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 448 ms: 1.17x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 349 ms: 1.21x slower                                            |
| async_tree_memoization     | 276 ms                                                      | 341 ms: 1.23x slower                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 465 ms: 1.24x slower                                            |
| async_tree_none_tg         | 209 ms                                                      | 270 ms: 1.29x slower                                            |
| async_tree_io              | 521 ms                                                      | 724 ms: 1.39x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 750 ms: 1.45x slower                                            |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (12): pylint, bench_thread_pool, xml_etree_generate, xml_etree_parse, richards_super, pidigits, tomli_loads, comprehensions, richards, sqlglot_optimize, genshi_xml, pycparser
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.011x faster
# HPT report

- Reliability score: 74.82% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown