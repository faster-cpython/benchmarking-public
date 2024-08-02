# Results vs. base

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: 2bab2aa
- commit date: 2024-07-09
- overall geometric mean: 1.00x faster
- HPT reliability: 97.78%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 274 ms: 1.01x slower                                                    |
| docutils       | 2.87 sec                                                              | 2.90 sec: 1.01x slower                                                  |
| html5lib       | 64.7 ms                                                               | 65.1 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 185 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                               | 24.4 ms: 1.04x faster                                                   |
| regex_effbot   | 3.86 ms                                                               | 3.74 ms: 1.03x faster                                                   |
| regex_compile  | 134 ms                                                                | 137 ms: 1.02x slower                                                    |
| regex_dna      | 222 ms                                                                | 229 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 215 us                                                                | 206 us: 1.04x faster                                                    |
| json_loads           | 28.1 us                                                               | 27.4 us: 1.03x faster                                                   |
| xml_etree_parse      | 150 ms                                                                | 147 ms: 1.02x faster                                                    |
| json_dumps           | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                   |
| xml_etree_generate   | 81.6 ms                                                               | 82.3 ms: 1.01x slower                                                   |
| pickle_pure_python   | 293 us                                                                | 297 us: 1.01x slower                                                    |
| tomli_loads          | 1.92 sec                                                              | 1.97 sec: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                               | 7.09 ms: 1.00x faster                                                   |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 9.76 ms                                                               | 9.82 ms: 1.01x slower                                                   |
| django_template | 35.1 ms                                                               | 35.8 ms: 1.02x slower                                                   |
| genshi_xml      | 58.0 ms                                                               | 59.4 ms: 1.02x slower                                                   |
| genshi_text     | 24.9 ms                                                               | 26.0 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| logging_silent           | 107 ns                                                                | 98.0 ns: 1.09x faster                                                   |
| gc_traversal             | 3.74 ms                                                               | 3.52 ms: 1.06x faster                                                   |
| richards                 | 41.8 ms                                                               | 39.8 ms: 1.05x faster                                                   |
| scimark_monte_carlo      | 61.1 ms                                                               | 58.2 ms: 1.05x faster                                                   |
| deepcopy_reduce          | 2.78 us                                                               | 2.65 us: 1.05x faster                                                   |
| unpickle_pure_python     | 215 us                                                                | 206 us: 1.04x faster                                                    |
| richards_super           | 47.5 ms                                                               | 45.7 ms: 1.04x faster                                                   |
| deepcopy_memo            | 28.4 us                                                               | 27.3 us: 1.04x faster                                                   |
| regex_v8                 | 25.3 ms                                                               | 24.4 ms: 1.04x faster                                                   |
| pyflate                  | 444 ms                                                                | 429 ms: 1.03x faster                                                    |
| regex_effbot             | 3.86 ms                                                               | 3.74 ms: 1.03x faster                                                   |
| json_loads               | 28.1 us                                                               | 27.4 us: 1.03x faster                                                   |
| pycparser                | 1.18 sec                                                              | 1.15 sec: 1.02x faster                                                  |
| pprint_safe_repr         | 710 ms                                                                | 694 ms: 1.02x faster                                                    |
| spectral_norm            | 104 ms                                                                | 102 ms: 1.02x faster                                                    |
| xml_etree_parse          | 150 ms                                                                | 147 ms: 1.02x faster                                                    |
| telco                    | 8.08 ms                                                               | 7.94 ms: 1.02x faster                                                   |
| json                     | 5.19 ms                                                               | 5.11 ms: 1.02x faster                                                   |
| typing_runtime_protocols | 172 us                                                                | 170 us: 1.01x faster                                                    |
| go                       | 145 ms                                                                | 143 ms: 1.01x faster                                                    |
| fannkuch                 | 361 ms                                                                | 357 ms: 1.01x faster                                                    |
| create_gc_cycles         | 1.76 ms                                                               | 1.75 ms: 1.01x faster                                                   |
| meteor_contest           | 107 ms                                                                | 106 ms: 1.01x faster                                                    |
| pathlib                  | 16.2 ms                                                               | 16.1 ms: 1.01x faster                                                   |
| bpe_tokeniser            | 4.84 sec                                                              | 4.80 sec: 1.01x faster                                                  |
| sqlglot_normalize        | 111 ms                                                                | 111 ms: 1.01x faster                                                    |
| pidigits                 | 186 ms                                                                | 185 ms: 1.00x faster                                                    |
| async_generators         | 452 ms                                                                | 450 ms: 1.00x faster                                                    |
| python_startup_no_site   | 7.10 ms                                                               | 7.09 ms: 1.00x faster                                                   |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                   |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                  |
| coroutines               | 23.4 ms                                                               | 23.5 ms: 1.00x slower                                                   |
| scimark_fft              | 309 ms                                                                | 310 ms: 1.00x slower                                                    |
| generators               | 29.5 ms                                                               | 29.7 ms: 1.01x slower                                                   |
| dulwich_log              | 67.1 ms                                                               | 67.4 ms: 1.01x slower                                                   |
| mako                     | 9.76 ms                                                               | 9.82 ms: 1.01x slower                                                   |
| sympy_sum                | 165 ms                                                                | 166 ms: 1.01x slower                                                    |
| logging_simple           | 5.42 us                                                               | 5.46 us: 1.01x slower                                                   |
| html5lib                 | 64.7 ms                                                               | 65.1 ms: 1.01x slower                                                   |
| sympy_integrate          | 21.8 ms                                                               | 22.0 ms: 1.01x slower                                                   |
| sympy_str                | 292 ms                                                                | 294 ms: 1.01x slower                                                    |
| json_dumps               | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                   |
| xml_etree_generate       | 81.6 ms                                                               | 82.3 ms: 1.01x slower                                                   |
| 2to3                     | 271 ms                                                                | 274 ms: 1.01x slower                                                    |
| sqlglot_optimize         | 55.0 ms                                                               | 55.6 ms: 1.01x slower                                                   |
| docutils                 | 2.87 sec                                                              | 2.90 sec: 1.01x slower                                                  |
| sympy_expand             | 492 ms                                                                | 498 ms: 1.01x slower                                                    |
| pickle_pure_python       | 293 us                                                                | 297 us: 1.01x slower                                                    |
| hexiom                   | 6.48 ms                                                               | 6.58 ms: 1.02x slower                                                   |
| coverage                 | 92.4 ms                                                               | 93.9 ms: 1.02x slower                                                   |
| scimark_sor              | 129 ms                                                                | 131 ms: 1.02x slower                                                    |
| logging_format           | 5.94 us                                                               | 6.04 us: 1.02x slower                                                   |
| django_template          | 35.1 ms                                                               | 35.8 ms: 1.02x slower                                                   |
| regex_compile            | 134 ms                                                                | 137 ms: 1.02x slower                                                    |
| raytrace                 | 266 ms                                                                | 272 ms: 1.02x slower                                                    |
| tomli_loads              | 1.92 sec                                                              | 1.97 sec: 1.02x slower                                                  |
| genshi_xml               | 58.0 ms                                                               | 59.4 ms: 1.02x slower                                                   |
| asyncio_tcp              | 488 ms                                                                | 501 ms: 1.03x slower                                                    |
| scimark_lu               | 124 ms                                                                | 128 ms: 1.03x slower                                                    |
| regex_dna                | 222 ms                                                                | 229 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult  | 4.28 ms                                                               | 4.46 ms: 1.04x slower                                                   |
| genshi_text              | 24.9 ms                                                               | 26.0 ms: 1.05x slower                                                   |
| chaos                    | 58.1 ms                                                               | 61.0 ms: 1.05x slower                                                   |
| mdp                      | 2.52 sec                                                              | 2.75 sec: 1.09x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (27): nqueens, pprint_pformat, deepcopy, float, thrift, xml_etree_iterparse, async_tree_memoization_tg, bench_thread_pool, async_tree_memoization, sqlglot_parse, async_tree_io_tg, sqlglot_transpile, deltablue, bench_mp_pool, comprehensions, async_tree_none_tg, asyncio_websockets, dask, nbody, tornado_http, xml_etree_process, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io, crypto_pyaes, pylint, async_tree_cpu_io_mixed

# HPT report

- Reliability score: 97.78% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x