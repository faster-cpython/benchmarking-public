
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 0a9b339
- commit date: 2023-07-24
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.92 sec: 1.16x faster                                      |
| tornado_http   | 152 ms                                                       | 123 ms: 1.23x faster                                        |
| Geometric mean | (ref)                                                        | 1.20x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 137 ms                                                       | 88.2 ms: 1.56x faster                                       |
| float          | 110 ms                                                       | 81.0 ms: 1.36x faster                                       |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 151 ms: 1.28x faster                                        |
| regex_v8       | 26.6 ms                                                      | 24.1 ms: 1.11x faster                                       |
| regex_dna      | 259 ms                                                       | 245 ms: 1.06x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 222 us: 1.44x faster                                        |
| pickle_pure_python   | 457 us                                                       | 316 us: 1.44x faster                                        |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                       |
| xml_etree_process    | 76.0 ms                                                      | 59.0 ms: 1.29x faster                                       |
| tomli_loads          | 2.97 sec                                                     | 2.34 sec: 1.27x faster                                      |
| json_loads           | 30.0 us                                                      | 24.1 us: 1.24x faster                                       |
| xml_etree_parse      | 162 ms                                                       | 143 ms: 1.13x faster                                        |
| xml_etree_generate   | 94.6 ms                                                      | 87.1 ms: 1.09x faster                                       |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                        |
| unpickle             | 14.2 us                                                      | 14.5 us: 1.02x slower                                       |
| pickle               | 9.94 us                                                      | 10.2 us: 1.03x slower                                       |
| pickle_list          | 4.11 us                                                      | 4.29 us: 1.05x slower                                       |
| unpickle_list        | 4.49 us                                                      | 4.83 us: 1.07x slower                                       |
| pickle_dict          | 30.0 us                                                      | 33.3 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.42 ms: 1.15x slower                                       |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339 |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 156 us: 3.35x faster                                        |
| asyncio_tcp              | 782 ms                                                       | 369 ms: 2.12x faster                                        |
| deltablue                | 7.47 ms                                                      | 3.74 ms: 2.00x faster                                       |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.96x faster                                      |
| chaos                    | 107 ms                                                       | 62.1 ms: 1.72x faster                                       |
| raytrace                 | 488 ms                                                       | 284 ms: 1.72x faster                                        |
| logging_silent           | 166 ns                                                       | 97.1 ns: 1.71x faster                                       |
| scimark_lu               | 164 ms                                                       | 98.7 ms: 1.66x faster                                       |
| crypto_pyaes             | 118 ms                                                       | 73.4 ms: 1.61x faster                                       |
| scimark_monte_carlo      | 109 ms                                                       | 69.1 ms: 1.58x faster                                       |
| nbody                    | 137 ms                                                       | 88.2 ms: 1.56x faster                                       |
| sqlglot_parse            | 2.26 ms                                                      | 1.45 ms: 1.55x faster                                       |
| generators               | 58.0 ms                                                      | 37.4 ms: 1.55x faster                                       |
| richards_super           | 90.8 ms                                                      | 60.3 ms: 1.51x faster                                       |
| bench_mp_pool            | 7.18 ms                                                      | 4.79 ms: 1.50x faster                                       |
| async_tree_none          | 700 ms                                                       | 472 ms: 1.48x faster                                        |
| async_tree_io            | 1.61 sec                                                     | 1.09 sec: 1.48x faster                                      |
| go                       | 259 ms                                                       | 177 ms: 1.46x faster                                        |
| sqlglot_transpile        | 2.71 ms                                                      | 1.86 ms: 1.46x faster                                       |
| hexiom                   | 9.52 ms                                                      | 6.56 ms: 1.45x faster                                       |
| spectral_norm            | 136 ms                                                       | 94.1 ms: 1.45x faster                                       |
| async_tree_memoization   | 824 ms                                                       | 570 ms: 1.45x faster                                        |
| unpickle_pure_python     | 321 us                                                       | 222 us: 1.44x faster                                        |
| pickle_pure_python       | 457 us                                                       | 316 us: 1.44x faster                                        |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                       |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                       |
| float                    | 110 ms                                                       | 81.0 ms: 1.36x faster                                       |
| pyflate                  | 697 ms                                                       | 513 ms: 1.36x faster                                        |
| richards                 | 74.1 ms                                                      | 54.6 ms: 1.36x faster                                       |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 718 ms: 1.32x faster                                        |
| deepcopy_memo            | 48.9 us                                                      | 37.2 us: 1.31x faster                                       |
| coroutines               | 30.4 ms                                                      | 23.5 ms: 1.30x faster                                       |
| xml_etree_process        | 76.0 ms                                                      | 59.0 ms: 1.29x faster                                       |
| regex_compile            | 194 ms                                                       | 151 ms: 1.28x faster                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.69 sec: 1.28x faster                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 825 ms: 1.27x faster                                        |
| logging_simple           | 8.90 us                                                      | 7.00 us: 1.27x faster                                       |
| tomli_loads              | 2.97 sec                                                     | 2.34 sec: 1.27x faster                                      |
| logging_format           | 9.57 us                                                      | 7.56 us: 1.26x faster                                       |
| mypy2                    | 466 ms                                                       | 372 ms: 1.25x faster                                        |
| json_loads               | 30.0 us                                                      | 24.1 us: 1.24x faster                                       |
| fannkuch                 | 496 ms                                                       | 399 ms: 1.24x faster                                        |
| pycparser                | 1.66 sec                                                     | 1.34 sec: 1.24x faster                                      |
| tornado_http             | 152 ms                                                       | 123 ms: 1.23x faster                                        |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.28 ms: 1.21x faster                                       |
| nqueens                  | 112 ms                                                       | 93.0 ms: 1.21x faster                                       |
| comprehensions           | 26.9 us                                                      | 22.3 us: 1.21x faster                                       |
| deepcopy                 | 454 us                                                       | 375 us: 1.21x faster                                        |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                        |
| scimark_sor              | 177 ms                                                       | 147 ms: 1.20x faster                                        |
| mdp                      | 3.03 sec                                                     | 2.56 sec: 1.19x faster                                      |
| scimark_fft              | 359 ms                                                       | 305 ms: 1.18x faster                                        |
| sqlglot_optimize         | 70.3 ms                                                      | 59.8 ms: 1.18x faster                                       |
| json                     | 5.96 ms                                                      | 5.08 ms: 1.17x faster                                       |
| deepcopy_reduce          | 4.03 us                                                      | 3.45 us: 1.17x faster                                       |
| docutils                 | 3.40 sec                                                     | 2.92 sec: 1.16x faster                                      |
| bench_thread_pool        | 1.14 ms                                                      | 979 us: 1.16x faster                                        |
| dulwich_log              | 80.1 ms                                                      | 69.3 ms: 1.16x faster                                       |
| xml_etree_parse          | 162 ms                                                       | 143 ms: 1.13x faster                                        |
| unpack_sequence          | 59.5 ns                                                      | 53.3 ns: 1.12x faster                                       |
| pathlib                  | 21.7 ms                                                      | 19.5 ms: 1.11x faster                                       |
| regex_v8                 | 26.6 ms                                                      | 24.1 ms: 1.11x faster                                       |
| create_gc_cycles         | 1.82 ms                                                      | 1.66 ms: 1.10x faster                                       |
| xml_etree_generate       | 94.6 ms                                                      | 87.1 ms: 1.09x faster                                       |
| sqlite_synth             | 2.97 us                                                      | 2.76 us: 1.08x faster                                       |
| regex_dna                | 259 ms                                                       | 245 ms: 1.06x faster                                        |
| async_generators         | 422 ms                                                       | 399 ms: 1.06x faster                                        |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                        |
| meteor_contest           | 137 ms                                                       | 130 ms: 1.05x faster                                        |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                        |
| python_startup           | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                       |
| unpickle                 | 14.2 us                                                      | 14.5 us: 1.02x slower                                       |
| pickle                   | 9.94 us                                                      | 10.2 us: 1.03x slower                                       |
| pickle_list              | 4.11 us                                                      | 4.29 us: 1.05x slower                                       |
| unpickle_list            | 4.49 us                                                      | 4.83 us: 1.07x slower                                       |
| telco                    | 7.14 ms                                                      | 7.70 ms: 1.08x slower                                       |
| pickle_dict              | 30.0 us                                                      | 33.3 us: 1.11x slower                                       |
| gc_traversal             | 3.45 ms                                                      | 3.95 ms: 1.14x slower                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.42 ms: 1.15x slower                                       |
| regex_effbot             | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                       |
| dask                     | 463 ms                                                       | 591 ms: 1.28x slower                                        |
| coverage                 | 64.0 ms                                                      | 87.3 ms: 1.37x slower                                       |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
