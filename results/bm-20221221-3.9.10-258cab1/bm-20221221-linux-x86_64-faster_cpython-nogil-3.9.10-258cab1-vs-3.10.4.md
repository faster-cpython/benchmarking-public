
# Results vs. 3.10.4

- fork: faster_cpython
- ref: nogil
- machine: linux-x86_64
- commit hash: 258cab1
- commit date: 2022-12-21
- overall geometric mean: 1.01x faster \*
- HPT reliability: 68.07%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 382 ms: 1.14x slower                                         |
| chameleon      | 9.06 ms                                                | 8.20 ms: 1.10x faster                                        |
| docutils       | 3.17 sec                                               | 5.20 sec: 1.64x slower                                       |
| html5lib       | 85.9 ms                                                | 81.7 ms: 1.05x faster                                        |
| tornado_http   | 127 ms                                                 | 124 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.09x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 111 ms                                                 | 104 ms: 1.06x faster                                         |
| pidigits       | 190 ms                                                 | 186 ms: 1.02x faster                                         |
| nbody          | 142 ms                                                 | 172 ms: 1.21x slower                                         |
| Geometric mean | (ref)                                                  | 1.04x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 25.0 ms                                                | 24.1 ms: 1.04x faster                                        |
| regex_dna      | 222 ms                                                 | 218 ms: 1.02x faster                                         |
| regex_effbot   | 3.23 ms                                                | 3.35 ms: 1.04x slower                                        |
| regex_compile  | 177 ms                                                 | 186 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 346 us: 1.32x faster                                         |
| xml_etree_iterparse  | 111 ms                                                 | 95.5 ms: 1.17x faster                                        |
| unpickle_pure_python | 300 us                                                 | 262 us: 1.14x faster                                         |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                         |
| pickle_list          | 4.56 us                                                | 4.17 us: 1.09x faster                                        |
| pickle_dict          | 27.3 us                                                | 25.3 us: 1.08x faster                                        |
| xml_etree_generate   | 94.2 ms                                                | 87.8 ms: 1.07x faster                                        |
| xml_etree_process    | 74.9 ms                                                | 71.4 ms: 1.05x faster                                        |
| pickle               | 10.3 us                                                | 10.0 us: 1.03x faster                                        |
| json_dumps           | 13.5 ms                                                | 13.4 ms: 1.01x faster                                        |
| json_loads           | 28.8 us                                                | 32.5 us: 1.13x slower                                        |
| unpickle_list        | 4.82 us                                                | 5.80 us: 1.20x slower                                        |
| unpickle             | 14.1 us                                                | 18.6 us: 1.31x slower                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.41 ms: 1.50x faster                                        |
| python_startup_no_site | 5.82 ms                                                | 5.91 ms: 1.02x slower                                        |
| Geometric mean         | (ref)                                                  | 1.22x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 45.9 ms                                                | 42.6 ms: 1.08x faster                                        |
| mako            | 14.8 ms                                                | 16.4 ms: 1.11x slower                                        |
| genshi_xml      | 63.3 ms                                                | 73.6 ms: 1.16x slower                                        |
| genshi_text     | 30.3 ms                                                | 52.1 ms: 1.72x slower                                        |
| Geometric mean  | (ref)                                                  | 1.20x slower                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 829 ms: 2.14x faster                                         |
| async_tree_none         | 717 ms                                                 | 372 ms: 1.93x faster                                         |
| richards                | 74.9 ms                                                | 39.3 ms: 1.90x faster                                        |
| async_tree_memoization  | 854 ms                                                 | 460 ms: 1.86x faster                                         |
| logging_silent          | 175 ns                                                 | 96.0 ns: 1.82x faster                                        |
| async_tree_cpu_io_mixed | 951 ms                                                 | 614 ms: 1.55x faster                                         |
| python_startup          | 14.2 ms                                                | 9.41 ms: 1.50x faster                                        |
| go                      | 229 ms                                                 | 159 ms: 1.44x faster                                         |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                       |
| deltablue               | 7.42 ms                                                | 5.41 ms: 1.37x faster                                        |
| scimark_sor             | 197 ms                                                 | 144 ms: 1.36x faster                                         |
| pickle_pure_python      | 455 us                                                 | 346 us: 1.32x faster                                         |
| deepcopy_memo           | 52.3 us                                                | 40.1 us: 1.31x faster                                        |
| unpack_sequence         | 64.7 ns                                                | 52.4 ns: 1.23x faster                                        |
| hexiom                  | 9.53 ms                                                | 7.74 ms: 1.23x faster                                        |
| xml_etree_iterparse     | 111 ms                                                 | 95.5 ms: 1.17x faster                                        |
| logging_simple          | 8.07 us                                                | 6.95 us: 1.16x faster                                        |
| logging_format          | 8.91 us                                                | 7.69 us: 1.16x faster                                        |
| unpickle_pure_python    | 300 us                                                 | 262 us: 1.14x faster                                         |
| deepcopy                | 442 us                                                 | 393 us: 1.12x faster                                         |
| raytrace                | 464 ms                                                 | 416 ms: 1.11x faster                                         |
| pycparser               | 1.50 sec                                               | 1.35 sec: 1.11x faster                                       |
| chameleon               | 9.06 ms                                                | 8.20 ms: 1.10x faster                                        |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                         |
| pickle_list             | 4.56 us                                                | 4.17 us: 1.09x faster                                        |
| scimark_lu              | 163 ms                                                 | 149 ms: 1.09x faster                                         |
| django_template         | 45.9 ms                                                | 42.6 ms: 1.08x faster                                        |
| pickle_dict             | 27.3 us                                                | 25.3 us: 1.08x faster                                        |
| scimark_monte_carlo     | 108 ms                                                 | 101 ms: 1.08x faster                                         |
| xml_etree_generate      | 94.2 ms                                                | 87.8 ms: 1.07x faster                                        |
| float                   | 111 ms                                                 | 104 ms: 1.06x faster                                         |
| pyflate                 | 673 ms                                                 | 636 ms: 1.06x faster                                         |
| deepcopy_reduce         | 3.82 us                                                | 3.63 us: 1.05x faster                                        |
| spectral_norm           | 150 ms                                                 | 143 ms: 1.05x faster                                         |
| html5lib                | 85.9 ms                                                | 81.7 ms: 1.05x faster                                        |
| xml_etree_process       | 74.9 ms                                                | 71.4 ms: 1.05x faster                                        |
| chaos                   | 106 ms                                                 | 102 ms: 1.04x faster                                         |
| thrift                  | 1.03 ms                                                | 992 us: 1.04x faster                                         |
| regex_v8                | 25.0 ms                                                | 24.1 ms: 1.04x faster                                        |
| pickle                  | 10.3 us                                                | 10.0 us: 1.03x faster                                        |
| tornado_http            | 127 ms                                                 | 124 ms: 1.03x faster                                         |
| sympy_expand            | 545 ms                                                 | 531 ms: 1.03x faster                                         |
| pidigits                | 190 ms                                                 | 186 ms: 1.02x faster                                         |
| regex_dna               | 222 ms                                                 | 218 ms: 1.02x faster                                         |
| json_dumps              | 13.5 ms                                                | 13.4 ms: 1.01x faster                                        |
| bench_mp_pool           | 24.0 ms                                                | 23.8 ms: 1.01x faster                                        |
| fannkuch                | 486 ms                                                 | 490 ms: 1.01x slower                                         |
| dulwich_log             | 75.9 ms                                                | 77.0 ms: 1.01x slower                                        |
| scimark_fft             | 424 ms                                                 | 430 ms: 1.02x slower                                         |
| python_startup_no_site  | 5.82 ms                                                | 5.91 ms: 1.02x slower                                        |
| sympy_str               | 328 ms                                                 | 335 ms: 1.02x slower                                         |
| crypto_pyaes            | 118 ms                                                 | 122 ms: 1.03x slower                                         |
| pathlib                 | 20.0 ms                                                | 20.6 ms: 1.03x slower                                        |
| regex_effbot            | 3.23 ms                                                | 3.35 ms: 1.04x slower                                        |
| aiohttp                 | 1.38 ms                                                | 1.44 ms: 1.04x slower                                        |
| gunicorn                | 1.46 ms                                                | 1.52 ms: 1.04x slower                                        |
| sqlglot_transpile       | 2.45 ms                                                | 2.55 ms: 1.04x slower                                        |
| sympy_integrate         | 24.3 ms                                                | 25.4 ms: 1.05x slower                                        |
| regex_compile           | 177 ms                                                 | 186 ms: 1.05x slower                                         |
| sqlglot_parse           | 2.06 ms                                                | 2.18 ms: 1.06x slower                                        |
| sqlglot_optimize        | 65.3 ms                                                | 69.3 ms: 1.06x slower                                        |
| generators              | 76.8 ms                                                | 81.6 ms: 1.06x slower                                        |
| sqlglot_normalize       | 135 ms                                                 | 144 ms: 1.07x slower                                         |
| nqueens                 | 100 ms                                                 | 109 ms: 1.09x slower                                         |
| telco                   | 6.54 ms                                                | 7.15 ms: 1.09x slower                                        |
| mdp                     | 2.82 sec                                               | 3.10 sec: 1.10x slower                                       |
| sqlite_synth            | 2.93 us                                                | 3.24 us: 1.10x slower                                        |
| meteor_contest          | 115 ms                                                 | 127 ms: 1.11x slower                                         |
| mako                    | 14.8 ms                                                | 16.4 ms: 1.11x slower                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 6.09 ms: 1.12x slower                                        |
| djangocms               | 35.9 us                                                | 40.5 us: 1.13x slower                                        |
| json_loads              | 28.8 us                                                | 32.5 us: 1.13x slower                                        |
| 2to3                    | 336 ms                                                 | 382 ms: 1.14x slower                                         |
| sympy_sum               | 185 ms                                                 | 212 ms: 1.15x slower                                         |
| genshi_xml              | 63.3 ms                                                | 73.6 ms: 1.16x slower                                        |
| pylint                  | 525 ms                                                 | 626 ms: 1.19x slower                                         |
| unpickle_list           | 4.82 us                                                | 5.80 us: 1.20x slower                                        |
| nbody                   | 142 ms                                                 | 172 ms: 1.21x slower                                         |
| bench_thread_pool       | 947 us                                                 | 1.19 ms: 1.25x slower                                        |
| unpickle                | 14.1 us                                                | 18.6 us: 1.31x slower                                        |
| flaskblogging           | 8.27 ms                                                | 12.1 ms: 1.47x slower                                        |
| async_generators        | 425 ms                                                 | 626 ms: 1.47x slower                                         |
| docutils                | 3.17 sec                                               | 5.20 sec: 1.64x slower                                       |
| genshi_text             | 30.3 ms                                                | 52.1 ms: 1.72x slower                                        |
| coroutines              | 31.8 ms                                                | 72.5 ms: 2.28x slower                                        |
| coverage                | 72.8 ms                                                | 553 ms: 7.59x slower                                         |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (1): json
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, gc_traversal, mypy2, pprint_safe_repr, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221221-3.9.10-258cab1/bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1.json: mypy


# HPT report

- Reliability score: 68.07% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
