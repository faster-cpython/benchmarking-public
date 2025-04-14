# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.001x slower
- HPT reliability: 71.48%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.87x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 294 ms: 1.01x slower                                             |
| chameleon      | 7.49 ms                                                      | 7.26 ms: 1.03x faster                                            |
| docutils       | 2.81 sec                                                     | 2.83 sec: 1.01x slower                                           |
| html5lib       | 72.9 ms                                                      | 73.9 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_generators           | 364 ms                                                       | 368 ms: 1.01x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.04x slower                                            |
| async_tree_none            | 370 ms                                                       | 435 ms: 1.18x slower                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 701 ms: 1.18x slower                                             |
| async_tree_memoization_tg  | 458 ms                                                       | 545 ms: 1.19x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 701 ms: 1.22x slower                                             |
| async_tree_memoization     | 447 ms                                                       | 547 ms: 1.22x slower                                             |
| async_tree_none_tg         | 342 ms                                                       | 430 ms: 1.26x slower                                             |
| async_tree_io              | 832 ms                                                       | 1.08 sec: 1.29x slower                                           |
| async_tree_io_tg           | 823 ms                                                       | 1.07 sec: 1.30x slower                                           |
| Geometric mean             | (ref)                                                        | 1.17x slower                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 85.3 ms: 1.08x faster                                            |
| float          | 81.6 ms                                                      | 78.0 ms: 1.05x faster                                            |
| pidigits       | 252 ms                                                       | 263 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                        | 1.03x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 141 ms: 1.01x faster                                             |
| regex_v8       | 24.9 ms                                                      | 26.0 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.23 sec: 1.09x faster                                           |
| pickle_pure_python   | 322 us                                                       | 307 us: 1.05x faster                                             |
| xml_etree_process    | 60.7 ms                                                      | 58.7 ms: 1.03x faster                                            |
| json_dumps           | 10.8 ms                                                      | 10.6 ms: 1.02x faster                                            |
| unpickle_pure_python | 216 us                                                       | 213 us: 1.02x faster                                             |
| xml_etree_generate   | 85.2 ms                                                      | 85.6 ms: 1.00x slower                                            |
| json_loads           | 24.7 us                                                      | 25.0 us: 1.01x slower                                            |
| xml_etree_parse      | 144 ms                                                       | 150 ms: 1.04x slower                                             |
| xml_etree_iterparse  | 99.8 ms                                                      | 107 ms: 1.07x slower                                             |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 12.6 ms: 1.24x faster                                            |
| python_startup_no_site | 8.93 ms                                                      | 11.0 ms: 1.23x slower                                            |
| Geometric mean         | (ref)                                                        | 1.00x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                            |
| genshi_xml      | 58.0 ms                                                      | 55.6 ms: 1.04x faster                                            |
| django_template | 38.9 ms                                                      | 38.4 ms: 1.01x faster                                            |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                     |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.57 ms: 1.69x faster                                            |
| typing_runtime_protocols   | 176 us                                                       | 113 us: 1.55x faster                                             |
| python_startup             | 15.6 ms                                                      | 12.6 ms: 1.24x faster                                            |
| mypy2                      | 1.02 sec                                                     | 864 ms: 1.19x faster                                             |
| gc_traversal               | 4.48 ms                                                      | 3.94 ms: 1.14x faster                                            |
| tomli_loads                | 2.43 sec                                                     | 2.23 sec: 1.09x faster                                           |
| nbody                      | 92.1 ms                                                      | 85.3 ms: 1.08x faster                                            |
| json                       | 5.62 ms                                                      | 5.27 ms: 1.07x faster                                            |
| deepcopy_reduce            | 3.49 us                                                      | 3.28 us: 1.07x faster                                            |
| telco                      | 8.77 ms                                                      | 8.23 ms: 1.07x faster                                            |
| deepcopy                   | 388 us                                                       | 367 us: 1.06x faster                                             |
| genshi_text                | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                            |
| spectral_norm              | 97.4 ms                                                      | 92.3 ms: 1.06x faster                                            |
| bench_mp_pool              | 4.82 ms                                                      | 4.57 ms: 1.05x faster                                            |
| thrift                     | 918 us                                                       | 872 us: 1.05x faster                                             |
| pickle_pure_python         | 322 us                                                       | 307 us: 1.05x faster                                             |
| deepcopy_memo              | 38.9 us                                                      | 37.1 us: 1.05x faster                                            |
| float                      | 81.6 ms                                                      | 78.0 ms: 1.05x faster                                            |
| comprehensions             | 17.3 us                                                      | 16.5 us: 1.04x faster                                            |
| genshi_xml                 | 58.0 ms                                                      | 55.6 ms: 1.04x faster                                            |
| nqueens                    | 92.3 ms                                                      | 89.1 ms: 1.04x faster                                            |
| xml_etree_process          | 60.7 ms                                                      | 58.7 ms: 1.03x faster                                            |
| chameleon                  | 7.49 ms                                                      | 7.26 ms: 1.03x faster                                            |
| crypto_pyaes               | 73.5 ms                                                      | 71.4 ms: 1.03x faster                                            |
| sqlglot_normalize          | 119 ms                                                       | 116 ms: 1.03x faster                                             |
| pprint_safe_repr           | 835 ms                                                       | 813 ms: 1.03x faster                                             |
| pprint_pformat             | 1.70 sec                                                     | 1.66 sec: 1.03x faster                                           |
| sympy_expand               | 506 ms                                                       | 494 ms: 1.03x faster                                             |
| json_dumps                 | 10.8 ms                                                      | 10.6 ms: 1.02x faster                                            |
| coverage                   | 84.5 ms                                                      | 82.9 ms: 1.02x faster                                            |
| unpickle_pure_python       | 216 us                                                       | 213 us: 1.02x faster                                             |
| logging_silent             | 97.5 ns                                                      | 96.0 ns: 1.02x faster                                            |
| regex_compile              | 143 ms                                                       | 141 ms: 1.01x faster                                             |
| richards_super             | 60.2 ms                                                      | 59.4 ms: 1.01x faster                                            |
| django_template            | 38.9 ms                                                      | 38.4 ms: 1.01x faster                                            |
| chaos                      | 60.6 ms                                                      | 59.9 ms: 1.01x faster                                            |
| sympy_str                  | 297 ms                                                       | 294 ms: 1.01x faster                                             |
| mdp                        | 2.53 sec                                                     | 2.50 sec: 1.01x faster                                           |
| raytrace                   | 267 ms                                                       | 265 ms: 1.01x faster                                             |
| go                         | 167 ms                                                       | 166 ms: 1.01x faster                                             |
| meteor_contest             | 130 ms                                                       | 130 ms: 1.00x faster                                             |
| sympy_integrate            | 23.4 ms                                                      | 23.3 ms: 1.00x faster                                            |
| scimark_lu                 | 97.4 ms                                                      | 97.8 ms: 1.00x slower                                            |
| xml_etree_generate         | 85.2 ms                                                      | 85.6 ms: 1.00x slower                                            |
| sqlglot_optimize           | 58.7 ms                                                      | 59.0 ms: 1.01x slower                                            |
| 2to3                       | 293 ms                                                       | 294 ms: 1.01x slower                                             |
| docutils                   | 2.81 sec                                                     | 2.83 sec: 1.01x slower                                           |
| json_loads                 | 24.7 us                                                      | 25.0 us: 1.01x slower                                            |
| async_generators           | 364 ms                                                       | 368 ms: 1.01x slower                                             |
| html5lib                   | 72.9 ms                                                      | 73.9 ms: 1.01x slower                                            |
| scimark_fft                | 298 ms                                                       | 302 ms: 1.01x slower                                             |
| sqlglot_transpile          | 1.76 ms                                                      | 1.79 ms: 1.01x slower                                            |
| pyflate                    | 493 ms                                                       | 501 ms: 1.02x slower                                             |
| sqlglot_parse              | 1.37 ms                                                      | 1.39 ms: 1.02x slower                                            |
| richards                   | 52.5 ms                                                      | 53.7 ms: 1.02x slower                                            |
| pycparser                  | 1.28 sec                                                     | 1.32 sec: 1.03x slower                                           |
| bench_thread_pool          | 929 us                                                       | 960 us: 1.03x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.04x slower                                            |
| dulwich_log                | 65.5 ms                                                      | 68.2 ms: 1.04x slower                                            |
| scimark_monte_carlo        | 65.2 ms                                                      | 67.9 ms: 1.04x slower                                            |
| regex_v8                   | 24.9 ms                                                      | 26.0 ms: 1.04x slower                                            |
| xml_etree_parse            | 144 ms                                                       | 150 ms: 1.04x slower                                             |
| pidigits                   | 252 ms                                                       | 263 ms: 1.04x slower                                             |
| deltablue                  | 3.38 ms                                                      | 3.54 ms: 1.04x slower                                            |
| logging_format             | 6.95 us                                                      | 7.31 us: 1.05x slower                                            |
| logging_simple             | 6.28 us                                                      | 6.66 us: 1.06x slower                                            |
| xml_etree_iterparse        | 99.8 ms                                                      | 107 ms: 1.07x slower                                             |
| pathlib                    | 17.4 ms                                                      | 18.9 ms: 1.08x slower                                            |
| scimark_sor                | 125 ms                                                       | 144 ms: 1.15x slower                                             |
| async_tree_none            | 370 ms                                                       | 435 ms: 1.18x slower                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 701 ms: 1.18x slower                                             |
| async_tree_memoization_tg  | 458 ms                                                       | 545 ms: 1.19x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 701 ms: 1.22x slower                                             |
| async_tree_memoization     | 447 ms                                                       | 547 ms: 1.22x slower                                             |
| python_startup_no_site     | 8.93 ms                                                      | 11.0 ms: 1.23x slower                                            |
| async_tree_none_tg         | 342 ms                                                       | 430 ms: 1.26x slower                                             |
| async_tree_io              | 832 ms                                                       | 1.08 sec: 1.29x slower                                           |
| async_tree_io_tg           | 823 ms                                                       | 1.07 sec: 1.30x slower                                           |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (11): tornado_http, pylint, generators, regex_effbot, hexiom, regex_dna, asyncio_websockets, scimark_sparse_mat_mult, sympy_sum, mako, fannkuch
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (11) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 71.48% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.87x