
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 730c873
- commit date: 2023-07-01
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-linux-x86_64-python-3.12-3.12.0b3+-730c873 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 267 ms: 1.26x faster                                   |
| docutils       | 3.17 sec                                               | 2.70 sec: 1.17x faster                                 |
| tornado_http   | 127 ms                                                 | 98.6 ms: 1.29x faster                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-linux-x86_64-python-3.12-3.12.0b3+-730c873 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.5 ms: 1.62x faster                                  |
| float          | 111 ms                                                 | 80.5 ms: 1.37x faster                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-linux-x86_64-python-3.12-3.12.0b3+-730c873 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 143 ms: 1.24x faster                                   |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                   |
| regex_v8       | 25.0 ms                                                | 23.0 ms: 1.09x faster                                  |
| regex_effbot   | 3.23 ms                                                | 3.47 ms: 1.08x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-linux-x86_64-python-3.12-3.12.0b3+-730c873 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 310 us: 1.47x faster                                   |
| unpickle_pure_python | 300 us                                                 | 217 us: 1.39x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.82 ms: 1.38x faster                                  |
| tomli_loads          | 2.92 sec                                               | 2.19 sec: 1.33x faster                                 |
| xml_etree_process    | 74.9 ms                                                | 59.8 ms: 1.25x faster                                  |
| json_loads           | 28.8 us                                                | 25.8 us: 1.12x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 85.1 ms: 1.11x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                   |
| pickle_list          | 4.56 us                                                | 4.52 us: 1.01x faster                                  |
| unpickle_list        | 4.82 us                                                | 4.98 us: 1.03x slower                                  |
| pickle               | 10.3 us                                                | 11.0 us: 1.07x slower                                  |
| unpickle             | 14.1 us                                                | 15.2 us: 1.07x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.7 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-linux-x86_64-python-3.12-3.12.0b3+-730c873 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.32 ms: 1.52x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.77 ms: 1.16x slower                                  |
| Geometric mean         | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-linux-x86_64-python-3.12-3.12.0b3+-730c873 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-linux-x86_64-python-3.12-3.12.0b3+-730c873 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 145 us: 3.51x faster                                   |
| generators               | 76.8 ms                                                | 31.6 ms: 2.43x faster                                  |
| deltablue                | 7.42 ms                                                | 3.51 ms: 2.11x faster                                  |
| richards_super           | 90.7 ms                                                | 49.6 ms: 1.83x faster                                  |
| asyncio_tcp              | 925 ms                                                 | 514 ms: 1.80x faster                                   |
| richards                 | 74.9 ms                                                | 43.5 ms: 1.72x faster                                  |
| logging_silent           | 175 ns                                                 | 102 ns: 1.72x faster                                   |
| go                       | 229 ms                                                 | 136 ms: 1.68x faster                                   |
| chaos                    | 106 ms                                                 | 63.4 ms: 1.68x faster                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                 |
| nbody                    | 142 ms                                                 | 87.5 ms: 1.62x faster                                  |
| scimark_sor              | 197 ms                                                 | 124 ms: 1.59x faster                                   |
| raytrace                 | 464 ms                                                 | 293 ms: 1.58x faster                                   |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.55x faster                                  |
| hexiom                   | 9.53 ms                                                | 6.17 ms: 1.54x faster                                  |
| async_tree_io            | 1.77 sec                                               | 1.16 sec: 1.53x faster                                 |
| async_tree_none          | 717 ms                                                 | 471 ms: 1.52x faster                                   |
| python_startup           | 14.2 ms                                                | 9.32 ms: 1.52x faster                                  |
| pyflate                  | 673 ms                                                 | 445 ms: 1.51x faster                                   |
| crypto_pyaes             | 118 ms                                                 | 78.4 ms: 1.51x faster                                  |
| scimark_monte_carlo      | 108 ms                                                 | 71.9 ms: 1.51x faster                                  |
| async_tree_memoization   | 854 ms                                                 | 573 ms: 1.49x faster                                   |
| sqlglot_transpile        | 2.45 ms                                                | 1.64 ms: 1.49x faster                                  |
| pickle_pure_python       | 455 us                                                 | 310 us: 1.47x faster                                   |
| scimark_lu               | 163 ms                                                 | 113 ms: 1.45x faster                                   |
| coroutines               | 31.8 ms                                                | 22.0 ms: 1.44x faster                                  |
| spectral_norm            | 150 ms                                                 | 104 ms: 1.44x faster                                   |
| unpickle_pure_python     | 300 us                                                 | 217 us: 1.39x faster                                   |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                  |
| json_dumps               | 13.5 ms                                                | 9.82 ms: 1.38x faster                                  |
| deepcopy_memo            | 52.3 us                                                | 38.1 us: 1.37x faster                                  |
| float                    | 111 ms                                                 | 80.5 ms: 1.37x faster                                  |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 712 ms: 1.34x faster                                   |
| pprint_pformat           | 1.99 sec                                               | 1.49 sec: 1.34x faster                                 |
| tomli_loads              | 2.92 sec                                               | 2.19 sec: 1.33x faster                                 |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.31x faster                                 |
| comprehensions           | 26.8 us                                                | 20.5 us: 1.31x faster                                  |
| pprint_safe_repr         | 955 ms                                                 | 738 ms: 1.29x faster                                   |
| logging_simple           | 8.07 us                                                | 6.24 us: 1.29x faster                                  |
| logging_format           | 8.91 us                                                | 6.89 us: 1.29x faster                                  |
| tornado_http             | 127 ms                                                 | 98.6 ms: 1.29x faster                                  |
| fannkuch                 | 486 ms                                                 | 385 ms: 1.26x faster                                   |
| 2to3                     | 336 ms                                                 | 267 ms: 1.26x faster                                   |
| unpack_sequence          | 64.7 ns                                                | 51.5 ns: 1.26x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 59.8 ms: 1.25x faster                                  |
| mypy2                    | 428 ms                                                 | 344 ms: 1.25x faster                                   |
| sqlglot_normalize        | 135 ms                                                 | 109 ms: 1.24x faster                                   |
| deepcopy                 | 442 us                                                 | 357 us: 1.24x faster                                   |
| regex_compile            | 177 ms                                                 | 143 ms: 1.24x faster                                   |
| nqueens                  | 100 ms                                                 | 81.4 ms: 1.23x faster                                  |
| sqlglot_optimize         | 65.3 ms                                                | 53.9 ms: 1.21x faster                                  |
| scimark_fft              | 424 ms                                                 | 350 ms: 1.21x faster                                   |
| deepcopy_reduce          | 3.82 us                                                | 3.20 us: 1.19x faster                                  |
| docutils                 | 3.17 sec                                               | 2.70 sec: 1.17x faster                                 |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.4 ms: 1.15x faster                                  |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.75 ms: 1.15x faster                                  |
| sqlalchemy_declarative   | 165 ms                                                 | 145 ms: 1.14x faster                                   |
| bench_thread_pool        | 947 us                                                 | 830 us: 1.14x faster                                   |
| dulwich_log              | 75.9 ms                                                | 67.8 ms: 1.12x faster                                  |
| json_loads               | 28.8 us                                                | 25.8 us: 1.12x faster                                  |
| xml_etree_generate       | 94.2 ms                                                | 85.1 ms: 1.11x faster                                  |
| pathlib                  | 20.0 ms                                                | 18.1 ms: 1.10x faster                                  |
| create_gc_cycles         | 1.67 ms                                                | 1.52 ms: 1.10x faster                                  |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.10x faster                                   |
| regex_dna                | 222 ms                                                 | 203 ms: 1.09x faster                                   |
| json                     | 5.42 ms                                                | 4.96 ms: 1.09x faster                                  |
| regex_v8                 | 25.0 ms                                                | 23.0 ms: 1.09x faster                                  |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                  |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                   |
| mdp                      | 2.82 sec                                               | 2.69 sec: 1.05x faster                                 |
| pickle_list              | 4.56 us                                                | 4.52 us: 1.01x faster                                  |
| unpickle_list            | 4.82 us                                                | 4.98 us: 1.03x slower                                  |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| gc_traversal             | 3.84 ms                                                | 3.99 ms: 1.04x slower                                  |
| async_generators         | 425 ms                                                 | 445 ms: 1.05x slower                                   |
| telco                    | 6.54 ms                                                | 6.88 ms: 1.05x slower                                  |
| pickle                   | 10.3 us                                                | 11.0 us: 1.07x slower                                  |
| unpickle                 | 14.1 us                                                | 15.2 us: 1.07x slower                                  |
| regex_effbot             | 3.23 ms                                                | 3.47 ms: 1.08x slower                                  |
| pickle_dict              | 27.3 us                                                | 30.7 us: 1.13x slower                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.77 ms: 1.16x slower                                  |
| dask                     | 423 ms                                                 | 535 ms: 1.27x slower                                   |
| coverage                 | 72.8 ms                                                | 93.6 ms: 1.29x slower                                  |
| Geometric mean           | (ref)                                                  | 1.28x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x
