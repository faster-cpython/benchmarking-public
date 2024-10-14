# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: linux-x86_64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 280 ms: 1.04x faster                                                                  |
| docutils       | 2.98 sec                                                         | 2.90 sec: 1.03x faster                                                                |
| html5lib       | 74.7 ms                                                          | 70.1 ms: 1.06x faster                                                                 |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 783 ms: 1.15x faster                                                                  |
| async_tree_memoization     | 460 ms                                                           | 403 ms: 1.14x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 321 ms: 1.14x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                           | 309 ms: 1.10x faster                                                                  |
| async_tree_io              | 873 ms                                                           | 803 ms: 1.09x faster                                                                  |
| async_tree_memoization_tg  | 421 ms                                                           | 393 ms: 1.07x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 550 ms: 1.04x faster                                                                  |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 252 ms: 1.00x faster                                                                  |
| float          | 80.2 ms                                                          | 80.6 ms: 1.00x slower                                                                 |
| nbody          | 87.8 ms                                                          | 89.8 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 24.9 ms: 1.04x faster                                                                 |
| regex_compile  | 144 ms                                                           | 140 ms: 1.03x faster                                                                  |
| regex_dna      | 249 ms                                                           | 242 ms: 1.03x faster                                                                  |
| regex_effbot   | 3.40 ms                                                          | 3.46 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 30.4 us: 1.08x faster                                                                 |
| unpickle_pure_python | 224 us                                                           | 215 us: 1.05x faster                                                                  |
| xml_etree_iterparse  | 103 ms                                                           | 101 ms: 1.01x faster                                                                  |
| xml_etree_generate   | 85.7 ms                                                          | 84.9 ms: 1.01x faster                                                                 |
| json_loads           | 25.0 us                                                          | 24.9 us: 1.00x faster                                                                 |
| pickle               | 10.6 us                                                          | 10.6 us: 1.00x faster                                                                 |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                                                  |
| pickle_list          | 4.44 us                                                          | 4.57 us: 1.03x slower                                                                 |
| pickle_pure_python   | 307 us                                                           | 317 us: 1.03x slower                                                                  |
| tomli_loads          | 2.40 sec                                                         | 2.50 sec: 1.04x slower                                                                |
| json_dumps           | 10.8 ms                                                          | 12.1 ms: 1.12x slower                                                                 |
| Geometric mean       | (ref)                                                            | 1.01x slower                                                                          |

Benchmark hidden because not significant (3): unpickle_list, unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                                 |
| python_startup_no_site | 8.85 ms                                                          | 8.96 ms: 1.01x slower                                                                 |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 53.1 ms: 1.09x faster                                                                 |
| genshi_text     | 25.9 ms                                                          | 24.6 ms: 1.05x faster                                                                 |
| mako            | 10.4 ms                                                          | 10.8 ms: 1.04x slower                                                                 |
| django_template | 39.0 ms                                                          | 42.7 ms: 1.09x slower                                                                 |
| Geometric mean  | (ref)                                                            | 1.00x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 287 us: 1.31x faster                                                                  |
| deepcopy_memo              | 37.3 us                                                          | 29.6 us: 1.26x faster                                                                 |
| go                         | 165 ms                                                           | 137 ms: 1.21x faster                                                                  |
| async_tree_io_tg           | 900 ms                                                           | 783 ms: 1.15x faster                                                                  |
| generators                 | 33.5 ms                                                          | 29.3 ms: 1.14x faster                                                                 |
| deepcopy_reduce            | 3.39 us                                                          | 2.96 us: 1.14x faster                                                                 |
| async_tree_memoization     | 460 ms                                                           | 403 ms: 1.14x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 321 ms: 1.14x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                           | 309 ms: 1.10x faster                                                                  |
| scimark_sor                | 119 ms                                                           | 108 ms: 1.10x faster                                                                  |
| genshi_xml                 | 58.1 ms                                                          | 53.1 ms: 1.09x faster                                                                 |
| richards_super             | 61.2 ms                                                          | 56.2 ms: 1.09x faster                                                                 |
| async_tree_io              | 873 ms                                                           | 803 ms: 1.09x faster                                                                  |
| pathlib                    | 17.1 ms                                                          | 15.8 ms: 1.09x faster                                                                 |
| richards                   | 53.4 ms                                                          | 49.3 ms: 1.08x faster                                                                 |
| pickle_dict                | 32.8 us                                                          | 30.4 us: 1.08x faster                                                                 |
| async_tree_memoization_tg  | 421 ms                                                           | 393 ms: 1.07x faster                                                                  |
| bpe_tokeniser              | 5.14 sec                                                         | 4.80 sec: 1.07x faster                                                                |
| telco                      | 8.40 ms                                                          | 7.88 ms: 1.07x faster                                                                 |
| html5lib                   | 74.7 ms                                                          | 70.1 ms: 1.06x faster                                                                 |
| coverage                   | 83.5 ms                                                          | 78.9 ms: 1.06x faster                                                                 |
| genshi_text                | 25.9 ms                                                          | 24.6 ms: 1.05x faster                                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                                  |
| scimark_fft                | 312 ms                                                           | 298 ms: 1.05x faster                                                                  |
| unpickle_pure_python       | 224 us                                                           | 215 us: 1.05x faster                                                                  |
| meteor_contest             | 128 ms                                                           | 123 ms: 1.04x faster                                                                  |
| regex_v8                   | 26.0 ms                                                          | 24.9 ms: 1.04x faster                                                                 |
| pprint_safe_repr           | 818 ms                                                           | 784 ms: 1.04x faster                                                                  |
| 2to3                       | 291 ms                                                           | 280 ms: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 550 ms: 1.04x faster                                                                  |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.13 ms: 1.04x faster                                                                 |
| scimark_lu                 | 97.5 ms                                                          | 94.3 ms: 1.03x faster                                                                 |
| regex_compile              | 144 ms                                                           | 140 ms: 1.03x faster                                                                  |
| regex_dna                  | 249 ms                                                           | 242 ms: 1.03x faster                                                                  |
| docutils                   | 2.98 sec                                                         | 2.90 sec: 1.03x faster                                                                |
| sympy_sum                  | 155 ms                                                           | 151 ms: 1.03x faster                                                                  |
| pprint_pformat             | 1.66 sec                                                         | 1.61 sec: 1.03x faster                                                                |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                                  |
| bench_thread_pool          | 908 us                                                           | 888 us: 1.02x faster                                                                  |
| coroutines                 | 22.0 ms                                                          | 21.5 ms: 1.02x faster                                                                 |
| dulwich_log                | 67.3 ms                                                          | 65.9 ms: 1.02x faster                                                                 |
| sqlite_synth               | 2.80 us                                                          | 2.74 us: 1.02x faster                                                                 |
| asyncio_tcp                | 378 ms                                                           | 371 ms: 1.02x faster                                                                  |
| sympy_str                  | 295 ms                                                           | 290 ms: 1.02x faster                                                                  |
| hexiom                     | 6.35 ms                                                          | 6.26 ms: 1.01x faster                                                                 |
| asyncio_websockets         | 395 ms                                                           | 390 ms: 1.01x faster                                                                  |
| sympy_expand               | 501 ms                                                           | 495 ms: 1.01x faster                                                                  |
| xml_etree_iterparse        | 103 ms                                                           | 101 ms: 1.01x faster                                                                  |
| xml_etree_generate         | 85.7 ms                                                          | 84.9 ms: 1.01x faster                                                                 |
| spectral_norm              | 97.3 ms                                                          | 96.5 ms: 1.01x faster                                                                 |
| pycparser                  | 1.22 sec                                                         | 1.21 sec: 1.01x faster                                                                |
| sqlglot_normalize          | 120 ms                                                           | 119 ms: 1.01x faster                                                                  |
| crypto_pyaes               | 73.6 ms                                                          | 73.1 ms: 1.01x faster                                                                 |
| pidigits                   | 254 ms                                                           | 252 ms: 1.00x faster                                                                  |
| json_loads                 | 25.0 us                                                          | 24.9 us: 1.00x faster                                                                 |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.57 sec: 1.00x faster                                                                |
| pickle                     | 10.6 us                                                          | 10.6 us: 1.00x faster                                                                 |
| mdp                        | 2.46 sec                                                         | 2.47 sec: 1.00x slower                                                                |
| float                      | 80.2 ms                                                          | 80.6 ms: 1.00x slower                                                                 |
| deltablue                  | 3.37 ms                                                          | 3.39 ms: 1.01x slower                                                                 |
| json                       | 5.35 ms                                                          | 5.39 ms: 1.01x slower                                                                 |
| sympy_integrate            | 23.2 ms                                                          | 23.4 ms: 1.01x slower                                                                 |
| xml_etree_parse            | 144 ms                                                           | 145 ms: 1.01x slower                                                                  |
| sqlglot_transpile          | 1.76 ms                                                          | 1.78 ms: 1.01x slower                                                                 |
| gc_traversal               | 4.69 ms                                                          | 4.74 ms: 1.01x slower                                                                 |
| comprehensions             | 17.0 us                                                          | 17.1 us: 1.01x slower                                                                 |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                                 |
| python_startup_no_site     | 8.85 ms                                                          | 8.96 ms: 1.01x slower                                                                 |
| scimark_monte_carlo        | 65.5 ms                                                          | 66.4 ms: 1.01x slower                                                                 |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.01x slower                                                                 |
| regex_effbot               | 3.40 ms                                                          | 3.46 ms: 1.02x slower                                                                 |
| nqueens                    | 88.4 ms                                                          | 90.0 ms: 1.02x slower                                                                 |
| logging_simple             | 6.40 us                                                          | 6.52 us: 1.02x slower                                                                 |
| logging_silent             | 96.3 ns                                                          | 98.2 ns: 1.02x slower                                                                 |
| async_generators           | 363 ms                                                           | 371 ms: 1.02x slower                                                                  |
| nbody                      | 87.8 ms                                                          | 89.8 ms: 1.02x slower                                                                 |
| raytrace                   | 260 ms                                                           | 267 ms: 1.03x slower                                                                  |
| create_gc_cycles           | 2.00 ms                                                          | 2.06 ms: 1.03x slower                                                                 |
| typing_runtime_protocols   | 171 us                                                           | 175 us: 1.03x slower                                                                  |
| pickle_list                | 4.44 us                                                          | 4.57 us: 1.03x slower                                                                 |
| pickle_pure_python         | 307 us                                                           | 317 us: 1.03x slower                                                                  |
| tomli_loads                | 2.40 sec                                                         | 2.50 sec: 1.04x slower                                                                |
| mako                       | 10.4 ms                                                          | 10.8 ms: 1.04x slower                                                                 |
| chaos                      | 59.6 ms                                                          | 63.5 ms: 1.07x slower                                                                 |
| django_template            | 39.0 ms                                                          | 42.7 ms: 1.09x slower                                                                 |
| json_dumps                 | 10.8 ms                                                          | 12.1 ms: 1.12x slower                                                                 |
| bench_mp_pool              | 4.91 ms                                                          | 2.45 sec: 500.00x slower                                                              |
| Geometric mean             | (ref)                                                            | 1.04x slower                                                                          |

Benchmark hidden because not significant (9): logging_format, thrift, unpickle_list, sqlglot_optimize, unpickle, fannkuch, xml_etree_process, pyflate, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x