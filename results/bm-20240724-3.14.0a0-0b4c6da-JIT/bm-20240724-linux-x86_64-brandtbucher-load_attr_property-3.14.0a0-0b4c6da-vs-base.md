# Results vs. base

- fork: brandtbucher
- ref: load_attr_property
- machine: linux-x86_64
- commit hash: 0b4c6da
- commit date: 2024-07-24
- overall geometric mean: 1.00x slower
- HPT reliability: 65.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 271 ms: 1.00x faster                                                      |
| html5lib       | 65.2 ms                                                               | 64.8 ms: 1.01x faster                                                     |
| tornado_http   | 94.4 ms                                                               | 92.9 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_generators       | 455 ms                                                                | 450 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl        | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                    |
| asyncio_tcp            | 501 ms                                                                | 504 ms: 1.00x slower                                                      |
| coroutines             | 22.7 ms                                                               | 23.0 ms: 1.01x slower                                                     |
| async_tree_memoization | 414 ms                                                                | 428 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, asyncio_websockets, async_tree_io, async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 81.6 ms                                                               | 81.0 ms: 1.01x faster                                                     |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                                | 134 ms: 1.01x faster                                                      |
| regex_dna      | 228 ms                                                                | 230 ms: 1.01x slower                                                      |
| regex_effbot   | 3.73 ms                                                               | 3.90 ms: 1.05x slower                                                     |
| regex_v8       | 23.8 ms                                                               | 26.3 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate  | 81.4 ms                                                               | 80.6 ms: 1.01x faster                                                     |
| pickle_pure_python  | 297 us                                                                | 295 us: 1.01x faster                                                      |
| xml_etree_iterparse | 98.8 ms                                                               | 98.6 ms: 1.00x faster                                                     |
| tomli_loads         | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                                    |
| json_dumps          | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                     |
| json_loads          | 27.7 us                                                               | 28.3 us: 1.02x slower                                                     |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (3): xml_etree_process, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                     |
| python_startup_no_site | 7.24 ms                                                               | 7.17 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml     | 58.0 ms                                                               | 57.5 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (3): genshi_text, django_template, mako

All benchmarks:
===============

| Benchmark                | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                      | 2.66 sec                                                              | 2.52 sec: 1.05x faster                                                    |
| dulwich_log              | 69.8 ms                                                               | 67.7 ms: 1.03x faster                                                     |
| pprint_safe_repr         | 717 ms                                                                | 702 ms: 1.02x faster                                                      |
| generators               | 28.9 ms                                                               | 28.3 ms: 1.02x faster                                                     |
| sqlglot_parse            | 1.28 ms                                                               | 1.26 ms: 1.02x faster                                                     |
| sympy_sum                | 170 ms                                                                | 167 ms: 1.02x faster                                                      |
| deepcopy_reduce          | 2.80 us                                                               | 2.75 us: 1.02x faster                                                     |
| tornado_http             | 94.4 ms                                                               | 92.9 ms: 1.02x faster                                                     |
| sqlglot_transpile        | 1.61 ms                                                               | 1.58 ms: 1.01x faster                                                     |
| regex_compile            | 136 ms                                                                | 134 ms: 1.01x faster                                                      |
| python_startup           | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                     |
| sympy_str                | 297 ms                                                                | 293 ms: 1.01x faster                                                      |
| logging_format           | 6.14 us                                                               | 6.08 us: 1.01x faster                                                     |
| async_generators         | 455 ms                                                                | 450 ms: 1.01x faster                                                      |
| python_startup_no_site   | 7.24 ms                                                               | 7.17 ms: 1.01x faster                                                     |
| logging_silent           | 103 ns                                                                | 102 ns: 1.01x faster                                                      |
| xml_etree_generate       | 81.4 ms                                                               | 80.6 ms: 1.01x faster                                                     |
| genshi_xml               | 58.0 ms                                                               | 57.5 ms: 1.01x faster                                                     |
| scimark_fft              | 307 ms                                                                | 305 ms: 1.01x faster                                                      |
| html5lib                 | 65.2 ms                                                               | 64.8 ms: 1.01x faster                                                     |
| comprehensions           | 16.5 us                                                               | 16.4 us: 1.01x faster                                                     |
| sympy_expand             | 501 ms                                                                | 498 ms: 1.01x faster                                                      |
| nbody                    | 81.6 ms                                                               | 81.0 ms: 1.01x faster                                                     |
| go                       | 145 ms                                                                | 144 ms: 1.01x faster                                                      |
| create_gc_cycles         | 1.77 ms                                                               | 1.76 ms: 1.01x faster                                                     |
| sympy_integrate          | 22.2 ms                                                               | 22.1 ms: 1.01x faster                                                     |
| pickle_pure_python       | 297 us                                                                | 295 us: 1.01x faster                                                      |
| richards                 | 40.1 ms                                                               | 39.9 ms: 1.00x faster                                                     |
| 2to3                     | 272 ms                                                                | 271 ms: 1.00x faster                                                      |
| spectral_norm            | 101 ms                                                                | 101 ms: 1.00x faster                                                      |
| xml_etree_iterparse      | 98.8 ms                                                               | 98.6 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                    |
| pidigits                 | 185 ms                                                                | 186 ms: 1.00x slower                                                      |
| bench_thread_pool        | 822 us                                                                | 825 us: 1.00x slower                                                      |
| pyflate                  | 436 ms                                                                | 438 ms: 1.00x slower                                                      |
| hexiom                   | 6.52 ms                                                               | 6.55 ms: 1.00x slower                                                     |
| asyncio_tcp              | 501 ms                                                                | 504 ms: 1.00x slower                                                      |
| tomli_loads              | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                                    |
| chaos                    | 58.0 ms                                                               | 58.3 ms: 1.01x slower                                                     |
| regex_dna                | 228 ms                                                                | 230 ms: 1.01x slower                                                      |
| gc_traversal             | 3.86 ms                                                               | 3.89 ms: 1.01x slower                                                     |
| bpe_tokeniser            | 4.53 sec                                                              | 4.56 sec: 1.01x slower                                                    |
| json_dumps               | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                     |
| fannkuch                 | 369 ms                                                                | 374 ms: 1.01x slower                                                      |
| coroutines               | 22.7 ms                                                               | 23.0 ms: 1.01x slower                                                     |
| richards_super           | 45.9 ms                                                               | 46.6 ms: 1.01x slower                                                     |
| typing_runtime_protocols | 169 us                                                                | 171 us: 1.01x slower                                                      |
| scimark_sor              | 125 ms                                                                | 127 ms: 1.01x slower                                                      |
| deepcopy                 | 269 us                                                                | 274 us: 1.02x slower                                                      |
| json_loads               | 27.7 us                                                               | 28.3 us: 1.02x slower                                                     |
| async_tree_memoization   | 414 ms                                                                | 428 ms: 1.03x slower                                                      |
| regex_effbot             | 3.73 ms                                                               | 3.90 ms: 1.05x slower                                                     |
| pycparser                | 1.12 sec                                                              | 1.17 sec: 1.05x slower                                                    |
| regex_v8                 | 23.8 ms                                                               | 26.3 ms: 1.11x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (37): async_tree_cpu_io_mixed, dask, async_tree_cpu_io_mixed_tg, pylint, genshi_text, async_tree_none, logging_simple, sqlglot_normalize, json, crypto_pyaes, xml_etree_process, pathlib, raytrace, pprint_pformat, coverage, asyncio_websockets, bench_mp_pool, unpickle_pure_python, nqueens, thrift, meteor_contest, django_template, docutils, scimark_sparse_mat_mult, async_tree_io, telco, sqlglot_optimize, float, scimark_lu, async_tree_memoization_tg, async_tree_io_tg, deltablue, deepcopy_memo, scimark_monte_carlo, async_tree_none_tg, xml_etree_parse, mako

# HPT report

- Reliability score: 65.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x