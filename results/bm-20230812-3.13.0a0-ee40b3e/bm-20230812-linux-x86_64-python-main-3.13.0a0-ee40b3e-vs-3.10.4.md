
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: ee40b3e
- commit date: 2023-08-12
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-python-main-3.13.0a0-ee40b3e |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.63 sec: 1.21x faster                                |
| tornado_http   | 127 ms                                                 | 95.5 ms: 1.33x faster                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-python-main-3.13.0a0-ee40b3e |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 142 ms                                                 | 91.8 ms: 1.54x faster                                 |
| float          | 111 ms                                                 | 80.0 ms: 1.38x faster                                 |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-python-main-3.13.0a0-ee40b3e |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                  |
| regex_v8       | 25.0 ms                                                | 23.2 ms: 1.08x faster                                 |
| regex_dna      | 222 ms                                                 | 214 ms: 1.03x faster                                  |
| regex_effbot   | 3.23 ms                                                | 3.63 ms: 1.12x slower                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-python-main-3.13.0a0-ee40b3e |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 304 us: 1.50x faster                                  |
| json_dumps           | 13.5 ms                                                | 9.75 ms: 1.39x faster                                 |
| unpickle_pure_python | 300 us                                                 | 217 us: 1.38x faster                                  |
| tomli_loads          | 2.92 sec                                               | 2.11 sec: 1.38x faster                                |
| xml_etree_process    | 74.9 ms                                                | 57.4 ms: 1.31x faster                                 |
| xml_etree_generate   | 94.2 ms                                                | 82.8 ms: 1.14x faster                                 |
| json_loads           | 28.8 us                                                | 25.4 us: 1.13x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 155 ms: 1.05x faster                                  |
| unpickle_list        | 4.82 us                                                | 4.92 us: 1.02x slower                                 |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                 |
| unpickle             | 14.1 us                                                | 14.9 us: 1.06x slower                                 |
| pickle_list          | 4.56 us                                                | 4.87 us: 1.07x slower                                 |
| pickle_dict          | 27.3 us                                                | 32.1 us: 1.18x slower                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-python-main-3.13.0a0-ee40b3e |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.39 ms: 1.51x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 6.87 ms: 1.18x slower                                 |
| Geometric mean         | (ref)                                                  | 1.13x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-python-main-3.13.0a0-ee40b3e |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.35x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-python-main-3.13.0a0-ee40b3e |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 144 us: 3.53x faster                                  |
| generators               | 76.8 ms                                                | 28.3 ms: 2.71x faster                                 |
| deltablue                | 7.42 ms                                                | 3.30 ms: 2.25x faster                                 |
| asyncio_tcp              | 925 ms                                                 | 486 ms: 1.91x faster                                  |
| chaos                    | 106 ms                                                 | 60.1 ms: 1.77x faster                                 |
| richards_super           | 90.7 ms                                                | 53.1 ms: 1.71x faster                                 |
| raytrace                 | 464 ms                                                 | 273 ms: 1.70x faster                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                |
| logging_silent           | 175 ns                                                 | 104 ns: 1.68x faster                                  |
| crypto_pyaes             | 118 ms                                                 | 71.0 ms: 1.67x faster                                 |
| async_tree_none          | 717 ms                                                 | 435 ms: 1.65x faster                                  |
| go                       | 229 ms                                                 | 139 ms: 1.64x faster                                  |
| sqlglot_parse            | 2.06 ms                                                | 1.27 ms: 1.62x faster                                 |
| scimark_monte_carlo      | 108 ms                                                 | 67.4 ms: 1.61x faster                                 |
| scimark_sor              | 197 ms                                                 | 124 ms: 1.59x faster                                  |
| richards                 | 74.9 ms                                                | 47.3 ms: 1.58x faster                                 |
| hexiom                   | 9.53 ms                                                | 6.11 ms: 1.56x faster                                 |
| nbody                    | 142 ms                                                 | 91.8 ms: 1.54x faster                                 |
| sqlglot_transpile        | 2.45 ms                                                | 1.60 ms: 1.53x faster                                 |
| async_tree_memoization   | 854 ms                                                 | 564 ms: 1.52x faster                                  |
| pyflate                  | 673 ms                                                 | 446 ms: 1.51x faster                                  |
| python_startup           | 14.2 ms                                                | 9.39 ms: 1.51x faster                                 |
| pickle_pure_python       | 455 us                                                 | 304 us: 1.50x faster                                  |
| async_tree_io            | 1.77 sec                                               | 1.18 sec: 1.50x faster                                |
| scimark_lu               | 163 ms                                                 | 109 ms: 1.49x faster                                  |
| coroutines               | 31.8 ms                                                | 21.9 ms: 1.46x faster                                 |
| spectral_norm            | 150 ms                                                 | 105 ms: 1.43x faster                                  |
| json_dumps               | 13.5 ms                                                | 9.75 ms: 1.39x faster                                 |
| unpickle_pure_python     | 300 us                                                 | 217 us: 1.38x faster                                  |
| float                    | 111 ms                                                 | 80.0 ms: 1.38x faster                                 |
| tomli_loads              | 2.92 sec                                               | 2.11 sec: 1.38x faster                                |
| unpack_sequence          | 64.7 ns                                                | 46.9 ns: 1.38x faster                                 |
| logging_simple           | 8.07 us                                                | 5.88 us: 1.37x faster                                 |
| logging_format           | 8.91 us                                                | 6.53 us: 1.36x faster                                 |
| deepcopy_memo            | 52.3 us                                                | 38.5 us: 1.36x faster                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 699 ms: 1.36x faster                                  |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.35x faster                                 |
| tornado_http             | 127 ms                                                 | 95.5 ms: 1.33x faster                                 |
| pprint_pformat           | 1.99 sec                                               | 1.49 sec: 1.33x faster                                |
| pprint_safe_repr         | 955 ms                                                 | 728 ms: 1.31x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 57.4 ms: 1.31x faster                                 |
| comprehensions           | 26.8 us                                                | 20.7 us: 1.30x faster                                 |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                  |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.29x faster                                  |
| pycparser                | 1.50 sec                                               | 1.17 sec: 1.28x faster                                |
| fannkuch                 | 486 ms                                                 | 386 ms: 1.26x faster                                  |
| deepcopy                 | 442 us                                                 | 354 us: 1.25x faster                                  |
| sqlglot_optimize         | 65.3 ms                                                | 52.8 ms: 1.24x faster                                 |
| nqueens                  | 100 ms                                                 | 81.9 ms: 1.22x faster                                 |
| docutils                 | 3.17 sec                                               | 2.63 sec: 1.21x faster                                |
| scimark_fft              | 424 ms                                                 | 353 ms: 1.20x faster                                  |
| deepcopy_reduce          | 3.82 us                                                | 3.19 us: 1.20x faster                                 |
| bench_thread_pool        | 947 us                                                 | 819 us: 1.16x faster                                  |
| dulwich_log              | 75.9 ms                                                | 66.1 ms: 1.15x faster                                 |
| xml_etree_generate       | 94.2 ms                                                | 82.8 ms: 1.14x faster                                 |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.80 ms: 1.14x faster                                 |
| json_loads               | 28.8 us                                                | 25.4 us: 1.13x faster                                 |
| create_gc_cycles         | 1.67 ms                                                | 1.48 ms: 1.13x faster                                 |
| json                     | 5.42 ms                                                | 4.89 ms: 1.11x faster                                 |
| mdp                      | 2.82 sec                                               | 2.55 sec: 1.10x faster                                |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                  |
| regex_v8                 | 25.0 ms                                                | 23.2 ms: 1.08x faster                                 |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                  |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                 |
| pathlib                  | 20.0 ms                                                | 18.8 ms: 1.07x faster                                 |
| xml_etree_parse          | 163 ms                                                 | 155 ms: 1.05x faster                                  |
| regex_dna                | 222 ms                                                 | 214 ms: 1.03x faster                                  |
| gc_traversal             | 3.84 ms                                                | 3.80 ms: 1.01x faster                                 |
| unpickle_list            | 4.82 us                                                | 4.92 us: 1.02x slower                                 |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                 |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.06x slower                                 |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                  |
| async_generators         | 425 ms                                                 | 454 ms: 1.07x slower                                  |
| pickle_list              | 4.56 us                                                | 4.87 us: 1.07x slower                                 |
| regex_effbot             | 3.23 ms                                                | 3.63 ms: 1.12x slower                                 |
| coverage                 | 72.8 ms                                                | 85.2 ms: 1.17x slower                                 |
| pickle_dict              | 27.3 us                                                | 32.1 us: 1.18x slower                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.87 ms: 1.18x slower                                 |
| telco                    | 6.54 ms                                                | 8.12 ms: 1.24x slower                                 |
| dask                     | 423 ms                                                 | 526 ms: 1.25x slower                                  |
| Geometric mean           | (ref)                                                  | 1.29x faster                                          |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x
