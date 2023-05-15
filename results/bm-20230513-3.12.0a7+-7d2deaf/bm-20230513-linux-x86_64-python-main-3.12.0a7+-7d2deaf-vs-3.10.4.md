
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 7d2deaf
- commit date: 2023-05-13
- overall geometric mean: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-linux-x86_64-python-main-3.12.0a7+-7d2deaf |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 268 ms: 1.26x faster                                   |
| docutils       | 3.17 sec                                               | 2.71 sec: 1.17x faster                                 |
| tornado_http   | 127 ms                                                 | 99.2 ms: 1.28x faster                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-linux-x86_64-python-main-3.12.0a7+-7d2deaf |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.4 ms: 1.57x faster                                  |
| float          | 111 ms                                                 | 81.1 ms: 1.36x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-linux-x86_64-python-main-3.12.0a7+-7d2deaf |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 147 ms: 1.20x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                  |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.63 ms: 1.12x slower                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-linux-x86_64-python-main-3.12.0a7+-7d2deaf |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 313 us: 1.46x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.75 ms: 1.39x faster                                  |
| unpickle_pure_python | 300 us                                                 | 218 us: 1.38x faster                                   |
| tomli_loads          | 2.92 sec                                               | 2.22 sec: 1.31x faster                                 |
| xml_etree_process    | 74.9 ms                                                | 59.3 ms: 1.26x faster                                  |
| json_loads           | 28.8 us                                                | 25.0 us: 1.15x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 85.8 ms: 1.10x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                   |
| unpickle_list        | 4.82 us                                                | 4.88 us: 1.01x slower                                  |
| unpickle             | 14.1 us                                                | 14.4 us: 1.02x slower                                  |
| pickle_list          | 4.56 us                                                | 4.69 us: 1.03x slower                                  |
| pickle               | 10.3 us                                                | 10.8 us: 1.04x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.3 us: 1.15x slower                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-linux-x86_64-python-main-3.12.0a7+-7d2deaf |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.13 ms: 1.55x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.66 ms: 1.15x slower                                  |
| Geometric mean         | (ref)                                                  | 1.16x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-linux-x86_64-python-main-3.12.0a7+-7d2deaf |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.35x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-linux-x86_64-python-main-3.12.0a7+-7d2deaf |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 148 us: 3.45x faster                                   |
| generators               | 76.8 ms                                                | 30.8 ms: 2.49x faster                                  |
| deltablue                | 7.42 ms                                                | 3.53 ms: 2.10x faster                                  |
| asyncio_tcp              | 925 ms                                                 | 514 ms: 1.80x faster                                   |
| richards_super           | 90.7 ms                                                | 50.5 ms: 1.80x faster                                  |
| logging_silent           | 175 ns                                                 | 102 ns: 1.72x faster                                   |
| richards                 | 74.9 ms                                                | 44.7 ms: 1.68x faster                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                 |
| go                       | 229 ms                                                 | 138 ms: 1.67x faster                                   |
| chaos                    | 106 ms                                                 | 65.4 ms: 1.62x faster                                  |
| scimark_sor              | 197 ms                                                 | 123 ms: 1.59x faster                                   |
| nbody                    | 142 ms                                                 | 90.4 ms: 1.57x faster                                  |
| python_startup           | 14.2 ms                                                | 9.13 ms: 1.55x faster                                  |
| hexiom                   | 9.53 ms                                                | 6.16 ms: 1.55x faster                                  |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.55x faster                                  |
| crypto_pyaes             | 118 ms                                                 | 76.8 ms: 1.54x faster                                  |
| raytrace                 | 464 ms                                                 | 301 ms: 1.54x faster                                   |
| async_tree_io            | 1.77 sec                                               | 1.15 sec: 1.54x faster                                 |
| async_tree_none          | 717 ms                                                 | 468 ms: 1.53x faster                                   |
| async_tree_memoization   | 854 ms                                                 | 569 ms: 1.50x faster                                   |
| sqlglot_transpile        | 2.45 ms                                                | 1.65 ms: 1.48x faster                                  |
| pyflate                  | 673 ms                                                 | 454 ms: 1.48x faster                                   |
| scimark_monte_carlo      | 108 ms                                                 | 74.0 ms: 1.46x faster                                  |
| pickle_pure_python       | 455 us                                                 | 313 us: 1.46x faster                                   |
| spectral_norm            | 150 ms                                                 | 105 ms: 1.42x faster                                   |
| scimark_lu               | 163 ms                                                 | 115 ms: 1.42x faster                                   |
| coroutines               | 31.8 ms                                                | 22.9 ms: 1.39x faster                                  |
| json_dumps               | 13.5 ms                                                | 9.75 ms: 1.39x faster                                  |
| unpickle_pure_python     | 300 us                                                 | 218 us: 1.38x faster                                   |
| float                    | 111 ms                                                 | 81.1 ms: 1.36x faster                                  |
| deepcopy_memo            | 52.3 us                                                | 38.6 us: 1.36x faster                                  |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.35x faster                                  |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 704 ms: 1.35x faster                                   |
| pprint_pformat           | 1.99 sec                                               | 1.50 sec: 1.32x faster                                 |
| unpack_sequence          | 64.7 ns                                                | 49.1 ns: 1.32x faster                                  |
| comprehensions           | 26.8 us                                                | 20.5 us: 1.31x faster                                  |
| tomli_loads              | 2.92 sec                                               | 2.22 sec: 1.31x faster                                 |
| pprint_safe_repr         | 955 ms                                                 | 737 ms: 1.30x faster                                   |
| tornado_http             | 127 ms                                                 | 99.2 ms: 1.28x faster                                  |
| logging_simple           | 8.07 us                                                | 6.29 us: 1.28x faster                                  |
| logging_format           | 8.91 us                                                | 6.95 us: 1.28x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 59.3 ms: 1.26x faster                                  |
| fannkuch                 | 486 ms                                                 | 387 ms: 1.26x faster                                   |
| 2to3                     | 336 ms                                                 | 268 ms: 1.26x faster                                   |
| pycparser                | 1.50 sec                                               | 1.20 sec: 1.25x faster                                 |
| deepcopy                 | 442 us                                                 | 355 us: 1.25x faster                                   |
| sqlglot_normalize        | 135 ms                                                 | 109 ms: 1.24x faster                                   |
| nqueens                  | 100 ms                                                 | 80.5 ms: 1.24x faster                                  |
| mypy2                    | 428 ms                                                 | 345 ms: 1.24x faster                                   |
| sqlglot_optimize         | 65.3 ms                                                | 54.1 ms: 1.21x faster                                  |
| deepcopy_reduce          | 3.82 us                                                | 3.18 us: 1.20x faster                                  |
| regex_compile            | 177 ms                                                 | 147 ms: 1.20x faster                                   |
| scimark_fft              | 424 ms                                                 | 360 ms: 1.18x faster                                   |
| docutils                 | 3.17 sec                                               | 2.71 sec: 1.17x faster                                 |
| json_loads               | 28.8 us                                                | 25.0 us: 1.15x faster                                  |
| regex_v8                 | 25.0 ms                                                | 21.9 ms: 1.14x faster                                  |
| bench_thread_pool        | 947 us                                                 | 828 us: 1.14x faster                                   |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.6 ms: 1.14x faster                                  |
| sqlalchemy_declarative   | 165 ms                                                 | 145 ms: 1.14x faster                                   |
| create_gc_cycles         | 1.67 ms                                                | 1.47 ms: 1.13x faster                                  |
| json                     | 5.42 ms                                                | 4.79 ms: 1.13x faster                                  |
| dulwich_log              | 75.9 ms                                                | 67.4 ms: 1.13x faster                                  |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.85 ms: 1.12x faster                                  |
| mdp                      | 2.82 sec                                               | 2.54 sec: 1.11x faster                                 |
| meteor_contest           | 115 ms                                                 | 104 ms: 1.11x faster                                   |
| xml_etree_generate       | 94.2 ms                                                | 85.8 ms: 1.10x faster                                  |
| regex_dna                | 222 ms                                                 | 204 ms: 1.09x faster                                   |
| pathlib                  | 20.0 ms                                                | 18.4 ms: 1.09x faster                                  |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| sqlite_synth             | 2.93 us                                                | 2.73 us: 1.07x faster                                  |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                   |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                   |
| unpickle_list            | 4.82 us                                                | 4.88 us: 1.01x slower                                  |
| unpickle                 | 14.1 us                                                | 14.4 us: 1.02x slower                                  |
| pickle_list              | 4.56 us                                                | 4.69 us: 1.03x slower                                  |
| pickle                   | 10.3 us                                                | 10.8 us: 1.04x slower                                  |
| gc_traversal             | 3.84 ms                                                | 4.07 ms: 1.06x slower                                  |
| async_generators         | 425 ms                                                 | 452 ms: 1.06x slower                                   |
| telco                    | 6.54 ms                                                | 6.97 ms: 1.07x slower                                  |
| regex_effbot             | 3.23 ms                                                | 3.63 ms: 1.12x slower                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.66 ms: 1.15x slower                                  |
| pickle_dict              | 27.3 us                                                | 31.3 us: 1.15x slower                                  |
| dask                     | 423 ms                                                 | 536 ms: 1.27x slower                                   |
| coverage                 | 72.8 ms                                                | 96.4 ms: 1.32x slower                                  |
| Geometric mean           | (ref)                                                  | 1.28x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
