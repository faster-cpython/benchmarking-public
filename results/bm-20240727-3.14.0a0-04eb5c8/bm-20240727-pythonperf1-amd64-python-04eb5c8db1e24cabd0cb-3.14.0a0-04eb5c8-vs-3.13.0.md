# Results vs. 3.13.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: windows-amd64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 234 ms: 1.08x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.75 sec: 1.11x slower                                                     |
| html5lib       | 38.6 ms                                                     | 42.0 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 533 ms: 1.23x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 249 ms: 1.16x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 196 ms: 1.05x faster                                                       |
| async_tree_none            | 223 ms                                                      | 216 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 391 ms: 1.04x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 548 ms: 1.07x slower                                                       |
| async_tree_io              | 521 ms                                                      | 559 ms: 1.07x slower                                                       |
| async_generators           | 223 ms                                                      | 240 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 48.1 ms                                                     | 55.9 ms: 1.16x slower                                                      |
| nbody          | 64.5 ms                                                     | 83.2 ms: 1.29x slower                                                      |
| Geometric mean | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                      |
| regex_dna      | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 90.4 ms: 1.13x slower                                                      |
| regex_v8       | 14.7 ms                                                     | 17.5 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 62.3 ms                                                     | 65.9 ms: 1.06x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.26 ms: 1.09x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 58.9 ms: 1.10x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.2 ms: 1.13x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 213 us: 1.16x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.59 sec: 1.17x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 151 us: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.4 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 36.9 ms: 1.13x slower                                                      |
| django_template | 21.8 ms                                                     | 24.6 ms: 1.13x slower                                                      |
| mako            | 6.24 ms                                                     | 7.07 ms: 1.13x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.3 ms: 1.16x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 519 us: 16.73x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 533 ms: 1.23x faster                                                       |
| deepcopy                   | 223 us                                                      | 187 us: 1.19x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 249 ms: 1.16x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.87 us: 1.08x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 20.6 us: 1.06x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 196 ms: 1.05x faster                                                       |
| async_tree_none            | 223 ms                                                      | 216 ms: 1.03x faster                                                       |
| bench_thread_pool          | 828 us                                                      | 805 us: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                      |
| coverage                   | 46.7 ms                                                     | 47.0 ms: 1.01x slower                                                      |
| telco                      | 4.85 ms                                                     | 4.89 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| python_startup_no_site     | 17.8 ms                                                     | 18.4 ms: 1.04x slower                                                      |
| regex_dna                  | 114 ms                                                      | 119 ms: 1.04x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 391 ms: 1.04x slower                                                       |
| bench_mp_pool              | 69.6 ms                                                     | 72.7 ms: 1.04x slower                                                      |
| generators                 | 19.5 ms                                                     | 20.3 ms: 1.04x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 90.6 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 65.9 ms: 1.06x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 42.7 ms: 1.06x slower                                                      |
| json                       | 2.98 ms                                                     | 3.17 ms: 1.06x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 77.0 ms: 1.06x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 548 ms: 1.07x slower                                                       |
| async_tree_io              | 521 ms                                                      | 559 ms: 1.07x slower                                                       |
| sympy_expand               | 285 ms                                                      | 306 ms: 1.07x slower                                                       |
| sympy_str                  | 166 ms                                                      | 178 ms: 1.07x slower                                                       |
| async_generators           | 223 ms                                                      | 240 ms: 1.08x slower                                                       |
| 2to3                       | 217 ms                                                      | 234 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 6.26 ms: 1.09x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.51 sec: 1.09x slower                                                     |
| html5lib                   | 38.6 ms                                                     | 42.0 ms: 1.09x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 908 us: 1.10x slower                                                       |
| pycparser                  | 758 ms                                                      | 834 ms: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 58.9 ms: 1.10x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.75 sec: 1.11x slower                                                     |
| sqlglot_optimize           | 33.1 ms                                                     | 36.8 ms: 1.11x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.43 us: 1.12x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 36.9 ms: 1.13x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 90.4 ms: 1.13x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 41.2 ms: 1.13x slower                                                      |
| django_template            | 21.8 ms                                                     | 24.6 ms: 1.13x slower                                                      |
| mako                       | 6.24 ms                                                     | 7.07 ms: 1.13x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.98 us: 1.13x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 114 us: 1.13x slower                                                       |
| go                         | 84.6 ms                                                     | 96.8 ms: 1.14x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 196 ms: 1.15x slower                                                       |
| pprint_safe_repr           | 493 ms                                                      | 566 ms: 1.15x slower                                                       |
| pyflate                    | 275 ms                                                      | 319 ms: 1.16x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 64.5 ms: 1.16x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 213 us: 1.16x slower                                                       |
| float                      | 48.1 ms                                                     | 55.9 ms: 1.16x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 886 us: 1.16x slower                                                       |
| pprint_pformat             | 991 ms                                                      | 1.15 sec: 1.16x slower                                                     |
| genshi_text                | 14.9 ms                                                     | 17.3 ms: 1.16x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.11 ms: 1.17x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.59 sec: 1.17x slower                                                     |
| scimark_lu                 | 54.0 ms                                                     | 63.2 ms: 1.17x slower                                                      |
| chaos                      | 37.9 ms                                                     | 44.4 ms: 1.17x slower                                                      |
| comprehensions             | 10.2 us                                                     | 12.0 us: 1.17x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 50.6 ms: 1.18x slower                                                      |
| scimark_fft                | 174 ms                                                      | 206 ms: 1.18x slower                                                       |
| fannkuch                   | 245 ms                                                      | 291 ms: 1.19x slower                                                       |
| unpickle_pure_python       | 127 us                                                      | 151 us: 1.19x slower                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.79 ms: 1.19x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 17.5 ms: 1.19x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 70.9 ms: 1.20x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.43 ms: 1.20x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.25 ms: 1.21x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 88.0 ms: 1.22x slower                                                      |
| richards                   | 26.0 ms                                                     | 32.3 ms: 1.24x slower                                                      |
| richards_super             | 29.3 ms                                                     | 36.4 ms: 1.24x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 63.7 ns: 1.25x slower                                                      |
| raytrace                   | 156 ms                                                      | 197 ms: 1.26x slower                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 50.9 ms: 1.26x slower                                                      |
| nbody                      | 64.5 ms                                                     | 83.2 ms: 1.29x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (10): asyncio_tcp_ssl, async_tree_memoization, xml_etree_parse, pathlib, async_tree_cpu_io_mixed, python_startup, gc_traversal, json_loads, tornado_http, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown