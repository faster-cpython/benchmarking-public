
# Results vs. 3.10.4

- fork: kumaraditya303
- ref: no_register
- machine: linux-x86_64
- commit hash: 7390302
- commit date: 2023-05-23
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 267 ms: 1.26x faster                                                 |
| docutils       | 3.17 sec                                               | 2.67 sec: 1.19x faster                                               |
| html5lib       | 85.9 ms                                                | 65.4 ms: 1.31x faster                                                |
| tornado_http   | 127 ms                                                 | 97.7 ms: 1.30x faster                                                |
| Geometric mean | (ref)                                                  | 1.26x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 91.9 ms: 1.54x faster                                                |
| float          | 111 ms                                                 | 80.2 ms: 1.38x faster                                                |
| pidigits       | 190 ms                                                 | 196 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                                 |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                                 |
| regex_effbot   | 3.23 ms                                                | 3.48 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 311 us: 1.46x faster                                                 |
| unpickle_pure_python | 300 us                                                 | 215 us: 1.40x faster                                                 |
| json_dumps           | 13.5 ms                                                | 9.75 ms: 1.39x faster                                                |
| tomli_loads          | 2.92 sec                                               | 2.21 sec: 1.32x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 59.1 ms: 1.27x faster                                                |
| json_loads           | 28.8 us                                                | 24.9 us: 1.16x faster                                                |
| xml_etree_generate   | 94.2 ms                                                | 84.9 ms: 1.11x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                 |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                 |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                |
| pickle_list          | 4.56 us                                                | 4.65 us: 1.02x slower                                                |
| unpickle_list        | 4.82 us                                                | 5.11 us: 1.06x slower                                                |
| unpickle             | 14.1 us                                                | 15.1 us: 1.06x slower                                                |
| pickle_dict          | 27.3 us                                                | 32.9 us: 1.21x slower                                                |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.14 ms: 1.55x faster                                                |
| python_startup_no_site | 5.82 ms                                                | 6.77 ms: 1.16x slower                                                |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako           | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                |
| genshi_text    | 30.3 ms                                                | 22.5 ms: 1.35x faster                                                |
| genshi_xml     | 63.3 ms                                                | 50.3 ms: 1.26x faster                                                |
| Geometric mean | (ref)                                                  | 1.32x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 141 us: 3.61x faster                                                 |
| generators               | 76.8 ms                                                | 31.0 ms: 2.48x faster                                                |
| deltablue                | 7.42 ms                                                | 3.51 ms: 2.11x faster                                                |
| async_tree_none          | 717 ms                                                 | 378 ms: 1.90x faster                                                 |
| richards_super           | 90.7 ms                                                | 49.6 ms: 1.83x faster                                                |
| asyncio_tcp              | 925 ms                                                 | 507 ms: 1.82x faster                                                 |
| logging_silent           | 175 ns                                                 | 98.9 ns: 1.77x faster                                                |
| richards                 | 74.9 ms                                                | 43.9 ms: 1.71x faster                                                |
| go                       | 229 ms                                                 | 135 ms: 1.70x faster                                                 |
| async_tree_memoization   | 854 ms                                                 | 506 ms: 1.69x faster                                                 |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                               |
| async_tree_io            | 1.77 sec                                               | 1.07 sec: 1.66x faster                                               |
| chaos                    | 106 ms                                                 | 64.1 ms: 1.66x faster                                                |
| scimark_sor              | 197 ms                                                 | 119 ms: 1.66x faster                                                 |
| raytrace                 | 464 ms                                                 | 297 ms: 1.56x faster                                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.32 ms: 1.56x faster                                                |
| hexiom                   | 9.53 ms                                                | 6.15 ms: 1.55x faster                                                |
| python_startup           | 14.2 ms                                                | 9.14 ms: 1.55x faster                                                |
| pyflate                  | 673 ms                                                 | 435 ms: 1.55x faster                                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 615 ms: 1.55x faster                                                 |
| nbody                    | 142 ms                                                 | 91.9 ms: 1.54x faster                                                |
| crypto_pyaes             | 118 ms                                                 | 78.0 ms: 1.52x faster                                                |
| scimark_monte_carlo      | 108 ms                                                 | 71.3 ms: 1.52x faster                                                |
| sqlglot_transpile        | 2.45 ms                                                | 1.64 ms: 1.49x faster                                                |
| pickle_pure_python       | 455 us                                                 | 311 us: 1.46x faster                                                 |
| scimark_lu               | 163 ms                                                 | 112 ms: 1.46x faster                                                 |
| coroutines               | 31.8 ms                                                | 22.0 ms: 1.44x faster                                                |
| spectral_norm            | 150 ms                                                 | 105 ms: 1.43x faster                                                 |
| unpickle_pure_python     | 300 us                                                 | 215 us: 1.40x faster                                                 |
| json_dumps               | 13.5 ms                                                | 9.75 ms: 1.39x faster                                                |
| float                    | 111 ms                                                 | 80.2 ms: 1.38x faster                                                |
| deepcopy_memo            | 52.3 us                                                | 38.1 us: 1.38x faster                                                |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                |
| genshi_text              | 30.3 ms                                                | 22.5 ms: 1.35x faster                                                |
| tomli_loads              | 2.92 sec                                               | 2.21 sec: 1.32x faster                                               |
| pprint_pformat           | 1.99 sec                                               | 1.50 sec: 1.32x faster                                               |
| html5lib                 | 85.9 ms                                                | 65.4 ms: 1.31x faster                                                |
| tornado_http             | 127 ms                                                 | 97.7 ms: 1.30x faster                                                |
| pprint_safe_repr         | 955 ms                                                 | 736 ms: 1.30x faster                                                 |
| comprehensions           | 26.8 us                                                | 20.8 us: 1.29x faster                                                |
| fannkuch                 | 486 ms                                                 | 379 ms: 1.28x faster                                                 |
| logging_simple           | 8.07 us                                                | 6.34 us: 1.27x faster                                                |
| xml_etree_process        | 74.9 ms                                                | 59.1 ms: 1.27x faster                                                |
| pycparser                | 1.50 sec                                               | 1.19 sec: 1.26x faster                                               |
| logging_format           | 8.91 us                                                | 7.06 us: 1.26x faster                                                |
| genshi_xml               | 63.3 ms                                                | 50.3 ms: 1.26x faster                                                |
| 2to3                     | 336 ms                                                 | 267 ms: 1.26x faster                                                 |
| sqlglot_normalize        | 135 ms                                                 | 108 ms: 1.25x faster                                                 |
| unpack_sequence          | 64.7 ns                                                | 51.7 ns: 1.25x faster                                                |
| nqueens                  | 100 ms                                                 | 80.6 ms: 1.24x faster                                                |
| deepcopy                 | 442 us                                                 | 359 us: 1.23x faster                                                 |
| sqlglot_optimize         | 65.3 ms                                                | 53.4 ms: 1.22x faster                                                |
| regex_compile            | 177 ms                                                 | 145 ms: 1.22x faster                                                 |
| scimark_fft              | 424 ms                                                 | 350 ms: 1.21x faster                                                 |
| deepcopy_reduce          | 3.82 us                                                | 3.22 us: 1.19x faster                                                |
| docutils                 | 3.17 sec                                               | 2.67 sec: 1.19x faster                                               |
| json_loads               | 28.8 us                                                | 24.9 us: 1.16x faster                                                |
| regex_v8                 | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                |
| json                     | 5.42 ms                                                | 4.72 ms: 1.15x faster                                                |
| bench_thread_pool        | 947 us                                                 | 829 us: 1.14x faster                                                 |
| dulwich_log              | 75.9 ms                                                | 68.0 ms: 1.12x faster                                                |
| meteor_contest           | 115 ms                                                 | 103 ms: 1.12x faster                                                 |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.12x faster                                                |
| xml_etree_generate       | 94.2 ms                                                | 84.9 ms: 1.11x faster                                                |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.92 ms: 1.11x faster                                                |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                 |
| gc_traversal             | 3.84 ms                                                | 3.54 ms: 1.08x faster                                                |
| pathlib                  | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                |
| sqlite_synth             | 2.93 us                                                | 2.71 us: 1.08x faster                                                |
| djangocms                | 35.9 us                                                | 33.3 us: 1.08x faster                                                |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                                 |
| regex_dna                | 222 ms                                                 | 208 ms: 1.07x faster                                                 |
| mdp                      | 2.82 sec                                               | 2.71 sec: 1.04x faster                                               |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                                |
| pickle_list              | 4.56 us                                                | 4.65 us: 1.02x slower                                                |
| pidigits                 | 190 ms                                                 | 196 ms: 1.03x slower                                                 |
| telco                    | 6.54 ms                                                | 6.78 ms: 1.04x slower                                                |
| async_generators         | 425 ms                                                 | 449 ms: 1.06x slower                                                 |
| unpickle_list            | 4.82 us                                                | 5.11 us: 1.06x slower                                                |
| unpickle                 | 14.1 us                                                | 15.1 us: 1.06x slower                                                |
| regex_effbot             | 3.23 ms                                                | 3.48 ms: 1.08x slower                                                |
| python_startup_no_site   | 5.82 ms                                                | 6.77 ms: 1.16x slower                                                |
| pickle_dict              | 27.3 us                                                | 32.9 us: 1.21x slower                                                |
| coverage                 | 72.8 ms                                                | 97.8 ms: 1.34x slower                                                |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                         |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, django_template, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
