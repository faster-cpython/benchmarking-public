
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 8c17729
- commit date: 2023-07-16
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf2-x86_64-python-main-3.13.0a0-8c17729 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.93 sec: 1.16x faster                                      |
| tornado_http   | 152 ms                                                       | 123 ms: 1.24x faster                                        |
| Geometric mean | (ref)                                                        | 1.20x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf2-x86_64-python-main-3.13.0a0-8c17729 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 137 ms                                                       | 89.4 ms: 1.54x faster                                       |
| float          | 110 ms                                                       | 82.1 ms: 1.34x faster                                       |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                        | 1.29x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf2-x86_64-python-main-3.13.0a0-8c17729 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 152 ms: 1.27x faster                                        |
| regex_v8       | 26.6 ms                                                      | 23.8 ms: 1.12x faster                                       |
| regex_dna      | 259 ms                                                       | 240 ms: 1.08x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.68 ms: 1.23x slower                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf2-x86_64-python-main-3.13.0a0-8c17729 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 220 us: 1.46x faster                                        |
| pickle_pure_python   | 457 us                                                       | 326 us: 1.40x faster                                        |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                       |
| xml_etree_process    | 76.0 ms                                                      | 59.7 ms: 1.27x faster                                       |
| tomli_loads          | 2.97 sec                                                     | 2.35 sec: 1.26x faster                                      |
| json_loads           | 30.0 us                                                      | 24.9 us: 1.20x faster                                       |
| xml_etree_generate   | 94.6 ms                                                      | 86.1 ms: 1.10x faster                                       |
| xml_etree_parse      | 162 ms                                                       | 150 ms: 1.08x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 107 ms: 1.03x faster                                        |
| unpickle             | 14.2 us                                                      | 14.4 us: 1.01x slower                                       |
| pickle               | 9.94 us                                                      | 10.2 us: 1.03x slower                                       |
| pickle_list          | 4.11 us                                                      | 4.30 us: 1.05x slower                                       |
| unpickle_list        | 4.49 us                                                      | 4.75 us: 1.06x slower                                       |
| pickle_dict          | 30.0 us                                                      | 32.8 us: 1.09x slower                                       |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf2-x86_64-python-main-3.13.0a0-8c17729 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.42 ms: 1.15x slower                                       |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf2-x86_64-python-main-3.13.0a0-8c17729 |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-pythonperf2-x86_64-python-main-3.13.0a0-8c17729 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 152 us: 3.45x faster                                        |
| asyncio_tcp              | 782 ms                                                       | 383 ms: 2.04x faster                                        |
| deltablue                | 7.47 ms                                                      | 3.73 ms: 2.00x faster                                       |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.96x faster                                      |
| chaos                    | 107 ms                                                       | 61.8 ms: 1.73x faster                                       |
| logging_silent           | 166 ns                                                       | 96.8 ns: 1.71x faster                                       |
| raytrace                 | 488 ms                                                       | 299 ms: 1.63x faster                                        |
| scimark_lu               | 164 ms                                                       | 101 ms: 1.62x faster                                        |
| scimark_monte_carlo      | 109 ms                                                       | 68.7 ms: 1.59x faster                                       |
| crypto_pyaes             | 118 ms                                                       | 75.2 ms: 1.57x faster                                       |
| generators               | 58.0 ms                                                      | 37.0 ms: 1.57x faster                                       |
| sqlglot_parse            | 2.26 ms                                                      | 1.45 ms: 1.56x faster                                       |
| nbody                    | 137 ms                                                       | 89.4 ms: 1.54x faster                                       |
| go                       | 259 ms                                                       | 174 ms: 1.49x faster                                        |
| async_tree_none          | 700 ms                                                       | 470 ms: 1.49x faster                                        |
| async_tree_io            | 1.61 sec                                                     | 1.08 sec: 1.48x faster                                      |
| richards_super           | 90.8 ms                                                      | 61.3 ms: 1.48x faster                                       |
| bench_mp_pool            | 7.18 ms                                                      | 4.87 ms: 1.48x faster                                       |
| sqlglot_transpile        | 2.71 ms                                                      | 1.85 ms: 1.47x faster                                       |
| unpickle_pure_python     | 321 us                                                       | 220 us: 1.46x faster                                        |
| async_tree_memoization   | 824 ms                                                       | 567 ms: 1.45x faster                                        |
| hexiom                   | 9.52 ms                                                      | 6.58 ms: 1.45x faster                                       |
| spectral_norm            | 136 ms                                                       | 94.6 ms: 1.44x faster                                       |
| mako                     | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                       |
| pickle_pure_python       | 457 us                                                       | 326 us: 1.40x faster                                        |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                       |
| pyflate                  | 697 ms                                                       | 514 ms: 1.36x faster                                        |
| richards                 | 74.1 ms                                                      | 55.0 ms: 1.35x faster                                       |
| float                    | 110 ms                                                       | 82.1 ms: 1.34x faster                                       |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 717 ms: 1.33x faster                                        |
| coroutines               | 30.4 ms                                                      | 23.3 ms: 1.30x faster                                       |
| xml_etree_process        | 76.0 ms                                                      | 59.7 ms: 1.27x faster                                       |
| regex_compile            | 194 ms                                                       | 152 ms: 1.27x faster                                        |
| tomli_loads              | 2.97 sec                                                     | 2.35 sec: 1.26x faster                                      |
| fannkuch                 | 496 ms                                                       | 393 ms: 1.26x faster                                        |
| pycparser                | 1.66 sec                                                     | 1.32 sec: 1.26x faster                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.72 sec: 1.25x faster                                      |
| mypy2                    | 466 ms                                                       | 372 ms: 1.25x faster                                        |
| deepcopy_memo            | 48.9 us                                                      | 39.1 us: 1.25x faster                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 843 ms: 1.24x faster                                        |
| tornado_http             | 152 ms                                                       | 123 ms: 1.24x faster                                        |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.19 ms: 1.24x faster                                       |
| nqueens                  | 112 ms                                                       | 91.8 ms: 1.23x faster                                       |
| logging_simple           | 8.90 us                                                      | 7.28 us: 1.22x faster                                       |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.22x faster                                        |
| comprehensions           | 26.9 us                                                      | 22.1 us: 1.22x faster                                       |
| scimark_sor              | 177 ms                                                       | 146 ms: 1.21x faster                                        |
| json_loads               | 30.0 us                                                      | 24.9 us: 1.20x faster                                       |
| logging_format           | 9.57 us                                                      | 7.97 us: 1.20x faster                                       |
| bench_thread_pool        | 1.14 ms                                                      | 959 us: 1.19x faster                                        |
| sqlglot_optimize         | 70.3 ms                                                      | 59.4 ms: 1.18x faster                                       |
| dulwich_log              | 80.1 ms                                                      | 68.2 ms: 1.17x faster                                       |
| mdp                      | 3.03 sec                                                     | 2.61 sec: 1.16x faster                                      |
| json                     | 5.96 ms                                                      | 5.13 ms: 1.16x faster                                       |
| deepcopy                 | 454 us                                                       | 391 us: 1.16x faster                                        |
| docutils                 | 3.40 sec                                                     | 2.93 sec: 1.16x faster                                      |
| scimark_fft              | 359 ms                                                       | 310 ms: 1.16x faster                                        |
| deepcopy_reduce          | 4.03 us                                                      | 3.57 us: 1.13x faster                                       |
| create_gc_cycles         | 1.82 ms                                                      | 1.62 ms: 1.12x faster                                       |
| regex_v8                 | 26.6 ms                                                      | 23.8 ms: 1.12x faster                                       |
| pathlib                  | 21.7 ms                                                      | 19.7 ms: 1.10x faster                                       |
| xml_etree_generate       | 94.6 ms                                                      | 86.1 ms: 1.10x faster                                       |
| unpack_sequence          | 59.5 ns                                                      | 54.3 ns: 1.10x faster                                       |
| sqlite_synth             | 2.97 us                                                      | 2.73 us: 1.09x faster                                       |
| regex_dna                | 259 ms                                                       | 240 ms: 1.08x faster                                        |
| xml_etree_parse          | 162 ms                                                       | 150 ms: 1.08x faster                                        |
| meteor_contest           | 137 ms                                                       | 129 ms: 1.06x faster                                        |
| async_generators         | 422 ms                                                       | 397 ms: 1.06x faster                                        |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                        |
| xml_etree_iterparse      | 110 ms                                                       | 107 ms: 1.03x faster                                        |
| python_startup           | 11.5 ms                                                      | 11.4 ms: 1.01x faster                                       |
| unpickle                 | 14.2 us                                                      | 14.4 us: 1.01x slower                                       |
| pickle                   | 9.94 us                                                      | 10.2 us: 1.03x slower                                       |
| pickle_list              | 4.11 us                                                      | 4.30 us: 1.05x slower                                       |
| unpickle_list            | 4.49 us                                                      | 4.75 us: 1.06x slower                                       |
| gc_traversal             | 3.45 ms                                                      | 3.67 ms: 1.06x slower                                       |
| telco                    | 7.14 ms                                                      | 7.77 ms: 1.09x slower                                       |
| pickle_dict              | 30.0 us                                                      | 32.8 us: 1.09x slower                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.42 ms: 1.15x slower                                       |
| regex_effbot             | 2.99 ms                                                      | 3.68 ms: 1.23x slower                                       |
| dask                     | 463 ms                                                       | 592 ms: 1.28x slower                                        |
| coverage                 | 64.0 ms                                                      | 89.1 ms: 1.39x slower                                       |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x
