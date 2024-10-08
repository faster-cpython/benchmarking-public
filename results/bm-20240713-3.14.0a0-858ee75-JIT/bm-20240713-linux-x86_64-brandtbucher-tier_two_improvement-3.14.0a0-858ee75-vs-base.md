# Results vs. base

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: 858ee75
- commit date: 2024-07-13
- overall geometric mean: 1.00x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 273 ms: 1.00x slower                                                        |
| docutils       | 2.87 sec                                                              | 2.89 sec: 1.01x slower                                                      |
| html5lib       | 64.7 ms                                                               | 63.6 ms: 1.02x faster                                                       |
| tornado_http   | 92.4 ms                                                               | 93.0 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                               | 79.5 ms: 1.01x faster                                                       |
| pidigits       | 186 ms                                                                | 186 ms: 1.00x faster                                                        |
| float          | 70.0 ms                                                               | 70.9 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                               | 26.3 ms: 1.04x slower                                                       |
| regex_effbot   | 3.86 ms                                                               | 4.03 ms: 1.04x slower                                                       |
| regex_dna      | 222 ms                                                                | 238 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 150 ms                                                                | 146 ms: 1.03x faster                                                        |
| xml_etree_iterparse  | 99.2 ms                                                               | 98.5 ms: 1.01x faster                                                       |
| unpickle_pure_python | 215 us                                                                | 216 us: 1.00x slower                                                        |
| pickle_pure_python   | 293 us                                                                | 297 us: 1.01x slower                                                        |
| json_loads           | 28.1 us                                                               | 28.5 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_generate, json_dumps, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                               | 7.06 ms: 1.01x faster                                                       |
| python_startup         | 10.5 ms                                                               | 10.4 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.76 ms                                                               | 9.73 ms: 1.00x faster                                                       |
| django_template | 35.1 ms                                                               | 35.5 ms: 1.01x slower                                                       |
| genshi_text     | 24.9 ms                                                               | 25.1 ms: 1.01x slower                                                       |
| genshi_xml      | 58.0 ms                                                               | 58.8 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal             | 3.74 ms                                                               | 3.55 ms: 1.05x faster                                                       |
| bpe_tokeniser            | 4.84 sec                                                              | 4.61 sec: 1.05x faster                                                      |
| xml_etree_parse          | 150 ms                                                                | 146 ms: 1.03x faster                                                        |
| html5lib                 | 64.7 ms                                                               | 63.6 ms: 1.02x faster                                                       |
| deepcopy_reduce          | 2.78 us                                                               | 2.74 us: 1.01x faster                                                       |
| json                     | 5.19 ms                                                               | 5.12 ms: 1.01x faster                                                       |
| pathlib                  | 16.2 ms                                                               | 16.0 ms: 1.01x faster                                                       |
| scimark_monte_carlo      | 61.1 ms                                                               | 60.4 ms: 1.01x faster                                                       |
| pyflate                  | 444 ms                                                                | 439 ms: 1.01x faster                                                        |
| create_gc_cycles         | 1.76 ms                                                               | 1.74 ms: 1.01x faster                                                       |
| typing_runtime_protocols | 172 us                                                                | 170 us: 1.01x faster                                                        |
| thrift                   | 801 us                                                                | 793 us: 1.01x faster                                                        |
| meteor_contest           | 107 ms                                                                | 106 ms: 1.01x faster                                                        |
| xml_etree_iterparse      | 99.2 ms                                                               | 98.5 ms: 1.01x faster                                                       |
| logging_silent           | 107 ns                                                                | 106 ns: 1.01x faster                                                        |
| python_startup_no_site   | 7.10 ms                                                               | 7.06 ms: 1.01x faster                                                       |
| go                       | 145 ms                                                                | 144 ms: 1.01x faster                                                        |
| nbody                    | 80.0 ms                                                               | 79.5 ms: 1.01x faster                                                       |
| python_startup           | 10.5 ms                                                               | 10.4 ms: 1.01x faster                                                       |
| pidigits                 | 186 ms                                                                | 186 ms: 1.00x faster                                                        |
| comprehensions           | 16.7 us                                                               | 16.6 us: 1.00x faster                                                       |
| mako                     | 9.76 ms                                                               | 9.73 ms: 1.00x faster                                                       |
| dulwich_log              | 67.1 ms                                                               | 67.3 ms: 1.00x slower                                                       |
| richards_super           | 47.5 ms                                                               | 47.7 ms: 1.00x slower                                                       |
| spectral_norm            | 104 ms                                                                | 105 ms: 1.00x slower                                                        |
| 2to3                     | 271 ms                                                                | 273 ms: 1.00x slower                                                        |
| unpickle_pure_python     | 215 us                                                                | 216 us: 1.00x slower                                                        |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                      |
| mdp                      | 2.52 sec                                                              | 2.53 sec: 1.01x slower                                                      |
| tornado_http             | 92.4 ms                                                               | 93.0 ms: 1.01x slower                                                       |
| deltablue                | 3.52 ms                                                               | 3.54 ms: 1.01x slower                                                       |
| raytrace                 | 266 ms                                                                | 268 ms: 1.01x slower                                                        |
| sympy_expand             | 492 ms                                                                | 495 ms: 1.01x slower                                                        |
| docutils                 | 2.87 sec                                                              | 2.89 sec: 1.01x slower                                                      |
| sqlglot_transpile        | 1.60 ms                                                               | 1.61 ms: 1.01x slower                                                       |
| sympy_str                | 292 ms                                                                | 294 ms: 1.01x slower                                                        |
| django_template          | 35.1 ms                                                               | 35.5 ms: 1.01x slower                                                       |
| coroutines               | 23.4 ms                                                               | 23.7 ms: 1.01x slower                                                       |
| genshi_text              | 24.9 ms                                                               | 25.1 ms: 1.01x slower                                                       |
| hexiom                   | 6.48 ms                                                               | 6.54 ms: 1.01x slower                                                       |
| sympy_integrate          | 21.8 ms                                                               | 22.1 ms: 1.01x slower                                                       |
| pickle_pure_python       | 293 us                                                                | 297 us: 1.01x slower                                                        |
| json_loads               | 28.1 us                                                               | 28.5 us: 1.01x slower                                                       |
| sympy_sum                | 165 ms                                                                | 167 ms: 1.01x slower                                                        |
| float                    | 70.0 ms                                                               | 70.9 ms: 1.01x slower                                                       |
| sqlglot_optimize         | 55.0 ms                                                               | 55.7 ms: 1.01x slower                                                       |
| scimark_fft              | 309 ms                                                                | 313 ms: 1.01x slower                                                        |
| genshi_xml               | 58.0 ms                                                               | 58.8 ms: 1.01x slower                                                       |
| fannkuch                 | 361 ms                                                                | 366 ms: 1.01x slower                                                        |
| pycparser                | 1.18 sec                                                              | 1.20 sec: 1.01x slower                                                      |
| scimark_sor              | 129 ms                                                                | 131 ms: 1.02x slower                                                        |
| coverage                 | 92.4 ms                                                               | 93.9 ms: 1.02x slower                                                       |
| pprint_pformat           | 1.45 sec                                                              | 1.48 sec: 1.02x slower                                                      |
| generators               | 29.5 ms                                                               | 30.2 ms: 1.02x slower                                                       |
| logging_format           | 5.94 us                                                               | 6.08 us: 1.02x slower                                                       |
| asyncio_tcp              | 488 ms                                                                | 503 ms: 1.03x slower                                                        |
| scimark_lu               | 124 ms                                                                | 129 ms: 1.04x slower                                                        |
| regex_v8                 | 25.3 ms                                                               | 26.3 ms: 1.04x slower                                                       |
| regex_effbot             | 3.86 ms                                                               | 4.03 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult  | 4.28 ms                                                               | 4.54 ms: 1.06x slower                                                       |
| regex_dna                | 222 ms                                                                | 238 ms: 1.07x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (30): crypto_pyaes, async_tree_io, async_tree_memoization_tg, nqueens, deepcopy_memo, xml_etree_process, deepcopy, chaos, async_tree_none_tg, async_tree_io_tg, xml_etree_generate, async_tree_cpu_io_mixed_tg, async_generators, bench_mp_pool, sqlglot_normalize, telco, bench_thread_pool, dask, async_tree_memoization, json_dumps, logging_simple, regex_compile, asyncio_websockets, pprint_safe_repr, pylint, tomli_loads, sqlglot_parse, richards, async_tree_none, async_tree_cpu_io_mixed

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x