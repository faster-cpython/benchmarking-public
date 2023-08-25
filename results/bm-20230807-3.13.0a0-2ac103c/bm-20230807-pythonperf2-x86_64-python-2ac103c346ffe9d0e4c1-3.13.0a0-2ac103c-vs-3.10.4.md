
# Results vs. 3.10.4

- fork: python
- ref: 2ac103c346ffe9d0e4c1
- machine: linux-x86_64
- commit hash: 2ac103c
- commit date: 2023-08-07
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| tornado_http   | 152 ms                                                       | 120 ms: 1.26x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 89.1 ms: 1.54x faster                                                       |
| float          | 110 ms                                                       | 81.3 ms: 1.36x faster                                                       |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 151 ms: 1.29x faster                                                        |
| regex_v8       | 26.6 ms                                                      | 24.0 ms: 1.11x faster                                                       |
| regex_dna      | 259 ms                                                       | 252 ms: 1.03x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.67 ms: 1.23x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 321 us: 1.42x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                       |
| unpickle_pure_python | 321 us                                                       | 236 us: 1.36x faster                                                        |
| xml_etree_process    | 76.0 ms                                                      | 59.6 ms: 1.28x faster                                                       |
| tomli_loads          | 2.97 sec                                                     | 2.41 sec: 1.23x faster                                                      |
| json_loads           | 30.0 us                                                      | 25.7 us: 1.17x faster                                                       |
| xml_etree_generate   | 94.6 ms                                                      | 84.9 ms: 1.11x faster                                                       |
| xml_etree_parse      | 162 ms                                                       | 147 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                                        |
| pickle               | 9.94 us                                                      | 10.2 us: 1.02x slower                                                       |
| unpickle             | 14.2 us                                                      | 15.1 us: 1.06x slower                                                       |
| unpickle_list        | 4.49 us                                                      | 4.79 us: 1.07x slower                                                       |
| pickle_dict          | 30.0 us                                                      | 32.7 us: 1.09x slower                                                       |
| pickle_list          | 4.11 us                                                      | 4.54 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.63 ms: 1.18x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c |
|-----------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 156 us: 3.34x faster                                                        |
| asyncio_tcp              | 782 ms                                                       | 369 ms: 2.12x faster                                                        |
| deltablue                | 7.47 ms                                                      | 3.67 ms: 2.04x faster                                                       |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| raytrace                 | 488 ms                                                       | 281 ms: 1.74x faster                                                        |
| chaos                    | 107 ms                                                       | 62.7 ms: 1.71x faster                                                       |
| logging_silent           | 166 ns                                                       | 97.0 ns: 1.71x faster                                                       |
| scimark_lu               | 164 ms                                                       | 99.0 ms: 1.65x faster                                                       |
| scimark_monte_carlo      | 109 ms                                                       | 68.7 ms: 1.59x faster                                                       |
| crypto_pyaes             | 118 ms                                                       | 74.4 ms: 1.59x faster                                                       |
| sqlglot_parse            | 2.26 ms                                                      | 1.43 ms: 1.58x faster                                                       |
| generators               | 58.0 ms                                                      | 37.4 ms: 1.55x faster                                                       |
| nbody                    | 137 ms                                                       | 89.1 ms: 1.54x faster                                                       |
| async_tree_none          | 700 ms                                                       | 470 ms: 1.49x faster                                                        |
| bench_mp_pool            | 7.18 ms                                                      | 4.83 ms: 1.49x faster                                                       |
| go                       | 259 ms                                                       | 174 ms: 1.49x faster                                                        |
| async_tree_io            | 1.61 sec                                                     | 1.08 sec: 1.48x faster                                                      |
| sqlglot_transpile        | 2.71 ms                                                      | 1.83 ms: 1.48x faster                                                       |
| richards_super           | 90.8 ms                                                      | 62.0 ms: 1.47x faster                                                       |
| hexiom                   | 9.52 ms                                                      | 6.53 ms: 1.46x faster                                                       |
| async_tree_memoization   | 824 ms                                                       | 567 ms: 1.45x faster                                                        |
| spectral_norm            | 136 ms                                                       | 94.8 ms: 1.44x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                       |
| pickle_pure_python       | 457 us                                                       | 321 us: 1.42x faster                                                        |
| json_dumps               | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                       |
| float                    | 110 ms                                                       | 81.3 ms: 1.36x faster                                                       |
| unpickle_pure_python     | 321 us                                                       | 236 us: 1.36x faster                                                        |
| pyflate                  | 697 ms                                                       | 514 ms: 1.36x faster                                                        |
| richards                 | 74.1 ms                                                      | 55.5 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 717 ms: 1.33x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                                      |
| logging_simple           | 8.90 us                                                      | 6.83 us: 1.30x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 808 ms: 1.30x faster                                                        |
| deepcopy_memo            | 48.9 us                                                      | 37.7 us: 1.30x faster                                                       |
| regex_compile            | 194 ms                                                       | 151 ms: 1.29x faster                                                        |
| logging_format           | 9.57 us                                                      | 7.44 us: 1.29x faster                                                       |
| coroutines               | 30.4 ms                                                      | 23.7 ms: 1.28x faster                                                       |
| xml_etree_process        | 76.0 ms                                                      | 59.6 ms: 1.28x faster                                                       |
| tornado_http             | 152 ms                                                       | 120 ms: 1.26x faster                                                        |
| pycparser                | 1.66 sec                                                     | 1.32 sec: 1.26x faster                                                      |
| fannkuch                 | 496 ms                                                       | 394 ms: 1.26x faster                                                        |
| mypy2                    | 466 ms                                                       | 372 ms: 1.25x faster                                                        |
| tomli_loads              | 2.97 sec                                                     | 2.41 sec: 1.23x faster                                                      |
| unpack_sequence          | 59.5 ns                                                      | 48.4 ns: 1.23x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.23x faster                                                        |
| scimark_sor              | 177 ms                                                       | 144 ms: 1.23x faster                                                        |
| nqueens                  | 112 ms                                                       | 91.9 ms: 1.22x faster                                                       |
| comprehensions           | 26.9 us                                                      | 22.1 us: 1.22x faster                                                       |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.34 ms: 1.20x faster                                                       |
| sqlglot_optimize         | 70.3 ms                                                      | 58.8 ms: 1.19x faster                                                       |
| mdp                      | 3.03 sec                                                     | 2.55 sec: 1.19x faster                                                      |
| bench_thread_pool        | 1.14 ms                                                      | 961 us: 1.18x faster                                                        |
| deepcopy                 | 454 us                                                       | 384 us: 1.18x faster                                                        |
| dulwich_log              | 80.1 ms                                                      | 68.2 ms: 1.17x faster                                                       |
| deepcopy_reduce          | 4.03 us                                                      | 3.44 us: 1.17x faster                                                       |
| scimark_fft              | 359 ms                                                       | 308 ms: 1.17x faster                                                        |
| docutils                 | 3.40 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| json_loads               | 30.0 us                                                      | 25.7 us: 1.17x faster                                                       |
| json                     | 5.96 ms                                                      | 5.22 ms: 1.14x faster                                                       |
| pathlib                  | 21.7 ms                                                      | 19.5 ms: 1.11x faster                                                       |
| xml_etree_generate       | 94.6 ms                                                      | 84.9 ms: 1.11x faster                                                       |
| regex_v8                 | 26.6 ms                                                      | 24.0 ms: 1.11x faster                                                       |
| create_gc_cycles         | 1.82 ms                                                      | 1.64 ms: 1.11x faster                                                       |
| xml_etree_parse          | 162 ms                                                       | 147 ms: 1.10x faster                                                        |
| sqlite_synth             | 2.97 us                                                      | 2.76 us: 1.07x faster                                                       |
| async_generators         | 422 ms                                                       | 395 ms: 1.07x faster                                                        |
| meteor_contest           | 137 ms                                                       | 130 ms: 1.05x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.04x faster                                                        |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                                        |
| regex_dna                | 259 ms                                                       | 252 ms: 1.03x faster                                                        |
| python_startup           | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                                       |
| gc_traversal             | 3.45 ms                                                      | 3.52 ms: 1.02x slower                                                       |
| pickle                   | 9.94 us                                                      | 10.2 us: 1.02x slower                                                       |
| unpickle                 | 14.2 us                                                      | 15.1 us: 1.06x slower                                                       |
| unpickle_list            | 4.49 us                                                      | 4.79 us: 1.07x slower                                                       |
| pickle_dict              | 30.0 us                                                      | 32.7 us: 1.09x slower                                                       |
| pickle_list              | 4.11 us                                                      | 4.54 us: 1.10x slower                                                       |
| telco                    | 7.14 ms                                                      | 8.15 ms: 1.14x slower                                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.63 ms: 1.18x slower                                                       |
| regex_effbot             | 2.99 ms                                                      | 3.67 ms: 1.23x slower                                                       |
| dask                     | 463 ms                                                       | 589 ms: 1.27x slower                                                        |
| coverage                 | 64.0 ms                                                      | 89.4 ms: 1.40x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x
