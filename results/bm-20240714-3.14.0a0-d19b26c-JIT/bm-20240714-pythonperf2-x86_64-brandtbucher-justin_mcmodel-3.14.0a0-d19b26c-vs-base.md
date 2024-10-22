# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.01x faster
- HPT reliability: 99.03%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                      | 298 ms: 1.02x faster                                                        |
| docutils       | 3.11 sec                                                                    | 3.10 sec: 1.01x faster                                                      |
| html5lib       | 71.4 ms                                                                     | 69.1 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 381 ms                                                                      | 383 ms: 1.01x slower                                                        |
| Geometric mean            | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_io, async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 75.7 ms                                                                     | 73.2 ms: 1.03x faster                                                       |
| nbody          | 83.1 ms                                                                     | 81.1 ms: 1.02x faster                                                       |
| pidigits       | 251 ms                                                                      | 251 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 138 ms                                                                      | 133 ms: 1.04x faster                                                        |
| regex_v8       | 26.8 ms                                                                     | 27.1 ms: 1.01x slower                                                       |
| regex_dna      | 256 ms                                                                      | 262 ms: 1.02x slower                                                        |
| regex_effbot   | 3.46 ms                                                                     | 3.58 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                                                    | 2.04 sec: 1.04x faster                                                      |
| pickle_pure_python   | 318 us                                                                      | 312 us: 1.02x faster                                                        |
| xml_etree_process    | 58.5 ms                                                                     | 57.6 ms: 1.02x faster                                                       |
| xml_etree_generate   | 82.1 ms                                                                     | 80.9 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 99.0 ms                                                                     | 97.7 ms: 1.01x faster                                                       |
| unpickle_pure_python | 217 us                                                                      | 217 us: 1.00x slower                                                        |
| xml_etree_parse      | 143 ms                                                                      | 144 ms: 1.00x slower                                                        |
| json_loads           | 25.1 us                                                                     | 25.4 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.4 ms                                                                     | 13.4 ms: 1.01x faster                                                       |
| python_startup_no_site | 9.08 ms                                                                     | 9.04 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 63.8 ms                                                                     | 58.8 ms: 1.09x faster                                                       |
| genshi_text     | 28.5 ms                                                                     | 26.5 ms: 1.08x faster                                                       |
| django_template | 42.1 ms                                                                     | 40.8 ms: 1.03x faster                                                       |
| mako            | 9.21 ms                                                                     | 8.96 ms: 1.03x faster                                                       |
| Geometric mean  | (ref)                                                                       | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml                | 63.8 ms                                                                     | 58.8 ms: 1.09x faster                                                       |
| richards_super            | 53.6 ms                                                                     | 49.6 ms: 1.08x faster                                                       |
| genshi_text               | 28.5 ms                                                                     | 26.5 ms: 1.08x faster                                                       |
| richards                  | 44.9 ms                                                                     | 43.0 ms: 1.04x faster                                                       |
| raytrace                  | 286 ms                                                                      | 275 ms: 1.04x faster                                                        |
| go                        | 161 ms                                                                      | 155 ms: 1.04x faster                                                        |
| deltablue                 | 3.70 ms                                                                     | 3.57 ms: 1.04x faster                                                       |
| regex_compile             | 138 ms                                                                      | 133 ms: 1.04x faster                                                        |
| fannkuch                  | 358 ms                                                                      | 346 ms: 1.04x faster                                                        |
| tomli_loads               | 2.11 sec                                                                    | 2.04 sec: 1.04x faster                                                      |
| scimark_sor               | 128 ms                                                                      | 124 ms: 1.03x faster                                                        |
| float                     | 75.7 ms                                                                     | 73.2 ms: 1.03x faster                                                       |
| html5lib                  | 71.4 ms                                                                     | 69.1 ms: 1.03x faster                                                       |
| django_template           | 42.1 ms                                                                     | 40.8 ms: 1.03x faster                                                       |
| sympy_str                 | 312 ms                                                                      | 303 ms: 1.03x faster                                                        |
| deepcopy                  | 310 us                                                                      | 301 us: 1.03x faster                                                        |
| pprint_pformat            | 1.65 sec                                                                    | 1.60 sec: 1.03x faster                                                      |
| sympy_expand              | 526 ms                                                                      | 512 ms: 1.03x faster                                                        |
| mako                      | 9.21 ms                                                                     | 8.96 ms: 1.03x faster                                                       |
| bench_mp_pool             | 4.91 ms                                                                     | 4.78 ms: 1.03x faster                                                       |
| 2to3                      | 306 ms                                                                      | 298 ms: 1.02x faster                                                        |
| nbody                     | 83.1 ms                                                                     | 81.1 ms: 1.02x faster                                                       |
| async_generators          | 385 ms                                                                      | 376 ms: 1.02x faster                                                        |
| sympy_sum                 | 168 ms                                                                      | 164 ms: 1.02x faster                                                        |
| thrift                    | 918 us                                                                      | 897 us: 1.02x faster                                                        |
| dulwich_log               | 67.2 ms                                                                     | 65.9 ms: 1.02x faster                                                       |
| chaos                     | 65.6 ms                                                                     | 64.3 ms: 1.02x faster                                                       |
| sqlglot_parse             | 1.42 ms                                                                     | 1.39 ms: 1.02x faster                                                       |
| logging_simple            | 6.39 us                                                                     | 6.27 us: 1.02x faster                                                       |
| pickle_pure_python        | 318 us                                                                      | 312 us: 1.02x faster                                                        |
| xml_etree_process         | 58.5 ms                                                                     | 57.6 ms: 1.02x faster                                                       |
| xml_etree_generate        | 82.1 ms                                                                     | 80.9 ms: 1.01x faster                                                       |
| xml_etree_iterparse       | 99.0 ms                                                                     | 97.7 ms: 1.01x faster                                                       |
| pprint_safe_repr          | 805 ms                                                                      | 794 ms: 1.01x faster                                                        |
| sqlglot_optimize          | 63.0 ms                                                                     | 62.2 ms: 1.01x faster                                                       |
| pyflate                   | 443 ms                                                                      | 438 ms: 1.01x faster                                                        |
| logging_format            | 7.09 us                                                                     | 7.00 us: 1.01x faster                                                       |
| hexiom                    | 6.64 ms                                                                     | 6.57 ms: 1.01x faster                                                       |
| sqlglot_transpile         | 1.82 ms                                                                     | 1.80 ms: 1.01x faster                                                       |
| pathlib                   | 16.3 ms                                                                     | 16.1 ms: 1.01x faster                                                       |
| generators                | 34.7 ms                                                                     | 34.4 ms: 1.01x faster                                                       |
| crypto_pyaes              | 70.7 ms                                                                     | 70.1 ms: 1.01x faster                                                       |
| asyncio_websockets        | 394 ms                                                                      | 391 ms: 1.01x faster                                                        |
| python_startup            | 13.4 ms                                                                     | 13.4 ms: 1.01x faster                                                       |
| sympy_integrate           | 25.6 ms                                                                     | 25.4 ms: 1.01x faster                                                       |
| python_startup_no_site    | 9.08 ms                                                                     | 9.04 ms: 1.01x faster                                                       |
| docutils                  | 3.11 sec                                                                    | 3.10 sec: 1.01x faster                                                      |
| asyncio_tcp_ssl           | 1.58 sec                                                                    | 1.58 sec: 1.00x faster                                                      |
| pidigits                  | 251 ms                                                                      | 251 ms: 1.00x faster                                                        |
| unpickle_pure_python      | 217 us                                                                      | 217 us: 1.00x slower                                                        |
| xml_etree_parse           | 143 ms                                                                      | 144 ms: 1.00x slower                                                        |
| meteor_contest            | 129 ms                                                                      | 130 ms: 1.00x slower                                                        |
| async_tree_memoization_tg | 381 ms                                                                      | 383 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult   | 4.17 ms                                                                     | 4.20 ms: 1.01x slower                                                       |
| json                      | 5.46 ms                                                                     | 5.50 ms: 1.01x slower                                                       |
| regex_v8                  | 26.8 ms                                                                     | 27.1 ms: 1.01x slower                                                       |
| json_loads                | 25.1 us                                                                     | 25.4 us: 1.01x slower                                                       |
| asyncio_tcp               | 375 ms                                                                      | 379 ms: 1.01x slower                                                        |
| bpe_tokeniser             | 5.11 sec                                                                    | 5.21 sec: 1.02x slower                                                      |
| deepcopy_memo             | 28.0 us                                                                     | 28.6 us: 1.02x slower                                                       |
| regex_dna                 | 256 ms                                                                      | 262 ms: 1.02x slower                                                        |
| mdp                       | 2.55 sec                                                                    | 2.62 sec: 1.03x slower                                                      |
| gc_traversal              | 4.31 ms                                                                     | 4.43 ms: 1.03x slower                                                       |
| scimark_monte_carlo       | 64.8 ms                                                                     | 66.9 ms: 1.03x slower                                                       |
| telco                     | 8.07 ms                                                                     | 8.35 ms: 1.03x slower                                                       |
| regex_effbot              | 3.46 ms                                                                     | 3.58 ms: 1.04x slower                                                       |
| logging_silent            | 101 ns                                                                      | 105 ns: 1.04x slower                                                        |
| coverage                  | 78.8 ms                                                                     | 82.8 ms: 1.05x slower                                                       |
| scimark_fft               | 291 ms                                                                      | 306 ms: 1.05x slower                                                        |
| scimark_lu                | 112 ms                                                                      | 123 ms: 1.10x slower                                                        |
| Geometric mean            | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (21): nqueens, deepcopy_reduce, pycparser, dask, comprehensions, sqlglot_normalize, tornado_http, create_gc_cycles, coroutines, json_dumps, spectral_norm, async_tree_memoization, async_tree_io, pylint, bench_thread_pool, async_tree_none, async_tree_cpu_io_mixed, typing_runtime_protocols, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io_tg

# HPT report

- Reliability score: 99.03% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x