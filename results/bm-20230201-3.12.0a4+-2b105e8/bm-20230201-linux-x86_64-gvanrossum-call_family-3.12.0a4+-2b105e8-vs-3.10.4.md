
# Results vs. 3.10.4

- fork: gvanrossum
- ref: call_family
- machine: linux-x86_64
- commit hash: 2b105e8
- commit date: 2023-02-01
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                              |
| chameleon      | 9.06 ms                                                | 6.42 ms: 1.41x faster                                             |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                            |
| html5lib       | 85.9 ms                                                | 59.4 ms: 1.45x faster                                             |
| tornado_http   | 127 ms                                                 | 94.3 ms: 1.35x faster                                             |
| Geometric mean | (ref)                                                  | 1.36x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.8 ms: 1.52x faster                                             |
| nbody          | 142 ms                                                 | 94.5 ms: 1.50x faster                                             |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.30x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.40x faster                                              |
| regex_v8       | 25.0 ms                                                | 21.5 ms: 1.16x faster                                             |
| regex_dna      | 222 ms                                                 | 213 ms: 1.04x faster                                              |
| regex_effbot   | 3.23 ms                                                | 3.62 ms: 1.12x slower                                             |
| Geometric mean | (ref)                                                  | 1.11x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                              |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.52x faster                                              |
| json_dumps           | 13.5 ms                                                | 9.40 ms: 1.44x faster                                             |
| xml_etree_process    | 74.9 ms                                                | 53.3 ms: 1.41x faster                                             |
| xml_etree_generate   | 94.2 ms                                                | 77.2 ms: 1.22x faster                                             |
| json_loads           | 28.8 us                                                | 23.8 us: 1.21x faster                                             |
| pickle_list          | 4.56 us                                                | 3.99 us: 1.14x faster                                             |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                              |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                             |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                             |
| unpickle_list        | 4.82 us                                                | 5.03 us: 1.04x slower                                             |
| pickle_dict          | 27.3 us                                                | 30.6 us: 1.12x slower                                             |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.95 ms: 1.58x faster                                             |
| python_startup_no_site | 5.82 ms                                                | 6.48 ms: 1.11x slower                                             |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.73 ms: 1.52x faster                                             |
| genshi_text     | 30.3 ms                                                | 20.8 ms: 1.46x faster                                             |
| django_template | 45.9 ms                                                | 32.1 ms: 1.43x faster                                             |
| genshi_xml      | 63.3 ms                                                | 46.2 ms: 1.37x faster                                             |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.13 ms: 2.37x faster                                             |
| logging_silent          | 175 ns                                                 | 91.1 ns: 1.92x faster                                             |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                              |
| asyncio_tcp             | 925 ms                                                 | 495 ms: 1.87x faster                                              |
| richards                | 74.9 ms                                                | 41.8 ms: 1.79x faster                                             |
| go                      | 229 ms                                                 | 133 ms: 1.72x faster                                              |
| pyflate                 | 673 ms                                                 | 395 ms: 1.71x faster                                              |
| chaos                   | 106 ms                                                 | 63.0 ms: 1.69x faster                                             |
| raytrace                | 464 ms                                                 | 280 ms: 1.66x faster                                              |
| scimark_monte_carlo     | 108 ms                                                 | 65.9 ms: 1.64x faster                                             |
| crypto_pyaes            | 118 ms                                                 | 73.7 ms: 1.61x faster                                             |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                              |
| hexiom                  | 9.53 ms                                                | 5.94 ms: 1.60x faster                                             |
| python_startup          | 14.2 ms                                                | 8.95 ms: 1.58x faster                                             |
| scimark_lu              | 163 ms                                                 | 105 ms: 1.55x faster                                              |
| spectral_norm           | 150 ms                                                 | 97.2 ms: 1.54x faster                                             |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.52x faster                                              |
| unpack_sequence         | 64.7 ns                                                | 42.6 ns: 1.52x faster                                             |
| float                   | 111 ms                                                 | 72.8 ms: 1.52x faster                                             |
| mako                    | 14.8 ms                                                | 9.73 ms: 1.52x faster                                             |
| deepcopy_memo           | 52.3 us                                                | 34.9 us: 1.50x faster                                             |
| nbody                   | 142 ms                                                 | 94.5 ms: 1.50x faster                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                             |
| genshi_text             | 30.3 ms                                                | 20.8 ms: 1.46x faster                                             |
| html5lib                | 85.9 ms                                                | 59.4 ms: 1.45x faster                                             |
| json_dumps              | 13.5 ms                                                | 9.40 ms: 1.44x faster                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                             |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.43x faster                                            |
| django_template         | 45.9 ms                                                | 32.1 ms: 1.43x faster                                             |
| pprint_safe_repr        | 955 ms                                                 | 674 ms: 1.42x faster                                              |
| chameleon               | 9.06 ms                                                | 6.42 ms: 1.41x faster                                             |
| xml_etree_process       | 74.9 ms                                                | 53.3 ms: 1.41x faster                                             |
| logging_format          | 8.91 us                                                | 6.37 us: 1.40x faster                                             |
| regex_compile           | 177 ms                                                 | 127 ms: 1.40x faster                                              |
| logging_simple          | 8.07 us                                                | 5.81 us: 1.39x faster                                             |
| aiohttp                 | 1.38 ms                                                | 999 us: 1.38x faster                                              |
| thrift                  | 1.03 ms                                                | 751 us: 1.38x faster                                              |
| genshi_xml              | 63.3 ms                                                | 46.2 ms: 1.37x faster                                             |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.37x faster                                            |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                              |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                             |
| scimark_fft             | 424 ms                                                 | 313 ms: 1.35x faster                                              |
| tornado_http            | 127 ms                                                 | 94.3 ms: 1.35x faster                                             |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                            |
| deepcopy                | 442 us                                                 | 329 us: 1.34x faster                                              |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                              |
| fannkuch                | 486 ms                                                 | 363 ms: 1.34x faster                                              |
| deepcopy_reduce         | 3.82 us                                                | 2.88 us: 1.33x faster                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.13 ms: 1.32x faster                                             |
| coroutines              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                             |
| nqueens                 | 100 ms                                                 | 77.3 ms: 1.29x faster                                             |
| async_tree_memoization  | 854 ms                                                 | 664 ms: 1.29x faster                                              |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                              |
| sqlglot_optimize        | 65.3 ms                                                | 51.1 ms: 1.28x faster                                             |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                            |
| async_tree_cpu_io_mixed | 951 ms                                                 | 754 ms: 1.26x faster                                              |
| sympy_integrate         | 24.3 ms                                                | 19.7 ms: 1.23x faster                                             |
| async_generators        | 425 ms                                                 | 348 ms: 1.22x faster                                              |
| xml_etree_generate      | 94.2 ms                                                | 77.2 ms: 1.22x faster                                             |
| bench_thread_pool       | 947 us                                                 | 779 us: 1.22x faster                                              |
| sympy_str               | 328 ms                                                 | 270 ms: 1.22x faster                                              |
| json_loads              | 28.8 us                                                | 23.8 us: 1.21x faster                                             |
| sympy_expand            | 545 ms                                                 | 453 ms: 1.20x faster                                              |
| dulwich_log             | 75.9 ms                                                | 63.3 ms: 1.20x faster                                             |
| sympy_sum               | 185 ms                                                 | 156 ms: 1.19x faster                                              |
| json                    | 5.42 ms                                                | 4.65 ms: 1.16x faster                                             |
| regex_v8                | 25.0 ms                                                | 21.5 ms: 1.16x faster                                             |
| pickle_list             | 4.56 us                                                | 3.99 us: 1.14x faster                                             |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                             |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                             |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                             |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                              |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                             |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                              |
| mdp                     | 2.82 sec                                               | 2.60 sec: 1.08x faster                                            |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                             |
| regex_dna               | 222 ms                                                 | 213 ms: 1.04x faster                                              |
| telco                   | 6.54 ms                                                | 6.36 ms: 1.03x faster                                             |
| generators              | 76.8 ms                                                | 74.9 ms: 1.03x faster                                             |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                             |
| gc_traversal            | 3.84 ms                                                | 3.96 ms: 1.03x slower                                             |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                              |
| unpickle_list           | 4.82 us                                                | 5.03 us: 1.04x slower                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.48 ms: 1.11x slower                                             |
| regex_effbot            | 3.23 ms                                                | 3.62 ms: 1.12x slower                                             |
| pickle_dict             | 27.3 us                                                | 30.6 us: 1.12x slower                                             |
| dask                    | 423 ms                                                 | 498 ms: 1.18x slower                                              |
| coverage                | 72.8 ms                                                | 97.1 ms: 1.33x slower                                             |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230201-3.12.0a4+-2b105e8/bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
