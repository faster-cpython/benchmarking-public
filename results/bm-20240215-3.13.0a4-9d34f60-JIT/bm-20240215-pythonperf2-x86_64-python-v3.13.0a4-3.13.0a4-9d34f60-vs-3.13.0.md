# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.030x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.89x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 300 ms: 1.02x slower                                             |
| chameleon      | 7.49 ms                                                      | 7.14 ms: 1.05x faster                                            |
| docutils       | 2.81 sec                                                     | 2.88 sec: 1.02x slower                                           |
| tornado_http   | 119 ms                                                       | 126 ms: 1.06x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                             |
| async_generators           | 364 ms                                                       | 371 ms: 1.02x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                            |
| async_tree_none            | 370 ms                                                       | 434 ms: 1.17x slower                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 701 ms: 1.18x slower                                             |
| async_tree_memoization_tg  | 458 ms                                                       | 549 ms: 1.20x slower                                             |
| async_tree_memoization     | 447 ms                                                       | 548 ms: 1.23x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 706 ms: 1.23x slower                                             |
| async_tree_none_tg         | 342 ms                                                       | 438 ms: 1.28x slower                                             |
| async_tree_io              | 832 ms                                                       | 1.08 sec: 1.30x slower                                           |
| async_tree_io_tg           | 823 ms                                                       | 1.08 sec: 1.31x slower                                           |
| Geometric mean             | (ref)                                                        | 1.17x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 80.7 ms: 1.01x faster                                            |
| pidigits       | 252 ms                                                       | 262 ms: 1.04x slower                                             |
| nbody          | 92.1 ms                                                      | 106 ms: 1.15x slower                                             |
| Geometric mean | (ref)                                                        | 1.06x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 24.9 ms                                                      | 25.0 ms: 1.00x slower                                            |
| regex_effbot   | 3.51 ms                                                      | 3.53 ms: 1.00x slower                                            |
| regex_compile  | 143 ms                                                       | 145 ms: 1.02x slower                                             |
| regex_dna      | 238 ms                                                       | 244 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 322 us                                                       | 304 us: 1.06x faster                                             |
| xml_etree_process    | 60.7 ms                                                      | 57.6 ms: 1.05x faster                                            |
| tomli_loads          | 2.43 sec                                                     | 2.31 sec: 1.05x faster                                           |
| json_dumps           | 10.8 ms                                                      | 10.5 ms: 1.03x faster                                            |
| xml_etree_generate   | 85.2 ms                                                      | 83.4 ms: 1.02x faster                                            |
| xml_etree_parse      | 144 ms                                                       | 148 ms: 1.03x slower                                             |
| json_loads           | 24.7 us                                                      | 25.6 us: 1.03x slower                                            |
| xml_etree_iterparse  | 99.8 ms                                                      | 103 ms: 1.04x slower                                             |
| unpickle_pure_python | 216 us                                                       | 230 us: 1.06x slower                                             |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 12.7 ms: 1.23x faster                                            |
| python_startup_no_site | 8.93 ms                                                      | 11.1 ms: 1.25x slower                                            |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 10.3 ms                                                      | 11.8 ms: 1.14x slower                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.55 ms: 1.71x faster                                            |
| typing_runtime_protocols   | 176 us                                                       | 117 us: 1.50x faster                                             |
| gc_traversal               | 4.48 ms                                                      | 3.47 ms: 1.29x faster                                            |
| python_startup             | 15.6 ms                                                      | 12.7 ms: 1.23x faster                                            |
| mypy2                      | 1.02 sec                                                     | 886 ms: 1.16x faster                                             |
| telco                      | 8.77 ms                                                      | 8.12 ms: 1.08x faster                                            |
| pickle_pure_python         | 322 us                                                       | 304 us: 1.06x faster                                             |
| xml_etree_process          | 60.7 ms                                                      | 57.6 ms: 1.05x faster                                            |
| deepcopy_memo              | 38.9 us                                                      | 36.9 us: 1.05x faster                                            |
| tomli_loads                | 2.43 sec                                                     | 2.31 sec: 1.05x faster                                           |
| json                       | 5.62 ms                                                      | 5.35 ms: 1.05x faster                                            |
| chameleon                  | 7.49 ms                                                      | 7.14 ms: 1.05x faster                                            |
| deepcopy                   | 388 us                                                       | 370 us: 1.05x faster                                             |
| deepcopy_reduce            | 3.49 us                                                      | 3.33 us: 1.05x faster                                            |
| richards_super             | 60.2 ms                                                      | 57.6 ms: 1.04x faster                                            |
| json_dumps                 | 10.8 ms                                                      | 10.5 ms: 1.03x faster                                            |
| xml_etree_generate         | 85.2 ms                                                      | 83.4 ms: 1.02x faster                                            |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                             |
| sqlglot_normalize          | 119 ms                                                       | 117 ms: 1.02x faster                                             |
| richards                   | 52.5 ms                                                      | 51.7 ms: 1.02x faster                                            |
| float                      | 81.6 ms                                                      | 80.7 ms: 1.01x faster                                            |
| pprint_safe_repr           | 835 ms                                                       | 826 ms: 1.01x faster                                             |
| sympy_expand               | 506 ms                                                       | 502 ms: 1.01x faster                                             |
| regex_v8                   | 24.9 ms                                                      | 25.0 ms: 1.00x slower                                            |
| sympy_str                  | 297 ms                                                       | 298 ms: 1.00x slower                                             |
| regex_effbot               | 3.51 ms                                                      | 3.53 ms: 1.00x slower                                            |
| pprint_pformat             | 1.70 sec                                                     | 1.72 sec: 1.01x slower                                           |
| regex_compile              | 143 ms                                                       | 145 ms: 1.02x slower                                             |
| sqlglot_parse              | 1.37 ms                                                      | 1.39 ms: 1.02x slower                                            |
| scimark_lu                 | 97.4 ms                                                      | 99.3 ms: 1.02x slower                                            |
| sympy_integrate            | 23.4 ms                                                      | 23.9 ms: 1.02x slower                                            |
| async_generators           | 364 ms                                                       | 371 ms: 1.02x slower                                             |
| regex_dna                  | 238 ms                                                       | 244 ms: 1.02x slower                                             |
| 2to3                       | 293 ms                                                       | 300 ms: 1.02x slower                                             |
| raytrace                   | 267 ms                                                       | 274 ms: 1.02x slower                                             |
| docutils                   | 2.81 sec                                                     | 2.88 sec: 1.02x slower                                           |
| sympy_sum                  | 154 ms                                                       | 158 ms: 1.03x slower                                             |
| sqlglot_optimize           | 58.7 ms                                                      | 60.4 ms: 1.03x slower                                            |
| sqlglot_transpile          | 1.76 ms                                                      | 1.82 ms: 1.03x slower                                            |
| xml_etree_parse            | 144 ms                                                       | 148 ms: 1.03x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                            |
| json_loads                 | 24.7 us                                                      | 25.6 us: 1.03x slower                                            |
| nqueens                    | 92.3 ms                                                      | 95.4 ms: 1.03x slower                                            |
| logging_format             | 6.95 us                                                      | 7.20 us: 1.04x slower                                            |
| xml_etree_iterparse        | 99.8 ms                                                      | 103 ms: 1.04x slower                                             |
| pycparser                  | 1.28 sec                                                     | 1.33 sec: 1.04x slower                                           |
| logging_simple             | 6.28 us                                                      | 6.51 us: 1.04x slower                                            |
| pidigits                   | 252 ms                                                       | 262 ms: 1.04x slower                                             |
| bench_thread_pool          | 929 us                                                       | 967 us: 1.04x slower                                             |
| dulwich_log                | 65.5 ms                                                      | 69.1 ms: 1.05x slower                                            |
| tornado_http               | 119 ms                                                       | 126 ms: 1.06x slower                                             |
| unpickle_pure_python       | 216 us                                                       | 230 us: 1.06x slower                                             |
| fannkuch                   | 384 ms                                                       | 409 ms: 1.06x slower                                             |
| pyflate                    | 493 ms                                                       | 529 ms: 1.07x slower                                             |
| crypto_pyaes               | 73.5 ms                                                      | 79.3 ms: 1.08x slower                                            |
| deltablue                  | 3.38 ms                                                      | 3.69 ms: 1.09x slower                                            |
| pathlib                    | 17.4 ms                                                      | 19.1 ms: 1.10x slower                                            |
| comprehensions             | 17.3 us                                                      | 19.3 us: 1.12x slower                                            |
| mako                       | 10.3 ms                                                      | 11.8 ms: 1.14x slower                                            |
| scimark_sor                | 125 ms                                                       | 143 ms: 1.15x slower                                             |
| chaos                      | 60.6 ms                                                      | 69.4 ms: 1.15x slower                                            |
| nbody                      | 92.1 ms                                                      | 106 ms: 1.15x slower                                             |
| async_tree_none            | 370 ms                                                       | 434 ms: 1.17x slower                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 701 ms: 1.18x slower                                             |
| spectral_norm              | 97.4 ms                                                      | 115 ms: 1.18x slower                                             |
| hexiom                     | 6.47 ms                                                      | 7.63 ms: 1.18x slower                                            |
| async_tree_memoization_tg  | 458 ms                                                       | 549 ms: 1.20x slower                                             |
| scimark_fft                | 298 ms                                                       | 357 ms: 1.20x slower                                             |
| scimark_monte_carlo        | 65.2 ms                                                      | 78.5 ms: 1.20x slower                                            |
| async_tree_memoization     | 447 ms                                                       | 548 ms: 1.23x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 706 ms: 1.23x slower                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.23 ms: 1.24x slower                                            |
| python_startup_no_site     | 8.93 ms                                                      | 11.1 ms: 1.25x slower                                            |
| async_tree_none_tg         | 342 ms                                                       | 438 ms: 1.28x slower                                             |
| async_tree_io              | 832 ms                                                       | 1.08 sec: 1.30x slower                                           |
| async_tree_io_tg           | 823 ms                                                       | 1.08 sec: 1.31x slower                                           |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                     |

Benchmark hidden because not significant (7): coverage, meteor_contest, mdp, go, logging_silent, generators, bench_mp_pool
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, django_template, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (10) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.030x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.89x