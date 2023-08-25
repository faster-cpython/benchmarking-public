
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 9cd3664
- commit date: 2023-06-24
- overall geometric mean: 1.31x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                         |
| docutils       | 3.40 sec                                                     | 2.88 sec: 1.18x faster                                       |
| tornado_http   | 152 ms                                                       | 120 ms: 1.27x faster                                         |
| Geometric mean | (ref)                                                        | 1.23x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 85.0 ms: 1.62x faster                                        |
| float          | 110 ms                                                       | 77.0 ms: 1.43x faster                                        |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.34x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 143 ms: 1.35x faster                                         |
| regex_v8       | 26.6 ms                                                      | 23.8 ms: 1.12x faster                                        |
| regex_dna      | 259 ms                                                       | 247 ms: 1.05x faster                                         |
| regex_effbot   | 2.99 ms                                                      | 3.57 ms: 1.19x slower                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 208 us: 1.54x faster                                         |
| pickle_pure_python   | 457 us                                                       | 318 us: 1.44x faster                                         |
| json_dumps           | 14.2 ms                                                      | 10.1 ms: 1.41x faster                                        |
| tomli_loads          | 2.97 sec                                                     | 2.19 sec: 1.35x faster                                       |
| xml_etree_process    | 76.0 ms                                                      | 58.3 ms: 1.30x faster                                        |
| json_loads           | 30.0 us                                                      | 25.0 us: 1.20x faster                                        |
| xml_etree_generate   | 94.6 ms                                                      | 85.1 ms: 1.11x faster                                        |
| xml_etree_parse      | 162 ms                                                       | 147 ms: 1.10x faster                                         |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                         |
| unpickle             | 14.2 us                                                      | 14.5 us: 1.02x slower                                        |
| pickle               | 9.94 us                                                      | 10.3 us: 1.03x slower                                        |
| unpickle_list        | 4.49 us                                                      | 4.77 us: 1.06x slower                                        |
| pickle_list          | 4.11 us                                                      | 4.36 us: 1.06x slower                                        |
| pickle_dict          | 30.0 us                                                      | 32.0 us: 1.07x slower                                        |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.44 ms: 1.15x slower                                        |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 9.91 ms: 1.48x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 149 us: 3.51x faster                                         |
| deltablue                | 7.47 ms                                                      | 3.22 ms: 2.32x faster                                        |
| asyncio_tcp              | 782 ms                                                       | 376 ms: 2.08x faster                                         |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.56 sec: 1.98x faster                                       |
| richards_super           | 90.8 ms                                                      | 49.9 ms: 1.82x faster                                        |
| logging_silent           | 166 ns                                                       | 91.6 ns: 1.81x faster                                        |
| go                       | 259 ms                                                       | 144 ms: 1.80x faster                                         |
| chaos                    | 107 ms                                                       | 62.3 ms: 1.72x faster                                        |
| scimark_lu               | 164 ms                                                       | 97.2 ms: 1.68x faster                                        |
| richards                 | 74.1 ms                                                      | 44.0 ms: 1.68x faster                                        |
| scimark_monte_carlo      | 109 ms                                                       | 66.3 ms: 1.65x faster                                        |
| raytrace                 | 488 ms                                                       | 297 ms: 1.65x faster                                         |
| sqlglot_parse            | 2.26 ms                                                      | 1.37 ms: 1.64x faster                                        |
| hexiom                   | 9.52 ms                                                      | 5.81 ms: 1.64x faster                                        |
| scimark_sor              | 177 ms                                                       | 110 ms: 1.62x faster                                         |
| nbody                    | 137 ms                                                       | 85.0 ms: 1.62x faster                                        |
| pyflate                  | 697 ms                                                       | 435 ms: 1.60x faster                                         |
| generators               | 58.0 ms                                                      | 36.6 ms: 1.59x faster                                        |
| unpickle_pure_python     | 321 us                                                       | 208 us: 1.54x faster                                         |
| spectral_norm            | 136 ms                                                       | 88.5 ms: 1.54x faster                                        |
| async_tree_none          | 700 ms                                                       | 456 ms: 1.53x faster                                         |
| sqlglot_transpile        | 2.71 ms                                                      | 1.77 ms: 1.53x faster                                        |
| async_tree_io            | 1.61 sec                                                     | 1.06 sec: 1.52x faster                                       |
| async_tree_memoization   | 824 ms                                                       | 549 ms: 1.50x faster                                         |
| mako                     | 14.7 ms                                                      | 9.91 ms: 1.48x faster                                        |
| fannkuch                 | 496 ms                                                       | 340 ms: 1.46x faster                                         |
| pickle_pure_python       | 457 us                                                       | 318 us: 1.44x faster                                         |
| float                    | 110 ms                                                       | 77.0 ms: 1.43x faster                                        |
| crypto_pyaes             | 118 ms                                                       | 82.7 ms: 1.43x faster                                        |
| json_dumps               | 14.2 ms                                                      | 10.1 ms: 1.41x faster                                        |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 700 ms: 1.36x faster                                         |
| tomli_loads              | 2.97 sec                                                     | 2.19 sec: 1.35x faster                                       |
| regex_compile            | 194 ms                                                       | 143 ms: 1.35x faster                                         |
| coroutines               | 30.4 ms                                                      | 22.6 ms: 1.35x faster                                        |
| logging_simple           | 8.90 us                                                      | 6.65 us: 1.34x faster                                        |
| deepcopy_memo            | 48.9 us                                                      | 36.6 us: 1.34x faster                                        |
| pycparser                | 1.66 sec                                                     | 1.25 sec: 1.33x faster                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.32x faster                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 803 ms: 1.31x faster                                         |
| xml_etree_process        | 76.0 ms                                                      | 58.3 ms: 1.30x faster                                        |
| logging_format           | 9.57 us                                                      | 7.34 us: 1.30x faster                                        |
| bench_mp_pool            | 7.18 ms                                                      | 5.53 ms: 1.30x faster                                        |
| mypy2                    | 466 ms                                                       | 363 ms: 1.29x faster                                         |
| tornado_http             | 152 ms                                                       | 120 ms: 1.27x faster                                         |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                         |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.24x faster                                         |
| comprehensions           | 26.9 us                                                      | 21.9 us: 1.23x faster                                        |
| dulwich_log              | 80.1 ms                                                      | 65.1 ms: 1.23x faster                                        |
| nqueens                  | 112 ms                                                       | 91.8 ms: 1.23x faster                                        |
| sqlglot_optimize         | 70.3 ms                                                      | 57.7 ms: 1.22x faster                                        |
| deepcopy                 | 454 us                                                       | 372 us: 1.22x faster                                         |
| mdp                      | 3.03 sec                                                     | 2.50 sec: 1.21x faster                                       |
| json_loads               | 30.0 us                                                      | 25.0 us: 1.20x faster                                        |
| deepcopy_reduce          | 4.03 us                                                      | 3.37 us: 1.19x faster                                        |
| bench_thread_pool        | 1.14 ms                                                      | 953 us: 1.19x faster                                         |
| unpack_sequence          | 59.5 ns                                                      | 50.3 ns: 1.18x faster                                        |
| docutils                 | 3.40 sec                                                     | 2.88 sec: 1.18x faster                                       |
| scimark_fft              | 359 ms                                                       | 305 ms: 1.18x faster                                         |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.41 ms: 1.18x faster                                        |
| json                     | 5.96 ms                                                      | 5.19 ms: 1.15x faster                                        |
| pathlib                  | 21.7 ms                                                      | 18.9 ms: 1.15x faster                                        |
| regex_v8                 | 26.6 ms                                                      | 23.8 ms: 1.12x faster                                        |
| create_gc_cycles         | 1.82 ms                                                      | 1.64 ms: 1.11x faster                                        |
| xml_etree_generate       | 94.6 ms                                                      | 85.1 ms: 1.11x faster                                        |
| xml_etree_parse          | 162 ms                                                       | 147 ms: 1.10x faster                                         |
| sqlite_synth             | 2.97 us                                                      | 2.74 us: 1.08x faster                                        |
| async_generators         | 422 ms                                                       | 391 ms: 1.08x faster                                         |
| meteor_contest           | 137 ms                                                       | 128 ms: 1.07x faster                                         |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.06x faster                                         |
| regex_dna                | 259 ms                                                       | 247 ms: 1.05x faster                                         |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                         |
| telco                    | 7.14 ms                                                      | 7.01 ms: 1.02x faster                                        |
| python_startup           | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                        |
| unpickle                 | 14.2 us                                                      | 14.5 us: 1.02x slower                                        |
| pickle                   | 9.94 us                                                      | 10.3 us: 1.03x slower                                        |
| unpickle_list            | 4.49 us                                                      | 4.77 us: 1.06x slower                                        |
| pickle_list              | 4.11 us                                                      | 4.36 us: 1.06x slower                                        |
| pickle_dict              | 30.0 us                                                      | 32.0 us: 1.07x slower                                        |
| gc_traversal             | 3.45 ms                                                      | 3.79 ms: 1.10x slower                                        |
| python_startup_no_site   | 7.32 ms                                                      | 8.44 ms: 1.15x slower                                        |
| regex_effbot             | 2.99 ms                                                      | 3.57 ms: 1.19x slower                                        |
| dask                     | 463 ms                                                       | 558 ms: 1.21x slower                                         |
| coverage                 | 64.0 ms                                                      | 88.2 ms: 1.38x slower                                        |
| Geometric mean           | (ref)                                                        | 1.31x faster                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x
