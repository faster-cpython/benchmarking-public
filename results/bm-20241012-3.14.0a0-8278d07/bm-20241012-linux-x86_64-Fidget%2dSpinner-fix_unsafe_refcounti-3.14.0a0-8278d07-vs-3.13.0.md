# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: linux-x86_64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.032x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 252 ms: 1.06x faster                                                            |
| docutils       | 2.59 sec                                               | 2.63 sec: 1.01x slower                                                          |
| html5lib       | 64.2 ms                                                | 61.9 ms: 1.04x faster                                                           |
| tornado_http   | 92.4 ms                                                | 89.9 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 403 ms: 1.15x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 391 ms: 1.13x faster                                                            |
| async_tree_none           | 351 ms                                                 | 320 ms: 1.10x faster                                                            |
| async_tree_none_tg        | 321 ms                                                 | 309 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 562 ms: 1.03x faster                                                            |
| async_generators          | 436 ms                                                 | 431 ms: 1.01x faster                                                            |
| asyncio_websockets        | 552 ms                                                 | 558 ms: 1.01x slower                                                            |
| coroutines                | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                           |
| async_tree_io_tg          | 857 ms                                                 | 915 ms: 1.07x slower                                                            |
| async_tree_io             | 842 ms                                                 | 929 ms: 1.10x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 77.8 ms: 1.02x faster                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| nbody          | 87.0 ms                                                | 88.9 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.9 ms: 1.05x faster                                                           |
| regex_effbot   | 3.73 ms                                                | 3.61 ms: 1.03x faster                                                           |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                            |
| regex_dna      | 218 ms                                                 | 217 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process   | 60.6 ms                                                | 59.4 ms: 1.02x faster                                                           |
| tomli_loads         | 2.14 sec                                               | 2.10 sec: 1.02x faster                                                          |
| json_loads          | 27.2 us                                                | 26.8 us: 1.01x faster                                                           |
| xml_etree_generate  | 86.7 ms                                                | 85.5 ms: 1.01x faster                                                           |
| pickle_pure_python  | 310 us                                                 | 306 us: 1.01x faster                                                            |
| xml_etree_iterparse | 101 ms                                                 | 105 ms: 1.04x slower                                                            |
| json_dumps          | 10.6 ms                                                | 11.8 ms: 1.12x slower                                                           |
| Geometric mean      | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                           |
| python_startup_no_site | 6.96 ms                                                | 7.03 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 21.9 ms: 1.08x faster                                                           |
| django_template | 35.2 ms                                                | 33.8 ms: 1.04x faster                                                           |
| genshi_xml      | 50.9 ms                                                | 49.3 ms: 1.03x faster                                                           |
| mako            | 11.1 ms                                                | 11.5 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                  | 358 us                                                 | 262 us: 1.37x faster                                                            |
| create_gc_cycles          | 2.41 ms                                                | 1.79 ms: 1.35x faster                                                           |
| deepcopy_memo             | 39.1 us                                                | 30.7 us: 1.27x faster                                                           |
| go                        | 144 ms                                                 | 119 ms: 1.21x faster                                                            |
| deepcopy_reduce           | 3.20 us                                                | 2.66 us: 1.20x faster                                                           |
| python_startup            | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                           |
| async_tree_memoization_tg | 464 ms                                                 | 403 ms: 1.15x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 391 ms: 1.13x faster                                                            |
| gc_traversal              | 4.37 ms                                                | 3.92 ms: 1.11x faster                                                           |
| generators                | 29.0 ms                                                | 26.3 ms: 1.10x faster                                                           |
| async_tree_none           | 351 ms                                                 | 320 ms: 1.10x faster                                                            |
| pathlib                   | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                           |
| telco                     | 8.54 ms                                                | 7.93 ms: 1.08x faster                                                           |
| genshi_text               | 23.5 ms                                                | 21.9 ms: 1.08x faster                                                           |
| pycparser                 | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                          |
| 2to3                      | 267 ms                                                 | 252 ms: 1.06x faster                                                            |
| json                      | 5.36 ms                                                | 5.06 ms: 1.06x faster                                                           |
| mdp                       | 2.72 sec                                               | 2.57 sec: 1.06x faster                                                          |
| spectral_norm             | 115 ms                                                 | 109 ms: 1.06x faster                                                            |
| regex_v8                  | 26.2 ms                                                | 24.9 ms: 1.05x faster                                                           |
| thrift                    | 809 us                                                 | 774 us: 1.05x faster                                                            |
| richards                  | 48.7 ms                                                | 46.7 ms: 1.04x faster                                                           |
| django_template           | 35.2 ms                                                | 33.8 ms: 1.04x faster                                                           |
| html5lib                  | 64.2 ms                                                | 61.9 ms: 1.04x faster                                                           |
| richards_super            | 54.9 ms                                                | 52.9 ms: 1.04x faster                                                           |
| async_tree_none_tg        | 321 ms                                                 | 309 ms: 1.04x faster                                                            |
| regex_effbot              | 3.73 ms                                                | 3.61 ms: 1.03x faster                                                           |
| regex_compile             | 132 ms                                                 | 128 ms: 1.03x faster                                                            |
| genshi_xml                | 50.9 ms                                                | 49.3 ms: 1.03x faster                                                           |
| crypto_pyaes              | 75.3 ms                                                | 73.0 ms: 1.03x faster                                                           |
| tornado_http              | 92.4 ms                                                | 89.9 ms: 1.03x faster                                                           |
| sympy_str                 | 275 ms                                                 | 268 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 562 ms: 1.03x faster                                                            |
| sympy_expand              | 463 ms                                                 | 451 ms: 1.03x faster                                                            |
| sympy_sum                 | 150 ms                                                 | 147 ms: 1.03x faster                                                            |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.92 ms: 1.02x faster                                                           |
| xml_etree_process         | 60.6 ms                                                | 59.4 ms: 1.02x faster                                                           |
| raytrace                  | 267 ms                                                 | 262 ms: 1.02x faster                                                            |
| typing_runtime_protocols  | 165 us                                                 | 162 us: 1.02x faster                                                            |
| tomli_loads               | 2.14 sec                                               | 2.10 sec: 1.02x faster                                                          |
| logging_format            | 6.40 us                                                | 6.28 us: 1.02x faster                                                           |
| float                     | 79.2 ms                                                | 77.8 ms: 1.02x faster                                                           |
| sqlglot_normalize         | 108 ms                                                 | 106 ms: 1.02x faster                                                            |
| bpe_tokeniser             | 4.75 sec                                               | 4.67 sec: 1.02x faster                                                          |
| logging_simple            | 5.72 us                                                | 5.63 us: 1.02x faster                                                           |
| meteor_contest            | 109 ms                                                 | 107 ms: 1.02x faster                                                            |
| json_loads                | 27.2 us                                                | 26.8 us: 1.01x faster                                                           |
| fannkuch                  | 404 ms                                                 | 399 ms: 1.01x faster                                                            |
| xml_etree_generate        | 86.7 ms                                                | 85.5 ms: 1.01x faster                                                           |
| pickle_pure_python        | 310 us                                                 | 306 us: 1.01x faster                                                            |
| sqlglot_optimize          | 53.7 ms                                                | 53.1 ms: 1.01x faster                                                           |
| async_generators          | 436 ms                                                 | 431 ms: 1.01x faster                                                            |
| regex_dna                 | 218 ms                                                 | 217 ms: 1.01x faster                                                            |
| pprint_pformat            | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                          |
| pyflate                   | 471 ms                                                 | 468 ms: 1.01x faster                                                            |
| sympy_integrate           | 19.9 ms                                                | 19.8 ms: 1.01x faster                                                           |
| deltablue                 | 3.23 ms                                                | 3.21 ms: 1.00x faster                                                           |
| scimark_fft               | 364 ms                                                 | 363 ms: 1.00x faster                                                            |
| pidigits                  | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| comprehensions            | 16.5 us                                                | 16.6 us: 1.01x slower                                                           |
| dulwich_log               | 64.3 ms                                                | 64.8 ms: 1.01x slower                                                           |
| scimark_lu                | 113 ms                                                 | 114 ms: 1.01x slower                                                            |
| coverage                  | 84.0 ms                                                | 84.7 ms: 1.01x slower                                                           |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.01x slower                                                           |
| python_startup_no_site    | 6.96 ms                                                | 7.03 ms: 1.01x slower                                                           |
| asyncio_websockets        | 552 ms                                                 | 558 ms: 1.01x slower                                                            |
| scimark_monte_carlo       | 67.4 ms                                                | 68.3 ms: 1.01x slower                                                           |
| docutils                  | 2.59 sec                                               | 2.63 sec: 1.01x slower                                                          |
| logging_silent            | 102 ns                                                 | 103 ns: 1.01x slower                                                            |
| chaos                     | 58.1 ms                                                | 58.9 ms: 1.01x slower                                                           |
| hexiom                    | 6.16 ms                                                | 6.29 ms: 1.02x slower                                                           |
| nbody                     | 87.0 ms                                                | 88.9 ms: 1.02x slower                                                           |
| nqueens                   | 78.4 ms                                                | 80.2 ms: 1.02x slower                                                           |
| coroutines                | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                           |
| bench_thread_pool         | 822 us                                                 | 844 us: 1.03x slower                                                            |
| mako                      | 11.1 ms                                                | 11.5 ms: 1.03x slower                                                           |
| xml_etree_iterparse       | 101 ms                                                 | 105 ms: 1.04x slower                                                            |
| async_tree_io_tg          | 857 ms                                                 | 915 ms: 1.07x slower                                                            |
| async_tree_io             | 842 ms                                                 | 929 ms: 1.10x slower                                                            |
| json_dumps                | 10.6 ms                                                | 11.8 ms: 1.12x slower                                                           |
| bench_mp_pool             | 24.0 ms                                                | 56.0 ms: 2.33x slower                                                           |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (7): unpickle_pure_python, pprint_safe_repr, xml_etree_parse, async_tree_cpu_io_mixed_tg, sqlglot_transpile, scimark_sor, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.032x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x