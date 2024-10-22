# Results vs. base

- fork: brandtbucher
- ref: exit_operand
- machine: linux-x86_64
- commit hash: d4c66d7
- commit date: 2024-07-24
- overall geometric mean: 1.01x slower
- HPT reliability: 99.31%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 274 ms: 1.01x slower                                                |
| docutils       | 2.90 sec                                                              | 2.91 sec: 1.01x slower                                              |
| html5lib       | 65.2 ms                                                               | 63.9 ms: 1.02x faster                                               |
| tornado_http   | 94.4 ms                                                               | 94.1 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp_ssl  | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                              |
| asyncio_tcp      | 501 ms                                                                | 505 ms: 1.01x slower                                                |
| coroutines       | 22.7 ms                                                               | 23.1 ms: 1.02x slower                                               |
| async_generators | 455 ms                                                                | 465 ms: 1.02x slower                                                |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (9): async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_none_tg, asyncio_websockets, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 81.6 ms                                                               | 80.4 ms: 1.01x faster                                               |
| pidigits       | 185 ms                                                                | 185 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 228 ms                                                                | 229 ms: 1.00x slower                                                |
| regex_compile  | 136 ms                                                                | 139 ms: 1.03x slower                                                |
| regex_effbot   | 3.73 ms                                                               | 3.94 ms: 1.06x slower                                               |
| regex_v8       | 23.8 ms                                                               | 25.3 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_generate  | 81.4 ms                                                               | 80.7 ms: 1.01x faster                                               |
| xml_etree_iterparse | 98.8 ms                                                               | 100 ms: 1.01x slower                                                |
| xml_etree_parse     | 146 ms                                                                | 148 ms: 1.02x slower                                                |
| xml_etree_process   | 57.0 ms                                                               | 57.9 ms: 1.02x slower                                               |
| json_loads          | 27.7 us                                                               | 28.2 us: 1.02x slower                                               |
| tomli_loads         | 1.93 sec                                                              | 1.97 sec: 1.02x slower                                              |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                        |

Benchmark hidden because not significant (3): unpickle_pure_python, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                               |
| python_startup_no_site | 7.24 ms                                                               | 7.19 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text    | 24.6 ms                                                               | 25.0 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (3): genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark               | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                     | 2.66 sec                                                              | 2.55 sec: 1.04x faster                                              |
| gc_traversal            | 3.86 ms                                                               | 3.72 ms: 1.04x faster                                               |
| html5lib                | 65.2 ms                                                               | 63.9 ms: 1.02x faster                                               |
| coverage                | 92.4 ms                                                               | 90.9 ms: 1.02x faster                                               |
| nbody                   | 81.6 ms                                                               | 80.4 ms: 1.01x faster                                               |
| create_gc_cycles        | 1.77 ms                                                               | 1.75 ms: 1.01x faster                                               |
| xml_etree_generate      | 81.4 ms                                                               | 80.7 ms: 1.01x faster                                               |
| python_startup          | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                               |
| python_startup_no_site  | 7.24 ms                                                               | 7.19 ms: 1.01x faster                                               |
| tornado_http            | 94.4 ms                                                               | 94.1 ms: 1.00x faster                                               |
| pidigits                | 185 ms                                                                | 185 ms: 1.00x faster                                                |
| regex_dna               | 228 ms                                                                | 229 ms: 1.00x slower                                                |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                              |
| bpe_tokeniser           | 4.53 sec                                                              | 4.54 sec: 1.00x slower                                              |
| sympy_integrate         | 22.2 ms                                                               | 22.3 ms: 1.00x slower                                               |
| pathlib                 | 16.0 ms                                                               | 16.1 ms: 1.00x slower                                               |
| scimark_sparse_mat_mult | 4.34 ms                                                               | 4.36 ms: 1.00x slower                                               |
| 2to3                    | 272 ms                                                                | 274 ms: 1.01x slower                                                |
| sqlglot_optimize        | 55.8 ms                                                               | 56.1 ms: 1.01x slower                                               |
| docutils                | 2.90 sec                                                              | 2.91 sec: 1.01x slower                                              |
| sqlglot_transpile       | 1.61 ms                                                               | 1.61 ms: 1.01x slower                                               |
| sqlglot_normalize       | 112 ms                                                                | 113 ms: 1.01x slower                                                |
| chaos                   | 58.0 ms                                                               | 58.3 ms: 1.01x slower                                               |
| sympy_str               | 297 ms                                                                | 299 ms: 1.01x slower                                                |
| thrift                  | 791 us                                                                | 797 us: 1.01x slower                                                |
| asyncio_tcp             | 501 ms                                                                | 505 ms: 1.01x slower                                                |
| sympy_expand            | 501 ms                                                                | 506 ms: 1.01x slower                                                |
| bench_thread_pool       | 822 us                                                                | 834 us: 1.01x slower                                                |
| xml_etree_iterparse     | 98.8 ms                                                               | 100 ms: 1.01x slower                                                |
| xml_etree_parse         | 146 ms                                                                | 148 ms: 1.02x slower                                                |
| xml_etree_process       | 57.0 ms                                                               | 57.9 ms: 1.02x slower                                               |
| hexiom                  | 6.52 ms                                                               | 6.62 ms: 1.02x slower                                               |
| genshi_text             | 24.6 ms                                                               | 25.0 ms: 1.02x slower                                               |
| scimark_monte_carlo     | 59.9 ms                                                               | 60.9 ms: 1.02x slower                                               |
| json_loads              | 27.7 us                                                               | 28.2 us: 1.02x slower                                               |
| crypto_pyaes            | 66.8 ms                                                               | 68.0 ms: 1.02x slower                                               |
| scimark_fft             | 307 ms                                                                | 313 ms: 1.02x slower                                                |
| generators              | 28.9 ms                                                               | 29.4 ms: 1.02x slower                                               |
| deepcopy_reduce         | 2.80 us                                                               | 2.85 us: 1.02x slower                                               |
| tomli_loads             | 1.93 sec                                                              | 1.97 sec: 1.02x slower                                              |
| nqueens                 | 87.0 ms                                                               | 88.7 ms: 1.02x slower                                               |
| logging_silent          | 103 ns                                                                | 105 ns: 1.02x slower                                                |
| go                      | 145 ms                                                                | 148 ms: 1.02x slower                                                |
| scimark_lu              | 124 ms                                                                | 127 ms: 1.02x slower                                                |
| coroutines              | 22.7 ms                                                               | 23.1 ms: 1.02x slower                                               |
| richards                | 40.1 ms                                                               | 41.0 ms: 1.02x slower                                               |
| async_generators        | 455 ms                                                                | 465 ms: 1.02x slower                                                |
| richards_super          | 45.9 ms                                                               | 47.1 ms: 1.02x slower                                               |
| regex_compile           | 136 ms                                                                | 139 ms: 1.03x slower                                                |
| deepcopy                | 269 us                                                                | 277 us: 1.03x slower                                                |
| spectral_norm           | 101 ms                                                                | 104 ms: 1.03x slower                                                |
| raytrace                | 266 ms                                                                | 274 ms: 1.03x slower                                                |
| scimark_sor             | 125 ms                                                                | 130 ms: 1.03x slower                                                |
| deltablue               | 3.51 ms                                                               | 3.64 ms: 1.04x slower                                               |
| deepcopy_memo           | 28.2 us                                                               | 29.4 us: 1.04x slower                                               |
| pycparser               | 1.12 sec                                                              | 1.17 sec: 1.05x slower                                              |
| regex_effbot            | 3.73 ms                                                               | 3.94 ms: 1.06x slower                                               |
| regex_v8                | 23.8 ms                                                               | 25.3 ms: 1.06x slower                                               |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                        |

Benchmark hidden because not significant (33): async_tree_io, async_tree_io_tg, logging_format, typing_runtime_protocols, async_tree_cpu_io_mixed, async_tree_none, pprint_pformat, genshi_xml, logging_simple, fannkuch, pprint_safe_repr, async_tree_none_tg, sqlglot_parse, asyncio_websockets, meteor_contest, comprehensions, sympy_sum, async_tree_memoization_tg, django_template, bench_mp_pool, dask, dulwich_log, mako, async_tree_cpu_io_mixed_tg, json, pyflate, telco, float, unpickle_pure_python, pickle_pure_python, json_dumps, pylint, async_tree_memoization

# HPT report

- Reliability score: 99.31% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x