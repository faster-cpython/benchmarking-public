# Results vs. 3.13.0b2

- fork: python
- ref: 4717aaa1a72d1964f153
- machine: windows-amd64
- commit hash: 4717aaa
- commit date: 2024-06-22
- overall geometric mean: 1.03x faster
- HPT reliability: 73.32%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 228 ms: 1.10x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.74 sec: 1.07x slower                                                     |
| html5lib       | 35.0 ms                                                         | 35.7 ms: 1.02x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 82.7 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                           | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 505 ms: 1.20x faster                                                       |
| async_tree_io              | 588 ms                                                          | 495 ms: 1.19x faster                                                       |
| async_tree_none_tg         | 202 ms                                                          | 178 ms: 1.13x faster                                                       |
| async_tree_memoization_tg  | 258 ms                                                          | 234 ms: 1.11x faster                                                       |
| async_tree_none            | 218 ms                                                          | 198 ms: 1.10x faster                                                       |
| async_tree_memoization     | 264 ms                                                          | 242 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 377 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 372 ms: 1.03x faster                                                       |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 53.6 ms: 1.26x faster                                                      |
| float          | 49.7 ms                                                         | 44.0 ms: 1.13x faster                                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                           | 1.13x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.56 ms: 1.01x faster                                                      |
| regex_dna      | 119 ms                                                          | 118 ms: 1.01x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 87.2 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                           | 1.04x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.21 sec: 1.12x faster                                                     |
| pickle_pure_python   | 175 us                                                          | 168 us: 1.04x faster                                                       |
| xml_etree_generate   | 53.2 ms                                                         | 51.3 ms: 1.04x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 17.7 us: 1.03x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 60.9 ms: 1.02x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.0 us: 1.01x faster                                                      |
| xml_etree_process    | 36.4 ms                                                         | 36.2 ms: 1.01x faster                                                      |
| json_dumps           | 5.61 ms                                                         | 5.65 ms: 1.01x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 123 us: 1.01x slower                                                       |
| xml_etree_parse      | 90.9 ms                                                         | 92.6 ms: 1.02x slower                                                      |
| pickle               | 7.11 us                                                         | 7.29 us: 1.03x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.80 us: 1.07x slower                                                      |
| unpickle             | 8.40 us                                                         | 9.00 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.5 ms: 1.11x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.4 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.08 ms: 1.25x faster                                                      |
| django_template | 21.7 ms                                                         | 24.6 ms: 1.13x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.2 ms: 1.19x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 41.8 ms: 1.32x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.09x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 510 us: 15.89x faster                                                      |
| deepcopy_memo              | 22.1 us                                                         | 15.3 us: 1.44x faster                                                      |
| spectral_norm              | 63.7 ms                                                         | 46.3 ms: 1.38x faster                                                      |
| nbody                      | 67.6 ms                                                         | 53.6 ms: 1.26x faster                                                      |
| deepcopy                   | 220 us                                                          | 175 us: 1.25x faster                                                       |
| mako                       | 6.36 ms                                                         | 5.08 ms: 1.25x faster                                                      |
| async_tree_io_tg           | 605 ms                                                          | 505 ms: 1.20x faster                                                       |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.09 ms: 1.19x faster                                                      |
| deepcopy_reduce            | 1.99 us                                                         | 1.68 us: 1.19x faster                                                      |
| async_tree_io              | 588 ms                                                          | 495 ms: 1.19x faster                                                       |
| scimark_fft                | 171 ms                                                          | 150 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 202 ms                                                          | 178 ms: 1.13x faster                                                       |
| float                      | 49.7 ms                                                         | 44.0 ms: 1.13x faster                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.21 sec: 1.12x faster                                                     |
| crypto_pyaes               | 45.5 ms                                                         | 40.7 ms: 1.12x faster                                                      |
| async_tree_memoization_tg  | 258 ms                                                          | 234 ms: 1.11x faster                                                       |
| pyflate                    | 279 ms                                                          | 252 ms: 1.11x faster                                                       |
| async_tree_none            | 218 ms                                                          | 198 ms: 1.10x faster                                                       |
| fannkuch                   | 243 ms                                                          | 222 ms: 1.10x faster                                                       |
| async_tree_memoization     | 264 ms                                                          | 242 ms: 1.09x faster                                                       |
| json                       | 3.19 ms                                                         | 2.93 ms: 1.09x faster                                                      |
| logging_format             | 6.22 us                                                         | 5.87 us: 1.06x faster                                                      |
| logging_simple             | 5.78 us                                                         | 5.49 us: 1.05x faster                                                      |
| pprint_safe_repr           | 474 ms                                                          | 450 ms: 1.05x faster                                                       |
| scimark_monte_carlo        | 39.1 ms                                                         | 37.4 ms: 1.05x faster                                                      |
| pprint_pformat             | 966 ms                                                          | 924 ms: 1.05x faster                                                       |
| telco                      | 4.67 ms                                                         | 4.48 ms: 1.04x faster                                                      |
| pickle_pure_python         | 175 us                                                          | 168 us: 1.04x faster                                                       |
| xml_etree_generate         | 53.2 ms                                                         | 51.3 ms: 1.04x faster                                                      |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 377 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 372 ms: 1.03x faster                                                       |
| pickle_dict                | 18.1 us                                                         | 17.7 us: 1.03x faster                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 60.9 ms: 1.02x faster                                                      |
| comprehensions             | 10.4 us                                                         | 10.2 us: 1.02x faster                                                      |
| sqlite_synth               | 1.60 us                                                         | 1.58 us: 1.01x faster                                                      |
| regex_effbot               | 1.58 ms                                                         | 1.56 ms: 1.01x faster                                                      |
| json_loads                 | 14.2 us                                                         | 14.0 us: 1.01x faster                                                      |
| regex_dna                  | 119 ms                                                          | 118 ms: 1.01x faster                                                       |
| xml_etree_process          | 36.4 ms                                                         | 36.2 ms: 1.01x faster                                                      |
| pidigits                   | 150 ms                                                          | 149 ms: 1.01x faster                                                       |
| chaos                      | 38.4 ms                                                         | 38.5 ms: 1.00x slower                                                      |
| gc_traversal               | 1.55 ms                                                         | 1.56 ms: 1.01x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 12.8 ms: 1.01x slower                                                      |
| json_dumps                 | 5.61 ms                                                         | 5.65 ms: 1.01x slower                                                      |
| tornado_http               | 81.8 ms                                                         | 82.7 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 123 us: 1.01x slower                                                       |
| xml_etree_parse            | 90.9 ms                                                         | 92.6 ms: 1.02x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 35.7 ms: 1.02x slower                                                      |
| generators                 | 19.6 ms                                                         | 20.0 ms: 1.02x slower                                                      |
| pickle                     | 7.11 us                                                         | 7.29 us: 1.03x slower                                                      |
| create_gc_cycles           | 888 us                                                          | 914 us: 1.03x slower                                                       |
| sqlglot_parse              | 748 us                                                          | 775 us: 1.04x slower                                                       |
| raytrace                   | 162 ms                                                          | 168 ms: 1.04x slower                                                       |
| coverage                   | 42.1 ms                                                         | 43.6 ms: 1.04x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 72.6 ms: 1.04x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.37 sec: 1.05x slower                                                     |
| logging_silent             | 52.9 ns                                                         | 55.4 ns: 1.05x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 59.5 ms: 1.05x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.01 ms: 1.05x slower                                                      |
| scimark_sor                | 75.3 ms                                                         | 79.3 ms: 1.05x slower                                                      |
| unpickle_list              | 2.62 us                                                         | 2.80 us: 1.07x slower                                                      |
| unpickle                   | 8.40 us                                                         | 9.00 us: 1.07x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 90.5 ms: 1.07x slower                                                      |
| go                         | 82.1 ms                                                         | 88.0 ms: 1.07x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.74 sec: 1.07x slower                                                     |
| bench_mp_pool              | 64.8 ms                                                         | 69.9 ms: 1.08x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 188 ms: 1.09x slower                                                       |
| sqlglot_optimize           | 32.7 ms                                                         | 35.6 ms: 1.09x slower                                                      |
| async_generators           | 223 ms                                                          | 243 ms: 1.09x slower                                                       |
| typing_runtime_protocols   | 101 us                                                          | 110 us: 1.09x slower                                                       |
| sympy_str                  | 159 ms                                                          | 175 ms: 1.10x slower                                                       |
| 2to3                       | 207 ms                                                          | 228 ms: 1.10x slower                                                       |
| python_startup             | 20.3 ms                                                         | 22.5 ms: 1.11x slower                                                      |
| deltablue                  | 1.88 ms                                                         | 2.09 ms: 1.11x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 13.6 ms: 1.11x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 87.2 ms: 1.12x slower                                                      |
| richards_super             | 30.2 ms                                                         | 33.8 ms: 1.12x slower                                                      |
| sympy_expand               | 271 ms                                                          | 305 ms: 1.13x slower                                                       |
| richards                   | 26.7 ms                                                         | 30.2 ms: 1.13x slower                                                      |
| pylint                     | 205 ms                                                          | 232 ms: 1.13x slower                                                       |
| django_template            | 21.7 ms                                                         | 24.6 ms: 1.13x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 18.4 ms: 1.14x slower                                                      |
| genshi_text                | 14.4 ms                                                         | 17.2 ms: 1.19x slower                                                      |
| scimark_lu                 | 56.6 ms                                                         | 68.8 ms: 1.22x slower                                                      |
| hexiom                     | 3.72 ms                                                         | 4.62 ms: 1.24x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 41.8 ms: 1.32x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                               |

Benchmark hidden because not significant (7): pickle_list, asyncio_tcp_ssl, pathlib, bench_thread_pool, asyncio_tcp, pycparser, regex_v8
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2

# HPT report

- Reliability score: 73.32% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown