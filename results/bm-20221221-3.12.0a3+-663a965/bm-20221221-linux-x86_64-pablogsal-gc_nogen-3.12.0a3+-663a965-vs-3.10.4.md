
# Results vs. 3.10.4

- fork: pablogsal
- ref: gc_nogen
- machine: linux-x86_64
- commit hash: 663a965
- commit date: 2022-12-21
- overall geometric mean: 1.38x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 243 ms: 1.38x faster                                          |
| chameleon      | 9.06 ms                                                | 6.29 ms: 1.44x faster                                         |
| docutils       | 3.17 sec                                               | 2.13 sec: 1.49x faster                                        |
| html5lib       | 85.9 ms                                                | 57.4 ms: 1.50x faster                                         |
| Geometric mean | (ref)                                                  | 1.45x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 111 ms                                                 | 61.8 ms: 1.79x faster                                         |
| nbody          | 142 ms                                                 | 93.2 ms: 1.52x faster                                         |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.38x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.35x faster                                          |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                         |
| regex_dna      | 222 ms                                                 | 201 ms: 1.10x faster                                          |
| regex_effbot   | 3.23 ms                                                | 3.35 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                  | 1.14x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.61x faster                                          |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.53x faster                                          |
| xml_etree_process    | 74.9 ms                                                | 51.5 ms: 1.46x faster                                         |
| json_dumps           | 13.5 ms                                                | 9.30 ms: 1.46x faster                                         |
| xml_etree_iterparse  | 111 ms                                                 | 80.8 ms: 1.38x faster                                         |
| xml_etree_parse      | 163 ms                                                 | 123 ms: 1.33x faster                                          |
| xml_etree_generate   | 94.2 ms                                                | 73.0 ms: 1.29x faster                                         |
| json_loads           | 28.8 us                                                | 23.7 us: 1.22x faster                                         |
| pickle_list          | 4.56 us                                                | 4.16 us: 1.10x faster                                         |
| unpickle             | 14.1 us                                                | 13.3 us: 1.07x faster                                         |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                         |
| unpickle_list        | 4.82 us                                                | 5.03 us: 1.04x slower                                         |
| pickle_dict          | 27.3 us                                                | 31.4 us: 1.15x slower                                         |
| Geometric mean       | (ref)                                                  | 1.23x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.06 ms: 1.76x faster                                         |
| python_startup_no_site | 5.82 ms                                                | 5.88 ms: 1.01x slower                                         |
| Geometric mean         | (ref)                                                  | 1.32x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.50 ms: 1.55x faster                                         |
| genshi_text     | 30.3 ms                                                | 20.4 ms: 1.48x faster                                         |
| django_template | 45.9 ms                                                | 32.8 ms: 1.40x faster                                         |
| genshi_xml      | 63.3 ms                                                | 46.2 ms: 1.37x faster                                         |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 537 ms: 3.30x faster                                          |
| async_tree_none         | 717 ms                                                 | 269 ms: 2.67x faster                                          |
| async_tree_memoization  | 854 ms                                                 | 324 ms: 2.63x faster                                          |
| deltablue               | 7.42 ms                                                | 3.11 ms: 2.39x faster                                         |
| async_tree_cpu_io_mixed | 951 ms                                                 | 474 ms: 2.01x faster                                          |
| logging_silent          | 175 ns                                                 | 91.2 ns: 1.92x faster                                         |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.90x faster                                          |
| richards                | 74.9 ms                                                | 41.1 ms: 1.82x faster                                         |
| float                   | 111 ms                                                 | 61.8 ms: 1.79x faster                                         |
| python_startup          | 14.2 ms                                                | 8.06 ms: 1.76x faster                                         |
| pyflate                 | 673 ms                                                 | 399 ms: 1.69x faster                                          |
| go                      | 229 ms                                                 | 137 ms: 1.68x faster                                          |
| scimark_monte_carlo     | 108 ms                                                 | 65.7 ms: 1.65x faster                                         |
| raytrace                | 464 ms                                                 | 282 ms: 1.65x faster                                          |
| pickle_pure_python      | 455 us                                                 | 282 us: 1.61x faster                                          |
| spectral_norm           | 150 ms                                                 | 93.6 ms: 1.60x faster                                         |
| crypto_pyaes            | 118 ms                                                 | 75.3 ms: 1.57x faster                                         |
| chaos                   | 106 ms                                                 | 67.6 ms: 1.57x faster                                         |
| mako                    | 14.8 ms                                                | 9.50 ms: 1.55x faster                                         |
| deepcopy_memo           | 52.3 us                                                | 33.9 us: 1.54x faster                                         |
| hexiom                  | 9.53 ms                                                | 6.18 ms: 1.54x faster                                         |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.54x faster                                          |
| pycparser               | 1.50 sec                                               | 983 ms: 1.53x faster                                          |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.53x faster                                          |
| nbody                   | 142 ms                                                 | 93.2 ms: 1.52x faster                                         |
| unpack_sequence         | 64.7 ns                                                | 42.8 ns: 1.51x faster                                         |
| sqlglot_parse           | 2.06 ms                                                | 1.36 ms: 1.51x faster                                         |
| html5lib                | 85.9 ms                                                | 57.4 ms: 1.50x faster                                         |
| docutils                | 3.17 sec                                               | 2.13 sec: 1.49x faster                                        |
| sqlglot_transpile       | 2.45 ms                                                | 1.65 ms: 1.49x faster                                         |
| genshi_text             | 30.3 ms                                                | 20.4 ms: 1.48x faster                                         |
| xml_etree_process       | 74.9 ms                                                | 51.5 ms: 1.46x faster                                         |
| json_dumps              | 13.5 ms                                                | 9.30 ms: 1.46x faster                                         |
| chameleon               | 9.06 ms                                                | 6.29 ms: 1.44x faster                                         |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                        |
| logging_simple          | 8.07 us                                                | 5.73 us: 1.41x faster                                         |
| logging_format          | 8.91 us                                                | 6.33 us: 1.41x faster                                         |
| scimark_fft             | 424 ms                                                 | 302 ms: 1.40x faster                                          |
| django_template         | 45.9 ms                                                | 32.8 ms: 1.40x faster                                         |
| pprint_safe_repr        | 955 ms                                                 | 686 ms: 1.39x faster                                          |
| thrift                  | 1.03 ms                                                | 747 us: 1.38x faster                                          |
| 2to3                    | 336 ms                                                 | 243 ms: 1.38x faster                                          |
| xml_etree_iterparse     | 111 ms                                                 | 80.8 ms: 1.38x faster                                         |
| genshi_xml              | 63.3 ms                                                | 46.2 ms: 1.37x faster                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.01 ms: 1.36x faster                                         |
| regex_compile           | 177 ms                                                 | 131 ms: 1.35x faster                                          |
| deepcopy                | 442 us                                                 | 331 us: 1.33x faster                                          |
| xml_etree_parse         | 163 ms                                                 | 123 ms: 1.33x faster                                          |
| fannkuch                | 486 ms                                                 | 372 ms: 1.31x faster                                          |
| deepcopy_reduce         | 3.82 us                                                | 2.95 us: 1.30x faster                                         |
| xml_etree_generate      | 94.2 ms                                                | 73.0 ms: 1.29x faster                                         |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                         |
| nqueens                 | 100 ms                                                 | 78.2 ms: 1.28x faster                                         |
| async_generators        | 425 ms                                                 | 334 ms: 1.27x faster                                          |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                          |
| json_loads              | 28.8 us                                                | 23.7 us: 1.22x faster                                         |
| coroutines              | 31.8 ms                                                | 26.1 ms: 1.22x faster                                         |
| bench_thread_pool       | 947 us                                                 | 783 us: 1.21x faster                                          |
| sympy_expand            | 545 ms                                                 | 451 ms: 1.21x faster                                          |
| dulwich_log             | 75.9 ms                                                | 63.1 ms: 1.20x faster                                         |
| sympy_integrate         | 24.3 ms                                                | 20.2 ms: 1.20x faster                                         |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                         |
| json                    | 5.42 ms                                                | 4.60 ms: 1.18x faster                                         |
| sympy_str               | 328 ms                                                 | 279 ms: 1.18x faster                                          |
| pathlib                 | 20.0 ms                                                | 17.4 ms: 1.15x faster                                         |
| sympy_sum               | 185 ms                                                 | 162 ms: 1.14x faster                                          |
| sqlite_synth            | 2.93 us                                                | 2.61 us: 1.12x faster                                         |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                          |
| regex_dna               | 222 ms                                                 | 201 ms: 1.10x faster                                          |
| pickle_list             | 4.56 us                                                | 4.16 us: 1.10x faster                                         |
| unpickle                | 14.1 us                                                | 13.3 us: 1.07x faster                                         |
| mdp                     | 2.82 sec                                               | 2.72 sec: 1.04x faster                                        |
| telco                   | 6.54 ms                                                | 6.41 ms: 1.02x faster                                         |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                         |
| python_startup_no_site  | 5.82 ms                                                | 5.88 ms: 1.01x slower                                         |
| generators              | 76.8 ms                                                | 78.4 ms: 1.02x slower                                         |
| regex_effbot            | 3.23 ms                                                | 3.35 ms: 1.04x slower                                         |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                          |
| unpickle_list           | 4.82 us                                                | 5.03 us: 1.04x slower                                         |
| pickle_dict             | 27.3 us                                                | 31.4 us: 1.15x slower                                         |
| coverage                | 72.8 ms                                                | 103 ms: 1.41x slower                                          |
| Geometric mean          | (ref)                                                  | 1.38x faster                                                  |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221221-3.12.0a3+-663a965/bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x
