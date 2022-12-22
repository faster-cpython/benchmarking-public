Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 243 ms: 1.37x faster                                          |
| chameleon      | 8.86 ms                                                | 6.29 ms: 1.41x faster                                         |
| docutils       | 3.18 sec                                               | 2.13 sec: 1.49x faster                                        |
| html5lib       | 85.8 ms                                                | 57.4 ms: 1.49x faster                                         |
| Geometric mean | (ref)                                                  | 1.44x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 108 ms                                                 | 61.8 ms: 1.74x faster                                         |
| nbody          | 136 ms                                                 | 93.2 ms: 1.46x faster                                         |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.35x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 131 ms: 1.33x faster                                          |
| regex_dna      | 214 ms                                                 | 201 ms: 1.06x faster                                          |
| regex_effbot   | 3.21 ms                                                | 3.35 ms: 1.05x slower                                         |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.17x faster                                         |
| Geometric mean | (ref)                                                  | 1.12x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.30 ms: 1.45x faster                                         |
| json_loads           | 28.9 us                                                | 23.7 us: 1.22x faster                                         |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                         |
| pickle_dict          | 28.3 us                                                | 31.4 us: 1.11x slower                                         |
| pickle_list          | 4.50 us                                                | 4.16 us: 1.08x faster                                         |
| pickle_pure_python   | 453 us                                                 | 282 us: 1.61x faster                                          |
| unpickle             | 14.3 us                                                | 13.3 us: 1.08x faster                                         |
| unpickle_list        | 4.99 us                                                | 5.03 us: 1.01x slower                                         |
| unpickle_pure_python | 297 us                                                 | 197 us: 1.51x faster                                          |
| xml_etree_parse      | 163 ms                                                 | 123 ms: 1.33x faster                                          |
| xml_etree_iterparse  | 110 ms                                                 | 80.8 ms: 1.37x faster                                         |
| xml_etree_generate   | 93.3 ms                                                | 73.0 ms: 1.28x faster                                         |
| xml_etree_process    | 74.5 ms                                                | 51.5 ms: 1.45x faster                                         |
| Geometric mean       | (ref)                                                  | 1.23x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.06 ms: 1.73x faster                                         |
| python_startup_no_site | 5.76 ms                                                | 5.88 ms: 1.02x slower                                         |
| Geometric mean         | (ref)                                                  | 1.30x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 32.8 ms: 1.41x faster                                         |
| genshi_text     | 30.6 ms                                                | 20.4 ms: 1.50x faster                                         |
| genshi_xml      | 63.6 ms                                                | 46.2 ms: 1.37x faster                                         |
| mako            | 14.3 ms                                                | 9.50 ms: 1.50x faster                                         |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 243 ms: 1.37x faster                                          |
| async_generators        | 428 ms                                                 | 334 ms: 1.28x faster                                          |
| async_tree_none         | 713 ms                                                 | 269 ms: 2.65x faster                                          |
| async_tree_cpu_io_mixed | 949 ms                                                 | 474 ms: 2.00x faster                                          |
| async_tree_io           | 1.78 sec                                               | 537 ms: 3.30x faster                                          |
| async_tree_memoization  | 854 ms                                                 | 324 ms: 2.63x faster                                          |
| chameleon               | 8.86 ms                                                | 6.29 ms: 1.41x faster                                         |
| chaos                   | 104 ms                                                 | 67.6 ms: 1.54x faster                                         |
| bench_thread_pool       | 943 us                                                 | 783 us: 1.20x faster                                          |
| coroutines              | 31.7 ms                                                | 26.1 ms: 1.21x faster                                         |
| coverage                | 75.3 ms                                                | 103 ms: 1.37x slower                                          |
| crypto_pyaes            | 118 ms                                                 | 75.3 ms: 1.56x faster                                         |
| deepcopy                | 429 us                                                 | 331 us: 1.30x faster                                          |
| deepcopy_reduce         | 3.75 us                                                | 2.95 us: 1.27x faster                                         |
| deepcopy_memo           | 50.0 us                                                | 33.9 us: 1.47x faster                                         |
| deltablue               | 7.39 ms                                                | 3.11 ms: 2.38x faster                                         |
| django_template         | 46.3 ms                                                | 32.8 ms: 1.41x faster                                         |
| docutils                | 3.18 sec                                               | 2.13 sec: 1.49x faster                                        |
| dulwich_log             | 75.5 ms                                                | 63.1 ms: 1.20x faster                                         |
| fannkuch                | 477 ms                                                 | 372 ms: 1.28x faster                                          |
| float                   | 108 ms                                                 | 61.8 ms: 1.74x faster                                         |
| generators              | 75.8 ms                                                | 78.4 ms: 1.04x slower                                         |
| genshi_text             | 30.6 ms                                                | 20.4 ms: 1.50x faster                                         |
| genshi_xml              | 63.6 ms                                                | 46.2 ms: 1.37x faster                                         |
| go                      | 226 ms                                                 | 137 ms: 1.65x faster                                          |
| hexiom                  | 9.42 ms                                                | 6.18 ms: 1.52x faster                                         |
| html5lib                | 85.8 ms                                                | 57.4 ms: 1.49x faster                                         |
| json                    | 5.35 ms                                                | 4.60 ms: 1.16x faster                                         |
| json_dumps              | 13.5 ms                                                | 9.30 ms: 1.45x faster                                         |
| json_loads              | 28.9 us                                                | 23.7 us: 1.22x faster                                         |
| logging_format          | 8.92 us                                                | 6.33 us: 1.41x faster                                         |
| logging_silent          | 173 ns                                                 | 91.2 ns: 1.90x faster                                         |
| logging_simple          | 8.06 us                                                | 5.73 us: 1.41x faster                                         |
| mako                    | 14.3 ms                                                | 9.50 ms: 1.50x faster                                         |
| mdp                     | 2.82 sec                                               | 2.72 sec: 1.04x faster                                        |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                          |
| mypy                    | 1.01 sec                                               | 610 ms: 1.66x faster                                          |
| nbody                   | 136 ms                                                 | 93.2 ms: 1.46x faster                                         |
| nqueens                 | 99.3 ms                                                | 78.2 ms: 1.27x faster                                         |
| pathlib                 | 20.0 ms                                                | 17.4 ms: 1.15x faster                                         |
| pickle                  | 10.1 us                                                | 10.4 us: 1.03x slower                                         |
| pickle_dict             | 28.3 us                                                | 31.4 us: 1.11x slower                                         |
| pickle_list             | 4.50 us                                                | 4.16 us: 1.08x faster                                         |
| pickle_pure_python      | 453 us                                                 | 282 us: 1.61x faster                                          |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                          |
| pprint_safe_repr        | 943 ms                                                 | 686 ms: 1.37x faster                                          |
| pprint_pformat          | 1.97 sec                                               | 1.40 sec: 1.41x faster                                        |
| pycparser               | 1.51 sec                                               | 983 ms: 1.54x faster                                          |
| pyflate                 | 675 ms                                                 | 399 ms: 1.69x faster                                          |
| python_startup          | 13.9 ms                                                | 8.06 ms: 1.73x faster                                         |
| python_startup_no_site  | 5.76 ms                                                | 5.88 ms: 1.02x slower                                         |
| raytrace                | 461 ms                                                 | 282 ms: 1.64x faster                                          |
| regex_compile           | 174 ms                                                 | 131 ms: 1.33x faster                                          |
| regex_dna               | 214 ms                                                 | 201 ms: 1.06x faster                                          |
| regex_effbot            | 3.21 ms                                                | 3.35 ms: 1.05x slower                                         |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.17x faster                                         |
| richards                | 71.4 ms                                                | 41.1 ms: 1.74x faster                                         |
| scimark_fft             | 414 ms                                                 | 302 ms: 1.37x faster                                          |
| scimark_lu              | 158 ms                                                 | 106 ms: 1.49x faster                                          |
| scimark_monte_carlo     | 105 ms                                                 | 65.7 ms: 1.59x faster                                         |
| scimark_sor             | 193 ms                                                 | 104 ms: 1.86x faster                                          |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.01 ms: 1.37x faster                                         |
| spectral_norm           | 148 ms                                                 | 93.6 ms: 1.58x faster                                         |
| sqlglot_parse           | 2.04 ms                                                | 1.36 ms: 1.50x faster                                         |
| sqlglot_transpile       | 2.42 ms                                                | 1.65 ms: 1.47x faster                                         |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                         |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                          |
| sqlite_synth            | 2.90 us                                                | 2.61 us: 1.11x faster                                         |
| sympy_expand            | 537 ms                                                 | 451 ms: 1.19x faster                                          |
| sympy_integrate         | 23.9 ms                                                | 20.2 ms: 1.19x faster                                         |
| sympy_sum               | 183 ms                                                 | 162 ms: 1.13x faster                                          |
| sympy_str               | 324 ms                                                 | 279 ms: 1.16x faster                                          |
| telco                   | 6.68 ms                                                | 6.41 ms: 1.04x faster                                         |
| thrift                  | 1.03 ms                                                | 747 us: 1.38x faster                                          |
| unpack_sequence         | 59.5 ns                                                | 42.8 ns: 1.39x faster                                         |
| unpickle                | 14.3 us                                                | 13.3 us: 1.08x faster                                         |
| unpickle_list           | 4.99 us                                                | 5.03 us: 1.01x slower                                         |
| unpickle_pure_python    | 297 us                                                 | 197 us: 1.51x faster                                          |
| xml_etree_parse         | 163 ms                                                 | 123 ms: 1.33x faster                                          |
| xml_etree_iterparse     | 110 ms                                                 | 80.8 ms: 1.37x faster                                         |
| xml_etree_generate      | 93.3 ms                                                | 73.0 ms: 1.28x faster                                         |
| xml_etree_process       | 74.5 ms                                                | 51.5 ms: 1.45x faster                                         |
| Geometric mean          | (ref)                                                  | 1.37x faster                                                  |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
