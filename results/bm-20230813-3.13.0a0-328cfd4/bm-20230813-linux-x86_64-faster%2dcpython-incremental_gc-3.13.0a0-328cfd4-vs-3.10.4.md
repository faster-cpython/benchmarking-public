
# Results vs. 3.10.4

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 328cfd4
- commit date: 2023-08-13
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.42 sec: 1.31x faster                                                    |
| tornado_http   | 127 ms                                                 | 93.6 ms: 1.36x faster                                                     |
| Geometric mean | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.7 ms: 1.60x faster                                                     |
| float          | 111 ms                                                 | 75.0 ms: 1.47x faster                                                     |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.31x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                     |
| regex_dna      | 222 ms                                                 | 213 ms: 1.04x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.53 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 299 us: 1.52x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 213 us: 1.41x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.72 ms: 1.39x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 58.0 ms: 1.29x faster                                                     |
| tomli_loads          | 2.92 sec                                               | 2.32 sec: 1.26x faster                                                    |
| json_loads           | 28.8 us                                                | 25.6 us: 1.12x faster                                                     |
| xml_etree_generate   | 94.2 ms                                                | 84.1 ms: 1.12x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 101 ms: 1.11x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                                      |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                                     |
| pickle_list          | 4.56 us                                                | 4.63 us: 1.02x slower                                                     |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                                     |
| unpickle_list        | 4.82 us                                                | 5.16 us: 1.07x slower                                                     |
| pickle_dict          | 27.3 us                                                | 32.2 us: 1.18x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.27 ms: 1.53x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.74 ms: 1.16x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.36x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 145 us: 3.52x faster                                                      |
| generators               | 76.8 ms                                                | 28.4 ms: 2.71x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 676 ms: 2.63x faster                                                      |
| async_tree_none          | 717 ms                                                 | 308 ms: 2.33x faster                                                      |
| deltablue                | 7.42 ms                                                | 3.20 ms: 2.32x faster                                                     |
| async_tree_memoization   | 854 ms                                                 | 393 ms: 2.17x faster                                                      |
| asyncio_tcp              | 925 ms                                                 | 487 ms: 1.90x faster                                                      |
| chaos                    | 106 ms                                                 | 59.6 ms: 1.78x faster                                                     |
| logging_silent           | 175 ns                                                 | 99.7 ns: 1.76x faster                                                     |
| richards_super           | 90.7 ms                                                | 52.5 ms: 1.73x faster                                                     |
| raytrace                 | 464 ms                                                 | 272 ms: 1.71x faster                                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 560 ms: 1.70x faster                                                      |
| crypto_pyaes             | 118 ms                                                 | 70.2 ms: 1.69x faster                                                     |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                    |
| go                       | 229 ms                                                 | 138 ms: 1.66x faster                                                      |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.61x faster                                                      |
| richards                 | 74.9 ms                                                | 46.6 ms: 1.61x faster                                                     |
| sqlglot_parse            | 2.06 ms                                                | 1.29 ms: 1.60x faster                                                     |
| nbody                    | 142 ms                                                 | 88.7 ms: 1.60x faster                                                     |
| scimark_monte_carlo      | 108 ms                                                 | 68.2 ms: 1.59x faster                                                     |
| hexiom                   | 9.53 ms                                                | 6.18 ms: 1.54x faster                                                     |
| python_startup           | 14.2 ms                                                | 9.27 ms: 1.53x faster                                                     |
| pickle_pure_python       | 455 us                                                 | 299 us: 1.52x faster                                                      |
| sqlglot_transpile        | 2.45 ms                                                | 1.61 ms: 1.52x faster                                                     |
| pyflate                  | 673 ms                                                 | 446 ms: 1.51x faster                                                      |
| float                    | 111 ms                                                 | 75.0 ms: 1.47x faster                                                     |
| scimark_lu               | 163 ms                                                 | 113 ms: 1.44x faster                                                      |
| coroutines               | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                     |
| spectral_norm            | 150 ms                                                 | 105 ms: 1.42x faster                                                      |
| unpack_sequence          | 64.7 ns                                                | 45.7 ns: 1.42x faster                                                     |
| unpickle_pure_python     | 300 us                                                 | 213 us: 1.41x faster                                                      |
| json_dumps               | 13.5 ms                                                | 9.72 ms: 1.39x faster                                                     |
| logging_format           | 8.91 us                                                | 6.41 us: 1.39x faster                                                     |
| logging_simple           | 8.07 us                                                | 5.84 us: 1.38x faster                                                     |
| deepcopy_memo            | 52.3 us                                                | 38.0 us: 1.38x faster                                                     |
| tornado_http             | 127 ms                                                 | 93.6 ms: 1.36x faster                                                     |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.36x faster                                                     |
| pprint_pformat           | 1.99 sec                                               | 1.46 sec: 1.36x faster                                                    |
| pycparser                | 1.50 sec                                               | 1.12 sec: 1.34x faster                                                    |
| pprint_safe_repr         | 955 ms                                                 | 718 ms: 1.33x faster                                                      |
| docutils                 | 3.17 sec                                               | 2.42 sec: 1.31x faster                                                    |
| comprehensions           | 26.8 us                                                | 20.6 us: 1.31x faster                                                     |
| xml_etree_process        | 74.9 ms                                                | 58.0 ms: 1.29x faster                                                     |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                                      |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.27x faster                                                      |
| tomli_loads              | 2.92 sec                                               | 2.32 sec: 1.26x faster                                                    |
| deepcopy                 | 442 us                                                 | 356 us: 1.24x faster                                                      |
| mypy2                    | 428 ms                                                 | 347 ms: 1.24x faster                                                      |
| sqlglot_optimize         | 65.3 ms                                                | 53.0 ms: 1.23x faster                                                     |
| fannkuch                 | 486 ms                                                 | 398 ms: 1.22x faster                                                      |
| nqueens                  | 100 ms                                                 | 82.7 ms: 1.21x faster                                                     |
| deepcopy_reduce          | 3.82 us                                                | 3.23 us: 1.18x faster                                                     |
| scimark_fft              | 424 ms                                                 | 364 ms: 1.16x faster                                                      |
| create_gc_cycles         | 1.67 ms                                                | 1.45 ms: 1.15x faster                                                     |
| dulwich_log              | 75.9 ms                                                | 66.3 ms: 1.14x faster                                                     |
| bench_thread_pool        | 947 us                                                 | 830 us: 1.14x faster                                                      |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.80 ms: 1.14x faster                                                     |
| regex_v8                 | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                     |
| json_loads               | 28.8 us                                                | 25.6 us: 1.12x faster                                                     |
| json                     | 5.42 ms                                                | 4.83 ms: 1.12x faster                                                     |
| xml_etree_generate       | 94.2 ms                                                | 84.1 ms: 1.12x faster                                                     |
| xml_etree_iterparse      | 111 ms                                                 | 101 ms: 1.11x faster                                                      |
| mdp                      | 2.82 sec                                               | 2.56 sec: 1.10x faster                                                    |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                                      |
| pathlib                  | 20.0 ms                                                | 18.6 ms: 1.08x faster                                                     |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                                      |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                                     |
| regex_dna                | 222 ms                                                 | 213 ms: 1.04x faster                                                      |
| gc_traversal             | 3.84 ms                                                | 3.79 ms: 1.01x faster                                                     |
| async_generators         | 425 ms                                                 | 430 ms: 1.01x slower                                                      |
| pickle                   | 10.3 us                                                | 10.4 us: 1.01x slower                                                     |
| pickle_list              | 4.56 us                                                | 4.63 us: 1.02x slower                                                     |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                                      |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                                     |
| unpickle_list            | 4.82 us                                                | 5.16 us: 1.07x slower                                                     |
| regex_effbot             | 3.23 ms                                                | 3.53 ms: 1.09x slower                                                     |
| python_startup_no_site   | 5.82 ms                                                | 6.74 ms: 1.16x slower                                                     |
| dask                     | 423 ms                                                 | 492 ms: 1.16x slower                                                      |
| pickle_dict              | 27.3 us                                                | 32.2 us: 1.18x slower                                                     |
| telco                    | 6.54 ms                                                | 8.16 ms: 1.25x slower                                                     |
| coverage                 | 72.8 ms                                                | 92.5 ms: 1.27x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x
