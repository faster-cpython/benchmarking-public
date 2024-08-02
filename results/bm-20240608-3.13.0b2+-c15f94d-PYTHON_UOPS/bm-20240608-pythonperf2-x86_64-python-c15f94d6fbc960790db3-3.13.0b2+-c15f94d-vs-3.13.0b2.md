# Results vs. 3.13.0b2

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-x86_64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.17x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 345 ms: 1.18x slower                                                         |
| chameleon      | 7.40 ms                                                          | 8.61 ms: 1.16x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.47 sec: 1.16x slower                                                       |
| html5lib       | 74.7 ms                                                          | 88.0 ms: 1.18x slower                                                        |
| tornado_http   | 119 ms                                                           | 129 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                            | 1.15x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 475 ms: 1.03x slower                                                         |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 613 ms: 1.07x slower                                                         |
| async_tree_none_tg         | 340 ms                                                           | 366 ms: 1.07x slower                                                         |
| async_tree_memoization_tg  | 421 ms                                                           | 454 ms: 1.08x slower                                                         |
| async_tree_io              | 873 ms                                                           | 943 ms: 1.08x slower                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 654 ms: 1.08x slower                                                         |
| async_tree_none            | 365 ms                                                           | 398 ms: 1.09x slower                                                         |
| Geometric mean             | (ref)                                                            | 1.06x slower                                                                 |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 96.2 ms: 1.20x slower                                                        |
| nbody          | 87.8 ms                                                          | 125 ms: 1.42x slower                                                         |
| Geometric mean | (ref)                                                            | 1.20x slower                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 26.0 ms: 1.00x faster                                                        |
| regex_dna      | 249 ms                                                           | 255 ms: 1.02x slower                                                         |
| regex_effbot   | 3.40 ms                                                          | 3.56 ms: 1.05x slower                                                        |
| regex_compile  | 144 ms                                                           | 216 ms: 1.50x slower                                                         |
| Geometric mean | (ref)                                                            | 1.13x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 31.3 us: 1.05x faster                                                        |
| unpickle             | 15.7 us                                                          | 15.0 us: 1.04x faster                                                        |
| json_loads           | 25.0 us                                                          | 24.4 us: 1.03x faster                                                        |
| pickle               | 10.6 us                                                          | 10.5 us: 1.01x faster                                                        |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                                         |
| pickle_list          | 4.44 us                                                          | 4.56 us: 1.03x slower                                                        |
| json_dumps           | 10.8 ms                                                          | 11.3 ms: 1.05x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 113 ms: 1.10x slower                                                         |
| xml_etree_generate   | 85.7 ms                                                          | 97.0 ms: 1.13x slower                                                        |
| xml_etree_process    | 59.7 ms                                                          | 68.8 ms: 1.15x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.91 sec: 1.21x slower                                                       |
| unpickle_pure_python | 224 us                                                           | 307 us: 1.37x slower                                                         |
| pickle_pure_python   | 307 us                                                           | 434 us: 1.41x slower                                                         |
| Geometric mean       | (ref)                                                            | 1.09x slower                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.2 ms: 1.00x slower                                                        |
| python_startup_no_site | 8.85 ms                                                          | 8.91 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                            | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 67.7 ms: 1.17x slower                                                        |
| django_template | 39.0 ms                                                          | 45.5 ms: 1.17x slower                                                        |
| genshi_text     | 25.9 ms                                                          | 33.0 ms: 1.28x slower                                                        |
| mako            | 10.4 ms                                                          | 14.6 ms: 1.41x slower                                                        |
| Geometric mean  | (ref)                                                            | 1.25x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict                | 32.8 us                                                          | 31.3 us: 1.05x faster                                                        |
| unpickle                   | 15.7 us                                                          | 15.0 us: 1.04x faster                                                        |
| json_loads                 | 25.0 us                                                          | 24.4 us: 1.03x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 386 ms: 1.02x faster                                                         |
| pickle                     | 10.6 us                                                          | 10.5 us: 1.01x faster                                                        |
| regex_v8                   | 26.0 ms                                                          | 26.0 ms: 1.00x faster                                                        |
| python_startup             | 13.2 ms                                                          | 13.2 ms: 1.00x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 8.91 ms: 1.01x slower                                                        |
| xml_etree_parse            | 144 ms                                                           | 145 ms: 1.01x slower                                                         |
| gc_traversal               | 4.69 ms                                                          | 4.72 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.60 sec: 1.01x slower                                                       |
| generators                 | 33.5 ms                                                          | 34.1 ms: 1.02x slower                                                        |
| regex_dna                  | 249 ms                                                           | 255 ms: 1.02x slower                                                         |
| json                       | 5.35 ms                                                          | 5.48 ms: 1.02x slower                                                        |
| pickle_list                | 4.44 us                                                          | 4.56 us: 1.03x slower                                                        |
| asyncio_tcp                | 378 ms                                                           | 388 ms: 1.03x slower                                                         |
| thrift                     | 880 us                                                           | 906 us: 1.03x slower                                                         |
| create_gc_cycles           | 2.00 ms                                                          | 2.06 ms: 1.03x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 475 ms: 1.03x slower                                                         |
| coroutines                 | 22.0 ms                                                          | 22.8 ms: 1.04x slower                                                        |
| logging_format             | 7.11 us                                                          | 7.39 us: 1.04x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.56 ms: 1.05x slower                                                        |
| json_dumps                 | 10.8 ms                                                          | 11.3 ms: 1.05x slower                                                        |
| flaskblogging              | 4.68 ms                                                          | 4.96 ms: 1.06x slower                                                        |
| sqlite_synth               | 2.80 us                                                          | 2.97 us: 1.06x slower                                                        |
| logging_simple             | 6.40 us                                                          | 6.82 us: 1.07x slower                                                        |
| pathlib                    | 17.1 ms                                                          | 18.3 ms: 1.07x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 613 ms: 1.07x slower                                                         |
| async_tree_none_tg         | 340 ms                                                           | 366 ms: 1.07x slower                                                         |
| async_tree_memoization_tg  | 421 ms                                                           | 454 ms: 1.08x slower                                                         |
| async_tree_io              | 873 ms                                                           | 943 ms: 1.08x slower                                                         |
| tornado_http               | 119 ms                                                           | 129 ms: 1.08x slower                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 654 ms: 1.08x slower                                                         |
| async_generators           | 363 ms                                                           | 395 ms: 1.09x slower                                                         |
| async_tree_none            | 365 ms                                                           | 398 ms: 1.09x slower                                                         |
| dask                       | 391 ms                                                           | 427 ms: 1.09x slower                                                         |
| xml_etree_iterparse        | 103 ms                                                           | 113 ms: 1.10x slower                                                         |
| aiohttp                    | 1.07 ms                                                          | 1.19 ms: 1.11x slower                                                        |
| gunicorn                   | 1.04 ms                                                          | 1.16 ms: 1.11x slower                                                        |
| meteor_contest             | 128 ms                                                           | 143 ms: 1.12x slower                                                         |
| richards_super             | 61.2 ms                                                          | 68.3 ms: 1.12x slower                                                        |
| telco                      | 8.40 ms                                                          | 9.41 ms: 1.12x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.77 sec: 1.12x slower                                                       |
| bench_thread_pool          | 908 us                                                           | 1.02 ms: 1.13x slower                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 97.0 ms: 1.13x slower                                                        |
| richards                   | 53.4 ms                                                          | 61.2 ms: 1.14x slower                                                        |
| xml_etree_process          | 59.7 ms                                                          | 68.8 ms: 1.15x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 197 us: 1.16x slower                                                         |
| pylint                     | 339 ms                                                           | 394 ms: 1.16x slower                                                         |
| docutils                   | 2.98 sec                                                         | 3.47 sec: 1.16x slower                                                       |
| dulwich_log                | 67.3 ms                                                          | 78.3 ms: 1.16x slower                                                        |
| chameleon                  | 7.40 ms                                                          | 8.61 ms: 1.16x slower                                                        |
| genshi_xml                 | 58.1 ms                                                          | 67.7 ms: 1.17x slower                                                        |
| django_template            | 39.0 ms                                                          | 45.5 ms: 1.17x slower                                                        |
| sqlglot_normalize          | 120 ms                                                           | 141 ms: 1.17x slower                                                         |
| mypy2                      | 764 ms                                                           | 897 ms: 1.17x slower                                                         |
| html5lib                   | 74.7 ms                                                          | 88.0 ms: 1.18x slower                                                        |
| 2to3                       | 291 ms                                                           | 345 ms: 1.18x slower                                                         |
| pycparser                  | 1.22 sec                                                         | 1.45 sec: 1.18x slower                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 70.7 ms: 1.19x slower                                                        |
| float                      | 80.2 ms                                                          | 96.2 ms: 1.20x slower                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 4.07 us: 1.20x slower                                                        |
| tomli_loads                | 2.40 sec                                                         | 2.91 sec: 1.21x slower                                                       |
| sympy_integrate            | 23.2 ms                                                          | 28.1 ms: 1.21x slower                                                        |
| sympy_sum                  | 155 ms                                                           | 189 ms: 1.22x slower                                                         |
| go                         | 165 ms                                                           | 202 ms: 1.22x slower                                                         |
| sqlglot_transpile          | 1.76 ms                                                          | 2.20 ms: 1.24x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 1.74 ms: 1.25x slower                                                        |
| sympy_expand               | 501 ms                                                           | 628 ms: 1.25x slower                                                         |
| crypto_pyaes               | 73.6 ms                                                          | 92.4 ms: 1.26x slower                                                        |
| sympy_str                  | 295 ms                                                           | 371 ms: 1.26x slower                                                         |
| deepcopy                   | 377 us                                                           | 475 us: 1.26x slower                                                         |
| pprint_safe_repr           | 818 ms                                                           | 1.04 sec: 1.27x slower                                                       |
| pprint_pformat             | 1.66 sec                                                         | 2.11 sec: 1.27x slower                                                       |
| genshi_text                | 25.9 ms                                                          | 33.0 ms: 1.28x slower                                                        |
| raytrace                   | 260 ms                                                           | 338 ms: 1.30x slower                                                         |
| nqueens                    | 88.4 ms                                                          | 117 ms: 1.32x slower                                                         |
| pyflate                    | 482 ms                                                           | 637 ms: 1.32x slower                                                         |
| deltablue                  | 3.37 ms                                                          | 4.54 ms: 1.35x slower                                                        |
| chaos                      | 59.6 ms                                                          | 80.7 ms: 1.35x slower                                                        |
| fannkuch                   | 353 ms                                                           | 479 ms: 1.36x slower                                                         |
| unpickle_pure_python       | 224 us                                                           | 307 us: 1.37x slower                                                         |
| scimark_sor                | 119 ms                                                           | 163 ms: 1.37x slower                                                         |
| scimark_fft                | 312 ms                                                           | 433 ms: 1.39x slower                                                         |
| pickle_pure_python         | 307 us                                                           | 434 us: 1.41x slower                                                         |
| mako                       | 10.4 ms                                                          | 14.6 ms: 1.41x slower                                                        |
| nbody                      | 87.8 ms                                                          | 125 ms: 1.42x slower                                                         |
| scimark_lu                 | 97.5 ms                                                          | 145 ms: 1.48x slower                                                         |
| regex_compile              | 144 ms                                                           | 216 ms: 1.50x slower                                                         |
| spectral_norm              | 97.3 ms                                                          | 147 ms: 1.51x slower                                                         |
| scimark_monte_carlo        | 65.5 ms                                                          | 99.7 ms: 1.52x slower                                                        |
| deepcopy_memo              | 37.3 us                                                          | 57.7 us: 1.55x slower                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 6.80 ms: 1.59x slower                                                        |
| comprehensions             | 17.0 us                                                          | 27.6 us: 1.63x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 157 ns: 1.63x slower                                                         |
| hexiom                     | 6.35 ms                                                          | 10.6 ms: 1.67x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.17x slower                                                                 |

Benchmark hidden because not significant (5): coverage, pidigits, async_tree_io_tg, unpickle_list, bench_mp_pool
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: 1.01x