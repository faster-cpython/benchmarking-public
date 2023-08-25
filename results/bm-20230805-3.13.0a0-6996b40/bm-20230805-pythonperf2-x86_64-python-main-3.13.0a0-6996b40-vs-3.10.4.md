
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 6996b40
- commit date: 2023-08-05
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf2-x86_64-python-main-3.13.0a0-6996b40 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.92 sec: 1.17x faster                                      |
| tornado_http   | 152 ms                                                       | 121 ms: 1.25x faster                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf2-x86_64-python-main-3.13.0a0-6996b40 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 137 ms                                                       | 93.6 ms: 1.47x faster                                       |
| float          | 110 ms                                                       | 81.3 ms: 1.36x faster                                       |
| pidigits       | 271 ms                                                       | 259 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                        | 1.28x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf2-x86_64-python-main-3.13.0a0-6996b40 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 150 ms: 1.29x faster                                        |
| regex_v8       | 26.6 ms                                                      | 23.9 ms: 1.11x faster                                       |
| regex_dna      | 259 ms                                                       | 236 ms: 1.10x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.41 ms: 1.14x slower                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf2-x86_64-python-main-3.13.0a0-6996b40 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 221 us: 1.45x faster                                        |
| pickle_pure_python   | 457 us                                                       | 323 us: 1.42x faster                                        |
| json_dumps           | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                       |
| tomli_loads          | 2.97 sec                                                     | 2.32 sec: 1.28x faster                                      |
| xml_etree_process    | 76.0 ms                                                      | 59.4 ms: 1.28x faster                                       |
| json_loads           | 30.0 us                                                      | 25.4 us: 1.18x faster                                       |
| xml_etree_parse      | 162 ms                                                       | 148 ms: 1.09x faster                                        |
| xml_etree_generate   | 94.6 ms                                                      | 86.7 ms: 1.09x faster                                       |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                        |
| unpickle             | 14.2 us                                                      | 14.6 us: 1.03x slower                                       |
| unpickle_list        | 4.49 us                                                      | 4.64 us: 1.03x slower                                       |
| pickle               | 9.94 us                                                      | 10.4 us: 1.04x slower                                       |
| pickle_dict          | 30.0 us                                                      | 31.7 us: 1.06x slower                                       |
| pickle_list          | 4.11 us                                                      | 4.38 us: 1.07x slower                                       |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf2-x86_64-python-main-3.13.0a0-6996b40 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.64 ms: 1.18x slower                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf2-x86_64-python-main-3.13.0a0-6996b40 |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-pythonperf2-x86_64-python-main-3.13.0a0-6996b40 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 153 us: 3.41x faster                                        |
| asyncio_tcp              | 782 ms                                                       | 371 ms: 2.11x faster                                        |
| deltablue                | 7.47 ms                                                      | 3.63 ms: 2.06x faster                                       |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.96x faster                                      |
| raytrace                 | 488 ms                                                       | 281 ms: 1.74x faster                                        |
| chaos                    | 107 ms                                                       | 62.5 ms: 1.71x faster                                       |
| logging_silent           | 166 ns                                                       | 98.1 ns: 1.69x faster                                       |
| scimark_lu               | 164 ms                                                       | 100 ms: 1.64x faster                                        |
| crypto_pyaes             | 118 ms                                                       | 72.5 ms: 1.63x faster                                       |
| scimark_monte_carlo      | 109 ms                                                       | 69.0 ms: 1.59x faster                                       |
| sqlglot_parse            | 2.26 ms                                                      | 1.44 ms: 1.57x faster                                       |
| generators               | 58.0 ms                                                      | 37.1 ms: 1.56x faster                                       |
| bench_mp_pool            | 7.18 ms                                                      | 4.68 ms: 1.54x faster                                       |
| go                       | 259 ms                                                       | 171 ms: 1.51x faster                                        |
| richards_super           | 90.8 ms                                                      | 60.5 ms: 1.50x faster                                       |
| async_tree_none          | 700 ms                                                       | 469 ms: 1.49x faster                                        |
| async_tree_io            | 1.61 sec                                                     | 1.08 sec: 1.49x faster                                      |
| sqlglot_transpile        | 2.71 ms                                                      | 1.84 ms: 1.47x faster                                       |
| nbody                    | 137 ms                                                       | 93.6 ms: 1.47x faster                                       |
| hexiom                   | 9.52 ms                                                      | 6.50 ms: 1.46x faster                                       |
| async_tree_memoization   | 824 ms                                                       | 564 ms: 1.46x faster                                        |
| spectral_norm            | 136 ms                                                       | 93.9 ms: 1.45x faster                                       |
| unpickle_pure_python     | 321 us                                                       | 221 us: 1.45x faster                                        |
| mako                     | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                       |
| pickle_pure_python       | 457 us                                                       | 323 us: 1.42x faster                                        |
| richards                 | 74.1 ms                                                      | 53.9 ms: 1.38x faster                                       |
| json_dumps               | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                       |
| float                    | 110 ms                                                       | 81.3 ms: 1.36x faster                                       |
| pyflate                  | 697 ms                                                       | 519 ms: 1.34x faster                                        |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 716 ms: 1.33x faster                                        |
| coroutines               | 30.4 ms                                                      | 23.2 ms: 1.31x faster                                       |
| logging_simple           | 8.90 us                                                      | 6.82 us: 1.30x faster                                       |
| regex_compile            | 194 ms                                                       | 150 ms: 1.29x faster                                        |
| deepcopy_memo            | 48.9 us                                                      | 37.9 us: 1.29x faster                                       |
| logging_format           | 9.57 us                                                      | 7.46 us: 1.28x faster                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                      |
| tomli_loads              | 2.97 sec                                                     | 2.32 sec: 1.28x faster                                      |
| xml_etree_process        | 76.0 ms                                                      | 59.4 ms: 1.28x faster                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 821 ms: 1.28x faster                                        |
| fannkuch                 | 496 ms                                                       | 390 ms: 1.27x faster                                        |
| tornado_http             | 152 ms                                                       | 121 ms: 1.25x faster                                        |
| mypy2                    | 466 ms                                                       | 372 ms: 1.25x faster                                        |
| pycparser                | 1.66 sec                                                     | 1.34 sec: 1.24x faster                                      |
| nqueens                  | 112 ms                                                       | 91.2 ms: 1.23x faster                                       |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                        |
| comprehensions           | 26.9 us                                                      | 21.9 us: 1.23x faster                                       |
| scimark_sor              | 177 ms                                                       | 146 ms: 1.22x faster                                        |
| mdp                      | 3.03 sec                                                     | 2.55 sec: 1.19x faster                                      |
| sqlglot_optimize         | 70.3 ms                                                      | 59.2 ms: 1.19x faster                                       |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.38 ms: 1.19x faster                                       |
| json_loads               | 30.0 us                                                      | 25.4 us: 1.18x faster                                       |
| bench_thread_pool        | 1.14 ms                                                      | 965 us: 1.18x faster                                        |
| deepcopy                 | 454 us                                                       | 388 us: 1.17x faster                                        |
| dulwich_log              | 80.1 ms                                                      | 68.4 ms: 1.17x faster                                       |
| docutils                 | 3.40 sec                                                     | 2.92 sec: 1.17x faster                                      |
| unpack_sequence          | 59.5 ns                                                      | 51.4 ns: 1.16x faster                                       |
| deepcopy_reduce          | 4.03 us                                                      | 3.50 us: 1.15x faster                                       |
| scimark_fft              | 359 ms                                                       | 316 ms: 1.14x faster                                        |
| json                     | 5.96 ms                                                      | 5.25 ms: 1.14x faster                                       |
| regex_v8                 | 26.6 ms                                                      | 23.9 ms: 1.11x faster                                       |
| pathlib                  | 21.7 ms                                                      | 19.6 ms: 1.11x faster                                       |
| create_gc_cycles         | 1.82 ms                                                      | 1.65 ms: 1.10x faster                                       |
| regex_dna                | 259 ms                                                       | 236 ms: 1.10x faster                                        |
| xml_etree_parse          | 162 ms                                                       | 148 ms: 1.09x faster                                        |
| xml_etree_generate       | 94.6 ms                                                      | 86.7 ms: 1.09x faster                                       |
| sqlite_synth             | 2.97 us                                                      | 2.74 us: 1.08x faster                                       |
| async_generators         | 422 ms                                                       | 395 ms: 1.07x faster                                        |
| meteor_contest           | 137 ms                                                       | 130 ms: 1.06x faster                                        |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                        |
| pidigits                 | 271 ms                                                       | 259 ms: 1.04x faster                                        |
| python_startup           | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                       |
| unpickle                 | 14.2 us                                                      | 14.6 us: 1.03x slower                                       |
| unpickle_list            | 4.49 us                                                      | 4.64 us: 1.03x slower                                       |
| pickle                   | 9.94 us                                                      | 10.4 us: 1.04x slower                                       |
| pickle_dict              | 30.0 us                                                      | 31.7 us: 1.06x slower                                       |
| pickle_list              | 4.11 us                                                      | 4.38 us: 1.07x slower                                       |
| gc_traversal             | 3.45 ms                                                      | 3.73 ms: 1.08x slower                                       |
| telco                    | 7.14 ms                                                      | 8.10 ms: 1.13x slower                                       |
| regex_effbot             | 2.99 ms                                                      | 3.41 ms: 1.14x slower                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.64 ms: 1.18x slower                                       |
| dask                     | 463 ms                                                       | 591 ms: 1.28x slower                                        |
| coverage                 | 64.0 ms                                                      | 91.9 ms: 1.44x slower                                       |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x
