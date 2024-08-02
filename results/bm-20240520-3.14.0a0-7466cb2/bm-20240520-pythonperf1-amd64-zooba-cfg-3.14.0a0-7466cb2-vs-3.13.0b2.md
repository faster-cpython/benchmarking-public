# Results vs. 3.13.0b2

- fork: zooba
- ref: cfg
- machine: windows-amd64
- commit hash: 7466cb2
- commit date: 2024-05-20
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 215 ms: 1.04x slower                                     |
| chameleon      | 4.80 ms                                                         | 5.03 ms: 1.05x slower                                    |
| docutils       | 1.63 sec                                                        | 1.74 sec: 1.07x slower                                   |
| html5lib       | 35.0 ms                                                         | 39.1 ms: 1.12x slower                                    |
| tornado_http   | 81.8 ms                                                         | 86.1 ms: 1.05x slower                                    |
| Geometric mean | (ref)                                                           | 1.07x slower                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io              | 588 ms                                                          | 618 ms: 1.05x slower                                     |
| async_tree_io_tg           | 605 ms                                                          | 640 ms: 1.06x slower                                     |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 405 ms: 1.06x slower                                     |
| async_tree_memoization     | 264 ms                                                          | 282 ms: 1.07x slower                                     |
| async_tree_none            | 218 ms                                                          | 234 ms: 1.07x slower                                     |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 420 ms: 1.08x slower                                     |
| async_tree_memoization_tg  | 258 ms                                                          | 279 ms: 1.08x slower                                     |
| async_tree_none_tg         | 202 ms                                                          | 220 ms: 1.09x slower                                     |
| Geometric mean             | (ref)                                                           | 1.07x slower                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                     |
| nbody          | 67.6 ms                                                         | 72.4 ms: 1.07x slower                                    |
| float          | 49.7 ms                                                         | 55.6 ms: 1.12x slower                                    |
| Geometric mean | (ref)                                                           | 1.06x slower                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 119 ms: 1.00x slower                                     |
| regex_effbot   | 1.58 ms                                                         | 1.66 ms: 1.05x slower                                    |
| regex_compile  | 78.0 ms                                                         | 85.5 ms: 1.10x slower                                    |
| Geometric mean | (ref)                                                           | 1.02x slower                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------:|
| pickle               | 7.11 us                                                         | 7.23 us: 1.02x slower                                    |
| pickle_dict          | 18.1 us                                                         | 18.7 us: 1.03x slower                                    |
| json_loads           | 14.2 us                                                         | 14.8 us: 1.04x slower                                    |
| pickle_list          | 2.90 us                                                         | 3.14 us: 1.08x slower                                    |
| unpickle             | 8.40 us                                                         | 9.08 us: 1.08x slower                                    |
| json_dumps           | 5.61 ms                                                         | 6.08 ms: 1.08x slower                                    |
| tomli_loads          | 1.35 sec                                                        | 1.46 sec: 1.08x slower                                   |
| xml_etree_process    | 36.4 ms                                                         | 39.7 ms: 1.09x slower                                    |
| pickle_pure_python   | 175 us                                                          | 192 us: 1.09x slower                                     |
| xml_etree_generate   | 53.2 ms                                                         | 58.2 ms: 1.10x slower                                    |
| unpickle_list        | 2.62 us                                                         | 2.90 us: 1.11x slower                                    |
| unpickle_pure_python | 122 us                                                          | 137 us: 1.12x slower                                     |
| xml_etree_iterparse  | 62.3 ms                                                         | 70.9 ms: 1.14x slower                                    |
| xml_etree_parse      | 90.9 ms                                                         | 104 ms: 1.14x slower                                     |
| Geometric mean       | (ref)                                                           | 1.09x slower                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.7 ms: 1.07x slower                                    |
| python_startup_no_site | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                    |
| Geometric mean         | (ref)                                                           | 1.09x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_xml      | 31.6 ms                                                         | 32.8 ms: 1.04x slower                                    |
| django_template | 21.7 ms                                                         | 23.0 ms: 1.06x slower                                    |
| genshi_text     | 14.4 ms                                                         | 15.3 ms: 1.07x slower                                    |
| mako            | 6.36 ms                                                         | 6.96 ms: 1.09x slower                                    |
| Geometric mean  | (ref)                                                           | 1.06x slower                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 521 us: 15.57x faster                                    |
| pycparser                  | 754 ms                                                          | 687 ms: 1.10x faster                                     |
| flaskblogging              | 2.03 sec                                                        | 2.03 sec: 1.00x faster                                   |
| regex_dna                  | 119 ms                                                          | 119 ms: 1.00x slower                                     |
| pidigits                   | 150 ms                                                          | 151 ms: 1.01x slower                                     |
| pickle                     | 7.11 us                                                         | 7.23 us: 1.02x slower                                    |
| raytrace                   | 162 ms                                                          | 166 ms: 1.03x slower                                     |
| generators                 | 19.6 ms                                                         | 20.1 ms: 1.03x slower                                    |
| pickle_dict                | 18.1 us                                                         | 18.7 us: 1.03x slower                                    |
| chaos                      | 38.4 ms                                                         | 39.5 ms: 1.03x slower                                    |
| coroutines                 | 12.8 ms                                                         | 13.2 ms: 1.03x slower                                    |
| logging_format             | 6.22 us                                                         | 6.44 us: 1.03x slower                                    |
| genshi_xml                 | 31.6 ms                                                         | 32.8 ms: 1.04x slower                                    |
| logging_simple             | 5.78 us                                                         | 6.01 us: 1.04x slower                                    |
| 2to3                       | 207 ms                                                          | 215 ms: 1.04x slower                                     |
| json_loads                 | 14.2 us                                                         | 14.8 us: 1.04x slower                                    |
| richards_super             | 30.2 ms                                                         | 31.5 ms: 1.04x slower                                    |
| regex_effbot               | 1.58 ms                                                         | 1.66 ms: 1.05x slower                                    |
| go                         | 82.1 ms                                                         | 85.9 ms: 1.05x slower                                    |
| chameleon                  | 4.80 ms                                                         | 5.03 ms: 1.05x slower                                    |
| nqueens                    | 56.7 ms                                                         | 59.4 ms: 1.05x slower                                    |
| async_tree_io              | 588 ms                                                          | 618 ms: 1.05x slower                                     |
| richards                   | 26.7 ms                                                         | 28.1 ms: 1.05x slower                                    |
| pathlib                    | 75.9 ms                                                         | 79.8 ms: 1.05x slower                                    |
| tornado_http               | 81.8 ms                                                         | 86.1 ms: 1.05x slower                                    |
| deepcopy_reduce            | 1.99 us                                                         | 2.10 us: 1.05x slower                                    |
| async_tree_io_tg           | 605 ms                                                          | 640 ms: 1.06x slower                                     |
| sqlglot_parse              | 748 us                                                          | 792 us: 1.06x slower                                     |
| django_template            | 21.7 ms                                                         | 23.0 ms: 1.06x slower                                    |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 405 ms: 1.06x slower                                     |
| sqlglot_transpile          | 955 us                                                          | 1.01 ms: 1.06x slower                                    |
| sqlite_synth               | 1.60 us                                                         | 1.69 us: 1.06x slower                                    |
| meteor_contest             | 69.9 ms                                                         | 74.3 ms: 1.06x slower                                    |
| pylint                     | 205 ms                                                          | 218 ms: 1.06x slower                                     |
| genshi_text                | 14.4 ms                                                         | 15.3 ms: 1.07x slower                                    |
| sqlglot_normalize          | 173 ms                                                          | 184 ms: 1.07x slower                                     |
| comprehensions             | 10.4 us                                                         | 11.1 us: 1.07x slower                                    |
| async_tree_memoization     | 264 ms                                                          | 282 ms: 1.07x slower                                     |
| deepcopy                   | 220 us                                                          | 235 us: 1.07x slower                                     |
| docutils                   | 1.63 sec                                                        | 1.74 sec: 1.07x slower                                   |
| nbody                      | 67.6 ms                                                         | 72.4 ms: 1.07x slower                                    |
| python_startup             | 20.3 ms                                                         | 21.7 ms: 1.07x slower                                    |
| sqlglot_optimize           | 32.7 ms                                                         | 35.0 ms: 1.07x slower                                    |
| async_tree_none            | 218 ms                                                          | 234 ms: 1.07x slower                                     |
| sympy_integrate            | 12.2 ms                                                         | 13.2 ms: 1.08x slower                                    |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 420 ms: 1.08x slower                                     |
| pickle_list                | 2.90 us                                                         | 3.14 us: 1.08x slower                                    |
| async_tree_memoization_tg  | 258 ms                                                          | 279 ms: 1.08x slower                                     |
| unpickle                   | 8.40 us                                                         | 9.08 us: 1.08x slower                                    |
| typing_runtime_protocols   | 101 us                                                          | 109 us: 1.08x slower                                     |
| pyflate                    | 279 ms                                                          | 302 ms: 1.08x slower                                     |
| json_dumps                 | 5.61 ms                                                         | 6.08 ms: 1.08x slower                                    |
| telco                      | 4.67 ms                                                         | 5.05 ms: 1.08x slower                                    |
| tomli_loads                | 1.35 sec                                                        | 1.46 sec: 1.08x slower                                   |
| hexiom                     | 3.72 ms                                                         | 4.04 ms: 1.08x slower                                    |
| async_tree_none_tg         | 202 ms                                                          | 220 ms: 1.09x slower                                     |
| fannkuch                   | 243 ms                                                          | 265 ms: 1.09x slower                                     |
| xml_etree_process          | 36.4 ms                                                         | 39.7 ms: 1.09x slower                                    |
| bench_mp_pool              | 64.8 ms                                                         | 70.6 ms: 1.09x slower                                    |
| pprint_pformat             | 966 ms                                                          | 1.05 sec: 1.09x slower                                   |
| sympy_sum                  | 84.4 ms                                                         | 92.3 ms: 1.09x slower                                    |
| pprint_safe_repr           | 474 ms                                                          | 518 ms: 1.09x slower                                     |
| mako                       | 6.36 ms                                                         | 6.96 ms: 1.09x slower                                    |
| pickle_pure_python         | 175 us                                                          | 192 us: 1.09x slower                                     |
| xml_etree_generate         | 53.2 ms                                                         | 58.2 ms: 1.10x slower                                    |
| regex_compile              | 78.0 ms                                                         | 85.5 ms: 1.10x slower                                    |
| logging_silent             | 52.9 ns                                                         | 58.1 ns: 1.10x slower                                    |
| spectral_norm              | 63.7 ms                                                         | 70.0 ms: 1.10x slower                                    |
| deltablue                  | 1.88 ms                                                         | 2.07 ms: 1.10x slower                                    |
| bench_thread_pool          | 768 us                                                          | 844 us: 1.10x slower                                     |
| python_startup_no_site     | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                    |
| crypto_pyaes               | 45.5 ms                                                         | 50.1 ms: 1.10x slower                                    |
| unpickle_list              | 2.62 us                                                         | 2.90 us: 1.11x slower                                    |
| scimark_sor                | 75.3 ms                                                         | 83.8 ms: 1.11x slower                                    |
| coverage                   | 42.1 ms                                                         | 46.9 ms: 1.12x slower                                    |
| float                      | 49.7 ms                                                         | 55.6 ms: 1.12x slower                                    |
| html5lib                   | 35.0 ms                                                         | 39.1 ms: 1.12x slower                                    |
| scimark_monte_carlo        | 39.1 ms                                                         | 43.8 ms: 1.12x slower                                    |
| unpickle_pure_python       | 122 us                                                          | 137 us: 1.12x slower                                     |
| sympy_str                  | 159 ms                                                          | 179 ms: 1.13x slower                                     |
| deepcopy_memo              | 22.1 us                                                         | 24.9 us: 1.13x slower                                    |
| scimark_lu                 | 56.6 ms                                                         | 63.9 ms: 1.13x slower                                    |
| async_generators           | 223 ms                                                          | 253 ms: 1.13x slower                                     |
| sympy_expand               | 271 ms                                                          | 307 ms: 1.13x slower                                     |
| xml_etree_iterparse        | 62.3 ms                                                         | 70.9 ms: 1.14x slower                                    |
| xml_etree_parse            | 90.9 ms                                                         | 104 ms: 1.14x slower                                     |
| create_gc_cycles           | 888 us                                                          | 1.08 ms: 1.21x slower                                    |
| mdp                        | 1.31 sec                                                        | 1.61 sec: 1.22x slower                                   |
| scimark_fft                | 171 ms                                                          | 212 ms: 1.24x slower                                     |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 3.14 ms: 1.26x slower                                    |
| gc_traversal               | 1.55 ms                                                         | 2.80 ms: 1.80x slower                                    |
| Geometric mean             | (ref)                                                           | 1.05x slower                                             |

Benchmark hidden because not significant (4): regex_v8, json, asyncio_tcp, asyncio_tcp_ssl
Ignored benchmarks (3) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, dulwich_log, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown