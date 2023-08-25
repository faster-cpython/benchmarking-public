
# Results vs. 3.10.4

- fork: Fidget_Spinner
- ref: per_class_cache
- machine: linux-x86_64
- commit hash: 78c9301
- commit date: 2023-01-09
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 254 ms: 1.33x faster                                                      |
| chameleon      | 9.06 ms                                                | 6.26 ms: 1.45x faster                                                     |
| docutils       | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                    |
| html5lib       | 85.9 ms                                                | 60.3 ms: 1.42x faster                                                     |
| Geometric mean | (ref)                                                  | 1.36x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.8 ms: 1.52x faster                                                     |
| nbody          | 142 ms                                                 | 94.9 ms: 1.49x faster                                                     |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.31x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.37x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                     |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.55 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 288 us: 1.58x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.48 ms: 1.43x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 53.9 ms: 1.39x faster                                                     |
| xml_etree_generate   | 94.2 ms                                                | 77.1 ms: 1.22x faster                                                     |
| json_loads           | 28.8 us                                                | 24.3 us: 1.19x faster                                                     |
| pickle_list          | 4.56 us                                                | 4.15 us: 1.10x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.06x faster                                                      |
| pickle               | 10.3 us                                                | 9.89 us: 1.04x faster                                                     |
| unpickle             | 14.1 us                                                | 13.7 us: 1.03x faster                                                     |
| unpickle_list        | 4.82 us                                                | 4.95 us: 1.03x slower                                                     |
| pickle_dict          | 27.3 us                                                | 30.2 us: 1.11x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.48 ms: 1.67x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.07 ms: 1.04x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.89 ms: 1.49x faster                                                     |
| genshi_text     | 30.3 ms                                                | 20.6 ms: 1.47x faster                                                     |
| django_template | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                     |
| genshi_xml      | 63.3 ms                                                | 46.7 ms: 1.36x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.71 ms: 2.00x faster                                                     |
| logging_silent          | 175 ns                                                 | 93.9 ns: 1.86x faster                                                     |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                      |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                                      |
| python_startup          | 14.2 ms                                                | 8.48 ms: 1.67x faster                                                     |
| scimark_monte_carlo     | 108 ms                                                 | 65.1 ms: 1.66x faster                                                     |
| pyflate                 | 673 ms                                                 | 409 ms: 1.65x faster                                                      |
| richards                | 74.9 ms                                                | 46.0 ms: 1.63x faster                                                     |
| raytrace                | 464 ms                                                 | 291 ms: 1.59x faster                                                      |
| pickle_pure_python      | 455 us                                                 | 288 us: 1.58x faster                                                      |
| chaos                   | 106 ms                                                 | 67.5 ms: 1.57x faster                                                     |
| crypto_pyaes            | 118 ms                                                 | 75.5 ms: 1.57x faster                                                     |
| hexiom                  | 9.53 ms                                                | 6.18 ms: 1.54x faster                                                     |
| spectral_norm           | 150 ms                                                 | 98.0 ms: 1.53x faster                                                     |
| float                   | 111 ms                                                 | 72.8 ms: 1.52x faster                                                     |
| unpack_sequence         | 64.7 ns                                                | 42.9 ns: 1.51x faster                                                     |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                      |
| deepcopy_memo           | 52.3 us                                                | 34.7 us: 1.51x faster                                                     |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                                      |
| mako                    | 14.8 ms                                                | 9.89 ms: 1.49x faster                                                     |
| nbody                   | 142 ms                                                 | 94.9 ms: 1.49x faster                                                     |
| genshi_text             | 30.3 ms                                                | 20.6 ms: 1.47x faster                                                     |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                                     |
| chameleon               | 9.06 ms                                                | 6.26 ms: 1.45x faster                                                     |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                     |
| json_dumps              | 13.5 ms                                                | 9.48 ms: 1.43x faster                                                     |
| html5lib                | 85.9 ms                                                | 60.3 ms: 1.42x faster                                                     |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                                    |
| pprint_safe_repr        | 955 ms                                                 | 676 ms: 1.41x faster                                                      |
| django_template         | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                     |
| xml_etree_process       | 74.9 ms                                                | 53.9 ms: 1.39x faster                                                     |
| regex_compile           | 177 ms                                                 | 130 ms: 1.37x faster                                                      |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.02 ms: 1.36x faster                                                     |
| genshi_xml              | 63.3 ms                                                | 46.7 ms: 1.36x faster                                                     |
| thrift                  | 1.03 ms                                                | 765 us: 1.35x faster                                                      |
| async_tree_none         | 717 ms                                                 | 531 ms: 1.35x faster                                                      |
| logging_simple          | 8.07 us                                                | 6.01 us: 1.34x faster                                                     |
| logging_format          | 8.91 us                                                | 6.64 us: 1.34x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.33x faster                                                    |
| scimark_fft             | 424 ms                                                 | 319 ms: 1.33x faster                                                      |
| 2to3                    | 336 ms                                                 | 254 ms: 1.33x faster                                                      |
| deepcopy                | 442 us                                                 | 335 us: 1.32x faster                                                      |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.30x faster                                                    |
| fannkuch                | 486 ms                                                 | 375 ms: 1.29x faster                                                      |
| coroutines              | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                     |
| nqueens                 | 100 ms                                                 | 78.4 ms: 1.28x faster                                                     |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                                      |
| async_tree_memoization  | 854 ms                                                 | 670 ms: 1.28x faster                                                      |
| sqlglot_optimize        | 65.3 ms                                                | 51.6 ms: 1.27x faster                                                     |
| deepcopy_reduce         | 3.82 us                                                | 3.03 us: 1.26x faster                                                     |
| docutils                | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                    |
| async_tree_cpu_io_mixed | 951 ms                                                 | 758 ms: 1.25x faster                                                      |
| dulwich_log             | 75.9 ms                                                | 62.0 ms: 1.23x faster                                                     |
| xml_etree_generate      | 94.2 ms                                                | 77.1 ms: 1.22x faster                                                     |
| bench_thread_pool       | 947 us                                                 | 786 us: 1.21x faster                                                      |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.20x faster                                                     |
| async_generators        | 425 ms                                                 | 356 ms: 1.20x faster                                                      |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                                      |
| json_loads              | 28.8 us                                                | 24.3 us: 1.19x faster                                                     |
| json                    | 5.42 ms                                                | 4.63 ms: 1.17x faster                                                     |
| sympy_str               | 328 ms                                                 | 281 ms: 1.17x faster                                                      |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                                     |
| sympy_sum               | 185 ms                                                 | 163 ms: 1.13x faster                                                      |
| regex_v8                | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                     |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                                     |
| pickle_list             | 4.56 us                                                | 4.15 us: 1.10x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                      |
| pathlib                 | 20.0 ms                                                | 18.3 ms: 1.09x faster                                                     |
| meteor_contest          | 115 ms                                                 | 106 ms: 1.09x faster                                                      |
| mdp                     | 2.82 sec                                               | 2.65 sec: 1.07x faster                                                    |
| regex_dna               | 222 ms                                                 | 209 ms: 1.06x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.06x faster                                                      |
| telco                   | 6.54 ms                                                | 6.28 ms: 1.04x faster                                                     |
| pickle                  | 10.3 us                                                | 9.89 us: 1.04x faster                                                     |
| unpickle                | 14.1 us                                                | 13.7 us: 1.03x faster                                                     |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                      |
| generators              | 76.8 ms                                                | 77.4 ms: 1.01x slower                                                     |
| unpickle_list           | 4.82 us                                                | 4.95 us: 1.03x slower                                                     |
| python_startup_no_site  | 5.82 ms                                                | 6.07 ms: 1.04x slower                                                     |
| regex_effbot            | 3.23 ms                                                | 3.55 ms: 1.10x slower                                                     |
| pickle_dict             | 27.3 us                                                | 30.2 us: 1.11x slower                                                     |
| coverage                | 72.8 ms                                                | 96.9 ms: 1.33x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230109-3.12.0a3+-78c9301/bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x
