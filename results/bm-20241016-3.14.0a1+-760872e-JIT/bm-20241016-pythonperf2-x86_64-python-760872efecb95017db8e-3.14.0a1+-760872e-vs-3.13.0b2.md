# Results vs. 3.13.0b2

- fork: python
- ref: 760872efecb95017db8e
- machine: linux-x86_64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.08x slower
- HPT reliability: 63.58%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 315 ms: 1.08x slower                                                         |
| docutils       | 2.98 sec                                                         | 3.20 sec: 1.07x slower                                                       |
| html5lib       | 74.7 ms                                                          | 69.9 ms: 1.07x faster                                                        |
| tornado_http   | 119 ms                                                           | 123 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                            | 1.03x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 413 ms: 1.11x faster                                                         |
| async_tree_memoization_tg  | 421 ms                                                           | 378 ms: 1.11x faster                                                         |
| async_tree_none            | 365 ms                                                           | 333 ms: 1.10x faster                                                         |
| async_tree_none_tg         | 340 ms                                                           | 322 ms: 1.06x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 578 ms: 1.05x faster                                                         |
| async_tree_io              | 873 ms                                                           | 846 ms: 1.03x faster                                                         |
| async_tree_io_tg           | 900 ms                                                           | 873 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 561 ms: 1.02x faster                                                         |
| Geometric mean             | (ref)                                                            | 1.06x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 81.9 ms: 1.07x faster                                                        |
| pidigits       | 254 ms                                                           | 252 ms: 1.01x faster                                                         |
| float          | 80.2 ms                                                          | 79.8 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                            | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 24.6 ms: 1.06x faster                                                        |
| regex_dna      | 249 ms                                                           | 243 ms: 1.03x faster                                                         |
| regex_effbot   | 3.40 ms                                                          | 3.44 ms: 1.01x slower                                                        |
| regex_compile  | 144 ms                                                           | 147 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.13 sec: 1.13x faster                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 81.9 ms: 1.05x faster                                                        |
| xml_etree_process    | 59.7 ms                                                          | 57.9 ms: 1.03x faster                                                        |
| unpickle             | 15.7 us                                                          | 15.3 us: 1.03x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 100 ms: 1.02x faster                                                         |
| json_loads           | 25.0 us                                                          | 24.6 us: 1.02x faster                                                        |
| unpickle_pure_python | 224 us                                                           | 220 us: 1.02x faster                                                         |
| pickle               | 10.6 us                                                          | 10.5 us: 1.01x faster                                                        |
| unpickle_list        | 4.70 us                                                          | 4.78 us: 1.02x slower                                                        |
| pickle_dict          | 32.8 us                                                          | 34.0 us: 1.03x slower                                                        |
| xml_etree_parse      | 144 ms                                                           | 149 ms: 1.04x slower                                                         |
| json_dumps           | 10.8 ms                                                          | 11.2 ms: 1.04x slower                                                        |
| pickle_list          | 4.44 us                                                          | 4.76 us: 1.07x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 330 us: 1.07x slower                                                         |
| Geometric mean       | (ref)                                                            | 1.00x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 9.02 ms: 1.02x slower                                                        |
| python_startup         | 13.2 ms                                                          | 15.0 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                            | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.46 ms: 1.10x faster                                                        |
| genshi_xml      | 58.1 ms                                                          | 62.6 ms: 1.08x slower                                                        |
| genshi_text     | 25.9 ms                                                          | 28.0 ms: 1.08x slower                                                        |
| django_template | 39.0 ms                                                          | 43.4 ms: 1.11x slower                                                        |
| Geometric mean  | (ref)                                                            | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 308 us: 1.22x faster                                                         |
| richards                   | 53.4 ms                                                          | 44.8 ms: 1.19x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 31.3 us: 1.19x faster                                                        |
| richards_super             | 61.2 ms                                                          | 53.0 ms: 1.16x faster                                                        |
| scimark_sor                | 119 ms                                                           | 103 ms: 1.15x faster                                                         |
| tomli_loads                | 2.40 sec                                                         | 2.13 sec: 1.13x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 413 ms: 1.11x faster                                                         |
| deepcopy_reduce            | 3.39 us                                                          | 3.05 us: 1.11x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 378 ms: 1.11x faster                                                         |
| scimark_fft                | 312 ms                                                           | 282 ms: 1.11x faster                                                         |
| async_tree_none            | 365 ms                                                           | 333 ms: 1.10x faster                                                         |
| mako                       | 10.4 ms                                                          | 9.46 ms: 1.10x faster                                                        |
| go                         | 165 ms                                                           | 151 ms: 1.09x faster                                                         |
| bpe_tokeniser              | 5.14 sec                                                         | 4.72 sec: 1.09x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 15.8 ms: 1.09x faster                                                        |
| nbody                      | 87.8 ms                                                          | 81.9 ms: 1.07x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 69.9 ms: 1.07x faster                                                        |
| telco                      | 8.40 ms                                                          | 7.90 ms: 1.06x faster                                                        |
| pyflate                    | 482 ms                                                           | 453 ms: 1.06x faster                                                         |
| json                       | 5.35 ms                                                          | 5.07 ms: 1.06x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 322 ms: 1.06x faster                                                         |
| regex_v8                   | 26.0 ms                                                          | 24.6 ms: 1.06x faster                                                        |
| logging_silent             | 96.3 ns                                                          | 91.4 ns: 1.05x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 81.9 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 578 ms: 1.05x faster                                                         |
| spectral_norm              | 97.3 ms                                                          | 93.1 ms: 1.05x faster                                                        |
| coverage                   | 83.5 ms                                                          | 80.2 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 818 ms                                                           | 790 ms: 1.03x faster                                                         |
| sqlite_synth               | 2.80 us                                                          | 2.71 us: 1.03x faster                                                        |
| async_tree_io              | 873 ms                                                           | 846 ms: 1.03x faster                                                         |
| xml_etree_process          | 59.7 ms                                                          | 57.9 ms: 1.03x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 873 ms: 1.03x faster                                                         |
| crypto_pyaes               | 73.6 ms                                                          | 71.5 ms: 1.03x faster                                                        |
| regex_dna                  | 249 ms                                                           | 243 ms: 1.03x faster                                                         |
| unpickle                   | 15.7 us                                                          | 15.3 us: 1.03x faster                                                        |
| scimark_lu                 | 97.5 ms                                                          | 95.1 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                           | 100 ms: 1.02x faster                                                         |
| dulwich_log                | 67.3 ms                                                          | 65.7 ms: 1.02x faster                                                        |
| deltablue                  | 3.37 ms                                                          | 3.30 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 561 ms: 1.02x faster                                                         |
| asyncio_websockets         | 395 ms                                                           | 387 ms: 1.02x faster                                                         |
| json_loads                 | 25.0 us                                                          | 24.6 us: 1.02x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 220 us: 1.02x faster                                                         |
| pprint_pformat             | 1.66 sec                                                         | 1.63 sec: 1.02x faster                                                       |
| coroutines                 | 22.0 ms                                                          | 21.7 ms: 1.01x faster                                                        |
| pickle                     | 10.6 us                                                          | 10.5 us: 1.01x faster                                                        |
| pidigits                   | 254 ms                                                           | 252 ms: 1.01x faster                                                         |
| float                      | 80.2 ms                                                          | 79.8 ms: 1.00x faster                                                        |
| thrift                     | 880 us                                                           | 887 us: 1.01x slower                                                         |
| regex_effbot               | 3.40 ms                                                          | 3.44 ms: 1.01x slower                                                        |
| logging_format             | 7.11 us                                                          | 7.23 us: 1.02x slower                                                        |
| unpickle_list              | 4.70 us                                                          | 4.78 us: 1.02x slower                                                        |
| regex_compile              | 144 ms                                                           | 147 ms: 1.02x slower                                                         |
| python_startup_no_site     | 8.85 ms                                                          | 9.02 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.37 ms: 1.02x slower                                                        |
| tornado_http               | 119 ms                                                           | 123 ms: 1.03x slower                                                         |
| logging_simple             | 6.40 us                                                          | 6.59 us: 1.03x slower                                                        |
| pickle_dict                | 32.8 us                                                          | 34.0 us: 1.03x slower                                                        |
| xml_etree_parse            | 144 ms                                                           | 149 ms: 1.04x slower                                                         |
| meteor_contest             | 128 ms                                                           | 134 ms: 1.04x slower                                                         |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.2 ms: 1.04x slower                                                        |
| json_dumps                 | 10.8 ms                                                          | 11.2 ms: 1.04x slower                                                        |
| async_generators           | 363 ms                                                           | 380 ms: 1.05x slower                                                         |
| fannkuch                   | 353 ms                                                           | 371 ms: 1.05x slower                                                         |
| bench_thread_pool          | 908 us                                                           | 959 us: 1.06x slower                                                         |
| pycparser                  | 1.22 sec                                                         | 1.29 sec: 1.06x slower                                                       |
| sympy_expand               | 501 ms                                                           | 532 ms: 1.06x slower                                                         |
| typing_runtime_protocols   | 171 us                                                           | 183 us: 1.07x slower                                                         |
| pickle_list                | 4.44 us                                                          | 4.76 us: 1.07x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.64 sec: 1.07x slower                                                       |
| docutils                   | 2.98 sec                                                         | 3.20 sec: 1.07x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 330 us: 1.07x slower                                                         |
| genshi_xml                 | 58.1 ms                                                          | 62.6 ms: 1.08x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 1.50 ms: 1.08x slower                                                        |
| genshi_text                | 25.9 ms                                                          | 28.0 ms: 1.08x slower                                                        |
| 2to3                       | 291 ms                                                           | 315 ms: 1.08x slower                                                         |
| sympy_str                  | 295 ms                                                           | 318 ms: 1.08x slower                                                         |
| comprehensions             | 17.0 us                                                          | 18.5 us: 1.09x slower                                                        |
| sqlglot_normalize          | 120 ms                                                           | 132 ms: 1.10x slower                                                         |
| hexiom                     | 6.35 ms                                                          | 7.06 ms: 1.11x slower                                                        |
| django_template            | 39.0 ms                                                          | 43.4 ms: 1.11x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 1.97 ms: 1.12x slower                                                        |
| sympy_sum                  | 155 ms                                                           | 173 ms: 1.12x slower                                                         |
| python_startup             | 13.2 ms                                                          | 15.0 ms: 1.13x slower                                                        |
| generators                 | 33.5 ms                                                          | 38.6 ms: 1.15x slower                                                        |
| nqueens                    | 88.4 ms                                                          | 102 ms: 1.15x slower                                                         |
| chaos                      | 59.6 ms                                                          | 69.1 ms: 1.16x slower                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 69.5 ms: 1.17x slower                                                        |
| gc_traversal               | 4.69 ms                                                          | 5.49 ms: 1.17x slower                                                        |
| sympy_integrate            | 23.2 ms                                                          | 27.2 ms: 1.17x slower                                                        |
| pylint                     | 339 ms                                                           | 424 ms: 1.25x slower                                                         |
| raytrace                   | 260 ms                                                           | 327 ms: 1.26x slower                                                         |
| create_gc_cycles           | 2.00 ms                                                          | 2.87 ms: 1.43x slower                                                        |
| bench_mp_pool              | 4.91 ms                                                          | 3.28 sec: 668.49x slower                                                     |
| Geometric mean             | (ref)                                                            | 1.08x slower                                                                 |

Benchmark hidden because not significant (2): asyncio_tcp, asyncio_tcp_ssl
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 63.58% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.19x