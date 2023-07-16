
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 30c127f
- commit date: 2023-07-15
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4+-30c127f |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                         |
| docutils       | 3.40 sec                                                     | 2.91 sec: 1.17x faster                                       |
| tornado_http   | 152 ms                                                       | 122 ms: 1.25x faster                                         |
| Geometric mean | (ref)                                                        | 1.21x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4+-30c127f |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 90.0 ms: 1.53x faster                                        |
| float          | 110 ms                                                       | 78.6 ms: 1.40x faster                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4+-30c127f |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 145 ms: 1.34x faster                                         |
| regex_v8       | 26.6 ms                                                      | 24.0 ms: 1.11x faster                                        |
| regex_dna      | 259 ms                                                       | 240 ms: 1.08x faster                                         |
| regex_effbot   | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4+-30c127f |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 210 us: 1.52x faster                                         |
| pickle_pure_python   | 457 us                                                       | 323 us: 1.42x faster                                         |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.39x faster                                        |
| tomli_loads          | 2.97 sec                                                     | 2.19 sec: 1.36x faster                                       |
| xml_etree_process    | 76.0 ms                                                      | 59.1 ms: 1.29x faster                                        |
| json_loads           | 30.0 us                                                      | 24.9 us: 1.20x faster                                        |
| xml_etree_generate   | 94.6 ms                                                      | 85.7 ms: 1.10x faster                                        |
| xml_etree_parse      | 162 ms                                                       | 149 ms: 1.08x faster                                         |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                         |
| pickle               | 9.94 us                                                      | 10.2 us: 1.03x slower                                        |
| unpickle             | 14.2 us                                                      | 14.6 us: 1.03x slower                                        |
| pickle_list          | 4.11 us                                                      | 4.41 us: 1.07x slower                                        |
| unpickle_list        | 4.49 us                                                      | 4.95 us: 1.10x slower                                        |
| pickle_dict          | 30.0 us                                                      | 33.5 us: 1.12x slower                                        |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4+-30c127f |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.5 ms: 1.00x slower                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.52 ms: 1.16x slower                                        |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4+-30c127f |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.0 ms: 1.46x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4+-30c127f |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 153 us: 3.42x faster                                         |
| deltablue                | 7.47 ms                                                      | 3.24 ms: 2.31x faster                                        |
| asyncio_tcp              | 782 ms                                                       | 378 ms: 2.07x faster                                         |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                       |
| richards_super           | 90.8 ms                                                      | 51.5 ms: 1.77x faster                                        |
| go                       | 259 ms                                                       | 148 ms: 1.75x faster                                         |
| logging_silent           | 166 ns                                                       | 97.7 ns: 1.70x faster                                        |
| chaos                    | 107 ms                                                       | 63.2 ms: 1.70x faster                                        |
| richards                 | 74.1 ms                                                      | 44.4 ms: 1.67x faster                                        |
| scimark_lu               | 164 ms                                                       | 99.4 ms: 1.65x faster                                        |
| hexiom                   | 9.52 ms                                                      | 5.87 ms: 1.62x faster                                        |
| sqlglot_parse            | 2.26 ms                                                      | 1.39 ms: 1.62x faster                                        |
| scimark_sor              | 177 ms                                                       | 109 ms: 1.62x faster                                         |
| scimark_monte_carlo      | 109 ms                                                       | 67.9 ms: 1.61x faster                                        |
| generators               | 58.0 ms                                                      | 36.1 ms: 1.61x faster                                        |
| pyflate                  | 697 ms                                                       | 442 ms: 1.58x faster                                         |
| raytrace                 | 488 ms                                                       | 311 ms: 1.57x faster                                         |
| nbody                    | 137 ms                                                       | 90.0 ms: 1.53x faster                                        |
| unpickle_pure_python     | 321 us                                                       | 210 us: 1.52x faster                                         |
| async_tree_io            | 1.61 sec                                                     | 1.06 sec: 1.51x faster                                       |
| async_tree_none          | 700 ms                                                       | 464 ms: 1.51x faster                                         |
| sqlglot_transpile        | 2.71 ms                                                      | 1.80 ms: 1.51x faster                                        |
| async_tree_memoization   | 824 ms                                                       | 555 ms: 1.48x faster                                         |
| bench_mp_pool            | 7.18 ms                                                      | 4.87 ms: 1.47x faster                                        |
| spectral_norm            | 136 ms                                                       | 92.7 ms: 1.47x faster                                        |
| mako                     | 14.7 ms                                                      | 10.0 ms: 1.46x faster                                        |
| crypto_pyaes             | 118 ms                                                       | 82.1 ms: 1.44x faster                                        |
| fannkuch                 | 496 ms                                                       | 345 ms: 1.44x faster                                         |
| pickle_pure_python       | 457 us                                                       | 323 us: 1.42x faster                                         |
| float                    | 110 ms                                                       | 78.6 ms: 1.40x faster                                        |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.39x faster                                        |
| tomli_loads              | 2.97 sec                                                     | 2.19 sec: 1.36x faster                                       |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 707 ms: 1.35x faster                                         |
| regex_compile            | 194 ms                                                       | 145 ms: 1.34x faster                                         |
| coroutines               | 30.4 ms                                                      | 22.7 ms: 1.34x faster                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 801 ms: 1.31x faster                                         |
| deepcopy_memo            | 48.9 us                                                      | 37.6 us: 1.30x faster                                        |
| logging_simple           | 8.90 us                                                      | 6.85 us: 1.30x faster                                        |
| pycparser                | 1.66 sec                                                     | 1.28 sec: 1.29x faster                                       |
| xml_etree_process        | 76.0 ms                                                      | 59.1 ms: 1.29x faster                                        |
| logging_format           | 9.57 us                                                      | 7.44 us: 1.29x faster                                        |
| mypy2                    | 466 ms                                                       | 368 ms: 1.27x faster                                         |
| sqlglot_normalize        | 144 ms                                                       | 115 ms: 1.26x faster                                         |
| tornado_http             | 152 ms                                                       | 122 ms: 1.25x faster                                         |
| nqueens                  | 112 ms                                                       | 90.3 ms: 1.25x faster                                        |
| comprehensions           | 26.9 us                                                      | 21.9 us: 1.23x faster                                        |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                         |
| sqlglot_optimize         | 70.3 ms                                                      | 57.5 ms: 1.22x faster                                        |
| deepcopy                 | 454 us                                                       | 374 us: 1.21x faster                                         |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.28 ms: 1.21x faster                                        |
| unpack_sequence          | 59.5 ns                                                      | 49.0 ns: 1.21x faster                                        |
| dulwich_log              | 80.1 ms                                                      | 66.4 ms: 1.21x faster                                        |
| json_loads               | 30.0 us                                                      | 24.9 us: 1.20x faster                                        |
| deepcopy_reduce          | 4.03 us                                                      | 3.39 us: 1.19x faster                                        |
| scimark_fft              | 359 ms                                                       | 302 ms: 1.19x faster                                         |
| bench_thread_pool        | 1.14 ms                                                      | 961 us: 1.18x faster                                         |
| mdp                      | 3.03 sec                                                     | 2.57 sec: 1.18x faster                                       |
| docutils                 | 3.40 sec                                                     | 2.91 sec: 1.17x faster                                       |
| json                     | 5.96 ms                                                      | 5.18 ms: 1.15x faster                                        |
| pathlib                  | 21.7 ms                                                      | 19.2 ms: 1.13x faster                                        |
| regex_v8                 | 26.6 ms                                                      | 24.0 ms: 1.11x faster                                        |
| xml_etree_generate       | 94.6 ms                                                      | 85.7 ms: 1.10x faster                                        |
| sqlite_synth             | 2.97 us                                                      | 2.71 us: 1.10x faster                                        |
| create_gc_cycles         | 1.82 ms                                                      | 1.67 ms: 1.09x faster                                        |
| async_generators         | 422 ms                                                       | 388 ms: 1.09x faster                                         |
| xml_etree_parse          | 162 ms                                                       | 149 ms: 1.08x faster                                         |
| regex_dna                | 259 ms                                                       | 240 ms: 1.08x faster                                         |
| meteor_contest           | 137 ms                                                       | 128 ms: 1.07x faster                                         |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                         |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| telco                    | 7.14 ms                                                      | 7.01 ms: 1.02x faster                                        |
| python_startup           | 11.5 ms                                                      | 11.5 ms: 1.00x slower                                        |
| pickle                   | 9.94 us                                                      | 10.2 us: 1.03x slower                                        |
| unpickle                 | 14.2 us                                                      | 14.6 us: 1.03x slower                                        |
| pickle_list              | 4.11 us                                                      | 4.41 us: 1.07x slower                                        |
| unpickle_list            | 4.49 us                                                      | 4.95 us: 1.10x slower                                        |
| pickle_dict              | 30.0 us                                                      | 33.5 us: 1.12x slower                                        |
| python_startup_no_site   | 7.32 ms                                                      | 8.52 ms: 1.16x slower                                        |
| regex_effbot             | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                        |
| gc_traversal             | 3.45 ms                                                      | 4.20 ms: 1.22x slower                                        |
| dask                     | 463 ms                                                       | 564 ms: 1.22x slower                                         |
| coverage                 | 64.0 ms                                                      | 90.1 ms: 1.41x slower                                        |
| Geometric mean           | (ref)                                                        | 1.29x faster                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
