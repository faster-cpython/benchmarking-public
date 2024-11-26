# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: linux-x86_64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.037x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 280 ms: 1.05x faster                                                                  |
| docutils       | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                                |
| html5lib       | 72.9 ms                                                      | 70.1 ms: 1.04x faster                                                                 |
| tornado_http   | 119 ms                                                       | 116 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 393 ms: 1.17x faster                                                                  |
| async_tree_none            | 370 ms                                                       | 321 ms: 1.15x faster                                                                  |
| async_tree_memoization     | 447 ms                                                       | 403 ms: 1.11x faster                                                                  |
| async_tree_none_tg         | 342 ms                                                       | 309 ms: 1.11x faster                                                                  |
| async_tree_io_tg           | 823 ms                                                       | 783 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 550 ms: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                                  |
| async_tree_io              | 832 ms                                                       | 803 ms: 1.04x faster                                                                  |
| asyncio_websockets         | 395 ms                                                       | 390 ms: 1.01x faster                                                                  |
| async_generators           | 364 ms                                                       | 371 ms: 1.02x slower                                                                  |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                          |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 80.6 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                          |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 140 ms: 1.02x faster                                                                  |
| regex_effbot   | 3.51 ms                                                      | 3.46 ms: 1.02x faster                                                                 |
| regex_dna      | 238 ms                                                       | 242 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pickle_pure_python   | 322 us                                                       | 317 us: 1.02x faster                                                                  |
| xml_etree_process    | 60.7 ms                                                      | 59.9 ms: 1.01x faster                                                                 |
| unpickle_pure_python | 216 us                                                       | 215 us: 1.01x faster                                                                  |
| xml_etree_generate   | 85.2 ms                                                      | 84.9 ms: 1.00x faster                                                                 |
| json_loads           | 24.7 us                                                      | 24.9 us: 1.01x slower                                                                 |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                                  |
| xml_etree_iterparse  | 99.8 ms                                                      | 101 ms: 1.02x slower                                                                  |
| tomli_loads          | 2.43 sec                                                     | 2.50 sec: 1.03x slower                                                                |
| json_dumps           | 10.8 ms                                                      | 12.1 ms: 1.11x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                                 |
| python_startup_no_site | 8.93 ms                                                      | 8.96 ms: 1.00x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.6 ms: 1.11x faster                                                                 |
| genshi_xml      | 58.0 ms                                                      | 53.1 ms: 1.09x faster                                                                 |
| mako            | 10.3 ms                                                      | 10.8 ms: 1.04x slower                                                                 |
| django_template | 38.9 ms                                                      | 42.7 ms: 1.10x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 287 us: 1.35x faster                                                                  |
| deepcopy_memo              | 38.9 us                                                      | 29.6 us: 1.31x faster                                                                 |
| create_gc_cycles           | 2.65 ms                                                      | 2.06 ms: 1.29x faster                                                                 |
| go                         | 167 ms                                                       | 137 ms: 1.22x faster                                                                  |
| deepcopy_reduce            | 3.49 us                                                      | 2.96 us: 1.18x faster                                                                 |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                                 |
| async_tree_memoization_tg  | 458 ms                                                       | 393 ms: 1.17x faster                                                                  |
| scimark_sor                | 125 ms                                                       | 108 ms: 1.16x faster                                                                  |
| generators                 | 33.9 ms                                                      | 29.3 ms: 1.16x faster                                                                 |
| async_tree_none            | 370 ms                                                       | 321 ms: 1.15x faster                                                                  |
| telco                      | 8.77 ms                                                      | 7.88 ms: 1.11x faster                                                                 |
| async_tree_memoization     | 447 ms                                                       | 403 ms: 1.11x faster                                                                  |
| async_tree_none_tg         | 342 ms                                                       | 309 ms: 1.11x faster                                                                  |
| genshi_text                | 27.2 ms                                                      | 24.6 ms: 1.11x faster                                                                 |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.11x faster                                                                 |
| genshi_xml                 | 58.0 ms                                                      | 53.1 ms: 1.09x faster                                                                 |
| fannkuch                   | 384 ms                                                       | 353 ms: 1.09x faster                                                                  |
| richards_super             | 60.2 ms                                                      | 56.2 ms: 1.07x faster                                                                 |
| coverage                   | 84.5 ms                                                      | 78.9 ms: 1.07x faster                                                                 |
| pprint_safe_repr           | 835 ms                                                       | 784 ms: 1.06x faster                                                                  |
| richards                   | 52.5 ms                                                      | 49.3 ms: 1.06x faster                                                                 |
| meteor_contest             | 130 ms                                                       | 123 ms: 1.06x faster                                                                  |
| bpe_tokeniser              | 5.09 sec                                                     | 4.80 sec: 1.06x faster                                                                |
| pycparser                  | 1.28 sec                                                     | 1.21 sec: 1.06x faster                                                                |
| pprint_pformat             | 1.70 sec                                                     | 1.61 sec: 1.05x faster                                                                |
| async_tree_io_tg           | 823 ms                                                       | 783 ms: 1.05x faster                                                                  |
| thrift                     | 918 us                                                       | 876 us: 1.05x faster                                                                  |
| bench_thread_pool          | 929 us                                                       | 888 us: 1.05x faster                                                                  |
| 2to3                       | 293 ms                                                       | 280 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 550 ms: 1.04x faster                                                                  |
| json                       | 5.62 ms                                                      | 5.39 ms: 1.04x faster                                                                 |
| html5lib                   | 72.9 ms                                                      | 70.1 ms: 1.04x faster                                                                 |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                                  |
| async_tree_io              | 832 ms                                                       | 803 ms: 1.04x faster                                                                  |
| hexiom                     | 6.47 ms                                                      | 6.26 ms: 1.03x faster                                                                 |
| scimark_lu                 | 97.4 ms                                                      | 94.3 ms: 1.03x faster                                                                 |
| nqueens                    | 92.3 ms                                                      | 90.0 ms: 1.03x faster                                                                 |
| tornado_http               | 119 ms                                                       | 116 ms: 1.02x faster                                                                  |
| mdp                        | 2.53 sec                                                     | 2.47 sec: 1.02x faster                                                                |
| sympy_expand               | 506 ms                                                       | 495 ms: 1.02x faster                                                                  |
| sympy_str                  | 297 ms                                                       | 290 ms: 1.02x faster                                                                  |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                                  |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.13 ms: 1.02x faster                                                                 |
| regex_compile              | 143 ms                                                       | 140 ms: 1.02x faster                                                                  |
| pyflate                    | 493 ms                                                       | 484 ms: 1.02x faster                                                                  |
| regex_effbot               | 3.51 ms                                                      | 3.46 ms: 1.02x faster                                                                 |
| pickle_pure_python         | 322 us                                                       | 317 us: 1.02x faster                                                                  |
| xml_etree_process          | 60.7 ms                                                      | 59.9 ms: 1.01x faster                                                                 |
| asyncio_websockets         | 395 ms                                                       | 390 ms: 1.01x faster                                                                  |
| float                      | 81.6 ms                                                      | 80.6 ms: 1.01x faster                                                                 |
| spectral_norm              | 97.4 ms                                                      | 96.5 ms: 1.01x faster                                                                 |
| unpickle_pure_python       | 216 us                                                       | 215 us: 1.01x faster                                                                  |
| comprehensions             | 17.3 us                                                      | 17.1 us: 1.01x faster                                                                 |
| crypto_pyaes               | 73.5 ms                                                      | 73.1 ms: 1.01x faster                                                                 |
| xml_etree_generate         | 85.2 ms                                                      | 84.9 ms: 1.00x faster                                                                 |
| python_startup_no_site     | 8.93 ms                                                      | 8.96 ms: 1.00x slower                                                                 |
| sqlglot_normalize          | 119 ms                                                       | 119 ms: 1.00x slower                                                                  |
| dulwich_log                | 65.5 ms                                                      | 65.9 ms: 1.01x slower                                                                 |
| logging_silent             | 97.5 ns                                                      | 98.2 ns: 1.01x slower                                                                 |
| json_loads                 | 24.7 us                                                      | 24.9 us: 1.01x slower                                                                 |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                                  |
| sqlglot_transpile          | 1.76 ms                                                      | 1.78 ms: 1.01x slower                                                                 |
| sqlglot_optimize           | 58.7 ms                                                      | 59.5 ms: 1.02x slower                                                                 |
| regex_dna                  | 238 ms                                                       | 242 ms: 1.02x slower                                                                  |
| xml_etree_iterparse        | 99.8 ms                                                      | 101 ms: 1.02x slower                                                                  |
| scimark_monte_carlo        | 65.2 ms                                                      | 66.4 ms: 1.02x slower                                                                 |
| logging_format             | 6.95 us                                                      | 7.08 us: 1.02x slower                                                                 |
| async_generators           | 364 ms                                                       | 371 ms: 1.02x slower                                                                  |
| tomli_loads                | 2.43 sec                                                     | 2.50 sec: 1.03x slower                                                                |
| docutils                   | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                                |
| sqlglot_parse              | 1.37 ms                                                      | 1.41 ms: 1.03x slower                                                                 |
| logging_simple             | 6.28 us                                                      | 6.52 us: 1.04x slower                                                                 |
| mako                       | 10.3 ms                                                      | 10.8 ms: 1.04x slower                                                                 |
| chaos                      | 60.6 ms                                                      | 63.5 ms: 1.05x slower                                                                 |
| gc_traversal               | 4.48 ms                                                      | 4.74 ms: 1.06x slower                                                                 |
| django_template            | 38.9 ms                                                      | 42.7 ms: 1.10x slower                                                                 |
| json_dumps                 | 10.8 ms                                                      | 12.1 ms: 1.11x slower                                                                 |
| bench_mp_pool              | 4.82 ms                                                      | 2.45 sec: 509.52x slower                                                              |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                          |

Benchmark hidden because not significant (10): nbody, coroutines, scimark_fft, sympy_integrate, typing_runtime_protocols, raytrace, regex_v8, pidigits, pylint, deltablue
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.037x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x