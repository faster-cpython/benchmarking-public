
# Results vs. 3.10.4

- fork: python
- ref: 6baddd9fb25e03040c1c
- machine: windows-amd64
- commit hash: 6baddd9
- commit date: 2023-06-18
- overall geometric mean: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf1-amd64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 219 ms: 1.08x faster                                                        |
| docutils       | 1.89 sec                                                    | 1.65 sec: 1.15x faster                                                      |
| tornado_http   | 109 ms                                                      | 89.9 ms: 1.21x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf1-amd64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 54.6 ms: 1.10x faster                                                       |
| pidigits       | 145 ms                                                      | 152 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf1-amd64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 86.8 ms: 1.19x faster                                                       |
| regex_dna      | 132 ms                                                      | 124 ms: 1.06x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 14.2 ms: 1.06x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf1-amd64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.60 ms: 1.52x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 194 us: 1.32x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 133 us: 1.29x faster                                                        |
| tomli_loads          | 1.62 sec                                                    | 1.37 sec: 1.18x faster                                                      |
| xml_etree_process    | 43.4 ms                                                     | 38.0 ms: 1.14x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 94.3 ms: 1.08x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.55 us: 1.07x faster                                                       |
| json_loads           | 14.2 us                                                     | 13.7 us: 1.04x faster                                                       |
| pickle               | 6.80 us                                                     | 7.04 us: 1.03x slower                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 56.4 ms: 1.03x slower                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 65.9 ms: 1.04x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.3 us: 1.08x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.86 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf1-amd64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 20.4 ms: 1.02x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf1-amd64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.96 ms: 1.26x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf1-amd64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 95.4 us: 3.40x faster                                                       |
| deltablue                | 4.17 ms                                                     | 2.06 ms: 2.02x faster                                                       |
| richards_super           | 51.7 ms                                                     | 29.3 ms: 1.77x faster                                                       |
| logging_silent           | 96.4 ns                                                     | 59.0 ns: 1.63x faster                                                       |
| mypy2                    | 352 ms                                                      | 217 ms: 1.62x faster                                                        |
| richards                 | 41.2 ms                                                     | 26.0 ms: 1.58x faster                                                       |
| go                       | 136 ms                                                      | 88.7 ms: 1.54x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 799 us: 1.53x faster                                                        |
| json_dumps               | 8.50 ms                                                     | 5.60 ms: 1.52x faster                                                       |
| sqlglot_transpile        | 1.46 ms                                                     | 1.00 ms: 1.46x faster                                                       |
| scimark_lu               | 85.4 ms                                                     | 58.8 ms: 1.45x faster                                                       |
| raytrace                 | 271 ms                                                      | 187 ms: 1.45x faster                                                        |
| async_tree_none          | 420 ms                                                      | 292 ms: 1.44x faster                                                        |
| async_tree_memoization   | 497 ms                                                      | 346 ms: 1.44x faster                                                        |
| async_tree_io            | 1.07 sec                                                    | 745 ms: 1.43x faster                                                        |
| asyncio_tcp              | 712 ms                                                      | 504 ms: 1.41x faster                                                        |
| generators               | 31.6 ms                                                     | 22.5 ms: 1.40x faster                                                       |
| chaos                    | 58.9 ms                                                     | 42.1 ms: 1.40x faster                                                       |
| hexiom                   | 5.52 ms                                                     | 4.02 ms: 1.37x faster                                                       |
| crypto_pyaes             | 62.3 ms                                                     | 46.8 ms: 1.33x faster                                                       |
| pickle_pure_python       | 257 us                                                      | 194 us: 1.32x faster                                                        |
| pyflate                  | 387 ms                                                      | 296 ms: 1.31x faster                                                        |
| scimark_monte_carlo      | 55.9 ms                                                     | 42.7 ms: 1.31x faster                                                       |
| unpickle_pure_python     | 171 us                                                      | 133 us: 1.29x faster                                                        |
| scimark_sor              | 105 ms                                                      | 81.7 ms: 1.28x faster                                                       |
| mako                     | 8.80 ms                                                     | 6.96 ms: 1.26x faster                                                       |
| pycparser                | 868 ms                                                      | 689 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 495 ms: 1.23x faster                                                        |
| tornado_http             | 109 ms                                                      | 89.9 ms: 1.21x faster                                                       |
| deepcopy_memo            | 28.5 us                                                     | 23.6 us: 1.21x faster                                                       |
| spectral_norm            | 78.0 ms                                                     | 65.2 ms: 1.20x faster                                                       |
| regex_compile            | 103 ms                                                      | 86.8 ms: 1.19x faster                                                       |
| tomli_loads              | 1.62 sec                                                    | 1.37 sec: 1.18x faster                                                      |
| mdp                      | 1.71 sec                                                    | 1.45 sec: 1.18x faster                                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.03 sec: 1.18x faster                                                      |
| pprint_safe_repr         | 589 ms                                                      | 506 ms: 1.16x faster                                                        |
| sqlglot_optimize         | 39.0 ms                                                     | 33.8 ms: 1.15x faster                                                       |
| docutils                 | 1.89 sec                                                    | 1.65 sec: 1.15x faster                                                      |
| xml_etree_process        | 43.4 ms                                                     | 38.0 ms: 1.14x faster                                                       |
| coroutines               | 15.9 ms                                                     | 14.0 ms: 1.14x faster                                                       |
| comprehensions           | 16.0 us                                                     | 14.0 us: 1.14x faster                                                       |
| aiohttp                  | 1.01 ms                                                     | 888 us: 1.13x faster                                                        |
| sqlglot_normalize        | 202 ms                                                      | 183 ms: 1.11x faster                                                        |
| float                    | 60.2 ms                                                     | 54.6 ms: 1.10x faster                                                       |
| nqueens                  | 67.0 ms                                                     | 61.2 ms: 1.10x faster                                                       |
| dulwich_log              | 47.6 ms                                                     | 43.8 ms: 1.09x faster                                                       |
| deepcopy                 | 255 us                                                      | 235 us: 1.09x faster                                                        |
| 2to3                     | 237 ms                                                      | 219 ms: 1.08x faster                                                        |
| scimark_fft              | 193 ms                                                      | 179 ms: 1.08x faster                                                        |
| xml_etree_parse          | 102 ms                                                      | 94.3 ms: 1.08x faster                                                       |
| unpickle                 | 9.17 us                                                     | 8.55 us: 1.07x faster                                                       |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.48 ms: 1.07x faster                                                       |
| regex_dna                | 132 ms                                                      | 124 ms: 1.06x faster                                                        |
| regex_v8                 | 15.0 ms                                                     | 14.2 ms: 1.06x faster                                                       |
| fannkuch                 | 258 ms                                                      | 244 ms: 1.06x faster                                                        |
| bench_thread_pool        | 946 us                                                      | 899 us: 1.05x faster                                                        |
| create_gc_cycles         | 782 us                                                      | 749 us: 1.04x faster                                                        |
| json_loads               | 14.2 us                                                     | 13.7 us: 1.04x faster                                                       |
| deepcopy_reduce          | 2.16 us                                                     | 2.08 us: 1.04x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                       |
| json                     | 3.05 ms                                                     | 2.97 ms: 1.03x faster                                                       |
| python_startup           | 20.0 ms                                                     | 20.4 ms: 1.02x slower                                                       |
| meteor_contest           | 72.5 ms                                                     | 74.0 ms: 1.02x slower                                                       |
| pickle                   | 6.80 us                                                     | 7.04 us: 1.03x slower                                                       |
| xml_etree_generate       | 54.5 ms                                                     | 56.4 ms: 1.03x slower                                                       |
| logging_format           | 6.66 us                                                     | 6.90 us: 1.04x slower                                                       |
| xml_etree_iterparse      | 63.5 ms                                                     | 65.9 ms: 1.04x slower                                                       |
| async_generators         | 224 ms                                                      | 234 ms: 1.05x slower                                                        |
| pidigits                 | 145 ms                                                      | 152 ms: 1.05x slower                                                        |
| logging_simple           | 6.20 us                                                     | 6.53 us: 1.05x slower                                                       |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 2.18 sec: 1.07x slower                                                      |
| pathlib                  | 77.4 ms                                                     | 82.9 ms: 1.07x slower                                                       |
| pickle_dict              | 16.9 us                                                     | 18.3 us: 1.08x slower                                                       |
| telco                    | 3.78 ms                                                     | 4.10 ms: 1.09x slower                                                       |
| pickle_list              | 2.59 us                                                     | 2.86 us: 1.11x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                                       |
| gc_traversal             | 1.34 ms                                                     | 1.51 ms: 1.13x slower                                                       |
| bench_mp_pool            | 60.7 ms                                                     | 69.7 ms: 1.15x slower                                                       |
| dask                     | 305 ms                                                      | 371 ms: 1.22x slower                                                        |
| coverage                 | 40.0 ms                                                     | 52.1 ms: 1.30x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                                |

Benchmark hidden because not significant (4): nbody, unpack_sequence, sqlite_synth, unpickle_list
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
