# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: more_robust_immortal
- machine: linux-x86_64
- commit hash: 94f8fd0
- commit date: 2024-10-10
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 280 ms: 1.04x faster                                                                  |
| docutils       | 2.98 sec                                                         | 2.87 sec: 1.04x faster                                                                |
| html5lib       | 74.7 ms                                                          | 70.7 ms: 1.06x faster                                                                 |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 400 ms: 1.15x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 320 ms: 1.14x faster                                                                  |
| async_tree_io_tg           | 900 ms                                                           | 795 ms: 1.13x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                           | 310 ms: 1.10x faster                                                                  |
| async_tree_memoization_tg  | 421 ms                                                           | 391 ms: 1.08x faster                                                                  |
| async_tree_io              | 873 ms                                                           | 812 ms: 1.08x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 571 ms: 1.06x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 549 ms: 1.04x faster                                                                  |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 79.7 ms: 1.01x faster                                                                 |
| pidigits       | 254 ms                                                           | 252 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 137 ms: 1.05x faster                                                                  |
| regex_dna      | 249 ms                                                           | 247 ms: 1.01x faster                                                                  |
| regex_v8       | 26.0 ms                                                          | 26.2 ms: 1.01x slower                                                                 |
| regex_effbot   | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_loads           | 25.0 us                                                          | 23.4 us: 1.07x faster                                                                 |
| unpickle_pure_python | 224 us                                                           | 213 us: 1.05x faster                                                                  |
| unpickle             | 15.7 us                                                          | 15.1 us: 1.04x faster                                                                 |
| xml_etree_iterparse  | 103 ms                                                           | 100 ms: 1.02x faster                                                                  |
| pickle               | 10.6 us                                                          | 10.4 us: 1.02x faster                                                                 |
| xml_etree_parse      | 144 ms                                                           | 142 ms: 1.01x faster                                                                  |
| xml_etree_generate   | 85.7 ms                                                          | 84.7 ms: 1.01x faster                                                                 |
| pickle_pure_python   | 307 us                                                           | 312 us: 1.02x slower                                                                  |
| pickle_dict          | 32.8 us                                                          | 33.9 us: 1.03x slower                                                                 |
| json_dumps           | 10.8 ms                                                          | 11.1 ms: 1.03x slower                                                                 |
| tomli_loads          | 2.40 sec                                                         | 2.52 sec: 1.05x slower                                                                |
| pickle_list          | 4.44 us                                                          | 4.81 us: 1.08x slower                                                                 |
| Geometric mean       | (ref)                                                            | 1.00x faster                                                                          |

Benchmark hidden because not significant (2): xml_etree_process, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                                 |
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                                 |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 52.3 ms: 1.11x faster                                                                 |
| genshi_text     | 25.9 ms                                                          | 24.2 ms: 1.07x faster                                                                 |
| mako            | 10.4 ms                                                          | 10.6 ms: 1.02x slower                                                                 |
| django_template | 39.0 ms                                                          | 41.8 ms: 1.07x slower                                                                 |
| Geometric mean  | (ref)                                                            | 1.02x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 284 us: 1.33x faster                                                                  |
| deepcopy_memo              | 37.3 us                                                          | 28.9 us: 1.29x faster                                                                 |
| go                         | 165 ms                                                           | 133 ms: 1.24x faster                                                                  |
| generators                 | 33.5 ms                                                          | 28.0 ms: 1.20x faster                                                                 |
| deepcopy_reduce            | 3.39 us                                                          | 2.90 us: 1.17x faster                                                                 |
| async_tree_memoization     | 460 ms                                                           | 400 ms: 1.15x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 320 ms: 1.14x faster                                                                  |
| async_tree_io_tg           | 900 ms                                                           | 795 ms: 1.13x faster                                                                  |
| genshi_xml                 | 58.1 ms                                                          | 52.3 ms: 1.11x faster                                                                 |
| async_tree_none_tg         | 340 ms                                                           | 310 ms: 1.10x faster                                                                  |
| scimark_sor                | 119 ms                                                           | 108 ms: 1.10x faster                                                                  |
| bpe_tokeniser              | 5.14 sec                                                         | 4.74 sec: 1.08x faster                                                                |
| pathlib                    | 17.1 ms                                                          | 15.9 ms: 1.08x faster                                                                 |
| richards_super             | 61.2 ms                                                          | 56.8 ms: 1.08x faster                                                                 |
| async_tree_memoization_tg  | 421 ms                                                           | 391 ms: 1.08x faster                                                                  |
| async_tree_io              | 873 ms                                                           | 812 ms: 1.08x faster                                                                  |
| genshi_text                | 25.9 ms                                                          | 24.2 ms: 1.07x faster                                                                 |
| json_loads                 | 25.0 us                                                          | 23.4 us: 1.07x faster                                                                 |
| telco                      | 8.40 ms                                                          | 7.87 ms: 1.07x faster                                                                 |
| scimark_fft                | 312 ms                                                           | 294 ms: 1.06x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 571 ms: 1.06x faster                                                                  |
| html5lib                   | 74.7 ms                                                          | 70.7 ms: 1.06x faster                                                                 |
| unpickle_pure_python       | 224 us                                                           | 213 us: 1.05x faster                                                                  |
| richards                   | 53.4 ms                                                          | 50.8 ms: 1.05x faster                                                                 |
| json                       | 5.35 ms                                                          | 5.10 ms: 1.05x faster                                                                 |
| regex_compile              | 144 ms                                                           | 137 ms: 1.05x faster                                                                  |
| coroutines                 | 22.0 ms                                                          | 21.0 ms: 1.05x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 549 ms: 1.04x faster                                                                  |
| 2to3                       | 291 ms                                                           | 280 ms: 1.04x faster                                                                  |
| unpickle                   | 15.7 us                                                          | 15.1 us: 1.04x faster                                                                 |
| docutils                   | 2.98 sec                                                         | 2.87 sec: 1.04x faster                                                                |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.14 ms: 1.03x faster                                                                 |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                                  |
| pprint_safe_repr           | 818 ms                                                           | 792 ms: 1.03x faster                                                                  |
| bench_thread_pool          | 908 us                                                           | 881 us: 1.03x faster                                                                  |
| pprint_pformat             | 1.66 sec                                                         | 1.61 sec: 1.03x faster                                                                |
| scimark_lu                 | 97.5 ms                                                          | 94.8 ms: 1.03x faster                                                                 |
| dulwich_log                | 67.3 ms                                                          | 65.5 ms: 1.03x faster                                                                 |
| hexiom                     | 6.35 ms                                                          | 6.20 ms: 1.03x faster                                                                 |
| sympy_sum                  | 155 ms                                                           | 151 ms: 1.02x faster                                                                  |
| xml_etree_iterparse        | 103 ms                                                           | 100 ms: 1.02x faster                                                                  |
| pickle                     | 10.6 us                                                          | 10.4 us: 1.02x faster                                                                 |
| sqlite_synth               | 2.80 us                                                          | 2.74 us: 1.02x faster                                                                 |
| asyncio_tcp                | 378 ms                                                           | 370 ms: 1.02x faster                                                                  |
| spectral_norm              | 97.3 ms                                                          | 95.3 ms: 1.02x faster                                                                 |
| coverage                   | 83.5 ms                                                          | 81.9 ms: 1.02x faster                                                                 |
| sympy_str                  | 295 ms                                                           | 289 ms: 1.02x faster                                                                  |
| meteor_contest             | 128 ms                                                           | 126 ms: 1.02x faster                                                                  |
| scimark_monte_carlo        | 65.5 ms                                                          | 64.4 ms: 1.02x faster                                                                 |
| nqueens                    | 88.4 ms                                                          | 87.2 ms: 1.01x faster                                                                 |
| async_generators           | 363 ms                                                           | 358 ms: 1.01x faster                                                                  |
| xml_etree_parse            | 144 ms                                                           | 142 ms: 1.01x faster                                                                  |
| xml_etree_generate         | 85.7 ms                                                          | 84.7 ms: 1.01x faster                                                                 |
| sqlglot_normalize          | 120 ms                                                           | 119 ms: 1.01x faster                                                                  |
| crypto_pyaes               | 73.6 ms                                                          | 72.9 ms: 1.01x faster                                                                 |
| regex_dna                  | 249 ms                                                           | 247 ms: 1.01x faster                                                                  |
| asyncio_websockets         | 395 ms                                                           | 392 ms: 1.01x faster                                                                  |
| sympy_expand               | 501 ms                                                           | 497 ms: 1.01x faster                                                                  |
| float                      | 80.2 ms                                                          | 79.7 ms: 1.01x faster                                                                 |
| pidigits                   | 254 ms                                                           | 252 ms: 1.01x faster                                                                  |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.57 sec: 1.00x faster                                                                |
| mdp                        | 2.46 sec                                                         | 2.48 sec: 1.01x slower                                                                |
| regex_v8                   | 26.0 ms                                                          | 26.2 ms: 1.01x slower                                                                 |
| gc_traversal               | 4.69 ms                                                          | 4.74 ms: 1.01x slower                                                                 |
| python_startup_no_site     | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                                 |
| typing_runtime_protocols   | 171 us                                                           | 173 us: 1.01x slower                                                                  |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                                 |
| logging_simple             | 6.40 us                                                          | 6.50 us: 1.01x slower                                                                 |
| fannkuch                   | 353 ms                                                           | 358 ms: 1.02x slower                                                                  |
| pickle_pure_python         | 307 us                                                           | 312 us: 1.02x slower                                                                  |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.02x slower                                                                 |
| sqlglot_transpile          | 1.76 ms                                                          | 1.79 ms: 1.02x slower                                                                 |
| logging_silent             | 96.3 ns                                                          | 98.0 ns: 1.02x slower                                                                 |
| raytrace                   | 260 ms                                                           | 266 ms: 1.02x slower                                                                  |
| mako                       | 10.4 ms                                                          | 10.6 ms: 1.02x slower                                                                 |
| pickle_dict                | 32.8 us                                                          | 33.9 us: 1.03x slower                                                                 |
| json_dumps                 | 10.8 ms                                                          | 11.1 ms: 1.03x slower                                                                 |
| chaos                      | 59.6 ms                                                          | 61.9 ms: 1.04x slower                                                                 |
| tomli_loads                | 2.40 sec                                                         | 2.52 sec: 1.05x slower                                                                |
| regex_effbot               | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                                                 |
| django_template            | 39.0 ms                                                          | 41.8 ms: 1.07x slower                                                                 |
| pickle_list                | 4.44 us                                                          | 4.81 us: 1.08x slower                                                                 |
| bench_mp_pool              | 4.91 ms                                                          | 1.92 sec: 391.51x slower                                                              |
| Geometric mean             | (ref)                                                            | 1.03x slower                                                                          |

Benchmark hidden because not significant (13): deltablue, pycparser, logging_format, thrift, xml_etree_process, comprehensions, pyflate, sqlglot_optimize, sympy_integrate, unpickle_list, create_gc_cycles, nbody, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241010-3.14.0a0-94f8fd0/bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.00x