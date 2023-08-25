
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0b3
- machine: linux-x86_64
- commit hash: f992a60
- commit date: 2023-06-19
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 267 ms: 1.26x faster                                       |
| docutils       | 3.17 sec                                               | 2.72 sec: 1.17x faster                                     |
| tornado_http   | 127 ms                                                 | 99.3 ms: 1.28x faster                                      |
| Geometric mean | (ref)                                                  | 1.23x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 142 ms                                                 | 94.3 ms: 1.50x faster                                      |
| float          | 111 ms                                                 | 80.4 ms: 1.37x faster                                      |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                  | 1.26x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 144 ms: 1.23x faster                                       |
| regex_dna      | 222 ms                                                 | 200 ms: 1.11x faster                                       |
| regex_v8       | 25.0 ms                                                | 22.9 ms: 1.09x faster                                      |
| regex_effbot   | 3.23 ms                                                | 3.56 ms: 1.10x slower                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 312 us: 1.46x faster                                       |
| unpickle_pure_python | 300 us                                                 | 215 us: 1.40x faster                                       |
| json_dumps           | 13.5 ms                                                | 9.79 ms: 1.38x faster                                      |
| tomli_loads          | 2.92 sec                                               | 2.17 sec: 1.35x faster                                     |
| xml_etree_process    | 74.9 ms                                                | 59.2 ms: 1.27x faster                                      |
| json_loads           | 28.8 us                                                | 25.0 us: 1.15x faster                                      |
| xml_etree_generate   | 94.2 ms                                                | 85.4 ms: 1.10x faster                                      |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                       |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.08x faster                                       |
| pickle_list          | 4.56 us                                                | 4.49 us: 1.01x faster                                      |
| unpickle_list        | 4.82 us                                                | 4.96 us: 1.03x slower                                      |
| unpickle             | 14.1 us                                                | 14.9 us: 1.05x slower                                      |
| pickle               | 10.3 us                                                | 11.0 us: 1.06x slower                                      |
| pickle_dict          | 27.3 us                                                | 31.8 us: 1.17x slower                                      |
| Geometric mean       | (ref)                                                  | 1.13x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.28 ms: 1.52x faster                                      |
| python_startup_no_site | 5.82 ms                                                | 6.74 ms: 1.16x slower                                      |
| Geometric mean         | (ref)                                                  | 1.15x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.39x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.50x faster                                       |
| generators               | 76.8 ms                                                | 30.3 ms: 2.53x faster                                      |
| deltablue                | 7.42 ms                                                | 3.50 ms: 2.12x faster                                      |
| richards_super           | 90.7 ms                                                | 49.2 ms: 1.84x faster                                      |
| asyncio_tcp              | 925 ms                                                 | 513 ms: 1.80x faster                                       |
| logging_silent           | 175 ns                                                 | 99.7 ns: 1.76x faster                                      |
| richards                 | 74.9 ms                                                | 43.8 ms: 1.71x faster                                      |
| go                       | 229 ms                                                 | 137 ms: 1.68x faster                                       |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                     |
| chaos                    | 106 ms                                                 | 63.8 ms: 1.66x faster                                      |
| scimark_sor              | 197 ms                                                 | 124 ms: 1.59x faster                                       |
| raytrace                 | 464 ms                                                 | 298 ms: 1.56x faster                                       |
| hexiom                   | 9.53 ms                                                | 6.13 ms: 1.55x faster                                      |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.55x faster                                      |
| async_tree_io            | 1.77 sec                                               | 1.16 sec: 1.53x faster                                     |
| async_tree_none          | 717 ms                                                 | 469 ms: 1.53x faster                                       |
| python_startup           | 14.2 ms                                                | 9.28 ms: 1.52x faster                                      |
| scimark_monte_carlo      | 108 ms                                                 | 71.2 ms: 1.52x faster                                      |
| crypto_pyaes             | 118 ms                                                 | 78.1 ms: 1.52x faster                                      |
| nbody                    | 142 ms                                                 | 94.3 ms: 1.50x faster                                      |
| sqlglot_transpile        | 2.45 ms                                                | 1.64 ms: 1.49x faster                                      |
| async_tree_memoization   | 854 ms                                                 | 575 ms: 1.49x faster                                       |
| pyflate                  | 673 ms                                                 | 453 ms: 1.49x faster                                       |
| pickle_pure_python       | 455 us                                                 | 312 us: 1.46x faster                                       |
| scimark_lu               | 163 ms                                                 | 112 ms: 1.45x faster                                       |
| coroutines               | 31.8 ms                                                | 22.2 ms: 1.44x faster                                      |
| spectral_norm            | 150 ms                                                 | 106 ms: 1.41x faster                                       |
| unpickle_pure_python     | 300 us                                                 | 215 us: 1.40x faster                                       |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.39x faster                                      |
| json_dumps               | 13.5 ms                                                | 9.79 ms: 1.38x faster                                      |
| float                    | 111 ms                                                 | 80.4 ms: 1.37x faster                                      |
| deepcopy_memo            | 52.3 us                                                | 38.3 us: 1.37x faster                                      |
| unpack_sequence          | 64.7 ns                                                | 47.4 ns: 1.37x faster                                      |
| tomli_loads              | 2.92 sec                                               | 2.17 sec: 1.35x faster                                     |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 713 ms: 1.33x faster                                       |
| pprint_pformat           | 1.99 sec                                               | 1.50 sec: 1.32x faster                                     |
| pprint_safe_repr         | 955 ms                                                 | 734 ms: 1.30x faster                                       |
| pycparser                | 1.50 sec                                               | 1.16 sec: 1.30x faster                                     |
| comprehensions           | 26.8 us                                                | 20.7 us: 1.29x faster                                      |
| logging_simple           | 8.07 us                                                | 6.25 us: 1.29x faster                                      |
| tornado_http             | 127 ms                                                 | 99.3 ms: 1.28x faster                                      |
| logging_format           | 8.91 us                                                | 6.99 us: 1.27x faster                                      |
| xml_etree_process        | 74.9 ms                                                | 59.2 ms: 1.27x faster                                      |
| 2to3                     | 336 ms                                                 | 267 ms: 1.26x faster                                       |
| fannkuch                 | 486 ms                                                 | 387 ms: 1.25x faster                                       |
| sqlglot_normalize        | 135 ms                                                 | 109 ms: 1.25x faster                                       |
| nqueens                  | 100 ms                                                 | 80.5 ms: 1.24x faster                                      |
| deepcopy                 | 442 us                                                 | 359 us: 1.23x faster                                       |
| regex_compile            | 177 ms                                                 | 144 ms: 1.23x faster                                       |
| deepcopy_reduce          | 3.82 us                                                | 3.12 us: 1.22x faster                                      |
| sqlglot_optimize         | 65.3 ms                                                | 53.5 ms: 1.22x faster                                      |
| scimark_fft              | 424 ms                                                 | 358 ms: 1.18x faster                                       |
| docutils                 | 3.17 sec                                               | 2.72 sec: 1.17x faster                                     |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.4 ms: 1.15x faster                                      |
| json_loads               | 28.8 us                                                | 25.0 us: 1.15x faster                                      |
| bench_thread_pool        | 947 us                                                 | 827 us: 1.15x faster                                       |
| sqlalchemy_declarative   | 165 ms                                                 | 145 ms: 1.14x faster                                       |
| json                     | 5.42 ms                                                | 4.74 ms: 1.14x faster                                      |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.88 ms: 1.12x faster                                      |
| dulwich_log              | 75.9 ms                                                | 67.9 ms: 1.12x faster                                      |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.11x faster                                      |
| regex_dna                | 222 ms                                                 | 200 ms: 1.11x faster                                       |
| xml_etree_generate       | 94.2 ms                                                | 85.4 ms: 1.10x faster                                      |
| pathlib                  | 20.0 ms                                                | 18.2 ms: 1.10x faster                                      |
| regex_v8                 | 25.0 ms                                                | 22.9 ms: 1.09x faster                                      |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                       |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                       |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.08x faster                                       |
| mdp                      | 2.82 sec                                               | 2.64 sec: 1.07x faster                                     |
| sqlite_synth             | 2.93 us                                                | 2.75 us: 1.07x faster                                      |
| pickle_list              | 4.56 us                                                | 4.49 us: 1.01x faster                                      |
| unpickle_list            | 4.82 us                                                | 4.96 us: 1.03x slower                                      |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                       |
| telco                    | 6.54 ms                                                | 6.82 ms: 1.04x slower                                      |
| async_generators         | 425 ms                                                 | 444 ms: 1.04x slower                                       |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.05x slower                                      |
| gc_traversal             | 3.84 ms                                                | 4.07 ms: 1.06x slower                                      |
| pickle                   | 10.3 us                                                | 11.0 us: 1.06x slower                                      |
| regex_effbot             | 3.23 ms                                                | 3.56 ms: 1.10x slower                                      |
| python_startup_no_site   | 5.82 ms                                                | 6.74 ms: 1.16x slower                                      |
| pickle_dict              | 27.3 us                                                | 31.8 us: 1.17x slower                                      |
| dask                     | 423 ms                                                 | 536 ms: 1.27x slower                                       |
| coverage                 | 72.8 ms                                                | 95.0 ms: 1.30x slower                                      |
| Geometric mean           | (ref)                                                  | 1.28x faster                                               |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x
