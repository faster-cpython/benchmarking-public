# Results vs. base

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: f135fa1
- commit date: 2024-08-06
- overall geometric mean: 1.00x slower
- HPT reliability: 99.09%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| html5lib       | 63.8 ms                                                               | 65.8 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| asyncio_tcp_ssl  | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                                    |
| asyncio_tcp      | 498 ms                                                                | 500 ms: 1.00x slower                                                      |
| async_generators | 453 ms                                                                | 469 ms: 1.04x slower                                                      |
| Geometric mean   | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, coroutines, asyncio_websockets, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 185 ms: 1.00x faster                                                      |
| float          | 70.5 ms                                                               | 71.6 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.83 ms                                                               | 3.57 ms: 1.07x faster                                                     |
| regex_dna      | 223 ms                                                                | 215 ms: 1.03x faster                                                      |
| regex_v8       | 24.4 ms                                                               | 23.7 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate  | 81.6 ms                                                               | 79.9 ms: 1.02x faster                                                     |
| pickle_pure_python  | 300 us                                                                | 297 us: 1.01x faster                                                      |
| xml_etree_process   | 57.2 ms                                                               | 56.6 ms: 1.01x faster                                                     |
| xml_etree_iterparse | 99.2 ms                                                               | 99.4 ms: 1.00x slower                                                     |
| tomli_loads         | 1.91 sec                                                              | 1.93 sec: 1.01x slower                                                    |
| json_dumps          | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                     |
| xml_etree_parse     | 146 ms                                                                | 149 ms: 1.02x slower                                                      |
| json_loads          | 27.7 us                                                               | 28.6 us: 1.03x slower                                                     |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                     |
| python_startup_no_site | 7.17 ms                                                               | 7.20 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text    | 24.5 ms                                                               | 24.0 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (3): mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot             | 3.83 ms                                                               | 3.57 ms: 1.07x faster                                                     |
| gc_traversal             | 3.85 ms                                                               | 3.61 ms: 1.07x faster                                                     |
| pycparser                | 1.19 sec                                                              | 1.12 sec: 1.06x faster                                                    |
| scimark_sparse_mat_mult  | 4.55 ms                                                               | 4.36 ms: 1.04x faster                                                     |
| regex_dna                | 223 ms                                                                | 215 ms: 1.03x faster                                                      |
| regex_v8                 | 24.4 ms                                                               | 23.7 ms: 1.03x faster                                                     |
| xml_etree_generate       | 81.6 ms                                                               | 79.9 ms: 1.02x faster                                                     |
| genshi_text              | 24.5 ms                                                               | 24.0 ms: 1.02x faster                                                     |
| fannkuch                 | 371 ms                                                                | 365 ms: 1.01x faster                                                      |
| pickle_pure_python       | 300 us                                                                | 297 us: 1.01x faster                                                      |
| xml_etree_process        | 57.2 ms                                                               | 56.6 ms: 1.01x faster                                                     |
| logging_format           | 6.17 us                                                               | 6.11 us: 1.01x faster                                                     |
| go                       | 146 ms                                                                | 145 ms: 1.01x faster                                                      |
| scimark_fft              | 307 ms                                                                | 304 ms: 1.01x faster                                                      |
| bpe_tokeniser            | 4.52 sec                                                              | 4.49 sec: 1.01x faster                                                    |
| pidigits                 | 186 ms                                                                | 185 ms: 1.00x faster                                                      |
| bench_thread_pool        | 822 us                                                                | 823 us: 1.00x slower                                                      |
| xml_etree_iterparse      | 99.2 ms                                                               | 99.4 ms: 1.00x slower                                                     |
| sqlglot_transpile        | 1.62 ms                                                               | 1.63 ms: 1.00x slower                                                     |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                     |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                                    |
| asyncio_tcp              | 498 ms                                                                | 500 ms: 1.00x slower                                                      |
| python_startup_no_site   | 7.17 ms                                                               | 7.20 ms: 1.00x slower                                                     |
| sympy_integrate          | 22.6 ms                                                               | 22.7 ms: 1.00x slower                                                     |
| deltablue                | 3.58 ms                                                               | 3.60 ms: 1.01x slower                                                     |
| sympy_sum                | 170 ms                                                                | 171 ms: 1.01x slower                                                      |
| sqlglot_normalize        | 113 ms                                                                | 113 ms: 1.01x slower                                                      |
| pyflate                  | 432 ms                                                                | 435 ms: 1.01x slower                                                      |
| deepcopy                 | 273 us                                                                | 275 us: 1.01x slower                                                      |
| thrift                   | 797 us                                                                | 803 us: 1.01x slower                                                      |
| tomli_loads              | 1.91 sec                                                              | 1.93 sec: 1.01x slower                                                    |
| sqlglot_optimize         | 55.9 ms                                                               | 56.4 ms: 1.01x slower                                                     |
| nqueens                  | 84.0 ms                                                               | 84.9 ms: 1.01x slower                                                     |
| comprehensions           | 16.2 us                                                               | 16.4 us: 1.01x slower                                                     |
| sqlglot_parse            | 1.29 ms                                                               | 1.31 ms: 1.01x slower                                                     |
| pathlib                  | 16.1 ms                                                               | 16.3 ms: 1.01x slower                                                     |
| sympy_expand             | 508 ms                                                                | 515 ms: 1.01x slower                                                      |
| richards                 | 41.2 ms                                                               | 41.7 ms: 1.01x slower                                                     |
| raytrace                 | 269 ms                                                                | 273 ms: 1.01x slower                                                      |
| typing_runtime_protocols | 171 us                                                                | 173 us: 1.01x slower                                                      |
| json                     | 5.09 ms                                                               | 5.16 ms: 1.01x slower                                                     |
| float                    | 70.5 ms                                                               | 71.6 ms: 1.02x slower                                                     |
| sympy_str                | 298 ms                                                                | 302 ms: 1.02x slower                                                      |
| crypto_pyaes             | 66.8 ms                                                               | 68.0 ms: 1.02x slower                                                     |
| pprint_safe_repr         | 722 ms                                                                | 737 ms: 1.02x slower                                                      |
| json_dumps               | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                     |
| spectral_norm            | 100 ms                                                                | 103 ms: 1.02x slower                                                      |
| xml_etree_parse          | 146 ms                                                                | 149 ms: 1.02x slower                                                      |
| html5lib                 | 63.8 ms                                                               | 65.8 ms: 1.03x slower                                                     |
| json_loads               | 27.7 us                                                               | 28.6 us: 1.03x slower                                                     |
| async_generators         | 453 ms                                                                | 469 ms: 1.04x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (38): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, scimark_sor, telco, scimark_monte_carlo, scimark_lu, richards_super, meteor_contest, coverage, 2to3, coroutines, hexiom, logging_silent, bench_mp_pool, create_gc_cycles, logging_simple, tornado_http, regex_compile, unpickle_pure_python, docutils, nbody, asyncio_websockets, generators, mako, genshi_xml, async_tree_memoization_tg, mdp, django_template, deepcopy_memo, pylint, async_tree_none, async_tree_none_tg, chaos, async_tree_io, deepcopy_reduce, pprint_pformat, async_tree_io_tg, async_tree_memoization

# HPT report

- Reliability score: 99.09% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x