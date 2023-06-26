
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: 9cd3664
- commit date: 2023-06-24
- overall geometric mean: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 217 ms: 1.09x faster                                        |
| docutils       | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                      |
| tornado_http   | 109 ms                                                      | 89.0 ms: 1.23x faster                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 54.4 ms: 1.11x faster                                       |
| nbody          | 69.3 ms                                                     | 70.2 ms: 1.01x slower                                       |
| pidigits       | 145 ms                                                      | 153 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                       | 1.01x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 88.3 ms: 1.17x faster                                       |
| regex_v8       | 15.0 ms                                                     | 14.1 ms: 1.07x faster                                       |
| regex_dna      | 132 ms                                                      | 125 ms: 1.05x faster                                        |
| regex_effbot   | 1.66 ms                                                     | 2.01 ms: 1.20x slower                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3+-9cd3664 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.86 ms: 1.45x faster                                       |
| pickle_pure_python   | 257 us                                                      | 197 us: 1.30x faster                                        |
| unpickle_pure_python | 171 us                                                      | 135 us: 1.27x faster                                        |
| tomli_loads          | 1.62 sec                                                    | 1.42 sec: 1.14x faster                                      |
| xml_etree_process    | 43.4 ms                                                     | 38.5 ms: 1.13x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 92.5 ms: 1.10x faster                                       |
| unpickle             | 9.17 us                                                     | 8.82 us: 1.04x faster                                       |
| json_loads           | 14.2 us                                                     | 14.4 us: 1.02x slower                                       |
| xml_etree_generate   | 54.5 ms                                                     | 55.6 ms: 1.02x slower                                       |
| pickle               | 6.80 us                                                     | 7.16 us: 1.05x slower                                       |
| pickle_dict          | 16.9 us                                                     | 18.4 us: 1.09x slower                                       |
| pickle_list          | 2.59 us                                                     | 2.97 us: 1.15x slower                                       |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3+-9cd3664 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 20.3 ms: 1.01x slower                                       |
| python_startup_no_site | 15.5 ms                                                     | 17.3 ms: 1.11x slower                                       |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3+-9cd3664 |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.10 ms: 1.24x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3+-9cd3664 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 95.9 us: 3.39x faster                                       |
| deltablue                | 4.17 ms                                                     | 2.06 ms: 2.02x faster                                       |
| richards_super           | 51.7 ms                                                     | 29.7 ms: 1.74x faster                                       |
| mypy2                    | 352 ms                                                      | 217 ms: 1.62x faster                                        |
| logging_silent           | 96.4 ns                                                     | 59.5 ns: 1.62x faster                                       |
| richards                 | 41.2 ms                                                     | 26.2 ms: 1.57x faster                                       |
| go                       | 136 ms                                                      | 88.0 ms: 1.55x faster                                       |
| sqlglot_parse            | 1.22 ms                                                     | 791 us: 1.54x faster                                        |
| scimark_lu               | 85.4 ms                                                     | 57.9 ms: 1.47x faster                                       |
| async_tree_io            | 1.07 sec                                                    | 727 ms: 1.47x faster                                        |
| raytrace                 | 271 ms                                                      | 185 ms: 1.46x faster                                        |
| json_dumps               | 8.50 ms                                                     | 5.86 ms: 1.45x faster                                       |
| async_tree_none          | 420 ms                                                      | 291 ms: 1.45x faster                                        |
| async_tree_memoization   | 497 ms                                                      | 345 ms: 1.44x faster                                        |
| asyncio_tcp              | 712 ms                                                      | 497 ms: 1.43x faster                                        |
| sqlglot_transpile        | 1.46 ms                                                     | 1.02 ms: 1.43x faster                                       |
| chaos                    | 58.9 ms                                                     | 41.9 ms: 1.41x faster                                       |
| generators               | 31.6 ms                                                     | 22.7 ms: 1.39x faster                                       |
| crypto_pyaes             | 62.3 ms                                                     | 46.9 ms: 1.33x faster                                       |
| hexiom                   | 5.52 ms                                                     | 4.17 ms: 1.32x faster                                       |
| pickle_pure_python       | 257 us                                                      | 197 us: 1.30x faster                                        |
| scimark_monte_carlo      | 55.9 ms                                                     | 43.0 ms: 1.30x faster                                       |
| pyflate                  | 387 ms                                                      | 300 ms: 1.29x faster                                        |
| scimark_sor              | 105 ms                                                      | 82.1 ms: 1.28x faster                                       |
| unpickle_pure_python     | 171 us                                                      | 135 us: 1.27x faster                                        |
| mdp                      | 1.71 sec                                                    | 1.38 sec: 1.24x faster                                      |
| mako                     | 8.80 ms                                                     | 7.10 ms: 1.24x faster                                       |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 497 ms: 1.23x faster                                        |
| tornado_http             | 109 ms                                                      | 89.0 ms: 1.23x faster                                       |
| pycparser                | 868 ms                                                      | 710 ms: 1.22x faster                                        |
| regex_compile            | 103 ms                                                      | 88.3 ms: 1.17x faster                                       |
| pprint_pformat           | 1.21 sec                                                    | 1.04 sec: 1.16x faster                                      |
| deepcopy_memo            | 28.5 us                                                     | 24.7 us: 1.16x faster                                       |
| pprint_safe_repr         | 589 ms                                                      | 510 ms: 1.15x faster                                        |
| spectral_norm            | 78.0 ms                                                     | 68.0 ms: 1.15x faster                                       |
| tomli_loads              | 1.62 sec                                                    | 1.42 sec: 1.14x faster                                      |
| docutils                 | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                      |
| aiohttp                  | 1.01 ms                                                     | 893 us: 1.13x faster                                        |
| sqlglot_optimize         | 39.0 ms                                                     | 34.6 ms: 1.13x faster                                       |
| xml_etree_process        | 43.4 ms                                                     | 38.5 ms: 1.13x faster                                       |
| comprehensions           | 16.0 us                                                     | 14.3 us: 1.11x faster                                       |
| float                    | 60.2 ms                                                     | 54.4 ms: 1.11x faster                                       |
| coroutines               | 15.9 ms                                                     | 14.5 ms: 1.10x faster                                       |
| xml_etree_parse          | 102 ms                                                      | 92.5 ms: 1.10x faster                                       |
| sqlglot_normalize        | 202 ms                                                      | 184 ms: 1.10x faster                                        |
| 2to3                     | 237 ms                                                      | 217 ms: 1.09x faster                                        |
| deepcopy                 | 255 us                                                      | 233 us: 1.09x faster                                        |
| bench_thread_pool        | 946 us                                                      | 877 us: 1.08x faster                                        |
| nqueens                  | 67.0 ms                                                     | 62.2 ms: 1.08x faster                                       |
| regex_v8                 | 15.0 ms                                                     | 14.1 ms: 1.07x faster                                       |
| regex_dna                | 132 ms                                                      | 125 ms: 1.05x faster                                        |
| create_gc_cycles         | 782 us                                                      | 749 us: 1.04x faster                                        |
| fannkuch                 | 258 ms                                                      | 248 ms: 1.04x faster                                        |
| unpickle                 | 9.17 us                                                     | 8.82 us: 1.04x faster                                       |
| scimark_fft              | 193 ms                                                      | 186 ms: 1.04x faster                                        |
| dulwich_log              | 47.6 ms                                                     | 46.0 ms: 1.04x faster                                       |
| deepcopy_reduce          | 2.16 us                                                     | 2.09 us: 1.03x faster                                       |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.63 ms: 1.01x faster                                       |
| json                     | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                       |
| nbody                    | 69.3 ms                                                     | 70.2 ms: 1.01x slower                                       |
| python_startup           | 20.0 ms                                                     | 20.3 ms: 1.01x slower                                       |
| json_loads               | 14.2 us                                                     | 14.4 us: 1.02x slower                                       |
| xml_etree_generate       | 54.5 ms                                                     | 55.6 ms: 1.02x slower                                       |
| meteor_contest           | 72.5 ms                                                     | 74.1 ms: 1.02x slower                                       |
| async_generators         | 224 ms                                                      | 232 ms: 1.04x slower                                        |
| pickle                   | 6.80 us                                                     | 7.16 us: 1.05x slower                                       |
| pidigits                 | 145 ms                                                      | 153 ms: 1.06x slower                                        |
| logging_format           | 6.66 us                                                     | 7.07 us: 1.06x slower                                       |
| pathlib                  | 77.4 ms                                                     | 82.2 ms: 1.06x slower                                       |
| logging_simple           | 6.20 us                                                     | 6.59 us: 1.06x slower                                       |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 2.17 sec: 1.07x slower                                      |
| pickle_dict              | 16.9 us                                                     | 18.4 us: 1.09x slower                                       |
| telco                    | 3.78 ms                                                     | 4.20 ms: 1.11x slower                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.3 ms: 1.11x slower                                       |
| bench_mp_pool            | 60.7 ms                                                     | 68.9 ms: 1.14x slower                                       |
| gc_traversal             | 1.34 ms                                                     | 1.54 ms: 1.14x slower                                       |
| pickle_list              | 2.59 us                                                     | 2.97 us: 1.15x slower                                       |
| regex_effbot             | 1.66 ms                                                     | 2.01 ms: 1.20x slower                                       |
| dask                     | 305 ms                                                      | 369 ms: 1.21x slower                                        |
| coverage                 | 40.0 ms                                                     | 50.6 ms: 1.26x slower                                       |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                |

Benchmark hidden because not significant (4): xml_etree_iterparse, sqlite_synth, unpack_sequence, unpickle_list
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
