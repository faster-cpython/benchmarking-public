# Results vs. 3.13.0b2

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-amd64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.01x slower
- HPT reliability: 99.83%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 241 ms: 1.16x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.91 sec: 1.18x slower                                                     |
| html5lib       | 35.0 ms                                                         | 42.0 ms: 1.20x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 97.7 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                           | 1.18x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 555 ms: 1.09x faster                                                       |
| async_tree_none            | 218 ms                                                          | 201 ms: 1.09x faster                                                       |
| async_tree_memoization     | 264 ms                                                          | 258 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 393 ms: 1.03x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                               |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 49.0 ms: 1.38x faster                                                      |
| float          | 49.7 ms                                                         | 43.8 ms: 1.14x faster                                                      |
| pidigits       | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                           | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                                      |
| regex_dna      | 119 ms                                                          | 124 ms: 1.04x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 95.2 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 53.2 ms                                                         | 49.0 ms: 1.09x faster                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.24 sec: 1.09x faster                                                     |
| xml_etree_process    | 36.4 ms                                                         | 34.7 ms: 1.05x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 17.7 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.5 ms: 1.01x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| pickle               | 7.11 us                                                         | 7.17 us: 1.01x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.6 ms: 1.02x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.86 ms: 1.04x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.80 us: 1.07x slower                                                      |
| unpickle             | 8.40 us                                                         | 9.18 us: 1.09x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 194 us: 1.10x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 141 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.3 ms: 1.10x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.5 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.15 ms: 1.23x faster                                                      |
| django_template | 21.7 ms                                                         | 26.1 ms: 1.20x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 18.7 ms: 1.30x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 44.0 ms: 1.39x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 520 us: 15.59x faster                                                      |
| deepcopy_memo              | 22.1 us                                                         | 15.2 us: 1.46x faster                                                      |
| spectral_norm              | 63.7 ms                                                         | 45.6 ms: 1.40x faster                                                      |
| nbody                      | 67.6 ms                                                         | 49.0 ms: 1.38x faster                                                      |
| scimark_sor                | 75.3 ms                                                         | 59.9 ms: 1.26x faster                                                      |
| mako                       | 6.36 ms                                                         | 5.15 ms: 1.23x faster                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 38.3 ms: 1.19x faster                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.12 ms: 1.18x faster                                                      |
| deepcopy                   | 220 us                                                          | 188 us: 1.17x faster                                                       |
| scimark_fft                | 171 ms                                                          | 148 ms: 1.16x faster                                                       |
| float                      | 49.7 ms                                                         | 43.8 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 1.99 us                                                         | 1.80 us: 1.11x faster                                                      |
| async_tree_io_tg           | 605 ms                                                          | 555 ms: 1.09x faster                                                       |
| xml_etree_generate         | 53.2 ms                                                         | 49.0 ms: 1.09x faster                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.24 sec: 1.09x faster                                                     |
| async_tree_none            | 218 ms                                                          | 201 ms: 1.09x faster                                                       |
| scimark_lu                 | 56.6 ms                                                         | 52.3 ms: 1.08x faster                                                      |
| json                       | 3.19 ms                                                         | 2.97 ms: 1.07x faster                                                      |
| pyflate                    | 279 ms                                                          | 261 ms: 1.07x faster                                                       |
| pycparser                  | 754 ms                                                          | 706 ms: 1.07x faster                                                       |
| xml_etree_process          | 36.4 ms                                                         | 34.7 ms: 1.05x faster                                                      |
| fannkuch                   | 243 ms                                                          | 232 ms: 1.05x faster                                                       |
| deltablue                  | 1.88 ms                                                         | 1.83 ms: 1.03x faster                                                      |
| pickle_dict                | 18.1 us                                                         | 17.7 us: 1.02x faster                                                      |
| async_tree_memoization     | 264 ms                                                          | 258 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 62.3 ms                                                         | 61.5 ms: 1.01x faster                                                      |
| telco                      | 4.67 ms                                                         | 4.64 ms: 1.01x faster                                                      |
| pidigits                   | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| json_loads                 | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| gc_traversal               | 1.55 ms                                                         | 1.56 ms: 1.01x slower                                                      |
| pickle                     | 7.11 us                                                         | 7.17 us: 1.01x slower                                                      |
| comprehensions             | 10.4 us                                                         | 10.6 us: 1.02x slower                                                      |
| xml_etree_parse            | 90.9 ms                                                         | 92.6 ms: 1.02x slower                                                      |
| regex_effbot               | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 393 ms: 1.03x slower                                                       |
| create_gc_cycles           | 888 us                                                          | 914 us: 1.03x slower                                                       |
| logging_simple             | 5.78 us                                                         | 5.97 us: 1.03x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.43 us: 1.03x slower                                                      |
| regex_dna                  | 119 ms                                                          | 124 ms: 1.04x slower                                                       |
| json_dumps                 | 5.61 ms                                                         | 5.86 ms: 1.04x slower                                                      |
| pathlib                    | 75.9 ms                                                         | 79.5 ms: 1.05x slower                                                      |
| chaos                      | 38.4 ms                                                         | 40.6 ms: 1.06x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 503 ms: 1.06x slower                                                       |
| nqueens                    | 56.7 ms                                                         | 60.5 ms: 1.07x slower                                                      |
| pprint_pformat             | 966 ms                                                          | 1.03 sec: 1.07x slower                                                     |
| unpickle_list              | 2.62 us                                                         | 2.80 us: 1.07x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 822 us: 1.07x slower                                                       |
| typing_runtime_protocols   | 101 us                                                          | 108 us: 1.07x slower                                                       |
| meteor_contest             | 69.9 ms                                                         | 75.1 ms: 1.08x slower                                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 42.1 ms: 1.08x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 13.8 ms: 1.08x slower                                                      |
| logging_silent             | 52.9 ns                                                         | 57.3 ns: 1.08x slower                                                      |
| unpickle                   | 8.40 us                                                         | 9.18 us: 1.09x slower                                                      |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.62 sec: 1.10x slower                                                     |
| python_startup             | 20.3 ms                                                         | 22.3 ms: 1.10x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 194 us: 1.10x slower                                                       |
| bench_mp_pool              | 64.8 ms                                                         | 71.6 ms: 1.11x slower                                                      |
| asyncio_tcp                | 471 ms                                                          | 523 ms: 1.11x slower                                                       |
| go                         | 82.1 ms                                                         | 91.4 ms: 1.11x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 43.0 ms: 1.13x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.49 sec: 1.14x slower                                                     |
| python_startup_no_site     | 16.2 ms                                                         | 18.5 ms: 1.14x slower                                                      |
| coverage                   | 42.1 ms                                                         | 48.2 ms: 1.15x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 200 ms: 1.16x slower                                                       |
| unpickle_pure_python       | 122 us                                                          | 141 us: 1.16x slower                                                       |
| sympy_sum                  | 84.4 ms                                                         | 97.8 ms: 1.16x slower                                                      |
| 2to3                       | 207 ms                                                          | 241 ms: 1.16x slower                                                       |
| generators                 | 19.6 ms                                                         | 22.8 ms: 1.17x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.91 sec: 1.18x slower                                                     |
| sqlglot_parse              | 748 us                                                          | 883 us: 1.18x slower                                                       |
| async_generators           | 223 ms                                                          | 264 ms: 1.18x slower                                                       |
| sympy_str                  | 159 ms                                                          | 188 ms: 1.18x slower                                                       |
| tornado_http               | 81.8 ms                                                         | 97.7 ms: 1.19x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 42.0 ms: 1.20x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.15 ms: 1.20x slower                                                      |
| django_template            | 21.7 ms                                                         | 26.1 ms: 1.20x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 14.8 ms: 1.21x slower                                                      |
| raytrace                   | 162 ms                                                          | 196 ms: 1.21x slower                                                       |
| sympy_expand               | 271 ms                                                          | 329 ms: 1.22x slower                                                       |
| sqlglot_optimize           | 32.7 ms                                                         | 39.8 ms: 1.22x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 95.2 ms: 1.22x slower                                                      |
| richards_super             | 30.2 ms                                                         | 38.4 ms: 1.28x slower                                                      |
| genshi_text                | 14.4 ms                                                         | 18.7 ms: 1.30x slower                                                      |
| pylint                     | 205 ms                                                          | 266 ms: 1.30x slower                                                       |
| hexiom                     | 3.72 ms                                                         | 4.92 ms: 1.32x slower                                                      |
| richards                   | 26.7 ms                                                         | 35.8 ms: 1.34x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 44.0 ms: 1.39x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (7): regex_v8, async_tree_none_tg, async_tree_memoization_tg, pickle_list, async_tree_io, sqlite_synth, async_tree_cpu_io_mixed
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: unpack_sequence

# HPT report

- Reliability score: 99.83% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown