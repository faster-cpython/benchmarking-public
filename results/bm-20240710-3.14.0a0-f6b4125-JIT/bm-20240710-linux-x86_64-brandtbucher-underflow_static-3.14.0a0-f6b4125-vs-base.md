# Results vs. base

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: f6b4125
- commit date: 2024-07-10
- overall geometric mean: 1.00x slower
- HPT reliability: 99.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 275 ms: 1.01x slower                                                    |
| docutils       | 2.87 sec                                                              | 2.90 sec: 1.01x slower                                                  |
| html5lib       | 64.7 ms                                                               | 63.1 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                               | 25.7 ms: 1.02x slower                                                   |
| regex_compile  | 134 ms                                                                | 136 ms: 1.02x slower                                                    |
| regex_dna      | 222 ms                                                                | 229 ms: 1.03x slower                                                    |
| regex_effbot   | 3.86 ms                                                               | 4.02 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 215 us                                                                | 207 us: 1.04x faster                                                    |
| xml_etree_parse      | 150 ms                                                                | 146 ms: 1.03x faster                                                    |
| json_loads           | 28.1 us                                                               | 27.8 us: 1.01x faster                                                   |
| xml_etree_process    | 57.5 ms                                                               | 57.1 ms: 1.01x faster                                                   |
| tomli_loads          | 1.92 sec                                                              | 1.91 sec: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_generate, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 58.0 ms                                                               | 58.7 ms: 1.01x slower                                                   |
| genshi_text     | 24.9 ms                                                               | 25.2 ms: 1.01x slower                                                   |
| mako            | 9.76 ms                                                               | 9.91 ms: 1.02x slower                                                   |
| django_template | 35.1 ms                                                               | 36.0 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| logging_silent           | 107 ns                                                                | 98.0 ns: 1.09x faster                                                   |
| scimark_monte_carlo      | 61.1 ms                                                               | 58.5 ms: 1.05x faster                                                   |
| deepcopy_memo            | 28.4 us                                                               | 27.4 us: 1.04x faster                                                   |
| unpickle_pure_python     | 215 us                                                                | 207 us: 1.04x faster                                                    |
| deepcopy_reduce          | 2.78 us                                                               | 2.69 us: 1.03x faster                                                   |
| html5lib                 | 64.7 ms                                                               | 63.1 ms: 1.03x faster                                                   |
| xml_etree_parse          | 150 ms                                                                | 146 ms: 1.03x faster                                                    |
| richards                 | 41.8 ms                                                               | 40.9 ms: 1.02x faster                                                   |
| typing_runtime_protocols | 172 us                                                                | 169 us: 1.02x faster                                                    |
| pprint_safe_repr         | 710 ms                                                                | 697 ms: 1.02x faster                                                    |
| pprint_pformat           | 1.45 sec                                                              | 1.43 sec: 1.02x faster                                                  |
| json_loads               | 28.1 us                                                               | 27.8 us: 1.01x faster                                                   |
| pyflate                  | 444 ms                                                                | 439 ms: 1.01x faster                                                    |
| telco                    | 8.08 ms                                                               | 8.00 ms: 1.01x faster                                                   |
| xml_etree_process        | 57.5 ms                                                               | 57.1 ms: 1.01x faster                                                   |
| tomli_loads              | 1.92 sec                                                              | 1.91 sec: 1.01x faster                                                  |
| bench_thread_pool        | 832 us                                                                | 829 us: 1.00x faster                                                    |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                   |
| mdp                      | 2.52 sec                                                              | 2.53 sec: 1.00x slower                                                  |
| comprehensions           | 16.7 us                                                               | 16.7 us: 1.00x slower                                                   |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                  |
| meteor_contest           | 107 ms                                                                | 107 ms: 1.01x slower                                                    |
| sqlglot_optimize         | 55.0 ms                                                               | 55.3 ms: 1.01x slower                                                   |
| sympy_integrate          | 21.8 ms                                                               | 22.0 ms: 1.01x slower                                                   |
| raytrace                 | 266 ms                                                                | 267 ms: 1.01x slower                                                    |
| go                       | 145 ms                                                                | 146 ms: 1.01x slower                                                    |
| spectral_norm            | 104 ms                                                                | 105 ms: 1.01x slower                                                    |
| sympy_expand             | 492 ms                                                                | 496 ms: 1.01x slower                                                    |
| create_gc_cycles         | 1.76 ms                                                               | 1.78 ms: 1.01x slower                                                   |
| pycparser                | 1.18 sec                                                              | 1.19 sec: 1.01x slower                                                  |
| sympy_str                | 292 ms                                                                | 295 ms: 1.01x slower                                                    |
| richards_super           | 47.5 ms                                                               | 48.0 ms: 1.01x slower                                                   |
| gc_traversal             | 3.74 ms                                                               | 3.78 ms: 1.01x slower                                                   |
| generators               | 29.5 ms                                                               | 29.9 ms: 1.01x slower                                                   |
| logging_simple           | 5.42 us                                                               | 5.49 us: 1.01x slower                                                   |
| genshi_xml               | 58.0 ms                                                               | 58.7 ms: 1.01x slower                                                   |
| 2to3                     | 271 ms                                                                | 275 ms: 1.01x slower                                                    |
| docutils                 | 2.87 sec                                                              | 2.90 sec: 1.01x slower                                                  |
| async_generators         | 452 ms                                                                | 458 ms: 1.01x slower                                                    |
| genshi_text              | 24.9 ms                                                               | 25.2 ms: 1.01x slower                                                   |
| logging_format           | 5.94 us                                                               | 6.02 us: 1.01x slower                                                   |
| scimark_sor              | 129 ms                                                                | 131 ms: 1.01x slower                                                    |
| mako                     | 9.76 ms                                                               | 9.91 ms: 1.02x slower                                                   |
| regex_v8                 | 25.3 ms                                                               | 25.7 ms: 1.02x slower                                                   |
| scimark_lu               | 124 ms                                                                | 126 ms: 1.02x slower                                                    |
| regex_compile            | 134 ms                                                                | 136 ms: 1.02x slower                                                    |
| deltablue                | 3.52 ms                                                               | 3.60 ms: 1.02x slower                                                   |
| asyncio_tcp              | 488 ms                                                                | 500 ms: 1.02x slower                                                    |
| django_template          | 35.1 ms                                                               | 36.0 ms: 1.02x slower                                                   |
| hexiom                   | 6.48 ms                                                               | 6.65 ms: 1.03x slower                                                   |
| regex_dna                | 222 ms                                                                | 229 ms: 1.03x slower                                                    |
| scimark_fft              | 309 ms                                                                | 320 ms: 1.04x slower                                                    |
| regex_effbot             | 3.86 ms                                                               | 4.02 ms: 1.04x slower                                                   |
| scimark_sparse_mat_mult  | 4.28 ms                                                               | 4.53 ms: 1.06x slower                                                   |
| chaos                    | 58.1 ms                                                               | 61.7 ms: 1.06x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (36): crypto_pyaes, bpe_tokeniser, nqueens, json, pickle_pure_python, deepcopy, sqlglot_normalize, sqlglot_parse, asyncio_websockets, sympy_sum, float, sqlglot_transpile, dulwich_log, async_tree_memoization_tg, coverage, nbody, pidigits, python_startup_no_site, thrift, xml_etree_generate, pathlib, bench_mp_pool, xml_etree_iterparse, tornado_http, dask, json_dumps, async_tree_io_tg, coroutines, async_tree_none_tg, fannkuch, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, pylint

# HPT report

- Reliability score: 99.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x