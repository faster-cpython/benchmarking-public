# Results vs. base

- fork: brandtbucher
- ref: no_escape
- machine: linux-x86_64
- commit hash: 3bd6587
- commit date: 2024-07-24
- overall geometric mean: 1.00x faster
- HPT reliability: 94.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 271 ms: 1.00x faster                                             |
| html5lib       | 65.2 ms                                                               | 63.7 ms: 1.02x faster                                            |
| tornado_http   | 94.4 ms                                                               | 93.4 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                     |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| coroutines             | 22.7 ms                                                               | 22.5 ms: 1.01x faster                                            |
| asyncio_websockets     | 558 ms                                                                | 555 ms: 1.00x faster                                             |
| asyncio_tcp            | 501 ms                                                                | 504 ms: 1.01x slower                                             |
| asyncio_tcp_ssl        | 1.80 sec                                                              | 1.81 sec: 1.01x slower                                           |
| async_generators       | 455 ms                                                                | 459 ms: 1.01x slower                                             |
| async_tree_memoization | 414 ms                                                                | 426 ms: 1.03x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                     |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_none, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                     |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 136 ms                                                                | 135 ms: 1.01x faster                                             |
| regex_effbot   | 3.73 ms                                                               | 3.76 ms: 1.01x slower                                            |
| regex_v8       | 23.8 ms                                                               | 24.0 ms: 1.01x slower                                            |
| regex_dna      | 228 ms                                                                | 231 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|---------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_process   | 57.0 ms                                                               | 56.2 ms: 1.02x faster                                            |
| xml_etree_generate  | 81.4 ms                                                               | 80.2 ms: 1.01x faster                                            |
| tomli_loads         | 1.93 sec                                                              | 1.91 sec: 1.01x faster                                           |
| xml_etree_iterparse | 98.8 ms                                                               | 98.4 ms: 1.00x faster                                            |
| json_loads          | 27.7 us                                                               | 27.8 us: 1.00x slower                                            |
| pickle_pure_python  | 297 us                                                                | 302 us: 1.02x slower                                             |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                     |

Benchmark hidden because not significant (3): unpickle_pure_python, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                            |
| python_startup_no_site | 7.24 ms                                                               | 7.16 ms: 1.01x faster                                            |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 9.78 ms                                                               | 9.72 ms: 1.01x faster                                            |
| django_template | 35.9 ms                                                               | 36.3 ms: 1.01x slower                                            |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                     |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| mdp                     | 2.66 sec                                                              | 2.54 sec: 1.04x faster                                           |
| scimark_sparse_mat_mult | 4.34 ms                                                               | 4.22 ms: 1.03x faster                                            |
| nqueens                 | 87.0 ms                                                               | 84.8 ms: 1.03x faster                                            |
| html5lib                | 65.2 ms                                                               | 63.7 ms: 1.02x faster                                            |
| deepcopy_reduce         | 2.80 us                                                               | 2.74 us: 1.02x faster                                            |
| gc_traversal            | 3.86 ms                                                               | 3.79 ms: 1.02x faster                                            |
| pprint_safe_repr        | 717 ms                                                                | 704 ms: 1.02x faster                                             |
| xml_etree_process       | 57.0 ms                                                               | 56.2 ms: 1.02x faster                                            |
| xml_etree_generate      | 81.4 ms                                                               | 80.2 ms: 1.01x faster                                            |
| dulwich_log             | 69.8 ms                                                               | 68.9 ms: 1.01x faster                                            |
| python_startup          | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                            |
| tomli_loads             | 1.93 sec                                                              | 1.91 sec: 1.01x faster                                           |
| python_startup_no_site  | 7.24 ms                                                               | 7.16 ms: 1.01x faster                                            |
| tornado_http            | 94.4 ms                                                               | 93.4 ms: 1.01x faster                                            |
| telco                   | 7.88 ms                                                               | 7.81 ms: 1.01x faster                                            |
| fannkuch                | 369 ms                                                                | 366 ms: 1.01x faster                                             |
| coroutines              | 22.7 ms                                                               | 22.5 ms: 1.01x faster                                            |
| regex_compile           | 136 ms                                                                | 135 ms: 1.01x faster                                             |
| mako                    | 9.78 ms                                                               | 9.72 ms: 1.01x faster                                            |
| bpe_tokeniser           | 4.53 sec                                                              | 4.50 sec: 1.01x faster                                           |
| sympy_sum               | 170 ms                                                                | 169 ms: 1.01x faster                                             |
| asyncio_websockets      | 558 ms                                                                | 555 ms: 1.00x faster                                             |
| sympy_str               | 297 ms                                                                | 296 ms: 1.00x faster                                             |
| 2to3                    | 272 ms                                                                | 271 ms: 1.00x faster                                             |
| comprehensions          | 16.5 us                                                               | 16.5 us: 1.00x faster                                            |
| coverage                | 92.4 ms                                                               | 92.0 ms: 1.00x faster                                            |
| xml_etree_iterparse     | 98.8 ms                                                               | 98.4 ms: 1.00x faster                                            |
| sympy_integrate         | 22.2 ms                                                               | 22.2 ms: 1.00x faster                                            |
| create_gc_cycles        | 1.77 ms                                                               | 1.77 ms: 1.00x faster                                            |
| scimark_fft             | 307 ms                                                                | 308 ms: 1.00x slower                                             |
| json_loads              | 27.7 us                                                               | 27.8 us: 1.00x slower                                            |
| pidigits                | 185 ms                                                                | 186 ms: 1.00x slower                                             |
| asyncio_tcp             | 501 ms                                                                | 504 ms: 1.01x slower                                             |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.81 sec: 1.01x slower                                           |
| spectral_norm           | 101 ms                                                                | 101 ms: 1.01x slower                                             |
| deltablue               | 3.51 ms                                                               | 3.53 ms: 1.01x slower                                            |
| regex_effbot            | 3.73 ms                                                               | 3.76 ms: 1.01x slower                                            |
| thrift                  | 791 us                                                                | 797 us: 1.01x slower                                             |
| sqlglot_normalize       | 112 ms                                                                | 113 ms: 1.01x slower                                             |
| async_generators        | 455 ms                                                                | 459 ms: 1.01x slower                                             |
| regex_v8                | 23.8 ms                                                               | 24.0 ms: 1.01x slower                                            |
| pyflate                 | 436 ms                                                                | 440 ms: 1.01x slower                                             |
| pathlib                 | 16.0 ms                                                               | 16.2 ms: 1.01x slower                                            |
| django_template         | 35.9 ms                                                               | 36.3 ms: 1.01x slower                                            |
| raytrace                | 266 ms                                                                | 269 ms: 1.01x slower                                             |
| regex_dna               | 228 ms                                                                | 231 ms: 1.01x slower                                             |
| pickle_pure_python      | 297 us                                                                | 302 us: 1.02x slower                                             |
| deepcopy                | 269 us                                                                | 275 us: 1.02x slower                                             |
| scimark_sor             | 125 ms                                                                | 128 ms: 1.02x slower                                             |
| async_tree_memoization  | 414 ms                                                                | 426 ms: 1.03x slower                                             |
| richards                | 40.1 ms                                                               | 41.5 ms: 1.03x slower                                            |
| richards_super          | 45.9 ms                                                               | 47.6 ms: 1.04x slower                                            |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                     |

Benchmark hidden because not significant (39): unpickle_pure_python, genshi_text, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, json, async_tree_io, dask, deepcopy_memo, crypto_pyaes, async_tree_io_tg, nbody, async_tree_none, sqlglot_transpile, hexiom, logging_silent, logging_format, docutils, generators, bench_thread_pool, logging_simple, xml_etree_parse, sympy_expand, sqlglot_parse, go, bench_mp_pool, scimark_monte_carlo, meteor_contest, pylint, async_tree_none_tg, typing_runtime_protocols, sqlglot_optimize, chaos, float, scimark_lu, async_tree_memoization_tg, json_dumps, pycparser, pprint_pformat, genshi_xml

# HPT report

- Reliability score: 94.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x