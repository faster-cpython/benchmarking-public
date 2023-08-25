
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0b3
- machine: windows-amd64
- commit hash: eb0004c
- commit date: 2022-06-01
- overall geometric mean: 1.05x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 212 ms: 1.01x slower                                            |
| chameleon      | 5.11 ms                                                     | 5.63 ms: 1.10x slower                                           |
| docutils       | 1.60 sec                                                    | 1.66 sec: 1.04x slower                                          |
| html5lib       | 37.5 ms                                                     | 41.2 ms: 1.10x slower                                           |
| tornado_http   | 91.8 ms                                                     | 94.8 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                       | 1.06x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 71.9 ms: 1.03x slower                                           |
| pidigits       | 148 ms                                                      | 154 ms: 1.04x slower                                            |
| float          | 54.6 ms                                                     | 57.2 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                       | 1.04x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 94.2 ms: 1.04x slower                                           |
| regex_effbot   | 1.50 ms                                                     | 1.62 ms: 1.08x slower                                           |
| regex_v8       | 13.8 ms                                                     | 15.2 ms: 1.10x slower                                           |
| regex_dna      | 115 ms                                                      | 127 ms: 1.10x slower                                            |
| Geometric mean | (ref)                                                       | 1.08x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_dict          | 18.5 us                                                     | 17.7 us: 1.04x faster                                           |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.3 ms: 1.01x slower                                           |
| xml_etree_parse      | 95.9 ms                                                     | 97.4 ms: 1.02x slower                                           |
| unpickle             | 8.09 us                                                     | 8.33 us: 1.03x slower                                           |
| pickle               | 6.61 us                                                     | 6.83 us: 1.03x slower                                           |
| unpickle_pure_python | 152 us                                                      | 158 us: 1.04x slower                                            |
| xml_etree_process    | 37.1 ms                                                     | 38.9 ms: 1.05x slower                                           |
| pickle_list          | 2.68 us                                                     | 2.81 us: 1.05x slower                                           |
| json_dumps           | 7.56 ms                                                     | 7.98 ms: 1.06x slower                                           |
| pickle_pure_python   | 200 us                                                      | 212 us: 1.06x slower                                            |
| unpickle_list        | 2.55 us                                                     | 2.71 us: 1.06x slower                                           |
| xml_etree_generate   | 52.2 ms                                                     | 55.8 ms: 1.07x slower                                           |
| json_loads           | 12.9 us                                                     | 14.2 us: 1.10x slower                                           |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.4 ms: 1.03x slower                                           |
| python_startup         | 18.7 ms                                                     | 19.4 ms: 1.04x slower                                           |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 7.26 ms                                                     | 7.38 ms: 1.02x slower                                           |
| django_template | 24.1 ms                                                     | 25.4 ms: 1.05x slower                                           |
| genshi_text     | 17.0 ms                                                     | 18.6 ms: 1.10x slower                                           |
| genshi_xml      | 37.3 ms                                                     | 41.0 ms: 1.10x slower                                           |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                    |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 36.8 ns: 1.25x faster                                           |
| logging_simple          | 6.61 us                                                     | 5.96 us: 1.11x faster                                           |
| logging_format          | 7.01 us                                                     | 6.43 us: 1.09x faster                                           |
| pickle_dict             | 18.5 us                                                     | 17.7 us: 1.04x faster                                           |
| mdp                     | 1.67 sec                                                    | 1.66 sec: 1.01x faster                                          |
| flaskblogging           | 2.04 sec                                                    | 2.05 sec: 1.00x slower                                          |
| xml_etree_iterparse     | 62.6 ms                                                     | 63.3 ms: 1.01x slower                                           |
| sqlalchemy_imperative   | 10.2 ms                                                     | 10.3 ms: 1.01x slower                                           |
| 2to3                    | 209 ms                                                      | 212 ms: 1.01x slower                                            |
| mako                    | 7.26 ms                                                     | 7.38 ms: 1.02x slower                                           |
| xml_etree_parse         | 95.9 ms                                                     | 97.4 ms: 1.02x slower                                           |
| scimark_monte_carlo     | 44.6 ms                                                     | 45.4 ms: 1.02x slower                                           |
| gc_traversal            | 1.46 ms                                                     | 1.49 ms: 1.02x slower                                           |
| raytrace                | 211 ms                                                      | 215 ms: 1.02x slower                                            |
| dulwich_log             | 44.5 ms                                                     | 45.5 ms: 1.02x slower                                           |
| nbody                   | 70.0 ms                                                     | 71.9 ms: 1.03x slower                                           |
| sqlglot_optimize        | 34.9 ms                                                     | 35.9 ms: 1.03x slower                                           |
| scimark_sor             | 75.6 ms                                                     | 77.7 ms: 1.03x slower                                           |
| unpickle                | 8.09 us                                                     | 8.33 us: 1.03x slower                                           |
| sympy_integrate         | 13.8 ms                                                     | 14.2 ms: 1.03x slower                                           |
| pathlib                 | 71.4 ms                                                     | 73.6 ms: 1.03x slower                                           |
| meteor_contest          | 74.7 ms                                                     | 77.1 ms: 1.03x slower                                           |
| tornado_http            | 91.8 ms                                                     | 94.8 ms: 1.03x slower                                           |
| python_startup_no_site  | 15.9 ms                                                     | 16.4 ms: 1.03x slower                                           |
| pickle                  | 6.61 us                                                     | 6.83 us: 1.03x slower                                           |
| deepcopy_memo           | 25.2 us                                                     | 26.0 us: 1.03x slower                                           |
| sqlite_synth            | 1.68 us                                                     | 1.74 us: 1.04x slower                                           |
| sympy_expand            | 295 ms                                                      | 306 ms: 1.04x slower                                            |
| pidigits                | 148 ms                                                      | 154 ms: 1.04x slower                                            |
| python_startup          | 18.7 ms                                                     | 19.4 ms: 1.04x slower                                           |
| async_tree_cpu_io_mixed | 501 ms                                                      | 519 ms: 1.04x slower                                            |
| docutils                | 1.60 sec                                                    | 1.66 sec: 1.04x slower                                          |
| regex_compile           | 90.6 ms                                                     | 94.2 ms: 1.04x slower                                           |
| unpickle_pure_python    | 152 us                                                      | 158 us: 1.04x slower                                            |
| logging_silent          | 69.8 ns                                                     | 72.7 ns: 1.04x slower                                           |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.68 ms: 1.04x slower                                           |
| sqlglot_normalize       | 190 ms                                                      | 198 ms: 1.04x slower                                            |
| sympy_str               | 182 ms                                                      | 190 ms: 1.04x slower                                            |
| bench_thread_pool       | 852 us                                                      | 890 us: 1.04x slower                                            |
| float                   | 54.6 ms                                                     | 57.2 ms: 1.05x slower                                           |
| pyflate                 | 304 ms                                                      | 318 ms: 1.05x slower                                            |
| generators              | 33.8 ms                                                     | 35.4 ms: 1.05x slower                                           |
| thrift                  | 491 us                                                      | 514 us: 1.05x slower                                            |
| xml_etree_process       | 37.1 ms                                                     | 38.9 ms: 1.05x slower                                           |
| pickle_list             | 2.68 us                                                     | 2.81 us: 1.05x slower                                           |
| spectral_norm           | 67.9 ms                                                     | 71.4 ms: 1.05x slower                                           |
| django_template         | 24.1 ms                                                     | 25.4 ms: 1.05x slower                                           |
| json_dumps              | 7.56 ms                                                     | 7.98 ms: 1.06x slower                                           |
| sqlalchemy_declarative  | 81.5 ms                                                     | 86.0 ms: 1.06x slower                                           |
| scimark_fft             | 178 ms                                                      | 188 ms: 1.06x slower                                            |
| async_tree_none         | 320 ms                                                      | 339 ms: 1.06x slower                                            |
| telco                   | 3.90 ms                                                     | 4.13 ms: 1.06x slower                                           |
| hexiom                  | 4.55 ms                                                     | 4.82 ms: 1.06x slower                                           |
| pprint_safe_repr        | 512 ms                                                      | 541 ms: 1.06x slower                                            |
| pickle_pure_python      | 200 us                                                      | 212 us: 1.06x slower                                            |
| dask                    | 264 ms                                                      | 281 ms: 1.06x slower                                            |
| pycparser               | 691 ms                                                      | 735 ms: 1.06x slower                                            |
| unpickle_list           | 2.55 us                                                     | 2.71 us: 1.06x slower                                           |
| deltablue               | 2.61 ms                                                     | 2.78 ms: 1.06x slower                                           |
| xml_etree_generate      | 52.2 ms                                                     | 55.8 ms: 1.07x slower                                           |
| coroutines              | 14.6 ms                                                     | 15.7 ms: 1.07x slower                                           |
| crypto_pyaes            | 47.6 ms                                                     | 50.9 ms: 1.07x slower                                           |
| go                      | 97.3 ms                                                     | 104 ms: 1.07x slower                                            |
| deepcopy_reduce         | 2.07 us                                                     | 2.22 us: 1.07x slower                                           |
| bench_mp_pool           | 62.5 ms                                                     | 67.0 ms: 1.07x slower                                           |
| deepcopy                | 246 us                                                      | 265 us: 1.08x slower                                            |
| async_generators        | 178 ms                                                      | 192 ms: 1.08x slower                                            |
| regex_effbot            | 1.50 ms                                                     | 1.62 ms: 1.08x slower                                           |
| pprint_pformat          | 1.04 sec                                                    | 1.12 sec: 1.08x slower                                          |
| async_tree_memoization  | 371 ms                                                      | 402 ms: 1.09x slower                                            |
| asyncio_tcp             | 699 ms                                                      | 762 ms: 1.09x slower                                            |
| nqueens                 | 64.9 ms                                                     | 71.0 ms: 1.09x slower                                           |
| genshi_text             | 17.0 ms                                                     | 18.6 ms: 1.10x slower                                           |
| regex_v8                | 13.8 ms                                                     | 15.2 ms: 1.10x slower                                           |
| html5lib                | 37.5 ms                                                     | 41.2 ms: 1.10x slower                                           |
| genshi_xml              | 37.3 ms                                                     | 41.0 ms: 1.10x slower                                           |
| json_loads              | 12.9 us                                                     | 14.2 us: 1.10x slower                                           |
| chaos                   | 47.1 ms                                                     | 51.8 ms: 1.10x slower                                           |
| regex_dna               | 115 ms                                                      | 127 ms: 1.10x slower                                            |
| chameleon               | 5.11 ms                                                     | 5.63 ms: 1.10x slower                                           |
| fannkuch                | 252 ms                                                      | 278 ms: 1.10x slower                                            |
| comprehensions          | 15.9 us                                                     | 18.7 us: 1.18x slower                                           |
| sqlglot_transpile       | 1.16 ms                                                     | 1.41 ms: 1.21x slower                                           |
| sqlglot_parse           | 952 us                                                      | 1.21 ms: 1.27x slower                                           |
| mypy2                   | 229 ms                                                      | 293 ms: 1.28x slower                                            |
| coverage                | 55.9 ms                                                     | 108 ms: 1.93x slower                                            |
| Geometric mean          | (ref)                                                       | 1.05x slower                                                    |

Benchmark hidden because not significant (8): create_gc_cycles, aiohttp, scimark_lu, json, richards, async_tree_io, sympy_sum, pylint
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x
