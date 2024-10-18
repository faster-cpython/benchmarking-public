# Results vs. 3.13.0b2

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.04x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 282 ms: 1.03x faster                                             |
| docutils       | 2.98 sec                                                         | 2.90 sec: 1.03x faster                                           |
| html5lib       | 74.7 ms                                                          | 71.1 ms: 1.05x faster                                            |
| tornado_http   | 119 ms                                                           | 117 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                            | 1.03x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|---------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization    | 460 ms                                                           | 415 ms: 1.11x faster                                             |
| async_tree_none           | 365 ms                                                           | 332 ms: 1.10x faster                                             |
| async_tree_memoization_tg | 421 ms                                                           | 386 ms: 1.09x faster                                             |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 558 ms: 1.08x faster                                             |
| async_tree_io_tg          | 900 ms                                                           | 837 ms: 1.07x faster                                             |
| async_tree_io             | 873 ms                                                           | 827 ms: 1.06x faster                                             |
| async_tree_none_tg        | 340 ms                                                           | 323 ms: 1.05x faster                                             |
| Geometric mean            | (ref)                                                            | 1.07x faster                                                     |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 252 ms: 1.01x faster                                             |
| float          | 80.2 ms                                                          | 82.2 ms: 1.02x slower                                            |
| nbody          | 87.8 ms                                                          | 90.1 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                            | 1.01x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 24.7 ms: 1.05x faster                                            |
| regex_compile  | 144 ms                                                           | 139 ms: 1.04x faster                                             |
| regex_dna      | 249 ms                                                           | 243 ms: 1.03x faster                                             |
| regex_effbot   | 3.40 ms                                                          | 3.43 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                            | 1.03x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 31.0 us: 1.06x faster                                            |
| unpickle_pure_python | 224 us                                                           | 214 us: 1.05x faster                                             |
| pickle_list          | 4.44 us                                                          | 4.31 us: 1.03x faster                                            |
| unpickle             | 15.7 us                                                          | 15.2 us: 1.03x faster                                            |
| unpickle_list        | 4.70 us                                                          | 4.58 us: 1.03x faster                                            |
| pickle               | 10.6 us                                                          | 10.5 us: 1.01x faster                                            |
| xml_etree_iterparse  | 103 ms                                                           | 102 ms: 1.01x faster                                             |
| xml_etree_generate   | 85.7 ms                                                          | 85.2 ms: 1.01x faster                                            |
| json_loads           | 25.0 us                                                          | 25.3 us: 1.01x slower                                            |
| tomli_loads          | 2.40 sec                                                         | 2.50 sec: 1.04x slower                                           |
| pickle_pure_python   | 307 us                                                           | 320 us: 1.04x slower                                             |
| json_dumps           | 10.8 ms                                                          | 11.4 ms: 1.06x slower                                            |
| Geometric mean       | (ref)                                                            | 1.00x faster                                                     |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.96 ms: 1.01x slower                                            |
| python_startup         | 13.2 ms                                                          | 15.0 ms: 1.13x slower                                            |
| Geometric mean         | (ref)                                                            | 1.07x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 54.4 ms: 1.07x faster                                            |
| genshi_text     | 25.9 ms                                                          | 25.0 ms: 1.04x faster                                            |
| mako            | 10.4 ms                                                          | 10.7 ms: 1.03x slower                                            |
| django_template | 39.0 ms                                                          | 41.0 ms: 1.05x slower                                            |
| Geometric mean  | (ref)                                                            | 1.00x faster                                                     |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|---------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy                  | 377 us                                                           | 289 us: 1.31x faster                                             |
| deepcopy_memo             | 37.3 us                                                          | 29.4 us: 1.27x faster                                            |
| go                        | 165 ms                                                           | 133 ms: 1.24x faster                                             |
| deepcopy_reduce           | 3.39 us                                                          | 2.96 us: 1.14x faster                                            |
| generators                | 33.5 ms                                                          | 29.3 ms: 1.14x faster                                            |
| async_tree_memoization    | 460 ms                                                           | 415 ms: 1.11x faster                                             |
| async_tree_none           | 365 ms                                                           | 332 ms: 1.10x faster                                             |
| richards_super            | 61.2 ms                                                          | 55.6 ms: 1.10x faster                                            |
| scimark_fft               | 312 ms                                                           | 286 ms: 1.09x faster                                             |
| async_tree_memoization_tg | 421 ms                                                           | 386 ms: 1.09x faster                                             |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 558 ms: 1.08x faster                                             |
| richards                  | 53.4 ms                                                          | 49.5 ms: 1.08x faster                                            |
| pathlib                   | 17.1 ms                                                          | 15.9 ms: 1.08x faster                                            |
| async_tree_io_tg          | 900 ms                                                           | 837 ms: 1.07x faster                                             |
| scimark_sor               | 119 ms                                                           | 111 ms: 1.07x faster                                             |
| genshi_xml                | 58.1 ms                                                          | 54.4 ms: 1.07x faster                                            |
| pickle_dict               | 32.8 us                                                          | 31.0 us: 1.06x faster                                            |
| bpe_tokeniser             | 5.14 sec                                                         | 4.86 sec: 1.06x faster                                           |
| async_tree_io             | 873 ms                                                           | 827 ms: 1.06x faster                                             |
| scimark_sparse_mat_mult   | 4.28 ms                                                          | 4.06 ms: 1.06x faster                                            |
| async_tree_none_tg        | 340 ms                                                           | 323 ms: 1.05x faster                                             |
| regex_v8                  | 26.0 ms                                                          | 24.7 ms: 1.05x faster                                            |
| html5lib                  | 74.7 ms                                                          | 71.1 ms: 1.05x faster                                            |
| unpickle_pure_python      | 224 us                                                           | 214 us: 1.05x faster                                             |
| coroutines                | 22.0 ms                                                          | 21.1 ms: 1.04x faster                                            |
| regex_compile             | 144 ms                                                           | 139 ms: 1.04x faster                                             |
| json                      | 5.35 ms                                                          | 5.16 ms: 1.04x faster                                            |
| genshi_text               | 25.9 ms                                                          | 25.0 ms: 1.04x faster                                            |
| scimark_lu                | 97.5 ms                                                          | 94.2 ms: 1.03x faster                                            |
| 2to3                      | 291 ms                                                           | 282 ms: 1.03x faster                                             |
| pickle_list               | 4.44 us                                                          | 4.31 us: 1.03x faster                                            |
| unpickle                  | 15.7 us                                                          | 15.2 us: 1.03x faster                                            |
| docutils                  | 2.98 sec                                                         | 2.90 sec: 1.03x faster                                           |
| regex_dna                 | 249 ms                                                           | 243 ms: 1.03x faster                                             |
| pyflate                   | 482 ms                                                           | 469 ms: 1.03x faster                                             |
| unpickle_list             | 4.70 us                                                          | 4.58 us: 1.03x faster                                            |
| meteor_contest            | 128 ms                                                           | 125 ms: 1.03x faster                                             |
| asyncio_websockets        | 395 ms                                                           | 385 ms: 1.02x faster                                             |
| tornado_http              | 119 ms                                                           | 117 ms: 1.02x faster                                             |
| sqlite_synth              | 2.80 us                                                          | 2.74 us: 1.02x faster                                            |
| telco                     | 8.40 ms                                                          | 8.23 ms: 1.02x faster                                            |
| pprint_pformat            | 1.66 sec                                                         | 1.63 sec: 1.02x faster                                           |
| pprint_safe_repr          | 818 ms                                                           | 803 ms: 1.02x faster                                             |
| hexiom                    | 6.35 ms                                                          | 6.24 ms: 1.02x faster                                            |
| asyncio_tcp               | 378 ms                                                           | 371 ms: 1.02x faster                                             |
| sqlglot_normalize         | 120 ms                                                           | 118 ms: 1.02x faster                                             |
| spectral_norm             | 97.3 ms                                                          | 96.0 ms: 1.01x faster                                            |
| pickle                    | 10.6 us                                                          | 10.5 us: 1.01x faster                                            |
| sympy_sum                 | 155 ms                                                           | 153 ms: 1.01x faster                                             |
| coverage                  | 83.5 ms                                                          | 82.6 ms: 1.01x faster                                            |
| xml_etree_iterparse       | 103 ms                                                           | 102 ms: 1.01x faster                                             |
| thrift                    | 880 us                                                           | 873 us: 1.01x faster                                             |
| sqlglot_optimize          | 59.5 ms                                                          | 59.1 ms: 1.01x faster                                            |
| xml_etree_generate        | 85.7 ms                                                          | 85.2 ms: 1.01x faster                                            |
| pidigits                  | 254 ms                                                           | 252 ms: 1.01x faster                                             |
| sympy_str                 | 295 ms                                                           | 293 ms: 1.01x faster                                             |
| sympy_expand              | 501 ms                                                           | 498 ms: 1.00x faster                                             |
| nqueens                   | 88.4 ms                                                          | 88.0 ms: 1.00x faster                                            |
| async_generators          | 363 ms                                                           | 364 ms: 1.00x slower                                             |
| sqlglot_transpile         | 1.76 ms                                                          | 1.77 ms: 1.00x slower                                            |
| fannkuch                  | 353 ms                                                           | 354 ms: 1.00x slower                                             |
| regex_effbot              | 3.40 ms                                                          | 3.43 ms: 1.01x slower                                            |
| json_loads                | 25.0 us                                                          | 25.3 us: 1.01x slower                                            |
| sympy_integrate           | 23.2 ms                                                          | 23.4 ms: 1.01x slower                                            |
| typing_runtime_protocols  | 171 us                                                           | 173 us: 1.01x slower                                             |
| python_startup_no_site    | 8.85 ms                                                          | 8.96 ms: 1.01x slower                                            |
| logging_silent            | 96.3 ns                                                          | 98.0 ns: 1.02x slower                                            |
| mdp                       | 2.46 sec                                                         | 2.51 sec: 1.02x slower                                           |
| chaos                     | 59.6 ms                                                          | 60.7 ms: 1.02x slower                                            |
| pycparser                 | 1.22 sec                                                         | 1.25 sec: 1.02x slower                                           |
| deltablue                 | 3.37 ms                                                          | 3.44 ms: 1.02x slower                                            |
| float                     | 80.2 ms                                                          | 82.2 ms: 1.02x slower                                            |
| nbody                     | 87.8 ms                                                          | 90.1 ms: 1.03x slower                                            |
| logging_simple            | 6.40 us                                                          | 6.57 us: 1.03x slower                                            |
| comprehensions            | 17.0 us                                                          | 17.4 us: 1.03x slower                                            |
| mako                      | 10.4 ms                                                          | 10.7 ms: 1.03x slower                                            |
| raytrace                  | 260 ms                                                           | 270 ms: 1.04x slower                                             |
| tomli_loads               | 2.40 sec                                                         | 2.50 sec: 1.04x slower                                           |
| pickle_pure_python        | 307 us                                                           | 320 us: 1.04x slower                                             |
| django_template           | 39.0 ms                                                          | 41.0 ms: 1.05x slower                                            |
| json_dumps                | 10.8 ms                                                          | 11.4 ms: 1.06x slower                                            |
| python_startup            | 13.2 ms                                                          | 15.0 ms: 1.13x slower                                            |
| gc_traversal              | 4.69 ms                                                          | 5.32 ms: 1.14x slower                                            |
| create_gc_cycles          | 2.00 ms                                                          | 2.97 ms: 1.48x slower                                            |
| bench_mp_pool             | 4.91 ms                                                          | 1.94 sec: 394.65x slower                                         |
| Geometric mean            | (ref)                                                            | 1.04x slower                                                     |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed_tg, crypto_pyaes, scimark_monte_carlo, asyncio_tcp_ssl, bench_thread_pool, sqlglot_parse, xml_etree_parse, dulwich_log, xml_etree_process, logging_format, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.13x