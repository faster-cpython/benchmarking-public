
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3a314f7
- commit date: 2023-06-10
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                      |
| tornado_http   | 152 ms                                                       | 114 ms: 1.33x faster                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 137 ms                                                       | 86.3 ms: 1.59x faster                                       |
| float          | 110 ms                                                       | 79.4 ms: 1.39x faster                                       |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 147 ms: 1.32x faster                                        |
| regex_v8       | 26.6 ms                                                      | 24.8 ms: 1.07x faster                                       |
| regex_dna      | 259 ms                                                       | 247 ms: 1.05x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.63 ms: 1.21x slower                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 214 us: 1.50x faster                                        |
| pickle_pure_python   | 457 us                                                       | 318 us: 1.44x faster                                        |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.40x faster                                       |
| tomli_loads          | 2.97 sec                                                     | 2.25 sec: 1.32x faster                                      |
| xml_etree_process    | 76.0 ms                                                      | 59.3 ms: 1.28x faster                                       |
| json_loads           | 30.0 us                                                      | 24.2 us: 1.24x faster                                       |
| xml_etree_parse      | 162 ms                                                       | 146 ms: 1.10x faster                                        |
| xml_etree_generate   | 94.6 ms                                                      | 85.8 ms: 1.10x faster                                       |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.07x faster                                        |
| pickle               | 9.94 us                                                      | 10.1 us: 1.01x slower                                       |
| unpickle             | 14.2 us                                                      | 14.5 us: 1.02x slower                                       |
| pickle_dict          | 30.0 us                                                      | 30.8 us: 1.03x slower                                       |
| unpickle_list        | 4.49 us                                                      | 4.71 us: 1.05x slower                                       |
| pickle_list          | 4.11 us                                                      | 4.37 us: 1.06x slower                                       |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.2 ms: 1.02x faster                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.29 ms: 1.13x slower                                       |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7 |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 149 us: 3.50x faster                                        |
| deltablue                | 7.47 ms                                                      | 3.25 ms: 2.30x faster                                       |
| asyncio_tcp              | 782 ms                                                       | 381 ms: 2.05x faster                                        |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                      |
| logging_silent           | 166 ns                                                       | 91.9 ns: 1.80x faster                                       |
| scimark_lu               | 164 ms                                                       | 93.2 ms: 1.76x faster                                       |
| richards_super           | 90.8 ms                                                      | 52.2 ms: 1.74x faster                                       |
| go                       | 259 ms                                                       | 150 ms: 1.73x faster                                        |
| chaos                    | 107 ms                                                       | 63.6 ms: 1.68x faster                                       |
| scimark_sor              | 177 ms                                                       | 106 ms: 1.66x faster                                        |
| richards                 | 74.1 ms                                                      | 45.4 ms: 1.63x faster                                       |
| sqlglot_parse            | 2.26 ms                                                      | 1.39 ms: 1.63x faster                                       |
| raytrace                 | 488 ms                                                       | 302 ms: 1.62x faster                                        |
| hexiom                   | 9.52 ms                                                      | 5.89 ms: 1.62x faster                                       |
| nbody                    | 137 ms                                                       | 86.3 ms: 1.59x faster                                       |
| generators               | 58.0 ms                                                      | 36.9 ms: 1.57x faster                                       |
| pyflate                  | 697 ms                                                       | 444 ms: 1.57x faster                                        |
| scimark_monte_carlo      | 109 ms                                                       | 70.5 ms: 1.55x faster                                       |
| spectral_norm            | 136 ms                                                       | 88.0 ms: 1.55x faster                                       |
| sqlglot_transpile        | 2.71 ms                                                      | 1.80 ms: 1.51x faster                                       |
| unpickle_pure_python     | 321 us                                                       | 214 us: 1.50x faster                                        |
| async_tree_io            | 1.61 sec                                                     | 1.08 sec: 1.48x faster                                      |
| async_tree_none          | 700 ms                                                       | 472 ms: 1.48x faster                                        |
| bench_mp_pool            | 7.18 ms                                                      | 4.92 ms: 1.46x faster                                       |
| async_tree_memoization   | 824 ms                                                       | 565 ms: 1.46x faster                                        |
| crypto_pyaes             | 118 ms                                                       | 81.6 ms: 1.45x faster                                       |
| mako                     | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                       |
| pickle_pure_python       | 457 us                                                       | 318 us: 1.44x faster                                        |
| json_dumps               | 14.2 ms                                                      | 10.2 ms: 1.40x faster                                       |
| float                    | 110 ms                                                       | 79.4 ms: 1.39x faster                                       |
| fannkuch                 | 496 ms                                                       | 357 ms: 1.39x faster                                        |
| coroutines               | 30.4 ms                                                      | 21.9 ms: 1.39x faster                                       |
| tornado_http             | 152 ms                                                       | 114 ms: 1.33x faster                                        |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 715 ms: 1.33x faster                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                      |
| tomli_loads              | 2.97 sec                                                     | 2.25 sec: 1.32x faster                                      |
| regex_compile            | 194 ms                                                       | 147 ms: 1.32x faster                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 796 ms: 1.32x faster                                        |
| logging_simple           | 8.90 us                                                      | 6.78 us: 1.31x faster                                       |
| pycparser                | 1.66 sec                                                     | 1.28 sec: 1.30x faster                                      |
| logging_format           | 9.57 us                                                      | 7.36 us: 1.30x faster                                       |
| deepcopy_memo            | 48.9 us                                                      | 37.7 us: 1.30x faster                                       |
| xml_etree_process        | 76.0 ms                                                      | 59.3 ms: 1.28x faster                                       |
| mypy2                    | 466 ms                                                       | 366 ms: 1.27x faster                                        |
| unpack_sequence          | 59.5 ns                                                      | 46.8 ns: 1.27x faster                                       |
| comprehensions           | 26.9 us                                                      | 21.7 us: 1.24x faster                                       |
| json_loads               | 30.0 us                                                      | 24.2 us: 1.24x faster                                       |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.24x faster                                        |
| nqueens                  | 112 ms                                                       | 91.7 ms: 1.23x faster                                       |
| scimark_fft              | 359 ms                                                       | 294 ms: 1.22x faster                                        |
| deepcopy                 | 454 us                                                       | 371 us: 1.22x faster                                        |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.27 ms: 1.22x faster                                       |
| sqlglot_optimize         | 70.3 ms                                                      | 57.9 ms: 1.21x faster                                       |
| dulwich_log              | 80.1 ms                                                      | 66.3 ms: 1.21x faster                                       |
| mdp                      | 3.03 sec                                                     | 2.53 sec: 1.20x faster                                      |
| docutils                 | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                      |
| deepcopy_reduce          | 4.03 us                                                      | 3.42 us: 1.18x faster                                       |
| bench_thread_pool        | 1.14 ms                                                      | 966 us: 1.18x faster                                        |
| json                     | 5.96 ms                                                      | 5.12 ms: 1.17x faster                                       |
| pathlib                  | 21.7 ms                                                      | 19.6 ms: 1.11x faster                                       |
| xml_etree_parse          | 162 ms                                                       | 146 ms: 1.10x faster                                        |
| xml_etree_generate       | 94.6 ms                                                      | 85.8 ms: 1.10x faster                                       |
| sqlite_synth             | 2.97 us                                                      | 2.71 us: 1.10x faster                                       |
| create_gc_cycles         | 1.82 ms                                                      | 1.67 ms: 1.09x faster                                       |
| regex_v8                 | 26.6 ms                                                      | 24.8 ms: 1.07x faster                                       |
| async_generators         | 422 ms                                                       | 394 ms: 1.07x faster                                        |
| meteor_contest           | 137 ms                                                       | 128 ms: 1.07x faster                                        |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.07x faster                                        |
| regex_dna                | 259 ms                                                       | 247 ms: 1.05x faster                                        |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                        |
| python_startup           | 11.5 ms                                                      | 11.2 ms: 1.02x faster                                       |
| pickle                   | 9.94 us                                                      | 10.1 us: 1.01x slower                                       |
| unpickle                 | 14.2 us                                                      | 14.5 us: 1.02x slower                                       |
| pickle_dict              | 30.0 us                                                      | 30.8 us: 1.03x slower                                       |
| unpickle_list            | 4.49 us                                                      | 4.71 us: 1.05x slower                                       |
| pickle_list              | 4.11 us                                                      | 4.37 us: 1.06x slower                                       |
| gc_traversal             | 3.45 ms                                                      | 3.83 ms: 1.11x slower                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.29 ms: 1.13x slower                                       |
| regex_effbot             | 2.99 ms                                                      | 3.63 ms: 1.21x slower                                       |
| coverage                 | 64.0 ms                                                      | 89.0 ms: 1.39x slower                                       |
| Geometric mean           | (ref)                                                        | 1.31x faster                                                |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
