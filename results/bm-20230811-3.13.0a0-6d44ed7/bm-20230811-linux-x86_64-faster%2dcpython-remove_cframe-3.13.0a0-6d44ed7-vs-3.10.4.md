
# Results vs. 3.10.4

- fork: faster-cpython
- ref: remove_cframe
- machine: linux-x86_64
- commit hash: 6d44ed7
- commit date: 2023-08-11
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.63 sec: 1.21x faster                                                   |
| tornado_http   | 127 ms                                                 | 95.2 ms: 1.34x faster                                                    |
| Geometric mean | (ref)                                                  | 1.27x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.8 ms: 1.58x faster                                                    |
| float          | 111 ms                                                 | 79.6 ms: 1.39x faster                                                    |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                  | 1.28x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.30x faster                                                     |
| regex_v8       | 25.0 ms                                                | 23.1 ms: 1.09x faster                                                    |
| regex_dna      | 222 ms                                                 | 215 ms: 1.03x faster                                                     |
| regex_effbot   | 3.23 ms                                                | 3.79 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 300 us: 1.52x faster                                                     |
| unpickle_pure_python | 300 us                                                 | 214 us: 1.40x faster                                                     |
| json_dumps           | 13.5 ms                                                | 9.75 ms: 1.39x faster                                                    |
| tomli_loads          | 2.92 sec                                               | 2.12 sec: 1.38x faster                                                   |
| xml_etree_process    | 74.9 ms                                                | 57.6 ms: 1.30x faster                                                    |
| json_loads           | 28.8 us                                                | 25.3 us: 1.14x faster                                                    |
| xml_etree_generate   | 94.2 ms                                                | 83.0 ms: 1.14x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                                     |
| unpickle             | 14.1 us                                                | 14.0 us: 1.01x faster                                                    |
| pickle_list          | 4.56 us                                                | 4.60 us: 1.01x slower                                                    |
| unpickle_list        | 4.82 us                                                | 4.92 us: 1.02x slower                                                    |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                    |
| pickle_dict          | 27.3 us                                                | 31.3 us: 1.15x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.33 ms: 1.52x faster                                                    |
| python_startup_no_site | 5.82 ms                                                | 6.82 ms: 1.17x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 148 us: 3.46x faster                                                     |
| generators               | 76.8 ms                                                | 28.9 ms: 2.66x faster                                                    |
| deltablue                | 7.42 ms                                                | 3.30 ms: 2.25x faster                                                    |
| asyncio_tcp              | 925 ms                                                 | 485 ms: 1.91x faster                                                     |
| chaos                    | 106 ms                                                 | 60.5 ms: 1.76x faster                                                    |
| crypto_pyaes             | 118 ms                                                 | 67.7 ms: 1.75x faster                                                    |
| raytrace                 | 464 ms                                                 | 271 ms: 1.71x faster                                                     |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                   |
| logging_silent           | 175 ns                                                 | 105 ns: 1.67x faster                                                     |
| richards_super           | 90.7 ms                                                | 54.3 ms: 1.67x faster                                                    |
| async_tree_none          | 717 ms                                                 | 436 ms: 1.65x faster                                                     |
| go                       | 229 ms                                                 | 140 ms: 1.63x faster                                                     |
| sqlglot_parse            | 2.06 ms                                                | 1.26 ms: 1.63x faster                                                    |
| scimark_monte_carlo      | 108 ms                                                 | 66.5 ms: 1.63x faster                                                    |
| scimark_sor              | 197 ms                                                 | 123 ms: 1.60x faster                                                     |
| nbody                    | 142 ms                                                 | 89.8 ms: 1.58x faster                                                    |
| hexiom                   | 9.53 ms                                                | 6.04 ms: 1.58x faster                                                    |
| richards                 | 74.9 ms                                                | 48.0 ms: 1.56x faster                                                    |
| sqlglot_transpile        | 2.45 ms                                                | 1.58 ms: 1.55x faster                                                    |
| unpack_sequence          | 64.7 ns                                                | 41.8 ns: 1.55x faster                                                    |
| async_tree_memoization   | 854 ms                                                 | 561 ms: 1.52x faster                                                     |
| pickle_pure_python       | 455 us                                                 | 300 us: 1.52x faster                                                     |
| python_startup           | 14.2 ms                                                | 9.33 ms: 1.52x faster                                                    |
| pyflate                  | 673 ms                                                 | 447 ms: 1.50x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.50x faster                                                   |
| coroutines               | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                    |
| scimark_lu               | 163 ms                                                 | 114 ms: 1.43x faster                                                     |
| spectral_norm            | 150 ms                                                 | 105 ms: 1.42x faster                                                     |
| deepcopy_memo            | 52.3 us                                                | 37.1 us: 1.41x faster                                                    |
| unpickle_pure_python     | 300 us                                                 | 214 us: 1.40x faster                                                     |
| float                    | 111 ms                                                 | 79.6 ms: 1.39x faster                                                    |
| json_dumps               | 13.5 ms                                                | 9.75 ms: 1.39x faster                                                    |
| logging_format           | 8.91 us                                                | 6.42 us: 1.39x faster                                                    |
| tomli_loads              | 2.92 sec                                               | 2.12 sec: 1.38x faster                                                   |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 696 ms: 1.37x faster                                                     |
| logging_simple           | 8.07 us                                                | 5.91 us: 1.37x faster                                                    |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                                   |
| tornado_http             | 127 ms                                                 | 95.2 ms: 1.34x faster                                                    |
| pprint_safe_repr         | 955 ms                                                 | 714 ms: 1.34x faster                                                     |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.30x faster                                                   |
| xml_etree_process        | 74.9 ms                                                | 57.6 ms: 1.30x faster                                                    |
| comprehensions           | 26.8 us                                                | 20.7 us: 1.30x faster                                                    |
| regex_compile            | 177 ms                                                 | 137 ms: 1.30x faster                                                     |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.29x faster                                                     |
| fannkuch                 | 486 ms                                                 | 384 ms: 1.27x faster                                                     |
| deepcopy                 | 442 us                                                 | 351 us: 1.26x faster                                                     |
| sqlglot_optimize         | 65.3 ms                                                | 52.6 ms: 1.24x faster                                                    |
| nqueens                  | 100 ms                                                 | 81.6 ms: 1.23x faster                                                    |
| docutils                 | 3.17 sec                                               | 2.63 sec: 1.21x faster                                                   |
| deepcopy_reduce          | 3.82 us                                                | 3.17 us: 1.21x faster                                                    |
| scimark_fft              | 424 ms                                                 | 354 ms: 1.20x faster                                                     |
| bench_thread_pool        | 947 us                                                 | 815 us: 1.16x faster                                                     |
| dulwich_log              | 75.9 ms                                                | 65.9 ms: 1.15x faster                                                    |
| json_loads               | 28.8 us                                                | 25.3 us: 1.14x faster                                                    |
| xml_etree_generate       | 94.2 ms                                                | 83.0 ms: 1.14x faster                                                    |
| create_gc_cycles         | 1.67 ms                                                | 1.47 ms: 1.13x faster                                                    |
| json                     | 5.42 ms                                                | 4.82 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.88 ms: 1.12x faster                                                    |
| mdp                      | 2.82 sec                                               | 2.56 sec: 1.10x faster                                                   |
| xml_etree_iterparse      | 111 ms                                                 | 102 ms: 1.09x faster                                                     |
| regex_v8                 | 25.0 ms                                                | 23.1 ms: 1.09x faster                                                    |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                                     |
| pathlib                  | 20.0 ms                                                | 18.6 ms: 1.08x faster                                                    |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                                     |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                                    |
| regex_dna                | 222 ms                                                 | 215 ms: 1.03x faster                                                     |
| unpickle                 | 14.1 us                                                | 14.0 us: 1.01x faster                                                    |
| pickle_list              | 4.56 us                                                | 4.60 us: 1.01x slower                                                    |
| unpickle_list            | 4.82 us                                                | 4.92 us: 1.02x slower                                                    |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                                    |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                                     |
| async_generators         | 425 ms                                                 | 457 ms: 1.08x slower                                                     |
| gc_traversal             | 3.84 ms                                                | 4.18 ms: 1.09x slower                                                    |
| pickle_dict              | 27.3 us                                                | 31.3 us: 1.15x slower                                                    |
| coverage                 | 72.8 ms                                                | 84.9 ms: 1.17x slower                                                    |
| python_startup_no_site   | 5.82 ms                                                | 6.82 ms: 1.17x slower                                                    |
| regex_effbot             | 3.23 ms                                                | 3.79 ms: 1.17x slower                                                    |
| telco                    | 6.54 ms                                                | 7.94 ms: 1.21x slower                                                    |
| dask                     | 423 ms                                                 | 516 ms: 1.22x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                             |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x
