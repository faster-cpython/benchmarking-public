# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.096x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 0.86x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 308 ms: 1.05x slower                                             |
| chameleon      | 7.49 ms                                                      | 7.89 ms: 1.05x slower                                            |
| docutils       | 2.81 sec                                                     | 2.94 sec: 1.05x slower                                           |
| tornado_http   | 119 ms                                                       | 123 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                        | 1.05x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                             |
| async_generators           | 364 ms                                                       | 372 ms: 1.02x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.5 ms: 1.05x slower                                            |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 710 ms: 1.19x slower                                             |
| async_tree_none            | 370 ms                                                       | 446 ms: 1.20x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 713 ms: 1.24x slower                                             |
| async_tree_memoization_tg  | 458 ms                                                       | 570 ms: 1.24x slower                                             |
| async_tree_memoization     | 447 ms                                                       | 558 ms: 1.25x slower                                             |
| async_tree_none_tg         | 342 ms                                                       | 442 ms: 1.29x slower                                             |
| async_tree_io              | 832 ms                                                       | 1.10 sec: 1.32x slower                                           |
| async_tree_io_tg           | 823 ms                                                       | 1.09 sec: 1.32x slower                                           |
| Geometric mean             | (ref)                                                        | 1.19x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 265 ms: 1.05x slower                                             |
| float          | 81.6 ms                                                      | 103 ms: 1.26x slower                                             |
| nbody          | 92.1 ms                                                      | 125 ms: 1.36x slower                                             |
| Geometric mean | (ref)                                                        | 1.22x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.43 ms: 1.02x faster                                            |
| regex_dna      | 238 ms                                                       | 240 ms: 1.01x slower                                             |
| regex_v8       | 24.9 ms                                                      | 26.4 ms: 1.06x slower                                            |
| regex_compile  | 143 ms                                                       | 170 ms: 1.19x slower                                             |
| Geometric mean | (ref)                                                        | 1.06x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 322 us                                                       | 311 us: 1.03x faster                                             |
| json_loads           | 24.7 us                                                      | 25.1 us: 1.01x slower                                            |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.02x slower                                             |
| xml_etree_process    | 60.7 ms                                                      | 62.3 ms: 1.03x slower                                            |
| xml_etree_generate   | 85.2 ms                                                      | 90.9 ms: 1.07x slower                                            |
| unpickle_pure_python | 216 us                                                       | 245 us: 1.13x slower                                             |
| tomli_loads          | 2.43 sec                                                     | 2.82 sec: 1.16x slower                                           |
| xml_etree_iterparse  | 99.8 ms                                                      | 117 ms: 1.17x slower                                             |
| Geometric mean       | (ref)                                                        | 1.06x slower                                                     |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 12.5 ms: 1.25x faster                                            |
| python_startup_no_site | 8.93 ms                                                      | 11.0 ms: 1.23x slower                                            |
| Geometric mean         | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 10.3 ms                                                      | 14.8 ms: 1.43x slower                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.59 ms: 1.67x faster                                            |
| typing_runtime_protocols   | 176 us                                                       | 124 us: 1.41x faster                                             |
| python_startup             | 15.6 ms                                                      | 12.5 ms: 1.25x faster                                            |
| gc_traversal               | 4.48 ms                                                      | 3.74 ms: 1.20x faster                                            |
| mypy2                      | 1.02 sec                                                     | 893 ms: 1.15x faster                                             |
| telco                      | 8.77 ms                                                      | 8.28 ms: 1.06x faster                                            |
| json                       | 5.62 ms                                                      | 5.35 ms: 1.05x faster                                            |
| pickle_pure_python         | 322 us                                                       | 311 us: 1.03x faster                                             |
| coverage                   | 84.5 ms                                                      | 81.8 ms: 1.03x faster                                            |
| deepcopy_reduce            | 3.49 us                                                      | 3.41 us: 1.03x faster                                            |
| regex_effbot               | 3.51 ms                                                      | 3.43 ms: 1.02x faster                                            |
| deepcopy                   | 388 us                                                       | 379 us: 1.02x faster                                             |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                             |
| regex_dna                  | 238 ms                                                       | 240 ms: 1.01x slower                                             |
| generators                 | 33.9 ms                                                      | 34.3 ms: 1.01x slower                                            |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.01x slower                                            |
| logging_silent             | 97.5 ns                                                      | 98.9 ns: 1.02x slower                                            |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.02x slower                                             |
| async_generators           | 364 ms                                                       | 372 ms: 1.02x slower                                             |
| xml_etree_process          | 60.7 ms                                                      | 62.3 ms: 1.03x slower                                            |
| deepcopy_memo              | 38.9 us                                                      | 40.3 us: 1.04x slower                                            |
| tornado_http               | 119 ms                                                       | 123 ms: 1.04x slower                                             |
| richards                   | 52.5 ms                                                      | 54.5 ms: 1.04x slower                                            |
| bench_thread_pool          | 929 us                                                       | 969 us: 1.04x slower                                             |
| sqlglot_normalize          | 119 ms                                                       | 124 ms: 1.04x slower                                             |
| mdp                        | 2.53 sec                                                     | 2.64 sec: 1.04x slower                                           |
| coroutines                 | 21.6 ms                                                      | 22.5 ms: 1.05x slower                                            |
| docutils                   | 2.81 sec                                                     | 2.94 sec: 1.05x slower                                           |
| pidigits                   | 252 ms                                                       | 265 ms: 1.05x slower                                             |
| 2to3                       | 293 ms                                                       | 308 ms: 1.05x slower                                             |
| chameleon                  | 7.49 ms                                                      | 7.89 ms: 1.05x slower                                            |
| sympy_expand               | 506 ms                                                       | 534 ms: 1.06x slower                                             |
| regex_v8                   | 24.9 ms                                                      | 26.4 ms: 1.06x slower                                            |
| sympy_integrate            | 23.4 ms                                                      | 24.8 ms: 1.06x slower                                            |
| logging_format             | 6.95 us                                                      | 7.38 us: 1.06x slower                                            |
| sqlglot_transpile          | 1.76 ms                                                      | 1.87 ms: 1.06x slower                                            |
| meteor_contest             | 130 ms                                                       | 139 ms: 1.06x slower                                             |
| pycparser                  | 1.28 sec                                                     | 1.36 sec: 1.06x slower                                           |
| sqlglot_parse              | 1.37 ms                                                      | 1.45 ms: 1.06x slower                                            |
| xml_etree_generate         | 85.2 ms                                                      | 90.9 ms: 1.07x slower                                            |
| scimark_lu                 | 97.4 ms                                                      | 104 ms: 1.07x slower                                             |
| go                         | 167 ms                                                       | 180 ms: 1.08x slower                                             |
| sympy_sum                  | 154 ms                                                       | 166 ms: 1.08x slower                                             |
| sqlglot_optimize           | 58.7 ms                                                      | 63.6 ms: 1.08x slower                                            |
| sympy_str                  | 297 ms                                                       | 322 ms: 1.09x slower                                             |
| logging_simple             | 6.28 us                                                      | 6.88 us: 1.10x slower                                            |
| pathlib                    | 17.4 ms                                                      | 19.1 ms: 1.10x slower                                            |
| dulwich_log                | 65.5 ms                                                      | 72.1 ms: 1.10x slower                                            |
| pprint_safe_repr           | 835 ms                                                       | 921 ms: 1.10x slower                                             |
| pprint_pformat             | 1.70 sec                                                     | 1.90 sec: 1.12x slower                                           |
| unpickle_pure_python       | 216 us                                                       | 245 us: 1.13x slower                                             |
| raytrace                   | 267 ms                                                       | 305 ms: 1.14x slower                                             |
| tomli_loads                | 2.43 sec                                                     | 2.82 sec: 1.16x slower                                           |
| nqueens                    | 92.3 ms                                                      | 108 ms: 1.17x slower                                             |
| xml_etree_iterparse        | 99.8 ms                                                      | 117 ms: 1.17x slower                                             |
| scimark_sor                | 125 ms                                                       | 147 ms: 1.17x slower                                             |
| crypto_pyaes               | 73.5 ms                                                      | 86.6 ms: 1.18x slower                                            |
| pyflate                    | 493 ms                                                       | 582 ms: 1.18x slower                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 710 ms: 1.19x slower                                             |
| regex_compile              | 143 ms                                                       | 170 ms: 1.19x slower                                             |
| async_tree_none            | 370 ms                                                       | 446 ms: 1.20x slower                                             |
| python_startup_no_site     | 8.93 ms                                                      | 11.0 ms: 1.23x slower                                            |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 713 ms: 1.24x slower                                             |
| async_tree_memoization_tg  | 458 ms                                                       | 570 ms: 1.24x slower                                             |
| async_tree_memoization     | 447 ms                                                       | 558 ms: 1.25x slower                                             |
| fannkuch                   | 384 ms                                                       | 481 ms: 1.25x slower                                             |
| float                      | 81.6 ms                                                      | 103 ms: 1.26x slower                                             |
| chaos                      | 60.6 ms                                                      | 77.4 ms: 1.28x slower                                            |
| async_tree_none_tg         | 342 ms                                                       | 442 ms: 1.29x slower                                             |
| async_tree_io              | 832 ms                                                       | 1.10 sec: 1.32x slower                                           |
| async_tree_io_tg           | 823 ms                                                       | 1.09 sec: 1.32x slower                                           |
| scimark_monte_carlo        | 65.2 ms                                                      | 88.7 ms: 1.36x slower                                            |
| nbody                      | 92.1 ms                                                      | 125 ms: 1.36x slower                                             |
| mako                       | 10.3 ms                                                      | 14.8 ms: 1.43x slower                                            |
| scimark_fft                | 298 ms                                                       | 429 ms: 1.44x slower                                             |
| comprehensions             | 17.3 us                                                      | 25.0 us: 1.44x slower                                            |
| hexiom                     | 6.47 ms                                                      | 9.82 ms: 1.52x slower                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.49 ms: 1.54x slower                                            |
| deltablue                  | 3.38 ms                                                      | 5.40 ms: 1.60x slower                                            |
| spectral_norm              | 97.4 ms                                                      | 161 ms: 1.65x slower                                             |
| Geometric mean             | (ref)                                                        | 1.10x slower                                                     |

Benchmark hidden because not significant (3): bench_mp_pool, richards_super, json_dumps
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, django_template, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (10) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.096x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 0.86x