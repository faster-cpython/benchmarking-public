# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.027x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                             |
| docutils       | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                           |
| html5lib       | 72.9 ms                                                      | 71.1 ms: 1.03x faster                                            |
| tornado_http   | 119 ms                                                       | 117 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 386 ms: 1.19x faster                                             |
| async_tree_none            | 370 ms                                                       | 332 ms: 1.12x faster                                             |
| async_tree_memoization     | 447 ms                                                       | 415 ms: 1.08x faster                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 558 ms: 1.07x faster                                             |
| async_tree_none_tg         | 342 ms                                                       | 323 ms: 1.06x faster                                             |
| asyncio_websockets         | 395 ms                                                       | 385 ms: 1.03x faster                                             |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                            |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 563 ms: 1.02x faster                                             |
| async_tree_io_tg           | 823 ms                                                       | 837 ms: 1.02x slower                                             |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                     |

Benchmark hidden because not significant (2): async_tree_io, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 82.2 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 139 ms: 1.03x faster                                             |
| regex_effbot   | 3.51 ms                                                      | 3.43 ms: 1.03x faster                                            |
| regex_v8       | 24.9 ms                                                      | 24.7 ms: 1.01x faster                                            |
| regex_dna      | 238 ms                                                       | 243 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_process    | 60.7 ms                                                      | 60.0 ms: 1.01x faster                                            |
| unpickle_pure_python | 216 us                                                       | 214 us: 1.01x faster                                             |
| pickle_pure_python   | 322 us                                                       | 320 us: 1.00x faster                                             |
| xml_etree_iterparse  | 99.8 ms                                                      | 102 ms: 1.02x slower                                             |
| json_loads           | 24.7 us                                                      | 25.3 us: 1.02x slower                                            |
| tomli_loads          | 2.43 sec                                                     | 2.50 sec: 1.03x slower                                           |
| json_dumps           | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                            |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 15.0 ms: 1.05x faster                                            |
| python_startup_no_site | 8.93 ms                                                      | 8.96 ms: 1.00x slower                                            |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                            |
| genshi_xml      | 58.0 ms                                                      | 54.4 ms: 1.07x faster                                            |
| mako            | 10.3 ms                                                      | 10.7 ms: 1.04x slower                                            |
| django_template | 38.9 ms                                                      | 41.0 ms: 1.06x slower                                            |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 289 us: 1.34x faster                                             |
| deepcopy_memo              | 38.9 us                                                      | 29.4 us: 1.32x faster                                            |
| go                         | 167 ms                                                       | 133 ms: 1.26x faster                                             |
| async_tree_memoization_tg  | 458 ms                                                       | 386 ms: 1.19x faster                                             |
| deepcopy_reduce            | 3.49 us                                                      | 2.96 us: 1.18x faster                                            |
| generators                 | 33.9 ms                                                      | 29.3 ms: 1.16x faster                                            |
| scimark_sor                | 125 ms                                                       | 111 ms: 1.13x faster                                             |
| async_tree_none            | 370 ms                                                       | 332 ms: 1.12x faster                                             |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                            |
| json                       | 5.62 ms                                                      | 5.16 ms: 1.09x faster                                            |
| genshi_text                | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                            |
| fannkuch                   | 384 ms                                                       | 354 ms: 1.09x faster                                             |
| richards_super             | 60.2 ms                                                      | 55.6 ms: 1.08x faster                                            |
| async_tree_memoization     | 447 ms                                                       | 415 ms: 1.08x faster                                             |
| genshi_xml                 | 58.0 ms                                                      | 54.4 ms: 1.07x faster                                            |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 558 ms: 1.07x faster                                             |
| telco                      | 8.77 ms                                                      | 8.23 ms: 1.07x faster                                            |
| richards                   | 52.5 ms                                                      | 49.5 ms: 1.06x faster                                            |
| async_tree_none_tg         | 342 ms                                                       | 323 ms: 1.06x faster                                             |
| thrift                     | 918 us                                                       | 873 us: 1.05x faster                                             |
| pyflate                    | 493 ms                                                       | 469 ms: 1.05x faster                                             |
| nqueens                    | 92.3 ms                                                      | 88.0 ms: 1.05x faster                                            |
| bpe_tokeniser              | 5.09 sec                                                     | 4.86 sec: 1.05x faster                                           |
| python_startup             | 15.6 ms                                                      | 15.0 ms: 1.05x faster                                            |
| pprint_pformat             | 1.70 sec                                                     | 1.63 sec: 1.04x faster                                           |
| meteor_contest             | 130 ms                                                       | 125 ms: 1.04x faster                                             |
| scimark_fft                | 298 ms                                                       | 286 ms: 1.04x faster                                             |
| pprint_safe_repr           | 835 ms                                                       | 803 ms: 1.04x faster                                             |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.06 ms: 1.04x faster                                            |
| hexiom                     | 6.47 ms                                                      | 6.24 ms: 1.04x faster                                            |
| scimark_lu                 | 97.4 ms                                                      | 94.2 ms: 1.03x faster                                            |
| regex_compile              | 143 ms                                                       | 139 ms: 1.03x faster                                             |
| pycparser                  | 1.28 sec                                                     | 1.25 sec: 1.03x faster                                           |
| asyncio_websockets         | 395 ms                                                       | 385 ms: 1.03x faster                                             |
| html5lib                   | 72.9 ms                                                      | 71.1 ms: 1.03x faster                                            |
| regex_effbot               | 3.51 ms                                                      | 3.43 ms: 1.03x faster                                            |
| bench_thread_pool          | 929 us                                                       | 908 us: 1.02x faster                                             |
| coverage                   | 84.5 ms                                                      | 82.6 ms: 1.02x faster                                            |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                            |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 563 ms: 1.02x faster                                             |
| tornado_http               | 119 ms                                                       | 117 ms: 1.02x faster                                             |
| typing_runtime_protocols   | 176 us                                                       | 173 us: 1.02x faster                                             |
| sympy_expand               | 506 ms                                                       | 498 ms: 1.02x faster                                             |
| spectral_norm              | 97.4 ms                                                      | 96.0 ms: 1.01x faster                                            |
| xml_etree_process          | 60.7 ms                                                      | 60.0 ms: 1.01x faster                                            |
| sympy_str                  | 297 ms                                                       | 293 ms: 1.01x faster                                             |
| mdp                        | 2.53 sec                                                     | 2.51 sec: 1.01x faster                                           |
| regex_v8                   | 24.9 ms                                                      | 24.7 ms: 1.01x faster                                            |
| unpickle_pure_python       | 216 us                                                       | 214 us: 1.01x faster                                             |
| sympy_sum                  | 154 ms                                                       | 153 ms: 1.01x faster                                             |
| pickle_pure_python         | 322 us                                                       | 320 us: 1.00x faster                                             |
| sqlglot_normalize          | 119 ms                                                       | 118 ms: 1.00x faster                                             |
| python_startup_no_site     | 8.93 ms                                                      | 8.96 ms: 1.00x slower                                            |
| logging_silent             | 97.5 ns                                                      | 98.0 ns: 1.01x slower                                            |
| sqlglot_transpile          | 1.76 ms                                                      | 1.77 ms: 1.01x slower                                            |
| float                      | 81.6 ms                                                      | 82.2 ms: 1.01x slower                                            |
| comprehensions             | 17.3 us                                                      | 17.4 us: 1.01x slower                                            |
| sqlglot_optimize           | 58.7 ms                                                      | 59.1 ms: 1.01x slower                                            |
| raytrace                   | 267 ms                                                       | 270 ms: 1.01x slower                                             |
| xml_etree_iterparse        | 99.8 ms                                                      | 102 ms: 1.02x slower                                             |
| async_tree_io_tg           | 823 ms                                                       | 837 ms: 1.02x slower                                             |
| deltablue                  | 3.38 ms                                                      | 3.44 ms: 1.02x slower                                            |
| regex_dna                  | 238 ms                                                       | 243 ms: 1.02x slower                                             |
| sqlglot_parse              | 1.37 ms                                                      | 1.39 ms: 1.02x slower                                            |
| json_loads                 | 24.7 us                                                      | 25.3 us: 1.02x slower                                            |
| tomli_loads                | 2.43 sec                                                     | 2.50 sec: 1.03x slower                                           |
| logging_format             | 6.95 us                                                      | 7.14 us: 1.03x slower                                            |
| dulwich_log                | 65.5 ms                                                      | 67.5 ms: 1.03x slower                                            |
| docutils                   | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                           |
| mako                       | 10.3 ms                                                      | 10.7 ms: 1.04x slower                                            |
| logging_simple             | 6.28 us                                                      | 6.57 us: 1.05x slower                                            |
| json_dumps                 | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                            |
| django_template            | 38.9 ms                                                      | 41.0 ms: 1.06x slower                                            |
| create_gc_cycles           | 2.65 ms                                                      | 2.97 ms: 1.12x slower                                            |
| gc_traversal               | 4.48 ms                                                      | 5.32 ms: 1.19x slower                                            |
| bench_mp_pool              | 4.82 ms                                                      | 1.94 sec: 402.16x slower                                         |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                     |

Benchmark hidden because not significant (12): nbody, async_tree_io, crypto_pyaes, pidigits, xml_etree_generate, async_generators, sympy_integrate, xml_etree_parse, pylint, chaos, scimark_monte_carlo, sphinx
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.027x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x