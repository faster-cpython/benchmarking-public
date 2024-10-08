# Results vs. base

- fork: brandtbucher
- ref: replicate_more
- machine: linux-x86_64
- commit hash: 3a2f40c
- commit date: 2024-08-06
- overall geometric mean: 1.00x faster
- HPT reliability: 96.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 275 ms                                                                | 274 ms: 1.00x faster                                                  |
| html5lib       | 63.8 ms                                                               | 64.3 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines             | 22.9 ms                                                               | 22.7 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl        | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                                |
| asyncio_tcp            | 498 ms                                                                | 497 ms: 1.00x faster                                                  |
| async_generators       | 453 ms                                                                | 461 ms: 1.02x slower                                                  |
| async_tree_memoization | 422 ms                                                                | 430 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io, asyncio_websockets, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 186 ms: 1.00x slower                                                  |
| float          | 70.5 ms                                                               | 72.9 ms: 1.03x slower                                                 |
| nbody          | 79.1 ms                                                               | 85.7 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 135 ms                                                                | 133 ms: 1.01x faster                                                  |
| regex_effbot   | 3.83 ms                                                               | 3.90 ms: 1.02x slower                                                 |
| regex_v8       | 24.4 ms                                                               | 25.1 ms: 1.03x slower                                                 |
| regex_dna      | 223 ms                                                                | 229 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 81.6 ms                                                               | 79.8 ms: 1.02x faster                                                 |
| pickle_pure_python   | 300 us                                                                | 293 us: 1.02x faster                                                  |
| xml_etree_process    | 57.2 ms                                                               | 56.2 ms: 1.02x faster                                                 |
| unpickle_pure_python | 215 us                                                                | 214 us: 1.00x faster                                                  |
| xml_etree_iterparse  | 99.2 ms                                                               | 99.5 ms: 1.00x slower                                                 |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                 |
| json_loads           | 27.7 us                                                               | 28.3 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (2): tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.17 ms                                                               | 7.15 ms: 1.00x faster                                                 |
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text    | 24.5 ms                                                               | 24.2 ms: 1.01x faster                                                 |
| genshi_xml     | 53.4 ms                                                               | 52.9 ms: 1.01x faster                                                 |
| mako           | 9.85 ms                                                               | 9.79 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 4.55 ms                                                               | 4.33 ms: 1.05x faster                                                 |
| deepcopy_reduce          | 2.78 us                                                               | 2.70 us: 1.03x faster                                                 |
| pprint_pformat           | 1.49 sec                                                              | 1.45 sec: 1.03x faster                                                |
| xml_etree_generate       | 81.6 ms                                                               | 79.8 ms: 1.02x faster                                                 |
| pickle_pure_python       | 300 us                                                                | 293 us: 1.02x faster                                                  |
| gc_traversal             | 3.85 ms                                                               | 3.77 ms: 1.02x faster                                                 |
| telco                    | 7.97 ms                                                               | 7.81 ms: 1.02x faster                                                 |
| xml_etree_process        | 57.2 ms                                                               | 56.2 ms: 1.02x faster                                                 |
| deltablue                | 3.58 ms                                                               | 3.52 ms: 1.02x faster                                                 |
| pprint_safe_repr         | 722 ms                                                                | 711 ms: 1.02x faster                                                  |
| scimark_fft              | 307 ms                                                                | 302 ms: 1.02x faster                                                  |
| scimark_sor              | 117 ms                                                                | 115 ms: 1.01x faster                                                  |
| deepcopy_memo            | 29.1 us                                                               | 28.7 us: 1.01x faster                                                 |
| fannkuch                 | 371 ms                                                                | 366 ms: 1.01x faster                                                  |
| pycparser                | 1.19 sec                                                              | 1.17 sec: 1.01x faster                                                |
| genshi_text              | 24.5 ms                                                               | 24.2 ms: 1.01x faster                                                 |
| regex_compile            | 135 ms                                                                | 133 ms: 1.01x faster                                                  |
| coroutines               | 22.9 ms                                                               | 22.7 ms: 1.01x faster                                                 |
| deepcopy                 | 273 us                                                                | 271 us: 1.01x faster                                                  |
| genshi_xml               | 53.4 ms                                                               | 52.9 ms: 1.01x faster                                                 |
| logging_format           | 6.17 us                                                               | 6.11 us: 1.01x faster                                                 |
| sympy_integrate          | 22.6 ms                                                               | 22.4 ms: 1.01x faster                                                 |
| go                       | 146 ms                                                                | 145 ms: 1.01x faster                                                  |
| raytrace                 | 269 ms                                                                | 267 ms: 1.01x faster                                                  |
| scimark_lu               | 109 ms                                                                | 108 ms: 1.01x faster                                                  |
| create_gc_cycles         | 1.78 ms                                                               | 1.77 ms: 1.01x faster                                                 |
| typing_runtime_protocols | 171 us                                                                | 169 us: 1.01x faster                                                  |
| mako                     | 9.85 ms                                                               | 9.79 ms: 1.01x faster                                                 |
| richards_super           | 47.5 ms                                                               | 47.2 ms: 1.01x faster                                                 |
| meteor_contest           | 105 ms                                                                | 105 ms: 1.00x faster                                                  |
| coverage                 | 91.8 ms                                                               | 91.4 ms: 1.00x faster                                                 |
| 2to3                     | 275 ms                                                                | 274 ms: 1.00x faster                                                  |
| sympy_sum                | 170 ms                                                                | 170 ms: 1.00x faster                                                  |
| sqlglot_normalize        | 113 ms                                                                | 112 ms: 1.00x faster                                                  |
| richards                 | 41.2 ms                                                               | 41.0 ms: 1.00x faster                                                 |
| bpe_tokeniser            | 4.52 sec                                                              | 4.50 sec: 1.00x faster                                                |
| bench_thread_pool        | 822 us                                                                | 819 us: 1.00x faster                                                  |
| logging_silent           | 104 ns                                                                | 104 ns: 1.00x faster                                                  |
| unpickle_pure_python     | 215 us                                                                | 214 us: 1.00x faster                                                  |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                                |
| asyncio_tcp              | 498 ms                                                                | 497 ms: 1.00x faster                                                  |
| python_startup_no_site   | 7.17 ms                                                               | 7.15 ms: 1.00x faster                                                 |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                                 |
| xml_etree_iterparse      | 99.2 ms                                                               | 99.5 ms: 1.00x slower                                                 |
| sqlglot_transpile        | 1.62 ms                                                               | 1.63 ms: 1.00x slower                                                 |
| crypto_pyaes             | 66.8 ms                                                               | 67.1 ms: 1.00x slower                                                 |
| pidigits                 | 186 ms                                                                | 186 ms: 1.00x slower                                                  |
| sqlglot_parse            | 1.29 ms                                                               | 1.30 ms: 1.01x slower                                                 |
| html5lib                 | 63.8 ms                                                               | 64.3 ms: 1.01x slower                                                 |
| json_dumps               | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                 |
| pathlib                  | 16.1 ms                                                               | 16.3 ms: 1.01x slower                                                 |
| comprehensions           | 16.2 us                                                               | 16.4 us: 1.01x slower                                                 |
| nqueens                  | 84.0 ms                                                               | 85.1 ms: 1.01x slower                                                 |
| spectral_norm            | 100 ms                                                                | 102 ms: 1.01x slower                                                  |
| pyflate                  | 432 ms                                                                | 439 ms: 1.02x slower                                                  |
| async_generators         | 453 ms                                                                | 461 ms: 1.02x slower                                                  |
| async_tree_memoization   | 422 ms                                                                | 430 ms: 1.02x slower                                                  |
| regex_effbot             | 3.83 ms                                                               | 3.90 ms: 1.02x slower                                                 |
| json_loads               | 27.7 us                                                               | 28.3 us: 1.02x slower                                                 |
| regex_v8                 | 24.4 ms                                                               | 25.1 ms: 1.03x slower                                                 |
| regex_dna                | 223 ms                                                                | 229 ms: 1.03x slower                                                  |
| float                    | 70.5 ms                                                               | 72.9 ms: 1.03x slower                                                 |
| nbody                    | 79.1 ms                                                               | 85.7 ms: 1.08x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (26): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, logging_simple, docutils, async_tree_none, generators, sqlglot_optimize, async_tree_io, sympy_expand, thrift, bench_mp_pool, tomli_loads, scimark_monte_carlo, json, hexiom, asyncio_websockets, sympy_str, async_tree_memoization_tg, mdp, pylint, tornado_http, chaos, xml_etree_parse, django_template, async_tree_none_tg, async_tree_io_tg

# HPT report

- Reliability score: 96.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x