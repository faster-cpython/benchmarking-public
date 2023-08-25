
# Results vs. 3.10.4

- fork: carljm
- ref: inlinecomp2
- machine: linux-x86_64
- commit hash: 9f0fc5b
- commit date: 2023-02-20
- overall geometric mean: 1.32x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 248 ms: 1.36x faster                                          |
| chameleon      | 9.06 ms                                                | 6.32 ms: 1.43x faster                                         |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.25x faster                                        |
| html5lib       | 85.9 ms                                                | 60.4 ms: 1.42x faster                                         |
| tornado_http   | 127 ms                                                 | 94.3 ms: 1.35x faster                                         |
| Geometric mean | (ref)                                                  | 1.36x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.0 ms: 1.54x faster                                         |
| nbody          | 142 ms                                                 | 94.0 ms: 1.51x faster                                         |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                  | 1.32x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                          |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                         |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                          |
| regex_effbot   | 3.23 ms                                                | 3.69 ms: 1.14x slower                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 281 us: 1.62x faster                                          |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.52x faster                                          |
| json_dumps           | 13.5 ms                                                | 9.49 ms: 1.43x faster                                         |
| xml_etree_process    | 74.9 ms                                                | 55.5 ms: 1.35x faster                                         |
| json_loads           | 28.8 us                                                | 24.1 us: 1.20x faster                                         |
| xml_etree_generate   | 94.2 ms                                                | 80.6 ms: 1.17x faster                                         |
| pickle_list          | 4.56 us                                                | 3.97 us: 1.15x faster                                         |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                          |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                          |
| unpickle             | 14.1 us                                                | 13.4 us: 1.05x faster                                         |
| pickle               | 10.3 us                                                | 10.0 us: 1.03x faster                                         |
| unpickle_list        | 4.82 us                                                | 5.13 us: 1.06x slower                                         |
| pickle_dict          | 27.3 us                                                | 30.0 us: 1.10x slower                                         |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.96 ms: 1.58x faster                                         |
| python_startup_no_site | 5.82 ms                                                | 6.50 ms: 1.12x slower                                         |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.83 ms: 1.50x faster                                         |
| genshi_text     | 30.3 ms                                                | 20.8 ms: 1.46x faster                                         |
| django_template | 45.9 ms                                                | 32.7 ms: 1.40x faster                                         |
| genshi_xml      | 63.3 ms                                                | 47.9 ms: 1.32x faster                                         |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.9 ms: 2.56x faster                                         |
| deltablue               | 7.42 ms                                                | 3.16 ms: 2.35x faster                                         |
| logging_silent          | 175 ns                                                 | 91.7 ns: 1.91x faster                                         |
| asyncio_tcp             | 925 ms                                                 | 502 ms: 1.84x faster                                          |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                          |
| richards                | 74.9 ms                                                | 41.3 ms: 1.81x faster                                         |
| go                      | 229 ms                                                 | 131 ms: 1.75x faster                                          |
| pyflate                 | 673 ms                                                 | 398 ms: 1.69x faster                                          |
| scimark_monte_carlo     | 108 ms                                                 | 64.7 ms: 1.67x faster                                         |
| chaos                   | 106 ms                                                 | 63.5 ms: 1.67x faster                                         |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                          |
| pickle_pure_python      | 455 us                                                 | 281 us: 1.62x faster                                          |
| crypto_pyaes            | 118 ms                                                 | 73.7 ms: 1.61x faster                                         |
| hexiom                  | 9.53 ms                                                | 5.94 ms: 1.60x faster                                         |
| python_startup          | 14.2 ms                                                | 8.96 ms: 1.58x faster                                         |
| spectral_norm           | 150 ms                                                 | 96.2 ms: 1.56x faster                                         |
| float                   | 111 ms                                                 | 72.0 ms: 1.54x faster                                         |
| deepcopy_memo           | 52.3 us                                                | 34.2 us: 1.53x faster                                         |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.52x faster                                          |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                          |
| unpack_sequence         | 64.7 ns                                                | 42.9 ns: 1.51x faster                                         |
| nbody                   | 142 ms                                                 | 94.0 ms: 1.51x faster                                         |
| mako                    | 14.8 ms                                                | 9.83 ms: 1.50x faster                                         |
| coroutines              | 31.8 ms                                                | 21.8 ms: 1.46x faster                                         |
| genshi_text             | 30.3 ms                                                | 20.8 ms: 1.46x faster                                         |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                        |
| chameleon               | 9.06 ms                                                | 6.32 ms: 1.43x faster                                         |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.43x faster                                         |
| json_dumps              | 13.5 ms                                                | 9.49 ms: 1.43x faster                                         |
| pprint_safe_repr        | 955 ms                                                 | 671 ms: 1.42x faster                                          |
| html5lib                | 85.9 ms                                                | 60.4 ms: 1.42x faster                                         |
| async_tree_none         | 717 ms                                                 | 505 ms: 1.42x faster                                          |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.42x faster                                         |
| logging_format          | 8.91 us                                                | 6.33 us: 1.41x faster                                         |
| logging_simple          | 8.07 us                                                | 5.73 us: 1.41x faster                                         |
| async_tree_io           | 1.77 sec                                               | 1.26 sec: 1.41x faster                                        |
| django_template         | 45.9 ms                                                | 32.7 ms: 1.40x faster                                         |
| async_tree_memoization  | 854 ms                                                 | 611 ms: 1.40x faster                                          |
| thrift                  | 1.03 ms                                                | 742 us: 1.39x faster                                          |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                          |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.93 ms: 1.39x faster                                         |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                         |
| scimark_fft             | 424 ms                                                 | 309 ms: 1.37x faster                                          |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                         |
| 2to3                    | 336 ms                                                 | 248 ms: 1.36x faster                                          |
| sqlglot_normalize       | 135 ms                                                 | 99.8 ms: 1.36x faster                                         |
| tornado_http            | 127 ms                                                 | 94.3 ms: 1.35x faster                                         |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                        |
| xml_etree_process       | 74.9 ms                                                | 55.5 ms: 1.35x faster                                         |
| deepcopy                | 442 us                                                 | 328 us: 1.35x faster                                          |
| fannkuch                | 486 ms                                                 | 368 ms: 1.32x faster                                          |
| genshi_xml              | 63.3 ms                                                | 47.9 ms: 1.32x faster                                         |
| sqlglot_optimize        | 65.3 ms                                                | 49.7 ms: 1.32x faster                                         |
| mypy2                   | 428 ms                                                 | 326 ms: 1.31x faster                                          |
| deepcopy_reduce         | 3.82 us                                                | 2.96 us: 1.29x faster                                         |
| async_tree_cpu_io_mixed | 951 ms                                                 | 739 ms: 1.29x faster                                          |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.25x faster                                        |
| nqueens                 | 100 ms                                                 | 80.3 ms: 1.25x faster                                         |
| sympy_expand            | 545 ms                                                 | 444 ms: 1.23x faster                                          |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.5 ms: 1.21x faster                                         |
| sympy_integrate         | 24.3 ms                                                | 20.1 ms: 1.21x faster                                         |
| bench_thread_pool       | 947 us                                                 | 783 us: 1.21x faster                                          |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.20x faster                                          |
| json_loads              | 28.8 us                                                | 24.1 us: 1.20x faster                                         |
| dulwich_log             | 75.9 ms                                                | 63.6 ms: 1.19x faster                                         |
| sympy_str               | 328 ms                                                 | 278 ms: 1.18x faster                                          |
| json                    | 5.42 ms                                                | 4.61 ms: 1.17x faster                                         |
| xml_etree_generate      | 94.2 ms                                                | 80.6 ms: 1.17x faster                                         |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                         |
| pickle_list             | 4.56 us                                                | 3.97 us: 1.15x faster                                         |
| mdp                     | 2.82 sec                                               | 2.48 sec: 1.14x faster                                        |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                         |
| sympy_sum               | 185 ms                                                 | 164 ms: 1.13x faster                                          |
| sqlite_synth            | 2.93 us                                                | 2.63 us: 1.12x faster                                         |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.12x faster                                          |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                          |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                         |
| pathlib                 | 20.0 ms                                                | 18.3 ms: 1.10x faster                                         |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                          |
| regex_dna               | 222 ms                                                 | 207 ms: 1.07x faster                                          |
| unpickle                | 14.1 us                                                | 13.4 us: 1.05x faster                                         |
| pickle                  | 10.3 us                                                | 10.0 us: 1.03x faster                                         |
| telco                   | 6.54 ms                                                | 6.42 ms: 1.02x faster                                         |
| async_generators        | 425 ms                                                 | 417 ms: 1.02x faster                                          |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                          |
| unpickle_list           | 4.82 us                                                | 5.13 us: 1.06x slower                                         |
| gc_traversal            | 3.84 ms                                                | 4.18 ms: 1.09x slower                                         |
| pickle_dict             | 27.3 us                                                | 30.0 us: 1.10x slower                                         |
| python_startup_no_site  | 5.82 ms                                                | 6.50 ms: 1.12x slower                                         |
| regex_effbot            | 3.23 ms                                                | 3.69 ms: 1.14x slower                                         |
| dask                    | 423 ms                                                 | 498 ms: 1.18x slower                                          |
| coverage                | 72.8 ms                                                | 96.1 ms: 1.32x slower                                         |
| Geometric mean          | (ref)                                                  | 1.32x faster                                                  |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x
