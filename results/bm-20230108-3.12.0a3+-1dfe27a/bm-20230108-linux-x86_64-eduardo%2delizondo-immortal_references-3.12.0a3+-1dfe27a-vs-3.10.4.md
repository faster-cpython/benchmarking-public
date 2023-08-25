
# Results vs. 3.10.4

- fork: eduardo-elizondo
- ref: immortal_references
- machine: linux-x86_64
- commit hash: 1dfe27a
- commit date: 2023-01-08
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 274 ms: 1.23x faster                                                              |
| chameleon      | 9.06 ms                                                | 6.83 ms: 1.33x faster                                                             |
| docutils       | 3.17 sec                                               | 2.69 sec: 1.18x faster                                                            |
| html5lib       | 85.9 ms                                                | 64.0 ms: 1.34x faster                                                             |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 96.7 ms: 1.46x faster                                                             |
| float          | 111 ms                                                 | 79.7 ms: 1.39x faster                                                             |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 144 ms: 1.23x faster                                                              |
| regex_v8       | 25.0 ms                                                | 21.1 ms: 1.19x faster                                                             |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                                              |
| regex_effbot   | 3.23 ms                                                | 3.39 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 309 us: 1.47x faster                                                              |
| json_dumps           | 13.5 ms                                                | 9.78 ms: 1.38x faster                                                             |
| unpickle_pure_python | 300 us                                                 | 217 us: 1.38x faster                                                              |
| xml_etree_process    | 74.9 ms                                                | 56.7 ms: 1.32x faster                                                             |
| xml_etree_generate   | 94.2 ms                                                | 79.5 ms: 1.19x faster                                                             |
| json_loads           | 28.8 us                                                | 26.6 us: 1.08x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 151 ms: 1.08x faster                                                              |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                              |
| pickle_list          | 4.56 us                                                | 4.35 us: 1.05x faster                                                             |
| unpickle             | 14.1 us                                                | 13.7 us: 1.03x faster                                                             |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                             |
| pickle_dict          | 27.3 us                                                | 30.5 us: 1.12x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                      |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.77 ms: 1.61x faster                                                             |
| python_startup_no_site | 5.82 ms                                                | 6.21 ms: 1.07x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.23x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.5 ms: 1.41x faster                                                             |
| genshi_text     | 30.3 ms                                                | 22.2 ms: 1.37x faster                                                             |
| django_template | 45.9 ms                                                | 34.8 ms: 1.32x faster                                                             |
| genshi_xml      | 63.3 ms                                                | 51.0 ms: 1.24x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.68 ms: 2.01x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 514 ms: 1.80x faster                                                              |
| logging_silent          | 175 ns                                                 | 101 ns: 1.74x faster                                                              |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                                              |
| richards                | 74.9 ms                                                | 44.9 ms: 1.67x faster                                                             |
| scimark_sor             | 197 ms                                                 | 121 ms: 1.63x faster                                                              |
| python_startup          | 14.2 ms                                                | 8.77 ms: 1.61x faster                                                             |
| pyflate                 | 673 ms                                                 | 429 ms: 1.57x faster                                                              |
| scimark_monte_carlo     | 108 ms                                                 | 69.6 ms: 1.56x faster                                                             |
| chaos                   | 106 ms                                                 | 69.2 ms: 1.54x faster                                                             |
| raytrace                | 464 ms                                                 | 309 ms: 1.50x faster                                                              |
| crypto_pyaes            | 118 ms                                                 | 79.0 ms: 1.50x faster                                                             |
| hexiom                  | 9.53 ms                                                | 6.38 ms: 1.49x faster                                                             |
| pickle_pure_python      | 455 us                                                 | 309 us: 1.47x faster                                                              |
| nbody                   | 142 ms                                                 | 96.7 ms: 1.46x faster                                                             |
| scimark_lu              | 163 ms                                                 | 115 ms: 1.42x faster                                                              |
| spectral_norm           | 150 ms                                                 | 106 ms: 1.41x faster                                                              |
| mako                    | 14.8 ms                                                | 10.5 ms: 1.41x faster                                                             |
| float                   | 111 ms                                                 | 79.7 ms: 1.39x faster                                                             |
| json_dumps              | 13.5 ms                                                | 9.78 ms: 1.38x faster                                                             |
| unpickle_pure_python    | 300 us                                                 | 217 us: 1.38x faster                                                              |
| deepcopy_memo           | 52.3 us                                                | 38.0 us: 1.38x faster                                                             |
| genshi_text             | 30.3 ms                                                | 22.2 ms: 1.37x faster                                                             |
| html5lib                | 85.9 ms                                                | 64.0 ms: 1.34x faster                                                             |
| async_tree_none         | 717 ms                                                 | 536 ms: 1.34x faster                                                              |
| pprint_pformat          | 1.99 sec                                               | 1.49 sec: 1.34x faster                                                            |
| thrift                  | 1.03 ms                                                | 775 us: 1.33x faster                                                              |
| sqlglot_parse           | 2.06 ms                                                | 1.55 ms: 1.33x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.34 sec: 1.33x faster                                                            |
| chameleon               | 9.06 ms                                                | 6.83 ms: 1.33x faster                                                             |
| xml_etree_process       | 74.9 ms                                                | 56.7 ms: 1.32x faster                                                             |
| django_template         | 45.9 ms                                                | 34.8 ms: 1.32x faster                                                             |
| pprint_safe_repr        | 955 ms                                                 | 729 ms: 1.31x faster                                                              |
| sqlglot_transpile       | 2.45 ms                                                | 1.87 ms: 1.31x faster                                                             |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.30x faster                                                            |
| logging_format          | 8.91 us                                                | 6.96 us: 1.28x faster                                                             |
| logging_simple          | 8.07 us                                                | 6.31 us: 1.28x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.34 ms: 1.26x faster                                                             |
| fannkuch                | 486 ms                                                 | 387 ms: 1.26x faster                                                              |
| unpack_sequence         | 64.7 ns                                                | 51.6 ns: 1.25x faster                                                             |
| nqueens                 | 100 ms                                                 | 80.1 ms: 1.25x faster                                                             |
| async_tree_cpu_io_mixed | 951 ms                                                 | 765 ms: 1.24x faster                                                              |
| async_tree_memoization  | 854 ms                                                 | 688 ms: 1.24x faster                                                              |
| genshi_xml              | 63.3 ms                                                | 51.0 ms: 1.24x faster                                                             |
| 2to3                    | 336 ms                                                 | 274 ms: 1.23x faster                                                              |
| regex_compile           | 177 ms                                                 | 144 ms: 1.23x faster                                                              |
| deepcopy                | 442 us                                                 | 366 us: 1.21x faster                                                              |
| coroutines              | 31.8 ms                                                | 26.6 ms: 1.20x faster                                                             |
| sqlglot_normalize       | 135 ms                                                 | 114 ms: 1.19x faster                                                              |
| deepcopy_reduce         | 3.82 us                                                | 3.21 us: 1.19x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.1 ms: 1.19x faster                                                             |
| xml_etree_generate      | 94.2 ms                                                | 79.5 ms: 1.19x faster                                                             |
| sqlglot_optimize        | 65.3 ms                                                | 55.2 ms: 1.18x faster                                                             |
| scimark_fft             | 424 ms                                                 | 359 ms: 1.18x faster                                                              |
| docutils                | 3.17 sec                                               | 2.69 sec: 1.18x faster                                                            |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                                             |
| bench_thread_pool       | 947 us                                                 | 834 us: 1.14x faster                                                              |
| async_generators        | 425 ms                                                 | 375 ms: 1.13x faster                                                              |
| sqlite_synth            | 2.93 us                                                | 2.65 us: 1.11x faster                                                             |
| dulwich_log             | 75.9 ms                                                | 68.7 ms: 1.11x faster                                                             |
| sympy_integrate         | 24.3 ms                                                | 22.0 ms: 1.10x faster                                                             |
| regex_dna               | 222 ms                                                 | 203 ms: 1.09x faster                                                              |
| sympy_expand            | 545 ms                                                 | 501 ms: 1.09x faster                                                              |
| pathlib                 | 20.0 ms                                                | 18.4 ms: 1.09x faster                                                             |
| json                    | 5.42 ms                                                | 5.00 ms: 1.08x faster                                                             |
| json_loads              | 28.8 us                                                | 26.6 us: 1.08x faster                                                             |
| xml_etree_parse         | 163 ms                                                 | 151 ms: 1.08x faster                                                              |
| mdp                     | 2.82 sec                                               | 2.61 sec: 1.08x faster                                                            |
| djangocms               | 35.9 us                                                | 33.6 us: 1.07x faster                                                             |
| sympy_str               | 328 ms                                                 | 311 ms: 1.06x faster                                                              |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                                              |
| pickle_list             | 4.56 us                                                | 4.35 us: 1.05x faster                                                             |
| unpickle                | 14.1 us                                                | 13.7 us: 1.03x faster                                                             |
| sympy_sum               | 185 ms                                                 | 182 ms: 1.02x faster                                                              |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                                              |
| telco                   | 6.54 ms                                                | 6.64 ms: 1.01x slower                                                             |
| gc_traversal            | 3.84 ms                                                | 3.90 ms: 1.02x slower                                                             |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                                             |
| generators              | 76.8 ms                                                | 80.5 ms: 1.05x slower                                                             |
| regex_effbot            | 3.23 ms                                                | 3.39 ms: 1.05x slower                                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.21 ms: 1.07x slower                                                             |
| pickle_dict             | 27.3 us                                                | 30.5 us: 1.12x slower                                                             |
| dask                    | 423 ms                                                 | 545 ms: 1.29x slower                                                              |
| coverage                | 72.8 ms                                                | 102 ms: 1.40x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.23x faster                                                                      |

Benchmark hidden because not significant (3): unpickle_list, bench_mp_pool, meteor_contest
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230108-3.12.0a3+-1dfe27a/bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x
