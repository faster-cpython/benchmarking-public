
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 60ade0c
- commit date: 2023-07-08
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-linux-x86_64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 267 ms: 1.26x faster                                   |
| docutils       | 3.17 sec                                               | 2.71 sec: 1.17x faster                                 |
| tornado_http   | 127 ms                                                 | 99.3 ms: 1.28x faster                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-linux-x86_64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.9 ms: 1.59x faster                                  |
| float          | 111 ms                                                 | 80.3 ms: 1.38x faster                                  |
| pidigits       | 190 ms                                                 | 196 ms: 1.03x slower                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-linux-x86_64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                   |
| regex_dna      | 222 ms                                                 | 202 ms: 1.10x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.8 ms: 1.10x faster                                  |
| regex_effbot   | 3.23 ms                                                | 3.66 ms: 1.14x slower                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-linux-x86_64-python-3.12-3.12.0b3+-60ade0c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 310 us: 1.47x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.69 ms: 1.40x faster                                  |
| unpickle_pure_python | 300 us                                                 | 217 us: 1.38x faster                                   |
| tomli_loads          | 2.92 sec                                               | 2.21 sec: 1.32x faster                                 |
| xml_etree_process    | 74.9 ms                                                | 59.2 ms: 1.27x faster                                  |
| json_loads           | 28.8 us                                                | 25.6 us: 1.13x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 84.9 ms: 1.11x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.06x faster                                   |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                  |
| unpickle_list        | 4.82 us                                                | 5.05 us: 1.05x slower                                  |
| unpickle             | 14.1 us                                                | 15.2 us: 1.08x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.5 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-linux-x86_64-python-3.12-3.12.0b3+-60ade0c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.30 ms: 1.52x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.76 ms: 1.16x slower                                  |
| Geometric mean         | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-linux-x86_64-python-3.12-3.12.0b3+-60ade0c |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.37x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-linux-x86_64-python-3.12-3.12.0b3+-60ade0c |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 150 us: 3.41x faster                                   |
| generators               | 76.8 ms                                                | 30.7 ms: 2.50x faster                                  |
| deltablue                | 7.42 ms                                                | 3.50 ms: 2.12x faster                                  |
| richards_super           | 90.7 ms                                                | 49.8 ms: 1.82x faster                                  |
| asyncio_tcp              | 925 ms                                                 | 513 ms: 1.80x faster                                   |
| go                       | 229 ms                                                 | 136 ms: 1.68x faster                                   |
| richards                 | 74.9 ms                                                | 44.6 ms: 1.68x faster                                  |
| chaos                    | 106 ms                                                 | 63.4 ms: 1.68x faster                                  |
| logging_silent           | 175 ns                                                 | 105 ns: 1.67x faster                                   |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                 |
| scimark_sor              | 197 ms                                                 | 121 ms: 1.63x faster                                   |
| nbody                    | 142 ms                                                 | 88.9 ms: 1.59x faster                                  |
| raytrace                 | 464 ms                                                 | 299 ms: 1.55x faster                                   |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.55x faster                                  |
| async_tree_io            | 1.77 sec                                               | 1.16 sec: 1.54x faster                                 |
| scimark_monte_carlo      | 108 ms                                                 | 70.6 ms: 1.53x faster                                  |
| hexiom                   | 9.53 ms                                                | 6.23 ms: 1.53x faster                                  |
| pyflate                  | 673 ms                                                 | 442 ms: 1.52x faster                                   |
| python_startup           | 14.2 ms                                                | 9.30 ms: 1.52x faster                                  |
| crypto_pyaes             | 118 ms                                                 | 78.0 ms: 1.52x faster                                  |
| async_tree_none          | 717 ms                                                 | 472 ms: 1.52x faster                                   |
| async_tree_memoization   | 854 ms                                                 | 574 ms: 1.49x faster                                   |
| sqlglot_transpile        | 2.45 ms                                                | 1.65 ms: 1.48x faster                                  |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.47x faster                                   |
| pickle_pure_python       | 455 us                                                 | 310 us: 1.47x faster                                   |
| spectral_norm            | 150 ms                                                 | 105 ms: 1.42x faster                                   |
| coroutines               | 31.8 ms                                                | 22.7 ms: 1.40x faster                                  |
| json_dumps               | 13.5 ms                                                | 9.69 ms: 1.40x faster                                  |
| deepcopy_memo            | 52.3 us                                                | 37.6 us: 1.39x faster                                  |
| unpickle_pure_python     | 300 us                                                 | 217 us: 1.38x faster                                   |
| float                    | 111 ms                                                 | 80.3 ms: 1.38x faster                                  |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.37x faster                                  |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 713 ms: 1.33x faster                                   |
| tomli_loads              | 2.92 sec                                               | 2.21 sec: 1.32x faster                                 |
| pprint_pformat           | 1.99 sec                                               | 1.51 sec: 1.32x faster                                 |
| logging_simple           | 8.07 us                                                | 6.17 us: 1.31x faster                                  |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.30x faster                                 |
| comprehensions           | 26.8 us                                                | 20.8 us: 1.29x faster                                  |
| pprint_safe_repr         | 955 ms                                                 | 740 ms: 1.29x faster                                   |
| logging_format           | 8.91 us                                                | 6.92 us: 1.29x faster                                  |
| tornado_http             | 127 ms                                                 | 99.3 ms: 1.28x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 59.2 ms: 1.27x faster                                  |
| fannkuch                 | 486 ms                                                 | 385 ms: 1.26x faster                                   |
| 2to3                     | 336 ms                                                 | 267 ms: 1.26x faster                                   |
| deepcopy                 | 442 us                                                 | 353 us: 1.25x faster                                   |
| sqlglot_normalize        | 135 ms                                                 | 108 ms: 1.25x faster                                   |
| unpack_sequence          | 64.7 ns                                                | 51.9 ns: 1.25x faster                                  |
| mypy2                    | 428 ms                                                 | 344 ms: 1.25x faster                                   |
| regex_compile            | 177 ms                                                 | 145 ms: 1.22x faster                                   |
| sqlglot_optimize         | 65.3 ms                                                | 53.6 ms: 1.22x faster                                  |
| nqueens                  | 100 ms                                                 | 82.3 ms: 1.22x faster                                  |
| deepcopy_reduce          | 3.82 us                                                | 3.16 us: 1.21x faster                                  |
| scimark_fft              | 424 ms                                                 | 352 ms: 1.20x faster                                   |
| docutils                 | 3.17 sec                                               | 2.71 sec: 1.17x faster                                 |
| sqlalchemy_declarative   | 165 ms                                                 | 144 ms: 1.15x faster                                   |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.78 ms: 1.14x faster                                  |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.6 ms: 1.14x faster                                  |
| bench_thread_pool        | 947 us                                                 | 833 us: 1.14x faster                                   |
| json_loads               | 28.8 us                                                | 25.6 us: 1.13x faster                                  |
| dulwich_log              | 75.9 ms                                                | 68.4 ms: 1.11x faster                                  |
| xml_etree_generate       | 94.2 ms                                                | 84.9 ms: 1.11x faster                                  |
| mdp                      | 2.82 sec                                               | 2.55 sec: 1.11x faster                                 |
| json                     | 5.42 ms                                                | 4.89 ms: 1.11x faster                                  |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                  |
| pathlib                  | 20.0 ms                                                | 18.2 ms: 1.10x faster                                  |
| regex_dna                | 222 ms                                                 | 202 ms: 1.10x faster                                   |
| regex_v8                 | 25.0 ms                                                | 22.8 ms: 1.10x faster                                  |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                   |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                  |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.06x faster                                   |
| gc_traversal             | 3.84 ms                                                | 3.86 ms: 1.00x slower                                  |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                  |
| pidigits                 | 190 ms                                                 | 196 ms: 1.03x slower                                   |
| telco                    | 6.54 ms                                                | 6.80 ms: 1.04x slower                                  |
| async_generators         | 425 ms                                                 | 445 ms: 1.05x slower                                   |
| unpickle_list            | 4.82 us                                                | 5.05 us: 1.05x slower                                  |
| unpickle                 | 14.1 us                                                | 15.2 us: 1.08x slower                                  |
| pickle_dict              | 27.3 us                                                | 30.5 us: 1.12x slower                                  |
| regex_effbot             | 3.23 ms                                                | 3.66 ms: 1.14x slower                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.76 ms: 1.16x slower                                  |
| dask                     | 423 ms                                                 | 535 ms: 1.27x slower                                   |
| coverage                 | 72.8 ms                                                | 95.2 ms: 1.31x slower                                  |
| Geometric mean           | (ref)                                                  | 1.28x faster                                           |

Benchmark hidden because not significant (2): bench_mp_pool, pickle_list
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x
