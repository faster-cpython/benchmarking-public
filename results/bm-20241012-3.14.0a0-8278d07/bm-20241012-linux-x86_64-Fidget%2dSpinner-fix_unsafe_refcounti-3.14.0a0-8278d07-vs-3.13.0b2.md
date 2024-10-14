# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: linux-x86_64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 252 ms: 1.09x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.63 sec: 1.08x faster                                                          |
| html5lib       | 67.2 ms                                                    | 61.9 ms: 1.09x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 89.9 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 391 ms: 1.18x faster                                                            |
| async_tree_none            | 378 ms                                                     | 320 ms: 1.18x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 403 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 309 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 546 ms: 1.08x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                            |
| float          | 78.9 ms                                                    | 77.8 ms: 1.01x faster                                                           |
| nbody          | 88.3 ms                                                    | 88.9 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 128 ms: 1.07x faster                                                            |
| regex_dna      | 221 ms                                                     | 217 ms: 1.02x faster                                                            |
| regex_effbot   | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                                           |
| regex_v8       | 25.1 ms                                                    | 24.9 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                      | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.8 us: 1.08x faster                                                           |
| xml_etree_parse      | 162 ms                                                     | 155 ms: 1.04x faster                                                            |
| xml_etree_process    | 61.2 ms                                                    | 59.4 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                                            |
| xml_etree_generate   | 87.4 ms                                                    | 85.5 ms: 1.02x faster                                                           |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                                            |
| tomli_loads          | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                          |
| pickle_dict          | 34.8 us                                                    | 34.5 us: 1.01x faster                                                           |
| pickle               | 11.5 us                                                    | 11.4 us: 1.01x faster                                                           |
| pickle_list          | 5.11 us                                                    | 5.14 us: 1.01x slower                                                           |
| unpickle_list        | 5.34 us                                                    | 5.43 us: 1.02x slower                                                           |
| json_dumps           | 10.7 ms                                                    | 11.8 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.03 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 21.9 ms: 1.08x faster                                                           |
| genshi_xml      | 51.6 ms                                                    | 49.3 ms: 1.05x faster                                                           |
| django_template | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                           |
| mako            | 11.2 ms                                                    | 11.5 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 262 us: 1.40x faster                                                            |
| deepcopy_memo              | 39.7 us                                                    | 30.7 us: 1.29x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.66 us: 1.26x faster                                                           |
| go                         | 145 ms                                                     | 119 ms: 1.21x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 391 ms: 1.18x faster                                                            |
| async_tree_none            | 378 ms                                                     | 320 ms: 1.18x faster                                                            |
| generators                 | 29.6 ms                                                    | 26.3 ms: 1.13x faster                                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 403 ms: 1.10x faster                                                            |
| coverage                   | 93.1 ms                                                    | 84.7 ms: 1.10x faster                                                           |
| richards                   | 50.9 ms                                                    | 46.7 ms: 1.09x faster                                                           |
| 2to3                       | 274 ms                                                     | 252 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 309 ms: 1.09x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 61.9 ms: 1.09x faster                                                           |
| richards_super             | 57.4 ms                                                    | 52.9 ms: 1.08x faster                                                           |
| mdp                        | 2.79 sec                                                   | 2.57 sec: 1.08x faster                                                          |
| genshi_text                | 23.7 ms                                                    | 21.9 ms: 1.08x faster                                                           |
| scimark_fft                | 392 ms                                                     | 363 ms: 1.08x faster                                                            |
| json_loads                 | 28.9 us                                                    | 26.8 us: 1.08x faster                                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 546 ms: 1.08x faster                                                            |
| bpe_tokeniser              | 5.02 sec                                                   | 4.67 sec: 1.08x faster                                                          |
| docutils                   | 2.83 sec                                                   | 2.63 sec: 1.08x faster                                                          |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                           |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.92 ms: 1.07x faster                                                           |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.07x faster                                                            |
| regex_compile              | 137 ms                                                     | 128 ms: 1.07x faster                                                            |
| spectral_norm              | 116 ms                                                     | 109 ms: 1.07x faster                                                            |
| thrift                     | 823 us                                                     | 774 us: 1.06x faster                                                            |
| telco                      | 8.41 ms                                                    | 7.93 ms: 1.06x faster                                                           |
| sympy_sum                  | 156 ms                                                     | 147 ms: 1.06x faster                                                            |
| crypto_pyaes               | 77.5 ms                                                    | 73.0 ms: 1.06x faster                                                           |
| asyncio_tcp                | 508 ms                                                     | 480 ms: 1.06x faster                                                            |
| sympy_str                  | 282 ms                                                     | 268 ms: 1.06x faster                                                            |
| tornado_http               | 94.6 ms                                                    | 89.9 ms: 1.05x faster                                                           |
| json                       | 5.31 ms                                                    | 5.06 ms: 1.05x faster                                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                          |
| genshi_xml                 | 51.6 ms                                                    | 49.3 ms: 1.05x faster                                                           |
| sympy_expand               | 473 ms                                                     | 451 ms: 1.05x faster                                                            |
| sqlite_synth               | 2.99 us                                                    | 2.86 us: 1.05x faster                                                           |
| sqlglot_optimize           | 55.5 ms                                                    | 53.1 ms: 1.05x faster                                                           |
| pprint_safe_repr           | 758 ms                                                     | 727 ms: 1.04x faster                                                            |
| sqlglot_normalize          | 110 ms                                                     | 106 ms: 1.04x faster                                                            |
| chaos                      | 61.3 ms                                                    | 58.9 ms: 1.04x faster                                                           |
| xml_etree_parse            | 162 ms                                                     | 155 ms: 1.04x faster                                                            |
| dulwich_log                | 67.2 ms                                                    | 64.8 ms: 1.04x faster                                                           |
| sympy_integrate            | 20.5 ms                                                    | 19.8 ms: 1.04x faster                                                           |
| pyflate                    | 484 ms                                                     | 468 ms: 1.03x faster                                                            |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                          |
| logging_format             | 6.47 us                                                    | 6.28 us: 1.03x faster                                                           |
| django_template            | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                           |
| xml_etree_process          | 61.2 ms                                                    | 59.4 ms: 1.03x faster                                                           |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.03x faster                                                           |
| scimark_sor                | 127 ms                                                     | 124 ms: 1.03x faster                                                            |
| async_generators           | 442 ms                                                     | 431 ms: 1.03x faster                                                            |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.03x faster                                                          |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                                            |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                            |
| xml_etree_generate         | 87.4 ms                                                    | 85.5 ms: 1.02x faster                                                           |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                            |
| logging_simple             | 5.74 us                                                    | 5.63 us: 1.02x faster                                                           |
| regex_dna                  | 221 ms                                                     | 217 ms: 1.02x faster                                                            |
| typing_runtime_protocols   | 165 us                                                     | 162 us: 1.02x faster                                                            |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| raytrace                   | 267 ms                                                     | 262 ms: 1.02x faster                                                            |
| regex_effbot               | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                                           |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                            |
| logging_silent             | 105 ns                                                     | 103 ns: 1.02x faster                                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.79 ms: 1.02x faster                                                           |
| nqueens                    | 81.4 ms                                                    | 80.2 ms: 1.01x faster                                                           |
| gc_traversal               | 3.98 ms                                                    | 3.92 ms: 1.01x faster                                                           |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                                            |
| float                      | 78.9 ms                                                    | 77.8 ms: 1.01x faster                                                           |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.3 ms: 1.01x faster                                                           |
| deltablue                  | 3.25 ms                                                    | 3.21 ms: 1.01x faster                                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.03 ms: 1.01x faster                                                           |
| tomli_loads                | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                          |
| regex_v8                   | 25.1 ms                                                    | 24.9 ms: 1.01x faster                                                           |
| fannkuch                   | 402 ms                                                     | 399 ms: 1.01x faster                                                            |
| pickle_dict                | 34.8 us                                                    | 34.5 us: 1.01x faster                                                           |
| pickle                     | 11.5 us                                                    | 11.4 us: 1.01x faster                                                           |
| pickle_list                | 5.11 us                                                    | 5.14 us: 1.01x slower                                                           |
| nbody                      | 88.3 ms                                                    | 88.9 ms: 1.01x slower                                                           |
| bench_thread_pool          | 834 us                                                     | 844 us: 1.01x slower                                                            |
| unpickle_list              | 5.34 us                                                    | 5.43 us: 1.02x slower                                                           |
| mako                       | 11.2 ms                                                    | 11.5 ms: 1.02x slower                                                           |
| json_dumps                 | 10.7 ms                                                    | 11.8 ms: 1.10x slower                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 56.0 ms: 2.35x slower                                                           |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                                    |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_io, comprehensions, hexiom, pylint, coroutines, pickle_pure_python, unpickle
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.00x