
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: e3b5ed7
- commit date: 2023-07-29
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 268 ms: 1.26x faster                                   |
| docutils       | 3.17 sec                                               | 2.72 sec: 1.17x faster                                 |
| tornado_http   | 127 ms                                                 | 102 ms: 1.25x faster                                   |
| Geometric mean | (ref)                                                  | 1.22x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.9 ms: 1.59x faster                                  |
| float          | 111 ms                                                 | 79.7 ms: 1.39x faster                                  |
| pidigits       | 190 ms                                                 | 196 ms: 1.03x slower                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                   |
| regex_v8       | 25.0 ms                                                | 23.0 ms: 1.09x faster                                  |
| regex_dna      | 222 ms                                                 | 206 ms: 1.08x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.54 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 310 us: 1.47x faster                                   |
| unpickle_pure_python | 300 us                                                 | 217 us: 1.38x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.98 ms: 1.36x faster                                  |
| tomli_loads          | 2.92 sec                                               | 2.21 sec: 1.32x faster                                 |
| xml_etree_process    | 74.9 ms                                                | 59.2 ms: 1.27x faster                                  |
| json_loads           | 28.8 us                                                | 25.6 us: 1.12x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 84.7 ms: 1.11x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 155 ms: 1.06x faster                                   |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.03x slower                                  |
| pickle_list          | 4.56 us                                                | 4.71 us: 1.03x slower                                  |
| unpickle             | 14.1 us                                                | 14.8 us: 1.04x slower                                  |
| pickle               | 10.3 us                                                | 10.8 us: 1.05x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.3 us: 1.15x slower                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.29 ms: 1.52x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.75 ms: 1.16x slower                                  |
| Geometric mean         | (ref)                                                  | 1.15x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 148 us: 3.46x faster                                   |
| generators               | 76.8 ms                                                | 30.2 ms: 2.54x faster                                  |
| deltablue                | 7.42 ms                                                | 3.51 ms: 2.11x faster                                  |
| richards_super           | 90.7 ms                                                | 49.6 ms: 1.83x faster                                  |
| asyncio_tcp              | 925 ms                                                 | 522 ms: 1.77x faster                                   |
| logging_silent           | 175 ns                                                 | 101 ns: 1.74x faster                                   |
| richards                 | 74.9 ms                                                | 43.8 ms: 1.71x faster                                  |
| go                       | 229 ms                                                 | 135 ms: 1.69x faster                                   |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                 |
| chaos                    | 106 ms                                                 | 64.2 ms: 1.66x faster                                  |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.61x faster                                   |
| nbody                    | 142 ms                                                 | 88.9 ms: 1.59x faster                                  |
| raytrace                 | 464 ms                                                 | 295 ms: 1.57x faster                                   |
| hexiom                   | 9.53 ms                                                | 6.15 ms: 1.55x faster                                  |
| sqlglot_parse            | 2.06 ms                                                | 1.34 ms: 1.54x faster                                  |
| python_startup           | 14.2 ms                                                | 9.29 ms: 1.52x faster                                  |
| scimark_monte_carlo      | 108 ms                                                 | 71.3 ms: 1.52x faster                                  |
| async_tree_io            | 1.77 sec                                               | 1.17 sec: 1.51x faster                                 |
| async_tree_none          | 717 ms                                                 | 476 ms: 1.51x faster                                   |
| pyflate                  | 673 ms                                                 | 447 ms: 1.51x faster                                   |
| crypto_pyaes             | 118 ms                                                 | 78.9 ms: 1.50x faster                                  |
| scimark_lu               | 163 ms                                                 | 110 ms: 1.48x faster                                   |
| async_tree_memoization   | 854 ms                                                 | 579 ms: 1.48x faster                                   |
| pickle_pure_python       | 455 us                                                 | 310 us: 1.47x faster                                   |
| sqlglot_transpile        | 2.45 ms                                                | 1.67 ms: 1.47x faster                                  |
| coroutines               | 31.8 ms                                                | 22.5 ms: 1.41x faster                                  |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.40x faster                                   |
| float                    | 111 ms                                                 | 79.7 ms: 1.39x faster                                  |
| unpickle_pure_python     | 300 us                                                 | 217 us: 1.38x faster                                   |
| deepcopy_memo            | 52.3 us                                                | 38.0 us: 1.38x faster                                  |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                  |
| json_dumps               | 13.5 ms                                                | 9.98 ms: 1.36x faster                                  |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 714 ms: 1.33x faster                                   |
| unpack_sequence          | 64.7 ns                                                | 48.8 ns: 1.32x faster                                  |
| tomli_loads              | 2.92 sec                                               | 2.21 sec: 1.32x faster                                 |
| pprint_pformat           | 1.99 sec                                               | 1.52 sec: 1.31x faster                                 |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.30x faster                                 |
| logging_simple           | 8.07 us                                                | 6.20 us: 1.30x faster                                  |
| comprehensions           | 26.8 us                                                | 20.8 us: 1.29x faster                                  |
| logging_format           | 8.91 us                                                | 6.92 us: 1.29x faster                                  |
| pprint_safe_repr         | 955 ms                                                 | 747 ms: 1.28x faster                                   |
| xml_etree_process        | 74.9 ms                                                | 59.2 ms: 1.27x faster                                  |
| 2to3                     | 336 ms                                                 | 268 ms: 1.26x faster                                   |
| fannkuch                 | 486 ms                                                 | 389 ms: 1.25x faster                                   |
| tornado_http             | 127 ms                                                 | 102 ms: 1.25x faster                                   |
| sqlglot_normalize        | 135 ms                                                 | 109 ms: 1.24x faster                                   |
| deepcopy                 | 442 us                                                 | 356 us: 1.24x faster                                   |
| mypy2                    | 428 ms                                                 | 345 ms: 1.24x faster                                   |
| regex_compile            | 177 ms                                                 | 145 ms: 1.22x faster                                   |
| deepcopy_reduce          | 3.82 us                                                | 3.13 us: 1.22x faster                                  |
| sqlglot_optimize         | 65.3 ms                                                | 54.0 ms: 1.21x faster                                  |
| scimark_fft              | 424 ms                                                 | 351 ms: 1.21x faster                                   |
| nqueens                  | 100 ms                                                 | 82.9 ms: 1.21x faster                                  |
| docutils                 | 3.17 sec                                               | 2.72 sec: 1.17x faster                                 |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.76 ms: 1.15x faster                                  |
| bench_thread_pool        | 947 us                                                 | 830 us: 1.14x faster                                   |
| sqlalchemy_declarative   | 165 ms                                                 | 146 ms: 1.14x faster                                   |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.7 ms: 1.13x faster                                  |
| json_loads               | 28.8 us                                                | 25.6 us: 1.12x faster                                  |
| xml_etree_generate       | 94.2 ms                                                | 84.7 ms: 1.11x faster                                  |
| mdp                      | 2.82 sec                                               | 2.54 sec: 1.11x faster                                 |
| dulwich_log              | 75.9 ms                                                | 68.4 ms: 1.11x faster                                  |
| pathlib                  | 20.0 ms                                                | 18.1 ms: 1.11x faster                                  |
| json                     | 5.42 ms                                                | 4.90 ms: 1.10x faster                                  |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.10x faster                                  |
| meteor_contest           | 115 ms                                                 | 104 ms: 1.10x faster                                   |
| regex_v8                 | 25.0 ms                                                | 23.0 ms: 1.09x faster                                  |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| regex_dna                | 222 ms                                                 | 206 ms: 1.08x faster                                   |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                  |
| xml_etree_parse          | 163 ms                                                 | 155 ms: 1.06x faster                                   |
| gc_traversal             | 3.84 ms                                                | 3.85 ms: 1.00x slower                                  |
| unpickle_list            | 4.82 us                                                | 4.94 us: 1.03x slower                                  |
| telco                    | 6.54 ms                                                | 6.73 ms: 1.03x slower                                  |
| pickle_list              | 4.56 us                                                | 4.71 us: 1.03x slower                                  |
| pidigits                 | 190 ms                                                 | 196 ms: 1.03x slower                                   |
| unpickle                 | 14.1 us                                                | 14.8 us: 1.04x slower                                  |
| async_generators         | 425 ms                                                 | 444 ms: 1.05x slower                                   |
| pickle                   | 10.3 us                                                | 10.8 us: 1.05x slower                                  |
| regex_effbot             | 3.23 ms                                                | 3.54 ms: 1.10x slower                                  |
| pickle_dict              | 27.3 us                                                | 31.3 us: 1.15x slower                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.75 ms: 1.16x slower                                  |
| dask                     | 423 ms                                                 | 538 ms: 1.27x slower                                   |
| coverage                 | 72.8 ms                                                | 93.8 ms: 1.29x slower                                  |
| Geometric mean           | (ref)                                                  | 1.28x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x
