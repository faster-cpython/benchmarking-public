
# Results vs. 3.10.4

- fork: python
- ref: 14fbd4e6b16dcbcbff44
- machine: linux-x86_64
- commit hash: 14fbd4e
- commit date: 2023-08-03
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.65 sec: 1.20x faster                                                |
| tornado_http   | 127 ms                                                 | 95.3 ms: 1.34x faster                                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.4 ms: 1.53x faster                                                 |
| float          | 111 ms                                                 | 80.5 ms: 1.37x faster                                                 |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                                  |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                 |
| regex_dna      | 222 ms                                                 | 211 ms: 1.05x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 3.51 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 294 us: 1.55x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 212 us: 1.42x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.87 ms: 1.37x faster                                                 |
| xml_etree_process    | 74.9 ms                                                | 57.7 ms: 1.30x faster                                                 |
| tomli_loads          | 2.92 sec                                               | 2.33 sec: 1.25x faster                                                |
| xml_etree_generate   | 94.2 ms                                                | 83.3 ms: 1.13x faster                                                 |
| json_loads           | 28.8 us                                                | 26.1 us: 1.10x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                                  |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                                 |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.03x slower                                                 |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                                 |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.33 ms: 1.52x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.83 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 11.0 ms: 1.34x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 144 us: 3.54x faster                                                  |
| generators               | 76.8 ms                                                | 28.2 ms: 2.73x faster                                                 |
| deltablue                | 7.42 ms                                                | 3.28 ms: 2.26x faster                                                 |
| asyncio_tcp              | 925 ms                                                 | 484 ms: 1.91x faster                                                  |
| chaos                    | 106 ms                                                 | 59.2 ms: 1.79x faster                                                 |
| crypto_pyaes             | 118 ms                                                 | 68.7 ms: 1.72x faster                                                 |
| raytrace                 | 464 ms                                                 | 272 ms: 1.70x faster                                                  |
| go                       | 229 ms                                                 | 137 ms: 1.68x faster                                                  |
| richards_super           | 90.7 ms                                                | 54.1 ms: 1.68x faster                                                 |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                |
| logging_silent           | 175 ns                                                 | 106 ns: 1.66x faster                                                  |
| scimark_sor              | 197 ms                                                 | 121 ms: 1.62x faster                                                  |
| sqlglot_parse            | 2.06 ms                                                | 1.29 ms: 1.60x faster                                                 |
| scimark_monte_carlo      | 108 ms                                                 | 68.1 ms: 1.59x faster                                                 |
| hexiom                   | 9.53 ms                                                | 6.01 ms: 1.58x faster                                                 |
| richards                 | 74.9 ms                                                | 47.5 ms: 1.58x faster                                                 |
| pickle_pure_python       | 455 us                                                 | 294 us: 1.55x faster                                                  |
| nbody                    | 142 ms                                                 | 92.4 ms: 1.53x faster                                                 |
| sqlglot_transpile        | 2.45 ms                                                | 1.60 ms: 1.53x faster                                                 |
| python_startup           | 14.2 ms                                                | 9.33 ms: 1.52x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.50x faster                                                |
| pyflate                  | 673 ms                                                 | 450 ms: 1.50x faster                                                  |
| async_tree_none          | 717 ms                                                 | 480 ms: 1.49x faster                                                  |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.48x faster                                                  |
| coroutines               | 31.8 ms                                                | 21.7 ms: 1.47x faster                                                 |
| async_tree_memoization   | 854 ms                                                 | 584 ms: 1.46x faster                                                  |
| spectral_norm            | 150 ms                                                 | 106 ms: 1.42x faster                                                  |
| unpickle_pure_python     | 300 us                                                 | 212 us: 1.42x faster                                                  |
| logging_format           | 8.91 us                                                | 6.48 us: 1.38x faster                                                 |
| float                    | 111 ms                                                 | 80.5 ms: 1.37x faster                                                 |
| json_dumps               | 13.5 ms                                                | 9.87 ms: 1.37x faster                                                 |
| deepcopy_memo            | 52.3 us                                                | 38.5 us: 1.36x faster                                                 |
| logging_simple           | 8.07 us                                                | 5.96 us: 1.35x faster                                                 |
| unpack_sequence          | 64.7 ns                                                | 48.0 ns: 1.35x faster                                                 |
| mako                     | 14.8 ms                                                | 11.0 ms: 1.34x faster                                                 |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.34x faster                                                |
| tornado_http             | 127 ms                                                 | 95.3 ms: 1.34x faster                                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 719 ms: 1.32x faster                                                  |
| comprehensions           | 26.8 us                                                | 20.3 us: 1.32x faster                                                 |
| pprint_safe_repr         | 955 ms                                                 | 724 ms: 1.32x faster                                                  |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                |
| xml_etree_process        | 74.9 ms                                                | 57.7 ms: 1.30x faster                                                 |
| sqlglot_normalize        | 135 ms                                                 | 104 ms: 1.30x faster                                                  |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                                  |
| mypy2                    | 428 ms                                                 | 336 ms: 1.27x faster                                                  |
| nqueens                  | 100 ms                                                 | 79.5 ms: 1.26x faster                                                 |
| tomli_loads              | 2.92 sec                                               | 2.33 sec: 1.25x faster                                                |
| deepcopy                 | 442 us                                                 | 355 us: 1.24x faster                                                  |
| sqlglot_optimize         | 65.3 ms                                                | 52.6 ms: 1.24x faster                                                 |
| fannkuch                 | 486 ms                                                 | 394 ms: 1.23x faster                                                  |
| docutils                 | 3.17 sec                                               | 2.65 sec: 1.20x faster                                                |
| deepcopy_reduce          | 3.82 us                                                | 3.19 us: 1.20x faster                                                 |
| scimark_fft              | 424 ms                                                 | 366 ms: 1.16x faster                                                  |
| dulwich_log              | 75.9 ms                                                | 65.9 ms: 1.15x faster                                                 |
| bench_thread_pool        | 947 us                                                 | 825 us: 1.15x faster                                                  |
| xml_etree_generate       | 94.2 ms                                                | 83.3 ms: 1.13x faster                                                 |
| create_gc_cycles         | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                 |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.85 ms: 1.12x faster                                                 |
| regex_v8                 | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                 |
| json                     | 5.42 ms                                                | 4.90 ms: 1.11x faster                                                 |
| json_loads               | 28.8 us                                                | 26.1 us: 1.10x faster                                                 |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.10x faster                                                  |
| pathlib                  | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                 |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                  |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                                  |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                                 |
| mdp                      | 2.82 sec                                               | 2.66 sec: 1.06x faster                                                |
| regex_dna                | 222 ms                                                 | 211 ms: 1.05x faster                                                  |
| gc_traversal             | 3.84 ms                                                | 3.66 ms: 1.05x faster                                                 |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                 |
| pickle                   | 10.3 us                                                | 10.4 us: 1.01x slower                                                 |
| unpickle_list            | 4.82 us                                                | 4.99 us: 1.03x slower                                                 |
| async_generators         | 425 ms                                                 | 444 ms: 1.04x slower                                                  |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                                  |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                                 |
| regex_effbot             | 3.23 ms                                                | 3.51 ms: 1.09x slower                                                 |
| pickle_dict              | 27.3 us                                                | 31.6 us: 1.16x slower                                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.83 ms: 1.17x slower                                                 |
| telco                    | 6.54 ms                                                | 7.84 ms: 1.20x slower                                                 |
| dask                     | 423 ms                                                 | 520 ms: 1.23x slower                                                  |
| coverage                 | 72.8 ms                                                | 92.9 ms: 1.28x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x
