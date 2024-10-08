# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a2
- machine: windows-amd64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 210 ms: 1.01x slower                                            |
| docutils       | 1.63 sec                                                        | 1.55 sec: 1.05x faster                                          |
| html5lib       | 35.0 ms                                                         | 36.6 ms: 1.04x slower                                           |
| tornado_http   | 81.8 ms                                                         | 86.1 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                    |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 389 ms                                                          | 453 ms: 1.16x slower                                            |
| async_tree_none            | 218 ms                                                          | 264 ms: 1.21x slower                                            |
| async_tree_io              | 588 ms                                                          | 731 ms: 1.24x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 482 ms: 1.26x slower                                            |
| async_tree_io_tg           | 605 ms                                                          | 769 ms: 1.27x slower                                            |
| async_tree_memoization     | 264 ms                                                          | 341 ms: 1.29x slower                                            |
| async_tree_none_tg         | 202 ms                                                          | 281 ms: 1.39x slower                                            |
| async_tree_memoization_tg  | 258 ms                                                          | 361 ms: 1.40x slower                                            |
| Geometric mean             | (ref)                                                           | 1.28x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 147 ms: 1.02x faster                                            |
| float          | 49.7 ms                                                         | 52.3 ms: 1.05x slower                                           |
| nbody          | 67.6 ms                                                         | 72.0 ms: 1.06x slower                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 78.0 ms                                                         | 78.9 ms: 1.01x slower                                           |
| regex_effbot   | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                           |
| regex_dna      | 119 ms                                                          | 122 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                           | 1.01x slower                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 13.4 us: 1.06x faster                                           |
| unpickle             | 8.40 us                                                         | 8.09 us: 1.04x faster                                           |
| pickle_list          | 2.90 us                                                         | 2.83 us: 1.03x faster                                           |
| pickle               | 7.11 us                                                         | 6.94 us: 1.02x faster                                           |
| json_dumps           | 5.61 ms                                                         | 5.50 ms: 1.02x faster                                           |
| tomli_loads          | 1.35 sec                                                        | 1.37 sec: 1.01x slower                                          |
| xml_etree_parse      | 90.9 ms                                                         | 92.3 ms: 1.01x slower                                           |
| pickle_pure_python   | 175 us                                                          | 179 us: 1.02x slower                                            |
| unpickle_list        | 2.62 us                                                         | 2.70 us: 1.03x slower                                           |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.5 ms: 1.03x slower                                           |
| unpickle_pure_python | 122 us                                                          | 128 us: 1.05x slower                                            |
| pickle_dict          | 18.1 us                                                         | 19.1 us: 1.05x slower                                           |
| Geometric mean       | (ref)                                                           | 1.00x slower                                                    |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 19.9 ms: 1.02x faster                                           |
| python_startup_no_site | 16.2 ms                                                         | 17.6 ms: 1.09x slower                                           |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 21.9 ms: 1.01x slower                                           |
| mako            | 6.36 ms                                                         | 6.48 ms: 1.02x slower                                           |
| genshi_text     | 14.4 ms                                                         | 15.0 ms: 1.04x slower                                           |
| genshi_xml      | 31.6 ms                                                         | 33.1 ms: 1.05x slower                                           |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols   | 101 us                                                          | 73.9 us: 1.37x faster                                           |
| create_gc_cycles           | 888 us                                                          | 746 us: 1.19x faster                                            |
| json                       | 3.19 ms                                                         | 2.85 ms: 1.12x faster                                           |
| json_loads                 | 14.2 us                                                         | 13.4 us: 1.06x faster                                           |
| crypto_pyaes               | 45.5 ms                                                         | 43.3 ms: 1.05x faster                                           |
| docutils                   | 1.63 sec                                                        | 1.55 sec: 1.05x faster                                          |
| unpickle                   | 8.40 us                                                         | 8.09 us: 1.04x faster                                           |
| pickle_list                | 2.90 us                                                         | 2.83 us: 1.03x faster                                           |
| sympy_sum                  | 84.4 ms                                                         | 82.3 ms: 1.03x faster                                           |
| pickle                     | 7.11 us                                                         | 6.94 us: 1.02x faster                                           |
| gc_traversal               | 1.55 ms                                                         | 1.52 ms: 1.02x faster                                           |
| sqlite_synth               | 1.60 us                                                         | 1.56 us: 1.02x faster                                           |
| deepcopy_reduce            | 1.99 us                                                         | 1.95 us: 1.02x faster                                           |
| telco                      | 4.67 ms                                                         | 4.57 ms: 1.02x faster                                           |
| json_dumps                 | 5.61 ms                                                         | 5.50 ms: 1.02x faster                                           |
| pidigits                   | 150 ms                                                          | 147 ms: 1.02x faster                                            |
| python_startup             | 20.3 ms                                                         | 19.9 ms: 1.02x faster                                           |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.46 ms: 1.02x faster                                           |
| sympy_str                  | 159 ms                                                          | 156 ms: 1.02x faster                                            |
| bench_mp_pool              | 64.8 ms                                                         | 64.0 ms: 1.01x faster                                           |
| sqlglot_normalize          | 173 ms                                                          | 171 ms: 1.01x faster                                            |
| fannkuch                   | 243 ms                                                          | 241 ms: 1.01x faster                                            |
| sqlglot_optimize           | 32.7 ms                                                         | 32.5 ms: 1.01x faster                                           |
| deepcopy                   | 220 us                                                          | 218 us: 1.01x faster                                            |
| sympy_expand               | 271 ms                                                          | 269 ms: 1.01x faster                                            |
| sympy_integrate            | 12.2 ms                                                         | 12.2 ms: 1.01x faster                                           |
| sqlglot_parse              | 748 us                                                          | 752 us: 1.00x slower                                            |
| pprint_safe_repr           | 474 ms                                                          | 479 ms: 1.01x slower                                            |
| sqlglot_transpile          | 955 us                                                          | 965 us: 1.01x slower                                            |
| regex_compile              | 78.0 ms                                                         | 78.9 ms: 1.01x slower                                           |
| django_template            | 21.7 ms                                                         | 21.9 ms: 1.01x slower                                           |
| tomli_loads                | 1.35 sec                                                        | 1.37 sec: 1.01x slower                                          |
| pprint_pformat             | 966 ms                                                          | 979 ms: 1.01x slower                                            |
| 2to3                       | 207 ms                                                          | 210 ms: 1.01x slower                                            |
| xml_etree_parse            | 90.9 ms                                                         | 92.3 ms: 1.01x slower                                           |
| async_generators           | 223 ms                                                          | 227 ms: 1.02x slower                                            |
| pickle_pure_python         | 175 us                                                          | 179 us: 1.02x slower                                            |
| mako                       | 6.36 ms                                                         | 6.48 ms: 1.02x slower                                           |
| richards_super             | 30.2 ms                                                         | 30.8 ms: 1.02x slower                                           |
| hexiom                     | 3.72 ms                                                         | 3.81 ms: 1.02x slower                                           |
| chaos                      | 38.4 ms                                                         | 39.2 ms: 1.02x slower                                           |
| logging_silent             | 52.9 ns                                                         | 54.1 ns: 1.02x slower                                           |
| generators                 | 19.6 ms                                                         | 20.0 ms: 1.02x slower                                           |
| richards                   | 26.7 ms                                                         | 27.3 ms: 1.02x slower                                           |
| regex_effbot               | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                           |
| nqueens                    | 56.7 ms                                                         | 58.2 ms: 1.03x slower                                           |
| go                         | 82.1 ms                                                         | 84.3 ms: 1.03x slower                                           |
| thrift                     | 8.11 ms                                                         | 8.35 ms: 1.03x slower                                           |
| regex_dna                  | 119 ms                                                          | 122 ms: 1.03x slower                                            |
| unpickle_list              | 2.62 us                                                         | 2.70 us: 1.03x slower                                           |
| xml_etree_iterparse        | 62.3 ms                                                         | 64.5 ms: 1.03x slower                                           |
| mdp                        | 1.31 sec                                                        | 1.36 sec: 1.03x slower                                          |
| coroutines                 | 12.8 ms                                                         | 13.2 ms: 1.04x slower                                           |
| meteor_contest             | 69.9 ms                                                         | 72.6 ms: 1.04x slower                                           |
| pyflate                    | 279 ms                                                          | 291 ms: 1.04x slower                                            |
| genshi_text                | 14.4 ms                                                         | 15.0 ms: 1.04x slower                                           |
| scimark_monte_carlo        | 39.1 ms                                                         | 40.9 ms: 1.04x slower                                           |
| html5lib                   | 35.0 ms                                                         | 36.6 ms: 1.04x slower                                           |
| logging_format             | 6.22 us                                                         | 6.51 us: 1.05x slower                                           |
| unpickle_pure_python       | 122 us                                                          | 128 us: 1.05x slower                                            |
| genshi_xml                 | 31.6 ms                                                         | 33.1 ms: 1.05x slower                                           |
| logging_simple             | 5.78 us                                                         | 6.07 us: 1.05x slower                                           |
| pickle_dict                | 18.1 us                                                         | 19.1 us: 1.05x slower                                           |
| float                      | 49.7 ms                                                         | 52.3 ms: 1.05x slower                                           |
| tornado_http               | 81.8 ms                                                         | 86.1 ms: 1.05x slower                                           |
| pathlib                    | 75.9 ms                                                         | 79.9 ms: 1.05x slower                                           |
| deepcopy_memo              | 22.1 us                                                         | 23.5 us: 1.06x slower                                           |
| nbody                      | 67.6 ms                                                         | 72.0 ms: 1.06x slower                                           |
| deltablue                  | 1.88 ms                                                         | 2.01 ms: 1.07x slower                                           |
| scimark_fft                | 171 ms                                                          | 184 ms: 1.08x slower                                            |
| python_startup_no_site     | 16.2 ms                                                         | 17.6 ms: 1.09x slower                                           |
| dulwich_log                | 38.0 ms                                                         | 41.4 ms: 1.09x slower                                           |
| coverage                   | 42.1 ms                                                         | 45.8 ms: 1.09x slower                                           |
| bench_thread_pool          | 768 us                                                          | 848 us: 1.10x slower                                            |
| scimark_sor                | 75.3 ms                                                         | 85.4 ms: 1.13x slower                                           |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 453 ms: 1.16x slower                                            |
| async_tree_none            | 218 ms                                                          | 264 ms: 1.21x slower                                            |
| async_tree_io              | 588 ms                                                          | 731 ms: 1.24x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 482 ms: 1.26x slower                                            |
| async_tree_io_tg           | 605 ms                                                          | 769 ms: 1.27x slower                                            |
| async_tree_memoization     | 264 ms                                                          | 341 ms: 1.29x slower                                            |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 2.02 sec: 1.36x slower                                          |
| async_tree_none_tg         | 202 ms                                                          | 281 ms: 1.39x slower                                            |
| mypy2                      | 418 ms                                                          | 584 ms: 1.40x slower                                            |
| async_tree_memoization_tg  | 258 ms                                                          | 361 ms: 1.40x slower                                            |
| Geometric mean             | (ref)                                                           | 1.03x slower                                                    |

Benchmark hidden because not significant (13): pycparser, regex_v8, asyncio_tcp, pylint, comprehensions, scimark_lu, spectral_norm, flaskblogging, xml_etree_process, xml_etree_generate, aiohttp, chameleon, raytrace

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown