# Results vs. 3.13.0

- fork: faster-cpython
- ref: more_robust_immortal
- machine: linux-x86_64
- commit hash: 9f86e46
- commit date: 2024-10-10
- overall geometric mean: 1.027x faster
- HPT reliability: 97.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 254 ms: 1.05x faster                                                            |
| docutils       | 2.59 sec                                               | 2.62 sec: 1.01x slower                                                          |
| html5lib       | 64.2 ms                                                | 61.7 ms: 1.04x faster                                                           |
| tornado_http   | 92.4 ms                                                | 90.4 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 404 ms: 1.15x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 396 ms: 1.12x faster                                                            |
| async_tree_none           | 351 ms                                                 | 325 ms: 1.08x faster                                                            |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 559 ms: 1.03x faster                                                            |
| async_tree_none_tg        | 321 ms                                                 | 312 ms: 1.03x faster                                                            |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                            |
| coroutines                | 22.7 ms                                                | 23.8 ms: 1.05x slower                                                           |
| async_tree_io_tg          | 857 ms                                                 | 919 ms: 1.07x slower                                                            |
| async_tree_io             | 842 ms                                                 | 937 ms: 1.11x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 78.8 ms: 1.01x faster                                                           |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| nbody          | 87.0 ms                                                | 92.7 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                           |
| regex_effbot   | 3.73 ms                                                | 3.62 ms: 1.03x faster                                                           |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                            |
| regex_dna      | 218 ms                                                 | 222 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 27.2 us                                                | 26.3 us: 1.04x faster                                                           |
| tomli_loads          | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                          |
| xml_etree_process    | 60.6 ms                                                | 59.6 ms: 1.02x faster                                                           |
| pickle_pure_python   | 310 us                                                 | 309 us: 1.00x faster                                                            |
| unpickle_pure_python | 216 us                                                 | 220 us: 1.02x slower                                                            |
| xml_etree_iterparse  | 101 ms                                                 | 105 ms: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                           |
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.9 ms                                                | 49.1 ms: 1.04x faster                                                           |
| genshi_text     | 23.5 ms                                                | 22.8 ms: 1.03x faster                                                           |
| django_template | 35.2 ms                                                | 34.2 ms: 1.03x faster                                                           |
| mako            | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                  | 358 us                                                 | 260 us: 1.38x faster                                                            |
| create_gc_cycles          | 2.41 ms                                                | 1.78 ms: 1.35x faster                                                           |
| deepcopy_memo             | 39.1 us                                                | 31.3 us: 1.25x faster                                                           |
| deepcopy_reduce           | 3.20 us                                                | 2.66 us: 1.20x faster                                                           |
| go                        | 144 ms                                                 | 121 ms: 1.18x faster                                                            |
| python_startup            | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                           |
| async_tree_memoization_tg | 464 ms                                                 | 404 ms: 1.15x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 396 ms: 1.12x faster                                                            |
| pathlib                   | 17.5 ms                                                | 16.0 ms: 1.10x faster                                                           |
| gc_traversal              | 4.37 ms                                                | 3.99 ms: 1.10x faster                                                           |
| json                      | 5.36 ms                                                | 4.93 ms: 1.09x faster                                                           |
| mdp                       | 2.72 sec                                               | 2.51 sec: 1.08x faster                                                          |
| async_tree_none           | 351 ms                                                 | 325 ms: 1.08x faster                                                            |
| regex_v8                  | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                           |
| generators                | 29.0 ms                                                | 26.9 ms: 1.08x faster                                                           |
| telco                     | 8.54 ms                                                | 8.01 ms: 1.07x faster                                                           |
| 2to3                      | 267 ms                                                 | 254 ms: 1.05x faster                                                            |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.80 ms: 1.05x faster                                                           |
| richards                  | 48.7 ms                                                | 46.8 ms: 1.04x faster                                                           |
| html5lib                  | 64.2 ms                                                | 61.7 ms: 1.04x faster                                                           |
| thrift                    | 809 us                                                 | 780 us: 1.04x faster                                                            |
| genshi_xml                | 50.9 ms                                                | 49.1 ms: 1.04x faster                                                           |
| richards_super            | 54.9 ms                                                | 52.9 ms: 1.04x faster                                                           |
| typing_runtime_protocols  | 165 us                                                 | 159 us: 1.04x faster                                                            |
| logging_format            | 6.40 us                                                | 6.18 us: 1.04x faster                                                           |
| json_loads                | 27.2 us                                                | 26.3 us: 1.04x faster                                                           |
| genshi_text               | 23.5 ms                                                | 22.8 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 559 ms: 1.03x faster                                                            |
| regex_effbot              | 3.73 ms                                                | 3.62 ms: 1.03x faster                                                           |
| pyflate                   | 471 ms                                                 | 457 ms: 1.03x faster                                                            |
| crypto_pyaes              | 75.3 ms                                                | 73.3 ms: 1.03x faster                                                           |
| async_tree_none_tg        | 321 ms                                                 | 312 ms: 1.03x faster                                                            |
| pycparser                 | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                          |
| tomli_loads               | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                          |
| django_template           | 35.2 ms                                                | 34.2 ms: 1.03x faster                                                           |
| regex_compile             | 132 ms                                                 | 129 ms: 1.03x faster                                                            |
| sympy_str                 | 275 ms                                                 | 268 ms: 1.02x faster                                                            |
| tornado_http              | 92.4 ms                                                | 90.4 ms: 1.02x faster                                                           |
| logging_simple            | 5.72 us                                                | 5.60 us: 1.02x faster                                                           |
| meteor_contest            | 109 ms                                                 | 107 ms: 1.02x faster                                                            |
| xml_etree_process         | 60.6 ms                                                | 59.6 ms: 1.02x faster                                                           |
| sympy_sum                 | 150 ms                                                 | 148 ms: 1.02x faster                                                            |
| sympy_expand              | 463 ms                                                 | 458 ms: 1.01x faster                                                            |
| bpe_tokeniser             | 4.75 sec                                               | 4.70 sec: 1.01x faster                                                          |
| sqlglot_normalize         | 108 ms                                                 | 107 ms: 1.01x faster                                                            |
| float                     | 79.2 ms                                                | 78.8 ms: 1.01x faster                                                           |
| pprint_safe_repr          | 728 ms                                                 | 725 ms: 1.00x faster                                                            |
| sqlglot_optimize          | 53.7 ms                                                | 53.6 ms: 1.00x faster                                                           |
| pickle_pure_python        | 310 us                                                 | 309 us: 1.00x faster                                                            |
| spectral_norm             | 115 ms                                                 | 116 ms: 1.00x slower                                                            |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                            |
| pidigits                  | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| raytrace                  | 267 ms                                                 | 269 ms: 1.01x slower                                                            |
| sqlglot_transpile         | 1.58 ms                                                | 1.60 ms: 1.01x slower                                                           |
| docutils                  | 2.59 sec                                               | 2.62 sec: 1.01x slower                                                          |
| python_startup_no_site    | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                           |
| scimark_monte_carlo       | 67.4 ms                                                | 68.5 ms: 1.02x slower                                                           |
| regex_dna                 | 218 ms                                                 | 222 ms: 1.02x slower                                                            |
| scimark_sor               | 124 ms                                                 | 126 ms: 1.02x slower                                                            |
| hexiom                    | 6.16 ms                                                | 6.29 ms: 1.02x slower                                                           |
| unpickle_pure_python      | 216 us                                                 | 220 us: 1.02x slower                                                            |
| comprehensions            | 16.5 us                                                | 16.9 us: 1.02x slower                                                           |
| sqlglot_parse             | 1.27 ms                                                | 1.30 ms: 1.02x slower                                                           |
| scimark_fft               | 364 ms                                                 | 373 ms: 1.02x slower                                                            |
| deltablue                 | 3.23 ms                                                | 3.32 ms: 1.03x slower                                                           |
| scimark_lu                | 113 ms                                                 | 116 ms: 1.03x slower                                                            |
| nqueens                   | 78.4 ms                                                | 80.7 ms: 1.03x slower                                                           |
| bench_thread_pool         | 822 us                                                 | 849 us: 1.03x slower                                                            |
| xml_etree_iterparse       | 101 ms                                                 | 105 ms: 1.03x slower                                                            |
| chaos                     | 58.1 ms                                                | 60.2 ms: 1.04x slower                                                           |
| mako                      | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                           |
| coroutines                | 22.7 ms                                                | 23.8 ms: 1.05x slower                                                           |
| logging_silent            | 102 ns                                                 | 108 ns: 1.06x slower                                                            |
| nbody                     | 87.0 ms                                                | 92.7 ms: 1.07x slower                                                           |
| async_tree_io_tg          | 857 ms                                                 | 919 ms: 1.07x slower                                                            |
| async_tree_io             | 842 ms                                                 | 937 ms: 1.11x slower                                                            |
| bench_mp_pool             | 24.0 ms                                                | 56.3 ms: 2.35x slower                                                           |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed_tg, xml_etree_parse, fannkuch, sympy_integrate, dulwich_log, json_dumps, coverage, pprint_pformat, async_generators, xml_etree_generate, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241010-3.14.0a0-9f86e46/bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.027x faster
# HPT report

- Reliability score: 97.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x