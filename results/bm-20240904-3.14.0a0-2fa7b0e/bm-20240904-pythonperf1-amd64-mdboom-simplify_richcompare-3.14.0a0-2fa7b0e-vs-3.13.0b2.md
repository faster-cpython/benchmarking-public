# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 228 ms: 1.10x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.70 sec: 1.04x slower                                                     |
| html5lib       | 35.0 ms                                                         | 40.2 ms: 1.15x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 93.2 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 567 ms: 1.07x faster                                                       |
| async_tree_none            | 218 ms                                                          | 213 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 400 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                               |

Benchmark hidden because not significant (5): async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 56.7 ms: 1.14x slower                                                      |
| nbody          | 67.6 ms                                                         | 88.1 ms: 1.30x slower                                                      |
| Geometric mean | (ref)                                                           | 1.14x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.5 ms: 1.09x faster                                                      |
| regex_dna      | 119 ms                                                          | 115 ms: 1.03x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 91.6 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                           | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 90.9 ms                                                         | 93.5 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.6 ms: 1.07x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 57.6 ms: 1.08x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.27 ms: 1.12x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 41.3 ms: 1.13x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.60 sec: 1.19x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 212 us: 1.21x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 155 us: 1.27x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.12x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.1 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 7.04 ms: 1.11x slower                                                      |
| django_template | 21.7 ms                                                         | 24.7 ms: 1.14x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 37.0 ms: 1.17x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.7 ms: 1.23x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 519 us: 15.62x faster                                                      |
| deepcopy                   | 220 us                                                          | 189 us: 1.17x faster                                                       |
| regex_v8                   | 15.8 ms                                                         | 14.5 ms: 1.09x faster                                                      |
| async_tree_io_tg           | 605 ms                                                          | 567 ms: 1.07x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 20.7 us: 1.07x faster                                                      |
| deepcopy_reduce            | 1.99 us                                                         | 1.92 us: 1.04x faster                                                      |
| regex_dna                  | 119 ms                                                          | 115 ms: 1.03x faster                                                       |
| regex_effbot               | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                      |
| async_tree_none            | 218 ms                                                          | 213 ms: 1.02x faster                                                       |
| pidigits                   | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| xml_etree_parse            | 90.9 ms                                                         | 93.5 ms: 1.03x slower                                                      |
| create_gc_cycles           | 888 us                                                          | 917 us: 1.03x slower                                                       |
| docutils                   | 1.63 sec                                                        | 1.70 sec: 1.04x slower                                                     |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 400 ms: 1.05x slower                                                       |
| pathlib                    | 75.9 ms                                                         | 79.5 ms: 1.05x slower                                                      |
| generators                 | 19.6 ms                                                         | 20.7 ms: 1.06x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 90.0 ms: 1.07x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 66.6 ms: 1.07x slower                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.69 ms: 1.07x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 825 us: 1.08x slower                                                       |
| go                         | 82.1 ms                                                         | 88.6 ms: 1.08x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 57.6 ms: 1.08x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 70.3 ms: 1.09x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 13.3 ms: 1.09x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 35.7 ms: 1.09x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.79 us: 1.09x slower                                                      |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.62 sec: 1.09x slower                                                     |
| python_startup             | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 49.8 ms: 1.10x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.37 us: 1.10x slower                                                      |
| 2to3                       | 207 ms                                                          | 228 ms: 1.10x slower                                                       |
| async_generators           | 223 ms                                                          | 247 ms: 1.10x slower                                                       |
| telco                      | 4.67 ms                                                         | 5.16 ms: 1.11x slower                                                      |
| mako                       | 6.36 ms                                                         | 7.04 ms: 1.11x slower                                                      |
| asyncio_tcp                | 471 ms                                                          | 522 ms: 1.11x slower                                                       |
| pylint                     | 205 ms                                                          | 227 ms: 1.11x slower                                                       |
| sqlglot_normalize          | 173 ms                                                          | 192 ms: 1.11x slower                                                       |
| sympy_str                  | 159 ms                                                          | 177 ms: 1.11x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                         | 18.1 ms: 1.11x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 42.4 ms: 1.11x slower                                                      |
| scimark_lu                 | 56.6 ms                                                         | 63.1 ms: 1.11x slower                                                      |
| json_dumps                 | 5.61 ms                                                         | 6.27 ms: 1.12x slower                                                      |
| sympy_expand               | 271 ms                                                          | 303 ms: 1.12x slower                                                       |
| typing_runtime_protocols   | 101 us                                                          | 114 us: 1.12x slower                                                       |
| meteor_contest             | 69.9 ms                                                         | 78.8 ms: 1.13x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 64.1 ms: 1.13x slower                                                      |
| xml_etree_process          | 36.4 ms                                                         | 41.3 ms: 1.13x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 14.5 ms: 1.14x slower                                                      |
| tornado_http               | 81.8 ms                                                         | 93.2 ms: 1.14x slower                                                      |
| float                      | 49.7 ms                                                         | 56.7 ms: 1.14x slower                                                      |
| django_template            | 21.7 ms                                                         | 24.7 ms: 1.14x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 40.2 ms: 1.15x slower                                                      |
| coverage                   | 42.1 ms                                                         | 48.4 ms: 1.15x slower                                                      |
| chaos                      | 38.4 ms                                                         | 44.2 ms: 1.15x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.51 sec: 1.15x slower                                                     |
| spectral_norm              | 63.7 ms                                                         | 73.9 ms: 1.16x slower                                                      |
| comprehensions             | 10.4 us                                                         | 12.1 us: 1.17x slower                                                      |
| raytrace                   | 162 ms                                                          | 190 ms: 1.17x slower                                                       |
| pyflate                    | 279 ms                                                          | 326 ms: 1.17x slower                                                       |
| genshi_xml                 | 31.6 ms                                                         | 37.0 ms: 1.17x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 91.6 ms: 1.18x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.12 ms: 1.18x slower                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.60 sec: 1.19x slower                                                     |
| pprint_safe_repr           | 474 ms                                                          | 563 ms: 1.19x slower                                                       |
| sqlglot_parse              | 748 us                                                          | 892 us: 1.19x slower                                                       |
| pprint_pformat             | 966 ms                                                          | 1.15 sec: 1.19x slower                                                     |
| deltablue                  | 1.88 ms                                                         | 2.28 ms: 1.21x slower                                                      |
| richards                   | 26.7 ms                                                         | 32.3 ms: 1.21x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 212 us: 1.21x slower                                                       |
| logging_silent             | 52.9 ns                                                         | 64.4 ns: 1.22x slower                                                      |
| richards_super             | 30.2 ms                                                         | 36.7 ms: 1.22x slower                                                      |
| hexiom                     | 3.72 ms                                                         | 4.56 ms: 1.22x slower                                                      |
| scimark_sor                | 75.3 ms                                                         | 92.7 ms: 1.23x slower                                                      |
| genshi_text                | 14.4 ms                                                         | 17.7 ms: 1.23x slower                                                      |
| scimark_fft                | 171 ms                                                          | 211 ms: 1.24x slower                                                       |
| fannkuch                   | 243 ms                                                          | 307 ms: 1.26x slower                                                       |
| unpickle_pure_python       | 122 us                                                          | 155 us: 1.27x slower                                                       |
| scimark_monte_carlo        | 39.1 ms                                                         | 50.9 ms: 1.30x slower                                                      |
| nbody                      | 67.6 ms                                                         | 88.1 ms: 1.30x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.07x slower                                                               |

Benchmark hidden because not significant (9): async_tree_io, json, async_tree_memoization_tg, json_loads, async_tree_cpu_io_mixed, gc_traversal, async_tree_memoization, async_tree_none_tg, pycparser
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown