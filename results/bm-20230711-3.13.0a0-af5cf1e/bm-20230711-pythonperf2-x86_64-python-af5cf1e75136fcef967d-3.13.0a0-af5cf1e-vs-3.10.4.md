
# Results vs. 3.10.4

- fork: python
- ref: af5cf1e75136fcef967d
- machine: linux-x86_64
- commit hash: af5cf1e
- commit date: 2023-07-11
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.92 sec: 1.16x faster                                                      |
| tornado_http   | 152 ms                                                       | 122 ms: 1.24x faster                                                        |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 88.8 ms: 1.55x faster                                                       |
| float          | 110 ms                                                       | 84.3 ms: 1.31x faster                                                       |
| pidigits       | 271 ms                                                       | 259 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 151 ms: 1.29x faster                                                        |
| regex_v8       | 26.6 ms                                                      | 24.1 ms: 1.11x faster                                                       |
| regex_dna      | 259 ms                                                       | 246 ms: 1.05x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.57 ms: 1.19x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 312 us: 1.46x faster                                                        |
| unpickle_pure_python | 321 us                                                       | 220 us: 1.46x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 10.1 ms: 1.40x faster                                                       |
| xml_etree_process    | 76.0 ms                                                      | 59.6 ms: 1.28x faster                                                       |
| tomli_loads          | 2.97 sec                                                     | 2.36 sec: 1.26x faster                                                      |
| json_loads           | 30.0 us                                                      | 24.8 us: 1.21x faster                                                       |
| xml_etree_generate   | 94.6 ms                                                      | 85.6 ms: 1.11x faster                                                       |
| xml_etree_parse      | 162 ms                                                       | 147 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                                        |
| unpickle             | 14.2 us                                                      | 14.6 us: 1.03x slower                                                       |
| unpickle_list        | 4.49 us                                                      | 4.67 us: 1.04x slower                                                       |
| pickle_dict          | 30.0 us                                                      | 32.1 us: 1.07x slower                                                       |
| pickle_list          | 4.11 us                                                      | 4.42 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.41 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|-----------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.5 ms: 1.39x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 151 us: 3.46x faster                                                        |
| asyncio_tcp              | 782 ms                                                       | 386 ms: 2.03x faster                                                        |
| deltablue                | 7.47 ms                                                      | 3.75 ms: 1.99x faster                                                       |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| raytrace                 | 488 ms                                                       | 277 ms: 1.76x faster                                                        |
| chaos                    | 107 ms                                                       | 62.2 ms: 1.72x faster                                                       |
| logging_silent           | 166 ns                                                       | 97.7 ns: 1.70x faster                                                       |
| scimark_lu               | 164 ms                                                       | 99.2 ms: 1.65x faster                                                       |
| crypto_pyaes             | 118 ms                                                       | 73.7 ms: 1.60x faster                                                       |
| generators               | 58.0 ms                                                      | 36.7 ms: 1.58x faster                                                       |
| sqlglot_parse            | 2.26 ms                                                      | 1.44 ms: 1.57x faster                                                       |
| bench_mp_pool            | 7.18 ms                                                      | 4.60 ms: 1.56x faster                                                       |
| nbody                    | 137 ms                                                       | 88.8 ms: 1.55x faster                                                       |
| richards_super           | 90.8 ms                                                      | 60.3 ms: 1.51x faster                                                       |
| scimark_monte_carlo      | 109 ms                                                       | 74.1 ms: 1.48x faster                                                       |
| async_tree_none          | 700 ms                                                       | 474 ms: 1.48x faster                                                        |
| go                       | 259 ms                                                       | 176 ms: 1.47x faster                                                        |
| hexiom                   | 9.52 ms                                                      | 6.47 ms: 1.47x faster                                                       |
| pickle_pure_python       | 457 us                                                       | 312 us: 1.46x faster                                                        |
| async_tree_io            | 1.61 sec                                                     | 1.10 sec: 1.46x faster                                                      |
| sqlglot_transpile        | 2.71 ms                                                      | 1.85 ms: 1.46x faster                                                       |
| unpickle_pure_python     | 321 us                                                       | 220 us: 1.46x faster                                                        |
| async_tree_memoization   | 824 ms                                                       | 573 ms: 1.44x faster                                                        |
| json_dumps               | 14.2 ms                                                      | 10.1 ms: 1.40x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.5 ms: 1.39x faster                                                       |
| spectral_norm            | 136 ms                                                       | 98.6 ms: 1.38x faster                                                       |
| pyflate                  | 697 ms                                                       | 516 ms: 1.35x faster                                                        |
| richards                 | 74.1 ms                                                      | 54.9 ms: 1.35x faster                                                       |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 720 ms: 1.32x faster                                                        |
| coroutines               | 30.4 ms                                                      | 23.2 ms: 1.31x faster                                                       |
| float                    | 110 ms                                                       | 84.3 ms: 1.31x faster                                                       |
| deepcopy_memo            | 48.9 us                                                      | 37.6 us: 1.30x faster                                                       |
| regex_compile            | 194 ms                                                       | 151 ms: 1.29x faster                                                        |
| xml_etree_process        | 76.0 ms                                                      | 59.6 ms: 1.28x faster                                                       |
| logging_simple           | 8.90 us                                                      | 6.99 us: 1.27x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.69 sec: 1.27x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 828 ms: 1.27x faster                                                        |
| tomli_loads              | 2.97 sec                                                     | 2.36 sec: 1.26x faster                                                      |
| mypy2                    | 466 ms                                                       | 372 ms: 1.26x faster                                                        |
| logging_format           | 9.57 us                                                      | 7.65 us: 1.25x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.25x faster                                                        |
| tornado_http             | 152 ms                                                       | 122 ms: 1.24x faster                                                        |
| pycparser                | 1.66 sec                                                     | 1.34 sec: 1.24x faster                                                      |
| unpack_sequence          | 59.5 ns                                                      | 47.9 ns: 1.24x faster                                                       |
| fannkuch                 | 496 ms                                                       | 402 ms: 1.23x faster                                                        |
| comprehensions           | 26.9 us                                                      | 22.0 us: 1.22x faster                                                       |
| nqueens                  | 112 ms                                                       | 92.1 ms: 1.22x faster                                                       |
| json_loads               | 30.0 us                                                      | 24.8 us: 1.21x faster                                                       |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.29 ms: 1.21x faster                                                       |
| scimark_sor              | 177 ms                                                       | 147 ms: 1.21x faster                                                        |
| deepcopy                 | 454 us                                                       | 376 us: 1.21x faster                                                        |
| sqlglot_optimize         | 70.3 ms                                                      | 58.7 ms: 1.20x faster                                                       |
| mdp                      | 3.03 sec                                                     | 2.54 sec: 1.19x faster                                                      |
| dulwich_log              | 80.1 ms                                                      | 67.6 ms: 1.18x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 962 us: 1.18x faster                                                        |
| deepcopy_reduce          | 4.03 us                                                      | 3.42 us: 1.18x faster                                                       |
| json                     | 5.96 ms                                                      | 5.12 ms: 1.17x faster                                                       |
| docutils                 | 3.40 sec                                                     | 2.92 sec: 1.16x faster                                                      |
| scimark_fft              | 359 ms                                                       | 312 ms: 1.15x faster                                                        |
| pathlib                  | 21.7 ms                                                      | 19.5 ms: 1.11x faster                                                       |
| regex_v8                 | 26.6 ms                                                      | 24.1 ms: 1.11x faster                                                       |
| xml_etree_generate       | 94.6 ms                                                      | 85.6 ms: 1.11x faster                                                       |
| xml_etree_parse          | 162 ms                                                       | 147 ms: 1.10x faster                                                        |
| create_gc_cycles         | 1.82 ms                                                      | 1.67 ms: 1.09x faster                                                       |
| sqlite_synth             | 2.97 us                                                      | 2.77 us: 1.07x faster                                                       |
| async_generators         | 422 ms                                                       | 398 ms: 1.06x faster                                                        |
| regex_dna                | 259 ms                                                       | 246 ms: 1.05x faster                                                        |
| meteor_contest           | 137 ms                                                       | 130 ms: 1.05x faster                                                        |
| pidigits                 | 271 ms                                                       | 259 ms: 1.04x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.04x faster                                                        |
| python_startup           | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                                       |
| unpickle                 | 14.2 us                                                      | 14.6 us: 1.03x slower                                                       |
| unpickle_list            | 4.49 us                                                      | 4.67 us: 1.04x slower                                                       |
| pickle_dict              | 30.0 us                                                      | 32.1 us: 1.07x slower                                                       |
| pickle_list              | 4.11 us                                                      | 4.42 us: 1.08x slower                                                       |
| telco                    | 7.14 ms                                                      | 7.70 ms: 1.08x slower                                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.41 ms: 1.15x slower                                                       |
| gc_traversal             | 3.45 ms                                                      | 4.02 ms: 1.16x slower                                                       |
| regex_effbot             | 2.99 ms                                                      | 3.57 ms: 1.19x slower                                                       |
| dask                     | 463 ms                                                       | 589 ms: 1.27x slower                                                        |
| coverage                 | 64.0 ms                                                      | 91.9 ms: 1.44x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
