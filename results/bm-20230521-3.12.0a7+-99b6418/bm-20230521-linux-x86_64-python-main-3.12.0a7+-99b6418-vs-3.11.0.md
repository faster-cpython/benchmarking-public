
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 99b6418
- commit date: 2023-05-21
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-linux-x86_64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 268 ms: 1.04x slower                                   |
| docutils       | 2.63 sec                                               | 2.73 sec: 1.04x slower                                 |
| tornado_http   | 96.3 ms                                                | 98.8 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-linux-x86_64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.0 ms: 1.05x faster                                  |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                   |
| float          | 77.2 ms                                                | 81.1 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-linux-x86_64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.64 ms: 1.10x faster                                  |
| regex_v8       | 22.0 ms                                                | 23.1 ms: 1.05x slower                                  |
| regex_compile  | 138 ms                                                 | 146 ms: 1.05x slower                                   |
| regex_dna      | 204 ms                                                 | 216 ms: 1.06x slower                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-linux-x86_64-python-main-3.12.0a7+-99b6418 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.82 ms: 1.28x faster                                  |
| json_loads           | 26.5 us                                                | 25.2 us: 1.05x faster                                  |
| unpickle_pure_python | 228 us                                                 | 218 us: 1.05x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                   |
| pickle_dict          | 31.1 us                                                | 30.8 us: 1.01x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| unpickle_list        | 4.91 us                                                | 4.93 us: 1.00x slower                                  |
| pickle_pure_python   | 306 us                                                 | 313 us: 1.02x slower                                   |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                  |
| unpickle             | 13.7 us                                                | 14.8 us: 1.08x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 59.8 ms: 1.11x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 86.0 ms: 1.13x slower                                  |
| pickle_list          | 4.11 us                                                | 4.64 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-linux-x86_64-python-main-3.12.0a7+-99b6418 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.36 ms: 1.10x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.79 ms: 1.13x slower                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-linux-x86_64-python-main-3.12.0a7+-99b6418 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-linux-x86_64-python-main-3.12.0a7+-99b6418 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 139 us: 3.50x faster                                   |
| generators               | 73.5 ms                                                | 31.9 ms: 2.30x faster                                  |
| asyncio_tcp              | 922 ms                                                 | 516 ms: 1.79x faster                                   |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                 |
| json_dumps               | 12.6 ms                                                | 9.82 ms: 1.28x faster                                  |
| richards_super           | 56.8 ms                                                | 49.9 ms: 1.14x faster                                  |
| gc_traversal             | 4.02 ms                                                | 3.60 ms: 1.12x faster                                  |
| async_tree_none          | 526 ms                                                 | 472 ms: 1.12x faster                                   |
| async_tree_io            | 1.30 sec                                               | 1.16 sec: 1.11x faster                                 |
| regex_effbot             | 3.99 ms                                                | 3.64 ms: 1.10x faster                                  |
| coroutines               | 25.5 ms                                                | 23.3 ms: 1.09x faster                                  |
| async_tree_memoization   | 627 ms                                                 | 574 ms: 1.09x faster                                   |
| comprehensions           | 22.4 us                                                | 20.6 us: 1.09x faster                                  |
| chaos                    | 69.2 ms                                                | 65.2 ms: 1.06x faster                                  |
| deltablue                | 3.67 ms                                                | 3.47 ms: 1.06x faster                                  |
| json_loads               | 26.5 us                                                | 25.2 us: 1.05x faster                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.34 ms: 1.05x faster                                  |
| nbody                    | 93.1 ms                                                | 89.0 ms: 1.05x faster                                  |
| unpickle_pure_python     | 228 us                                                 | 218 us: 1.05x faster                                   |
| richards                 | 45.7 ms                                                | 43.9 ms: 1.04x faster                                  |
| json                     | 4.94 ms                                                | 4.75 ms: 1.04x faster                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 712 ms: 1.04x faster                                   |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                   |
| go                       | 140 ms                                                 | 135 ms: 1.04x faster                                   |
| sqlglot_transpile        | 1.70 ms                                                | 1.65 ms: 1.03x faster                                  |
| coverage                 | 100 ms                                                 | 97.2 ms: 1.03x faster                                  |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.03x faster                                 |
| mdp                      | 2.62 sec                                               | 2.55 sec: 1.03x faster                                 |
| hexiom                   | 6.37 ms                                                | 6.27 ms: 1.02x faster                                  |
| nqueens                  | 83.4 ms                                                | 82.1 ms: 1.01x faster                                  |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.01x faster                                   |
| pickle_dict              | 31.1 us                                                | 30.8 us: 1.01x faster                                  |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| raytrace                 | 297 ms                                                 | 295 ms: 1.01x faster                                   |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                   |
| unpickle_list            | 4.91 us                                                | 4.93 us: 1.00x slower                                  |
| pathlib                  | 18.2 ms                                                | 18.3 ms: 1.01x slower                                  |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                  |
| bench_thread_pool        | 819 us                                                 | 827 us: 1.01x slower                                   |
| sqlglot_normalize        | 108 ms                                                 | 109 ms: 1.01x slower                                   |
| sqlglot_optimize         | 53.1 ms                                                | 53.8 ms: 1.01x slower                                  |
| deepcopy_memo            | 37.0 us                                                | 37.7 us: 1.02x slower                                  |
| fannkuch                 | 388 ms                                                 | 395 ms: 1.02x slower                                   |
| pickle_pure_python       | 306 us                                                 | 313 us: 1.02x slower                                   |
| tornado_http             | 96.3 ms                                                | 98.8 ms: 1.03x slower                                  |
| pprint_pformat           | 1.46 sec                                               | 1.50 sec: 1.03x slower                                 |
| telco                    | 6.58 ms                                                | 6.82 ms: 1.04x slower                                  |
| 2to3                     | 259 ms                                                 | 268 ms: 1.04x slower                                   |
| scimark_sor              | 118 ms                                                 | 122 ms: 1.04x slower                                   |
| deepcopy                 | 342 us                                                 | 355 us: 1.04x slower                                   |
| docutils                 | 2.63 sec                                               | 2.73 sec: 1.04x slower                                 |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.6 ms: 1.04x slower                                  |
| sqlalchemy_declarative   | 138 ms                                                 | 144 ms: 1.05x slower                                   |
| regex_v8                 | 22.0 ms                                                | 23.1 ms: 1.05x slower                                  |
| pprint_safe_repr         | 701 ms                                                 | 736 ms: 1.05x slower                                   |
| float                    | 77.2 ms                                                | 81.1 ms: 1.05x slower                                  |
| crypto_pyaes             | 74.7 ms                                                | 78.6 ms: 1.05x slower                                  |
| scimark_lu               | 110 ms                                                 | 116 ms: 1.05x slower                                   |
| regex_compile            | 138 ms                                                 | 146 ms: 1.05x slower                                   |
| regex_dna                | 204 ms                                                 | 216 ms: 1.06x slower                                   |
| pickle                   | 10.1 us                                                | 10.7 us: 1.06x slower                                  |
| spectral_norm            | 100 ms                                                 | 106 ms: 1.06x slower                                   |
| dulwich_log              | 63.7 ms                                                | 67.7 ms: 1.06x slower                                  |
| scimark_monte_carlo      | 68.1 ms                                                | 72.4 ms: 1.06x slower                                  |
| logging_simple           | 6.03 us                                                | 6.44 us: 1.07x slower                                  |
| deepcopy_reduce          | 2.94 us                                                | 3.14 us: 1.07x slower                                  |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                  |
| sqlite_synth             | 2.52 us                                                | 2.70 us: 1.07x slower                                  |
| pyflate                  | 418 ms                                                 | 449 ms: 1.07x slower                                   |
| logging_format           | 6.68 us                                                | 7.19 us: 1.08x slower                                  |
| unpickle                 | 13.7 us                                                | 14.8 us: 1.08x slower                                  |
| scimark_fft              | 328 ms                                                 | 357 ms: 1.09x slower                                   |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.91 ms: 1.09x slower                                  |
| python_startup           | 8.52 ms                                                | 9.36 ms: 1.10x slower                                  |
| xml_etree_process        | 53.9 ms                                                | 59.8 ms: 1.11x slower                                  |
| xml_etree_generate       | 76.2 ms                                                | 86.0 ms: 1.13x slower                                  |
| pickle_list              | 4.11 us                                                | 4.64 us: 1.13x slower                                  |
| python_startup_no_site   | 6.01 ms                                                | 6.79 ms: 1.13x slower                                  |
| unpack_sequence          | 43.1 ns                                                | 50.1 ns: 1.16x slower                                  |
| async_generators         | 368 ms                                                 | 446 ms: 1.21x slower                                   |
| dask                     | 360 ms                                                 | 538 ms: 1.49x slower                                   |
| Geometric mean           | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (4): bench_mp_pool, logging_silent, tomli_loads, mypy2
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
