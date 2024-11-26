# Results vs. base

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-x86_64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.006x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 317 ms                                                                       | 317 ms: 1.00x faster                                                          |
| docutils       | 3.23 sec                                                                     | 3.21 sec: 1.01x faster                                                        |
| html5lib       | 69.6 ms                                                                      | 70.3 ms: 1.01x slower                                                         |
| tornado_http   | 122 ms                                                                       | 124 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io              | 851 ms                                                                       | 821 ms: 1.04x faster                                                          |
| async_tree_io_tg           | 872 ms                                                                       | 857 ms: 1.02x faster                                                          |
| async_tree_memoization_tg  | 378 ms                                                                       | 373 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                       | 559 ms: 1.01x faster                                                          |
| async_tree_none            | 336 ms                                                                       | 333 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl            | 1.58 sec                                                                     | 1.59 sec: 1.00x slower                                                        |
| coroutines                 | 21.6 ms                                                                      | 21.6 ms: 1.00x slower                                                         |
| asyncio_tcp                | 374 ms                                                                       | 376 ms: 1.01x slower                                                          |
| async_generators           | 378 ms                                                                       | 380 ms: 1.01x slower                                                          |
| Geometric mean             | (ref)                                                                        | 1.01x faster                                                                  |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 79.1 ms                                                                      | 78.7 ms: 1.01x faster                                                         |
| pidigits       | 252 ms                                                                       | 252 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 27.3 ms                                                                      | 24.9 ms: 1.09x faster                                                         |
| regex_dna      | 246 ms                                                                       | 231 ms: 1.07x faster                                                          |
| regex_effbot   | 3.52 ms                                                                      | 3.42 ms: 1.03x faster                                                         |
| regex_compile  | 152 ms                                                                       | 153 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                        | 1.05x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle             | 15.4 us                                                                      | 14.8 us: 1.04x faster                                                         |
| xml_etree_process    | 58.2 ms                                                                      | 56.9 ms: 1.02x faster                                                         |
| tomli_loads          | 2.16 sec                                                                     | 2.13 sec: 1.01x faster                                                        |
| unpickle_pure_python | 225 us                                                                       | 223 us: 1.01x faster                                                          |
| xml_etree_parse      | 144 ms                                                                       | 143 ms: 1.01x faster                                                          |
| pickle_pure_python   | 333 us                                                                       | 332 us: 1.00x faster                                                          |
| json_loads           | 24.2 us                                                                      | 24.1 us: 1.00x faster                                                         |
| pickle               | 10.5 us                                                                      | 10.6 us: 1.01x slower                                                         |
| json_dumps           | 11.0 ms                                                                      | 11.1 ms: 1.01x slower                                                         |
| unpickle_list        | 4.82 us                                                                      | 4.90 us: 1.02x slower                                                         |
| pickle_list          | 4.43 us                                                                      | 4.60 us: 1.04x slower                                                         |
| pickle_dict          | 30.9 us                                                                      | 32.9 us: 1.06x slower                                                         |
| Geometric mean       | (ref)                                                                        | 1.00x slower                                                                  |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 15.0 ms                                                                      | 15.0 ms: 1.00x slower                                                         |
| python_startup_no_site | 9.01 ms                                                                      | 9.02 ms: 1.00x slower                                                         |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 30.1 ms                                                                      | 28.8 ms: 1.04x faster                                                         |
| genshi_xml      | 65.7 ms                                                                      | 63.0 ms: 1.04x faster                                                         |
| django_template | 43.5 ms                                                                      | 42.7 ms: 1.02x faster                                                         |
| mako            | 9.42 ms                                                                      | 9.57 ms: 1.02x slower                                                         |
| Geometric mean  | (ref)                                                                        | 1.02x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8                   | 27.3 ms                                                                      | 24.9 ms: 1.09x faster                                                         |
| regex_dna                  | 246 ms                                                                       | 231 ms: 1.07x faster                                                          |
| scimark_sor                | 109 ms                                                                       | 104 ms: 1.05x faster                                                          |
| nqueens                    | 106 ms                                                                       | 101 ms: 1.05x faster                                                          |
| unpickle                   | 15.4 us                                                                      | 14.8 us: 1.04x faster                                                         |
| genshi_text                | 30.1 ms                                                                      | 28.8 ms: 1.04x faster                                                         |
| genshi_xml                 | 65.7 ms                                                                      | 63.0 ms: 1.04x faster                                                         |
| coverage                   | 82.9 ms                                                                      | 79.8 ms: 1.04x faster                                                         |
| async_tree_io              | 851 ms                                                                       | 821 ms: 1.04x faster                                                          |
| pyflate                    | 476 ms                                                                       | 460 ms: 1.04x faster                                                          |
| chaos                      | 67.5 ms                                                                      | 65.2 ms: 1.03x faster                                                         |
| regex_effbot               | 3.52 ms                                                                      | 3.42 ms: 1.03x faster                                                         |
| gc_traversal               | 5.50 ms                                                                      | 5.35 ms: 1.03x faster                                                         |
| logging_format             | 7.22 us                                                                      | 7.04 us: 1.03x faster                                                         |
| xml_etree_process          | 58.2 ms                                                                      | 56.9 ms: 1.02x faster                                                         |
| django_template            | 43.5 ms                                                                      | 42.7 ms: 1.02x faster                                                         |
| pprint_pformat             | 1.64 sec                                                                     | 1.61 sec: 1.02x faster                                                        |
| async_tree_io_tg           | 872 ms                                                                       | 857 ms: 1.02x faster                                                          |
| comprehensions             | 18.9 us                                                                      | 18.6 us: 1.02x faster                                                         |
| raytrace                   | 303 ms                                                                       | 299 ms: 1.01x faster                                                          |
| tomli_loads                | 2.16 sec                                                                     | 2.13 sec: 1.01x faster                                                        |
| async_tree_memoization_tg  | 378 ms                                                                       | 373 ms: 1.01x faster                                                          |
| fannkuch                   | 368 ms                                                                       | 364 ms: 1.01x faster                                                          |
| crypto_pyaes               | 72.1 ms                                                                      | 71.4 ms: 1.01x faster                                                         |
| sqlglot_parse              | 1.52 ms                                                                      | 1.51 ms: 1.01x faster                                                         |
| pprint_safe_repr           | 795 ms                                                                       | 788 ms: 1.01x faster                                                          |
| sqlglot_transpile          | 2.00 ms                                                                      | 1.98 ms: 1.01x faster                                                         |
| mdp                        | 2.64 sec                                                                     | 2.62 sec: 1.01x faster                                                        |
| bpe_tokeniser              | 4.81 sec                                                                     | 4.77 sec: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                       | 559 ms: 1.01x faster                                                          |
| async_tree_none            | 336 ms                                                                       | 333 ms: 1.01x faster                                                          |
| unpickle_pure_python       | 225 us                                                                       | 223 us: 1.01x faster                                                          |
| dulwich_log                | 65.4 ms                                                                      | 65.0 ms: 1.01x faster                                                         |
| docutils                   | 3.23 sec                                                                     | 3.21 sec: 1.01x faster                                                        |
| float                      | 79.1 ms                                                                      | 78.7 ms: 1.01x faster                                                         |
| scimark_lu                 | 95.2 ms                                                                      | 94.7 ms: 1.01x faster                                                         |
| xml_etree_parse            | 144 ms                                                                       | 143 ms: 1.01x faster                                                          |
| sqlite_synth               | 2.70 us                                                                      | 2.69 us: 1.00x faster                                                         |
| pickle_pure_python         | 333 us                                                                       | 332 us: 1.00x faster                                                          |
| json_loads                 | 24.2 us                                                                      | 24.1 us: 1.00x faster                                                         |
| unpack_sequence            | 90.4 ns                                                                      | 90.0 ns: 1.00x faster                                                         |
| sympy_expand               | 537 ms                                                                       | 535 ms: 1.00x faster                                                          |
| pidigits                   | 252 ms                                                                       | 252 ms: 1.00x faster                                                          |
| 2to3                       | 317 ms                                                                       | 317 ms: 1.00x faster                                                          |
| python_startup             | 15.0 ms                                                                      | 15.0 ms: 1.00x slower                                                         |
| python_startup_no_site     | 9.01 ms                                                                      | 9.02 ms: 1.00x slower                                                         |
| asyncio_tcp_ssl            | 1.58 sec                                                                     | 1.59 sec: 1.00x slower                                                        |
| hexiom                     | 7.16 ms                                                                      | 7.18 ms: 1.00x slower                                                         |
| coroutines                 | 21.6 ms                                                                      | 21.6 ms: 1.00x slower                                                         |
| richards_super             | 49.6 ms                                                                      | 49.8 ms: 1.00x slower                                                         |
| asyncio_tcp                | 374 ms                                                                       | 376 ms: 1.01x slower                                                          |
| async_generators           | 378 ms                                                                       | 380 ms: 1.01x slower                                                          |
| regex_compile              | 152 ms                                                                       | 153 ms: 1.01x slower                                                          |
| thrift                     | 892 us                                                                       | 898 us: 1.01x slower                                                          |
| pickle                     | 10.5 us                                                                      | 10.6 us: 1.01x slower                                                         |
| scimark_sparse_mat_mult    | 4.37 ms                                                                      | 4.41 ms: 1.01x slower                                                         |
| telco                      | 7.67 ms                                                                      | 7.74 ms: 1.01x slower                                                         |
| json_dumps                 | 11.0 ms                                                                      | 11.1 ms: 1.01x slower                                                         |
| html5lib                   | 69.6 ms                                                                      | 70.3 ms: 1.01x slower                                                         |
| scimark_fft                | 284 ms                                                                       | 288 ms: 1.01x slower                                                          |
| mako                       | 9.42 ms                                                                      | 9.57 ms: 1.02x slower                                                         |
| pycparser                  | 1.28 sec                                                                     | 1.30 sec: 1.02x slower                                                        |
| tornado_http               | 122 ms                                                                       | 124 ms: 1.02x slower                                                          |
| unpickle_list              | 4.82 us                                                                      | 4.90 us: 1.02x slower                                                         |
| generators                 | 38.3 ms                                                                      | 38.9 ms: 1.02x slower                                                         |
| typing_runtime_protocols   | 179 us                                                                       | 182 us: 1.02x slower                                                          |
| deepcopy_reduce            | 3.05 us                                                                      | 3.11 us: 1.02x slower                                                         |
| deepcopy_memo              | 29.0 us                                                                      | 29.7 us: 1.02x slower                                                         |
| richards                   | 43.5 ms                                                                      | 44.5 ms: 1.02x slower                                                         |
| meteor_contest             | 132 ms                                                                       | 135 ms: 1.02x slower                                                          |
| go                         | 152 ms                                                                       | 156 ms: 1.03x slower                                                          |
| deepcopy                   | 310 us                                                                       | 319 us: 1.03x slower                                                          |
| pickle_list                | 4.43 us                                                                      | 4.60 us: 1.04x slower                                                         |
| pickle_dict                | 30.9 us                                                                      | 32.9 us: 1.06x slower                                                         |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                                  |

Benchmark hidden because not significant (24): async_tree_none_tg, async_tree_memoization, logging_simple, nbody, json, async_tree_cpu_io_mixed, deltablue, sphinx, pathlib, logging_silent, asyncio_websockets, sqlglot_optimize, sympy_str, xml_etree_generate, spectral_norm, bench_thread_pool, sympy_sum, sqlglot_normalize, scimark_monte_carlo, xml_etree_iterparse, sympy_integrate, create_gc_cycles, pylint, bench_mp_pool

- Geometric mean (including insignificant results): 1.006x faster
# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x