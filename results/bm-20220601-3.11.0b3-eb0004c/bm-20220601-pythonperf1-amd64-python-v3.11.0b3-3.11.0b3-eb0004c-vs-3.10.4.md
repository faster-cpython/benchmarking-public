
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0b3
- machine: windows-amd64
- commit hash: eb0004c
- commit date: 2022-06-01
- overall geometric mean: 1.06x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 212 ms: 1.12x faster                                            |
| chameleon      | 5.92 ms                                                     | 5.63 ms: 1.05x faster                                           |
| docutils       | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                          |
| html5lib       | 46.5 ms                                                     | 41.2 ms: 1.13x faster                                           |
| tornado_http   | 109 ms                                                      | 94.8 ms: 1.15x faster                                           |
| Geometric mean | (ref)                                                       | 1.12x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 57.2 ms: 1.05x faster                                           |
| nbody          | 69.3 ms                                                     | 71.9 ms: 1.04x slower                                           |
| pidigits       | 145 ms                                                      | 154 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                       | 1.01x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 94.2 ms: 1.10x faster                                           |
| regex_dna      | 132 ms                                                      | 127 ms: 1.04x faster                                            |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                           |
| regex_v8       | 15.0 ms                                                     | 15.2 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                       | 1.04x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 257 us                                                      | 212 us: 1.21x faster                                            |
| xml_etree_process    | 43.4 ms                                                     | 38.9 ms: 1.12x faster                                           |
| unpickle             | 9.17 us                                                     | 8.33 us: 1.10x faster                                           |
| unpickle_pure_python | 171 us                                                      | 158 us: 1.08x faster                                            |
| json_dumps           | 8.50 ms                                                     | 7.98 ms: 1.07x faster                                           |
| xml_etree_parse      | 102 ms                                                      | 97.4 ms: 1.04x faster                                           |
| unpickle_list        | 2.81 us                                                     | 2.71 us: 1.04x faster                                           |
| xml_etree_generate   | 54.5 ms                                                     | 55.8 ms: 1.02x slower                                           |
| pickle_dict          | 16.9 us                                                     | 17.7 us: 1.05x slower                                           |
| pickle_list          | 2.59 us                                                     | 2.81 us: 1.09x slower                                           |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                    |

Benchmark hidden because not significant (3): xml_etree_iterparse, json_loads, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.4 ms: 1.03x faster                                           |
| python_startup_no_site | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                           |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 7.38 ms: 1.19x faster                                           |
| django_template | 28.2 ms                                                     | 25.4 ms: 1.11x faster                                           |
| genshi_text     | 19.0 ms                                                     | 18.6 ms: 1.03x faster                                           |
| genshi_xml      | 40.5 ms                                                     | 41.0 ms: 1.01x slower                                           |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                    |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.78 ms: 1.50x faster                                           |
| async_tree_io           | 1.07 sec                                                    | 781 ms: 1.36x faster                                            |
| scimark_sor             | 105 ms                                                      | 77.7 ms: 1.35x faster                                           |
| scimark_lu              | 85.4 ms                                                     | 63.6 ms: 1.34x faster                                           |
| richards                | 41.2 ms                                                     | 30.7 ms: 1.34x faster                                           |
| logging_silent          | 96.4 ns                                                     | 72.7 ns: 1.33x faster                                           |
| go                      | 136 ms                                                      | 104 ms: 1.31x faster                                            |
| raytrace                | 271 ms                                                      | 215 ms: 1.26x faster                                            |
| async_tree_none         | 420 ms                                                      | 339 ms: 1.24x faster                                            |
| async_tree_memoization  | 497 ms                                                      | 402 ms: 1.24x faster                                            |
| scimark_monte_carlo     | 55.9 ms                                                     | 45.4 ms: 1.23x faster                                           |
| crypto_pyaes            | 62.3 ms                                                     | 50.9 ms: 1.22x faster                                           |
| pyflate                 | 387 ms                                                      | 318 ms: 1.22x faster                                            |
| pickle_pure_python      | 257 us                                                      | 212 us: 1.21x faster                                            |
| mypy2                   | 352 ms                                                      | 293 ms: 1.20x faster                                            |
| thrift                  | 615 us                                                      | 514 us: 1.20x faster                                            |
| mako                    | 8.80 ms                                                     | 7.38 ms: 1.19x faster                                           |
| pycparser               | 868 ms                                                      | 735 ms: 1.18x faster                                            |
| async_tree_cpu_io_mixed | 609 ms                                                      | 519 ms: 1.17x faster                                            |
| async_generators        | 224 ms                                                      | 192 ms: 1.17x faster                                            |
| tornado_http            | 109 ms                                                      | 94.8 ms: 1.15x faster                                           |
| hexiom                  | 5.52 ms                                                     | 4.82 ms: 1.14x faster                                           |
| create_gc_cycles        | 782 us                                                      | 686 us: 1.14x faster                                            |
| docutils                | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                          |
| chaos                   | 58.9 ms                                                     | 51.8 ms: 1.14x faster                                           |
| html5lib                | 46.5 ms                                                     | 41.2 ms: 1.13x faster                                           |
| aiohttp                 | 1.01 ms                                                     | 897 us: 1.12x faster                                            |
| 2to3                    | 237 ms                                                      | 212 ms: 1.12x faster                                            |
| xml_etree_process       | 43.4 ms                                                     | 38.9 ms: 1.12x faster                                           |
| django_template         | 28.2 ms                                                     | 25.4 ms: 1.11x faster                                           |
| sqlalchemy_declarative  | 95.4 ms                                                     | 86.0 ms: 1.11x faster                                           |
| unpickle                | 9.17 us                                                     | 8.33 us: 1.10x faster                                           |
| regex_compile           | 103 ms                                                      | 94.2 ms: 1.10x faster                                           |
| deepcopy_memo           | 28.5 us                                                     | 26.0 us: 1.10x faster                                           |
| spectral_norm           | 78.0 ms                                                     | 71.4 ms: 1.09x faster                                           |
| pprint_safe_repr        | 589 ms                                                      | 541 ms: 1.09x faster                                            |
| sqlglot_optimize        | 39.0 ms                                                     | 35.9 ms: 1.09x faster                                           |
| dask                    | 305 ms                                                      | 281 ms: 1.08x faster                                            |
| unpickle_pure_python    | 171 us                                                      | 158 us: 1.08x faster                                            |
| pprint_pformat          | 1.21 sec                                                    | 1.12 sec: 1.07x faster                                          |
| json_dumps              | 8.50 ms                                                     | 7.98 ms: 1.07x faster                                           |
| bench_thread_pool       | 946 us                                                      | 890 us: 1.06x faster                                            |
| sqlalchemy_imperative   | 11.0 ms                                                     | 10.3 ms: 1.06x faster                                           |
| sqlite_synth            | 1.84 us                                                     | 1.74 us: 1.06x faster                                           |
| float                   | 60.2 ms                                                     | 57.2 ms: 1.05x faster                                           |
| chameleon               | 5.92 ms                                                     | 5.63 ms: 1.05x faster                                           |
| pathlib                 | 77.4 ms                                                     | 73.6 ms: 1.05x faster                                           |
| pylint                  | 347 ms                                                      | 331 ms: 1.05x faster                                            |
| dulwich_log             | 47.6 ms                                                     | 45.5 ms: 1.05x faster                                           |
| xml_etree_parse         | 102 ms                                                      | 97.4 ms: 1.04x faster                                           |
| sympy_integrate         | 14.8 ms                                                     | 14.2 ms: 1.04x faster                                           |
| logging_simple          | 6.20 us                                                     | 5.96 us: 1.04x faster                                           |
| regex_dna               | 132 ms                                                      | 127 ms: 1.04x faster                                            |
| sqlglot_transpile       | 1.46 ms                                                     | 1.41 ms: 1.04x faster                                           |
| unpickle_list           | 2.81 us                                                     | 2.71 us: 1.04x faster                                           |
| sympy_sum               | 104 ms                                                      | 100 ms: 1.04x faster                                            |
| logging_format          | 6.66 us                                                     | 6.43 us: 1.04x faster                                           |
| mdp                     | 1.71 sec                                                    | 1.66 sec: 1.03x faster                                          |
| python_startup          | 20.0 ms                                                     | 19.4 ms: 1.03x faster                                           |
| sympy_expand            | 315 ms                                                      | 306 ms: 1.03x faster                                            |
| regex_effbot            | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                           |
| unpack_sequence         | 37.8 ns                                                     | 36.8 ns: 1.03x faster                                           |
| genshi_text             | 19.0 ms                                                     | 18.6 ms: 1.03x faster                                           |
| scimark_fft             | 193 ms                                                      | 188 ms: 1.03x faster                                            |
| sqlglot_normalize       | 202 ms                                                      | 198 ms: 1.02x faster                                            |
| coroutines              | 15.9 ms                                                     | 15.7 ms: 1.02x faster                                           |
| sqlglot_parse           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                           |
| flaskblogging           | 2.04 sec                                                    | 2.05 sec: 1.00x slower                                          |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.68 ms: 1.01x slower                                           |
| sympy_str               | 188 ms                                                      | 190 ms: 1.01x slower                                            |
| regex_v8                | 15.0 ms                                                     | 15.2 ms: 1.01x slower                                           |
| genshi_xml              | 40.5 ms                                                     | 41.0 ms: 1.01x slower                                           |
| xml_etree_generate      | 54.5 ms                                                     | 55.8 ms: 1.02x slower                                           |
| deepcopy_reduce         | 2.16 us                                                     | 2.22 us: 1.03x slower                                           |
| nbody                   | 69.3 ms                                                     | 71.9 ms: 1.04x slower                                           |
| deepcopy                | 255 us                                                      | 265 us: 1.04x slower                                            |
| pickle_dict             | 16.9 us                                                     | 17.7 us: 1.05x slower                                           |
| python_startup_no_site  | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                           |
| pidigits                | 145 ms                                                      | 154 ms: 1.06x slower                                            |
| nqueens                 | 67.0 ms                                                     | 71.0 ms: 1.06x slower                                           |
| meteor_contest          | 72.5 ms                                                     | 77.1 ms: 1.06x slower                                           |
| asyncio_tcp             | 712 ms                                                      | 762 ms: 1.07x slower                                            |
| json                    | 3.05 ms                                                     | 3.26 ms: 1.07x slower                                           |
| fannkuch                | 258 ms                                                      | 278 ms: 1.08x slower                                            |
| pickle_list             | 2.59 us                                                     | 2.81 us: 1.09x slower                                           |
| telco                   | 3.78 ms                                                     | 4.13 ms: 1.09x slower                                           |
| bench_mp_pool           | 60.7 ms                                                     | 67.0 ms: 1.10x slower                                           |
| gc_traversal            | 1.34 ms                                                     | 1.49 ms: 1.11x slower                                           |
| generators              | 31.6 ms                                                     | 35.4 ms: 1.12x slower                                           |
| comprehensions          | 16.0 us                                                     | 18.7 us: 1.17x slower                                           |
| coverage                | 40.0 ms                                                     | 108 ms: 2.69x slower                                            |
| Geometric mean          | (ref)                                                       | 1.06x faster                                                    |

Benchmark hidden because not significant (3): xml_etree_iterparse, json_loads, pickle
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x
