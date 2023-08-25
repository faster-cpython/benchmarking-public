
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: b9aa14a
- commit date: 2022-12-24
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                   |
| chameleon      | 9.06 ms                                                | 6.38 ms: 1.42x faster                                  |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                 |
| html5lib       | 85.9 ms                                                | 60.2 ms: 1.43x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 72.1 ms: 1.53x faster                                  |
| nbody          | 142 ms                                                 | 96.5 ms: 1.47x faster                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                  |
| regex_dna      | 222 ms                                                 | 206 ms: 1.08x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.40 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.61x faster                                   |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.52x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.42 ms: 1.44x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 53.3 ms: 1.41x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 75.9 ms: 1.24x faster                                  |
| json_loads           | 28.8 us                                                | 23.9 us: 1.21x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| unpickle             | 14.1 us                                                | 13.0 us: 1.09x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| pickle_list          | 4.56 us                                                | 4.25 us: 1.07x faster                                  |
| unpickle_list        | 4.82 us                                                | 4.91 us: 1.02x slower                                  |
| pickle_dict          | 27.3 us                                                | 32.4 us: 1.19x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.49 ms: 1.67x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.08 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.26x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.59 ms: 1.54x faster                                  |
| genshi_text     | 30.3 ms                                                | 20.9 ms: 1.45x faster                                  |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                  |
| genshi_xml      | 63.3 ms                                                | 49.0 ms: 1.29x faster                                  |
| Geometric mean  | (ref)                                                  | 1.42x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.27 ms: 2.27x faster                                  |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.89x faster                                   |
| logging_silent          | 175 ns                                                 | 94.8 ns: 1.85x faster                                  |
| richards                | 74.9 ms                                                | 41.8 ms: 1.79x faster                                  |
| pyflate                 | 673 ms                                                 | 403 ms: 1.67x faster                                   |
| python_startup          | 14.2 ms                                                | 8.49 ms: 1.67x faster                                  |
| go                      | 229 ms                                                 | 138 ms: 1.67x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 65.6 ms: 1.65x faster                                  |
| raytrace                | 464 ms                                                 | 282 ms: 1.65x faster                                   |
| pickle_pure_python      | 455 us                                                 | 282 us: 1.61x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 75.2 ms: 1.57x faster                                  |
| spectral_norm           | 150 ms                                                 | 95.4 ms: 1.57x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 33.4 us: 1.57x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.09 ms: 1.56x faster                                  |
| mako                    | 14.8 ms                                                | 9.59 ms: 1.54x faster                                  |
| float                   | 111 ms                                                 | 72.1 ms: 1.53x faster                                  |
| chaos                   | 106 ms                                                 | 69.6 ms: 1.53x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.52x faster                                   |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                   |
| unpack_sequence         | 64.7 ns                                                | 43.2 ns: 1.50x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.47x faster                                  |
| nbody                   | 142 ms                                                 | 96.5 ms: 1.47x faster                                  |
| genshi_text             | 30.3 ms                                                | 20.9 ms: 1.45x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                 |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.42 ms: 1.44x faster                                  |
| html5lib                | 85.9 ms                                                | 60.2 ms: 1.43x faster                                  |
| logging_simple          | 8.07 us                                                | 5.67 us: 1.42x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 671 ms: 1.42x faster                                   |
| chameleon               | 9.06 ms                                                | 6.38 ms: 1.42x faster                                  |
| logging_format          | 8.91 us                                                | 6.29 us: 1.42x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 53.3 ms: 1.41x faster                                  |
| django_template         | 45.9 ms                                                | 33.0 ms: 1.39x faster                                  |
| thrift                  | 1.03 ms                                                | 750 us: 1.38x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 622 ms: 1.37x faster                                   |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.37x faster                                 |
| async_tree_none         | 717 ms                                                 | 525 ms: 1.37x faster                                   |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.35x faster                                 |
| scimark_fft             | 424 ms                                                 | 316 ms: 1.34x faster                                   |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                   |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.95 us: 1.30x faster                                  |
| fannkuch                | 486 ms                                                 | 375 ms: 1.30x faster                                   |
| genshi_xml              | 63.3 ms                                                | 49.0 ms: 1.29x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.9 ms: 1.28x faster                                  |
| coroutines              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.25 ms: 1.28x faster                                  |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                 |
| nqueens                 | 100 ms                                                 | 79.1 ms: 1.26x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 759 ms: 1.25x faster                                   |
| xml_etree_generate      | 94.2 ms                                                | 75.9 ms: 1.24x faster                                  |
| dulwich_log             | 75.9 ms                                                | 62.3 ms: 1.22x faster                                  |
| bench_thread_pool       | 947 us                                                 | 781 us: 1.21x faster                                   |
| json_loads              | 28.8 us                                                | 23.9 us: 1.21x faster                                  |
| async_generators        | 425 ms                                                 | 353 ms: 1.21x faster                                   |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.19x faster                                  |
| sympy_expand            | 545 ms                                                 | 456 ms: 1.19x faster                                   |
| sympy_str               | 328 ms                                                 | 281 ms: 1.17x faster                                   |
| sqlite_synth            | 2.93 us                                                | 2.56 us: 1.15x faster                                  |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                  |
| json                    | 5.42 ms                                                | 4.74 ms: 1.14x faster                                  |
| sympy_sum               | 185 ms                                                 | 162 ms: 1.14x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                  |
| djangocms               | 35.9 us                                                | 32.2 us: 1.12x faster                                  |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                   |
| mdp                     | 2.82 sec                                               | 2.54 sec: 1.11x faster                                 |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| unpickle                | 14.1 us                                                | 13.0 us: 1.09x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| regex_dna               | 222 ms                                                 | 206 ms: 1.08x faster                                   |
| pickle_list             | 4.56 us                                                | 4.25 us: 1.07x faster                                  |
| telco                   | 6.54 ms                                                | 6.25 ms: 1.05x faster                                  |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| generators              | 76.8 ms                                                | 77.6 ms: 1.01x slower                                  |
| unpickle_list           | 4.82 us                                                | 4.91 us: 1.02x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.08 ms: 1.05x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.40 ms: 1.05x slower                                  |
| pickle_dict             | 27.3 us                                                | 32.4 us: 1.19x slower                                  |
| coverage                | 72.8 ms                                                | 98.1 ms: 1.35x slower                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                           |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221224-3.12.0a3+-b9aa14a/bm-20221224-linux-x86_64-python-main-3.12.0a3+-b9aa14a.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x
