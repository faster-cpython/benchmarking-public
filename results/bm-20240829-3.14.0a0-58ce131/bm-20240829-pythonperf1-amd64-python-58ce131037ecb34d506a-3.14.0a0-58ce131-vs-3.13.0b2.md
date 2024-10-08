# Results vs. 3.13.0b2

- fork: python
- ref: 58ce131037ecb34d506a
- machine: windows-amd64
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 228 ms: 1.10x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.69 sec: 1.04x slower                                                     |
| html5lib       | 35.0 ms                                                         | 40.4 ms: 1.15x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 92.8 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 562 ms: 1.08x faster                                                       |
| async_tree_none            | 218 ms                                                          | 209 ms: 1.04x faster                                                       |
| async_tree_memoization     | 264 ms                                                          | 254 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 401 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 56.0 ms: 1.13x slower                                                      |
| nbody          | 67.6 ms                                                         | 85.1 ms: 1.26x slower                                                      |
| Geometric mean | (ref)                                                           | 1.13x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 115 ms: 1.03x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 89.9 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.0 us: 1.01x faster                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 94.7 ms: 1.04x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.1 ms: 1.04x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 58.2 ms: 1.09x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 41.0 ms: 1.13x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.35 ms: 1.13x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.57 sec: 1.16x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 209 us: 1.19x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 148 us: 1.21x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.0 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.99 ms: 1.10x slower                                                      |
| django_template | 21.7 ms                                                         | 24.7 ms: 1.14x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 36.9 ms: 1.17x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 16.9 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 510 us: 15.91x faster                                                      |
| deepcopy                   | 220 us                                                          | 184 us: 1.19x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 20.1 us: 1.10x faster                                                      |
| async_tree_io_tg           | 605 ms                                                          | 562 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 1.99 us                                                         | 1.89 us: 1.06x faster                                                      |
| async_tree_none            | 218 ms                                                          | 209 ms: 1.04x faster                                                       |
| async_tree_memoization     | 264 ms                                                          | 254 ms: 1.04x faster                                                       |
| regex_dna                  | 119 ms                                                          | 115 ms: 1.03x faster                                                       |
| regex_effbot               | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                      |
| json_loads                 | 14.2 us                                                         | 14.0 us: 1.01x faster                                                      |
| pidigits                   | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| create_gc_cycles           | 888 us                                                          | 911 us: 1.03x slower                                                       |
| go                         | 82.1 ms                                                         | 85.4 ms: 1.04x slower                                                      |
| xml_etree_parse            | 90.9 ms                                                         | 94.7 ms: 1.04x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.69 sec: 1.04x slower                                                     |
| pathlib                    | 75.9 ms                                                         | 79.1 ms: 1.04x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 65.1 ms: 1.04x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 47.7 ms: 1.05x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 401 ms: 1.05x slower                                                       |
| spectral_norm              | 63.7 ms                                                         | 67.0 ms: 1.05x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 89.3 ms: 1.06x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 13.0 ms: 1.06x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 819 us: 1.07x slower                                                       |
| async_generators           | 223 ms                                                          | 238 ms: 1.07x slower                                                       |
| telco                      | 4.67 ms                                                         | 5.01 ms: 1.07x slower                                                      |
| generators                 | 19.6 ms                                                         | 21.1 ms: 1.08x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.72 us: 1.08x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 70.3 ms: 1.08x slower                                                      |
| python_startup             | 20.3 ms                                                         | 22.0 ms: 1.09x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.33 us: 1.09x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 58.2 ms: 1.09x slower                                                      |
| sympy_str                  | 159 ms                                                          | 175 ms: 1.10x slower                                                       |
| mako                       | 6.36 ms                                                         | 6.99 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 101 us                                                          | 111 us: 1.10x slower                                                       |
| 2to3                       | 207 ms                                                          | 228 ms: 1.10x slower                                                       |
| nqueens                    | 56.7 ms                                                         | 62.6 ms: 1.10x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 36.2 ms: 1.11x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 191 ms: 1.11x slower                                                       |
| mdp                        | 1.31 sec                                                        | 1.45 sec: 1.11x slower                                                     |
| pylint                     | 205 ms                                                          | 227 ms: 1.11x slower                                                       |
| meteor_contest             | 69.9 ms                                                         | 77.7 ms: 1.11x slower                                                      |
| scimark_lu                 | 56.6 ms                                                         | 63.0 ms: 1.11x slower                                                      |
| sympy_expand               | 271 ms                                                          | 301 ms: 1.11x slower                                                       |
| coroutines                 | 12.8 ms                                                         | 14.2 ms: 1.11x slower                                                      |
| coverage                   | 42.1 ms                                                         | 47.0 ms: 1.12x slower                                                      |
| asyncio_tcp                | 471 ms                                                          | 527 ms: 1.12x slower                                                       |
| dulwich_log                | 38.0 ms                                                         | 42.6 ms: 1.12x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                      |
| chaos                      | 38.4 ms                                                         | 43.0 ms: 1.12x slower                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.81 ms: 1.12x slower                                                      |
| xml_etree_process          | 36.4 ms                                                         | 41.0 ms: 1.13x slower                                                      |
| float                      | 49.7 ms                                                         | 56.0 ms: 1.13x slower                                                      |
| json_dumps                 | 5.61 ms                                                         | 6.35 ms: 1.13x slower                                                      |
| pyflate                    | 279 ms                                                          | 316 ms: 1.13x slower                                                       |
| tornado_http               | 81.8 ms                                                         | 92.8 ms: 1.13x slower                                                      |
| comprehensions             | 10.4 us                                                         | 11.8 us: 1.14x slower                                                      |
| django_template            | 21.7 ms                                                         | 24.7 ms: 1.14x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.09 ms: 1.15x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 544 ms: 1.15x slower                                                       |
| html5lib                   | 35.0 ms                                                         | 40.4 ms: 1.15x slower                                                      |
| pprint_pformat             | 966 ms                                                          | 1.11 sec: 1.15x slower                                                     |
| regex_compile              | 78.0 ms                                                         | 89.9 ms: 1.15x slower                                                      |
| pycparser                  | 754 ms                                                          | 870 ms: 1.15x slower                                                       |
| tomli_loads                | 1.35 sec                                                        | 1.57 sec: 1.16x slower                                                     |
| hexiom                     | 3.72 ms                                                         | 4.33 ms: 1.16x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 36.9 ms: 1.17x slower                                                      |
| raytrace                   | 162 ms                                                          | 190 ms: 1.17x slower                                                       |
| genshi_text                | 14.4 ms                                                         | 16.9 ms: 1.17x slower                                                      |
| sqlglot_parse              | 748 us                                                          | 879 us: 1.17x slower                                                       |
| fannkuch                   | 243 ms                                                          | 288 ms: 1.18x slower                                                       |
| scimark_sor                | 75.3 ms                                                         | 89.4 ms: 1.19x slower                                                      |
| deltablue                  | 1.88 ms                                                         | 2.24 ms: 1.19x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 209 us: 1.19x slower                                                       |
| scimark_fft                | 171 ms                                                          | 204 ms: 1.19x slower                                                       |
| logging_silent             | 52.9 ns                                                         | 63.3 ns: 1.20x slower                                                      |
| richards_super             | 30.2 ms                                                         | 36.5 ms: 1.21x slower                                                      |
| richards                   | 26.7 ms                                                         | 32.4 ms: 1.21x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 148 us: 1.21x slower                                                       |
| nbody                      | 67.6 ms                                                         | 85.1 ms: 1.26x slower                                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 50.3 ms: 1.29x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (8): regex_v8, json, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed, gc_traversal, async_tree_none_tg, asyncio_tcp_ssl
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown