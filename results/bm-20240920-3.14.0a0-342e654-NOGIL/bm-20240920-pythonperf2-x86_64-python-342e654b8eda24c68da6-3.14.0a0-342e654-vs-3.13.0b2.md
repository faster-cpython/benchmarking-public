# Results vs. 3.13.0b2

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-x86_64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.38x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 423 ms: 1.45x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.38 sec: 1.13x slower                                                      |
| html5lib       | 74.7 ms                                                          | 107 ms: 1.43x slower                                                        |
| tornado_http   | 119 ms                                                           | 169 ms: 1.41x slower                                                        |
| Geometric mean | (ref)                                                            | 1.35x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 885 ms: 1.02x faster                                                        |
| async_tree_io              | 873 ms                                                           | 940 ms: 1.08x slower                                                        |
| async_tree_none_tg         | 340 ms                                                           | 367 ms: 1.08x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 631 ms: 1.10x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 469 ms: 1.11x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 675 ms: 1.12x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 515 ms: 1.12x slower                                                        |
| async_tree_none            | 365 ms                                                           | 416 ms: 1.14x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.09x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 250 ms: 1.02x faster                                                        |
| float          | 80.2 ms                                                          | 140 ms: 1.75x slower                                                        |
| nbody          | 87.8 ms                                                          | 194 ms: 2.21x slower                                                        |
| Geometric mean | (ref)                                                            | 1.56x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 236 ms: 1.06x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 27.0 ms: 1.04x slower                                                       |
| regex_compile  | 144 ms                                                           | 223 ms: 1.55x slower                                                        |
| Geometric mean | (ref)                                                            | 1.11x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                           | 140 ms: 1.02x faster                                                        |
| pickle               | 10.6 us                                                          | 10.4 us: 1.02x faster                                                       |
| pickle_dict          | 32.8 us                                                          | 32.2 us: 1.02x faster                                                       |
| pickle_list          | 4.44 us                                                          | 4.50 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 105 ms: 1.02x slower                                                        |
| unpickle             | 15.7 us                                                          | 16.8 us: 1.07x slower                                                       |
| unpickle_list        | 4.70 us                                                          | 5.29 us: 1.13x slower                                                       |
| json_loads           | 25.0 us                                                          | 29.0 us: 1.16x slower                                                       |
| json_dumps           | 10.8 ms                                                          | 14.0 ms: 1.30x slower                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 113 ms: 1.32x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 3.31 sec: 1.38x slower                                                      |
| xml_etree_process    | 59.7 ms                                                          | 91.9 ms: 1.54x slower                                                       |
| unpickle_pure_python | 224 us                                                           | 396 us: 1.77x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 585 us: 1.90x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.22x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 17.5 ms: 1.32x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 11.8 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.33x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 80.5 ms: 1.39x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 42.6 ms: 1.65x slower                                                       |
| django_template | 39.0 ms                                                          | 66.9 ms: 1.72x slower                                                       |
| mako            | 10.4 ms                                                          | 21.5 ms: 2.07x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.69x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.69 ms                                                          | 2.81 ms: 1.67x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.70 ms: 1.18x faster                                                       |
| regex_dna                  | 249 ms                                                           | 236 ms: 1.06x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 385 ms: 1.03x faster                                                        |
| xml_etree_parse            | 144 ms                                                           | 140 ms: 1.02x faster                                                        |
| pickle                     | 10.6 us                                                          | 10.4 us: 1.02x faster                                                       |
| pickle_dict                | 32.8 us                                                          | 32.2 us: 1.02x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 885 ms: 1.02x faster                                                        |
| pidigits                   | 254 ms                                                           | 250 ms: 1.02x faster                                                        |
| pickle_list                | 4.44 us                                                          | 4.50 us: 1.01x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 105 ms: 1.02x slower                                                        |
| regex_v8                   | 26.0 ms                                                          | 27.0 ms: 1.04x slower                                                       |
| sqlite_synth               | 2.80 us                                                          | 2.98 us: 1.07x slower                                                       |
| unpickle                   | 15.7 us                                                          | 16.8 us: 1.07x slower                                                       |
| async_tree_io              | 873 ms                                                           | 940 ms: 1.08x slower                                                        |
| async_tree_none_tg         | 340 ms                                                           | 367 ms: 1.08x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 631 ms: 1.10x slower                                                        |
| json                       | 5.35 ms                                                          | 5.93 ms: 1.11x slower                                                       |
| async_tree_memoization_tg  | 421 ms                                                           | 469 ms: 1.11x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 675 ms: 1.12x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 515 ms: 1.12x slower                                                        |
| unpickle_list              | 4.70 us                                                          | 5.29 us: 1.13x slower                                                       |
| deepcopy                   | 377 us                                                           | 424 us: 1.13x slower                                                        |
| docutils                   | 2.98 sec                                                         | 3.38 sec: 1.13x slower                                                      |
| async_tree_none            | 365 ms                                                           | 416 ms: 1.14x slower                                                        |
| pathlib                    | 17.1 ms                                                          | 19.6 ms: 1.14x slower                                                       |
| json_loads                 | 25.0 us                                                          | 29.0 us: 1.16x slower                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.86 sec: 1.18x slower                                                      |
| asyncio_tcp                | 378 ms                                                           | 457 ms: 1.21x slower                                                        |
| generators                 | 33.5 ms                                                          | 41.4 ms: 1.23x slower                                                       |
| telco                      | 8.40 ms                                                          | 10.4 ms: 1.24x slower                                                       |
| scimark_fft                | 312 ms                                                           | 388 ms: 1.24x slower                                                        |
| coroutines                 | 22.0 ms                                                          | 28.0 ms: 1.27x slower                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 6.54 sec: 1.27x slower                                                      |
| pylint                     | 339 ms                                                           | 436 ms: 1.29x slower                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 5.52 ms: 1.29x slower                                                       |
| meteor_contest             | 128 ms                                                           | 166 ms: 1.29x slower                                                        |
| deepcopy_memo              | 37.3 us                                                          | 48.4 us: 1.30x slower                                                       |
| coverage                   | 83.5 ms                                                          | 109 ms: 1.30x slower                                                        |
| json_dumps                 | 10.8 ms                                                          | 14.0 ms: 1.30x slower                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 113 ms: 1.32x slower                                                        |
| python_startup             | 13.2 ms                                                          | 17.5 ms: 1.32x slower                                                       |
| mdp                        | 2.46 sec                                                         | 3.26 sec: 1.32x slower                                                      |
| dulwich_log                | 67.3 ms                                                          | 89.2 ms: 1.33x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 11.8 ms: 1.33x slower                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 4.53 us: 1.34x slower                                                       |
| async_generators           | 363 ms                                                           | 488 ms: 1.34x slower                                                        |
| tomli_loads                | 2.40 sec                                                         | 3.31 sec: 1.38x slower                                                      |
| sympy_integrate            | 23.2 ms                                                          | 32.1 ms: 1.39x slower                                                       |
| genshi_xml                 | 58.1 ms                                                          | 80.5 ms: 1.39x slower                                                       |
| tornado_http               | 119 ms                                                           | 169 ms: 1.41x slower                                                        |
| pycparser                  | 1.22 sec                                                         | 1.74 sec: 1.42x slower                                                      |
| html5lib                   | 74.7 ms                                                          | 107 ms: 1.43x slower                                                        |
| nqueens                    | 88.4 ms                                                          | 128 ms: 1.45x slower                                                        |
| 2to3                       | 291 ms                                                           | 423 ms: 1.45x slower                                                        |
| sqlglot_normalize          | 120 ms                                                           | 180 ms: 1.49x slower                                                        |
| sympy_str                  | 295 ms                                                           | 447 ms: 1.52x slower                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 90.5 ms: 1.52x slower                                                       |
| richards                   | 53.4 ms                                                          | 81.4 ms: 1.52x slower                                                       |
| typing_runtime_protocols   | 171 us                                                           | 261 us: 1.53x slower                                                        |
| xml_etree_process          | 59.7 ms                                                          | 91.9 ms: 1.54x slower                                                       |
| thrift                     | 880 us                                                           | 1.36 ms: 1.54x slower                                                       |
| regex_compile              | 144 ms                                                           | 223 ms: 1.55x slower                                                        |
| pyflate                    | 482 ms                                                           | 767 ms: 1.59x slower                                                        |
| richards_super             | 61.2 ms                                                          | 97.4 ms: 1.59x slower                                                       |
| sympy_expand               | 501 ms                                                           | 807 ms: 1.61x slower                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 120 ms: 1.63x slower                                                        |
| genshi_text                | 25.9 ms                                                          | 42.6 ms: 1.65x slower                                                       |
| pprint_safe_repr           | 818 ms                                                           | 1.35 sec: 1.65x slower                                                      |
| sympy_sum                  | 155 ms                                                           | 259 ms: 1.67x slower                                                        |
| spectral_norm              | 97.3 ms                                                          | 164 ms: 1.69x slower                                                        |
| pprint_pformat             | 1.66 sec                                                         | 2.81 sec: 1.69x slower                                                      |
| django_template            | 39.0 ms                                                          | 66.9 ms: 1.72x slower                                                       |
| comprehensions             | 17.0 us                                                          | 29.3 us: 1.73x slower                                                       |
| logging_format             | 7.11 us                                                          | 12.4 us: 1.74x slower                                                       |
| float                      | 80.2 ms                                                          | 140 ms: 1.75x slower                                                        |
| fannkuch                   | 353 ms                                                           | 619 ms: 1.76x slower                                                        |
| unpickle_pure_python       | 224 us                                                           | 396 us: 1.77x slower                                                        |
| logging_simple             | 6.40 us                                                          | 11.5 us: 1.80x slower                                                       |
| hexiom                     | 6.35 ms                                                          | 11.5 ms: 1.81x slower                                                       |
| go                         | 165 ms                                                           | 301 ms: 1.82x slower                                                        |
| bench_thread_pool          | 908 us                                                           | 1.66 ms: 1.82x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 3.35 ms: 1.90x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 585 us: 1.90x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 187 ns: 1.94x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 131 ms: 2.00x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 2.83 ms: 2.03x slower                                                       |
| chaos                      | 59.6 ms                                                          | 122 ms: 2.05x slower                                                        |
| mako                       | 10.4 ms                                                          | 21.5 ms: 2.07x slower                                                       |
| scimark_sor                | 119 ms                                                           | 258 ms: 2.17x slower                                                        |
| nbody                      | 87.8 ms                                                          | 194 ms: 2.21x slower                                                        |
| scimark_lu                 | 97.5 ms                                                          | 217 ms: 2.23x slower                                                        |
| raytrace                   | 260 ms                                                           | 605 ms: 2.33x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 8.17 ms: 2.42x slower                                                       |
| Geometric mean             | (ref)                                                            | 1.38x slower                                                                |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-342e654-NOGIL/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.32x
- 95% likely to have a slowdown of 1.30x
- 99% likely to have a slowdown of 1.27x

# Memory
- memory change: 1.16x