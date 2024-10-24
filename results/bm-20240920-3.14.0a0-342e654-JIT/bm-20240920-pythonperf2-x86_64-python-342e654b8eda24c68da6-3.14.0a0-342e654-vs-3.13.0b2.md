# Results vs. 3.13.0b2

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-x86_64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.01x faster
- HPT reliability: 87.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 310 ms: 1.06x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.16 sec: 1.06x slower                                                      |
| html5lib       | 74.7 ms                                                          | 70.3 ms: 1.06x faster                                                       |
| tornado_http   | 119 ms                                                           | 121 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.14x faster                                                        |
| async_tree_none            | 365 ms                                                           | 320 ms: 1.14x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 801 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 308 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 801 ms: 1.09x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 390 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 574 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 544 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 73.7 ms: 1.09x faster                                                       |
| nbody          | 87.8 ms                                                          | 81.1 ms: 1.08x faster                                                       |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 235 ms: 1.06x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.3 ms: 1.03x faster                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.46 ms: 1.02x slower                                                       |
| regex_compile  | 144 ms                                                           | 147 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.12 sec: 1.13x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 78.7 ms: 1.09x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 55.8 ms: 1.07x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 213 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 98.3 ms: 1.04x faster                                                       |
| unpickle             | 15.7 us                                                          | 15.4 us: 1.02x faster                                                       |
| json_loads           | 25.0 us                                                          | 24.7 us: 1.01x faster                                                       |
| pickle_dict          | 32.8 us                                                          | 32.4 us: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 143 ms: 1.00x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| unpickle_list        | 4.70 us                                                          | 4.75 us: 1.01x slower                                                       |
| pickle_list          | 4.44 us                                                          | 4.51 us: 1.01x slower                                                       |
| pickle               | 10.6 us                                                          | 10.8 us: 1.02x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 328 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 8.97 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.10 ms: 1.14x faster                                                       |
| genshi_xml      | 58.1 ms                                                          | 62.3 ms: 1.07x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 28.3 ms: 1.09x slower                                                       |
| django_template | 39.0 ms                                                          | 43.1 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 26.9 us: 1.39x faster                                                       |
| deepcopy                   | 377 us                                                           | 289 us: 1.30x faster                                                        |
| richards                   | 53.4 ms                                                          | 44.9 ms: 1.19x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 82.3 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 2.88 us: 1.18x faster                                                       |
| richards_super             | 61.2 ms                                                          | 52.9 ms: 1.16x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.14x faster                                                        |
| scimark_sor                | 119 ms                                                           | 104 ms: 1.14x faster                                                        |
| async_tree_none            | 365 ms                                                           | 320 ms: 1.14x faster                                                        |
| mako                       | 10.4 ms                                                          | 9.10 ms: 1.14x faster                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.12 sec: 1.13x faster                                                      |
| async_tree_io_tg           | 900 ms                                                           | 801 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 308 ms: 1.10x faster                                                        |
| scimark_fft                | 312 ms                                                           | 283 ms: 1.10x faster                                                        |
| go                         | 165 ms                                                           | 151 ms: 1.09x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 15.7 ms: 1.09x faster                                                       |
| async_tree_io              | 873 ms                                                           | 801 ms: 1.09x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 78.7 ms: 1.09x faster                                                       |
| float                      | 80.2 ms                                                          | 73.7 ms: 1.09x faster                                                       |
| nbody                      | 87.8 ms                                                          | 81.1 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 3.96 ms: 1.08x faster                                                       |
| async_tree_memoization_tg  | 421 ms                                                           | 390 ms: 1.08x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 4.78 sec: 1.08x faster                                                      |
| xml_etree_process          | 59.7 ms                                                          | 55.8 ms: 1.07x faster                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.40 ms: 1.06x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 70.3 ms: 1.06x faster                                                       |
| regex_dna                  | 249 ms                                                           | 235 ms: 1.06x faster                                                        |
| deltablue                  | 3.37 ms                                                          | 3.19 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 574 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 544 ms: 1.05x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 213 us: 1.05x faster                                                        |
| create_gc_cycles           | 2.00 ms                                                          | 1.91 ms: 1.05x faster                                                       |
| telco                      | 8.40 ms                                                          | 8.05 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 98.3 ms: 1.04x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 70.6 ms: 1.04x faster                                                       |
| dulwich_log                | 67.3 ms                                                          | 64.6 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 818 ms                                                           | 789 ms: 1.04x faster                                                        |
| pyflate                    | 482 ms                                                           | 465 ms: 1.04x faster                                                        |
| coverage                   | 83.5 ms                                                          | 81.1 ms: 1.03x faster                                                       |
| json                       | 5.35 ms                                                          | 5.20 ms: 1.03x faster                                                       |
| sqlite_synth               | 2.80 us                                                          | 2.72 us: 1.03x faster                                                       |
| regex_v8                   | 26.0 ms                                                          | 25.3 ms: 1.03x faster                                                       |
| coroutines                 | 22.0 ms                                                          | 21.4 ms: 1.03x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.62 sec: 1.03x faster                                                      |
| unpickle                   | 15.7 us                                                          | 15.4 us: 1.02x faster                                                       |
| pidigits                   | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| json_loads                 | 25.0 us                                                          | 24.7 us: 1.01x faster                                                       |
| pickle_dict                | 32.8 us                                                          | 32.4 us: 1.01x faster                                                       |
| scimark_lu                 | 97.5 ms                                                          | 96.5 ms: 1.01x faster                                                       |
| asyncio_websockets         | 395 ms                                                           | 391 ms: 1.01x faster                                                        |
| xml_etree_parse            | 144 ms                                                           | 143 ms: 1.00x faster                                                        |
| json_dumps                 | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| unpickle_list              | 4.70 us                                                          | 4.75 us: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| tornado_http               | 119 ms                                                           | 121 ms: 1.01x slower                                                        |
| pickle_list                | 4.44 us                                                          | 4.51 us: 1.01x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 8.97 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.60 sec: 1.01x slower                                                      |
| regex_effbot               | 3.40 ms                                                          | 3.46 ms: 1.02x slower                                                       |
| regex_compile              | 144 ms                                                           | 147 ms: 1.02x slower                                                        |
| pickle                     | 10.6 us                                                          | 10.8 us: 1.02x slower                                                       |
| thrift                     | 880 us                                                           | 896 us: 1.02x slower                                                        |
| logging_simple             | 6.40 us                                                          | 6.54 us: 1.02x slower                                                       |
| meteor_contest             | 128 ms                                                           | 131 ms: 1.02x slower                                                        |
| fannkuch                   | 353 ms                                                           | 361 ms: 1.02x slower                                                        |
| bench_thread_pool          | 908 us                                                           | 939 us: 1.03x slower                                                        |
| pycparser                  | 1.22 sec                                                         | 1.28 sec: 1.05x slower                                                      |
| sympy_expand               | 501 ms                                                           | 524 ms: 1.05x slower                                                        |
| sympy_str                  | 295 ms                                                           | 309 ms: 1.05x slower                                                        |
| async_generators           | 363 ms                                                           | 380 ms: 1.05x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 179 us: 1.05x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.59 sec: 1.05x slower                                                      |
| logging_silent             | 96.3 ns                                                          | 102 ns: 1.06x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 69.2 ms: 1.06x slower                                                       |
| docutils                   | 2.98 sec                                                         | 3.16 sec: 1.06x slower                                                      |
| 2to3                       | 291 ms                                                           | 310 ms: 1.06x slower                                                        |
| pickle_pure_python         | 307 us                                                           | 328 us: 1.07x slower                                                        |
| comprehensions             | 17.0 us                                                          | 18.1 us: 1.07x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.48 ms: 1.07x slower                                                       |
| sqlglot_normalize          | 120 ms                                                           | 129 ms: 1.07x slower                                                        |
| genshi_xml                 | 58.1 ms                                                          | 62.3 ms: 1.07x slower                                                       |
| sympy_sum                  | 155 ms                                                           | 168 ms: 1.08x slower                                                        |
| genshi_text                | 25.9 ms                                                          | 28.3 ms: 1.09x slower                                                       |
| hexiom                     | 6.35 ms                                                          | 6.95 ms: 1.09x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 97.2 ms: 1.10x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.94 ms: 1.10x slower                                                       |
| generators                 | 33.5 ms                                                          | 36.9 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 65.6 ms: 1.10x slower                                                       |
| django_template            | 39.0 ms                                                          | 43.1 ms: 1.11x slower                                                       |
| chaos                      | 59.6 ms                                                          | 66.6 ms: 1.12x slower                                                       |
| sympy_integrate            | 23.2 ms                                                          | 26.3 ms: 1.13x slower                                                       |
| pylint                     | 339 ms                                                           | 409 ms: 1.21x slower                                                        |
| raytrace                   | 260 ms                                                           | 316 ms: 1.21x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (3): asyncio_tcp, logging_format, bench_mp_pool
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: unpack_sequence

# HPT report

- Reliability score: 87.81% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x