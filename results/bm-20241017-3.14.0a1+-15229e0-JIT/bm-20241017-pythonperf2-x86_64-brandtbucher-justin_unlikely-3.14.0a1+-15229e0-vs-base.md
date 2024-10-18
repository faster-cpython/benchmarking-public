# Results vs. base

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-x86_64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.00x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 317 ms                                                                       | 317 ms: 1.00x faster                                                          |
| html5lib       | 70.7 ms                                                                      | 70.3 ms: 1.01x faster                                                         |
| tornado_http   | 122 ms                                                                       | 124 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                  |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io              | 860 ms                                                                       | 821 ms: 1.05x faster                                                          |
| async_tree_io_tg           | 879 ms                                                                       | 857 ms: 1.03x faster                                                          |
| async_tree_memoization_tg  | 380 ms                                                                       | 373 ms: 1.02x faster                                                          |
| async_tree_none            | 338 ms                                                                       | 333 ms: 1.02x faster                                                          |
| async_generators           | 385 ms                                                                       | 380 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg | 566 ms                                                                       | 559 ms: 1.01x faster                                                          |
| asyncio_tcp                | 378 ms                                                                       | 376 ms: 1.01x faster                                                          |
| Geometric mean             | (ref)                                                                        | 1.02x faster                                                                  |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, asyncio_websockets, coroutines, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 79.4 ms                                                                      | 78.7 ms: 1.01x faster                                                         |
| nbody          | 83.3 ms                                                                      | 84.6 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.49 ms                                                                      | 3.42 ms: 1.02x faster                                                         |
| regex_dna      | 234 ms                                                                       | 231 ms: 1.02x faster                                                          |
| regex_v8       | 25.1 ms                                                                      | 24.9 ms: 1.01x faster                                                         |
| regex_compile  | 151 ms                                                                       | 153 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_process    | 58.3 ms                                                                      | 56.9 ms: 1.03x faster                                                         |
| pickle               | 10.9 us                                                                      | 10.6 us: 1.03x faster                                                         |
| unpickle             | 15.1 us                                                                      | 14.8 us: 1.02x faster                                                         |
| xml_etree_parse      | 146 ms                                                                       | 143 ms: 1.02x faster                                                          |
| unpickle_pure_python | 227 us                                                                       | 223 us: 1.02x faster                                                          |
| pickle_list          | 4.67 us                                                                      | 4.60 us: 1.01x faster                                                         |
| pickle_pure_python   | 336 us                                                                       | 332 us: 1.01x faster                                                          |
| json_loads           | 24.3 us                                                                      | 24.1 us: 1.01x faster                                                         |
| xml_etree_generate   | 82.1 ms                                                                      | 81.4 ms: 1.01x faster                                                         |
| json_dumps           | 11.2 ms                                                                      | 11.1 ms: 1.00x faster                                                         |
| tomli_loads          | 2.11 sec                                                                     | 2.13 sec: 1.01x slower                                                        |
| pickle_dict          | 32.5 us                                                                      | 32.9 us: 1.01x slower                                                         |
| unpickle_list        | 4.73 us                                                                      | 4.90 us: 1.03x slower                                                         |
| Geometric mean       | (ref)                                                                        | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 43.8 ms                                                                      | 42.7 ms: 1.03x faster                                                         |
| genshi_xml      | 64.8 ms                                                                      | 63.0 ms: 1.03x faster                                                         |
| mako            | 9.50 ms                                                                      | 9.57 ms: 1.01x slower                                                         |
| Geometric mean  | (ref)                                                                        | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| gc_traversal               | 5.80 ms                                                                      | 5.35 ms: 1.08x faster                                                         |
| raytrace                   | 319 ms                                                                       | 299 ms: 1.07x faster                                                          |
| async_tree_io              | 860 ms                                                                       | 821 ms: 1.05x faster                                                          |
| logging_format             | 7.33 us                                                                      | 7.04 us: 1.04x faster                                                         |
| thrift                     | 933 us                                                                       | 898 us: 1.04x faster                                                          |
| django_template            | 43.8 ms                                                                      | 42.7 ms: 1.03x faster                                                         |
| genshi_xml                 | 64.8 ms                                                                      | 63.0 ms: 1.03x faster                                                         |
| chaos                      | 66.9 ms                                                                      | 65.2 ms: 1.03x faster                                                         |
| async_tree_io_tg           | 879 ms                                                                       | 857 ms: 1.03x faster                                                          |
| xml_etree_process          | 58.3 ms                                                                      | 56.9 ms: 1.03x faster                                                         |
| pickle                     | 10.9 us                                                                      | 10.6 us: 1.03x faster                                                         |
| pprint_pformat             | 1.65 sec                                                                     | 1.61 sec: 1.02x faster                                                        |
| crypto_pyaes               | 73.2 ms                                                                      | 71.4 ms: 1.02x faster                                                         |
| pyflate                    | 471 ms                                                                       | 460 ms: 1.02x faster                                                          |
| scimark_sor                | 106 ms                                                                       | 104 ms: 1.02x faster                                                          |
| regex_effbot               | 3.49 ms                                                                      | 3.42 ms: 1.02x faster                                                         |
| unpickle                   | 15.1 us                                                                      | 14.8 us: 1.02x faster                                                         |
| fannkuch                   | 371 ms                                                                       | 364 ms: 1.02x faster                                                          |
| sqlite_synth               | 2.75 us                                                                      | 2.69 us: 1.02x faster                                                         |
| async_tree_memoization_tg  | 380 ms                                                                       | 373 ms: 1.02x faster                                                          |
| telco                      | 7.88 ms                                                                      | 7.74 ms: 1.02x faster                                                         |
| xml_etree_parse            | 146 ms                                                                       | 143 ms: 1.02x faster                                                          |
| unpack_sequence            | 91.6 ns                                                                      | 90.0 ns: 1.02x faster                                                         |
| async_tree_none            | 338 ms                                                                       | 333 ms: 1.02x faster                                                          |
| regex_dna                  | 234 ms                                                                       | 231 ms: 1.02x faster                                                          |
| unpickle_pure_python       | 227 us                                                                       | 223 us: 1.02x faster                                                          |
| deltablue                  | 3.35 ms                                                                      | 3.30 ms: 1.02x faster                                                         |
| sqlglot_transpile          | 2.01 ms                                                                      | 1.98 ms: 1.02x faster                                                         |
| pickle_list                | 4.67 us                                                                      | 4.60 us: 1.01x faster                                                         |
| scimark_lu                 | 96.1 ms                                                                      | 94.7 ms: 1.01x faster                                                         |
| async_generators           | 385 ms                                                                       | 380 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg | 566 ms                                                                       | 559 ms: 1.01x faster                                                          |
| json                       | 5.10 ms                                                                      | 5.03 ms: 1.01x faster                                                         |
| logging_simple             | 6.62 us                                                                      | 6.53 us: 1.01x faster                                                         |
| coverage                   | 80.8 ms                                                                      | 79.8 ms: 1.01x faster                                                         |
| pickle_pure_python         | 336 us                                                                       | 332 us: 1.01x faster                                                          |
| pathlib                    | 16.0 ms                                                                      | 15.8 ms: 1.01x faster                                                         |
| json_loads                 | 24.3 us                                                                      | 24.1 us: 1.01x faster                                                         |
| mdp                        | 2.65 sec                                                                     | 2.62 sec: 1.01x faster                                                        |
| logging_silent             | 92.3 ns                                                                      | 91.4 ns: 1.01x faster                                                         |
| spectral_norm              | 94.2 ms                                                                      | 93.3 ms: 1.01x faster                                                         |
| float                      | 79.4 ms                                                                      | 78.7 ms: 1.01x faster                                                         |
| sqlglot_parse              | 1.53 ms                                                                      | 1.51 ms: 1.01x faster                                                         |
| pprint_safe_repr           | 795 ms                                                                       | 788 ms: 1.01x faster                                                          |
| regex_v8                   | 25.1 ms                                                                      | 24.9 ms: 1.01x faster                                                         |
| bpe_tokeniser              | 4.81 sec                                                                     | 4.77 sec: 1.01x faster                                                        |
| xml_etree_generate         | 82.1 ms                                                                      | 81.4 ms: 1.01x faster                                                         |
| scimark_monte_carlo        | 70.2 ms                                                                      | 69.7 ms: 1.01x faster                                                         |
| html5lib                   | 70.7 ms                                                                      | 70.3 ms: 1.01x faster                                                         |
| scimark_fft                | 289 ms                                                                       | 288 ms: 1.01x faster                                                          |
| asyncio_tcp                | 378 ms                                                                       | 376 ms: 1.01x faster                                                          |
| json_dumps                 | 11.2 ms                                                                      | 11.1 ms: 1.00x faster                                                         |
| 2to3                       | 317 ms                                                                       | 317 ms: 1.00x faster                                                          |
| comprehensions             | 18.5 us                                                                      | 18.6 us: 1.00x slower                                                         |
| go                         | 156 ms                                                                       | 156 ms: 1.00x slower                                                          |
| mako                       | 9.50 ms                                                                      | 9.57 ms: 1.01x slower                                                         |
| sympy_integrate            | 27.4 ms                                                                      | 27.6 ms: 1.01x slower                                                         |
| tomli_loads                | 2.11 sec                                                                     | 2.13 sec: 1.01x slower                                                        |
| hexiom                     | 7.12 ms                                                                      | 7.18 ms: 1.01x slower                                                         |
| sqlglot_optimize           | 69.2 ms                                                                      | 69.9 ms: 1.01x slower                                                         |
| deepcopy_reduce            | 3.08 us                                                                      | 3.11 us: 1.01x slower                                                         |
| pickle_dict                | 32.5 us                                                                      | 32.9 us: 1.01x slower                                                         |
| tornado_http               | 122 ms                                                                       | 124 ms: 1.01x slower                                                          |
| scimark_sparse_mat_mult    | 4.35 ms                                                                      | 4.41 ms: 1.01x slower                                                         |
| generators                 | 38.4 ms                                                                      | 38.9 ms: 1.01x slower                                                         |
| bench_thread_pool          | 941 us                                                                       | 955 us: 1.02x slower                                                          |
| nbody                      | 83.3 ms                                                                      | 84.6 ms: 1.02x slower                                                         |
| regex_compile              | 151 ms                                                                       | 153 ms: 1.02x slower                                                          |
| meteor_contest             | 133 ms                                                                       | 135 ms: 1.02x slower                                                          |
| sqlglot_normalize          | 130 ms                                                                       | 133 ms: 1.03x slower                                                          |
| deepcopy                   | 310 us                                                                       | 319 us: 1.03x slower                                                          |
| unpickle_list              | 4.73 us                                                                      | 4.90 us: 1.03x slower                                                         |
| richards                   | 42.9 ms                                                                      | 44.5 ms: 1.04x slower                                                         |
| bench_mp_pool              | 1.45 sec                                                                     | 3.14 sec: 2.17x slower                                                        |
| Geometric mean             | (ref)                                                                        | 1.00x slower                                                                  |

Benchmark hidden because not significant (24): async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, nqueens, create_gc_cycles, asyncio_websockets, dulwich_log, sympy_sum, coroutines, docutils, python_startup, sympy_str, pidigits, asyncio_tcp_ssl, sympy_expand, python_startup_no_site, richards_super, genshi_text, xml_etree_iterparse, pycparser, sphinx, typing_runtime_protocols, deepcopy_memo, pylint

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x