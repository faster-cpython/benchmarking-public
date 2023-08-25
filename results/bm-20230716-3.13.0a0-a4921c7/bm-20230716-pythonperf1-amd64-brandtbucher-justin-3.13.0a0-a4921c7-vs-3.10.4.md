
# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin
- machine: windows-amd64
- commit hash: a4921c7
- commit date: 2023-07-16
- overall geometric mean: 1.14x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.64 sec: 1.15x faster                                             |
| tornado_http   | 109 ms                                                      | 89.6 ms: 1.22x faster                                              |
| Geometric mean | (ref)                                                       | 1.19x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 52.0 ms: 1.16x faster                                              |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                               |
| nbody          | 69.3 ms                                                     | 72.1 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                       | 1.02x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 88.7 ms: 1.17x faster                                              |
| regex_dna      | 132 ms                                                      | 116 ms: 1.14x faster                                               |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.07x faster                                              |
| regex_v8       | 15.0 ms                                                     | 24.0 ms: 1.60x slower                                              |
| Geometric mean | (ref)                                                       | 1.03x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.78 ms: 1.47x faster                                              |
| pickle_pure_python   | 257 us                                                      | 196 us: 1.31x faster                                               |
| unpickle_pure_python | 171 us                                                      | 136 us: 1.25x faster                                               |
| tomli_loads          | 1.62 sec                                                    | 1.41 sec: 1.15x faster                                             |
| unpickle             | 9.17 us                                                     | 8.26 us: 1.11x faster                                              |
| xml_etree_process    | 43.4 ms                                                     | 39.2 ms: 1.11x faster                                              |
| xml_etree_parse      | 102 ms                                                      | 92.8 ms: 1.10x faster                                              |
| json_loads           | 14.2 us                                                     | 13.5 us: 1.05x faster                                              |
| xml_etree_generate   | 54.5 ms                                                     | 56.8 ms: 1.04x slower                                              |
| pickle               | 6.80 us                                                     | 7.15 us: 1.05x slower                                              |
| pickle_dict          | 16.9 us                                                     | 19.1 us: 1.13x slower                                              |
| pickle_list          | 2.59 us                                                     | 2.92 us: 1.13x slower                                              |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                       |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 22.2 ms: 1.11x slower                                              |
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                              |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|-----------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.39 ms: 1.19x faster                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 97.3 us: 3.34x faster                                              |
| deltablue                | 4.17 ms                                                     | 2.31 ms: 1.81x faster                                              |
| richards_super           | 51.7 ms                                                     | 30.1 ms: 1.72x faster                                              |
| mypy2                    | 352 ms                                                      | 215 ms: 1.64x faster                                               |
| richards                 | 41.2 ms                                                     | 26.5 ms: 1.56x faster                                              |
| logging_silent           | 96.4 ns                                                     | 62.9 ns: 1.53x faster                                              |
| go                       | 136 ms                                                      | 91.4 ms: 1.49x faster                                              |
| asyncio_tcp              | 712 ms                                                      | 478 ms: 1.49x faster                                               |
| json_dumps               | 8.50 ms                                                     | 5.78 ms: 1.47x faster                                              |
| async_tree_io            | 1.07 sec                                                    | 735 ms: 1.45x faster                                               |
| sqlglot_parse            | 1.22 ms                                                     | 842 us: 1.45x faster                                               |
| async_tree_memoization   | 497 ms                                                      | 344 ms: 1.45x faster                                               |
| async_tree_none          | 420 ms                                                      | 294 ms: 1.43x faster                                               |
| sqlglot_transpile        | 1.46 ms                                                     | 1.06 ms: 1.38x faster                                              |
| raytrace                 | 271 ms                                                      | 197 ms: 1.37x faster                                               |
| chaos                    | 58.9 ms                                                     | 44.2 ms: 1.33x faster                                              |
| generators               | 31.6 ms                                                     | 23.9 ms: 1.32x faster                                              |
| scimark_sor              | 105 ms                                                      | 79.6 ms: 1.32x faster                                              |
| pickle_pure_python       | 257 us                                                      | 196 us: 1.31x faster                                               |
| scimark_monte_carlo      | 55.9 ms                                                     | 42.8 ms: 1.31x faster                                              |
| pyflate                  | 387 ms                                                      | 301 ms: 1.29x faster                                               |
| pycparser                | 868 ms                                                      | 685 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 481 ms: 1.27x faster                                               |
| unpickle_pure_python     | 171 us                                                      | 136 us: 1.25x faster                                               |
| mdp                      | 1.71 sec                                                    | 1.40 sec: 1.23x faster                                             |
| tornado_http             | 109 ms                                                      | 89.6 ms: 1.22x faster                                              |
| scimark_lu               | 85.4 ms                                                     | 70.3 ms: 1.21x faster                                              |
| hexiom                   | 5.52 ms                                                     | 4.62 ms: 1.20x faster                                              |
| mako                     | 8.80 ms                                                     | 7.39 ms: 1.19x faster                                              |
| spectral_norm            | 78.0 ms                                                     | 66.0 ms: 1.18x faster                                              |
| regex_compile            | 103 ms                                                      | 88.7 ms: 1.17x faster                                              |
| crypto_pyaes             | 62.3 ms                                                     | 53.6 ms: 1.16x faster                                              |
| float                    | 60.2 ms                                                     | 52.0 ms: 1.16x faster                                              |
| docutils                 | 1.89 sec                                                    | 1.64 sec: 1.15x faster                                             |
| tomli_loads              | 1.62 sec                                                    | 1.41 sec: 1.15x faster                                             |
| bench_thread_pool        | 946 us                                                      | 832 us: 1.14x faster                                               |
| regex_dna                | 132 ms                                                      | 116 ms: 1.14x faster                                               |
| pprint_pformat           | 1.21 sec                                                    | 1.06 sec: 1.13x faster                                             |
| pprint_safe_repr         | 589 ms                                                      | 520 ms: 1.13x faster                                               |
| sqlglot_optimize         | 39.0 ms                                                     | 34.8 ms: 1.12x faster                                              |
| unpickle                 | 9.17 us                                                     | 8.26 us: 1.11x faster                                              |
| dulwich_log              | 47.6 ms                                                     | 42.9 ms: 1.11x faster                                              |
| xml_etree_process        | 43.4 ms                                                     | 39.2 ms: 1.11x faster                                              |
| xml_etree_parse          | 102 ms                                                      | 92.8 ms: 1.10x faster                                              |
| create_gc_cycles         | 782 us                                                      | 722 us: 1.08x faster                                               |
| sqlglot_normalize        | 202 ms                                                      | 188 ms: 1.08x faster                                               |
| coroutines               | 15.9 ms                                                     | 14.8 ms: 1.08x faster                                              |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.48 ms: 1.07x faster                                              |
| scimark_fft              | 193 ms                                                      | 181 ms: 1.07x faster                                               |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.07x faster                                              |
| deepcopy                 | 255 us                                                      | 240 us: 1.06x faster                                               |
| json                     | 3.05 ms                                                     | 2.87 ms: 1.06x faster                                              |
| sqlite_synth             | 1.84 us                                                     | 1.74 us: 1.06x faster                                              |
| json_loads               | 14.2 us                                                     | 13.5 us: 1.05x faster                                              |
| deepcopy_memo            | 28.5 us                                                     | 27.2 us: 1.05x faster                                              |
| nqueens                  | 67.0 ms                                                     | 63.9 ms: 1.05x faster                                              |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 1.97 sec: 1.03x faster                                             |
| comprehensions           | 16.0 us                                                     | 15.5 us: 1.03x faster                                              |
| deepcopy_reduce          | 2.16 us                                                     | 2.11 us: 1.02x faster                                              |
| fannkuch                 | 258 ms                                                      | 255 ms: 1.01x faster                                               |
| pidigits                 | 145 ms                                                      | 151 ms: 1.04x slower                                               |
| pathlib                  | 77.4 ms                                                     | 80.3 ms: 1.04x slower                                              |
| nbody                    | 69.3 ms                                                     | 72.1 ms: 1.04x slower                                              |
| meteor_contest           | 72.5 ms                                                     | 75.4 ms: 1.04x slower                                              |
| xml_etree_generate       | 54.5 ms                                                     | 56.8 ms: 1.04x slower                                              |
| pickle                   | 6.80 us                                                     | 7.15 us: 1.05x slower                                              |
| logging_format           | 6.66 us                                                     | 7.01 us: 1.05x slower                                              |
| logging_simple           | 6.20 us                                                     | 6.58 us: 1.06x slower                                              |
| async_generators         | 224 ms                                                      | 239 ms: 1.07x slower                                               |
| telco                    | 3.78 ms                                                     | 4.11 ms: 1.09x slower                                              |
| gc_traversal             | 1.34 ms                                                     | 1.48 ms: 1.10x slower                                              |
| python_startup           | 20.0 ms                                                     | 22.2 ms: 1.11x slower                                              |
| pickle_dict              | 16.9 us                                                     | 19.1 us: 1.13x slower                                              |
| pickle_list              | 2.59 us                                                     | 2.92 us: 1.13x slower                                              |
| bench_mp_pool            | 60.7 ms                                                     | 70.0 ms: 1.15x slower                                              |
| dask                     | 305 ms                                                      | 363 ms: 1.19x slower                                               |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                              |
| coverage                 | 40.0 ms                                                     | 53.3 ms: 1.33x slower                                              |
| regex_v8                 | 15.0 ms                                                     | 24.0 ms: 1.60x slower                                              |
| Geometric mean           | (ref)                                                       | 1.14x faster                                                       |

Benchmark hidden because not significant (3): unpack_sequence, xml_etree_iterparse, unpickle_list
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x
