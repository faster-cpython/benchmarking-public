
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 18b1fde
- commit date: 2023-07-01
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf1-amd64-python-main-3.13.0a0-18b1fde |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.67 sec: 1.13x faster                                     |
| tornado_http   | 109 ms                                                      | 91.9 ms: 1.19x faster                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf1-amd64-python-main-3.13.0a0-18b1fde |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 56.8 ms: 1.06x faster                                      |
| pidigits       | 145 ms                                                      | 153 ms: 1.05x slower                                       |
| nbody          | 69.3 ms                                                     | 75.8 ms: 1.09x slower                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf1-amd64-python-main-3.13.0a0-18b1fde |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 92.4 ms: 1.12x faster                                      |
| regex_dna      | 132 ms                                                      | 129 ms: 1.02x faster                                       |
| regex_effbot   | 1.66 ms                                                     | 1.78 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf1-amd64-python-main-3.13.0a0-18b1fde |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 6.03 ms: 1.41x faster                                      |
| pickle_pure_python   | 257 us                                                      | 194 us: 1.32x faster                                       |
| unpickle_pure_python | 171 us                                                      | 141 us: 1.21x faster                                       |
| xml_etree_process    | 43.4 ms                                                     | 38.3 ms: 1.13x faster                                      |
| xml_etree_parse      | 102 ms                                                      | 94.2 ms: 1.08x faster                                      |
| unpickle             | 9.17 us                                                     | 8.83 us: 1.04x faster                                      |
| tomli_loads          | 1.62 sec                                                    | 1.56 sec: 1.04x faster                                     |
| json_loads           | 14.2 us                                                     | 14.4 us: 1.02x slower                                      |
| unpickle_list        | 2.81 us                                                     | 2.89 us: 1.03x slower                                      |
| pickle               | 6.80 us                                                     | 7.10 us: 1.04x slower                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 66.4 ms: 1.05x slower                                      |
| xml_etree_generate   | 54.5 ms                                                     | 57.3 ms: 1.05x slower                                      |
| pickle_list          | 2.59 us                                                     | 2.83 us: 1.09x slower                                      |
| pickle_dict          | 16.9 us                                                     | 18.6 us: 1.10x slower                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf1-amd64-python-main-3.13.0a0-18b1fde |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.3 ms: 1.11x slower                                      |
| Geometric mean         | (ref)                                                       | 1.06x slower                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf1-amd64-python-main-3.13.0a0-18b1fde |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.81 ms: 1.13x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-pythonperf1-amd64-python-main-3.13.0a0-18b1fde |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 94.4 us: 3.44x faster                                      |
| deltablue                | 4.17 ms                                                     | 2.24 ms: 1.86x faster                                      |
| richards_super           | 51.7 ms                                                     | 32.2 ms: 1.61x faster                                      |
| mypy2                    | 352 ms                                                      | 221 ms: 1.60x faster                                       |
| raytrace                 | 271 ms                                                      | 175 ms: 1.55x faster                                       |
| go                       | 136 ms                                                      | 92.4 ms: 1.47x faster                                      |
| logging_silent           | 96.4 ns                                                     | 65.5 ns: 1.47x faster                                      |
| richards                 | 41.2 ms                                                     | 28.5 ms: 1.44x faster                                      |
| sqlglot_parse            | 1.22 ms                                                     | 845 us: 1.44x faster                                       |
| asyncio_tcp              | 712 ms                                                      | 495 ms: 1.44x faster                                       |
| async_tree_io            | 1.07 sec                                                    | 744 ms: 1.43x faster                                       |
| async_tree_memoization   | 497 ms                                                      | 347 ms: 1.43x faster                                       |
| chaos                    | 58.9 ms                                                     | 41.2 ms: 1.43x faster                                      |
| scimark_lu               | 85.4 ms                                                     | 60.5 ms: 1.41x faster                                      |
| json_dumps               | 8.50 ms                                                     | 6.03 ms: 1.41x faster                                      |
| async_tree_none          | 420 ms                                                      | 299 ms: 1.41x faster                                       |
| sqlglot_transpile        | 1.46 ms                                                     | 1.08 ms: 1.36x faster                                      |
| generators               | 31.6 ms                                                     | 23.9 ms: 1.32x faster                                      |
| pickle_pure_python       | 257 us                                                      | 194 us: 1.32x faster                                       |
| crypto_pyaes             | 62.3 ms                                                     | 48.3 ms: 1.29x faster                                      |
| hexiom                   | 5.52 ms                                                     | 4.32 ms: 1.28x faster                                      |
| scimark_sor              | 105 ms                                                      | 82.2 ms: 1.28x faster                                      |
| scimark_monte_carlo      | 55.9 ms                                                     | 44.6 ms: 1.25x faster                                      |
| pyflate                  | 387 ms                                                      | 310 ms: 1.25x faster                                       |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 497 ms: 1.22x faster                                       |
| unpickle_pure_python     | 171 us                                                      | 141 us: 1.21x faster                                       |
| tornado_http             | 109 ms                                                      | 91.9 ms: 1.19x faster                                      |
| mdp                      | 1.71 sec                                                    | 1.45 sec: 1.18x faster                                     |
| deepcopy_memo            | 28.5 us                                                     | 25.0 us: 1.14x faster                                      |
| xml_etree_process        | 43.4 ms                                                     | 38.3 ms: 1.13x faster                                      |
| sqlglot_optimize         | 39.0 ms                                                     | 34.4 ms: 1.13x faster                                      |
| docutils                 | 1.89 sec                                                    | 1.67 sec: 1.13x faster                                     |
| mako                     | 8.80 ms                                                     | 7.81 ms: 1.13x faster                                      |
| spectral_norm            | 78.0 ms                                                     | 69.7 ms: 1.12x faster                                      |
| regex_compile            | 103 ms                                                      | 92.4 ms: 1.12x faster                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.09 sec: 1.10x faster                                     |
| pycparser                | 868 ms                                                      | 789 ms: 1.10x faster                                       |
| pprint_safe_repr         | 589 ms                                                      | 536 ms: 1.10x faster                                       |
| sqlglot_normalize        | 202 ms                                                      | 185 ms: 1.09x faster                                       |
| xml_etree_parse          | 102 ms                                                      | 94.2 ms: 1.08x faster                                      |
| nqueens                  | 67.0 ms                                                     | 62.7 ms: 1.07x faster                                      |
| deepcopy                 | 255 us                                                      | 240 us: 1.06x faster                                       |
| comprehensions           | 16.0 us                                                     | 15.1 us: 1.06x faster                                      |
| float                    | 60.2 ms                                                     | 56.8 ms: 1.06x faster                                      |
| coroutines               | 15.9 ms                                                     | 15.3 ms: 1.04x faster                                      |
| unpickle                 | 9.17 us                                                     | 8.83 us: 1.04x faster                                      |
| tomli_loads              | 1.62 sec                                                    | 1.56 sec: 1.04x faster                                     |
| create_gc_cycles         | 782 us                                                      | 759 us: 1.03x faster                                       |
| scimark_fft              | 193 ms                                                      | 188 ms: 1.03x faster                                       |
| sqlite_synth             | 1.84 us                                                     | 1.80 us: 1.02x faster                                      |
| dulwich_log              | 47.6 ms                                                     | 46.7 ms: 1.02x faster                                      |
| regex_dna                | 132 ms                                                      | 129 ms: 1.02x faster                                       |
| fannkuch                 | 258 ms                                                      | 254 ms: 1.01x faster                                       |
| deepcopy_reduce          | 2.16 us                                                     | 2.13 us: 1.01x faster                                      |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.63 ms: 1.01x faster                                      |
| json_loads               | 14.2 us                                                     | 14.4 us: 1.02x slower                                      |
| unpickle_list            | 2.81 us                                                     | 2.89 us: 1.03x slower                                      |
| pickle                   | 6.80 us                                                     | 7.10 us: 1.04x slower                                      |
| xml_etree_iterparse      | 63.5 ms                                                     | 66.4 ms: 1.05x slower                                      |
| meteor_contest           | 72.5 ms                                                     | 76.1 ms: 1.05x slower                                      |
| xml_etree_generate       | 54.5 ms                                                     | 57.3 ms: 1.05x slower                                      |
| pidigits                 | 145 ms                                                      | 153 ms: 1.05x slower                                       |
| logging_format           | 6.66 us                                                     | 7.08 us: 1.06x slower                                      |
| regex_effbot             | 1.66 ms                                                     | 1.78 ms: 1.07x slower                                      |
| pathlib                  | 77.4 ms                                                     | 82.8 ms: 1.07x slower                                      |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 2.18 sec: 1.07x slower                                     |
| async_generators         | 224 ms                                                      | 241 ms: 1.08x slower                                       |
| logging_simple           | 6.20 us                                                     | 6.73 us: 1.09x slower                                      |
| pickle_list              | 2.59 us                                                     | 2.83 us: 1.09x slower                                      |
| nbody                    | 69.3 ms                                                     | 75.8 ms: 1.09x slower                                      |
| pickle_dict              | 16.9 us                                                     | 18.6 us: 1.10x slower                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.3 ms: 1.11x slower                                      |
| bench_mp_pool            | 60.7 ms                                                     | 68.8 ms: 1.13x slower                                      |
| gc_traversal             | 1.34 ms                                                     | 1.53 ms: 1.14x slower                                      |
| telco                    | 3.78 ms                                                     | 4.40 ms: 1.16x slower                                      |
| coverage                 | 40.0 ms                                                     | 51.3 ms: 1.28x slower                                      |
| Geometric mean           | (ref)                                                       | 1.13x faster                                               |

Benchmark hidden because not significant (5): bench_thread_pool, json, unpack_sequence, python_startup, regex_v8
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x
