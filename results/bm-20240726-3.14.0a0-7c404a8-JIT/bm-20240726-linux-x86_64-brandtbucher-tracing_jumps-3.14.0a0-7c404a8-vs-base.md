# Results vs. base

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: 7c404a8
- commit date: 2024-07-26
- overall geometric mean: 1.00x slower
- HPT reliability: 74.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 275 ms: 1.01x slower                                                 |
| tornado_http   | 94.4 ms                                                               | 92.5 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization | 414 ms                                                                | 394 ms: 1.05x faster                                                 |
| asyncio_tcp            | 501 ms                                                                | 498 ms: 1.01x faster                                                 |
| asyncio_websockets     | 558 ms                                                                | 555 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl        | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (9): async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_generators, coroutines, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 81.6 ms                                                               | 80.2 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 228 ms                                                                | 221 ms: 1.03x faster                                                 |
| regex_compile  | 136 ms                                                                | 134 ms: 1.01x faster                                                 |
| regex_effbot   | 3.73 ms                                                               | 3.79 ms: 1.02x slower                                                |
| regex_v8       | 23.8 ms                                                               | 25.9 ms: 1.09x slower                                                |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_process  | 57.0 ms                                                               | 56.1 ms: 1.02x faster                                                |
| xml_etree_generate | 81.4 ms                                                               | 80.6 ms: 1.01x faster                                                |
| tomli_loads        | 1.93 sec                                                              | 1.97 sec: 1.02x slower                                               |
| json_loads         | 27.7 us                                                               | 28.3 us: 1.02x slower                                                |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (5): unpickle_pure_python, json_dumps, xml_etree_iterparse, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                |
| python_startup_no_site | 7.24 ms                                                               | 7.17 ms: 1.01x faster                                                |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml     | 58.0 ms                                                               | 53.1 ms: 1.09x faster                                                |
| genshi_text    | 24.6 ms                                                               | 24.2 ms: 1.02x faster                                                |
| mako           | 9.78 ms                                                               | 9.65 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                         |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml               | 58.0 ms                                                               | 53.1 ms: 1.09x faster                                                |
| async_tree_memoization   | 414 ms                                                                | 394 ms: 1.05x faster                                                 |
| regex_dna                | 228 ms                                                                | 221 ms: 1.03x faster                                                 |
| nqueens                  | 87.0 ms                                                               | 84.4 ms: 1.03x faster                                                |
| gc_traversal             | 3.86 ms                                                               | 3.77 ms: 1.02x faster                                                |
| tornado_http             | 94.4 ms                                                               | 92.5 ms: 1.02x faster                                                |
| comprehensions           | 16.5 us                                                               | 16.2 us: 1.02x faster                                                |
| genshi_text              | 24.6 ms                                                               | 24.2 ms: 1.02x faster                                                |
| nbody                    | 81.6 ms                                                               | 80.2 ms: 1.02x faster                                                |
| meteor_contest           | 106 ms                                                                | 104 ms: 1.02x faster                                                 |
| xml_etree_process        | 57.0 ms                                                               | 56.1 ms: 1.02x faster                                                |
| pprint_safe_repr         | 717 ms                                                                | 707 ms: 1.01x faster                                                 |
| mako                     | 9.78 ms                                                               | 9.65 ms: 1.01x faster                                                |
| sympy_sum                | 170 ms                                                                | 168 ms: 1.01x faster                                                 |
| regex_compile            | 136 ms                                                                | 134 ms: 1.01x faster                                                 |
| python_startup           | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                |
| python_startup_no_site   | 7.24 ms                                                               | 7.17 ms: 1.01x faster                                                |
| logging_format           | 6.14 us                                                               | 6.09 us: 1.01x faster                                                |
| xml_etree_generate       | 81.4 ms                                                               | 80.6 ms: 1.01x faster                                                |
| fannkuch                 | 369 ms                                                                | 366 ms: 1.01x faster                                                 |
| create_gc_cycles         | 1.77 ms                                                               | 1.76 ms: 1.01x faster                                                |
| bench_thread_pool        | 822 us                                                                | 816 us: 1.01x faster                                                 |
| asyncio_tcp              | 501 ms                                                                | 498 ms: 1.01x faster                                                 |
| dulwich_log              | 69.8 ms                                                               | 69.4 ms: 1.01x faster                                                |
| asyncio_websockets       | 558 ms                                                                | 555 ms: 1.00x faster                                                 |
| sqlglot_optimize         | 55.8 ms                                                               | 55.6 ms: 1.00x faster                                                |
| bpe_tokeniser            | 4.53 sec                                                              | 4.51 sec: 1.00x faster                                               |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                               |
| sympy_integrate          | 22.2 ms                                                               | 22.3 ms: 1.00x slower                                                |
| coverage                 | 92.4 ms                                                               | 92.7 ms: 1.00x slower                                                |
| scimark_fft              | 307 ms                                                                | 309 ms: 1.01x slower                                                 |
| sympy_expand             | 501 ms                                                                | 505 ms: 1.01x slower                                                 |
| sqlglot_transpile        | 1.61 ms                                                               | 1.62 ms: 1.01x slower                                                |
| pathlib                  | 16.0 ms                                                               | 16.1 ms: 1.01x slower                                                |
| 2to3                     | 272 ms                                                                | 275 ms: 1.01x slower                                                 |
| telco                    | 7.88 ms                                                               | 7.96 ms: 1.01x slower                                                |
| crypto_pyaes             | 66.8 ms                                                               | 67.5 ms: 1.01x slower                                                |
| deepcopy_memo            | 28.2 us                                                               | 28.5 us: 1.01x slower                                                |
| raytrace                 | 266 ms                                                                | 270 ms: 1.01x slower                                                 |
| regex_effbot             | 3.73 ms                                                               | 3.79 ms: 1.02x slower                                                |
| scimark_monte_carlo      | 59.9 ms                                                               | 60.9 ms: 1.02x slower                                                |
| hexiom                   | 6.52 ms                                                               | 6.63 ms: 1.02x slower                                                |
| deltablue                | 3.51 ms                                                               | 3.57 ms: 1.02x slower                                                |
| tomli_loads              | 1.93 sec                                                              | 1.97 sec: 1.02x slower                                               |
| go                       | 145 ms                                                                | 148 ms: 1.02x slower                                                 |
| spectral_norm            | 101 ms                                                                | 103 ms: 1.02x slower                                                 |
| typing_runtime_protocols | 169 us                                                                | 173 us: 1.02x slower                                                 |
| json_loads               | 27.7 us                                                               | 28.3 us: 1.02x slower                                                |
| richards_super           | 45.9 ms                                                               | 47.1 ms: 1.03x slower                                                |
| scimark_sor              | 125 ms                                                                | 129 ms: 1.03x slower                                                 |
| mdp                      | 2.66 sec                                                              | 2.72 sec: 1.03x slower                                               |
| scimark_sparse_mat_mult  | 4.34 ms                                                               | 4.45 ms: 1.03x slower                                                |
| logging_silent           | 103 ns                                                                | 106 ns: 1.03x slower                                                 |
| richards                 | 40.1 ms                                                               | 41.4 ms: 1.03x slower                                                |
| pycparser                | 1.12 sec                                                              | 1.17 sec: 1.05x slower                                               |
| regex_v8                 | 23.8 ms                                                               | 25.9 ms: 1.09x slower                                                |
| generators               | 28.9 ms                                                               | 33.1 ms: 1.15x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (34): deepcopy_reduce, unpickle_pure_python, logging_simple, async_tree_none, async_tree_cpu_io_mixed, dask, async_tree_memoization_tg, chaos, float, json_dumps, thrift, pyflate, sympy_str, json, async_tree_io, deepcopy, html5lib, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_generators, coroutines, pidigits, docutils, async_tree_io_tg, bench_mp_pool, scimark_lu, sqlglot_normalize, xml_etree_iterparse, pickle_pure_python, pprint_pformat, sqlglot_parse, django_template, xml_etree_parse, pylint

# HPT report

- Reliability score: 74.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x