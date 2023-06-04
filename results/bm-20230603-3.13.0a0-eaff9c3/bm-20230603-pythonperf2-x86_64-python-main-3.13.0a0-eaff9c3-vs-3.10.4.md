
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: eaff9c3
- commit date: 2023-06-03
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-pythonperf2-x86_64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                      |
| tornado_http   | 152 ms                                                       | 115 ms: 1.32x faster                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-pythonperf2-x86_64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 137 ms                                                       | 85.6 ms: 1.60x faster                                       |
| float          | 110 ms                                                       | 78.2 ms: 1.41x faster                                       |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                        | 1.33x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-pythonperf2-x86_64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 144 ms: 1.34x faster                                        |
| regex_v8       | 26.6 ms                                                      | 24.5 ms: 1.09x faster                                       |
| regex_dna      | 259 ms                                                       | 246 ms: 1.05x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.67 ms: 1.22x slower                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-pythonperf2-x86_64-python-main-3.13.0a0-eaff9c3 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 208 us: 1.54x faster                                        |
| pickle_pure_python   | 457 us                                                       | 324 us: 1.41x faster                                        |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                       |
| tomli_loads          | 2.97 sec                                                     | 2.16 sec: 1.38x faster                                      |
| xml_etree_process    | 76.0 ms                                                      | 58.4 ms: 1.30x faster                                       |
| json_loads           | 30.0 us                                                      | 24.0 us: 1.25x faster                                       |
| xml_etree_generate   | 94.6 ms                                                      | 85.4 ms: 1.11x faster                                       |
| xml_etree_parse      | 162 ms                                                       | 146 ms: 1.10x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                        |
| unpickle             | 14.2 us                                                      | 14.3 us: 1.01x slower                                       |
| unpickle_list        | 4.49 us                                                      | 4.70 us: 1.05x slower                                       |
| pickle_dict          | 30.0 us                                                      | 31.9 us: 1.06x slower                                       |
| pickle_list          | 4.11 us                                                      | 4.40 us: 1.07x slower                                       |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-pythonperf2-x86_64-python-main-3.13.0a0-eaff9c3 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.43 ms: 1.15x slower                                       |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-pythonperf2-x86_64-python-main-3.13.0a0-eaff9c3 |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.1 ms: 1.45x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-pythonperf2-x86_64-python-main-3.13.0a0-eaff9c3 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 149 us: 3.52x faster                                        |
| deltablue                | 7.47 ms                                                      | 3.23 ms: 2.31x faster                                       |
| asyncio_tcp              | 782 ms                                                       | 383 ms: 2.04x faster                                        |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                      |
| go                       | 259 ms                                                       | 146 ms: 1.77x faster                                        |
| logging_silent           | 166 ns                                                       | 94.9 ns: 1.75x faster                                       |
| richards_super           | 90.8 ms                                                      | 52.4 ms: 1.73x faster                                       |
| chaos                    | 107 ms                                                       | 63.3 ms: 1.69x faster                                       |
| scimark_lu               | 164 ms                                                       | 97.0 ms: 1.69x faster                                       |
| scimark_sor              | 177 ms                                                       | 108 ms: 1.64x faster                                        |
| generators               | 58.0 ms                                                      | 35.5 ms: 1.63x faster                                       |
| sqlglot_parse            | 2.26 ms                                                      | 1.39 ms: 1.63x faster                                       |
| hexiom                   | 9.52 ms                                                      | 5.86 ms: 1.62x faster                                       |
| richards                 | 74.1 ms                                                      | 45.9 ms: 1.61x faster                                       |
| nbody                    | 137 ms                                                       | 85.6 ms: 1.60x faster                                       |
| scimark_monte_carlo      | 109 ms                                                       | 68.7 ms: 1.59x faster                                       |
| raytrace                 | 488 ms                                                       | 307 ms: 1.59x faster                                        |
| pyflate                  | 697 ms                                                       | 443 ms: 1.57x faster                                        |
| unpickle_pure_python     | 321 us                                                       | 208 us: 1.54x faster                                        |
| sqlglot_transpile        | 2.71 ms                                                      | 1.78 ms: 1.52x faster                                       |
| async_tree_none          | 700 ms                                                       | 467 ms: 1.50x faster                                        |
| async_tree_io            | 1.61 sec                                                     | 1.07 sec: 1.50x faster                                      |
| async_tree_memoization   | 824 ms                                                       | 558 ms: 1.48x faster                                        |
| spectral_norm            | 136 ms                                                       | 92.8 ms: 1.47x faster                                       |
| crypto_pyaes             | 118 ms                                                       | 80.8 ms: 1.46x faster                                       |
| mako                     | 14.7 ms                                                      | 10.1 ms: 1.45x faster                                       |
| bench_mp_pool            | 7.18 ms                                                      | 5.09 ms: 1.41x faster                                       |
| float                    | 110 ms                                                       | 78.2 ms: 1.41x faster                                       |
| pickle_pure_python       | 457 us                                                       | 324 us: 1.41x faster                                        |
| json_dumps               | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                       |
| tomli_loads              | 2.97 sec                                                     | 2.16 sec: 1.38x faster                                      |
| fannkuch                 | 496 ms                                                       | 361 ms: 1.37x faster                                        |
| regex_compile            | 194 ms                                                       | 144 ms: 1.34x faster                                        |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 709 ms: 1.34x faster                                        |
| coroutines               | 30.4 ms                                                      | 22.8 ms: 1.34x faster                                       |
| logging_simple           | 8.90 us                                                      | 6.69 us: 1.33x faster                                       |
| deepcopy_memo            | 48.9 us                                                      | 36.8 us: 1.33x faster                                       |
| tornado_http             | 152 ms                                                       | 115 ms: 1.32x faster                                        |
| logging_format           | 9.57 us                                                      | 7.27 us: 1.32x faster                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                      |
| xml_etree_process        | 76.0 ms                                                      | 58.4 ms: 1.30x faster                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 808 ms: 1.30x faster                                        |
| pycparser                | 1.66 sec                                                     | 1.29 sec: 1.29x faster                                      |
| mypy2                    | 466 ms                                                       | 366 ms: 1.27x faster                                        |
| sqlglot_normalize        | 144 ms                                                       | 115 ms: 1.25x faster                                        |
| comprehensions           | 26.9 us                                                      | 21.5 us: 1.25x faster                                       |
| json_loads               | 30.0 us                                                      | 24.0 us: 1.25x faster                                       |
| nqueens                  | 112 ms                                                       | 91.0 ms: 1.24x faster                                       |
| dulwich_log              | 80.1 ms                                                      | 65.3 ms: 1.23x faster                                       |
| sqlglot_optimize         | 70.3 ms                                                      | 57.5 ms: 1.22x faster                                       |
| deepcopy                 | 454 us                                                       | 376 us: 1.21x faster                                        |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.32 ms: 1.20x faster                                       |
| bench_thread_pool        | 1.14 ms                                                      | 947 us: 1.20x faster                                        |
| scimark_fft              | 359 ms                                                       | 302 ms: 1.19x faster                                        |
| mdp                      | 3.03 sec                                                     | 2.56 sec: 1.19x faster                                      |
| deepcopy_reduce          | 4.03 us                                                      | 3.41 us: 1.18x faster                                       |
| docutils                 | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                      |
| json                     | 5.96 ms                                                      | 5.16 ms: 1.16x faster                                       |
| create_gc_cycles         | 1.82 ms                                                      | 1.63 ms: 1.12x faster                                       |
| pathlib                  | 21.7 ms                                                      | 19.5 ms: 1.11x faster                                       |
| unpack_sequence          | 59.5 ns                                                      | 53.5 ns: 1.11x faster                                       |
| xml_etree_generate       | 94.6 ms                                                      | 85.4 ms: 1.11x faster                                       |
| xml_etree_parse          | 162 ms                                                       | 146 ms: 1.10x faster                                        |
| sqlite_synth             | 2.97 us                                                      | 2.71 us: 1.09x faster                                       |
| regex_v8                 | 26.6 ms                                                      | 24.5 ms: 1.09x faster                                       |
| meteor_contest           | 137 ms                                                       | 126 ms: 1.08x faster                                        |
| async_generators         | 422 ms                                                       | 391 ms: 1.08x faster                                        |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                        |
| regex_dna                | 259 ms                                                       | 246 ms: 1.05x faster                                        |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                        |
| python_startup           | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                       |
| unpickle                 | 14.2 us                                                      | 14.3 us: 1.01x slower                                       |
| gc_traversal             | 3.45 ms                                                      | 3.56 ms: 1.03x slower                                       |
| unpickle_list            | 4.49 us                                                      | 4.70 us: 1.05x slower                                       |
| pickle_dict              | 30.0 us                                                      | 31.9 us: 1.06x slower                                       |
| pickle_list              | 4.11 us                                                      | 4.40 us: 1.07x slower                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.43 ms: 1.15x slower                                       |
| regex_effbot             | 2.99 ms                                                      | 3.67 ms: 1.22x slower                                       |
| coverage                 | 64.0 ms                                                      | 91.9 ms: 1.44x slower                                       |
| Geometric mean           | (ref)                                                        | 1.31x faster                                                |

Benchmark hidden because not significant (2): telco, pickle
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
