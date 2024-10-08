# Results vs. base

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: c482bbf
- commit date: 2024-08-07
- overall geometric mean: 1.00x faster
- HPT reliability: 99.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 275 ms                                                                | 274 ms: 1.00x faster                                                      |
| html5lib       | 63.8 ms                                                               | 66.1 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines       | 22.9 ms                                                               | 22.8 ms: 1.01x faster                                                     |
| asyncio_tcp_ssl  | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                                    |
| asyncio_tcp      | 498 ms                                                                | 500 ms: 1.00x slower                                                      |
| async_generators | 453 ms                                                                | 459 ms: 1.01x slower                                                      |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (9): async_tree_io, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 79.1 ms                                                               | 78.1 ms: 1.01x faster                                                     |
| float          | 70.5 ms                                                               | 70.0 ms: 1.01x faster                                                     |
| pidigits       | 186 ms                                                                | 185 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.83 ms                                                               | 3.84 ms: 1.00x slower                                                     |
| regex_dna      | 223 ms                                                                | 228 ms: 1.02x slower                                                      |
| regex_v8       | 24.4 ms                                                               | 25.4 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate | 81.6 ms                                                               | 79.4 ms: 1.03x faster                                                     |
| xml_etree_process  | 57.2 ms                                                               | 55.8 ms: 1.03x faster                                                     |
| pickle_pure_python | 300 us                                                                | 295 us: 1.02x faster                                                      |
| json_loads         | 27.7 us                                                               | 28.0 us: 1.01x slower                                                     |
| Geometric mean     | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (5): xml_etree_iterparse, xml_etree_parse, json_dumps, tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                     |
| python_startup_no_site | 7.17 ms                                                               | 7.20 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text    | 24.5 ms                                                               | 24.0 ms: 1.02x faster                                                     |
| mako           | 9.85 ms                                                               | 9.70 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 4.55 ms                                                               | 4.31 ms: 1.06x faster                                                     |
| deltablue                | 3.58 ms                                                               | 3.48 ms: 1.03x faster                                                     |
| xml_etree_generate       | 81.6 ms                                                               | 79.4 ms: 1.03x faster                                                     |
| logging_silent           | 104 ns                                                                | 102 ns: 1.03x faster                                                      |
| fannkuch                 | 371 ms                                                                | 361 ms: 1.03x faster                                                      |
| xml_etree_process        | 57.2 ms                                                               | 55.8 ms: 1.03x faster                                                     |
| pyflate                  | 432 ms                                                                | 421 ms: 1.03x faster                                                      |
| go                       | 146 ms                                                                | 143 ms: 1.02x faster                                                      |
| raytrace                 | 269 ms                                                                | 263 ms: 1.02x faster                                                      |
| gc_traversal             | 3.85 ms                                                               | 3.77 ms: 1.02x faster                                                     |
| genshi_text              | 24.5 ms                                                               | 24.0 ms: 1.02x faster                                                     |
| typing_runtime_protocols | 171 us                                                                | 167 us: 1.02x faster                                                      |
| deepcopy_memo            | 29.1 us                                                               | 28.6 us: 1.02x faster                                                     |
| pickle_pure_python       | 300 us                                                                | 295 us: 1.02x faster                                                      |
| mako                     | 9.85 ms                                                               | 9.70 ms: 1.02x faster                                                     |
| deepcopy_reduce          | 2.78 us                                                               | 2.74 us: 1.01x faster                                                     |
| nbody                    | 79.1 ms                                                               | 78.1 ms: 1.01x faster                                                     |
| richards_super           | 47.5 ms                                                               | 47.0 ms: 1.01x faster                                                     |
| hexiom                   | 6.71 ms                                                               | 6.64 ms: 1.01x faster                                                     |
| bpe_tokeniser            | 4.52 sec                                                              | 4.47 sec: 1.01x faster                                                    |
| scimark_monte_carlo      | 60.7 ms                                                               | 60.1 ms: 1.01x faster                                                     |
| coverage                 | 91.8 ms                                                               | 90.9 ms: 1.01x faster                                                     |
| float                    | 70.5 ms                                                               | 70.0 ms: 1.01x faster                                                     |
| coroutines               | 22.9 ms                                                               | 22.8 ms: 1.01x faster                                                     |
| sqlglot_normalize        | 113 ms                                                                | 112 ms: 1.01x faster                                                      |
| sympy_sum                | 170 ms                                                                | 170 ms: 1.00x faster                                                      |
| create_gc_cycles         | 1.78 ms                                                               | 1.77 ms: 1.00x faster                                                     |
| bench_thread_pool        | 822 us                                                                | 819 us: 1.00x faster                                                      |
| sympy_integrate          | 22.6 ms                                                               | 22.5 ms: 1.00x faster                                                     |
| 2to3                     | 275 ms                                                                | 274 ms: 1.00x faster                                                      |
| pidigits                 | 186 ms                                                                | 185 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                                    |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                     |
| regex_effbot             | 3.83 ms                                                               | 3.84 ms: 1.00x slower                                                     |
| python_startup_no_site   | 7.17 ms                                                               | 7.20 ms: 1.00x slower                                                     |
| mdp                      | 2.56 sec                                                              | 2.57 sec: 1.00x slower                                                    |
| asyncio_tcp              | 498 ms                                                                | 500 ms: 1.00x slower                                                      |
| generators               | 32.9 ms                                                               | 33.1 ms: 1.01x slower                                                     |
| logging_simple           | 5.57 us                                                               | 5.61 us: 1.01x slower                                                     |
| nqueens                  | 84.0 ms                                                               | 84.8 ms: 1.01x slower                                                     |
| json_loads               | 27.7 us                                                               | 28.0 us: 1.01x slower                                                     |
| async_generators         | 453 ms                                                                | 459 ms: 1.01x slower                                                      |
| json                     | 5.09 ms                                                               | 5.16 ms: 1.02x slower                                                     |
| comprehensions           | 16.2 us                                                               | 16.5 us: 1.02x slower                                                     |
| regex_dna                | 223 ms                                                                | 228 ms: 1.02x slower                                                      |
| spectral_norm            | 100 ms                                                                | 103 ms: 1.02x slower                                                      |
| html5lib                 | 63.8 ms                                                               | 66.1 ms: 1.03x slower                                                     |
| regex_v8                 | 24.4 ms                                                               | 25.4 ms: 1.04x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (41): async_tree_io, telco, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, pprint_safe_repr, sqlglot_optimize, richards, sqlglot_transpile, docutils, regex_compile, pathlib, scimark_fft, sympy_expand, async_tree_io_tg, genshi_xml, pycparser, pylint, async_tree_none_tg, sqlglot_parse, django_template, bench_mp_pool, xml_etree_iterparse, xml_etree_parse, tornado_http, thrift, sympy_str, logging_format, asyncio_websockets, meteor_contest, crypto_pyaes, chaos, json_dumps, deepcopy, tomli_loads, unpickle_pure_python, scimark_sor, pprint_pformat, scimark_lu

# HPT report

- Reliability score: 99.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x