# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.002x slower
- HPT reliability: 55.32%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 314 ms: 1.07x slower                                             |
| docutils       | 2.81 sec                                                     | 3.17 sec: 1.13x slower                                           |
| html5lib       | 72.9 ms                                                      | 69.2 ms: 1.05x faster                                            |
| sphinx         | 1.11 sec                                                     | 1.26 sec: 1.13x slower                                           |
| tornado_http   | 119 ms                                                       | 123 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                        | 1.06x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 373 ms: 1.23x faster                                             |
| async_tree_none            | 370 ms                                                       | 333 ms: 1.11x faster                                             |
| async_tree_memoization     | 447 ms                                                       | 408 ms: 1.10x faster                                             |
| async_tree_none_tg         | 342 ms                                                       | 323 ms: 1.06x faster                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 574 ms: 1.04x faster                                             |
| asyncio_websockets         | 395 ms                                                       | 381 ms: 1.04x faster                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 557 ms: 1.03x faster                                             |
| async_tree_io              | 832 ms                                                       | 846 ms: 1.02x slower                                             |
| async_generators           | 364 ms                                                       | 379 ms: 1.04x slower                                             |
| async_tree_io_tg           | 823 ms                                                       | 865 ms: 1.05x slower                                             |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                     |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 83.7 ms: 1.10x faster                                            |
| float          | 81.6 ms                                                      | 79.3 ms: 1.03x faster                                            |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                             |
| Geometric mean | (ref)                                                        | 1.04x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 233 ms: 1.02x faster                                             |
| regex_effbot   | 3.51 ms                                                      | 3.57 ms: 1.01x slower                                            |
| regex_compile  | 143 ms                                                       | 150 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.12 sec: 1.15x faster                                           |
| xml_etree_generate   | 85.2 ms                                                      | 80.6 ms: 1.06x faster                                            |
| xml_etree_process    | 60.7 ms                                                      | 57.7 ms: 1.05x faster                                            |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                             |
| unpickle_pure_python | 216 us                                                       | 221 us: 1.02x slower                                             |
| pickle_pure_python   | 322 us                                                       | 333 us: 1.03x slower                                             |
| json_dumps           | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                            |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                     |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 14.9 ms: 1.05x faster                                            |
| python_startup_no_site | 8.93 ms                                                      | 9.01 ms: 1.01x slower                                            |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.52 ms: 1.08x faster                                            |
| genshi_text     | 27.2 ms                                                      | 28.0 ms: 1.03x slower                                            |
| genshi_xml      | 58.0 ms                                                      | 62.1 ms: 1.07x slower                                            |
| django_template | 38.9 ms                                                      | 42.9 ms: 1.10x slower                                            |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 29.9 us: 1.30x faster                                            |
| deepcopy                   | 388 us                                                       | 309 us: 1.26x faster                                             |
| async_tree_memoization_tg  | 458 ms                                                       | 373 ms: 1.23x faster                                             |
| scimark_sor                | 125 ms                                                       | 103 ms: 1.21x faster                                             |
| tomli_loads                | 2.43 sec                                                     | 2.12 sec: 1.15x faster                                           |
| richards                   | 52.5 ms                                                      | 46.6 ms: 1.13x faster                                            |
| deepcopy_reduce            | 3.49 us                                                      | 3.10 us: 1.13x faster                                            |
| telco                      | 8.77 ms                                                      | 7.80 ms: 1.12x faster                                            |
| richards_super             | 60.2 ms                                                      | 53.6 ms: 1.12x faster                                            |
| async_tree_none            | 370 ms                                                       | 333 ms: 1.11x faster                                             |
| json                       | 5.62 ms                                                      | 5.08 ms: 1.11x faster                                            |
| nbody                      | 92.1 ms                                                      | 83.7 ms: 1.10x faster                                            |
| async_tree_memoization     | 447 ms                                                       | 408 ms: 1.10x faster                                             |
| go                         | 167 ms                                                       | 152 ms: 1.10x faster                                             |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.09x faster                                            |
| mako                       | 10.3 ms                                                      | 9.52 ms: 1.08x faster                                            |
| bpe_tokeniser              | 5.09 sec                                                     | 4.74 sec: 1.07x faster                                           |
| coverage                   | 84.5 ms                                                      | 79.2 ms: 1.07x faster                                            |
| fannkuch                   | 384 ms                                                       | 361 ms: 1.07x faster                                             |
| xml_etree_generate         | 85.2 ms                                                      | 80.6 ms: 1.06x faster                                            |
| async_tree_none_tg         | 342 ms                                                       | 323 ms: 1.06x faster                                             |
| html5lib                   | 72.9 ms                                                      | 69.2 ms: 1.05x faster                                            |
| xml_etree_process          | 60.7 ms                                                      | 57.7 ms: 1.05x faster                                            |
| python_startup             | 15.6 ms                                                      | 14.9 ms: 1.05x faster                                            |
| spectral_norm              | 97.4 ms                                                      | 93.0 ms: 1.05x faster                                            |
| pprint_safe_repr           | 835 ms                                                       | 798 ms: 1.05x faster                                             |
| pyflate                    | 493 ms                                                       | 473 ms: 1.04x faster                                             |
| logging_silent             | 97.5 ns                                                      | 93.9 ns: 1.04x faster                                            |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 574 ms: 1.04x faster                                             |
| asyncio_websockets         | 395 ms                                                       | 381 ms: 1.04x faster                                             |
| pprint_pformat             | 1.70 sec                                                     | 1.64 sec: 1.03x faster                                           |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 557 ms: 1.03x faster                                             |
| float                      | 81.6 ms                                                      | 79.3 ms: 1.03x faster                                            |
| scimark_fft                | 298 ms                                                       | 290 ms: 1.03x faster                                             |
| thrift                     | 918 us                                                       | 894 us: 1.03x faster                                             |
| regex_dna                  | 238 ms                                                       | 233 ms: 1.02x faster                                             |
| deltablue                  | 3.38 ms                                                      | 3.30 ms: 1.02x faster                                            |
| scimark_lu                 | 97.4 ms                                                      | 95.5 ms: 1.02x faster                                            |
| crypto_pyaes               | 73.5 ms                                                      | 72.2 ms: 1.02x faster                                            |
| dulwich_log                | 65.5 ms                                                      | 64.5 ms: 1.02x faster                                            |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                             |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                             |
| python_startup_no_site     | 8.93 ms                                                      | 9.01 ms: 1.01x slower                                            |
| pycparser                  | 1.28 sec                                                     | 1.29 sec: 1.01x slower                                           |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.26 ms: 1.01x slower                                            |
| regex_effbot               | 3.51 ms                                                      | 3.57 ms: 1.01x slower                                            |
| async_tree_io              | 832 ms                                                       | 846 ms: 1.02x slower                                             |
| meteor_contest             | 130 ms                                                       | 133 ms: 1.02x slower                                             |
| unpickle_pure_python       | 216 us                                                       | 221 us: 1.02x slower                                             |
| bench_thread_pool          | 929 us                                                       | 950 us: 1.02x slower                                             |
| typing_runtime_protocols   | 176 us                                                       | 180 us: 1.02x slower                                             |
| mdp                        | 2.53 sec                                                     | 2.59 sec: 1.02x slower                                           |
| genshi_text                | 27.2 ms                                                      | 28.0 ms: 1.03x slower                                            |
| pickle_pure_python         | 322 us                                                       | 333 us: 1.03x slower                                             |
| json_dumps                 | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                            |
| logging_format             | 6.95 us                                                      | 7.21 us: 1.04x slower                                            |
| tornado_http               | 119 ms                                                       | 123 ms: 1.04x slower                                             |
| async_generators           | 364 ms                                                       | 379 ms: 1.04x slower                                             |
| sympy_expand               | 506 ms                                                       | 530 ms: 1.05x slower                                             |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.4 ms: 1.05x slower                                            |
| async_tree_io_tg           | 823 ms                                                       | 865 ms: 1.05x slower                                             |
| regex_compile              | 143 ms                                                       | 150 ms: 1.05x slower                                             |
| logging_simple             | 6.28 us                                                      | 6.62 us: 1.05x slower                                            |
| genshi_xml                 | 58.0 ms                                                      | 62.1 ms: 1.07x slower                                            |
| 2to3                       | 293 ms                                                       | 314 ms: 1.07x slower                                             |
| sympy_str                  | 297 ms                                                       | 319 ms: 1.08x slower                                             |
| comprehensions             | 17.3 us                                                      | 18.8 us: 1.09x slower                                            |
| create_gc_cycles           | 2.65 ms                                                      | 2.90 ms: 1.10x slower                                            |
| hexiom                     | 6.47 ms                                                      | 7.11 ms: 1.10x slower                                            |
| chaos                      | 60.6 ms                                                      | 66.5 ms: 1.10x slower                                            |
| sqlglot_parse              | 1.37 ms                                                      | 1.50 ms: 1.10x slower                                            |
| django_template            | 38.9 ms                                                      | 42.9 ms: 1.10x slower                                            |
| sqlglot_normalize          | 119 ms                                                       | 132 ms: 1.11x slower                                             |
| nqueens                    | 92.3 ms                                                      | 104 ms: 1.12x slower                                             |
| sqlglot_transpile          | 1.76 ms                                                      | 1.98 ms: 1.12x slower                                            |
| sympy_sum                  | 154 ms                                                       | 173 ms: 1.13x slower                                             |
| sphinx                     | 1.11 sec                                                     | 1.26 sec: 1.13x slower                                           |
| docutils                   | 2.81 sec                                                     | 3.17 sec: 1.13x slower                                           |
| generators                 | 33.9 ms                                                      | 39.4 ms: 1.16x slower                                            |
| gc_traversal               | 4.48 ms                                                      | 5.21 ms: 1.16x slower                                            |
| sympy_integrate            | 23.4 ms                                                      | 27.3 ms: 1.17x slower                                            |
| raytrace                   | 267 ms                                                       | 315 ms: 1.18x slower                                             |
| sqlglot_optimize           | 58.7 ms                                                      | 69.7 ms: 1.19x slower                                            |
| pylint                     | 345 ms                                                       | 423 ms: 1.23x slower                                             |
| bench_mp_pool              | 4.82 ms                                                      | 2.28 sec: 474.15x slower                                         |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                     |

Benchmark hidden because not significant (4): xml_etree_iterparse, json_loads, regex_v8, coroutines
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.002x slower
# HPT report

- Reliability score: 55.32% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x