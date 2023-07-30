
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 5113ed7
- commit date: 2023-07-29
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                |
| tornado_http   | 127 ms                                                 | 95.6 ms: 1.33x faster                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.4 ms: 1.52x faster                                 |
| float          | 111 ms                                                 | 80.4 ms: 1.37x faster                                 |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 139 ms: 1.28x faster                                  |
| regex_v8       | 25.0 ms                                                | 22.9 ms: 1.09x faster                                 |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                  |
| regex_effbot   | 3.23 ms                                                | 3.49 ms: 1.08x slower                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-python-main-3.13.0a0-5113ed7 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 298 us: 1.53x faster                                  |
| unpickle_pure_python | 300 us                                                 | 216 us: 1.39x faster                                  |
| json_dumps           | 13.5 ms                                                | 9.75 ms: 1.39x faster                                 |
| xml_etree_process    | 74.9 ms                                                | 58.4 ms: 1.28x faster                                 |
| tomli_loads          | 2.92 sec                                               | 2.34 sec: 1.25x faster                                |
| json_loads           | 28.8 us                                                | 25.7 us: 1.12x faster                                 |
| xml_etree_generate   | 94.2 ms                                                | 84.2 ms: 1.12x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                  |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                 |
| unpickle_list        | 4.82 us                                                | 5.01 us: 1.04x slower                                 |
| pickle_list          | 4.56 us                                                | 4.77 us: 1.05x slower                                 |
| unpickle             | 14.1 us                                                | 15.4 us: 1.09x slower                                 |
| pickle_dict          | 27.3 us                                                | 31.5 us: 1.16x slower                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-python-main-3.13.0a0-5113ed7 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.31 ms: 1.52x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 6.80 ms: 1.17x slower                                 |
| Geometric mean         | (ref)                                                  | 1.14x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-python-main-3.13.0a0-5113ed7 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.37x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-python-main-3.13.0a0-5113ed7 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 141 us: 3.62x faster                                  |
| generators               | 76.8 ms                                                | 28.5 ms: 2.70x faster                                 |
| deltablue                | 7.42 ms                                                | 3.22 ms: 2.31x faster                                 |
| asyncio_tcp              | 925 ms                                                 | 491 ms: 1.88x faster                                  |
| chaos                    | 106 ms                                                 | 59.8 ms: 1.78x faster                                 |
| raytrace                 | 464 ms                                                 | 271 ms: 1.71x faster                                  |
| richards_super           | 90.7 ms                                                | 53.2 ms: 1.71x faster                                 |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.78 sec: 1.69x faster                                |
| logging_silent           | 175 ns                                                 | 105 ns: 1.67x faster                                  |
| crypto_pyaes             | 118 ms                                                 | 71.8 ms: 1.65x faster                                 |
| go                       | 229 ms                                                 | 140 ms: 1.64x faster                                  |
| richards                 | 74.9 ms                                                | 46.4 ms: 1.62x faster                                 |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.61x faster                                  |
| scimark_monte_carlo      | 108 ms                                                 | 68.4 ms: 1.58x faster                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.30 ms: 1.58x faster                                 |
| hexiom                   | 9.53 ms                                                | 6.12 ms: 1.56x faster                                 |
| pickle_pure_python       | 455 us                                                 | 298 us: 1.53x faster                                  |
| python_startup           | 14.2 ms                                                | 9.31 ms: 1.52x faster                                 |
| nbody                    | 142 ms                                                 | 93.4 ms: 1.52x faster                                 |
| sqlglot_transpile        | 2.45 ms                                                | 1.62 ms: 1.51x faster                                 |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                |
| async_tree_none          | 717 ms                                                 | 482 ms: 1.49x faster                                  |
| coroutines               | 31.8 ms                                                | 21.6 ms: 1.47x faster                                 |
| pyflate                  | 673 ms                                                 | 457 ms: 1.47x faster                                  |
| unpack_sequence          | 64.7 ns                                                | 44.4 ns: 1.46x faster                                 |
| scimark_lu               | 163 ms                                                 | 112 ms: 1.46x faster                                  |
| async_tree_memoization   | 854 ms                                                 | 587 ms: 1.45x faster                                  |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.40x faster                                  |
| unpickle_pure_python     | 300 us                                                 | 216 us: 1.39x faster                                  |
| json_dumps               | 13.5 ms                                                | 9.75 ms: 1.39x faster                                 |
| deepcopy_memo            | 52.3 us                                                | 37.8 us: 1.39x faster                                 |
| float                    | 111 ms                                                 | 80.4 ms: 1.37x faster                                 |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.37x faster                                 |
| logging_simple           | 8.07 us                                                | 5.92 us: 1.36x faster                                 |
| logging_format           | 8.91 us                                                | 6.55 us: 1.36x faster                                 |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.34x faster                                |
| tornado_http             | 127 ms                                                 | 95.6 ms: 1.33x faster                                 |
| pprint_safe_repr         | 955 ms                                                 | 722 ms: 1.32x faster                                  |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 722 ms: 1.32x faster                                  |
| comprehensions           | 26.8 us                                                | 20.6 us: 1.30x faster                                 |
| pycparser                | 1.50 sec                                               | 1.16 sec: 1.30x faster                                |
| xml_etree_process        | 74.9 ms                                                | 58.4 ms: 1.28x faster                                 |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.28x faster                                  |
| regex_compile            | 177 ms                                                 | 139 ms: 1.28x faster                                  |
| mypy2                    | 428 ms                                                 | 338 ms: 1.27x faster                                  |
| nqueens                  | 100 ms                                                 | 79.8 ms: 1.25x faster                                 |
| tomli_loads              | 2.92 sec                                               | 2.34 sec: 1.25x faster                                |
| sqlglot_optimize         | 65.3 ms                                                | 53.1 ms: 1.23x faster                                 |
| deepcopy                 | 442 us                                                 | 362 us: 1.22x faster                                  |
| fannkuch                 | 486 ms                                                 | 402 ms: 1.21x faster                                  |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                |
| deepcopy_reduce          | 3.82 us                                                | 3.26 us: 1.17x faster                                 |
| scimark_fft              | 424 ms                                                 | 366 ms: 1.16x faster                                  |
| bench_thread_pool        | 947 us                                                 | 819 us: 1.16x faster                                  |
| dulwich_log              | 75.9 ms                                                | 66.3 ms: 1.14x faster                                 |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.83 ms: 1.13x faster                                 |
| create_gc_cycles         | 1.67 ms                                                | 1.48 ms: 1.13x faster                                 |
| json_loads               | 28.8 us                                                | 25.7 us: 1.12x faster                                 |
| xml_etree_generate       | 94.2 ms                                                | 84.2 ms: 1.12x faster                                 |
| json                     | 5.42 ms                                                | 4.89 ms: 1.11x faster                                 |
| regex_v8                 | 25.0 ms                                                | 22.9 ms: 1.09x faster                                 |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.09x faster                                  |
| pathlib                  | 20.0 ms                                                | 18.5 ms: 1.08x faster                                 |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                  |
| sqlite_synth             | 2.93 us                                                | 2.73 us: 1.07x faster                                 |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                  |
| regex_dna                | 222 ms                                                 | 208 ms: 1.07x faster                                  |
| gc_traversal             | 3.84 ms                                                | 3.66 ms: 1.05x faster                                 |
| mdp                      | 2.82 sec                                               | 2.74 sec: 1.03x faster                                |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                 |
| unpickle_list            | 4.82 us                                                | 5.01 us: 1.04x slower                                 |
| pickle_list              | 4.56 us                                                | 4.77 us: 1.05x slower                                 |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                  |
| async_generators         | 425 ms                                                 | 449 ms: 1.06x slower                                  |
| regex_effbot             | 3.23 ms                                                | 3.49 ms: 1.08x slower                                 |
| unpickle                 | 14.1 us                                                | 15.4 us: 1.09x slower                                 |
| pickle_dict              | 27.3 us                                                | 31.5 us: 1.16x slower                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.80 ms: 1.17x slower                                 |
| telco                    | 6.54 ms                                                | 7.95 ms: 1.22x slower                                 |
| dask                     | 423 ms                                                 | 521 ms: 1.23x slower                                  |
| coverage                 | 72.8 ms                                                | 93.2 ms: 1.28x slower                                 |
| Geometric mean           | (ref)                                                  | 1.29x faster                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
