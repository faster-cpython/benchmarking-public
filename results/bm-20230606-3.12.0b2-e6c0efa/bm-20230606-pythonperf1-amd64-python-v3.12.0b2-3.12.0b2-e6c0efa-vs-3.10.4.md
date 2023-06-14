
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0b2
- machine: windows-amd64
- commit hash: e6c0efa
- commit date: 2023-06-06
- overall geometric mean: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf1-amd64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 216 ms: 1.10x faster                                            |
| docutils       | 1.89 sec                                                    | 1.67 sec: 1.14x faster                                          |
| tornado_http   | 109 ms                                                      | 88.5 ms: 1.23x faster                                           |
| Geometric mean | (ref)                                                       | 1.15x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf1-amd64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 55.2 ms: 1.09x faster                                           |
| nbody          | 69.3 ms                                                     | 68.3 ms: 1.02x faster                                           |
| pidigits       | 145 ms                                                      | 153 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                       | 1.02x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf1-amd64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 87.9 ms: 1.18x faster                                           |
| regex_v8       | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                           |
| regex_dna      | 132 ms                                                      | 125 ms: 1.06x faster                                            |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                       | 1.08x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf1-amd64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.59 ms: 1.52x faster                                           |
| pickle_pure_python   | 257 us                                                      | 197 us: 1.31x faster                                            |
| unpickle_pure_python | 171 us                                                      | 135 us: 1.27x faster                                            |
| tomli_loads          | 1.62 sec                                                    | 1.37 sec: 1.18x faster                                          |
| xml_etree_process    | 43.4 ms                                                     | 38.3 ms: 1.13x faster                                           |
| xml_etree_parse      | 102 ms                                                      | 91.6 ms: 1.11x faster                                           |
| unpickle             | 9.17 us                                                     | 8.48 us: 1.08x faster                                           |
| json_loads           | 14.2 us                                                     | 13.7 us: 1.03x faster                                           |
| xml_etree_iterparse  | 63.5 ms                                                     | 65.0 ms: 1.02x slower                                           |
| unpickle_list        | 2.81 us                                                     | 2.90 us: 1.03x slower                                           |
| pickle               | 6.80 us                                                     | 7.11 us: 1.04x slower                                           |
| xml_etree_generate   | 54.5 ms                                                     | 57.0 ms: 1.05x slower                                           |
| pickle_dict          | 16.9 us                                                     | 18.2 us: 1.07x slower                                           |
| pickle_list          | 2.59 us                                                     | 2.85 us: 1.10x slower                                           |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf1-amd64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                           |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf1-amd64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.05 ms: 1.25x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf1-amd64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 95.0 us: 3.42x faster                                           |
| deltablue                | 4.17 ms                                                     | 2.08 ms: 2.00x faster                                           |
| richards_super           | 51.7 ms                                                     | 29.2 ms: 1.77x faster                                           |
| mypy2                    | 352 ms                                                      | 217 ms: 1.63x faster                                            |
| logging_silent           | 96.4 ns                                                     | 59.4 ns: 1.62x faster                                           |
| richards                 | 41.2 ms                                                     | 25.7 ms: 1.60x faster                                           |
| go                       | 136 ms                                                      | 87.8 ms: 1.55x faster                                           |
| sqlglot_parse            | 1.22 ms                                                     | 799 us: 1.53x faster                                            |
| json_dumps               | 8.50 ms                                                     | 5.59 ms: 1.52x faster                                           |
| scimark_lu               | 85.4 ms                                                     | 56.8 ms: 1.50x faster                                           |
| asyncio_tcp              | 712 ms                                                      | 478 ms: 1.49x faster                                            |
| sqlglot_transpile        | 1.46 ms                                                     | 1.01 ms: 1.45x faster                                           |
| raytrace                 | 271 ms                                                      | 187 ms: 1.45x faster                                            |
| async_tree_memoization   | 497 ms                                                      | 347 ms: 1.43x faster                                            |
| async_tree_io            | 1.07 sec                                                    | 744 ms: 1.43x faster                                            |
| async_tree_none          | 420 ms                                                      | 298 ms: 1.41x faster                                            |
| generators               | 31.6 ms                                                     | 22.4 ms: 1.41x faster                                           |
| hexiom                   | 5.52 ms                                                     | 4.00 ms: 1.38x faster                                           |
| chaos                    | 58.9 ms                                                     | 42.8 ms: 1.37x faster                                           |
| scimark_sor              | 105 ms                                                      | 77.3 ms: 1.36x faster                                           |
| crypto_pyaes             | 62.3 ms                                                     | 47.2 ms: 1.32x faster                                           |
| scimark_monte_carlo      | 55.9 ms                                                     | 42.6 ms: 1.31x faster                                           |
| pyflate                  | 387 ms                                                      | 296 ms: 1.31x faster                                            |
| pickle_pure_python       | 257 us                                                      | 197 us: 1.31x faster                                            |
| pycparser                | 868 ms                                                      | 680 ms: 1.28x faster                                            |
| unpickle_pure_python     | 171 us                                                      | 135 us: 1.27x faster                                            |
| mako                     | 8.80 ms                                                     | 7.05 ms: 1.25x faster                                           |
| mdp                      | 1.71 sec                                                    | 1.38 sec: 1.24x faster                                          |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 493 ms: 1.24x faster                                            |
| tornado_http             | 109 ms                                                      | 88.5 ms: 1.23x faster                                           |
| deepcopy_memo            | 28.5 us                                                     | 23.8 us: 1.20x faster                                           |
| tomli_loads              | 1.62 sec                                                    | 1.37 sec: 1.18x faster                                          |
| spectral_norm            | 78.0 ms                                                     | 66.0 ms: 1.18x faster                                           |
| regex_compile            | 103 ms                                                      | 87.9 ms: 1.18x faster                                           |
| pprint_pformat           | 1.21 sec                                                    | 1.03 sec: 1.17x faster                                          |
| pprint_safe_repr         | 589 ms                                                      | 510 ms: 1.16x faster                                            |
| sqlglot_optimize         | 39.0 ms                                                     | 33.8 ms: 1.15x faster                                           |
| coroutines               | 15.9 ms                                                     | 13.9 ms: 1.15x faster                                           |
| aiohttp                  | 1.01 ms                                                     | 879 us: 1.15x faster                                            |
| docutils                 | 1.89 sec                                                    | 1.67 sec: 1.14x faster                                          |
| xml_etree_process        | 43.4 ms                                                     | 38.3 ms: 1.13x faster                                           |
| comprehensions           | 16.0 us                                                     | 14.4 us: 1.11x faster                                           |
| xml_etree_parse          | 102 ms                                                      | 91.6 ms: 1.11x faster                                           |
| scimark_fft              | 193 ms                                                      | 174 ms: 1.11x faster                                            |
| sqlglot_normalize        | 202 ms                                                      | 183 ms: 1.11x faster                                            |
| 2to3                     | 237 ms                                                      | 216 ms: 1.10x faster                                            |
| nqueens                  | 67.0 ms                                                     | 61.1 ms: 1.10x faster                                           |
| bench_thread_pool        | 946 us                                                      | 867 us: 1.09x faster                                            |
| float                    | 60.2 ms                                                     | 55.2 ms: 1.09x faster                                           |
| unpickle                 | 9.17 us                                                     | 8.48 us: 1.08x faster                                           |
| regex_v8                 | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                           |
| dulwich_log              | 47.6 ms                                                     | 44.2 ms: 1.08x faster                                           |
| fannkuch                 | 258 ms                                                      | 240 ms: 1.07x faster                                            |
| regex_dna                | 132 ms                                                      | 125 ms: 1.06x faster                                            |
| deepcopy                 | 255 us                                                      | 241 us: 1.06x faster                                            |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.52 ms: 1.05x faster                                           |
| create_gc_cycles         | 782 us                                                      | 744 us: 1.05x faster                                            |
| json_loads               | 14.2 us                                                     | 13.7 us: 1.03x faster                                           |
| sqlite_synth             | 1.84 us                                                     | 1.79 us: 1.03x faster                                           |
| deepcopy_reduce          | 2.16 us                                                     | 2.10 us: 1.03x faster                                           |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                           |
| json                     | 3.05 ms                                                     | 2.99 ms: 1.02x faster                                           |
| nbody                    | 69.3 ms                                                     | 68.3 ms: 1.02x faster                                           |
| meteor_contest           | 72.5 ms                                                     | 73.9 ms: 1.02x slower                                           |
| xml_etree_iterparse      | 63.5 ms                                                     | 65.0 ms: 1.02x slower                                           |
| unpickle_list            | 2.81 us                                                     | 2.90 us: 1.03x slower                                           |
| unpack_sequence          | 37.8 ns                                                     | 39.1 ns: 1.03x slower                                           |
| async_generators         | 224 ms                                                      | 233 ms: 1.04x slower                                            |
| pickle                   | 6.80 us                                                     | 7.11 us: 1.04x slower                                           |
| xml_etree_generate       | 54.5 ms                                                     | 57.0 ms: 1.05x slower                                           |
| logging_format           | 6.66 us                                                     | 7.01 us: 1.05x slower                                           |
| logging_simple           | 6.20 us                                                     | 6.54 us: 1.06x slower                                           |
| pidigits                 | 145 ms                                                      | 153 ms: 1.06x slower                                            |
| pickle_dict              | 16.9 us                                                     | 18.2 us: 1.07x slower                                           |
| pathlib                  | 77.4 ms                                                     | 83.2 ms: 1.08x slower                                           |
| telco                    | 3.78 ms                                                     | 4.15 ms: 1.10x slower                                           |
| pickle_list              | 2.59 us                                                     | 2.85 us: 1.10x slower                                           |
| bench_mp_pool            | 60.7 ms                                                     | 68.0 ms: 1.12x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                           |
| gc_traversal             | 1.34 ms                                                     | 1.53 ms: 1.14x slower                                           |
| dask                     | 305 ms                                                      | 373 ms: 1.22x slower                                            |
| coverage                 | 40.0 ms                                                     | 52.5 ms: 1.31x slower                                           |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                    |

Benchmark hidden because not significant (2): python_startup, asyncio_tcp_ssl
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
