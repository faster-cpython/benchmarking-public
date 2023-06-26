
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 9cd3664
- commit date: 2023-06-24
- overall geometric mean: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-linux-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 269 ms: 1.25x faster                                   |
| docutils       | 3.17 sec                                               | 2.72 sec: 1.16x faster                                 |
| tornado_http   | 127 ms                                                 | 99.9 ms: 1.28x faster                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-linux-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 91.0 ms: 1.56x faster                                  |
| float          | 111 ms                                                 | 80.6 ms: 1.37x faster                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-linux-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                   |
| regex_dna      | 222 ms                                                 | 200 ms: 1.11x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.7 ms: 1.10x faster                                  |
| regex_effbot   | 3.23 ms                                                | 3.66 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-linux-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 310 us: 1.47x faster                                   |
| unpickle_pure_python | 300 us                                                 | 215 us: 1.40x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.73 ms: 1.39x faster                                  |
| tomli_loads          | 2.92 sec                                               | 2.17 sec: 1.34x faster                                 |
| xml_etree_process    | 74.9 ms                                                | 59.7 ms: 1.26x faster                                  |
| json_loads           | 28.8 us                                                | 24.9 us: 1.16x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 84.9 ms: 1.11x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                   |
| unpickle_list        | 4.82 us                                                | 4.92 us: 1.02x slower                                  |
| pickle_list          | 4.56 us                                                | 4.71 us: 1.03x slower                                  |
| pickle               | 10.3 us                                                | 10.9 us: 1.06x slower                                  |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.8 us: 1.17x slower                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-linux-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.33 ms: 1.52x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.78 ms: 1.16x slower                                  |
| Geometric mean         | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-linux-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.39x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230624-linux-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 144 us: 3.53x faster                                   |
| generators               | 76.8 ms                                                | 31.3 ms: 2.45x faster                                  |
| deltablue                | 7.42 ms                                                | 3.47 ms: 2.14x faster                                  |
| richards_super           | 90.7 ms                                                | 49.2 ms: 1.85x faster                                  |
| asyncio_tcp              | 925 ms                                                 | 510 ms: 1.82x faster                                   |
| logging_silent           | 175 ns                                                 | 97.9 ns: 1.79x faster                                  |
| richards                 | 74.9 ms                                                | 44.1 ms: 1.70x faster                                  |
| go                       | 229 ms                                                 | 136 ms: 1.69x faster                                   |
| chaos                    | 106 ms                                                 | 63.2 ms: 1.68x faster                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                 |
| scimark_sor              | 197 ms                                                 | 123 ms: 1.60x faster                                   |
| raytrace                 | 464 ms                                                 | 294 ms: 1.58x faster                                   |
| hexiom                   | 9.53 ms                                                | 6.07 ms: 1.57x faster                                  |
| nbody                    | 142 ms                                                 | 91.0 ms: 1.56x faster                                  |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.54x faster                                  |
| async_tree_io            | 1.77 sec                                               | 1.16 sec: 1.53x faster                                 |
| crypto_pyaes             | 118 ms                                                 | 77.8 ms: 1.52x faster                                  |
| async_tree_none          | 717 ms                                                 | 471 ms: 1.52x faster                                   |
| python_startup           | 14.2 ms                                                | 9.33 ms: 1.52x faster                                  |
| pyflate                  | 673 ms                                                 | 444 ms: 1.51x faster                                   |
| scimark_monte_carlo      | 108 ms                                                 | 71.8 ms: 1.51x faster                                  |
| async_tree_memoization   | 854 ms                                                 | 574 ms: 1.49x faster                                   |
| sqlglot_transpile        | 2.45 ms                                                | 1.65 ms: 1.48x faster                                  |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.47x faster                                   |
| pickle_pure_python       | 455 us                                                 | 310 us: 1.47x faster                                   |
| spectral_norm            | 150 ms                                                 | 104 ms: 1.45x faster                                   |
| coroutines               | 31.8 ms                                                | 22.1 ms: 1.44x faster                                  |
| unpickle_pure_python     | 300 us                                                 | 215 us: 1.40x faster                                   |
| json_dumps               | 13.5 ms                                                | 9.73 ms: 1.39x faster                                  |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.39x faster                                  |
| deepcopy_memo            | 52.3 us                                                | 37.8 us: 1.39x faster                                  |
| float                    | 111 ms                                                 | 80.6 ms: 1.37x faster                                  |
| tomli_loads              | 2.92 sec                                               | 2.17 sec: 1.34x faster                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 712 ms: 1.34x faster                                   |
| pprint_pformat           | 1.99 sec                                               | 1.51 sec: 1.32x faster                                 |
| pycparser                | 1.50 sec                                               | 1.16 sec: 1.30x faster                                 |
| pprint_safe_repr         | 955 ms                                                 | 737 ms: 1.30x faster                                   |
| logging_format           | 8.91 us                                                | 6.87 us: 1.30x faster                                  |
| logging_simple           | 8.07 us                                                | 6.24 us: 1.29x faster                                  |
| tornado_http             | 127 ms                                                 | 99.9 ms: 1.28x faster                                  |
| comprehensions           | 26.8 us                                                | 21.1 us: 1.27x faster                                  |
| unpack_sequence          | 64.7 ns                                                | 51.4 ns: 1.26x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 59.7 ms: 1.26x faster                                  |
| fannkuch                 | 486 ms                                                 | 388 ms: 1.25x faster                                   |
| 2to3                     | 336 ms                                                 | 269 ms: 1.25x faster                                   |
| mypy2                    | 428 ms                                                 | 343 ms: 1.25x faster                                   |
| sqlglot_normalize        | 135 ms                                                 | 109 ms: 1.25x faster                                   |
| deepcopy                 | 442 us                                                 | 357 us: 1.24x faster                                   |
| nqueens                  | 100 ms                                                 | 81.0 ms: 1.24x faster                                  |
| regex_compile            | 177 ms                                                 | 145 ms: 1.22x faster                                   |
| sqlglot_optimize         | 65.3 ms                                                | 53.7 ms: 1.22x faster                                  |
| deepcopy_reduce          | 3.82 us                                                | 3.17 us: 1.21x faster                                  |
| scimark_fft              | 424 ms                                                 | 356 ms: 1.19x faster                                   |
| docutils                 | 3.17 sec                                               | 2.72 sec: 1.16x faster                                 |
| json_loads               | 28.8 us                                                | 24.9 us: 1.16x faster                                  |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.4 ms: 1.15x faster                                  |
| sqlalchemy_declarative   | 165 ms                                                 | 144 ms: 1.14x faster                                   |
| bench_thread_pool        | 947 us                                                 | 828 us: 1.14x faster                                   |
| json                     | 5.42 ms                                                | 4.76 ms: 1.14x faster                                  |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.83 ms: 1.13x faster                                  |
| dulwich_log              | 75.9 ms                                                | 68.0 ms: 1.12x faster                                  |
| xml_etree_generate       | 94.2 ms                                                | 84.9 ms: 1.11x faster                                  |
| regex_dna                | 222 ms                                                 | 200 ms: 1.11x faster                                   |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.10x faster                                  |
| regex_v8                 | 25.0 ms                                                | 22.7 ms: 1.10x faster                                  |
| pathlib                  | 20.0 ms                                                | 18.2 ms: 1.10x faster                                  |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.10x faster                                   |
| mdp                      | 2.82 sec                                               | 2.58 sec: 1.09x faster                                 |
| sqlite_synth             | 2.93 us                                                | 2.71 us: 1.08x faster                                  |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                   |
| gc_traversal             | 3.84 ms                                                | 3.83 ms: 1.00x faster                                  |
| unpickle_list            | 4.82 us                                                | 4.92 us: 1.02x slower                                  |
| pickle_list              | 4.56 us                                                | 4.71 us: 1.03x slower                                  |
| telco                    | 6.54 ms                                                | 6.80 ms: 1.04x slower                                  |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| async_generators         | 425 ms                                                 | 445 ms: 1.05x slower                                   |
| pickle                   | 10.3 us                                                | 10.9 us: 1.06x slower                                  |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                  |
| regex_effbot             | 3.23 ms                                                | 3.66 ms: 1.13x slower                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.78 ms: 1.16x slower                                  |
| pickle_dict              | 27.3 us                                                | 31.8 us: 1.17x slower                                  |
| dask                     | 423 ms                                                 | 535 ms: 1.27x slower                                   |
| coverage                 | 72.8 ms                                                | 94.6 ms: 1.30x slower                                  |
| Geometric mean           | (ref)                                                  | 1.28x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
