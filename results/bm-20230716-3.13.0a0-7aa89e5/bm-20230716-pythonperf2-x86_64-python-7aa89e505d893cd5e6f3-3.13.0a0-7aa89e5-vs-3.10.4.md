
# Results vs. 3.10.4

- fork: python
- ref: 7aa89e505d893cd5e6f3
- machine: linux-x86_64
- commit hash: 7aa89e5
- commit date: 2023-07-16
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf2-x86_64-python-7aa89e505d893cd5e6f3-3.13.0a0-7aa89e5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| tornado_http   | 152 ms                                                       | 122 ms: 1.25x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf2-x86_64-python-7aa89e505d893cd5e6f3-3.13.0a0-7aa89e5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 90.6 ms: 1.51x faster                                                       |
| float          | 110 ms                                                       | 80.3 ms: 1.37x faster                                                       |
| pidigits       | 271 ms                                                       | 259 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf2-x86_64-python-7aa89e505d893cd5e6f3-3.13.0a0-7aa89e5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 150 ms: 1.29x faster                                                        |
| regex_v8       | 26.6 ms                                                      | 24.1 ms: 1.11x faster                                                       |
| regex_dna      | 259 ms                                                       | 238 ms: 1.09x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.44 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf2-x86_64-python-7aa89e505d893cd5e6f3-3.13.0a0-7aa89e5 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 314 us: 1.45x faster                                                        |
| unpickle_pure_python | 321 us                                                       | 221 us: 1.45x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                                       |
| xml_etree_process    | 76.0 ms                                                      | 59.6 ms: 1.28x faster                                                       |
| tomli_loads          | 2.97 sec                                                     | 2.33 sec: 1.27x faster                                                      |
| json_loads           | 30.0 us                                                      | 24.7 us: 1.21x faster                                                       |
| xml_etree_parse      | 162 ms                                                       | 146 ms: 1.10x faster                                                        |
| xml_etree_generate   | 94.6 ms                                                      | 86.7 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                                        |
| unpickle             | 14.2 us                                                      | 14.3 us: 1.01x slower                                                       |
| pickle               | 9.94 us                                                      | 10.2 us: 1.03x slower                                                       |
| pickle_list          | 4.11 us                                                      | 4.35 us: 1.06x slower                                                       |
| pickle_dict          | 30.0 us                                                      | 32.6 us: 1.09x slower                                                       |
| unpickle_list        | 4.49 us                                                      | 4.89 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf2-x86_64-python-7aa89e505d893cd5e6f3-3.13.0a0-7aa89e5 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.40 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf2-x86_64-python-7aa89e505d893cd5e6f3-3.13.0a0-7aa89e5 |
|-----------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf2-x86_64-python-7aa89e505d893cd5e6f3-3.13.0a0-7aa89e5 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 155 us: 3.38x faster                                                        |
| asyncio_tcp              | 782 ms                                                       | 380 ms: 2.06x faster                                                        |
| deltablue                | 7.47 ms                                                      | 3.72 ms: 2.01x faster                                                       |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| raytrace                 | 488 ms                                                       | 284 ms: 1.72x faster                                                        |
| chaos                    | 107 ms                                                       | 63.3 ms: 1.69x faster                                                       |
| logging_silent           | 166 ns                                                       | 98.5 ns: 1.68x faster                                                       |
| scimark_lu               | 164 ms                                                       | 99.8 ms: 1.64x faster                                                       |
| crypto_pyaes             | 118 ms                                                       | 73.9 ms: 1.60x faster                                                       |
| generators               | 58.0 ms                                                      | 36.7 ms: 1.58x faster                                                       |
| sqlglot_parse            | 2.26 ms                                                      | 1.43 ms: 1.58x faster                                                       |
| scimark_monte_carlo      | 109 ms                                                       | 70.9 ms: 1.54x faster                                                       |
| nbody                    | 137 ms                                                       | 90.6 ms: 1.51x faster                                                       |
| richards_super           | 90.8 ms                                                      | 60.8 ms: 1.49x faster                                                       |
| go                       | 259 ms                                                       | 173 ms: 1.49x faster                                                        |
| async_tree_io            | 1.61 sec                                                     | 1.08 sec: 1.49x faster                                                      |
| async_tree_none          | 700 ms                                                       | 470 ms: 1.49x faster                                                        |
| sqlglot_transpile        | 2.71 ms                                                      | 1.83 ms: 1.48x faster                                                       |
| hexiom                   | 9.52 ms                                                      | 6.47 ms: 1.47x faster                                                       |
| async_tree_memoization   | 824 ms                                                       | 564 ms: 1.46x faster                                                        |
| pickle_pure_python       | 457 us                                                       | 314 us: 1.45x faster                                                        |
| unpickle_pure_python     | 321 us                                                       | 221 us: 1.45x faster                                                        |
| spectral_norm            | 136 ms                                                       | 94.2 ms: 1.45x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                                       |
| float                    | 110 ms                                                       | 80.3 ms: 1.37x faster                                                       |
| richards                 | 74.1 ms                                                      | 54.6 ms: 1.36x faster                                                       |
| bench_mp_pool            | 7.18 ms                                                      | 5.31 ms: 1.35x faster                                                       |
| pyflate                  | 697 ms                                                       | 516 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 713 ms: 1.33x faster                                                        |
| coroutines               | 30.4 ms                                                      | 23.2 ms: 1.31x faster                                                       |
| deepcopy_memo            | 48.9 us                                                      | 37.4 us: 1.31x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 812 ms: 1.29x faster                                                        |
| regex_compile            | 194 ms                                                       | 150 ms: 1.29x faster                                                        |
| logging_simple           | 8.90 us                                                      | 6.94 us: 1.28x faster                                                       |
| xml_etree_process        | 76.0 ms                                                      | 59.6 ms: 1.28x faster                                                       |
| tomli_loads              | 2.97 sec                                                     | 2.33 sec: 1.27x faster                                                      |
| logging_format           | 9.57 us                                                      | 7.59 us: 1.26x faster                                                       |
| mypy2                    | 466 ms                                                       | 372 ms: 1.26x faster                                                        |
| tornado_http             | 152 ms                                                       | 122 ms: 1.25x faster                                                        |
| fannkuch                 | 496 ms                                                       | 398 ms: 1.25x faster                                                        |
| pycparser                | 1.66 sec                                                     | 1.34 sec: 1.24x faster                                                      |
| nqueens                  | 112 ms                                                       | 91.3 ms: 1.23x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.23x faster                                                        |
| json_loads               | 30.0 us                                                      | 24.7 us: 1.21x faster                                                       |
| deepcopy                 | 454 us                                                       | 374 us: 1.21x faster                                                        |
| scimark_sor              | 177 ms                                                       | 146 ms: 1.21x faster                                                        |
| comprehensions           | 26.9 us                                                      | 22.4 us: 1.20x faster                                                       |
| mdp                      | 3.03 sec                                                     | 2.54 sec: 1.19x faster                                                      |
| dulwich_log              | 80.1 ms                                                      | 67.4 ms: 1.19x faster                                                       |
| sqlglot_optimize         | 70.3 ms                                                      | 59.2 ms: 1.19x faster                                                       |
| deepcopy_reduce          | 4.03 us                                                      | 3.40 us: 1.19x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 962 us: 1.18x faster                                                        |
| json                     | 5.96 ms                                                      | 5.06 ms: 1.18x faster                                                       |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.41 ms: 1.18x faster                                                       |
| docutils                 | 3.40 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| scimark_fft              | 359 ms                                                       | 312 ms: 1.15x faster                                                        |
| unpack_sequence          | 59.5 ns                                                      | 52.8 ns: 1.13x faster                                                       |
| create_gc_cycles         | 1.82 ms                                                      | 1.63 ms: 1.11x faster                                                       |
| regex_v8                 | 26.6 ms                                                      | 24.1 ms: 1.11x faster                                                       |
| pathlib                  | 21.7 ms                                                      | 19.7 ms: 1.10x faster                                                       |
| xml_etree_parse          | 162 ms                                                       | 146 ms: 1.10x faster                                                        |
| sqlite_synth             | 2.97 us                                                      | 2.72 us: 1.09x faster                                                       |
| xml_etree_generate       | 94.6 ms                                                      | 86.7 ms: 1.09x faster                                                       |
| regex_dna                | 259 ms                                                       | 238 ms: 1.09x faster                                                        |
| async_generators         | 422 ms                                                       | 393 ms: 1.07x faster                                                        |
| meteor_contest           | 137 ms                                                       | 130 ms: 1.05x faster                                                        |
| pidigits                 | 271 ms                                                       | 259 ms: 1.05x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.04x faster                                                        |
| python_startup           | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                       |
| unpickle                 | 14.2 us                                                      | 14.3 us: 1.01x slower                                                       |
| pickle                   | 9.94 us                                                      | 10.2 us: 1.03x slower                                                       |
| pickle_list              | 4.11 us                                                      | 4.35 us: 1.06x slower                                                       |
| telco                    | 7.14 ms                                                      | 7.60 ms: 1.06x slower                                                       |
| pickle_dict              | 30.0 us                                                      | 32.6 us: 1.09x slower                                                       |
| gc_traversal             | 3.45 ms                                                      | 3.76 ms: 1.09x slower                                                       |
| unpickle_list            | 4.49 us                                                      | 4.89 us: 1.09x slower                                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.40 ms: 1.15x slower                                                       |
| regex_effbot             | 2.99 ms                                                      | 3.44 ms: 1.15x slower                                                       |
| dask                     | 463 ms                                                       | 587 ms: 1.27x slower                                                        |
| coverage                 | 64.0 ms                                                      | 91.7 ms: 1.43x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
