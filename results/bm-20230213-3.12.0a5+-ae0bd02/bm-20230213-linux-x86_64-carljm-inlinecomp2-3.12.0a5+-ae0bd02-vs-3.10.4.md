
# Results vs. 3.10.4

- fork: carljm
- ref: inlinecomp2
- machine: linux-x86_64
- commit hash: ae0bd02
- commit date: 2023-02-13
- overall geometric mean: 1.32x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 245 ms: 1.37x faster                                          |
| chameleon      | 9.06 ms                                                | 6.44 ms: 1.41x faster                                         |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                        |
| html5lib       | 85.9 ms                                                | 60.8 ms: 1.41x faster                                         |
| tornado_http   | 127 ms                                                 | 94.9 ms: 1.34x faster                                         |
| Geometric mean | (ref)                                                  | 1.35x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.7 ms: 1.52x faster                                         |
| nbody          | 142 ms                                                 | 99.9 ms: 1.42x faster                                         |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                  | 1.29x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                          |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                         |
| regex_dna      | 222 ms                                                 | 200 ms: 1.11x faster                                          |
| regex_effbot   | 3.23 ms                                                | 3.50 ms: 1.08x slower                                         |
| Geometric mean | (ref)                                                  | 1.13x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                          |
| unpickle_pure_python | 300 us                                                 | 200 us: 1.50x faster                                          |
| json_dumps           | 13.5 ms                                                | 9.51 ms: 1.42x faster                                         |
| xml_etree_process    | 74.9 ms                                                | 55.2 ms: 1.36x faster                                         |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                         |
| xml_etree_generate   | 94.2 ms                                                | 80.4 ms: 1.17x faster                                         |
| xml_etree_iterparse  | 111 ms                                                 | 99.8 ms: 1.12x faster                                         |
| pickle_list          | 4.56 us                                                | 4.13 us: 1.10x faster                                         |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                          |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                         |
| pickle               | 10.3 us                                                | 10.0 us: 1.02x faster                                         |
| unpickle_list        | 4.82 us                                                | 5.04 us: 1.05x slower                                         |
| pickle_dict          | 27.3 us                                                | 30.7 us: 1.13x slower                                         |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.89 ms: 1.59x faster                                         |
| python_startup_no_site | 5.82 ms                                                | 6.45 ms: 1.11x slower                                         |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.0 ms: 1.47x faster                                         |
| genshi_text     | 30.3 ms                                                | 20.8 ms: 1.46x faster                                         |
| django_template | 45.9 ms                                                | 33.3 ms: 1.38x faster                                         |
| genshi_xml      | 63.3 ms                                                | 46.8 ms: 1.35x faster                                         |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.6 ms: 2.51x faster                                         |
| deltablue               | 7.42 ms                                                | 3.18 ms: 2.34x faster                                         |
| logging_silent          | 175 ns                                                 | 93.8 ns: 1.87x faster                                         |
| asyncio_tcp             | 925 ms                                                 | 502 ms: 1.84x faster                                          |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                          |
| richards                | 74.9 ms                                                | 43.1 ms: 1.74x faster                                         |
| pyflate                 | 673 ms                                                 | 402 ms: 1.67x faster                                          |
| scimark_monte_carlo     | 108 ms                                                 | 65.5 ms: 1.65x faster                                         |
| go                      | 229 ms                                                 | 139 ms: 1.64x faster                                          |
| raytrace                | 464 ms                                                 | 284 ms: 1.63x faster                                          |
| chaos                   | 106 ms                                                 | 65.2 ms: 1.63x faster                                         |
| crypto_pyaes            | 118 ms                                                 | 73.4 ms: 1.61x faster                                         |
| spectral_norm           | 150 ms                                                 | 93.5 ms: 1.60x faster                                         |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                          |
| python_startup          | 14.2 ms                                                | 8.89 ms: 1.59x faster                                         |
| hexiom                  | 9.53 ms                                                | 6.12 ms: 1.56x faster                                         |
| float                   | 111 ms                                                 | 72.7 ms: 1.52x faster                                         |
| unpickle_pure_python    | 300 us                                                 | 200 us: 1.50x faster                                          |
| deepcopy_memo           | 52.3 us                                                | 34.9 us: 1.50x faster                                         |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                          |
| mako                    | 14.8 ms                                                | 10.0 ms: 1.47x faster                                         |
| genshi_text             | 30.3 ms                                                | 20.8 ms: 1.46x faster                                         |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.45x faster                                         |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                        |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.43x faster                                         |
| unpack_sequence         | 64.7 ns                                                | 45.5 ns: 1.42x faster                                         |
| json_dumps              | 13.5 ms                                                | 9.51 ms: 1.42x faster                                         |
| nbody                   | 142 ms                                                 | 99.9 ms: 1.42x faster                                         |
| html5lib                | 85.9 ms                                                | 60.8 ms: 1.41x faster                                         |
| async_tree_none         | 717 ms                                                 | 507 ms: 1.41x faster                                          |
| scimark_fft             | 424 ms                                                 | 300 ms: 1.41x faster                                          |
| chameleon               | 9.06 ms                                                | 6.44 ms: 1.41x faster                                         |
| pprint_safe_repr        | 955 ms                                                 | 679 ms: 1.41x faster                                          |
| logging_format          | 8.91 us                                                | 6.34 us: 1.40x faster                                         |
| async_tree_io           | 1.77 sec                                               | 1.27 sec: 1.39x faster                                        |
| coroutines              | 31.8 ms                                                | 22.9 ms: 1.39x faster                                         |
| async_tree_memoization  | 854 ms                                                 | 615 ms: 1.39x faster                                          |
| logging_simple          | 8.07 us                                                | 5.82 us: 1.39x faster                                         |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                         |
| django_template         | 45.9 ms                                                | 33.3 ms: 1.38x faster                                         |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                          |
| thrift                  | 1.03 ms                                                | 754 us: 1.37x faster                                          |
| 2to3                    | 336 ms                                                 | 245 ms: 1.37x faster                                          |
| xml_etree_process       | 74.9 ms                                                | 55.2 ms: 1.36x faster                                         |
| sqlglot_normalize       | 135 ms                                                 | 99.7 ms: 1.36x faster                                         |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.36x faster                                        |
| genshi_xml              | 63.3 ms                                                | 46.8 ms: 1.35x faster                                         |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.06 ms: 1.34x faster                                         |
| tornado_http            | 127 ms                                                 | 94.9 ms: 1.34x faster                                         |
| deepcopy                | 442 us                                                 | 332 us: 1.33x faster                                          |
| mypy2                   | 428 ms                                                 | 325 ms: 1.32x faster                                          |
| sqlglot_optimize        | 65.3 ms                                                | 49.9 ms: 1.31x faster                                         |
| fannkuch                | 486 ms                                                 | 376 ms: 1.29x faster                                          |
| async_tree_cpu_io_mixed | 951 ms                                                 | 743 ms: 1.28x faster                                          |
| deepcopy_reduce         | 3.82 us                                                | 3.03 us: 1.26x faster                                         |
| nqueens                 | 100 ms                                                 | 79.7 ms: 1.25x faster                                         |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                        |
| sympy_integrate         | 24.3 ms                                                | 19.6 ms: 1.24x faster                                         |
| sqlalchemy_declarative  | 165 ms                                                 | 135 ms: 1.22x faster                                          |
| sympy_str               | 328 ms                                                 | 268 ms: 1.22x faster                                          |
| sympy_expand            | 545 ms                                                 | 446 ms: 1.22x faster                                          |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.4 ms: 1.22x faster                                         |
| dulwich_log             | 75.9 ms                                                | 62.9 ms: 1.21x faster                                         |
| bench_thread_pool       | 947 us                                                 | 786 us: 1.20x faster                                          |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                         |
| sympy_sum               | 185 ms                                                 | 156 ms: 1.18x faster                                          |
| xml_etree_generate      | 94.2 ms                                                | 80.4 ms: 1.17x faster                                         |
| create_gc_cycles        | 1.67 ms                                                | 1.44 ms: 1.16x faster                                         |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                         |
| sqlite_synth            | 2.93 us                                                | 2.63 us: 1.12x faster                                         |
| mdp                     | 2.82 sec                                               | 2.53 sec: 1.12x faster                                        |
| xml_etree_iterparse     | 111 ms                                                 | 99.8 ms: 1.12x faster                                         |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                         |
| json                    | 5.42 ms                                                | 4.85 ms: 1.12x faster                                         |
| regex_dna               | 222 ms                                                 | 200 ms: 1.11x faster                                          |
| pickle_list             | 4.56 us                                                | 4.13 us: 1.10x faster                                         |
| djangocms               | 35.9 us                                                | 32.5 us: 1.10x faster                                         |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                          |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                          |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                         |
| telco                   | 6.54 ms                                                | 6.33 ms: 1.03x faster                                         |
| async_generators        | 425 ms                                                 | 414 ms: 1.03x faster                                          |
| pickle                  | 10.3 us                                                | 10.0 us: 1.02x faster                                         |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                          |
| unpickle_list           | 4.82 us                                                | 5.04 us: 1.05x slower                                         |
| gc_traversal            | 3.84 ms                                                | 4.04 ms: 1.05x slower                                         |
| regex_effbot            | 3.23 ms                                                | 3.50 ms: 1.08x slower                                         |
| python_startup_no_site  | 5.82 ms                                                | 6.45 ms: 1.11x slower                                         |
| pickle_dict             | 27.3 us                                                | 30.7 us: 1.13x slower                                         |
| coverage                | 72.8 ms                                                | 98.2 ms: 1.35x slower                                         |
| Geometric mean          | (ref)                                                  | 1.32x faster                                                  |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x
