# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_likely
- machine: linux-x86_64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.08x slower
- HPT reliability: 66.82%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 314 ms: 1.08x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.21 sec: 1.08x slower                                                      |
| html5lib       | 74.7 ms                                                          | 70.7 ms: 1.06x faster                                                       |
| tornado_http   | 119 ms                                                           | 123 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                            | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 421 ms                                                           | 377 ms: 1.12x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 412 ms: 1.11x faster                                                        |
| async_tree_none            | 365 ms                                                           | 332 ms: 1.10x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 321 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 577 ms: 1.05x faster                                                        |
| async_tree_io              | 873 ms                                                           | 836 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 863 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 560 ms: 1.02x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.07x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 83.3 ms: 1.05x faster                                                       |
| float          | 80.2 ms                                                          | 79.3 ms: 1.01x faster                                                       |
| pidigits       | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 247 ms: 1.01x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.51 ms: 1.03x slower                                                       |
| regex_v8       | 26.0 ms                                                          | 26.9 ms: 1.03x slower                                                       |
| regex_compile  | 144 ms                                                           | 152 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                            | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|---------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads         | 2.40 sec                                                         | 2.15 sec: 1.12x faster                                                      |
| xml_etree_generate  | 85.7 ms                                                          | 82.0 ms: 1.05x faster                                                       |
| pickle_dict         | 32.8 us                                                          | 31.7 us: 1.04x faster                                                       |
| json_loads          | 25.0 us                                                          | 24.3 us: 1.03x faster                                                       |
| xml_etree_iterparse | 103 ms                                                           | 100.0 ms: 1.03x faster                                                      |
| xml_etree_process   | 59.7 ms                                                          | 58.6 ms: 1.02x faster                                                       |
| unpickle            | 15.7 us                                                          | 15.4 us: 1.02x faster                                                       |
| pickle              | 10.6 us                                                          | 10.7 us: 1.01x slower                                                       |
| pickle_list         | 4.44 us                                                          | 4.60 us: 1.03x slower                                                       |
| json_dumps          | 10.8 ms                                                          | 11.2 ms: 1.04x slower                                                       |
| pickle_pure_python  | 307 us                                                           | 337 us: 1.10x slower                                                        |
| Geometric mean      | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (3): unpickle_list, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.98 ms: 1.01x slower                                                       |
| python_startup         | 13.2 ms                                                          | 14.9 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.39 ms: 1.10x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 28.3 ms: 1.09x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 65.1 ms: 1.12x slower                                                       |
| django_template | 39.0 ms                                                          | 43.9 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| richards_super             | 61.2 ms                                                          | 48.9 ms: 1.25x faster                                                       |
| deepcopy_memo              | 37.3 us                                                          | 29.9 us: 1.25x faster                                                       |
| richards                   | 53.4 ms                                                          | 43.7 ms: 1.22x faster                                                       |
| deepcopy                   | 377 us                                                           | 313 us: 1.21x faster                                                        |
| scimark_sor                | 119 ms                                                           | 103 ms: 1.15x faster                                                        |
| tomli_loads                | 2.40 sec                                                         | 2.15 sec: 1.12x faster                                                      |
| async_tree_memoization_tg  | 421 ms                                                           | 377 ms: 1.12x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 412 ms: 1.11x faster                                                        |
| mako                       | 10.4 ms                                                          | 9.39 ms: 1.10x faster                                                       |
| async_tree_none            | 365 ms                                                           | 332 ms: 1.10x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 3.11 us: 1.09x faster                                                       |
| go                         | 165 ms                                                           | 151 ms: 1.09x faster                                                        |
| telco                      | 8.40 ms                                                          | 7.73 ms: 1.09x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 15.9 ms: 1.08x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.77 sec: 1.08x faster                                                      |
| scimark_fft                | 312 ms                                                           | 291 ms: 1.07x faster                                                        |
| logging_silent             | 96.3 ns                                                          | 90.8 ns: 1.06x faster                                                       |
| async_tree_none_tg         | 340 ms                                                           | 321 ms: 1.06x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 70.7 ms: 1.06x faster                                                       |
| nbody                      | 87.8 ms                                                          | 83.3 ms: 1.05x faster                                                       |
| json                       | 5.35 ms                                                          | 5.10 ms: 1.05x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 92.8 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 577 ms: 1.05x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 82.0 ms: 1.05x faster                                                       |
| dulwich_log                | 67.3 ms                                                          | 64.4 ms: 1.05x faster                                                       |
| async_tree_io              | 873 ms                                                           | 836 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 863 ms: 1.04x faster                                                        |
| scimark_lu                 | 97.5 ms                                                          | 93.9 ms: 1.04x faster                                                       |
| pickle_dict                | 32.8 us                                                          | 31.7 us: 1.04x faster                                                       |
| asyncio_websockets         | 395 ms                                                           | 381 ms: 1.04x faster                                                        |
| pyflate                    | 482 ms                                                           | 467 ms: 1.03x faster                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 71.5 ms: 1.03x faster                                                       |
| json_loads                 | 25.0 us                                                          | 24.3 us: 1.03x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 100.0 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 560 ms: 1.02x faster                                                        |
| deltablue                  | 3.37 ms                                                          | 3.31 ms: 1.02x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 58.6 ms: 1.02x faster                                                       |
| sqlite_synth               | 2.80 us                                                          | 2.74 us: 1.02x faster                                                       |
| unpickle                   | 15.7 us                                                          | 15.4 us: 1.02x faster                                                       |
| pprint_safe_repr           | 818 ms                                                           | 807 ms: 1.01x faster                                                        |
| float                      | 80.2 ms                                                          | 79.3 ms: 1.01x faster                                                       |
| coroutines                 | 22.0 ms                                                          | 21.8 ms: 1.01x faster                                                       |
| pidigits                   | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| regex_dna                  | 249 ms                                                           | 247 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.59 sec: 1.00x slower                                                      |
| pickle                     | 10.6 us                                                          | 10.7 us: 1.01x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 8.98 ms: 1.01x slower                                                       |
| thrift                     | 880 us                                                           | 899 us: 1.02x slower                                                        |
| meteor_contest             | 128 ms                                                           | 131 ms: 1.02x slower                                                        |
| tornado_http               | 119 ms                                                           | 123 ms: 1.03x slower                                                        |
| fannkuch                   | 353 ms                                                           | 364 ms: 1.03x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.51 ms: 1.03x slower                                                       |
| regex_v8                   | 26.0 ms                                                          | 26.9 ms: 1.03x slower                                                       |
| pickle_list                | 4.44 us                                                          | 4.60 us: 1.03x slower                                                       |
| logging_simple             | 6.40 us                                                          | 6.63 us: 1.04x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.27 sec: 1.04x slower                                                      |
| json_dumps                 | 10.8 ms                                                          | 11.2 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.47 ms: 1.04x slower                                                       |
| typing_runtime_protocols   | 171 us                                                           | 178 us: 1.05x slower                                                        |
| bench_thread_pool          | 908 us                                                           | 952 us: 1.05x slower                                                        |
| regex_compile              | 144 ms                                                           | 152 ms: 1.06x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.60 sec: 1.06x slower                                                      |
| scimark_monte_carlo        | 65.5 ms                                                          | 69.6 ms: 1.06x slower                                                       |
| sympy_expand               | 501 ms                                                           | 534 ms: 1.07x slower                                                        |
| async_generators           | 363 ms                                                           | 388 ms: 1.07x slower                                                        |
| docutils                   | 2.98 sec                                                         | 3.21 sec: 1.08x slower                                                      |
| 2to3                       | 291 ms                                                           | 314 ms: 1.08x slower                                                        |
| genshi_text                | 25.9 ms                                                          | 28.3 ms: 1.09x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.52 ms: 1.09x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 337 us: 1.10x slower                                                        |
| sympy_str                  | 295 ms                                                           | 324 ms: 1.10x slower                                                        |
| gc_traversal               | 4.69 ms                                                          | 5.21 ms: 1.11x slower                                                       |
| comprehensions             | 17.0 us                                                          | 18.9 us: 1.11x slower                                                       |
| sqlglot_normalize          | 120 ms                                                           | 134 ms: 1.11x slower                                                        |
| genshi_xml                 | 58.1 ms                                                          | 65.1 ms: 1.12x slower                                                       |
| chaos                      | 59.6 ms                                                          | 67.0 ms: 1.12x slower                                                       |
| django_template            | 39.0 ms                                                          | 43.9 ms: 1.13x slower                                                       |
| hexiom                     | 6.35 ms                                                          | 7.16 ms: 1.13x slower                                                       |
| python_startup             | 13.2 ms                                                          | 14.9 ms: 1.13x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 2.01 ms: 1.14x slower                                                       |
| sympy_sum                  | 155 ms                                                           | 176 ms: 1.14x slower                                                        |
| generators                 | 33.5 ms                                                          | 38.3 ms: 1.14x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 103 ms: 1.17x slower                                                        |
| raytrace                   | 260 ms                                                           | 307 ms: 1.18x slower                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 70.3 ms: 1.18x slower                                                       |
| sympy_integrate            | 23.2 ms                                                          | 27.6 ms: 1.19x slower                                                       |
| pylint                     | 339 ms                                                           | 422 ms: 1.24x slower                                                        |
| create_gc_cycles           | 2.00 ms                                                          | 2.89 ms: 1.44x slower                                                       |
| bench_mp_pool              | 4.91 ms                                                          | 3.16 sec: 644.03x slower                                                    |
| Geometric mean             | (ref)                                                            | 1.08x slower                                                                |

Benchmark hidden because not significant (7): coverage, pprint_pformat, unpickle_list, asyncio_tcp, xml_etree_parse, logging_format, unpickle_pure_python
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 66.82% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.19x