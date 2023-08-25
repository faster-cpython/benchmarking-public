
# Results vs. 3.10.4

- fork: gvanrossum
- ref: new_for_iter_uops
- machine: linux-x86_64
- commit hash: 4ccb873
- commit date: 2023-07-12
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.65 sec: 1.20x faster                                                 |
| tornado_http   | 127 ms                                                 | 96.2 ms: 1.32x faster                                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.1 ms: 1.61x faster                                                  |
| float          | 111 ms                                                 | 80.3 ms: 1.38x faster                                                  |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                  |
| regex_dna      | 222 ms                                                 | 211 ms: 1.05x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.68 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 295 us: 1.54x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 211 us: 1.42x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.82 ms: 1.38x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 57.6 ms: 1.30x faster                                                  |
| tomli_loads          | 2.92 sec                                               | 2.30 sec: 1.27x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 83.7 ms: 1.13x faster                                                  |
| json_loads           | 28.8 us                                                | 25.7 us: 1.12x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                   |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                  |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.03x slower                                                  |
| unpickle             | 14.1 us                                                | 14.8 us: 1.05x slower                                                  |
| pickle_dict          | 27.3 us                                                | 32.6 us: 1.20x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.22 ms: 1.54x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.70 ms: 1.15x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 143 us: 3.56x faster                                                   |
| generators               | 76.8 ms                                                | 28.9 ms: 2.65x faster                                                  |
| deltablue                | 7.42 ms                                                | 3.29 ms: 2.25x faster                                                  |
| asyncio_tcp              | 925 ms                                                 | 507 ms: 1.83x faster                                                   |
| chaos                    | 106 ms                                                 | 58.8 ms: 1.81x faster                                                  |
| crypto_pyaes             | 118 ms                                                 | 68.9 ms: 1.72x faster                                                  |
| raytrace                 | 464 ms                                                 | 270 ms: 1.72x faster                                                   |
| logging_silent           | 175 ns                                                 | 102 ns: 1.72x faster                                                   |
| richards_super           | 90.7 ms                                                | 53.2 ms: 1.71x faster                                                  |
| go                       | 229 ms                                                 | 137 ms: 1.68x faster                                                   |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                 |
| scimark_sor              | 197 ms                                                 | 120 ms: 1.64x faster                                                   |
| nbody                    | 142 ms                                                 | 88.1 ms: 1.61x faster                                                  |
| richards                 | 74.9 ms                                                | 46.8 ms: 1.60x faster                                                  |
| sqlglot_parse            | 2.06 ms                                                | 1.29 ms: 1.59x faster                                                  |
| scimark_monte_carlo      | 108 ms                                                 | 68.1 ms: 1.59x faster                                                  |
| hexiom                   | 9.53 ms                                                | 5.99 ms: 1.59x faster                                                  |
| pickle_pure_python       | 455 us                                                 | 295 us: 1.54x faster                                                   |
| python_startup           | 14.2 ms                                                | 9.22 ms: 1.54x faster                                                  |
| sqlglot_transpile        | 2.45 ms                                                | 1.61 ms: 1.52x faster                                                  |
| pyflate                  | 673 ms                                                 | 449 ms: 1.50x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.50x faster                                                 |
| async_tree_none          | 717 ms                                                 | 479 ms: 1.50x faster                                                   |
| async_tree_memoization   | 854 ms                                                 | 586 ms: 1.46x faster                                                   |
| scimark_lu               | 163 ms                                                 | 112 ms: 1.45x faster                                                   |
| unpack_sequence          | 64.7 ns                                                | 45.3 ns: 1.43x faster                                                  |
| unpickle_pure_python     | 300 us                                                 | 211 us: 1.42x faster                                                   |
| spectral_norm            | 150 ms                                                 | 106 ms: 1.41x faster                                                   |
| coroutines               | 31.8 ms                                                | 22.6 ms: 1.41x faster                                                  |
| json_dumps               | 13.5 ms                                                | 9.82 ms: 1.38x faster                                                  |
| logging_format           | 8.91 us                                                | 6.47 us: 1.38x faster                                                  |
| float                    | 111 ms                                                 | 80.3 ms: 1.38x faster                                                  |
| deepcopy_memo            | 52.3 us                                                | 38.1 us: 1.37x faster                                                  |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                  |
| logging_simple           | 8.07 us                                                | 5.95 us: 1.36x faster                                                  |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                                 |
| pprint_safe_repr         | 955 ms                                                 | 716 ms: 1.33x faster                                                   |
| tornado_http             | 127 ms                                                 | 96.2 ms: 1.32x faster                                                  |
| comprehensions           | 26.8 us                                                | 20.3 us: 1.32x faster                                                  |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 725 ms: 1.31x faster                                                   |
| xml_etree_process        | 74.9 ms                                                | 57.6 ms: 1.30x faster                                                  |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                                   |
| pycparser                | 1.50 sec                                               | 1.17 sec: 1.28x faster                                                 |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.28x faster                                                   |
| mypy2                    | 428 ms                                                 | 337 ms: 1.27x faster                                                   |
| tomli_loads              | 2.92 sec                                               | 2.30 sec: 1.27x faster                                                 |
| nqueens                  | 100 ms                                                 | 78.9 ms: 1.27x faster                                                  |
| deepcopy                 | 442 us                                                 | 354 us: 1.25x faster                                                   |
| sqlglot_optimize         | 65.3 ms                                                | 52.9 ms: 1.24x faster                                                  |
| fannkuch                 | 486 ms                                                 | 396 ms: 1.23x faster                                                   |
| deepcopy_reduce          | 3.82 us                                                | 3.18 us: 1.20x faster                                                  |
| docutils                 | 3.17 sec                                               | 2.65 sec: 1.20x faster                                                 |
| scimark_fft              | 424 ms                                                 | 357 ms: 1.19x faster                                                   |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.68 ms: 1.17x faster                                                  |
| bench_thread_pool        | 947 us                                                 | 814 us: 1.16x faster                                                   |
| dulwich_log              | 75.9 ms                                                | 66.0 ms: 1.15x faster                                                  |
| xml_etree_generate       | 94.2 ms                                                | 83.7 ms: 1.13x faster                                                  |
| json_loads               | 28.8 us                                                | 25.7 us: 1.12x faster                                                  |
| regex_v8                 | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                  |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                                  |
| meteor_contest           | 115 ms                                                 | 104 ms: 1.10x faster                                                   |
| json                     | 5.42 ms                                                | 4.94 ms: 1.10x faster                                                  |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                   |
| pathlib                  | 20.0 ms                                                | 18.7 ms: 1.07x faster                                                  |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                                   |
| mdp                      | 2.82 sec                                               | 2.65 sec: 1.06x faster                                                 |
| sqlite_synth             | 2.93 us                                                | 2.77 us: 1.06x faster                                                  |
| regex_dna                | 222 ms                                                 | 211 ms: 1.05x faster                                                   |
| pidigits                 | 190 ms                                                 | 192 ms: 1.01x slower                                                   |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                                  |
| unpickle_list            | 4.82 us                                                | 4.94 us: 1.03x slower                                                  |
| gc_traversal             | 3.84 ms                                                | 3.96 ms: 1.03x slower                                                  |
| async_generators         | 425 ms                                                 | 442 ms: 1.04x slower                                                   |
| unpickle                 | 14.1 us                                                | 14.8 us: 1.05x slower                                                  |
| telco                    | 6.54 ms                                                | 7.24 ms: 1.11x slower                                                  |
| regex_effbot             | 3.23 ms                                                | 3.68 ms: 1.14x slower                                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.70 ms: 1.15x slower                                                  |
| pickle_dict              | 27.3 us                                                | 32.6 us: 1.20x slower                                                  |
| dask                     | 423 ms                                                 | 517 ms: 1.22x slower                                                   |
| coverage                 | 72.8 ms                                                | 93.6 ms: 1.29x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (2): pickle_list, bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x
