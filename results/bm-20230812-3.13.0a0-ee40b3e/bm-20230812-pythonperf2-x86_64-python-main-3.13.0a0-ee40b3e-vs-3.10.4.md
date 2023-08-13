
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: ee40b3e
- commit date: 2023-08-12
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                      |
| tornado_http   | 152 ms                                                       | 122 ms: 1.25x faster                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 137 ms                                                       | 91.2 ms: 1.51x faster                                       |
| float          | 110 ms                                                       | 81.3 ms: 1.36x faster                                       |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                        | 1.29x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 151 ms: 1.28x faster                                        |
| regex_v8       | 26.6 ms                                                      | 23.5 ms: 1.13x faster                                       |
| regex_dna      | 259 ms                                                       | 238 ms: 1.09x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.33 ms: 1.11x slower                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 225 us: 1.42x faster                                        |
| pickle_pure_python   | 457 us                                                       | 324 us: 1.41x faster                                        |
| json_dumps           | 14.2 ms                                                      | 10.5 ms: 1.36x faster                                       |
| tomli_loads          | 2.97 sec                                                     | 2.28 sec: 1.30x faster                                      |
| xml_etree_process    | 76.0 ms                                                      | 58.8 ms: 1.29x faster                                       |
| json_loads           | 30.0 us                                                      | 25.8 us: 1.16x faster                                       |
| xml_etree_generate   | 94.6 ms                                                      | 85.2 ms: 1.11x faster                                       |
| xml_etree_parse      | 162 ms                                                       | 150 ms: 1.08x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                        |
| pickle               | 9.94 us                                                      | 10.2 us: 1.03x slower                                       |
| unpickle             | 14.2 us                                                      | 14.8 us: 1.05x slower                                       |
| unpickle_list        | 4.49 us                                                      | 4.74 us: 1.05x slower                                       |
| pickle_dict          | 30.0 us                                                      | 31.6 us: 1.06x slower                                       |
| pickle_list          | 4.11 us                                                      | 4.35 us: 1.06x slower                                       |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.65 ms: 1.18x slower                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 153 us: 3.41x faster                                        |
| asyncio_tcp              | 782 ms                                                       | 369 ms: 2.12x faster                                        |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.59 sec: 1.95x faster                                      |
| deltablue                | 7.47 ms                                                      | 3.84 ms: 1.95x faster                                       |
| raytrace                 | 488 ms                                                       | 278 ms: 1.76x faster                                        |
| chaos                    | 107 ms                                                       | 63.6 ms: 1.68x faster                                       |
| logging_silent           | 166 ns                                                       | 101 ns: 1.65x faster                                        |
| scimark_lu               | 164 ms                                                       | 100 ms: 1.63x faster                                        |
| generators               | 58.0 ms                                                      | 36.5 ms: 1.59x faster                                       |
| async_tree_none          | 700 ms                                                       | 441 ms: 1.59x faster                                        |
| sqlglot_parse            | 2.26 ms                                                      | 1.44 ms: 1.57x faster                                       |
| crypto_pyaes             | 118 ms                                                       | 75.7 ms: 1.56x faster                                       |
| scimark_monte_carlo      | 109 ms                                                       | 70.4 ms: 1.56x faster                                       |
| bench_mp_pool            | 7.18 ms                                                      | 4.62 ms: 1.55x faster                                       |
| nbody                    | 137 ms                                                       | 91.2 ms: 1.51x faster                                       |
| async_tree_memoization   | 824 ms                                                       | 552 ms: 1.49x faster                                        |
| async_tree_io            | 1.61 sec                                                     | 1.08 sec: 1.49x faster                                      |
| sqlglot_transpile        | 2.71 ms                                                      | 1.85 ms: 1.47x faster                                       |
| richards_super           | 90.8 ms                                                      | 62.6 ms: 1.45x faster                                       |
| go                       | 259 ms                                                       | 180 ms: 1.43x faster                                        |
| spectral_norm            | 136 ms                                                       | 95.1 ms: 1.43x faster                                       |
| hexiom                   | 9.52 ms                                                      | 6.65 ms: 1.43x faster                                       |
| unpickle_pure_python     | 321 us                                                       | 225 us: 1.42x faster                                        |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                       |
| pickle_pure_python       | 457 us                                                       | 324 us: 1.41x faster                                        |
| pyflate                  | 697 ms                                                       | 512 ms: 1.36x faster                                        |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 700 ms: 1.36x faster                                        |
| float                    | 110 ms                                                       | 81.3 ms: 1.36x faster                                       |
| json_dumps               | 14.2 ms                                                      | 10.5 ms: 1.36x faster                                       |
| richards                 | 74.1 ms                                                      | 56.3 ms: 1.32x faster                                       |
| coroutines               | 30.4 ms                                                      | 23.2 ms: 1.31x faster                                       |
| tomli_loads              | 2.97 sec                                                     | 2.28 sec: 1.30x faster                                      |
| xml_etree_process        | 76.0 ms                                                      | 58.8 ms: 1.29x faster                                       |
| fannkuch                 | 496 ms                                                       | 386 ms: 1.28x faster                                        |
| regex_compile            | 194 ms                                                       | 151 ms: 1.28x faster                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 825 ms: 1.27x faster                                        |
| deepcopy_memo            | 48.9 us                                                      | 38.6 us: 1.27x faster                                       |
| logging_simple           | 8.90 us                                                      | 7.07 us: 1.26x faster                                       |
| logging_format           | 9.57 us                                                      | 7.60 us: 1.26x faster                                       |
| tornado_http             | 152 ms                                                       | 122 ms: 1.25x faster                                        |
| pycparser                | 1.66 sec                                                     | 1.33 sec: 1.25x faster                                      |
| nqueens                  | 112 ms                                                       | 90.5 ms: 1.24x faster                                       |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.20 ms: 1.24x faster                                       |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.22x faster                                        |
| scimark_fft              | 359 ms                                                       | 301 ms: 1.19x faster                                        |
| mdp                      | 3.03 sec                                                     | 2.54 sec: 1.19x faster                                      |
| comprehensions           | 26.9 us                                                      | 22.9 us: 1.18x faster                                       |
| sqlglot_optimize         | 70.3 ms                                                      | 59.7 ms: 1.18x faster                                       |
| docutils                 | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                      |
| bench_thread_pool        | 1.14 ms                                                      | 974 us: 1.17x faster                                        |
| json_loads               | 30.0 us                                                      | 25.8 us: 1.16x faster                                       |
| dulwich_log              | 80.1 ms                                                      | 69.3 ms: 1.16x faster                                       |
| scimark_sor              | 177 ms                                                       | 153 ms: 1.15x faster                                        |
| regex_v8                 | 26.6 ms                                                      | 23.5 ms: 1.13x faster                                       |
| json                     | 5.96 ms                                                      | 5.27 ms: 1.13x faster                                       |
| deepcopy                 | 454 us                                                       | 407 us: 1.12x faster                                        |
| create_gc_cycles         | 1.82 ms                                                      | 1.63 ms: 1.11x faster                                       |
| deepcopy_reduce          | 4.03 us                                                      | 3.62 us: 1.11x faster                                       |
| pathlib                  | 21.7 ms                                                      | 19.5 ms: 1.11x faster                                       |
| xml_etree_generate       | 94.6 ms                                                      | 85.2 ms: 1.11x faster                                       |
| sqlite_synth             | 2.97 us                                                      | 2.68 us: 1.11x faster                                       |
| regex_dna                | 259 ms                                                       | 238 ms: 1.09x faster                                        |
| xml_etree_parse          | 162 ms                                                       | 150 ms: 1.08x faster                                        |
| meteor_contest           | 137 ms                                                       | 129 ms: 1.06x faster                                        |
| async_generators         | 422 ms                                                       | 402 ms: 1.05x faster                                        |
| unpack_sequence          | 59.5 ns                                                      | 56.8 ns: 1.05x faster                                       |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                        |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.04x faster                                        |
| python_startup           | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                       |
| pickle                   | 9.94 us                                                      | 10.2 us: 1.03x slower                                       |
| unpickle                 | 14.2 us                                                      | 14.8 us: 1.05x slower                                       |
| unpickle_list            | 4.49 us                                                      | 4.74 us: 1.05x slower                                       |
| pickle_dict              | 30.0 us                                                      | 31.6 us: 1.06x slower                                       |
| pickle_list              | 4.11 us                                                      | 4.35 us: 1.06x slower                                       |
| gc_traversal             | 3.45 ms                                                      | 3.72 ms: 1.08x slower                                       |
| regex_effbot             | 2.99 ms                                                      | 3.33 ms: 1.11x slower                                       |
| telco                    | 7.14 ms                                                      | 8.09 ms: 1.13x slower                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.65 ms: 1.18x slower                                       |
| dask                     | 463 ms                                                       | 594 ms: 1.28x slower                                        |
| coverage                 | 64.0 ms                                                      | 82.5 ms: 1.29x slower                                       |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
