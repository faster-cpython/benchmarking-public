# Results vs. 3.13.0b2

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-amd64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.01x slower
- HPT reliability: 98.56%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 239 ms: 1.16x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.91 sec: 1.18x slower                                                     |
| html5lib       | 35.0 ms                                                         | 42.1 ms: 1.20x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 87.4 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                           | 1.15x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 555 ms: 1.09x faster                                                       |
| async_tree_none            | 218 ms                                                          | 206 ms: 1.06x faster                                                       |
| async_tree_memoization     | 264 ms                                                          | 258 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 397 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 49.4 ms: 1.37x faster                                                      |
| float          | 49.7 ms                                                         | 44.5 ms: 1.12x faster                                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                           | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 121 ms: 1.02x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 94.2 ms: 1.21x slower                                                      |
| Geometric mean | (ref)                                                           | 1.04x slower                                                               |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 53.2 ms                                                         | 49.0 ms: 1.09x faster                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.26 sec: 1.07x faster                                                     |
| xml_etree_process    | 36.4 ms                                                         | 34.8 ms: 1.05x faster                                                      |
| pickle_list          | 2.90 us                                                         | 2.78 us: 1.04x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 60.7 ms: 1.03x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 17.9 us: 1.01x faster                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.4 ms: 1.02x slower                                                      |
| json_loads           | 14.2 us                                                         | 14.4 us: 1.02x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.73 ms: 1.02x slower                                                      |
| pickle               | 7.11 us                                                         | 7.38 us: 1.04x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.87 us: 1.10x slower                                                      |
| unpickle             | 8.40 us                                                         | 9.27 us: 1.10x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 196 us: 1.12x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 145 us: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.6 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.0 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.26 ms: 1.21x faster                                                      |
| django_template | 21.7 ms                                                         | 26.2 ms: 1.21x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 18.9 ms: 1.31x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 45.7 ms: 1.45x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.17x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 525 us: 15.43x faster                                                      |
| deepcopy_memo              | 22.1 us                                                         | 14.8 us: 1.49x faster                                                      |
| spectral_norm              | 63.7 ms                                                         | 43.3 ms: 1.47x faster                                                      |
| nbody                      | 67.6 ms                                                         | 49.4 ms: 1.37x faster                                                      |
| scimark_sor                | 75.3 ms                                                         | 60.7 ms: 1.24x faster                                                      |
| deepcopy                   | 220 us                                                          | 181 us: 1.21x faster                                                       |
| mako                       | 6.36 ms                                                         | 5.26 ms: 1.21x faster                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 38.6 ms: 1.18x faster                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.13 ms: 1.18x faster                                                      |
| scimark_fft                | 171 ms                                                          | 149 ms: 1.15x faster                                                       |
| float                      | 49.7 ms                                                         | 44.5 ms: 1.12x faster                                                      |
| deepcopy_reduce            | 1.99 us                                                         | 1.79 us: 1.11x faster                                                      |
| async_tree_io_tg           | 605 ms                                                          | 555 ms: 1.09x faster                                                       |
| xml_etree_generate         | 53.2 ms                                                         | 49.0 ms: 1.09x faster                                                      |
| json                       | 3.19 ms                                                         | 2.95 ms: 1.08x faster                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.26 sec: 1.07x faster                                                     |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.39 sec: 1.07x faster                                                     |
| async_tree_none            | 218 ms                                                          | 206 ms: 1.06x faster                                                       |
| pyflate                    | 279 ms                                                          | 265 ms: 1.05x faster                                                       |
| xml_etree_process          | 36.4 ms                                                         | 34.8 ms: 1.05x faster                                                      |
| pickle_list                | 2.90 us                                                         | 2.78 us: 1.04x faster                                                      |
| scimark_lu                 | 56.6 ms                                                         | 54.4 ms: 1.04x faster                                                      |
| deltablue                  | 1.88 ms                                                         | 1.82 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 60.7 ms: 1.03x faster                                                      |
| async_tree_memoization     | 264 ms                                                          | 258 ms: 1.02x faster                                                       |
| pickle_dict                | 18.1 us                                                         | 17.9 us: 1.01x faster                                                      |
| telco                      | 4.67 ms                                                         | 4.60 ms: 1.01x faster                                                      |
| pathlib                    | 75.9 ms                                                         | 74.8 ms: 1.01x faster                                                      |
| pidigits                   | 150 ms                                                          | 149 ms: 1.01x faster                                                       |
| gc_traversal               | 1.55 ms                                                         | 1.55 ms: 1.01x faster                                                      |
| create_gc_cycles           | 888 us                                                          | 901 us: 1.01x slower                                                       |
| xml_etree_parse            | 90.9 ms                                                         | 92.4 ms: 1.02x slower                                                      |
| json_loads                 | 14.2 us                                                         | 14.4 us: 1.02x slower                                                      |
| regex_dna                  | 119 ms                                                          | 121 ms: 1.02x slower                                                       |
| fannkuch                   | 243 ms                                                          | 248 ms: 1.02x slower                                                       |
| json_dumps                 | 5.61 ms                                                         | 5.73 ms: 1.02x slower                                                      |
| comprehensions             | 10.4 us                                                         | 10.7 us: 1.03x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.45 us: 1.04x slower                                                      |
| pickle                     | 7.11 us                                                         | 7.38 us: 1.04x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 397 ms: 1.04x slower                                                       |
| chaos                      | 38.4 ms                                                         | 40.0 ms: 1.04x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.06 us: 1.05x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 59.6 ms: 1.05x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 809 us: 1.05x slower                                                       |
| pprint_safe_repr           | 474 ms                                                          | 503 ms: 1.06x slower                                                       |
| python_startup             | 20.3 ms                                                         | 21.6 ms: 1.06x slower                                                      |
| tornado_http               | 81.8 ms                                                         | 87.4 ms: 1.07x slower                                                      |
| pprint_pformat             | 966 ms                                                          | 1.03 sec: 1.07x slower                                                     |
| meteor_contest             | 69.9 ms                                                         | 74.9 ms: 1.07x slower                                                      |
| generators                 | 19.6 ms                                                         | 21.1 ms: 1.08x slower                                                      |
| logging_silent             | 52.9 ns                                                         | 57.2 ns: 1.08x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 13.8 ms: 1.08x slower                                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 42.7 ms: 1.09x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.43 sec: 1.09x slower                                                     |
| unpickle_list              | 2.62 us                                                         | 2.87 us: 1.10x slower                                                      |
| typing_runtime_protocols   | 101 us                                                          | 111 us: 1.10x slower                                                       |
| unpickle                   | 8.40 us                                                         | 9.27 us: 1.10x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 71.7 ms: 1.11x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 18.0 ms: 1.11x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 42.3 ms: 1.11x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 196 us: 1.12x slower                                                       |
| go                         | 82.1 ms                                                         | 92.2 ms: 1.12x slower                                                      |
| coverage                   | 42.1 ms                                                         | 48.1 ms: 1.14x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 199 ms: 1.15x slower                                                       |
| 2to3                       | 207 ms                                                          | 239 ms: 1.16x slower                                                       |
| sympy_sum                  | 84.4 ms                                                         | 97.9 ms: 1.16x slower                                                      |
| async_generators           | 223 ms                                                          | 260 ms: 1.16x slower                                                       |
| docutils                   | 1.63 sec                                                        | 1.91 sec: 1.18x slower                                                     |
| sqlglot_parse              | 748 us                                                          | 886 us: 1.18x slower                                                       |
| sympy_str                  | 159 ms                                                          | 189 ms: 1.19x slower                                                       |
| unpickle_pure_python       | 122 us                                                          | 145 us: 1.19x slower                                                       |
| sqlglot_transpile          | 955 us                                                          | 1.14 ms: 1.20x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 42.1 ms: 1.20x slower                                                      |
| django_template            | 21.7 ms                                                         | 26.2 ms: 1.21x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 94.2 ms: 1.21x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 14.8 ms: 1.21x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 39.7 ms: 1.21x slower                                                      |
| sympy_expand               | 271 ms                                                          | 330 ms: 1.22x slower                                                       |
| raytrace                   | 162 ms                                                          | 202 ms: 1.25x slower                                                       |
| pylint                     | 205 ms                                                          | 263 ms: 1.29x slower                                                       |
| richards_super             | 30.2 ms                                                         | 39.1 ms: 1.30x slower                                                      |
| hexiom                     | 3.72 ms                                                         | 4.89 ms: 1.31x slower                                                      |
| genshi_text                | 14.4 ms                                                         | 18.9 ms: 1.31x slower                                                      |
| richards                   | 26.7 ms                                                         | 36.5 ms: 1.37x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 45.7 ms: 1.45x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (9): regex_v8, pycparser, async_tree_none_tg, asyncio_tcp, async_tree_io, async_tree_memoization_tg, sqlite_synth, regex_effbot, async_tree_cpu_io_mixed
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: unpack_sequence

# HPT report

- Reliability score: 98.56% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown