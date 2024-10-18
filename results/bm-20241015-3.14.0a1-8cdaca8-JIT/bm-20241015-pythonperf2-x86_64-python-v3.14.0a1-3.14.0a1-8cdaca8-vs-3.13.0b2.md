# Results vs. 3.13.0b2

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.07x slower
- HPT reliability: 59.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 314 ms: 1.08x slower                                             |
| docutils       | 2.98 sec                                                         | 3.17 sec: 1.06x slower                                           |
| html5lib       | 74.7 ms                                                          | 69.2 ms: 1.08x faster                                            |
| tornado_http   | 119 ms                                                           | 123 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                            | 1.02x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 421 ms                                                           | 373 ms: 1.13x faster                                             |
| async_tree_memoization     | 460 ms                                                           | 408 ms: 1.13x faster                                             |
| async_tree_none            | 365 ms                                                           | 333 ms: 1.10x faster                                             |
| async_tree_none_tg         | 340 ms                                                           | 323 ms: 1.05x faster                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 574 ms: 1.05x faster                                             |
| async_tree_io_tg           | 900 ms                                                           | 865 ms: 1.04x faster                                             |
| async_tree_io              | 873 ms                                                           | 846 ms: 1.03x faster                                             |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 557 ms: 1.03x faster                                             |
| Geometric mean             | (ref)                                                            | 1.07x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 83.7 ms: 1.05x faster                                            |
| float          | 80.2 ms                                                          | 79.3 ms: 1.01x faster                                            |
| pidigits       | 254 ms                                                           | 251 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                            | 1.02x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 233 ms: 1.07x faster                                             |
| regex_v8       | 26.0 ms                                                          | 25.0 ms: 1.04x faster                                            |
| regex_compile  | 144 ms                                                           | 150 ms: 1.04x slower                                             |
| regex_effbot   | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                            | 1.00x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.12 sec: 1.13x faster                                           |
| xml_etree_generate   | 85.7 ms                                                          | 80.6 ms: 1.06x faster                                            |
| unpickle             | 15.7 us                                                          | 14.9 us: 1.05x faster                                            |
| xml_etree_process    | 59.7 ms                                                          | 57.7 ms: 1.04x faster                                            |
| xml_etree_iterparse  | 103 ms                                                           | 99.5 ms: 1.03x faster                                            |
| json_loads           | 25.0 us                                                          | 24.6 us: 1.02x faster                                            |
| unpickle_pure_python | 224 us                                                           | 221 us: 1.02x faster                                             |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                             |
| pickle               | 10.6 us                                                          | 10.7 us: 1.01x slower                                            |
| json_dumps           | 10.8 ms                                                          | 11.2 ms: 1.04x slower                                            |
| pickle_list          | 4.44 us                                                          | 4.66 us: 1.05x slower                                            |
| pickle_pure_python   | 307 us                                                           | 333 us: 1.08x slower                                             |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                     |

Benchmark hidden because not significant (2): unpickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 9.01 ms: 1.02x slower                                            |
| python_startup         | 13.2 ms                                                          | 14.9 ms: 1.13x slower                                            |
| Geometric mean         | (ref)                                                            | 1.07x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.52 ms: 1.09x faster                                            |
| genshi_xml      | 58.1 ms                                                          | 62.1 ms: 1.07x slower                                            |
| genshi_text     | 25.9 ms                                                          | 28.0 ms: 1.08x slower                                            |
| django_template | 39.0 ms                                                          | 42.9 ms: 1.10x slower                                            |
| Geometric mean  | (ref)                                                            | 1.04x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 29.9 us: 1.25x faster                                            |
| deepcopy                   | 377 us                                                           | 309 us: 1.22x faster                                             |
| scimark_sor                | 119 ms                                                           | 103 ms: 1.15x faster                                             |
| richards                   | 53.4 ms                                                          | 46.6 ms: 1.15x faster                                            |
| richards_super             | 61.2 ms                                                          | 53.6 ms: 1.14x faster                                            |
| tomli_loads                | 2.40 sec                                                         | 2.12 sec: 1.13x faster                                           |
| async_tree_memoization_tg  | 421 ms                                                           | 373 ms: 1.13x faster                                             |
| async_tree_memoization     | 460 ms                                                           | 408 ms: 1.13x faster                                             |
| async_tree_none            | 365 ms                                                           | 333 ms: 1.10x faster                                             |
| deepcopy_reduce            | 3.39 us                                                          | 3.10 us: 1.09x faster                                            |
| mako                       | 10.4 ms                                                          | 9.52 ms: 1.09x faster                                            |
| bpe_tokeniser              | 5.14 sec                                                         | 4.74 sec: 1.08x faster                                           |
| go                         | 165 ms                                                           | 152 ms: 1.08x faster                                             |
| html5lib                   | 74.7 ms                                                          | 69.2 ms: 1.08x faster                                            |
| scimark_fft                | 312 ms                                                           | 290 ms: 1.08x faster                                             |
| telco                      | 8.40 ms                                                          | 7.80 ms: 1.08x faster                                            |
| pathlib                    | 17.1 ms                                                          | 15.9 ms: 1.08x faster                                            |
| regex_dna                  | 249 ms                                                           | 233 ms: 1.07x faster                                             |
| xml_etree_generate         | 85.7 ms                                                          | 80.6 ms: 1.06x faster                                            |
| unpickle                   | 15.7 us                                                          | 14.9 us: 1.05x faster                                            |
| coverage                   | 83.5 ms                                                          | 79.2 ms: 1.05x faster                                            |
| json                       | 5.35 ms                                                          | 5.08 ms: 1.05x faster                                            |
| async_tree_none_tg         | 340 ms                                                           | 323 ms: 1.05x faster                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 574 ms: 1.05x faster                                             |
| nbody                      | 87.8 ms                                                          | 83.7 ms: 1.05x faster                                            |
| spectral_norm              | 97.3 ms                                                          | 93.0 ms: 1.05x faster                                            |
| dulwich_log                | 67.3 ms                                                          | 64.5 ms: 1.04x faster                                            |
| regex_v8                   | 26.0 ms                                                          | 25.0 ms: 1.04x faster                                            |
| async_tree_io_tg           | 900 ms                                                           | 865 ms: 1.04x faster                                             |
| xml_etree_process          | 59.7 ms                                                          | 57.7 ms: 1.04x faster                                            |
| asyncio_websockets         | 395 ms                                                           | 381 ms: 1.04x faster                                             |
| async_tree_io              | 873 ms                                                           | 846 ms: 1.03x faster                                             |
| xml_etree_iterparse        | 103 ms                                                           | 99.5 ms: 1.03x faster                                            |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 557 ms: 1.03x faster                                             |
| sqlite_synth               | 2.80 us                                                          | 2.73 us: 1.03x faster                                            |
| pprint_safe_repr           | 818 ms                                                           | 798 ms: 1.03x faster                                             |
| deltablue                  | 3.37 ms                                                          | 3.30 ms: 1.02x faster                                            |
| scimark_lu                 | 97.5 ms                                                          | 95.5 ms: 1.02x faster                                            |
| crypto_pyaes               | 73.6 ms                                                          | 72.2 ms: 1.02x faster                                            |
| pyflate                    | 482 ms                                                           | 473 ms: 1.02x faster                                             |
| coroutines                 | 22.0 ms                                                          | 21.6 ms: 1.02x faster                                            |
| json_loads                 | 25.0 us                                                          | 24.6 us: 1.02x faster                                            |
| unpickle_pure_python       | 224 us                                                           | 221 us: 1.02x faster                                             |
| float                      | 80.2 ms                                                          | 79.3 ms: 1.01x faster                                            |
| pprint_pformat             | 1.66 sec                                                         | 1.64 sec: 1.01x faster                                           |
| pidigits                   | 254 ms                                                           | 251 ms: 1.01x faster                                             |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.26 ms: 1.01x faster                                            |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x slower                                           |
| xml_etree_parse            | 144 ms                                                           | 145 ms: 1.01x slower                                             |
| pickle                     | 10.6 us                                                          | 10.7 us: 1.01x slower                                            |
| logging_format             | 7.11 us                                                          | 7.21 us: 1.01x slower                                            |
| thrift                     | 880 us                                                           | 894 us: 1.02x slower                                             |
| python_startup_no_site     | 8.85 ms                                                          | 9.01 ms: 1.02x slower                                            |
| fannkuch                   | 353 ms                                                           | 361 ms: 1.02x slower                                             |
| tornado_http               | 119 ms                                                           | 123 ms: 1.03x slower                                             |
| logging_simple             | 6.40 us                                                          | 6.62 us: 1.03x slower                                            |
| meteor_contest             | 128 ms                                                           | 133 ms: 1.04x slower                                             |
| json_dumps                 | 10.8 ms                                                          | 11.2 ms: 1.04x slower                                            |
| regex_compile              | 144 ms                                                           | 150 ms: 1.04x slower                                             |
| async_generators           | 363 ms                                                           | 379 ms: 1.04x slower                                             |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.4 ms: 1.05x slower                                            |
| bench_thread_pool          | 908 us                                                           | 950 us: 1.05x slower                                             |
| pickle_list                | 4.44 us                                                          | 4.66 us: 1.05x slower                                            |
| regex_effbot               | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                            |
| mdp                        | 2.46 sec                                                         | 2.59 sec: 1.05x slower                                           |
| typing_runtime_protocols   | 171 us                                                           | 180 us: 1.05x slower                                             |
| pycparser                  | 1.22 sec                                                         | 1.29 sec: 1.06x slower                                           |
| sympy_expand               | 501 ms                                                           | 530 ms: 1.06x slower                                             |
| docutils                   | 2.98 sec                                                         | 3.17 sec: 1.06x slower                                           |
| genshi_xml                 | 58.1 ms                                                          | 62.1 ms: 1.07x slower                                            |
| 2to3                       | 291 ms                                                           | 314 ms: 1.08x slower                                             |
| sqlglot_parse              | 1.39 ms                                                          | 1.50 ms: 1.08x slower                                            |
| genshi_text                | 25.9 ms                                                          | 28.0 ms: 1.08x slower                                            |
| pickle_pure_python         | 307 us                                                           | 333 us: 1.08x slower                                             |
| sympy_str                  | 295 ms                                                           | 319 ms: 1.08x slower                                             |
| django_template            | 39.0 ms                                                          | 42.9 ms: 1.10x slower                                            |
| sqlglot_normalize          | 120 ms                                                           | 132 ms: 1.10x slower                                             |
| comprehensions             | 17.0 us                                                          | 18.8 us: 1.11x slower                                            |
| gc_traversal               | 4.69 ms                                                          | 5.21 ms: 1.11x slower                                            |
| chaos                      | 59.6 ms                                                          | 66.5 ms: 1.12x slower                                            |
| sympy_sum                  | 155 ms                                                           | 173 ms: 1.12x slower                                             |
| hexiom                     | 6.35 ms                                                          | 7.11 ms: 1.12x slower                                            |
| sqlglot_transpile          | 1.76 ms                                                          | 1.98 ms: 1.12x slower                                            |
| python_startup             | 13.2 ms                                                          | 14.9 ms: 1.13x slower                                            |
| sqlglot_optimize           | 59.5 ms                                                          | 69.7 ms: 1.17x slower                                            |
| nqueens                    | 88.4 ms                                                          | 104 ms: 1.17x slower                                             |
| generators                 | 33.5 ms                                                          | 39.4 ms: 1.18x slower                                            |
| sympy_integrate            | 23.2 ms                                                          | 27.3 ms: 1.18x slower                                            |
| raytrace                   | 260 ms                                                           | 315 ms: 1.21x slower                                             |
| pylint                     | 339 ms                                                           | 423 ms: 1.25x slower                                             |
| create_gc_cycles           | 2.00 ms                                                          | 2.90 ms: 1.45x slower                                            |
| bench_mp_pool              | 4.91 ms                                                          | 2.28 sec: 465.29x slower                                         |
| Geometric mean             | (ref)                                                            | 1.07x slower                                                     |

Benchmark hidden because not significant (4): logging_silent, unpickle_list, asyncio_tcp, pickle_dict
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 59.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.19x