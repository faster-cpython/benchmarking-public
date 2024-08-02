# Results vs. base

- fork: brandtbucher
- ref: binary_op_inplace_ad
- machine: linux-x86_64
- commit hash: cfb0a0a
- commit date: 2024-07-24
- overall geometric mean: 1.00x slower
- HPT reliability: 59.62%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 273 ms: 1.00x slower                                                        |
| docutils       | 2.90 sec                                                              | 2.92 sec: 1.01x slower                                                      |
| html5lib       | 65.2 ms                                                               | 64.6 ms: 1.01x faster                                                       |
| tornado_http   | 94.4 ms                                                               | 95.4 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_generators | 455 ms                                                                | 453 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl  | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                      |
| asyncio_tcp      | 501 ms                                                                | 504 ms: 1.00x slower                                                        |
| coroutines       | 22.7 ms                                                               | 23.2 ms: 1.02x slower                                                       |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (9): async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io, asyncio_websockets, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 81.6 ms                                                               | 79.8 ms: 1.02x faster                                                       |
| float          | 70.5 ms                                                               | 70.1 ms: 1.01x faster                                                       |
| pidigits       | 185 ms                                                                | 185 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 228 ms                                                                | 222 ms: 1.03x faster                                                        |
| regex_compile  | 136 ms                                                                | 134 ms: 1.01x faster                                                        |
| regex_effbot   | 3.73 ms                                                               | 3.77 ms: 1.01x slower                                                       |
| regex_v8       | 23.8 ms                                                               | 25.4 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads        | 1.93 sec                                                              | 1.92 sec: 1.01x faster                                                      |
| xml_etree_process  | 57.0 ms                                                               | 56.7 ms: 1.01x faster                                                       |
| pickle_pure_python | 297 us                                                                | 299 us: 1.01x slower                                                        |
| json_dumps         | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                       |
| json_loads         | 27.7 us                                                               | 28.1 us: 1.01x slower                                                       |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_iterparse, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                       |
| python_startup_no_site | 7.24 ms                                                               | 7.21 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 9.78 ms                                                               | 9.80 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                     | 2.66 sec                                                              | 2.52 sec: 1.05x faster                                                      |
| gc_traversal            | 3.86 ms                                                               | 3.68 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult | 4.34 ms                                                               | 4.22 ms: 1.03x faster                                                       |
| regex_dna               | 228 ms                                                                | 222 ms: 1.03x faster                                                        |
| nbody                   | 81.6 ms                                                               | 79.8 ms: 1.02x faster                                                       |
| meteor_contest          | 106 ms                                                                | 104 ms: 1.02x faster                                                        |
| deepcopy_reduce         | 2.80 us                                                               | 2.75 us: 1.02x faster                                                       |
| fannkuch                | 369 ms                                                                | 365 ms: 1.01x faster                                                        |
| regex_compile           | 136 ms                                                                | 134 ms: 1.01x faster                                                        |
| comprehensions          | 16.5 us                                                               | 16.4 us: 1.01x faster                                                       |
| html5lib                | 65.2 ms                                                               | 64.6 ms: 1.01x faster                                                       |
| create_gc_cycles        | 1.77 ms                                                               | 1.76 ms: 1.01x faster                                                       |
| pyflate                 | 436 ms                                                                | 432 ms: 1.01x faster                                                        |
| sqlglot_normalize       | 112 ms                                                                | 111 ms: 1.01x faster                                                        |
| tomli_loads             | 1.93 sec                                                              | 1.92 sec: 1.01x faster                                                      |
| xml_etree_process       | 57.0 ms                                                               | 56.7 ms: 1.01x faster                                                       |
| float                   | 70.5 ms                                                               | 70.1 ms: 1.01x faster                                                       |
| python_startup          | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                       |
| python_startup_no_site  | 7.24 ms                                                               | 7.21 ms: 1.00x faster                                                       |
| async_generators        | 455 ms                                                                | 453 ms: 1.00x faster                                                        |
| pidigits                | 185 ms                                                                | 185 ms: 1.00x faster                                                        |
| mako                    | 9.78 ms                                                               | 9.80 ms: 1.00x slower                                                       |
| sqlglot_optimize        | 55.8 ms                                                               | 56.0 ms: 1.00x slower                                                       |
| 2to3                    | 272 ms                                                                | 273 ms: 1.00x slower                                                        |
| sympy_integrate         | 22.2 ms                                                               | 22.3 ms: 1.00x slower                                                       |
| hexiom                  | 6.52 ms                                                               | 6.55 ms: 1.00x slower                                                       |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                      |
| spectral_norm           | 101 ms                                                                | 101 ms: 1.00x slower                                                        |
| asyncio_tcp             | 501 ms                                                                | 504 ms: 1.00x slower                                                        |
| scimark_fft             | 307 ms                                                                | 309 ms: 1.01x slower                                                        |
| sympy_str               | 297 ms                                                                | 299 ms: 1.01x slower                                                        |
| sympy_expand            | 501 ms                                                                | 506 ms: 1.01x slower                                                        |
| regex_effbot            | 3.73 ms                                                               | 3.77 ms: 1.01x slower                                                       |
| pickle_pure_python      | 297 us                                                                | 299 us: 1.01x slower                                                        |
| docutils                | 2.90 sec                                                              | 2.92 sec: 1.01x slower                                                      |
| bench_thread_pool       | 822 us                                                                | 831 us: 1.01x slower                                                        |
| tornado_http            | 94.4 ms                                                               | 95.4 ms: 1.01x slower                                                       |
| thrift                  | 791 us                                                                | 800 us: 1.01x slower                                                        |
| json_dumps              | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                       |
| pathlib                 | 16.0 ms                                                               | 16.2 ms: 1.01x slower                                                       |
| go                      | 145 ms                                                                | 147 ms: 1.01x slower                                                        |
| json_loads              | 27.7 us                                                               | 28.1 us: 1.01x slower                                                       |
| logging_format          | 6.14 us                                                               | 6.24 us: 1.02x slower                                                       |
| richards_super          | 45.9 ms                                                               | 46.7 ms: 1.02x slower                                                       |
| richards                | 40.1 ms                                                               | 40.8 ms: 1.02x slower                                                       |
| raytrace                | 266 ms                                                                | 271 ms: 1.02x slower                                                        |
| dulwich_log             | 69.8 ms                                                               | 71.2 ms: 1.02x slower                                                       |
| coroutines              | 22.7 ms                                                               | 23.2 ms: 1.02x slower                                                       |
| deltablue               | 3.51 ms                                                               | 3.60 ms: 1.03x slower                                                       |
| scimark_lu              | 124 ms                                                                | 128 ms: 1.03x slower                                                        |
| logging_silent          | 103 ns                                                                | 107 ns: 1.04x slower                                                        |
| pycparser               | 1.12 sec                                                              | 1.17 sec: 1.04x slower                                                      |
| scimark_sor             | 125 ms                                                                | 132 ms: 1.05x slower                                                        |
| regex_v8                | 23.8 ms                                                               | 25.4 ms: 1.07x slower                                                       |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (37): async_tree_none, pprint_safe_repr, async_tree_cpu_io_mixed, xml_etree_generate, json, coverage, async_tree_cpu_io_mixed_tg, async_tree_none_tg, django_template, async_tree_io, genshi_text, telco, asyncio_websockets, logging_simple, async_tree_io_tg, bench_mp_pool, bpe_tokeniser, dask, generators, xml_etree_iterparse, genshi_xml, nqueens, unpickle_pure_python, scimark_monte_carlo, typing_runtime_protocols, sqlglot_transpile, sqlglot_parse, chaos, sympy_sum, deepcopy, async_tree_memoization_tg, pylint, pprint_pformat, xml_etree_parse, deepcopy_memo, crypto_pyaes, async_tree_memoization

# HPT report

- Reliability score: 59.62% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x