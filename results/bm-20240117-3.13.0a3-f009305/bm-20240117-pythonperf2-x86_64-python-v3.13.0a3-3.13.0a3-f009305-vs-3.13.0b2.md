# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.01x slower
- HPT reliability: 56.42%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 294 ms: 1.01x slower                                             |
| chameleon      | 7.40 ms                                                          | 7.26 ms: 1.02x faster                                            |
| docutils       | 2.98 sec                                                         | 2.83 sec: 1.06x faster                                           |
| html5lib       | 74.7 ms                                                          | 73.9 ms: 1.01x faster                                            |
| tornado_http   | 119 ms                                                           | 118 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                            | 1.02x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 604 ms                                                           | 701 ms: 1.16x slower                                             |
| async_tree_io_tg           | 900 ms                                                           | 1.07 sec: 1.19x slower                                           |
| async_tree_memoization     | 460 ms                                                           | 547 ms: 1.19x slower                                             |
| async_tree_none            | 365 ms                                                           | 435 ms: 1.19x slower                                             |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 701 ms: 1.22x slower                                             |
| async_tree_io              | 873 ms                                                           | 1.08 sec: 1.23x slower                                           |
| async_tree_none_tg         | 340 ms                                                           | 430 ms: 1.26x slower                                             |
| async_tree_memoization_tg  | 421 ms                                                           | 545 ms: 1.30x slower                                             |
| Geometric mean             | (ref)                                                            | 1.22x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 85.3 ms: 1.03x faster                                            |
| float          | 80.2 ms                                                          | 78.0 ms: 1.03x faster                                            |
| pidigits       | 254 ms                                                           | 263 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                            | 1.01x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 238 ms: 1.05x faster                                             |
| regex_compile  | 144 ms                                                           | 141 ms: 1.02x faster                                             |
| regex_effbot   | 3.40 ms                                                          | 3.50 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                            | 1.01x faster                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.23 sec: 1.08x faster                                           |
| unpickle_pure_python | 224 us                                                           | 213 us: 1.06x faster                                             |
| pickle               | 10.6 us                                                          | 10.4 us: 1.02x faster                                            |
| json_dumps           | 10.8 ms                                                          | 10.6 ms: 1.02x faster                                            |
| unpickle             | 15.7 us                                                          | 15.4 us: 1.02x faster                                            |
| xml_etree_process    | 59.7 ms                                                          | 58.7 ms: 1.02x faster                                            |
| pickle_dict          | 32.8 us                                                          | 32.5 us: 1.01x faster                                            |
| json_loads           | 25.0 us                                                          | 25.0 us: 1.00x faster                                            |
| pickle_list          | 4.44 us                                                          | 4.49 us: 1.01x slower                                            |
| unpickle_list        | 4.70 us                                                          | 4.82 us: 1.03x slower                                            |
| xml_etree_iterparse  | 103 ms                                                           | 107 ms: 1.04x slower                                             |
| xml_etree_parse      | 144 ms                                                           | 150 ms: 1.04x slower                                             |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                     |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 12.6 ms: 1.05x faster                                            |
| python_startup_no_site | 8.85 ms                                                          | 11.0 ms: 1.24x slower                                            |
| Geometric mean         | (ref)                                                            | 1.09x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 55.6 ms: 1.04x faster                                            |
| django_template | 39.0 ms                                                          | 38.4 ms: 1.02x faster                                            |
| Geometric mean  | (ref)                                                            | 1.02x faster                                                     |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols   | 171 us                                                           | 113 us: 1.51x faster                                             |
| create_gc_cycles           | 2.00 ms                                                          | 1.57 ms: 1.28x faster                                            |
| gc_traversal               | 4.69 ms                                                          | 3.94 ms: 1.19x faster                                            |
| tomli_loads                | 2.40 sec                                                         | 2.23 sec: 1.08x faster                                           |
| bench_mp_pool              | 4.91 ms                                                          | 4.57 ms: 1.07x faster                                            |
| unpickle_pure_python       | 224 us                                                           | 213 us: 1.06x faster                                             |
| docutils                   | 2.98 sec                                                         | 2.83 sec: 1.06x faster                                           |
| spectral_norm              | 97.3 ms                                                          | 92.3 ms: 1.05x faster                                            |
| python_startup             | 13.2 ms                                                          | 12.6 ms: 1.05x faster                                            |
| regex_dna                  | 249 ms                                                           | 238 ms: 1.05x faster                                             |
| genshi_xml                 | 58.1 ms                                                          | 55.6 ms: 1.04x faster                                            |
| sqlglot_normalize          | 120 ms                                                           | 116 ms: 1.04x faster                                             |
| deepcopy_reduce            | 3.39 us                                                          | 3.28 us: 1.03x faster                                            |
| scimark_fft                | 312 ms                                                           | 302 ms: 1.03x faster                                             |
| crypto_pyaes               | 73.6 ms                                                          | 71.4 ms: 1.03x faster                                            |
| richards_super             | 61.2 ms                                                          | 59.4 ms: 1.03x faster                                            |
| nbody                      | 87.8 ms                                                          | 85.3 ms: 1.03x faster                                            |
| deepcopy                   | 377 us                                                           | 367 us: 1.03x faster                                             |
| float                      | 80.2 ms                                                          | 78.0 ms: 1.03x faster                                            |
| comprehensions             | 17.0 us                                                          | 16.5 us: 1.03x faster                                            |
| pickle                     | 10.6 us                                                          | 10.4 us: 1.02x faster                                            |
| regex_compile              | 144 ms                                                           | 141 ms: 1.02x faster                                             |
| telco                      | 8.40 ms                                                          | 8.23 ms: 1.02x faster                                            |
| json_dumps                 | 10.8 ms                                                          | 10.6 ms: 1.02x faster                                            |
| asyncio_tcp                | 378 ms                                                           | 371 ms: 1.02x faster                                             |
| unpickle                   | 15.7 us                                                          | 15.4 us: 1.02x faster                                            |
| chameleon                  | 7.40 ms                                                          | 7.26 ms: 1.02x faster                                            |
| xml_etree_process          | 59.7 ms                                                          | 58.7 ms: 1.02x faster                                            |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.21 ms: 1.02x faster                                            |
| json                       | 5.35 ms                                                          | 5.27 ms: 1.02x faster                                            |
| django_template            | 39.0 ms                                                          | 38.4 ms: 1.02x faster                                            |
| flaskblogging              | 4.68 ms                                                          | 4.61 ms: 1.02x faster                                            |
| tornado_http               | 119 ms                                                           | 118 ms: 1.01x faster                                             |
| sympy_expand               | 501 ms                                                           | 494 ms: 1.01x faster                                             |
| pickle_dict                | 32.8 us                                                          | 32.5 us: 1.01x faster                                            |
| html5lib                   | 74.7 ms                                                          | 73.9 ms: 1.01x faster                                            |
| sqlglot_optimize           | 59.5 ms                                                          | 59.0 ms: 1.01x faster                                            |
| thrift                     | 880 us                                                           | 872 us: 1.01x faster                                             |
| sqlite_synth               | 2.80 us                                                          | 2.77 us: 1.01x faster                                            |
| aiohttp                    | 1.07 ms                                                          | 1.06 ms: 1.01x faster                                            |
| sympy_sum                  | 155 ms                                                           | 154 ms: 1.01x faster                                             |
| coverage                   | 83.5 ms                                                          | 82.9 ms: 1.01x faster                                            |
| pprint_safe_repr           | 818 ms                                                           | 813 ms: 1.01x faster                                             |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.57 sec: 1.00x faster                                           |
| deepcopy_memo              | 37.3 us                                                          | 37.1 us: 1.00x faster                                            |
| sympy_str                  | 295 ms                                                           | 294 ms: 1.00x faster                                             |
| json_loads                 | 25.0 us                                                          | 25.0 us: 1.00x faster                                            |
| richards                   | 53.4 ms                                                          | 53.7 ms: 1.00x slower                                            |
| go                         | 165 ms                                                           | 166 ms: 1.01x slower                                             |
| sympy_integrate            | 23.2 ms                                                          | 23.3 ms: 1.01x slower                                            |
| generators                 | 33.5 ms                                                          | 33.8 ms: 1.01x slower                                            |
| nqueens                    | 88.4 ms                                                          | 89.1 ms: 1.01x slower                                            |
| 2to3                       | 291 ms                                                           | 294 ms: 1.01x slower                                             |
| pickle_list                | 4.44 us                                                          | 4.49 us: 1.01x slower                                            |
| meteor_contest             | 128 ms                                                           | 130 ms: 1.01x slower                                             |
| sqlglot_transpile          | 1.76 ms                                                          | 1.79 ms: 1.01x slower                                            |
| dulwich_log                | 67.3 ms                                                          | 68.2 ms: 1.01x slower                                            |
| async_generators           | 363 ms                                                           | 368 ms: 1.01x slower                                             |
| coroutines                 | 22.0 ms                                                          | 22.3 ms: 1.02x slower                                            |
| mdp                        | 2.46 sec                                                         | 2.50 sec: 1.02x slower                                           |
| hexiom                     | 6.35 ms                                                          | 6.46 ms: 1.02x slower                                            |
| raytrace                   | 260 ms                                                           | 265 ms: 1.02x slower                                             |
| unpickle_list              | 4.70 us                                                          | 4.82 us: 1.03x slower                                            |
| logging_format             | 7.11 us                                                          | 7.31 us: 1.03x slower                                            |
| regex_effbot               | 3.40 ms                                                          | 3.50 ms: 1.03x slower                                            |
| scimark_monte_carlo        | 65.5 ms                                                          | 67.9 ms: 1.04x slower                                            |
| pidigits                   | 254 ms                                                           | 263 ms: 1.04x slower                                             |
| xml_etree_iterparse        | 103 ms                                                           | 107 ms: 1.04x slower                                             |
| pyflate                    | 482 ms                                                           | 501 ms: 1.04x slower                                             |
| logging_simple             | 6.40 us                                                          | 6.66 us: 1.04x slower                                            |
| xml_etree_parse            | 144 ms                                                           | 150 ms: 1.04x slower                                             |
| deltablue                  | 3.37 ms                                                          | 3.54 ms: 1.05x slower                                            |
| bench_thread_pool          | 908 us                                                           | 960 us: 1.06x slower                                             |
| pycparser                  | 1.22 sec                                                         | 1.32 sec: 1.08x slower                                           |
| fannkuch                   | 353 ms                                                           | 386 ms: 1.10x slower                                             |
| pathlib                    | 17.1 ms                                                          | 18.9 ms: 1.10x slower                                            |
| mypy2                      | 764 ms                                                           | 864 ms: 1.13x slower                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 701 ms: 1.16x slower                                             |
| async_tree_io_tg           | 900 ms                                                           | 1.07 sec: 1.19x slower                                           |
| async_tree_memoization     | 460 ms                                                           | 547 ms: 1.19x slower                                             |
| async_tree_none            | 365 ms                                                           | 435 ms: 1.19x slower                                             |
| scimark_sor                | 119 ms                                                           | 144 ms: 1.21x slower                                             |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 701 ms: 1.22x slower                                             |
| async_tree_io              | 873 ms                                                           | 1.08 sec: 1.23x slower                                           |
| python_startup_no_site     | 8.85 ms                                                          | 11.0 ms: 1.24x slower                                            |
| async_tree_none_tg         | 340 ms                                                           | 430 ms: 1.26x slower                                             |
| async_tree_memoization_tg  | 421 ms                                                           | 545 ms: 1.30x slower                                             |
| Geometric mean             | (ref)                                                            | 1.01x slower                                                     |

Benchmark hidden because not significant (13): genshi_text, mako, logging_silent, pprint_pformat, pickle_pure_python, xml_etree_generate, regex_v8, sqlglot_parse, asyncio_websockets, gunicorn, scimark_lu, chaos, pylint
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, dask

# HPT report

- Reliability score: 56.42% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.95x