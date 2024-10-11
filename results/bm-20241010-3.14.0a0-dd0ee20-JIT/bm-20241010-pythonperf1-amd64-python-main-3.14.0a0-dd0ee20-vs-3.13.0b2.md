# Results vs. 3.13.0b2

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: dd0ee20
- commit date: 2024-10-10
- overall geometric mean: 1.20x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 283 ms: 1.37x slower                                       |
| docutils       | 1.63 sec                                                        | 2.17 sec: 1.34x slower                                     |
| html5lib       | 35.0 ms                                                         | 46.3 ms: 1.32x slower                                      |
| tornado_http   | 81.8 ms                                                         | 106 ms: 1.30x slower                                       |
| Geometric mean | (ref)                                                           | 1.33x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 633 ms: 1.05x slower                                       |
| async_tree_io              | 588 ms                                                          | 639 ms: 1.09x slower                                       |
| async_tree_none            | 218 ms                                                          | 238 ms: 1.09x slower                                       |
| async_tree_memoization_tg  | 258 ms                                                          | 288 ms: 1.12x slower                                       |
| async_tree_memoization     | 264 ms                                                          | 298 ms: 1.13x slower                                       |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 446 ms: 1.15x slower                                       |
| async_tree_none_tg         | 202 ms                                                          | 231 ms: 1.15x slower                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 442 ms: 1.16x slower                                       |
| Geometric mean             | (ref)                                                           | 1.11x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 48.1 ms: 1.41x faster                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                       |
| float          | 49.7 ms                                                         | 54.6 ms: 1.10x slower                                      |
| Geometric mean | (ref)                                                           | 1.09x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 115 ms: 1.04x faster                                       |
| regex_effbot   | 1.58 ms                                                         | 1.85 ms: 1.17x slower                                      |
| regex_compile  | 78.0 ms                                                         | 107 ms: 1.37x slower                                       |
| Geometric mean | (ref)                                                           | 1.13x slower                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.47 sec: 1.09x slower                                     |
| unpickle_list        | 2.62 us                                                         | 3.07 us: 1.17x slower                                      |
| xml_etree_parse      | 90.9 ms                                                         | 109 ms: 1.20x slower                                       |
| pickle               | 7.11 us                                                         | 8.55 us: 1.20x slower                                      |
| xml_etree_generate   | 53.2 ms                                                         | 64.6 ms: 1.22x slower                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 76.0 ms: 1.22x slower                                      |
| pickle_list          | 2.90 us                                                         | 3.56 us: 1.22x slower                                      |
| pickle_dict          | 18.1 us                                                         | 22.9 us: 1.26x slower                                      |
| xml_etree_process    | 36.4 ms                                                         | 46.7 ms: 1.28x slower                                      |
| unpickle             | 8.40 us                                                         | 11.4 us: 1.35x slower                                      |
| json_dumps           | 5.61 ms                                                         | 7.69 ms: 1.37x slower                                      |
| pickle_pure_python   | 175 us                                                          | 251 us: 1.43x slower                                       |
| json_loads           | 14.2 us                                                         | 21.2 us: 1.49x slower                                      |
| unpickle_pure_python | 122 us                                                          | 207 us: 1.70x slower                                       |
| Geometric mean       | (ref)                                                           | 1.29x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 24.2 ms: 1.19x slower                                      |
| python_startup_no_site | 16.2 ms                                                         | 19.9 ms: 1.23x slower                                      |
| Geometric mean         | (ref)                                                           | 1.21x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.17 ms: 1.03x faster                                      |
| genshi_text     | 14.4 ms                                                         | 21.4 ms: 1.49x slower                                      |
| django_template | 21.7 ms                                                         | 32.7 ms: 1.51x slower                                      |
| genshi_xml      | 31.6 ms                                                         | 50.1 ms: 1.59x slower                                      |
| Geometric mean  | (ref)                                                           | 1.36x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 656 us: 12.37x faster                                      |
| nbody                      | 67.6 ms                                                         | 48.1 ms: 1.41x faster                                      |
| deepcopy_memo              | 22.1 us                                                         | 18.6 us: 1.19x faster                                      |
| spectral_norm              | 63.7 ms                                                         | 58.8 ms: 1.08x faster                                      |
| regex_dna                  | 119 ms                                                          | 115 ms: 1.04x faster                                       |
| mako                       | 6.36 ms                                                         | 6.17 ms: 1.03x faster                                      |
| deepcopy                   | 220 us                                                          | 214 us: 1.03x faster                                       |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.43 ms: 1.03x faster                                      |
| pidigits                   | 150 ms                                                          | 149 ms: 1.00x faster                                       |
| async_tree_io_tg           | 605 ms                                                          | 633 ms: 1.05x slower                                       |
| scimark_fft                | 171 ms                                                          | 179 ms: 1.05x slower                                       |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.57 sec: 1.06x slower                                     |
| scimark_sor                | 75.3 ms                                                         | 80.7 ms: 1.07x slower                                      |
| crypto_pyaes               | 45.5 ms                                                         | 49.0 ms: 1.08x slower                                      |
| pathlib                    | 75.9 ms                                                         | 82.0 ms: 1.08x slower                                      |
| async_tree_io              | 588 ms                                                          | 639 ms: 1.09x slower                                       |
| tomli_loads                | 1.35 sec                                                        | 1.47 sec: 1.09x slower                                     |
| async_tree_none            | 218 ms                                                          | 238 ms: 1.09x slower                                       |
| float                      | 49.7 ms                                                         | 54.6 ms: 1.10x slower                                      |
| sqlite_synth               | 1.60 us                                                         | 1.75 us: 1.10x slower                                      |
| pprint_safe_repr           | 474 ms                                                          | 523 ms: 1.10x slower                                       |
| pycparser                  | 754 ms                                                          | 833 ms: 1.11x slower                                       |
| pprint_pformat             | 966 ms                                                          | 1.07 sec: 1.11x slower                                     |
| pyflate                    | 279 ms                                                          | 309 ms: 1.11x slower                                       |
| async_tree_memoization_tg  | 258 ms                                                          | 288 ms: 1.12x slower                                       |
| fannkuch                   | 243 ms                                                          | 274 ms: 1.13x slower                                       |
| async_tree_memoization     | 264 ms                                                          | 298 ms: 1.13x slower                                       |
| telco                      | 4.67 ms                                                         | 5.30 ms: 1.14x slower                                      |
| deepcopy_reduce            | 1.99 us                                                         | 2.27 us: 1.14x slower                                      |
| meteor_contest             | 69.9 ms                                                         | 80.0 ms: 1.14x slower                                      |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 446 ms: 1.15x slower                                       |
| async_tree_none_tg         | 202 ms                                                          | 231 ms: 1.15x slower                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 442 ms: 1.16x slower                                       |
| regex_effbot               | 1.58 ms                                                         | 1.85 ms: 1.17x slower                                      |
| unpickle_list              | 2.62 us                                                         | 3.07 us: 1.17x slower                                      |
| json                       | 3.19 ms                                                         | 3.78 ms: 1.19x slower                                      |
| python_startup             | 20.3 ms                                                         | 24.2 ms: 1.19x slower                                      |
| asyncio_tcp                | 471 ms                                                          | 563 ms: 1.19x slower                                       |
| xml_etree_parse            | 90.9 ms                                                         | 109 ms: 1.20x slower                                       |
| pickle                     | 7.11 us                                                         | 8.55 us: 1.20x slower                                      |
| deltablue                  | 1.88 ms                                                         | 2.27 ms: 1.21x slower                                      |
| bench_thread_pool          | 768 us                                                          | 930 us: 1.21x slower                                       |
| create_gc_cycles           | 888 us                                                          | 1.08 ms: 1.21x slower                                      |
| xml_etree_generate         | 53.2 ms                                                         | 64.6 ms: 1.22x slower                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 76.0 ms: 1.22x slower                                      |
| pickle_list                | 2.90 us                                                         | 3.56 us: 1.22x slower                                      |
| logging_format             | 6.22 us                                                         | 7.64 us: 1.23x slower                                      |
| python_startup_no_site     | 16.2 ms                                                         | 19.9 ms: 1.23x slower                                      |
| comprehensions             | 10.4 us                                                         | 12.8 us: 1.23x slower                                      |
| logging_simple             | 5.78 us                                                         | 7.14 us: 1.23x slower                                      |
| chaos                      | 38.4 ms                                                         | 47.7 ms: 1.24x slower                                      |
| dulwich_log                | 38.0 ms                                                         | 47.6 ms: 1.25x slower                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 49.0 ms: 1.25x slower                                      |
| pickle_dict                | 18.1 us                                                         | 22.9 us: 1.26x slower                                      |
| mdp                        | 1.31 sec                                                        | 1.67 sec: 1.27x slower                                     |
| xml_etree_process          | 36.4 ms                                                         | 46.7 ms: 1.28x slower                                      |
| bench_mp_pool              | 64.8 ms                                                         | 83.6 ms: 1.29x slower                                      |
| tornado_http               | 81.8 ms                                                         | 106 ms: 1.30x slower                                       |
| typing_runtime_protocols   | 101 us                                                          | 132 us: 1.31x slower                                       |
| html5lib                   | 35.0 ms                                                         | 46.3 ms: 1.32x slower                                      |
| nqueens                    | 56.7 ms                                                         | 75.2 ms: 1.33x slower                                      |
| generators                 | 19.6 ms                                                         | 26.0 ms: 1.33x slower                                      |
| docutils                   | 1.63 sec                                                        | 2.17 sec: 1.34x slower                                     |
| logging_silent             | 52.9 ns                                                         | 71.4 ns: 1.35x slower                                      |
| unpickle                   | 8.40 us                                                         | 11.4 us: 1.35x slower                                      |
| go                         | 82.1 ms                                                         | 112 ms: 1.36x slower                                       |
| 2to3                       | 207 ms                                                          | 283 ms: 1.37x slower                                       |
| regex_compile              | 78.0 ms                                                         | 107 ms: 1.37x slower                                       |
| json_dumps                 | 5.61 ms                                                         | 7.69 ms: 1.37x slower                                      |
| sqlglot_parse              | 748 us                                                          | 1.04 ms: 1.39x slower                                      |
| sympy_sum                  | 84.4 ms                                                         | 118 ms: 1.40x slower                                       |
| sqlglot_normalize          | 173 ms                                                          | 244 ms: 1.41x slower                                       |
| sympy_integrate            | 12.2 ms                                                         | 17.3 ms: 1.42x slower                                      |
| coverage                   | 42.1 ms                                                         | 59.6 ms: 1.42x slower                                      |
| sqlglot_transpile          | 955 us                                                          | 1.35 ms: 1.42x slower                                      |
| sympy_str                  | 159 ms                                                          | 226 ms: 1.42x slower                                       |
| pickle_pure_python         | 175 us                                                          | 251 us: 1.43x slower                                       |
| sympy_expand               | 271 ms                                                          | 389 ms: 1.44x slower                                       |
| scimark_lu                 | 56.6 ms                                                         | 82.8 ms: 1.46x slower                                      |
| richards_super             | 30.2 ms                                                         | 44.4 ms: 1.47x slower                                      |
| pylint                     | 205 ms                                                          | 302 ms: 1.47x slower                                       |
| genshi_text                | 14.4 ms                                                         | 21.4 ms: 1.49x slower                                      |
| json_loads                 | 14.2 us                                                         | 21.2 us: 1.49x slower                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 49.1 ms: 1.50x slower                                      |
| django_template            | 21.7 ms                                                         | 32.7 ms: 1.51x slower                                      |
| raytrace                   | 162 ms                                                          | 245 ms: 1.51x slower                                       |
| richards                   | 26.7 ms                                                         | 41.0 ms: 1.54x slower                                      |
| coroutines                 | 12.8 ms                                                         | 19.9 ms: 1.56x slower                                      |
| hexiom                     | 3.72 ms                                                         | 5.85 ms: 1.57x slower                                      |
| async_generators           | 223 ms                                                          | 351 ms: 1.57x slower                                       |
| genshi_xml                 | 31.6 ms                                                         | 50.1 ms: 1.59x slower                                      |
| gc_traversal               | 1.55 ms                                                         | 2.52 ms: 1.62x slower                                      |
| unpickle_pure_python       | 122 us                                                          | 207 us: 1.70x slower                                       |
| Geometric mean             | (ref)                                                           | 1.20x slower                                               |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20241010-3.14.0a0-dd0ee20-JIT/bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.19x
- 95% likely to have a slowdown of 1.17x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: unknown