# Results vs. 3.13.0b2

- fork: python
- ref: 99400930ac1d4e5e10a5
- machine: windows-amd64
- commit hash: 9940093
- commit date: 2024-10-09
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 227 ms: 1.10x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.73 sec: 1.06x slower                                                     |
| html5lib       | 35.0 ms                                                         | 41.9 ms: 1.20x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 94.1 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                           | 1.13x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 593 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 395 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 404 ms: 1.04x slower                                                       |
| async_tree_memoization_tg  | 258 ms                                                          | 268 ms: 1.04x slower                                                       |
| async_tree_none_tg         | 202 ms                                                          | 212 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (3): async_tree_none, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 149 ms: 1.01x faster                                                       |
| float          | 49.7 ms                                                         | 56.5 ms: 1.14x slower                                                      |
| nbody          | 67.6 ms                                                         | 85.6 ms: 1.27x slower                                                      |
| Geometric mean | (ref)                                                           | 1.13x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 114 ms: 1.04x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 91.8 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                           | 1.04x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.11 us                                                         | 7.31 us: 1.03x slower                                                      |
| json_loads           | 14.2 us                                                         | 14.7 us: 1.04x slower                                                      |
| pickle_dict          | 18.1 us                                                         | 19.0 us: 1.05x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 95.9 ms: 1.06x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.0 ms: 1.06x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.82 us: 1.08x slower                                                      |
| unpickle             | 8.40 us                                                         | 9.17 us: 1.09x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 59.4 ms: 1.12x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.41 ms: 1.14x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 42.5 ms: 1.17x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.66 sec: 1.23x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 220 us: 1.26x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 159 us: 1.30x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.11x slower                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.1 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.7 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 7.19 ms: 1.13x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 38.3 ms: 1.21x slower                                                      |
| django_template | 21.7 ms                                                         | 26.3 ms: 1.21x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.8 ms: 1.24x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.20x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 528 us: 15.36x faster                                                      |
| deepcopy                   | 220 us                                                          | 193 us: 1.14x faster                                                       |
| regex_dna                  | 119 ms                                                          | 114 ms: 1.04x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 21.6 us: 1.02x faster                                                      |
| async_tree_io_tg           | 605 ms                                                          | 593 ms: 1.02x faster                                                       |
| gc_traversal               | 1.55 ms                                                         | 1.53 ms: 1.01x faster                                                      |
| regex_effbot               | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| pidigits                   | 150 ms                                                          | 149 ms: 1.01x faster                                                       |
| sqlite_synth               | 1.60 us                                                         | 1.64 us: 1.03x slower                                                      |
| pickle                     | 7.11 us                                                         | 7.31 us: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 395 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 404 ms: 1.04x slower                                                       |
| async_tree_memoization_tg  | 258 ms                                                          | 268 ms: 1.04x slower                                                       |
| json_loads                 | 14.2 us                                                         | 14.7 us: 1.04x slower                                                      |
| create_gc_cycles           | 888 us                                                          | 928 us: 1.05x slower                                                       |
| pickle_dict                | 18.1 us                                                         | 19.0 us: 1.05x slower                                                      |
| async_tree_none_tg         | 202 ms                                                          | 212 ms: 1.05x slower                                                       |
| telco                      | 4.67 ms                                                         | 4.90 ms: 1.05x slower                                                      |
| xml_etree_parse            | 90.9 ms                                                         | 95.9 ms: 1.06x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 66.0 ms: 1.06x slower                                                      |
| pathlib                    | 75.9 ms                                                         | 80.4 ms: 1.06x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.73 sec: 1.06x slower                                                     |
| bench_mp_pool              | 64.8 ms                                                         | 69.2 ms: 1.07x slower                                                      |
| unpickle_list              | 2.62 us                                                         | 2.82 us: 1.08x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 827 us: 1.08x slower                                                       |
| sympy_sum                  | 84.4 ms                                                         | 91.5 ms: 1.08x slower                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.72 ms: 1.09x slower                                                      |
| python_startup             | 20.3 ms                                                         | 22.1 ms: 1.09x slower                                                      |
| unpickle                   | 8.40 us                                                         | 9.17 us: 1.09x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 13.9 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 17.7 ms: 1.09x slower                                                      |
| 2to3                       | 207 ms                                                          | 227 ms: 1.10x slower                                                       |
| crypto_pyaes               | 45.5 ms                                                         | 50.1 ms: 1.10x slower                                                      |
| async_generators           | 223 ms                                                          | 248 ms: 1.11x slower                                                       |
| xml_etree_generate         | 53.2 ms                                                         | 59.4 ms: 1.12x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 13.7 ms: 1.12x slower                                                      |
| go                         | 82.1 ms                                                         | 91.7 ms: 1.12x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 78.1 ms: 1.12x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.47 sec: 1.12x slower                                                     |
| pylint                     | 205 ms                                                          | 230 ms: 1.12x slower                                                       |
| typing_runtime_protocols   | 101 us                                                          | 114 us: 1.13x slower                                                       |
| sympy_str                  | 159 ms                                                          | 179 ms: 1.13x slower                                                       |
| generators                 | 19.6 ms                                                         | 22.1 ms: 1.13x slower                                                      |
| logging_format             | 6.22 us                                                         | 7.02 us: 1.13x slower                                                      |
| mako                       | 6.36 ms                                                         | 7.19 ms: 1.13x slower                                                      |
| float                      | 49.7 ms                                                         | 56.5 ms: 1.14x slower                                                      |
| json_dumps                 | 5.61 ms                                                         | 6.41 ms: 1.14x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.62 us: 1.15x slower                                                      |
| tornado_http               | 81.8 ms                                                         | 94.1 ms: 1.15x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 200 ms: 1.15x slower                                                       |
| scimark_lu                 | 56.6 ms                                                         | 65.3 ms: 1.15x slower                                                      |
| sympy_expand               | 271 ms                                                          | 312 ms: 1.15x slower                                                       |
| comprehensions             | 10.4 us                                                         | 12.0 us: 1.16x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 65.5 ms: 1.16x slower                                                      |
| coverage                   | 42.1 ms                                                         | 48.7 ms: 1.16x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 37.9 ms: 1.16x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 44.2 ms: 1.16x slower                                                      |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.72 sec: 1.16x slower                                                     |
| xml_etree_process          | 36.4 ms                                                         | 42.5 ms: 1.17x slower                                                      |
| spectral_norm              | 63.7 ms                                                         | 74.6 ms: 1.17x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 91.8 ms: 1.18x slower                                                      |
| chaos                      | 38.4 ms                                                         | 45.5 ms: 1.19x slower                                                      |
| pyflate                    | 279 ms                                                          | 332 ms: 1.19x slower                                                       |
| html5lib                   | 35.0 ms                                                         | 41.9 ms: 1.20x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.15 ms: 1.20x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 38.3 ms: 1.21x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 575 ms: 1.21x slower                                                       |
| hexiom                     | 3.72 ms                                                         | 4.52 ms: 1.21x slower                                                      |
| django_template            | 21.7 ms                                                         | 26.3 ms: 1.21x slower                                                      |
| fannkuch                   | 243 ms                                                          | 297 ms: 1.22x slower                                                       |
| pprint_pformat             | 966 ms                                                          | 1.18 sec: 1.22x slower                                                     |
| tomli_loads                | 1.35 sec                                                        | 1.66 sec: 1.23x slower                                                     |
| logging_silent             | 52.9 ns                                                         | 65.4 ns: 1.24x slower                                                      |
| genshi_text                | 14.4 ms                                                         | 17.8 ms: 1.24x slower                                                      |
| deltablue                  | 1.88 ms                                                         | 2.33 ms: 1.24x slower                                                      |
| raytrace                   | 162 ms                                                          | 201 ms: 1.24x slower                                                       |
| sqlglot_parse              | 748 us                                                          | 936 us: 1.25x slower                                                       |
| pickle_pure_python         | 175 us                                                          | 220 us: 1.26x slower                                                       |
| scimark_fft                | 171 ms                                                          | 215 ms: 1.26x slower                                                       |
| scimark_sor                | 75.3 ms                                                         | 94.8 ms: 1.26x slower                                                      |
| richards                   | 26.7 ms                                                         | 33.7 ms: 1.26x slower                                                      |
| richards_super             | 30.2 ms                                                         | 38.1 ms: 1.26x slower                                                      |
| nbody                      | 67.6 ms                                                         | 85.6 ms: 1.27x slower                                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 50.4 ms: 1.29x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 159 us: 1.30x slower                                                       |
| asyncio_tcp                | 471 ms                                                          | 652 ms: 1.38x slower                                                       |
| json                       | 3.19 ms                                                         | 4.52 ms: 1.42x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.09x slower                                                               |

Benchmark hidden because not significant (7): pycparser, deepcopy_reduce, async_tree_none, pickle_list, async_tree_memoization, async_tree_io, regex_v8
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20241009-3.14.0a0-9940093/bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: unknown