# Results vs. base

- fork: faster-cpython
- ref: remove_build_const_k
- machine: linux-x86_64
- commit hash: bcb5b37
- commit date: 2024-07-23
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.72 sec                                                              | 2.70 sec: 1.01x faster                                                          |
| html5lib       | 64.5 ms                                                               | 63.5 ms: 1.02x faster                                                           |
| tornado_http   | 90.0 ms                                                               | 89.7 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                 | 22.8 ms                                                               | 22.2 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                                              | 1.78 sec: 1.00x faster                                                          |
| async_tree_cpu_io_mixed_tg | 535 ms                                                                | 541 ms: 1.01x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (10): async_tree_none, async_tree_io, async_tree_memoization, async_tree_memoization_tg, asyncio_websockets, async_generators, asyncio_tcp, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 87.2 ms                                                               | 86.5 ms: 1.01x faster                                                           |
| pidigits       | 187 ms                                                                | 188 ms: 1.00x slower                                                            |
| float          | 76.5 ms                                                               | 77.3 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 131 ms                                                                | 129 ms: 1.01x faster                                                            |
| regex_effbot   | 3.62 ms                                                               | 3.69 ms: 1.02x slower                                                           |
| regex_v8       | 24.6 ms                                                               | 25.4 ms: 1.03x slower                                                           |
| regex_dna      | 217 ms                                                                | 225 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                                | 153 ms: 1.03x faster                                                            |
| unpickle_pure_python | 214 us                                                                | 209 us: 1.02x faster                                                            |
| xml_etree_process    | 58.9 ms                                                               | 58.1 ms: 1.01x faster                                                           |
| pickle_pure_python   | 299 us                                                                | 296 us: 1.01x faster                                                            |
| xml_etree_generate   | 85.2 ms                                                               | 84.5 ms: 1.01x faster                                                           |
| json_loads           | 27.3 us                                                               | 28.1 us: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (3): tomli_loads, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.09 ms                                                               | 7.09 ms: 1.00x faster                                                           |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml     | 50.4 ms                                                               | 49.1 ms: 1.03x faster                                                           |
| mako           | 10.9 ms                                                               | 10.8 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| spectral_norm              | 116 ms                                                                | 104 ms: 1.11x faster                                                            |
| scimark_sparse_mat_mult    | 4.80 ms                                                               | 4.35 ms: 1.10x faster                                                           |
| mdp                        | 2.70 sec                                                              | 2.53 sec: 1.07x faster                                                          |
| crypto_pyaes               | 74.6 ms                                                               | 70.5 ms: 1.06x faster                                                           |
| xml_etree_parse            | 159 ms                                                                | 153 ms: 1.03x faster                                                            |
| gc_traversal               | 3.65 ms                                                               | 3.54 ms: 1.03x faster                                                           |
| genshi_xml                 | 50.4 ms                                                               | 49.1 ms: 1.03x faster                                                           |
| coroutines                 | 22.8 ms                                                               | 22.2 ms: 1.03x faster                                                           |
| scimark_fft                | 364 ms                                                                | 356 ms: 1.02x faster                                                            |
| fannkuch                   | 405 ms                                                                | 395 ms: 1.02x faster                                                            |
| scimark_lu                 | 113 ms                                                                | 110 ms: 1.02x faster                                                            |
| scimark_sor                | 124 ms                                                                | 121 ms: 1.02x faster                                                            |
| unpickle_pure_python       | 214 us                                                                | 209 us: 1.02x faster                                                            |
| deepcopy_memo              | 29.6 us                                                               | 29.0 us: 1.02x faster                                                           |
| chaos                      | 58.7 ms                                                               | 57.6 ms: 1.02x faster                                                           |
| mako                       | 10.9 ms                                                               | 10.8 ms: 1.02x faster                                                           |
| html5lib                   | 64.5 ms                                                               | 63.5 ms: 1.02x faster                                                           |
| xml_etree_process          | 58.9 ms                                                               | 58.1 ms: 1.01x faster                                                           |
| logging_silent             | 99.4 ns                                                               | 98.1 ns: 1.01x faster                                                           |
| regex_compile              | 131 ms                                                                | 129 ms: 1.01x faster                                                            |
| pathlib                    | 15.8 ms                                                               | 15.6 ms: 1.01x faster                                                           |
| pprint_safe_repr           | 730 ms                                                                | 722 ms: 1.01x faster                                                            |
| bpe_tokeniser              | 4.84 sec                                                              | 4.79 sec: 1.01x faster                                                          |
| pickle_pure_python         | 299 us                                                                | 296 us: 1.01x faster                                                            |
| hexiom                     | 6.12 ms                                                               | 6.06 ms: 1.01x faster                                                           |
| raytrace                   | 255 ms                                                                | 253 ms: 1.01x faster                                                            |
| generators                 | 27.9 ms                                                               | 27.7 ms: 1.01x faster                                                           |
| pprint_pformat             | 1.50 sec                                                              | 1.48 sec: 1.01x faster                                                          |
| xml_etree_generate         | 85.2 ms                                                               | 84.5 ms: 1.01x faster                                                           |
| nbody                      | 87.2 ms                                                               | 86.5 ms: 1.01x faster                                                           |
| sympy_sum                  | 151 ms                                                                | 150 ms: 1.01x faster                                                            |
| docutils                   | 2.72 sec                                                              | 2.70 sec: 1.01x faster                                                          |
| logging_simple             | 5.44 us                                                               | 5.40 us: 1.01x faster                                                           |
| go                         | 140 ms                                                                | 139 ms: 1.01x faster                                                            |
| richards_super             | 52.0 ms                                                               | 51.7 ms: 1.01x faster                                                           |
| sqlglot_parse              | 1.26 ms                                                               | 1.25 ms: 1.01x faster                                                           |
| create_gc_cycles           | 1.74 ms                                                               | 1.73 ms: 1.00x faster                                                           |
| dulwich_log                | 63.7 ms                                                               | 63.4 ms: 1.00x faster                                                           |
| sympy_integrate            | 19.7 ms                                                               | 19.7 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                                              | 1.78 sec: 1.00x faster                                                          |
| sqlglot_normalize          | 105 ms                                                                | 105 ms: 1.00x faster                                                            |
| meteor_contest             | 108 ms                                                                | 107 ms: 1.00x faster                                                            |
| tornado_http               | 90.0 ms                                                               | 89.7 ms: 1.00x faster                                                           |
| sqlglot_optimize           | 52.9 ms                                                               | 52.8 ms: 1.00x faster                                                           |
| python_startup_no_site     | 7.09 ms                                                               | 7.09 ms: 1.00x faster                                                           |
| python_startup             | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                           |
| pidigits                   | 187 ms                                                                | 188 ms: 1.00x slower                                                            |
| richards                   | 45.5 ms                                                               | 45.6 ms: 1.00x slower                                                           |
| thrift                     | 773 us                                                                | 777 us: 1.00x slower                                                            |
| nqueens                    | 79.9 ms                                                               | 80.5 ms: 1.01x slower                                                           |
| telco                      | 8.08 ms                                                               | 8.15 ms: 1.01x slower                                                           |
| json                       | 5.01 ms                                                               | 5.06 ms: 1.01x slower                                                           |
| float                      | 76.5 ms                                                               | 77.3 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 535 ms                                                                | 541 ms: 1.01x slower                                                            |
| regex_effbot               | 3.62 ms                                                               | 3.69 ms: 1.02x slower                                                           |
| pyflate                    | 473 ms                                                                | 482 ms: 1.02x slower                                                            |
| deepcopy_reduce            | 2.59 us                                                               | 2.65 us: 1.02x slower                                                           |
| deepcopy                   | 254 us                                                                | 261 us: 1.03x slower                                                            |
| json_loads                 | 27.3 us                                                               | 28.1 us: 1.03x slower                                                           |
| regex_v8                   | 24.6 ms                                                               | 25.4 ms: 1.03x slower                                                           |
| regex_dna                  | 217 ms                                                                | 225 ms: 1.04x slower                                                            |
| pycparser                  | 1.12 sec                                                              | 1.17 sec: 1.05x slower                                                          |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (29): async_tree_none, dask, async_tree_io, sympy_expand, tomli_loads, async_tree_memoization, coverage, xml_etree_iterparse, genshi_text, async_tree_memoization_tg, pylint, asyncio_websockets, sqlglot_transpile, bench_mp_pool, async_generators, 2to3, bench_thread_pool, logging_format, django_template, comprehensions, asyncio_tcp, sympy_str, scimark_monte_carlo, async_tree_cpu_io_mixed, json_dumps, deltablue, async_tree_io_tg, async_tree_none_tg, typing_runtime_protocols

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x