# Results vs. base

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.00x faster
- HPT reliability: 97.08%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                      | 306 ms: 1.00x slower                                                              |
| docutils       | 3.11 sec                                                                    | 3.08 sec: 1.01x faster                                                            |
| html5lib       | 71.4 ms                                                                     | 70.4 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io, async_tree_none, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 75.7 ms                                                                     | 74.1 ms: 1.02x faster                                                             |
| pidigits       | 251 ms                                                                      | 250 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 256 ms                                                                      | 235 ms: 1.09x faster                                                              |
| regex_v8       | 26.8 ms                                                                     | 25.6 ms: 1.05x faster                                                             |
| regex_compile  | 138 ms                                                                      | 135 ms: 1.02x faster                                                              |
| regex_effbot   | 3.46 ms                                                                     | 3.49 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                       | 1.04x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 217 us                                                                      | 211 us: 1.03x faster                                                              |
| json_dumps           | 11.0 ms                                                                     | 10.9 ms: 1.02x faster                                                             |
| tomli_loads          | 2.11 sec                                                                    | 2.09 sec: 1.01x faster                                                            |
| pickle_pure_python   | 318 us                                                                      | 315 us: 1.01x faster                                                              |
| xml_etree_process    | 58.5 ms                                                                     | 58.0 ms: 1.01x faster                                                             |
| xml_etree_generate   | 82.1 ms                                                                     | 81.8 ms: 1.00x faster                                                             |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                      |

Benchmark hidden because not significant (3): json_loads, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 13.4 ms                                                                     | 13.4 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 42.1 ms                                                                     | 40.8 ms: 1.03x faster                                                             |
| genshi_xml      | 63.8 ms                                                                     | 61.9 ms: 1.03x faster                                                             |
| mako            | 9.21 ms                                                                     | 9.24 ms: 1.00x slower                                                             |
| genshi_text     | 28.5 ms                                                                     | 29.2 ms: 1.03x slower                                                             |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|--------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna                | 256 ms                                                                      | 235 ms: 1.09x faster                                                              |
| scimark_sparse_mat_mult  | 4.17 ms                                                                     | 3.92 ms: 1.06x faster                                                             |
| bpe_tokeniser            | 5.11 sec                                                                    | 4.88 sec: 1.05x faster                                                            |
| regex_v8                 | 26.8 ms                                                                     | 25.6 ms: 1.05x faster                                                             |
| fannkuch                 | 358 ms                                                                      | 345 ms: 1.04x faster                                                              |
| django_template          | 42.1 ms                                                                     | 40.8 ms: 1.03x faster                                                             |
| genshi_xml               | 63.8 ms                                                                     | 61.9 ms: 1.03x faster                                                             |
| bench_mp_pool            | 4.91 ms                                                                     | 4.77 ms: 1.03x faster                                                             |
| dulwich_log              | 67.2 ms                                                                     | 65.3 ms: 1.03x faster                                                             |
| richards_super           | 53.6 ms                                                                     | 52.1 ms: 1.03x faster                                                             |
| unpickle_pure_python     | 217 us                                                                      | 211 us: 1.03x faster                                                              |
| float                    | 75.7 ms                                                                     | 74.1 ms: 1.02x faster                                                             |
| regex_compile            | 138 ms                                                                      | 135 ms: 1.02x faster                                                              |
| dask                     | 400 ms                                                                      | 393 ms: 1.02x faster                                                              |
| scimark_sor              | 128 ms                                                                      | 126 ms: 1.02x faster                                                              |
| logging_format           | 7.09 us                                                                     | 6.96 us: 1.02x faster                                                             |
| json_dumps               | 11.0 ms                                                                     | 10.9 ms: 1.02x faster                                                             |
| deltablue                | 3.70 ms                                                                     | 3.64 ms: 1.02x faster                                                             |
| sympy_str                | 312 ms                                                                      | 308 ms: 1.02x faster                                                              |
| pyflate                  | 443 ms                                                                      | 437 ms: 1.01x faster                                                              |
| crypto_pyaes             | 70.7 ms                                                                     | 69.7 ms: 1.01x faster                                                             |
| sympy_expand             | 526 ms                                                                      | 519 ms: 1.01x faster                                                              |
| html5lib                 | 71.4 ms                                                                     | 70.4 ms: 1.01x faster                                                             |
| sympy_sum                | 168 ms                                                                      | 165 ms: 1.01x faster                                                              |
| thrift                   | 918 us                                                                      | 906 us: 1.01x faster                                                              |
| pprint_pformat           | 1.65 sec                                                                    | 1.63 sec: 1.01x faster                                                            |
| typing_runtime_protocols | 184 us                                                                      | 182 us: 1.01x faster                                                              |
| deepcopy                 | 310 us                                                                      | 307 us: 1.01x faster                                                              |
| tomli_loads              | 2.11 sec                                                                    | 2.09 sec: 1.01x faster                                                            |
| sqlglot_optimize         | 63.0 ms                                                                     | 62.4 ms: 1.01x faster                                                             |
| docutils                 | 3.11 sec                                                                    | 3.08 sec: 1.01x faster                                                            |
| pickle_pure_python       | 318 us                                                                      | 315 us: 1.01x faster                                                              |
| xml_etree_process        | 58.5 ms                                                                     | 58.0 ms: 1.01x faster                                                             |
| spectral_norm            | 82.9 ms                                                                     | 82.3 ms: 1.01x faster                                                             |
| asyncio_tcp              | 375 ms                                                                      | 373 ms: 1.01x faster                                                              |
| richards                 | 44.9 ms                                                                     | 44.7 ms: 1.01x faster                                                             |
| async_generators         | 385 ms                                                                      | 383 ms: 1.01x faster                                                              |
| pidigits                 | 251 ms                                                                      | 250 ms: 1.00x faster                                                              |
| python_startup           | 13.4 ms                                                                     | 13.4 ms: 1.00x faster                                                             |
| sympy_integrate          | 25.6 ms                                                                     | 25.5 ms: 1.00x faster                                                             |
| xml_etree_generate       | 82.1 ms                                                                     | 81.8 ms: 1.00x faster                                                             |
| 2to3                     | 306 ms                                                                      | 306 ms: 1.00x slower                                                              |
| mako                     | 9.21 ms                                                                     | 9.24 ms: 1.00x slower                                                             |
| meteor_contest           | 129 ms                                                                      | 130 ms: 1.00x slower                                                              |
| scimark_lu               | 112 ms                                                                      | 113 ms: 1.01x slower                                                              |
| deepcopy_memo            | 28.0 us                                                                     | 28.2 us: 1.01x slower                                                             |
| telco                    | 8.07 ms                                                                     | 8.14 ms: 1.01x slower                                                             |
| regex_effbot             | 3.46 ms                                                                     | 3.49 ms: 1.01x slower                                                             |
| create_gc_cycles         | 1.92 ms                                                                     | 1.94 ms: 1.01x slower                                                             |
| scimark_monte_carlo      | 64.8 ms                                                                     | 65.7 ms: 1.02x slower                                                             |
| go                       | 161 ms                                                                      | 163 ms: 1.02x slower                                                              |
| mdp                      | 2.55 sec                                                                    | 2.61 sec: 1.02x slower                                                            |
| genshi_text              | 28.5 ms                                                                     | 29.2 ms: 1.03x slower                                                             |
| coverage                 | 78.8 ms                                                                     | 81.1 ms: 1.03x slower                                                             |
| raytrace                 | 286 ms                                                                      | 295 ms: 1.03x slower                                                              |
| pycparser                | 1.21 sec                                                                    | 1.25 sec: 1.03x slower                                                            |
| generators               | 34.7 ms                                                                     | 36.0 ms: 1.04x slower                                                             |
| logging_silent           | 101 ns                                                                      | 105 ns: 1.04x slower                                                              |
| coroutines               | 21.1 ms                                                                     | 22.1 ms: 1.05x slower                                                             |
| gc_traversal             | 4.31 ms                                                                     | 4.68 ms: 1.09x slower                                                             |
| Geometric mean           | (ref)                                                                       | 1.00x faster                                                                      |

Benchmark hidden because not significant (31): nqueens, async_tree_io_tg, pylint, tornado_http, pprint_safe_repr, deepcopy_reduce, scimark_fft, logging_simple, sqlglot_normalize, sqlglot_parse, hexiom, bench_thread_pool, json, chaos, sqlglot_transpile, json_loads, pathlib, asyncio_tcp_ssl, xml_etree_parse, python_startup_no_site, comprehensions, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_memoization_tg, async_tree_io, async_tree_none, xml_etree_iterparse, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization, nbody

# HPT report

- Reliability score: 97.08% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x