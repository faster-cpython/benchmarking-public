
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: 730c873
- commit date: 2023-07-01
- overall geometric mean: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf1-amd64-python-3.12-3.12.0b3+-730c873 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 215 ms: 1.10x faster                                        |
| docutils       | 1.89 sec                                                    | 1.68 sec: 1.12x faster                                      |
| tornado_http   | 109 ms                                                      | 90.0 ms: 1.21x faster                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf1-amd64-python-3.12-3.12.0b3+-730c873 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 54.2 ms: 1.11x faster                                       |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf1-amd64-python-3.12-3.12.0b3+-730c873 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 86.1 ms: 1.20x faster                                       |
| regex_v8       | 15.0 ms                                                     | 13.4 ms: 1.12x faster                                       |
| regex_dna      | 132 ms                                                      | 118 ms: 1.12x faster                                        |
| regex_effbot   | 1.66 ms                                                     | 1.82 ms: 1.09x slower                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf1-amd64-python-3.12-3.12.0b3+-730c873 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 6.03 ms: 1.41x faster                                       |
| pickle_pure_python   | 257 us                                                      | 190 us: 1.35x faster                                        |
| unpickle_pure_python | 171 us                                                      | 134 us: 1.28x faster                                        |
| tomli_loads          | 1.62 sec                                                    | 1.40 sec: 1.16x faster                                      |
| xml_etree_process    | 43.4 ms                                                     | 38.0 ms: 1.14x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 93.5 ms: 1.09x faster                                       |
| unpickle             | 9.17 us                                                     | 8.68 us: 1.06x faster                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 64.7 ms: 1.02x slower                                       |
| unpickle_list        | 2.81 us                                                     | 2.87 us: 1.02x slower                                       |
| xml_etree_generate   | 54.5 ms                                                     | 55.7 ms: 1.02x slower                                       |
| json_loads           | 14.2 us                                                     | 14.6 us: 1.03x slower                                       |
| pickle               | 6.80 us                                                     | 7.32 us: 1.08x slower                                       |
| pickle_dict          | 16.9 us                                                     | 18.7 us: 1.11x slower                                       |
| pickle_list          | 2.59 us                                                     | 2.93 us: 1.13x slower                                       |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf1-amd64-python-3.12-3.12.0b3+-730c873 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 20.3 ms: 1.02x slower                                       |
| python_startup_no_site | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                       |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf1-amd64-python-3.12-3.12.0b3+-730c873 |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.93 ms: 1.27x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf1-amd64-python-3.12-3.12.0b3+-730c873 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 97.2 us: 3.34x faster                                       |
| deltablue                | 4.17 ms                                                     | 2.11 ms: 1.98x faster                                       |
| richards_super           | 51.7 ms                                                     | 30.0 ms: 1.72x faster                                       |
| mypy2                    | 352 ms                                                      | 213 ms: 1.65x faster                                        |
| logging_silent           | 96.4 ns                                                     | 58.8 ns: 1.64x faster                                       |
| richards                 | 41.2 ms                                                     | 26.1 ms: 1.58x faster                                       |
| go                       | 136 ms                                                      | 86.9 ms: 1.57x faster                                       |
| sqlglot_parse            | 1.22 ms                                                     | 796 us: 1.53x faster                                        |
| scimark_lu               | 85.4 ms                                                     | 57.3 ms: 1.49x faster                                       |
| async_tree_io            | 1.07 sec                                                    | 727 ms: 1.46x faster                                        |
| generators               | 31.6 ms                                                     | 21.6 ms: 1.46x faster                                       |
| async_tree_memoization   | 497 ms                                                      | 342 ms: 1.45x faster                                        |
| raytrace                 | 271 ms                                                      | 187 ms: 1.45x faster                                        |
| sqlglot_transpile        | 1.46 ms                                                     | 1.01 ms: 1.44x faster                                       |
| asyncio_tcp              | 712 ms                                                      | 500 ms: 1.42x faster                                        |
| json_dumps               | 8.50 ms                                                     | 6.03 ms: 1.41x faster                                       |
| async_tree_none          | 420 ms                                                      | 298 ms: 1.41x faster                                        |
| chaos                    | 58.9 ms                                                     | 41.9 ms: 1.41x faster                                       |
| hexiom                   | 5.52 ms                                                     | 4.01 ms: 1.37x faster                                       |
| pickle_pure_python       | 257 us                                                      | 190 us: 1.35x faster                                        |
| scimark_monte_carlo      | 55.9 ms                                                     | 41.6 ms: 1.34x faster                                       |
| crypto_pyaes             | 62.3 ms                                                     | 48.1 ms: 1.30x faster                                       |
| scimark_sor              | 105 ms                                                      | 81.2 ms: 1.29x faster                                       |
| pyflate                  | 387 ms                                                      | 300 ms: 1.29x faster                                        |
| unpickle_pure_python     | 171 us                                                      | 134 us: 1.28x faster                                        |
| pycparser                | 868 ms                                                      | 684 ms: 1.27x faster                                        |
| mako                     | 8.80 ms                                                     | 6.93 ms: 1.27x faster                                       |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 493 ms: 1.24x faster                                        |
| tornado_http             | 109 ms                                                      | 90.0 ms: 1.21x faster                                       |
| deepcopy_memo            | 28.5 us                                                     | 23.6 us: 1.21x faster                                       |
| regex_compile            | 103 ms                                                      | 86.1 ms: 1.20x faster                                       |
| pprint_pformat           | 1.21 sec                                                    | 1.03 sec: 1.17x faster                                      |
| sqlglot_optimize         | 39.0 ms                                                     | 33.5 ms: 1.16x faster                                       |
| mdp                      | 1.71 sec                                                    | 1.48 sec: 1.16x faster                                      |
| pprint_safe_repr         | 589 ms                                                      | 508 ms: 1.16x faster                                        |
| tomli_loads              | 1.62 sec                                                    | 1.40 sec: 1.16x faster                                      |
| comprehensions           | 16.0 us                                                     | 13.9 us: 1.15x faster                                       |
| sqlglot_normalize        | 202 ms                                                      | 176 ms: 1.15x faster                                        |
| xml_etree_process        | 43.4 ms                                                     | 38.0 ms: 1.14x faster                                       |
| aiohttp                  | 1.01 ms                                                     | 889 us: 1.13x faster                                        |
| regex_v8                 | 15.0 ms                                                     | 13.4 ms: 1.12x faster                                       |
| docutils                 | 1.89 sec                                                    | 1.68 sec: 1.12x faster                                      |
| coroutines               | 15.9 ms                                                     | 14.2 ms: 1.12x faster                                       |
| nqueens                  | 67.0 ms                                                     | 59.7 ms: 1.12x faster                                       |
| regex_dna                | 132 ms                                                      | 118 ms: 1.12x faster                                        |
| float                    | 60.2 ms                                                     | 54.2 ms: 1.11x faster                                       |
| 2to3                     | 237 ms                                                      | 215 ms: 1.10x faster                                        |
| deepcopy                 | 255 us                                                      | 231 us: 1.10x faster                                        |
| spectral_norm            | 78.0 ms                                                     | 71.5 ms: 1.09x faster                                       |
| bench_thread_pool        | 946 us                                                      | 869 us: 1.09x faster                                        |
| xml_etree_parse          | 102 ms                                                      | 93.5 ms: 1.09x faster                                       |
| fannkuch                 | 258 ms                                                      | 239 ms: 1.08x faster                                        |
| dulwich_log              | 47.6 ms                                                     | 44.1 ms: 1.08x faster                                       |
| scimark_fft              | 193 ms                                                      | 182 ms: 1.06x faster                                        |
| unpickle                 | 9.17 us                                                     | 8.68 us: 1.06x faster                                       |
| sqlite_synth             | 1.84 us                                                     | 1.76 us: 1.05x faster                                       |
| create_gc_cycles         | 782 us                                                      | 752 us: 1.04x faster                                        |
| deepcopy_reduce          | 2.16 us                                                     | 2.08 us: 1.04x faster                                       |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.65 ms: 1.01x faster                                       |
| meteor_contest           | 72.5 ms                                                     | 73.3 ms: 1.01x slower                                       |
| python_startup           | 20.0 ms                                                     | 20.3 ms: 1.02x slower                                       |
| xml_etree_iterparse      | 63.5 ms                                                     | 64.7 ms: 1.02x slower                                       |
| logging_format           | 6.66 us                                                     | 6.79 us: 1.02x slower                                       |
| unpickle_list            | 2.81 us                                                     | 2.87 us: 1.02x slower                                       |
| xml_etree_generate       | 54.5 ms                                                     | 55.7 ms: 1.02x slower                                       |
| json                     | 3.05 ms                                                     | 3.12 ms: 1.03x slower                                       |
| logging_simple           | 6.20 us                                                     | 6.35 us: 1.03x slower                                       |
| json_loads               | 14.2 us                                                     | 14.6 us: 1.03x slower                                       |
| pidigits                 | 145 ms                                                      | 150 ms: 1.03x slower                                        |
| unpack_sequence          | 37.8 ns                                                     | 39.5 ns: 1.04x slower                                       |
| async_generators         | 224 ms                                                      | 237 ms: 1.06x slower                                        |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 2.16 sec: 1.06x slower                                      |
| pathlib                  | 77.4 ms                                                     | 83.0 ms: 1.07x slower                                       |
| pickle                   | 6.80 us                                                     | 7.32 us: 1.08x slower                                       |
| telco                    | 3.78 ms                                                     | 4.13 ms: 1.09x slower                                       |
| regex_effbot             | 1.66 ms                                                     | 1.82 ms: 1.09x slower                                       |
| pickle_dict              | 16.9 us                                                     | 18.7 us: 1.11x slower                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                       |
| bench_mp_pool            | 60.7 ms                                                     | 68.8 ms: 1.13x slower                                       |
| pickle_list              | 2.59 us                                                     | 2.93 us: 1.13x slower                                       |
| gc_traversal             | 1.34 ms                                                     | 1.54 ms: 1.15x slower                                       |
| dask                     | 305 ms                                                      | 365 ms: 1.20x slower                                        |
| coverage                 | 40.0 ms                                                     | 54.2 ms: 1.35x slower                                       |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                |

Benchmark hidden because not significant (1): nbody
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
