
# Results vs. 3.10.4

- fork: faster-cpython
- ref: always_allocate_valu
- machine: linux-x86_64
- commit hash: 17ae178
- commit date: 2023-08-10
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-always_allocate_valu-3.13.0a0-17ae178 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.63 sec: 1.20x faster                                                          |
| tornado_http   | 127 ms                                                 | 95.3 ms: 1.34x faster                                                           |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-always_allocate_valu-3.13.0a0-17ae178 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.4 ms: 1.58x faster                                                           |
| float          | 111 ms                                                 | 79.3 ms: 1.39x faster                                                           |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-always_allocate_valu-3.13.0a0-17ae178 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                                            |
| regex_v8       | 25.0 ms                                                | 23.1 ms: 1.08x faster                                                           |
| regex_dna      | 222 ms                                                 | 214 ms: 1.04x faster                                                            |
| regex_effbot   | 3.23 ms                                                | 3.66 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-always_allocate_valu-3.13.0a0-17ae178 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 298 us: 1.53x faster                                                            |
| unpickle_pure_python | 300 us                                                 | 213 us: 1.41x faster                                                            |
| tomli_loads          | 2.92 sec                                               | 2.09 sec: 1.39x faster                                                          |
| json_dumps           | 13.5 ms                                                | 9.79 ms: 1.38x faster                                                           |
| xml_etree_process    | 74.9 ms                                                | 56.7 ms: 1.32x faster                                                           |
| xml_etree_generate   | 94.2 ms                                                | 82.6 ms: 1.14x faster                                                           |
| json_loads           | 28.8 us                                                | 25.7 us: 1.12x faster                                                           |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                            |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                           |
| pickle_list          | 4.56 us                                                | 4.64 us: 1.02x slower                                                           |
| unpickle_list        | 4.82 us                                                | 4.91 us: 1.02x slower                                                           |
| unpickle             | 14.1 us                                                | 14.8 us: 1.05x slower                                                           |
| pickle_dict          | 27.3 us                                                | 30.3 us: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-always_allocate_valu-3.13.0a0-17ae178 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.41 ms: 1.50x faster                                                           |
| python_startup_no_site | 5.82 ms                                                | 6.88 ms: 1.18x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-always_allocate_valu-3.13.0a0-17ae178 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.39x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-always_allocate_valu-3.13.0a0-17ae178 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 148 us: 3.45x faster                                                            |
| generators               | 76.8 ms                                                | 28.4 ms: 2.71x faster                                                           |
| deltablue                | 7.42 ms                                                | 3.32 ms: 2.24x faster                                                           |
| asyncio_tcp              | 925 ms                                                 | 482 ms: 1.92x faster                                                            |
| chaos                    | 106 ms                                                 | 59.7 ms: 1.78x faster                                                           |
| crypto_pyaes             | 118 ms                                                 | 69.3 ms: 1.71x faster                                                           |
| raytrace                 | 464 ms                                                 | 274 ms: 1.70x faster                                                            |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                          |
| logging_silent           | 175 ns                                                 | 105 ns: 1.67x faster                                                            |
| richards_super           | 90.7 ms                                                | 54.5 ms: 1.66x faster                                                           |
| async_tree_none          | 717 ms                                                 | 438 ms: 1.64x faster                                                            |
| go                       | 229 ms                                                 | 141 ms: 1.63x faster                                                            |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.62x faster                                                            |
| sqlglot_parse            | 2.06 ms                                                | 1.28 ms: 1.61x faster                                                           |
| scimark_monte_carlo      | 108 ms                                                 | 68.3 ms: 1.58x faster                                                           |
| nbody                    | 142 ms                                                 | 89.4 ms: 1.58x faster                                                           |
| hexiom                   | 9.53 ms                                                | 6.04 ms: 1.58x faster                                                           |
| richards                 | 74.9 ms                                                | 48.1 ms: 1.56x faster                                                           |
| sqlglot_transpile        | 2.45 ms                                                | 1.59 ms: 1.53x faster                                                           |
| pickle_pure_python       | 455 us                                                 | 298 us: 1.53x faster                                                            |
| async_tree_memoization   | 854 ms                                                 | 567 ms: 1.51x faster                                                            |
| python_startup           | 14.2 ms                                                | 9.41 ms: 1.50x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                                          |
| unpack_sequence          | 64.7 ns                                                | 43.4 ns: 1.49x faster                                                           |
| pyflate                  | 673 ms                                                 | 452 ms: 1.49x faster                                                            |
| scimark_lu               | 163 ms                                                 | 112 ms: 1.46x faster                                                            |
| deepcopy_memo            | 52.3 us                                                | 37.0 us: 1.41x faster                                                           |
| unpickle_pure_python     | 300 us                                                 | 213 us: 1.41x faster                                                            |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.41x faster                                                            |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.39x faster                                                           |
| float                    | 111 ms                                                 | 79.3 ms: 1.39x faster                                                           |
| tomli_loads              | 2.92 sec                                               | 2.09 sec: 1.39x faster                                                          |
| logging_simple           | 8.07 us                                                | 5.82 us: 1.39x faster                                                           |
| json_dumps               | 13.5 ms                                                | 9.79 ms: 1.38x faster                                                           |
| logging_format           | 8.91 us                                                | 6.49 us: 1.37x faster                                                           |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 701 ms: 1.36x faster                                                            |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                                          |
| tornado_http             | 127 ms                                                 | 95.3 ms: 1.34x faster                                                           |
| coroutines               | 31.8 ms                                                | 23.8 ms: 1.34x faster                                                           |
| pprint_safe_repr         | 955 ms                                                 | 717 ms: 1.33x faster                                                            |
| xml_etree_process        | 74.9 ms                                                | 56.7 ms: 1.32x faster                                                           |
| sqlglot_normalize        | 135 ms                                                 | 104 ms: 1.30x faster                                                            |
| comprehensions           | 26.8 us                                                | 20.7 us: 1.30x faster                                                           |
| pycparser                | 1.50 sec                                               | 1.16 sec: 1.29x faster                                                          |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                                            |
| nqueens                  | 100 ms                                                 | 79.6 ms: 1.26x faster                                                           |
| deepcopy                 | 442 us                                                 | 353 us: 1.25x faster                                                            |
| sqlglot_optimize         | 65.3 ms                                                | 52.7 ms: 1.24x faster                                                           |
| fannkuch                 | 486 ms                                                 | 392 ms: 1.24x faster                                                            |
| deepcopy_reduce          | 3.82 us                                                | 3.17 us: 1.21x faster                                                           |
| docutils                 | 3.17 sec                                               | 2.63 sec: 1.20x faster                                                          |
| scimark_fft              | 424 ms                                                 | 355 ms: 1.19x faster                                                            |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.60 ms: 1.19x faster                                                           |
| bench_thread_pool        | 947 us                                                 | 820 us: 1.16x faster                                                            |
| dulwich_log              | 75.9 ms                                                | 66.4 ms: 1.14x faster                                                           |
| xml_etree_generate       | 94.2 ms                                                | 82.6 ms: 1.14x faster                                                           |
| create_gc_cycles         | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                           |
| json_loads               | 28.8 us                                                | 25.7 us: 1.12x faster                                                           |
| mdp                      | 2.82 sec                                               | 2.56 sec: 1.10x faster                                                          |
| json                     | 5.42 ms                                                | 4.92 ms: 1.10x faster                                                           |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                                            |
| regex_v8                 | 25.0 ms                                                | 23.1 ms: 1.08x faster                                                           |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                            |
| pathlib                  | 20.0 ms                                                | 18.6 ms: 1.08x faster                                                           |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                                           |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                                            |
| regex_dna                | 222 ms                                                 | 214 ms: 1.04x faster                                                            |
| pickle                   | 10.3 us                                                | 10.2 us: 1.01x faster                                                           |
| pickle_list              | 4.56 us                                                | 4.64 us: 1.02x slower                                                           |
| unpickle_list            | 4.82 us                                                | 4.91 us: 1.02x slower                                                           |
| unpickle                 | 14.1 us                                                | 14.8 us: 1.05x slower                                                           |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                                            |
| gc_traversal             | 3.84 ms                                                | 4.06 ms: 1.06x slower                                                           |
| async_generators         | 425 ms                                                 | 450 ms: 1.06x slower                                                            |
| pickle_dict              | 27.3 us                                                | 30.3 us: 1.11x slower                                                           |
| regex_effbot             | 3.23 ms                                                | 3.66 ms: 1.13x slower                                                           |
| coverage                 | 72.8 ms                                                | 84.3 ms: 1.16x slower                                                           |
| python_startup_no_site   | 5.82 ms                                                | 6.88 ms: 1.18x slower                                                           |
| telco                    | 6.54 ms                                                | 7.79 ms: 1.19x slower                                                           |
| dask                     | 423 ms                                                 | 522 ms: 1.24x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                                    |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
