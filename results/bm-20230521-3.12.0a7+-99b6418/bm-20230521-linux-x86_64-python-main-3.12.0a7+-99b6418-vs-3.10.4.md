
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 99b6418
- commit date: 2023-05-21
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-linux-x86_64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 268 ms: 1.25x faster                                   |
| docutils       | 3.17 sec                                               | 2.73 sec: 1.16x faster                                 |
| tornado_http   | 127 ms                                                 | 98.8 ms: 1.29x faster                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-linux-x86_64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.0 ms: 1.59x faster                                  |
| float          | 111 ms                                                 | 81.1 ms: 1.36x faster                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-linux-x86_64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 146 ms: 1.21x faster                                   |
| regex_v8       | 25.0 ms                                                | 23.1 ms: 1.08x faster                                  |
| regex_dna      | 222 ms                                                 | 216 ms: 1.03x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.64 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-linux-x86_64-python-main-3.12.0a7+-99b6418 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 313 us: 1.45x faster                                   |
| unpickle_pure_python | 300 us                                                 | 218 us: 1.38x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.82 ms: 1.38x faster                                  |
| tomli_loads          | 2.92 sec                                               | 2.23 sec: 1.31x faster                                 |
| xml_etree_process    | 74.9 ms                                                | 59.8 ms: 1.25x faster                                  |
| json_loads           | 28.8 us                                                | 25.2 us: 1.14x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 86.0 ms: 1.10x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                   |
| pickle_list          | 4.56 us                                                | 4.64 us: 1.02x slower                                  |
| unpickle_list        | 4.82 us                                                | 4.93 us: 1.02x slower                                  |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                  |
| unpickle             | 14.1 us                                                | 14.8 us: 1.05x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-linux-x86_64-python-main-3.12.0a7+-99b6418 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.36 ms: 1.51x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.79 ms: 1.17x slower                                  |
| Geometric mean         | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-linux-x86_64-python-main-3.12.0a7+-99b6418 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.36x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-linux-x86_64-python-main-3.12.0a7+-99b6418 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 139 us: 3.68x faster                                   |
| generators               | 76.8 ms                                                | 31.9 ms: 2.40x faster                                  |
| deltablue                | 7.42 ms                                                | 3.47 ms: 2.14x faster                                  |
| richards_super           | 90.7 ms                                                | 49.9 ms: 1.82x faster                                  |
| asyncio_tcp              | 925 ms                                                 | 516 ms: 1.79x faster                                   |
| logging_silent           | 175 ns                                                 | 101 ns: 1.73x faster                                   |
| richards                 | 74.9 ms                                                | 43.9 ms: 1.71x faster                                  |
| go                       | 229 ms                                                 | 135 ms: 1.70x faster                                   |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                 |
| chaos                    | 106 ms                                                 | 65.2 ms: 1.63x faster                                  |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.61x faster                                   |
| nbody                    | 142 ms                                                 | 89.0 ms: 1.59x faster                                  |
| raytrace                 | 464 ms                                                 | 295 ms: 1.57x faster                                   |
| sqlglot_parse            | 2.06 ms                                                | 1.34 ms: 1.54x faster                                  |
| async_tree_io            | 1.77 sec                                               | 1.16 sec: 1.52x faster                                 |
| async_tree_none          | 717 ms                                                 | 472 ms: 1.52x faster                                   |
| hexiom                   | 9.53 ms                                                | 6.27 ms: 1.52x faster                                  |
| python_startup           | 14.2 ms                                                | 9.36 ms: 1.51x faster                                  |
| crypto_pyaes             | 118 ms                                                 | 78.6 ms: 1.51x faster                                  |
| pyflate                  | 673 ms                                                 | 449 ms: 1.50x faster                                   |
| scimark_monte_carlo      | 108 ms                                                 | 72.4 ms: 1.49x faster                                  |
| async_tree_memoization   | 854 ms                                                 | 574 ms: 1.49x faster                                   |
| sqlglot_transpile        | 2.45 ms                                                | 1.65 ms: 1.48x faster                                  |
| pickle_pure_python       | 455 us                                                 | 313 us: 1.45x faster                                   |
| scimark_lu               | 163 ms                                                 | 116 ms: 1.41x faster                                   |
| spectral_norm            | 150 ms                                                 | 106 ms: 1.41x faster                                   |
| deepcopy_memo            | 52.3 us                                                | 37.7 us: 1.39x faster                                  |
| unpickle_pure_python     | 300 us                                                 | 218 us: 1.38x faster                                   |
| json_dumps               | 13.5 ms                                                | 9.82 ms: 1.38x faster                                  |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.36x faster                                  |
| coroutines               | 31.8 ms                                                | 23.3 ms: 1.36x faster                                  |
| float                    | 111 ms                                                 | 81.1 ms: 1.36x faster                                  |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 712 ms: 1.34x faster                                   |
| pprint_pformat           | 1.99 sec                                               | 1.50 sec: 1.33x faster                                 |
| tomli_loads              | 2.92 sec                                               | 2.23 sec: 1.31x faster                                 |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.31x faster                                 |
| comprehensions           | 26.8 us                                                | 20.6 us: 1.30x faster                                  |
| pprint_safe_repr         | 955 ms                                                 | 736 ms: 1.30x faster                                   |
| unpack_sequence          | 64.7 ns                                                | 50.1 ns: 1.29x faster                                  |
| tornado_http             | 127 ms                                                 | 98.8 ms: 1.29x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 59.8 ms: 1.25x faster                                  |
| 2to3                     | 336 ms                                                 | 268 ms: 1.25x faster                                   |
| logging_simple           | 8.07 us                                                | 6.44 us: 1.25x faster                                  |
| deepcopy                 | 442 us                                                 | 355 us: 1.24x faster                                   |
| sqlglot_normalize        | 135 ms                                                 | 109 ms: 1.24x faster                                   |
| logging_format           | 8.91 us                                                | 7.19 us: 1.24x faster                                  |
| fannkuch                 | 486 ms                                                 | 395 ms: 1.23x faster                                   |
| nqueens                  | 100 ms                                                 | 82.1 ms: 1.22x faster                                  |
| deepcopy_reduce          | 3.82 us                                                | 3.14 us: 1.22x faster                                  |
| regex_compile            | 177 ms                                                 | 146 ms: 1.21x faster                                   |
| sqlglot_optimize         | 65.3 ms                                                | 53.8 ms: 1.21x faster                                  |
| scimark_fft              | 424 ms                                                 | 357 ms: 1.18x faster                                   |
| docutils                 | 3.17 sec                                               | 2.73 sec: 1.16x faster                                 |
| bench_thread_pool        | 947 us                                                 | 827 us: 1.15x faster                                   |
| json_loads               | 28.8 us                                                | 25.2 us: 1.14x faster                                  |
| sqlalchemy_declarative   | 165 ms                                                 | 144 ms: 1.14x faster                                   |
| json                     | 5.42 ms                                                | 4.75 ms: 1.14x faster                                  |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.6 ms: 1.14x faster                                  |
| dulwich_log              | 75.9 ms                                                | 67.7 ms: 1.12x faster                                  |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.12x faster                                  |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.91 ms: 1.11x faster                                  |
| mdp                      | 2.82 sec                                               | 2.55 sec: 1.11x faster                                 |
| xml_etree_generate       | 94.2 ms                                                | 86.0 ms: 1.10x faster                                  |
| pathlib                  | 20.0 ms                                                | 18.3 ms: 1.09x faster                                  |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.09x faster                                   |
| sqlite_synth             | 2.93 us                                                | 2.70 us: 1.09x faster                                  |
| regex_v8                 | 25.0 ms                                                | 23.1 ms: 1.08x faster                                  |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                   |
| gc_traversal             | 3.84 ms                                                | 3.60 ms: 1.07x faster                                  |
| regex_dna                | 222 ms                                                 | 216 ms: 1.03x faster                                   |
| pickle_list              | 4.56 us                                                | 4.64 us: 1.02x slower                                  |
| unpickle_list            | 4.82 us                                                | 4.93 us: 1.02x slower                                  |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                  |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| telco                    | 6.54 ms                                                | 6.82 ms: 1.04x slower                                  |
| unpickle                 | 14.1 us                                                | 14.8 us: 1.05x slower                                  |
| async_generators         | 425 ms                                                 | 446 ms: 1.05x slower                                   |
| regex_effbot             | 3.23 ms                                                | 3.64 ms: 1.13x slower                                  |
| pickle_dict              | 27.3 us                                                | 30.8 us: 1.13x slower                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.79 ms: 1.17x slower                                  |
| dask                     | 423 ms                                                 | 538 ms: 1.27x slower                                   |
| coverage                 | 72.8 ms                                                | 97.2 ms: 1.34x slower                                  |
| Geometric mean           | (ref)                                                  | 1.27x faster                                           |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
