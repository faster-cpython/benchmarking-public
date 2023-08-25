
# Results vs. 3.10.4

- fork: brandtbucher
- ref: un_materialize_alt
- machine: linux-x86_64
- commit hash: b2495de
- commit date: 2023-08-05
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.65 sec: 1.19x faster                                                    |
| tornado_http   | 127 ms                                                 | 95.0 ms: 1.34x faster                                                     |
| Geometric mean | (ref)                                                  | 1.27x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.2 ms: 1.59x faster                                                     |
| float          | 111 ms                                                 | 80.2 ms: 1.38x faster                                                     |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                     |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.53 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 296 us: 1.54x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 215 us: 1.40x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.78 ms: 1.38x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 58.0 ms: 1.29x faster                                                     |
| tomli_loads          | 2.92 sec                                               | 2.31 sec: 1.26x faster                                                    |
| xml_etree_generate   | 94.2 ms                                                | 83.4 ms: 1.13x faster                                                     |
| json_loads           | 28.8 us                                                | 25.6 us: 1.13x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                      |
| unpickle_list        | 4.82 us                                                | 4.91 us: 1.02x slower                                                     |
| pickle_list          | 4.56 us                                                | 4.66 us: 1.02x slower                                                     |
| pickle               | 10.3 us                                                | 10.8 us: 1.05x slower                                                     |
| unpickle             | 14.1 us                                                | 15.3 us: 1.08x slower                                                     |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.43 ms: 1.50x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.89 ms: 1.19x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.37x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 143 us: 3.57x faster                                                      |
| generators               | 76.8 ms                                                | 28.1 ms: 2.73x faster                                                     |
| deltablue                | 7.42 ms                                                | 3.23 ms: 2.30x faster                                                     |
| asyncio_tcp              | 925 ms                                                 | 485 ms: 1.91x faster                                                      |
| chaos                    | 106 ms                                                 | 59.3 ms: 1.79x faster                                                     |
| logging_silent           | 175 ns                                                 | 101 ns: 1.73x faster                                                      |
| crypto_pyaes             | 118 ms                                                 | 69.9 ms: 1.70x faster                                                     |
| raytrace                 | 464 ms                                                 | 275 ms: 1.69x faster                                                      |
| richards_super           | 90.7 ms                                                | 53.9 ms: 1.68x faster                                                     |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                    |
| go                       | 229 ms                                                 | 138 ms: 1.66x faster                                                      |
| scimark_sor              | 197 ms                                                 | 120 ms: 1.64x faster                                                      |
| sqlglot_parse            | 2.06 ms                                                | 1.29 ms: 1.59x faster                                                     |
| nbody                    | 142 ms                                                 | 89.2 ms: 1.59x faster                                                     |
| scimark_monte_carlo      | 108 ms                                                 | 68.5 ms: 1.58x faster                                                     |
| hexiom                   | 9.53 ms                                                | 6.03 ms: 1.58x faster                                                     |
| richards                 | 74.9 ms                                                | 48.2 ms: 1.56x faster                                                     |
| pickle_pure_python       | 455 us                                                 | 296 us: 1.54x faster                                                      |
| sqlglot_transpile        | 2.45 ms                                                | 1.61 ms: 1.52x faster                                                     |
| pyflate                  | 673 ms                                                 | 443 ms: 1.52x faster                                                      |
| python_startup           | 14.2 ms                                                | 9.43 ms: 1.50x faster                                                     |
| coroutines               | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                     |
| async_tree_none          | 717 ms                                                 | 483 ms: 1.48x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.48x faster                                                    |
| scimark_lu               | 163 ms                                                 | 112 ms: 1.46x faster                                                      |
| async_tree_memoization   | 854 ms                                                 | 585 ms: 1.46x faster                                                      |
| spectral_norm            | 150 ms                                                 | 106 ms: 1.41x faster                                                      |
| unpickle_pure_python     | 300 us                                                 | 215 us: 1.40x faster                                                      |
| deepcopy_memo            | 52.3 us                                                | 37.6 us: 1.39x faster                                                     |
| json_dumps               | 13.5 ms                                                | 9.78 ms: 1.38x faster                                                     |
| logging_format           | 8.91 us                                                | 6.44 us: 1.38x faster                                                     |
| float                    | 111 ms                                                 | 80.2 ms: 1.38x faster                                                     |
| logging_simple           | 8.07 us                                                | 5.86 us: 1.38x faster                                                     |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.37x faster                                                     |
| unpack_sequence          | 64.7 ns                                                | 47.6 ns: 1.36x faster                                                     |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                                    |
| tornado_http             | 127 ms                                                 | 95.0 ms: 1.34x faster                                                     |
| pprint_safe_repr         | 955 ms                                                 | 715 ms: 1.34x faster                                                      |
| comprehensions           | 26.8 us                                                | 20.2 us: 1.33x faster                                                     |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 723 ms: 1.32x faster                                                      |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                    |
| sqlglot_normalize        | 135 ms                                                 | 104 ms: 1.30x faster                                                      |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                                      |
| xml_etree_process        | 74.9 ms                                                | 58.0 ms: 1.29x faster                                                     |
| nqueens                  | 100 ms                                                 | 79.2 ms: 1.26x faster                                                     |
| tomli_loads              | 2.92 sec                                               | 2.31 sec: 1.26x faster                                                    |
| fannkuch                 | 486 ms                                                 | 386 ms: 1.26x faster                                                      |
| sqlglot_optimize         | 65.3 ms                                                | 52.6 ms: 1.24x faster                                                     |
| deepcopy                 | 442 us                                                 | 358 us: 1.24x faster                                                      |
| docutils                 | 3.17 sec                                               | 2.65 sec: 1.19x faster                                                    |
| deepcopy_reduce          | 3.82 us                                                | 3.21 us: 1.19x faster                                                     |
| scimark_fft              | 424 ms                                                 | 356 ms: 1.19x faster                                                      |
| bench_thread_pool        | 947 us                                                 | 820 us: 1.15x faster                                                      |
| dulwich_log              | 75.9 ms                                                | 66.2 ms: 1.15x faster                                                     |
| xml_etree_generate       | 94.2 ms                                                | 83.4 ms: 1.13x faster                                                     |
| json_loads               | 28.8 us                                                | 25.6 us: 1.13x faster                                                     |
| json                     | 5.42 ms                                                | 4.83 ms: 1.12x faster                                                     |
| regex_v8                 | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                     |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.91 ms: 1.11x faster                                                     |
| mdp                      | 2.82 sec                                               | 2.54 sec: 1.11x faster                                                    |
| create_gc_cycles         | 1.67 ms                                                | 1.52 ms: 1.10x faster                                                     |
| regex_dna                | 222 ms                                                 | 203 ms: 1.09x faster                                                      |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                      |
| sqlite_synth             | 2.93 us                                                | 2.71 us: 1.08x faster                                                     |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                                      |
| pathlib                  | 20.0 ms                                                | 18.8 ms: 1.07x faster                                                     |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                                      |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                                      |
| unpickle_list            | 4.82 us                                                | 4.91 us: 1.02x slower                                                     |
| pickle_list              | 4.56 us                                                | 4.66 us: 1.02x slower                                                     |
| pickle                   | 10.3 us                                                | 10.8 us: 1.05x slower                                                     |
| async_generators         | 425 ms                                                 | 447 ms: 1.05x slower                                                      |
| unpickle                 | 14.1 us                                                | 15.3 us: 1.08x slower                                                     |
| regex_effbot             | 3.23 ms                                                | 3.53 ms: 1.09x slower                                                     |
| gc_traversal             | 3.84 ms                                                | 4.34 ms: 1.13x slower                                                     |
| pickle_dict              | 27.3 us                                                | 31.6 us: 1.16x slower                                                     |
| python_startup_no_site   | 5.82 ms                                                | 6.89 ms: 1.19x slower                                                     |
| telco                    | 6.54 ms                                                | 7.97 ms: 1.22x slower                                                     |
| dask                     | 423 ms                                                 | 516 ms: 1.22x slower                                                      |
| coverage                 | 72.8 ms                                                | 93.3 ms: 1.28x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                              |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x
