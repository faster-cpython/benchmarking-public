
# Results vs. 3.10.4

- fork: faster-cpython
- ref: gc_scan_roots
- machine: linux-x86_64
- commit hash: 3994224
- commit date: 2023-08-04
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 3.00 sec: 1.14x faster                                                         |
| tornado_http   | 152 ms                                                       | 122 ms: 1.25x faster                                                           |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 87.7 ms: 1.56x faster                                                          |
| float          | 110 ms                                                       | 82.4 ms: 1.34x faster                                                          |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 148 ms: 1.31x faster                                                           |
| regex_v8       | 26.6 ms                                                      | 23.9 ms: 1.12x faster                                                          |
| regex_dna      | 259 ms                                                       | 248 ms: 1.05x faster                                                           |
| regex_effbot   | 2.99 ms                                                      | 3.74 ms: 1.25x slower                                                          |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 318 us: 1.44x faster                                                           |
| unpickle_pure_python | 321 us                                                       | 232 us: 1.39x faster                                                           |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                                          |
| tomli_loads          | 2.97 sec                                                     | 2.29 sec: 1.29x faster                                                         |
| xml_etree_process    | 76.0 ms                                                      | 58.9 ms: 1.29x faster                                                          |
| json_loads           | 30.0 us                                                      | 25.3 us: 1.19x faster                                                          |
| xml_etree_parse      | 162 ms                                                       | 143 ms: 1.13x faster                                                           |
| xml_etree_generate   | 94.6 ms                                                      | 85.6 ms: 1.10x faster                                                          |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                                           |
| pickle               | 9.94 us                                                      | 10.1 us: 1.02x slower                                                          |
| pickle_list          | 4.11 us                                                      | 4.36 us: 1.06x slower                                                          |
| unpickle             | 14.2 us                                                      | 15.1 us: 1.06x slower                                                          |
| pickle_dict          | 30.0 us                                                      | 31.9 us: 1.06x slower                                                          |
| unpickle_list        | 4.49 us                                                      | 4.83 us: 1.08x slower                                                          |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                                          |
| python_startup_no_site | 7.32 ms                                                      | 8.64 ms: 1.18x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-3994224 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 151 us: 3.45x faster                                                           |
| asyncio_tcp              | 782 ms                                                       | 368 ms: 2.13x faster                                                           |
| deltablue                | 7.47 ms                                                      | 3.71 ms: 2.01x faster                                                          |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.96x faster                                                         |
| raytrace                 | 488 ms                                                       | 279 ms: 1.75x faster                                                           |
| chaos                    | 107 ms                                                       | 62.2 ms: 1.72x faster                                                          |
| logging_silent           | 166 ns                                                       | 98.3 ns: 1.69x faster                                                          |
| scimark_lu               | 164 ms                                                       | 97.3 ms: 1.68x faster                                                          |
| crypto_pyaes             | 118 ms                                                       | 73.2 ms: 1.61x faster                                                          |
| sqlglot_parse            | 2.26 ms                                                      | 1.42 ms: 1.59x faster                                                          |
| generators               | 58.0 ms                                                      | 36.6 ms: 1.58x faster                                                          |
| scimark_monte_carlo      | 109 ms                                                       | 69.7 ms: 1.57x faster                                                          |
| nbody                    | 137 ms                                                       | 87.7 ms: 1.56x faster                                                          |
| bench_mp_pool            | 7.18 ms                                                      | 4.73 ms: 1.52x faster                                                          |
| go                       | 259 ms                                                       | 174 ms: 1.49x faster                                                           |
| hexiom                   | 9.52 ms                                                      | 6.46 ms: 1.47x faster                                                          |
| sqlglot_transpile        | 2.71 ms                                                      | 1.84 ms: 1.47x faster                                                          |
| richards_super           | 90.8 ms                                                      | 61.8 ms: 1.47x faster                                                          |
| pickle_pure_python       | 457 us                                                       | 318 us: 1.44x faster                                                           |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                          |
| async_tree_none          | 700 ms                                                       | 491 ms: 1.42x faster                                                           |
| async_tree_io            | 1.61 sec                                                     | 1.13 sec: 1.42x faster                                                         |
| spectral_norm            | 136 ms                                                       | 96.7 ms: 1.41x faster                                                          |
| async_tree_memoization   | 824 ms                                                       | 589 ms: 1.40x faster                                                           |
| unpickle_pure_python     | 321 us                                                       | 232 us: 1.39x faster                                                           |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                                          |
| richards                 | 74.1 ms                                                      | 54.8 ms: 1.35x faster                                                          |
| pyflate                  | 697 ms                                                       | 517 ms: 1.35x faster                                                           |
| float                    | 110 ms                                                       | 82.4 ms: 1.34x faster                                                          |
| deepcopy_memo            | 48.9 us                                                      | 37.2 us: 1.32x faster                                                          |
| regex_compile            | 194 ms                                                       | 148 ms: 1.31x faster                                                           |
| logging_simple           | 8.90 us                                                      | 6.82 us: 1.30x faster                                                          |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.30x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 809 ms: 1.30x faster                                                           |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 735 ms: 1.30x faster                                                           |
| tomli_loads              | 2.97 sec                                                     | 2.29 sec: 1.29x faster                                                         |
| coroutines               | 30.4 ms                                                      | 23.5 ms: 1.29x faster                                                          |
| xml_etree_process        | 76.0 ms                                                      | 58.9 ms: 1.29x faster                                                          |
| logging_format           | 9.57 us                                                      | 7.46 us: 1.28x faster                                                          |
| pycparser                | 1.66 sec                                                     | 1.32 sec: 1.26x faster                                                         |
| fannkuch                 | 496 ms                                                       | 395 ms: 1.26x faster                                                           |
| mypy2                    | 466 ms                                                       | 372 ms: 1.26x faster                                                           |
| nqueens                  | 112 ms                                                       | 90.3 ms: 1.25x faster                                                          |
| tornado_http             | 152 ms                                                       | 122 ms: 1.25x faster                                                           |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.21 ms: 1.23x faster                                                          |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.23x faster                                                           |
| comprehensions           | 26.9 us                                                      | 22.2 us: 1.21x faster                                                          |
| deepcopy                 | 454 us                                                       | 376 us: 1.21x faster                                                           |
| bench_thread_pool        | 1.14 ms                                                      | 946 us: 1.20x faster                                                           |
| unpack_sequence          | 59.5 ns                                                      | 49.6 ns: 1.20x faster                                                          |
| sqlglot_optimize         | 70.3 ms                                                      | 58.7 ms: 1.20x faster                                                          |
| mdp                      | 3.03 sec                                                     | 2.54 sec: 1.19x faster                                                         |
| scimark_sor              | 177 ms                                                       | 149 ms: 1.19x faster                                                           |
| json_loads               | 30.0 us                                                      | 25.3 us: 1.19x faster                                                          |
| scimark_fft              | 359 ms                                                       | 303 ms: 1.18x faster                                                           |
| deepcopy_reduce          | 4.03 us                                                      | 3.43 us: 1.17x faster                                                          |
| dulwich_log              | 80.1 ms                                                      | 69.5 ms: 1.15x faster                                                          |
| json                     | 5.96 ms                                                      | 5.25 ms: 1.14x faster                                                          |
| docutils                 | 3.40 sec                                                     | 3.00 sec: 1.14x faster                                                         |
| xml_etree_parse          | 162 ms                                                       | 143 ms: 1.13x faster                                                           |
| pathlib                  | 21.7 ms                                                      | 19.3 ms: 1.12x faster                                                          |
| regex_v8                 | 26.6 ms                                                      | 23.9 ms: 1.12x faster                                                          |
| xml_etree_generate       | 94.6 ms                                                      | 85.6 ms: 1.10x faster                                                          |
| sqlite_synth             | 2.97 us                                                      | 2.72 us: 1.09x faster                                                          |
| create_gc_cycles         | 1.82 ms                                                      | 1.72 ms: 1.06x faster                                                          |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                                           |
| meteor_contest           | 137 ms                                                       | 131 ms: 1.05x faster                                                           |
| regex_dna                | 259 ms                                                       | 248 ms: 1.05x faster                                                           |
| async_generators         | 422 ms                                                       | 404 ms: 1.04x faster                                                           |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                                           |
| python_startup           | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                                          |
| pickle                   | 9.94 us                                                      | 10.1 us: 1.02x slower                                                          |
| pickle_list              | 4.11 us                                                      | 4.36 us: 1.06x slower                                                          |
| unpickle                 | 14.2 us                                                      | 15.1 us: 1.06x slower                                                          |
| pickle_dict              | 30.0 us                                                      | 31.9 us: 1.06x slower                                                          |
| unpickle_list            | 4.49 us                                                      | 4.83 us: 1.08x slower                                                          |
| gc_traversal             | 3.45 ms                                                      | 3.82 ms: 1.11x slower                                                          |
| telco                    | 7.14 ms                                                      | 8.06 ms: 1.13x slower                                                          |
| python_startup_no_site   | 7.32 ms                                                      | 8.64 ms: 1.18x slower                                                          |
| regex_effbot             | 2.99 ms                                                      | 3.74 ms: 1.25x slower                                                          |
| dask                     | 463 ms                                                       | 588 ms: 1.27x slower                                                           |
| coverage                 | 64.0 ms                                                      | 89.8 ms: 1.40x slower                                                          |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                   |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
