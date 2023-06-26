
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: bef1c87
- commit date: 2023-06-25
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-linux-x86_64-python-main-3.13.0a0-bef1c87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.64 sec: 1.20x faster                                |
| tornado_http   | 127 ms                                                 | 95.7 ms: 1.33x faster                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-linux-x86_64-python-main-3.13.0a0-bef1c87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 142 ms                                                 | 91.0 ms: 1.56x faster                                 |
| float          | 111 ms                                                 | 79.3 ms: 1.39x faster                                 |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-linux-x86_64-python-main-3.13.0a0-bef1c87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                  |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                 |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                  |
| regex_effbot   | 3.23 ms                                                | 3.48 ms: 1.08x slower                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-linux-x86_64-python-main-3.13.0a0-bef1c87 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 308 us: 1.48x faster                                  |
| unpickle_pure_python | 300 us                                                 | 213 us: 1.41x faster                                  |
| json_dumps           | 13.5 ms                                                | 9.76 ms: 1.39x faster                                 |
| tomli_loads          | 2.92 sec                                               | 2.17 sec: 1.35x faster                                |
| xml_etree_process    | 74.9 ms                                                | 57.1 ms: 1.31x faster                                 |
| json_loads           | 28.8 us                                                | 25.4 us: 1.13x faster                                 |
| xml_etree_generate   | 94.2 ms                                                | 83.8 ms: 1.12x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.08x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                  |
| pickle_list          | 4.56 us                                                | 4.53 us: 1.01x faster                                 |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.03x slower                                 |
| pickle               | 10.3 us                                                | 10.8 us: 1.05x slower                                 |
| unpickle             | 14.1 us                                                | 15.1 us: 1.07x slower                                 |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-linux-x86_64-python-main-3.13.0a0-bef1c87 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.17 ms: 1.54x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 6.67 ms: 1.15x slower                                 |
| Geometric mean         | (ref)                                                  | 1.16x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-linux-x86_64-python-main-3.13.0a0-bef1c87 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-linux-x86_64-python-main-3.13.0a0-bef1c87 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.49x faster                                  |
| generators               | 76.8 ms                                                | 28.9 ms: 2.66x faster                                 |
| deltablue                | 7.42 ms                                                | 3.22 ms: 2.30x faster                                 |
| asyncio_tcp              | 925 ms                                                 | 503 ms: 1.84x faster                                  |
| logging_silent           | 175 ns                                                 | 97.8 ns: 1.79x faster                                 |
| chaos                    | 106 ms                                                 | 59.4 ms: 1.79x faster                                 |
| richards_super           | 90.7 ms                                                | 50.7 ms: 1.79x faster                                 |
| raytrace                 | 464 ms                                                 | 268 ms: 1.73x faster                                  |
| go                       | 229 ms                                                 | 135 ms: 1.70x faster                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                |
| scimark_sor              | 197 ms                                                 | 117 ms: 1.68x faster                                  |
| richards                 | 74.9 ms                                                | 44.7 ms: 1.68x faster                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.29 ms: 1.59x faster                                 |
| hexiom                   | 9.53 ms                                                | 6.04 ms: 1.58x faster                                 |
| pyflate                  | 673 ms                                                 | 431 ms: 1.56x faster                                  |
| nbody                    | 142 ms                                                 | 91.0 ms: 1.56x faster                                 |
| python_startup           | 14.2 ms                                                | 9.17 ms: 1.54x faster                                 |
| sqlglot_transpile        | 2.45 ms                                                | 1.60 ms: 1.53x faster                                 |
| scimark_monte_carlo      | 108 ms                                                 | 71.1 ms: 1.52x faster                                 |
| crypto_pyaes             | 118 ms                                                 | 77.8 ms: 1.52x faster                                 |
| async_tree_io            | 1.77 sec                                               | 1.18 sec: 1.51x faster                                |
| async_tree_none          | 717 ms                                                 | 478 ms: 1.50x faster                                  |
| scimark_lu               | 163 ms                                                 | 109 ms: 1.49x faster                                  |
| pickle_pure_python       | 455 us                                                 | 308 us: 1.48x faster                                  |
| async_tree_memoization   | 854 ms                                                 | 583 ms: 1.47x faster                                  |
| coroutines               | 31.8 ms                                                | 21.8 ms: 1.46x faster                                 |
| spectral_norm            | 150 ms                                                 | 103 ms: 1.45x faster                                  |
| deepcopy_memo            | 52.3 us                                                | 37.0 us: 1.41x faster                                 |
| unpickle_pure_python     | 300 us                                                 | 213 us: 1.41x faster                                  |
| float                    | 111 ms                                                 | 79.3 ms: 1.39x faster                                 |
| json_dumps               | 13.5 ms                                                | 9.76 ms: 1.39x faster                                 |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                 |
| logging_format           | 8.91 us                                                | 6.51 us: 1.37x faster                                 |
| pprint_pformat           | 1.99 sec                                               | 1.46 sec: 1.36x faster                                |
| logging_simple           | 8.07 us                                                | 5.93 us: 1.36x faster                                 |
| pprint_safe_repr         | 955 ms                                                 | 709 ms: 1.35x faster                                  |
| tomli_loads              | 2.92 sec                                               | 2.17 sec: 1.35x faster                                |
| pycparser                | 1.50 sec                                               | 1.13 sec: 1.33x faster                                |
| tornado_http             | 127 ms                                                 | 95.7 ms: 1.33x faster                                 |
| comprehensions           | 26.8 us                                                | 20.2 us: 1.33x faster                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 719 ms: 1.32x faster                                  |
| regex_compile            | 177 ms                                                 | 135 ms: 1.31x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 57.1 ms: 1.31x faster                                 |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.28x faster                                  |
| mypy2                    | 428 ms                                                 | 335 ms: 1.28x faster                                  |
| deepcopy                 | 442 us                                                 | 349 us: 1.26x faster                                  |
| sqlglot_optimize         | 65.3 ms                                                | 52.4 ms: 1.25x faster                                 |
| nqueens                  | 100 ms                                                 | 80.3 ms: 1.24x faster                                 |
| fannkuch                 | 486 ms                                                 | 391 ms: 1.24x faster                                  |
| unpack_sequence          | 64.7 ns                                                | 53.3 ns: 1.21x faster                                 |
| deepcopy_reduce          | 3.82 us                                                | 3.15 us: 1.21x faster                                 |
| scimark_fft              | 424 ms                                                 | 352 ms: 1.20x faster                                  |
| docutils                 | 3.17 sec                                               | 2.64 sec: 1.20x faster                                |
| dulwich_log              | 75.9 ms                                                | 65.2 ms: 1.16x faster                                 |
| bench_thread_pool        | 947 us                                                 | 814 us: 1.16x faster                                  |
| regex_v8                 | 25.0 ms                                                | 21.8 ms: 1.15x faster                                 |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.75 ms: 1.15x faster                                 |
| json_loads               | 28.8 us                                                | 25.4 us: 1.13x faster                                 |
| json                     | 5.42 ms                                                | 4.79 ms: 1.13x faster                                 |
| xml_etree_generate       | 94.2 ms                                                | 83.8 ms: 1.12x faster                                 |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.11x faster                                 |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.09x faster                                  |
| regex_dna                | 222 ms                                                 | 204 ms: 1.09x faster                                  |
| sqlite_synth             | 2.93 us                                                | 2.73 us: 1.08x faster                                 |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.08x faster                                  |
| mdp                      | 2.82 sec                                               | 2.64 sec: 1.07x faster                                |
| pathlib                  | 20.0 ms                                                | 18.8 ms: 1.07x faster                                 |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                  |
| pickle_list              | 4.56 us                                                | 4.53 us: 1.01x faster                                 |
| pidigits                 | 190 ms                                                 | 192 ms: 1.01x slower                                  |
| unpickle_list            | 4.82 us                                                | 4.94 us: 1.03x slower                                 |
| telco                    | 6.54 ms                                                | 6.80 ms: 1.04x slower                                 |
| pickle                   | 10.3 us                                                | 10.8 us: 1.05x slower                                 |
| async_generators         | 425 ms                                                 | 451 ms: 1.06x slower                                  |
| gc_traversal             | 3.84 ms                                                | 4.09 ms: 1.06x slower                                 |
| unpickle                 | 14.1 us                                                | 15.1 us: 1.07x slower                                 |
| regex_effbot             | 3.23 ms                                                | 3.48 ms: 1.08x slower                                 |
| pickle_dict              | 27.3 us                                                | 30.8 us: 1.13x slower                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.67 ms: 1.15x slower                                 |
| dask                     | 423 ms                                                 | 512 ms: 1.21x slower                                  |
| coverage                 | 72.8 ms                                                | 92.8 ms: 1.28x slower                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
