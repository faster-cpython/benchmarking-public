
# Results vs. 3.10.4

- fork: carljm
- ref: inlinecomp2
- machine: linux-x86_64
- commit hash: 36b2917
- commit date: 2023-02-10
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                          |
| chameleon      | 9.06 ms                                                | 6.47 ms: 1.40x faster                                         |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.25x faster                                        |
| html5lib       | 85.9 ms                                                | 60.6 ms: 1.42x faster                                         |
| tornado_http   | 127 ms                                                 | 94.1 ms: 1.35x faster                                         |
| Geometric mean | (ref)                                                  | 1.35x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.8 ms: 1.52x faster                                         |
| nbody          | 142 ms                                                 | 94.0 ms: 1.51x faster                                         |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.31x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                          |
| regex_v8       | 25.0 ms                                                | 21.6 ms: 1.16x faster                                         |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                          |
| regex_effbot   | 3.23 ms                                                | 3.66 ms: 1.13x slower                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 291 us: 1.56x faster                                          |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.51x faster                                          |
| json_dumps           | 13.5 ms                                                | 9.39 ms: 1.44x faster                                         |
| xml_etree_process    | 74.9 ms                                                | 54.8 ms: 1.37x faster                                         |
| json_loads           | 28.8 us                                                | 23.7 us: 1.22x faster                                         |
| xml_etree_generate   | 94.2 ms                                                | 80.2 ms: 1.17x faster                                         |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.11x faster                                          |
| pickle_list          | 4.56 us                                                | 4.15 us: 1.10x faster                                         |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                          |
| unpickle             | 14.1 us                                                | 13.7 us: 1.04x faster                                         |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                         |
| unpickle_list        | 4.82 us                                                | 5.13 us: 1.06x slower                                         |
| pickle_dict          | 27.3 us                                                | 30.9 us: 1.13x slower                                         |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.90 ms: 1.59x faster                                         |
| python_startup_no_site | 5.82 ms                                                | 6.46 ms: 1.11x slower                                         |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.90 ms: 1.49x faster                                         |
| genshi_text     | 30.3 ms                                                | 20.9 ms: 1.45x faster                                         |
| django_template | 45.9 ms                                                | 32.6 ms: 1.41x faster                                         |
| genshi_xml      | 63.3 ms                                                | 47.8 ms: 1.32x faster                                         |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.13 ms: 2.37x faster                                         |
| logging_silent          | 175 ns                                                 | 94.1 ns: 1.86x faster                                         |
| asyncio_tcp             | 925 ms                                                 | 498 ms: 1.86x faster                                          |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                          |
| richards                | 74.9 ms                                                | 42.1 ms: 1.78x faster                                         |
| chaos                   | 106 ms                                                 | 63.2 ms: 1.68x faster                                         |
| pyflate                 | 673 ms                                                 | 403 ms: 1.67x faster                                          |
| go                      | 229 ms                                                 | 137 ms: 1.67x faster                                          |
| raytrace                | 464 ms                                                 | 279 ms: 1.66x faster                                          |
| scimark_monte_carlo     | 108 ms                                                 | 65.5 ms: 1.65x faster                                         |
| hexiom                  | 9.53 ms                                                | 5.87 ms: 1.62x faster                                         |
| crypto_pyaes            | 118 ms                                                 | 73.3 ms: 1.62x faster                                         |
| spectral_norm           | 150 ms                                                 | 93.9 ms: 1.60x faster                                         |
| python_startup          | 14.2 ms                                                | 8.90 ms: 1.59x faster                                         |
| pickle_pure_python      | 455 us                                                 | 291 us: 1.56x faster                                          |
| deepcopy_memo           | 52.3 us                                                | 34.1 us: 1.53x faster                                         |
| float                   | 111 ms                                                 | 72.8 ms: 1.52x faster                                         |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.51x faster                                          |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                          |
| nbody                   | 142 ms                                                 | 94.0 ms: 1.51x faster                                         |
| mako                    | 14.8 ms                                                | 9.90 ms: 1.49x faster                                         |
| unpack_sequence         | 64.7 ns                                                | 44.4 ns: 1.46x faster                                         |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                         |
| genshi_text             | 30.3 ms                                                | 20.9 ms: 1.45x faster                                         |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                        |
| json_dumps              | 13.5 ms                                                | 9.39 ms: 1.44x faster                                         |
| async_tree_none         | 717 ms                                                 | 498 ms: 1.44x faster                                          |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                         |
| pprint_safe_repr        | 955 ms                                                 | 668 ms: 1.43x faster                                          |
| html5lib                | 85.9 ms                                                | 60.6 ms: 1.42x faster                                         |
| django_template         | 45.9 ms                                                | 32.6 ms: 1.41x faster                                         |
| chameleon               | 9.06 ms                                                | 6.47 ms: 1.40x faster                                         |
| async_tree_memoization  | 854 ms                                                 | 612 ms: 1.40x faster                                          |
| logging_format          | 8.91 us                                                | 6.39 us: 1.39x faster                                         |
| async_tree_io           | 1.77 sec                                               | 1.27 sec: 1.39x faster                                        |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                          |
| logging_simple          | 8.07 us                                                | 5.83 us: 1.38x faster                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.94 ms: 1.38x faster                                         |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.38x faster                                        |
| scimark_fft             | 424 ms                                                 | 307 ms: 1.38x faster                                          |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                         |
| xml_etree_process       | 74.9 ms                                                | 54.8 ms: 1.37x faster                                         |
| deepcopy                | 442 us                                                 | 324 us: 1.37x faster                                          |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                         |
| thrift                  | 1.03 ms                                                | 760 us: 1.36x faster                                          |
| tornado_http            | 127 ms                                                 | 94.1 ms: 1.35x faster                                         |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                          |
| sqlglot_normalize       | 135 ms                                                 | 101 ms: 1.34x faster                                          |
| nqueens                 | 100 ms                                                 | 74.9 ms: 1.33x faster                                         |
| mypy2                   | 428 ms                                                 | 322 ms: 1.33x faster                                          |
| fannkuch                | 486 ms                                                 | 366 ms: 1.33x faster                                          |
| genshi_xml              | 63.3 ms                                                | 47.8 ms: 1.32x faster                                         |
| deepcopy_reduce         | 3.82 us                                                | 2.90 us: 1.32x faster                                         |
| sqlglot_optimize        | 65.3 ms                                                | 50.4 ms: 1.30x faster                                         |
| async_tree_cpu_io_mixed | 951 ms                                                 | 747 ms: 1.27x faster                                          |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.25x faster                                        |
| sympy_integrate         | 24.3 ms                                                | 19.5 ms: 1.25x faster                                         |
| sympy_expand            | 545 ms                                                 | 439 ms: 1.24x faster                                          |
| sympy_str               | 328 ms                                                 | 265 ms: 1.24x faster                                          |
| coroutines              | 31.8 ms                                                | 25.8 ms: 1.24x faster                                         |
| sqlalchemy_declarative  | 165 ms                                                 | 134 ms: 1.23x faster                                          |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.4 ms: 1.22x faster                                         |
| json_loads              | 28.8 us                                                | 23.7 us: 1.22x faster                                         |
| dulwich_log             | 75.9 ms                                                | 62.6 ms: 1.21x faster                                         |
| bench_thread_pool       | 947 us                                                 | 785 us: 1.21x faster                                          |
| sympy_sum               | 185 ms                                                 | 155 ms: 1.19x faster                                          |
| json                    | 5.42 ms                                                | 4.55 ms: 1.19x faster                                         |
| xml_etree_generate      | 94.2 ms                                                | 80.2 ms: 1.17x faster                                         |
| regex_v8                | 25.0 ms                                                | 21.6 ms: 1.16x faster                                         |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.14x faster                                         |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                         |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                         |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                          |
| djangocms               | 35.9 us                                                | 32.5 us: 1.11x faster                                         |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.11x faster                                          |
| pickle_list             | 4.56 us                                                | 4.15 us: 1.10x faster                                         |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.09x faster                                          |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                          |
| gc_traversal            | 3.84 ms                                                | 3.58 ms: 1.07x faster                                         |
| mdp                     | 2.82 sec                                               | 2.66 sec: 1.06x faster                                        |
| unpickle                | 14.1 us                                                | 13.7 us: 1.04x faster                                         |
| telco                   | 6.54 ms                                                | 6.40 ms: 1.02x faster                                         |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                         |
| async_generators        | 425 ms                                                 | 427 ms: 1.01x slower                                          |
| generators              | 76.8 ms                                                | 77.7 ms: 1.01x slower                                         |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                          |
| unpickle_list           | 4.82 us                                                | 5.13 us: 1.06x slower                                         |
| python_startup_no_site  | 5.82 ms                                                | 6.46 ms: 1.11x slower                                         |
| regex_effbot            | 3.23 ms                                                | 3.66 ms: 1.13x slower                                         |
| pickle_dict             | 27.3 us                                                | 30.9 us: 1.13x slower                                         |
| coverage                | 72.8 ms                                                | 99.3 ms: 1.36x slower                                         |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                  |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x
