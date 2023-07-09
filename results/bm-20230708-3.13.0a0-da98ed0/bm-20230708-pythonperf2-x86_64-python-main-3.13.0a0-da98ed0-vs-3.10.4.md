
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: da98ed0
- commit date: 2023-07-08
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf2-x86_64-python-main-3.13.0a0-da98ed0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.92 sec: 1.17x faster                                      |
| tornado_http   | 152 ms                                                       | 122 ms: 1.24x faster                                        |
| Geometric mean | (ref)                                                        | 1.20x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf2-x86_64-python-main-3.13.0a0-da98ed0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 137 ms                                                       | 87.5 ms: 1.57x faster                                       |
| float          | 110 ms                                                       | 80.0 ms: 1.38x faster                                       |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf2-x86_64-python-main-3.13.0a0-da98ed0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 151 ms: 1.28x faster                                        |
| regex_v8       | 26.6 ms                                                      | 24.2 ms: 1.10x faster                                       |
| regex_dna      | 259 ms                                                       | 241 ms: 1.08x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.53 ms: 1.18x slower                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf2-x86_64-python-main-3.13.0a0-da98ed0 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 223 us: 1.44x faster                                        |
| pickle_pure_python   | 457 us                                                       | 323 us: 1.41x faster                                        |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                       |
| xml_etree_process    | 76.0 ms                                                      | 59.0 ms: 1.29x faster                                       |
| tomli_loads          | 2.97 sec                                                     | 2.39 sec: 1.24x faster                                      |
| json_loads           | 30.0 us                                                      | 24.6 us: 1.22x faster                                       |
| xml_etree_generate   | 94.6 ms                                                      | 85.0 ms: 1.11x faster                                       |
| xml_etree_parse      | 162 ms                                                       | 147 ms: 1.10x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 107 ms: 1.03x faster                                        |
| pickle               | 9.94 us                                                      | 10.1 us: 1.02x slower                                       |
| unpickle             | 14.2 us                                                      | 14.5 us: 1.02x slower                                       |
| pickle_dict          | 30.0 us                                                      | 31.0 us: 1.03x slower                                       |
| unpickle_list        | 4.49 us                                                      | 4.67 us: 1.04x slower                                       |
| pickle_list          | 4.11 us                                                      | 4.29 us: 1.05x slower                                       |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf2-x86_64-python-main-3.13.0a0-da98ed0 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.36 ms: 1.14x slower                                       |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf2-x86_64-python-main-3.13.0a0-da98ed0 |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-pythonperf2-x86_64-python-main-3.13.0a0-da98ed0 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 152 us: 3.43x faster                                        |
| deltablue                | 7.47 ms                                                      | 3.53 ms: 2.12x faster                                       |
| asyncio_tcp              | 782 ms                                                       | 381 ms: 2.05x faster                                        |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                      |
| raytrace                 | 488 ms                                                       | 277 ms: 1.76x faster                                        |
| chaos                    | 107 ms                                                       | 62.4 ms: 1.72x faster                                       |
| logging_silent           | 166 ns                                                       | 97.0 ns: 1.71x faster                                       |
| scimark_lu               | 164 ms                                                       | 99.2 ms: 1.65x faster                                       |
| generators               | 58.0 ms                                                      | 36.3 ms: 1.60x faster                                       |
| nbody                    | 137 ms                                                       | 87.5 ms: 1.57x faster                                       |
| richards_super           | 90.8 ms                                                      | 58.3 ms: 1.56x faster                                       |
| sqlglot_parse            | 2.26 ms                                                      | 1.47 ms: 1.54x faster                                       |
| scimark_monte_carlo      | 109 ms                                                       | 72.5 ms: 1.51x faster                                       |
| async_tree_none          | 700 ms                                                       | 465 ms: 1.50x faster                                        |
| async_tree_io            | 1.61 sec                                                     | 1.08 sec: 1.49x faster                                      |
| go                       | 259 ms                                                       | 173 ms: 1.49x faster                                        |
| async_tree_memoization   | 824 ms                                                       | 561 ms: 1.47x faster                                        |
| hexiom                   | 9.52 ms                                                      | 6.50 ms: 1.46x faster                                       |
| mako                     | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                       |
| sqlglot_transpile        | 2.71 ms                                                      | 1.88 ms: 1.44x faster                                       |
| unpickle_pure_python     | 321 us                                                       | 223 us: 1.44x faster                                        |
| pickle_pure_python       | 457 us                                                       | 323 us: 1.41x faster                                        |
| crypto_pyaes             | 118 ms                                                       | 83.7 ms: 1.41x faster                                       |
| richards                 | 74.1 ms                                                      | 52.5 ms: 1.41x faster                                       |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                       |
| float                    | 110 ms                                                       | 80.0 ms: 1.38x faster                                       |
| pyflate                  | 697 ms                                                       | 510 ms: 1.37x faster                                        |
| spectral_norm            | 136 ms                                                       | 99.9 ms: 1.36x faster                                       |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 713 ms: 1.33x faster                                        |
| coroutines               | 30.4 ms                                                      | 23.1 ms: 1.32x faster                                       |
| deepcopy_memo            | 48.9 us                                                      | 37.3 us: 1.31x faster                                       |
| logging_simple           | 8.90 us                                                      | 6.88 us: 1.29x faster                                       |
| xml_etree_process        | 76.0 ms                                                      | 59.0 ms: 1.29x faster                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                      |
| logging_format           | 9.57 us                                                      | 7.45 us: 1.28x faster                                       |
| regex_compile            | 194 ms                                                       | 151 ms: 1.28x faster                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 820 ms: 1.28x faster                                        |
| pycparser                | 1.66 sec                                                     | 1.31 sec: 1.27x faster                                      |
| fannkuch                 | 496 ms                                                       | 392 ms: 1.26x faster                                        |
| mypy2                    | 466 ms                                                       | 371 ms: 1.26x faster                                        |
| tomli_loads              | 2.97 sec                                                     | 2.39 sec: 1.24x faster                                      |
| tornado_http             | 152 ms                                                       | 122 ms: 1.24x faster                                        |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.23x faster                                        |
| json_loads               | 30.0 us                                                      | 24.6 us: 1.22x faster                                       |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.28 ms: 1.21x faster                                       |
| nqueens                  | 112 ms                                                       | 92.8 ms: 1.21x faster                                       |
| scimark_sor              | 177 ms                                                       | 146 ms: 1.21x faster                                        |
| comprehensions           | 26.9 us                                                      | 22.2 us: 1.21x faster                                       |
| bench_thread_pool        | 1.14 ms                                                      | 939 us: 1.21x faster                                        |
| mdp                      | 3.03 sec                                                     | 2.53 sec: 1.20x faster                                      |
| dulwich_log              | 80.1 ms                                                      | 66.7 ms: 1.20x faster                                       |
| deepcopy                 | 454 us                                                       | 381 us: 1.19x faster                                        |
| sqlglot_optimize         | 70.3 ms                                                      | 59.4 ms: 1.18x faster                                       |
| deepcopy_reduce          | 4.03 us                                                      | 3.41 us: 1.18x faster                                       |
| docutils                 | 3.40 sec                                                     | 2.92 sec: 1.17x faster                                      |
| json                     | 5.96 ms                                                      | 5.17 ms: 1.15x faster                                       |
| scimark_fft              | 359 ms                                                       | 312 ms: 1.15x faster                                        |
| create_gc_cycles         | 1.82 ms                                                      | 1.63 ms: 1.12x faster                                       |
| xml_etree_generate       | 94.6 ms                                                      | 85.0 ms: 1.11x faster                                       |
| pathlib                  | 21.7 ms                                                      | 19.6 ms: 1.10x faster                                       |
| xml_etree_parse          | 162 ms                                                       | 147 ms: 1.10x faster                                        |
| regex_v8                 | 26.6 ms                                                      | 24.2 ms: 1.10x faster                                       |
| unpack_sequence          | 59.5 ns                                                      | 54.5 ns: 1.09x faster                                       |
| sqlite_synth             | 2.97 us                                                      | 2.74 us: 1.08x faster                                       |
| regex_dna                | 259 ms                                                       | 241 ms: 1.08x faster                                        |
| async_generators         | 422 ms                                                       | 399 ms: 1.06x faster                                        |
| meteor_contest           | 137 ms                                                       | 130 ms: 1.05x faster                                        |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                        |
| xml_etree_iterparse      | 110 ms                                                       | 107 ms: 1.03x faster                                        |
| python_startup           | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                       |
| pickle                   | 9.94 us                                                      | 10.1 us: 1.02x slower                                       |
| unpickle                 | 14.2 us                                                      | 14.5 us: 1.02x slower                                       |
| pickle_dict              | 30.0 us                                                      | 31.0 us: 1.03x slower                                       |
| gc_traversal             | 3.45 ms                                                      | 3.58 ms: 1.04x slower                                       |
| unpickle_list            | 4.49 us                                                      | 4.67 us: 1.04x slower                                       |
| pickle_list              | 4.11 us                                                      | 4.29 us: 1.05x slower                                       |
| telco                    | 7.14 ms                                                      | 7.72 ms: 1.08x slower                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.36 ms: 1.14x slower                                       |
| regex_effbot             | 2.99 ms                                                      | 3.53 ms: 1.18x slower                                       |
| dask                     | 463 ms                                                       | 589 ms: 1.27x slower                                        |
| coverage                 | 64.0 ms                                                      | 87.7 ms: 1.37x slower                                       |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
