
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3a314f7
- commit date: 2023-06-10
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.68 sec: 1.18x faster                                |
| tornado_http   | 127 ms                                                 | 96.3 ms: 1.32x faster                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.7 ms: 1.53x faster                                 |
| float          | 111 ms                                                 | 79.7 ms: 1.39x faster                                 |
| pidigits       | 190 ms                                                 | 196 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                  |
| regex_v8       | 25.0 ms                                                | 23.0 ms: 1.09x faster                                 |
| regex_dna      | 222 ms                                                 | 215 ms: 1.03x faster                                  |
| regex_effbot   | 3.23 ms                                                | 3.56 ms: 1.10x slower                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 305 us: 1.49x faster                                  |
| unpickle_pure_python | 300 us                                                 | 212 us: 1.42x faster                                  |
| json_dumps           | 13.5 ms                                                | 9.88 ms: 1.37x faster                                 |
| tomli_loads          | 2.92 sec                                               | 2.21 sec: 1.32x faster                                |
| xml_etree_process    | 74.9 ms                                                | 57.4 ms: 1.30x faster                                 |
| json_loads           | 28.8 us                                                | 25.3 us: 1.14x faster                                 |
| xml_etree_generate   | 94.2 ms                                                | 83.8 ms: 1.12x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                  |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.03x slower                                 |
| pickle               | 10.3 us                                                | 10.8 us: 1.05x slower                                 |
| unpickle             | 14.1 us                                                | 15.3 us: 1.08x slower                                 |
| pickle_dict          | 27.3 us                                                | 31.2 us: 1.14x slower                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                          |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.19 ms: 1.54x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 6.68 ms: 1.15x slower                                 |
| Geometric mean         | (ref)                                                  | 1.16x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.5 ms: 1.40x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 143 us: 3.57x faster                                  |
| generators               | 76.8 ms                                                | 28.7 ms: 2.67x faster                                 |
| deltablue                | 7.42 ms                                                | 3.22 ms: 2.30x faster                                 |
| asyncio_tcp              | 925 ms                                                 | 504 ms: 1.84x faster                                  |
| logging_silent           | 175 ns                                                 | 95.4 ns: 1.84x faster                                 |
| richards_super           | 90.7 ms                                                | 50.5 ms: 1.80x faster                                 |
| chaos                    | 106 ms                                                 | 61.8 ms: 1.72x faster                                 |
| richards                 | 74.9 ms                                                | 44.3 ms: 1.69x faster                                 |
| go                       | 229 ms                                                 | 136 ms: 1.69x faster                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.78 sec: 1.69x faster                                |
| scimark_sor              | 197 ms                                                 | 118 ms: 1.67x faster                                  |
| raytrace                 | 464 ms                                                 | 291 ms: 1.59x faster                                  |
| sqlglot_parse            | 2.06 ms                                                | 1.30 ms: 1.58x faster                                 |
| hexiom                   | 9.53 ms                                                | 6.03 ms: 1.58x faster                                 |
| python_startup           | 14.2 ms                                                | 9.19 ms: 1.54x faster                                 |
| nbody                    | 142 ms                                                 | 92.7 ms: 1.53x faster                                 |
| scimark_monte_carlo      | 108 ms                                                 | 71.2 ms: 1.52x faster                                 |
| pyflate                  | 673 ms                                                 | 444 ms: 1.52x faster                                  |
| crypto_pyaes             | 118 ms                                                 | 78.2 ms: 1.52x faster                                 |
| sqlglot_transpile        | 2.45 ms                                                | 1.62 ms: 1.51x faster                                 |
| scimark_lu               | 163 ms                                                 | 109 ms: 1.50x faster                                  |
| pickle_pure_python       | 455 us                                                 | 305 us: 1.49x faster                                  |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.47x faster                                |
| async_tree_none          | 717 ms                                                 | 488 ms: 1.47x faster                                  |
| unpack_sequence          | 64.7 ns                                                | 44.3 ns: 1.46x faster                                 |
| spectral_norm            | 150 ms                                                 | 103 ms: 1.46x faster                                  |
| async_tree_memoization   | 854 ms                                                 | 590 ms: 1.45x faster                                  |
| deepcopy_memo            | 52.3 us                                                | 36.7 us: 1.43x faster                                 |
| unpickle_pure_python     | 300 us                                                 | 212 us: 1.42x faster                                  |
| coroutines               | 31.8 ms                                                | 22.5 ms: 1.42x faster                                 |
| mako                     | 14.8 ms                                                | 10.5 ms: 1.40x faster                                 |
| float                    | 111 ms                                                 | 79.7 ms: 1.39x faster                                 |
| logging_format           | 8.91 us                                                | 6.46 us: 1.38x faster                                 |
| json_dumps               | 13.5 ms                                                | 9.88 ms: 1.37x faster                                 |
| pprint_pformat           | 1.99 sec                                               | 1.46 sec: 1.36x faster                                |
| logging_simple           | 8.07 us                                                | 5.98 us: 1.35x faster                                 |
| pprint_safe_repr         | 955 ms                                                 | 720 ms: 1.33x faster                                  |
| tomli_loads              | 2.92 sec                                               | 2.21 sec: 1.32x faster                                |
| tornado_http             | 127 ms                                                 | 96.3 ms: 1.32x faster                                 |
| comprehensions           | 26.8 us                                                | 20.4 us: 1.32x faster                                 |
| pycparser                | 1.50 sec                                               | 1.14 sec: 1.31x faster                                |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 728 ms: 1.31x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 57.4 ms: 1.30x faster                                 |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                  |
| mypy2                    | 428 ms                                                 | 336 ms: 1.28x faster                                  |
| deepcopy                 | 442 us                                                 | 347 us: 1.27x faster                                  |
| sqlglot_normalize        | 135 ms                                                 | 107 ms: 1.27x faster                                  |
| nqueens                  | 100 ms                                                 | 79.7 ms: 1.26x faster                                 |
| sqlglot_optimize         | 65.3 ms                                                | 52.9 ms: 1.23x faster                                 |
| fannkuch                 | 486 ms                                                 | 394 ms: 1.23x faster                                  |
| deepcopy_reduce          | 3.82 us                                                | 3.16 us: 1.21x faster                                 |
| scimark_fft              | 424 ms                                                 | 357 ms: 1.19x faster                                  |
| docutils                 | 3.17 sec                                               | 2.68 sec: 1.18x faster                                |
| dulwich_log              | 75.9 ms                                                | 65.0 ms: 1.17x faster                                 |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.72 ms: 1.15x faster                                 |
| bench_thread_pool        | 947 us                                                 | 825 us: 1.15x faster                                  |
| json_loads               | 28.8 us                                                | 25.3 us: 1.14x faster                                 |
| xml_etree_generate       | 94.2 ms                                                | 83.8 ms: 1.12x faster                                 |
| json                     | 5.42 ms                                                | 4.86 ms: 1.11x faster                                 |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.11x faster                                 |
| mdp                      | 2.82 sec                                               | 2.55 sec: 1.11x faster                                |
| meteor_contest           | 115 ms                                                 | 104 ms: 1.10x faster                                  |
| regex_v8                 | 25.0 ms                                                | 23.0 ms: 1.09x faster                                 |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.09x faster                                  |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                  |
| pathlib                  | 20.0 ms                                                | 18.7 ms: 1.07x faster                                 |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                 |
| regex_dna                | 222 ms                                                 | 215 ms: 1.03x faster                                  |
| gc_traversal             | 3.84 ms                                                | 3.85 ms: 1.00x slower                                 |
| unpickle_list            | 4.82 us                                                | 4.94 us: 1.03x slower                                 |
| pidigits                 | 190 ms                                                 | 196 ms: 1.03x slower                                  |
| pickle                   | 10.3 us                                                | 10.8 us: 1.05x slower                                 |
| async_generators         | 425 ms                                                 | 448 ms: 1.05x slower                                  |
| telco                    | 6.54 ms                                                | 6.92 ms: 1.06x slower                                 |
| unpickle                 | 14.1 us                                                | 15.3 us: 1.08x slower                                 |
| regex_effbot             | 3.23 ms                                                | 3.56 ms: 1.10x slower                                 |
| pickle_dict              | 27.3 us                                                | 31.2 us: 1.14x slower                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.68 ms: 1.15x slower                                 |
| dask                     | 423 ms                                                 | 519 ms: 1.23x slower                                  |
| coverage                 | 72.8 ms                                                | 92.4 ms: 1.27x slower                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                          |

Benchmark hidden because not significant (2): pickle_list, bench_mp_pool
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
