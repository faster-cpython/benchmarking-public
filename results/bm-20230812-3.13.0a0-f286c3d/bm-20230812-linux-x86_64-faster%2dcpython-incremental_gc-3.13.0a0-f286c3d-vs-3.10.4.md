
# Results vs. 3.10.4

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: f286c3d
- commit date: 2023-08-12
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.37 sec: 1.34x faster                                                    |
| tornado_http   | 127 ms                                                 | 93.4 ms: 1.36x faster                                                     |
| Geometric mean | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.1 ms: 1.61x faster                                                     |
| float          | 111 ms                                                 | 71.7 ms: 1.54x faster                                                     |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                                      |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                     |
| regex_dna      | 222 ms                                                 | 210 ms: 1.05x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.42 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 295 us: 1.54x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 213 us: 1.41x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.88 ms: 1.37x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 56.9 ms: 1.32x faster                                                     |
| tomli_loads          | 2.92 sec                                               | 2.34 sec: 1.25x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                 | 94.2 ms: 1.18x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 141 ms: 1.16x faster                                                      |
| xml_etree_generate   | 94.2 ms                                                | 81.3 ms: 1.16x faster                                                     |
| json_loads           | 28.8 us                                                | 25.7 us: 1.12x faster                                                     |
| pickle_list          | 4.56 us                                                | 4.64 us: 1.02x slower                                                     |
| unpickle_list        | 4.82 us                                                | 4.92 us: 1.02x slower                                                     |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                     |
| unpickle             | 14.1 us                                                | 15.4 us: 1.09x slower                                                     |
| pickle_dict          | 27.3 us                                                | 32.6 us: 1.19x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.27 ms: 1.53x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.79 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 147 us: 3.48x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 565 ms: 3.14x faster                                                      |
| generators               | 76.8 ms                                                | 28.5 ms: 2.70x faster                                                     |
| async_tree_none          | 717 ms                                                 | 278 ms: 2.58x faster                                                      |
| async_tree_memoization   | 854 ms                                                 | 344 ms: 2.48x faster                                                      |
| deltablue                | 7.42 ms                                                | 3.15 ms: 2.35x faster                                                     |
| asyncio_tcp              | 925 ms                                                 | 487 ms: 1.90x faster                                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 506 ms: 1.88x faster                                                      |
| chaos                    | 106 ms                                                 | 59.5 ms: 1.79x faster                                                     |
| raytrace                 | 464 ms                                                 | 270 ms: 1.72x faster                                                      |
| crypto_pyaes             | 118 ms                                                 | 69.0 ms: 1.72x faster                                                     |
| logging_silent           | 175 ns                                                 | 102 ns: 1.72x faster                                                      |
| richards_super           | 90.7 ms                                                | 53.6 ms: 1.69x faster                                                     |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.78 sec: 1.69x faster                                                    |
| go                       | 229 ms                                                 | 136 ms: 1.68x faster                                                      |
| scimark_sor              | 197 ms                                                 | 120 ms: 1.63x faster                                                      |
| sqlglot_parse            | 2.06 ms                                                | 1.26 ms: 1.63x faster                                                     |
| scimark_monte_carlo      | 108 ms                                                 | 67.4 ms: 1.61x faster                                                     |
| nbody                    | 142 ms                                                 | 88.1 ms: 1.61x faster                                                     |
| hexiom                   | 9.53 ms                                                | 6.08 ms: 1.57x faster                                                     |
| richards                 | 74.9 ms                                                | 48.0 ms: 1.56x faster                                                     |
| sqlglot_transpile        | 2.45 ms                                                | 1.58 ms: 1.55x faster                                                     |
| pickle_pure_python       | 455 us                                                 | 295 us: 1.54x faster                                                      |
| float                    | 111 ms                                                 | 71.7 ms: 1.54x faster                                                     |
| python_startup           | 14.2 ms                                                | 9.27 ms: 1.53x faster                                                     |
| pyflate                  | 673 ms                                                 | 451 ms: 1.49x faster                                                      |
| spectral_norm            | 150 ms                                                 | 103 ms: 1.45x faster                                                      |
| scimark_lu               | 163 ms                                                 | 113 ms: 1.45x faster                                                      |
| unpack_sequence          | 64.7 ns                                                | 45.1 ns: 1.44x faster                                                     |
| coroutines               | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                     |
| unpickle_pure_python     | 300 us                                                 | 213 us: 1.41x faster                                                      |
| deepcopy_memo            | 52.3 us                                                | 37.5 us: 1.40x faster                                                     |
| logging_format           | 8.91 us                                                | 6.44 us: 1.38x faster                                                     |
| logging_simple           | 8.07 us                                                | 5.88 us: 1.37x faster                                                     |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                     |
| json_dumps               | 13.5 ms                                                | 9.88 ms: 1.37x faster                                                     |
| tornado_http             | 127 ms                                                 | 93.4 ms: 1.36x faster                                                     |
| pycparser                | 1.50 sec                                               | 1.12 sec: 1.35x faster                                                    |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.34x faster                                                    |
| docutils                 | 3.17 sec                                               | 2.37 sec: 1.34x faster                                                    |
| comprehensions           | 26.8 us                                                | 20.3 us: 1.32x faster                                                     |
| pprint_safe_repr         | 955 ms                                                 | 723 ms: 1.32x faster                                                      |
| xml_etree_process        | 74.9 ms                                                | 56.9 ms: 1.32x faster                                                     |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                                      |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.28x faster                                                      |
| mypy2                    | 428 ms                                                 | 339 ms: 1.26x faster                                                      |
| deepcopy                 | 442 us                                                 | 352 us: 1.26x faster                                                      |
| tomli_loads              | 2.92 sec                                               | 2.34 sec: 1.25x faster                                                    |
| fannkuch                 | 486 ms                                                 | 392 ms: 1.24x faster                                                      |
| sqlglot_optimize         | 65.3 ms                                                | 52.9 ms: 1.24x faster                                                     |
| nqueens                  | 100 ms                                                 | 81.9 ms: 1.22x faster                                                     |
| deepcopy_reduce          | 3.82 us                                                | 3.16 us: 1.21x faster                                                     |
| scimark_fft              | 424 ms                                                 | 352 ms: 1.20x faster                                                      |
| xml_etree_iterparse      | 111 ms                                                 | 94.2 ms: 1.18x faster                                                     |
| create_gc_cycles         | 1.67 ms                                                | 1.41 ms: 1.18x faster                                                     |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.68 ms: 1.17x faster                                                     |
| xml_etree_parse          | 163 ms                                                 | 141 ms: 1.16x faster                                                      |
| xml_etree_generate       | 94.2 ms                                                | 81.3 ms: 1.16x faster                                                     |
| regex_v8                 | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                     |
| dulwich_log              | 75.9 ms                                                | 66.0 ms: 1.15x faster                                                     |
| bench_thread_pool        | 947 us                                                 | 826 us: 1.15x faster                                                      |
| gc_traversal             | 3.84 ms                                                | 3.40 ms: 1.13x faster                                                     |
| json                     | 5.42 ms                                                | 4.84 ms: 1.12x faster                                                     |
| json_loads               | 28.8 us                                                | 25.7 us: 1.12x faster                                                     |
| mdp                      | 2.82 sec                                               | 2.53 sec: 1.11x faster                                                    |
| pathlib                  | 20.0 ms                                                | 18.4 ms: 1.09x faster                                                     |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                                      |
| regex_dna                | 222 ms                                                 | 210 ms: 1.05x faster                                                      |
| sqlite_synth             | 2.93 us                                                | 2.79 us: 1.05x faster                                                     |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                                      |
| pickle_list              | 4.56 us                                                | 4.64 us: 1.02x slower                                                     |
| unpickle_list            | 4.82 us                                                | 4.92 us: 1.02x slower                                                     |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                                     |
| regex_effbot             | 3.23 ms                                                | 3.42 ms: 1.06x slower                                                     |
| unpickle                 | 14.1 us                                                | 15.4 us: 1.09x slower                                                     |
| dask                     | 423 ms                                                 | 485 ms: 1.15x slower                                                      |
| python_startup_no_site   | 5.82 ms                                                | 6.79 ms: 1.17x slower                                                     |
| pickle_dict              | 27.3 us                                                | 32.6 us: 1.19x slower                                                     |
| telco                    | 6.54 ms                                                | 7.90 ms: 1.21x slower                                                     |
| coverage                 | 72.8 ms                                                | 93.0 ms: 1.28x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                              |

Benchmark hidden because not significant (2): async_generators, bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x
