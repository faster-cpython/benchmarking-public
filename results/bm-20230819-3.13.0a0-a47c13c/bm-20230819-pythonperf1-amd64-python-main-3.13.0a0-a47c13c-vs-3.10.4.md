
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: a47c13c
- commit date: 2023-08-19
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.62 sec: 1.17x faster                                     |
| tornado_http   | 109 ms                                                      | 88.2 ms: 1.24x faster                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 54.6 ms: 1.10x faster                                      |
| pidigits       | 145 ms                                                      | 150 ms: 1.04x slower                                       |
| nbody          | 69.3 ms                                                     | 79.6 ms: 1.15x slower                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 91.9 ms: 1.12x faster                                      |
| regex_dna      | 132 ms                                                      | 120 ms: 1.09x faster                                       |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.60 ms: 1.52x faster                                      |
| pickle_pure_python   | 257 us                                                      | 196 us: 1.31x faster                                       |
| unpickle_pure_python | 171 us                                                      | 140 us: 1.22x faster                                       |
| xml_etree_process    | 43.4 ms                                                     | 38.3 ms: 1.13x faster                                      |
| xml_etree_parse      | 102 ms                                                      | 92.3 ms: 1.10x faster                                      |
| tomli_loads          | 1.62 sec                                                    | 1.49 sec: 1.09x faster                                     |
| unpickle             | 9.17 us                                                     | 8.60 us: 1.07x faster                                      |
| json_loads           | 14.2 us                                                     | 13.4 us: 1.06x faster                                      |
| xml_etree_generate   | 54.5 ms                                                     | 55.5 ms: 1.02x slower                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 64.8 ms: 1.02x slower                                      |
| unpickle_list        | 2.81 us                                                     | 2.99 us: 1.06x slower                                      |
| pickle               | 6.80 us                                                     | 7.37 us: 1.08x slower                                      |
| pickle_list          | 2.59 us                                                     | 2.85 us: 1.10x slower                                      |
| pickle_dict          | 16.9 us                                                     | 21.2 us: 1.25x slower                                      |
| Geometric mean       | (ref)                                                       | 1.06x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.6 ms: 1.02x faster                                      |
| python_startup_no_site | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                      |
| Geometric mean         | (ref)                                                       | 1.02x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.41 ms: 1.19x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 97.8 us: 3.32x faster                                      |
| deltablue                | 4.17 ms                                                     | 2.22 ms: 1.88x faster                                      |
| richards_super           | 51.7 ms                                                     | 32.7 ms: 1.58x faster                                      |
| async_tree_none          | 420 ms                                                      | 266 ms: 1.58x faster                                       |
| raytrace                 | 271 ms                                                      | 176 ms: 1.54x faster                                       |
| json_dumps               | 8.50 ms                                                     | 5.60 ms: 1.52x faster                                      |
| logging_silent           | 96.4 ns                                                     | 63.7 ns: 1.51x faster                                      |
| asyncio_tcp              | 712 ms                                                      | 475 ms: 1.50x faster                                       |
| go                       | 136 ms                                                      | 91.7 ms: 1.49x faster                                      |
| sqlglot_parse            | 1.22 ms                                                     | 829 us: 1.47x faster                                       |
| async_tree_io            | 1.07 sec                                                    | 733 ms: 1.45x faster                                       |
| async_tree_memoization   | 497 ms                                                      | 344 ms: 1.45x faster                                       |
| richards                 | 41.2 ms                                                     | 29.1 ms: 1.42x faster                                      |
| chaos                    | 58.9 ms                                                     | 41.7 ms: 1.41x faster                                      |
| crypto_pyaes             | 62.3 ms                                                     | 44.5 ms: 1.40x faster                                      |
| sqlglot_transpile        | 1.46 ms                                                     | 1.05 ms: 1.39x faster                                      |
| scimark_lu               | 85.4 ms                                                     | 61.6 ms: 1.39x faster                                      |
| pickle_pure_python       | 257 us                                                      | 196 us: 1.31x faster                                       |
| generators               | 31.6 ms                                                     | 24.2 ms: 1.30x faster                                      |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 471 ms: 1.29x faster                                       |
| hexiom                   | 5.52 ms                                                     | 4.27 ms: 1.29x faster                                      |
| pyflate                  | 387 ms                                                      | 305 ms: 1.27x faster                                       |
| scimark_sor              | 105 ms                                                      | 84.0 ms: 1.25x faster                                      |
| scimark_monte_carlo      | 55.9 ms                                                     | 45.0 ms: 1.24x faster                                      |
| tornado_http             | 109 ms                                                      | 88.2 ms: 1.24x faster                                      |
| unpickle_pure_python     | 171 us                                                      | 140 us: 1.22x faster                                       |
| pycparser                | 868 ms                                                      | 714 ms: 1.21x faster                                       |
| spectral_norm            | 78.0 ms                                                     | 64.7 ms: 1.21x faster                                      |
| mypy2                    | 352 ms                                                      | 295 ms: 1.19x faster                                       |
| mdp                      | 1.71 sec                                                    | 1.44 sec: 1.19x faster                                     |
| mako                     | 8.80 ms                                                     | 7.41 ms: 1.19x faster                                      |
| docutils                 | 1.89 sec                                                    | 1.62 sec: 1.17x faster                                     |
| deepcopy_memo            | 28.5 us                                                     | 24.8 us: 1.15x faster                                      |
| bench_thread_pool        | 946 us                                                      | 828 us: 1.14x faster                                       |
| xml_etree_process        | 43.4 ms                                                     | 38.3 ms: 1.13x faster                                      |
| regex_compile            | 103 ms                                                      | 91.9 ms: 1.12x faster                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.08 sec: 1.12x faster                                     |
| pprint_safe_repr         | 589 ms                                                      | 529 ms: 1.11x faster                                       |
| sqlglot_optimize         | 39.0 ms                                                     | 35.2 ms: 1.11x faster                                      |
| float                    | 60.2 ms                                                     | 54.6 ms: 1.10x faster                                      |
| xml_etree_parse          | 102 ms                                                      | 92.3 ms: 1.10x faster                                      |
| comprehensions           | 16.0 us                                                     | 14.6 us: 1.10x faster                                      |
| regex_dna                | 132 ms                                                      | 120 ms: 1.09x faster                                       |
| tomli_loads              | 1.62 sec                                                    | 1.49 sec: 1.09x faster                                     |
| nqueens                  | 67.0 ms                                                     | 62.2 ms: 1.08x faster                                      |
| create_gc_cycles         | 782 us                                                      | 727 us: 1.08x faster                                       |
| sqlglot_normalize        | 202 ms                                                      | 188 ms: 1.07x faster                                       |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.49 ms: 1.07x faster                                      |
| unpickle                 | 9.17 us                                                     | 8.60 us: 1.07x faster                                      |
| deepcopy                 | 255 us                                                      | 240 us: 1.06x faster                                       |
| json_loads               | 14.2 us                                                     | 13.4 us: 1.06x faster                                      |
| json                     | 3.05 ms                                                     | 2.89 ms: 1.06x faster                                      |
| dulwich_log              | 47.6 ms                                                     | 45.1 ms: 1.06x faster                                      |
| sqlite_synth             | 1.84 us                                                     | 1.75 us: 1.05x faster                                      |
| coroutines               | 15.9 ms                                                     | 15.2 ms: 1.05x faster                                      |
| unpack_sequence          | 37.8 ns                                                     | 36.5 ns: 1.04x faster                                      |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 1.97 sec: 1.03x faster                                     |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                      |
| python_startup           | 20.0 ms                                                     | 19.6 ms: 1.02x faster                                      |
| fannkuch                 | 258 ms                                                      | 253 ms: 1.02x faster                                       |
| scimark_fft              | 193 ms                                                      | 192 ms: 1.01x faster                                       |
| pathlib                  | 77.4 ms                                                     | 78.5 ms: 1.01x slower                                      |
| deepcopy_reduce          | 2.16 us                                                     | 2.19 us: 1.01x slower                                      |
| xml_etree_generate       | 54.5 ms                                                     | 55.5 ms: 1.02x slower                                      |
| meteor_contest           | 72.5 ms                                                     | 73.9 ms: 1.02x slower                                      |
| xml_etree_iterparse      | 63.5 ms                                                     | 64.8 ms: 1.02x slower                                      |
| logging_format           | 6.66 us                                                     | 6.82 us: 1.02x slower                                      |
| pidigits                 | 145 ms                                                      | 150 ms: 1.04x slower                                       |
| logging_simple           | 6.20 us                                                     | 6.43 us: 1.04x slower                                      |
| python_startup_no_site   | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                      |
| unpickle_list            | 2.81 us                                                     | 2.99 us: 1.06x slower                                      |
| pickle                   | 6.80 us                                                     | 7.37 us: 1.08x slower                                      |
| bench_mp_pool            | 60.7 ms                                                     | 65.8 ms: 1.08x slower                                      |
| async_generators         | 224 ms                                                      | 244 ms: 1.09x slower                                       |
| gc_traversal             | 1.34 ms                                                     | 1.47 ms: 1.09x slower                                      |
| pickle_list              | 2.59 us                                                     | 2.85 us: 1.10x slower                                      |
| nbody                    | 69.3 ms                                                     | 79.6 ms: 1.15x slower                                      |
| coverage                 | 40.0 ms                                                     | 47.2 ms: 1.18x slower                                      |
| dask                     | 305 ms                                                      | 372 ms: 1.22x slower                                       |
| pickle_dict              | 16.9 us                                                     | 21.2 us: 1.25x slower                                      |
| telco                    | 3.78 ms                                                     | 4.77 ms: 1.26x slower                                      |
| Geometric mean           | (ref)                                                       | 1.15x faster                                               |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x
