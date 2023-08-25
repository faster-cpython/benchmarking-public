
# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialized_send
- machine: linux-x86_64
- commit hash: 685d559
- commit date: 2023-02-10
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 246 ms: 1.37x faster                                                         |
| chameleon      | 9.06 ms                                                | 6.51 ms: 1.39x faster                                                        |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                       |
| html5lib       | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                        |
| tornado_http   | 127 ms                                                 | 95.1 ms: 1.34x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.0 ms: 1.52x faster                                                        |
| float          | 111 ms                                                 | 73.9 ms: 1.50x faster                                                        |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.35x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.13x faster                                                        |
| regex_dna      | 222 ms                                                 | 211 ms: 1.05x faster                                                         |
| regex_effbot   | 3.23 ms                                                | 3.38 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                                         |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.46 ms: 1.43x faster                                                        |
| xml_etree_process    | 74.9 ms                                                | 55.9 ms: 1.34x faster                                                        |
| json_loads           | 28.8 us                                                | 23.9 us: 1.21x faster                                                        |
| xml_etree_generate   | 94.2 ms                                                | 80.6 ms: 1.17x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| pickle_list          | 4.56 us                                                | 4.12 us: 1.11x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.10x faster                                                         |
| unpickle             | 14.1 us                                                | 13.7 us: 1.03x faster                                                        |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                                        |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                                        |
| pickle_dict          | 27.3 us                                                | 30.9 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.96 ms: 1.58x faster                                                        |
| python_startup_no_site | 5.82 ms                                                | 6.49 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.75 ms: 1.51x faster                                                        |
| genshi_text     | 30.3 ms                                                | 20.8 ms: 1.46x faster                                                        |
| django_template | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                        |
| genshi_xml      | 63.3 ms                                                | 48.1 ms: 1.32x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-faster%2dcpython-specialized_send-3.12.0a5+-685d559 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 31.1 ms: 2.47x faster                                                        |
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.33x faster                                                        |
| asyncio_tcp             | 925 ms                                                 | 495 ms: 1.87x faster                                                         |
| logging_silent          | 175 ns                                                 | 94.0 ns: 1.86x faster                                                        |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.81x faster                                                         |
| richards                | 74.9 ms                                                | 42.9 ms: 1.74x faster                                                        |
| go                      | 229 ms                                                 | 134 ms: 1.72x faster                                                         |
| pyflate                 | 673 ms                                                 | 403 ms: 1.67x faster                                                         |
| scimark_monte_carlo     | 108 ms                                                 | 66.1 ms: 1.64x faster                                                        |
| raytrace                | 464 ms                                                 | 285 ms: 1.62x faster                                                         |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                                         |
| crypto_pyaes            | 118 ms                                                 | 73.7 ms: 1.61x faster                                                        |
| chaos                   | 106 ms                                                 | 66.1 ms: 1.61x faster                                                        |
| python_startup          | 14.2 ms                                                | 8.96 ms: 1.58x faster                                                        |
| spectral_norm           | 150 ms                                                 | 95.8 ms: 1.57x faster                                                        |
| hexiom                  | 9.53 ms                                                | 6.14 ms: 1.55x faster                                                        |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                                         |
| nbody                   | 142 ms                                                 | 93.0 ms: 1.52x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 34.5 us: 1.52x faster                                                        |
| mako                    | 14.8 ms                                                | 9.75 ms: 1.51x faster                                                        |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                                         |
| float                   | 111 ms                                                 | 73.9 ms: 1.50x faster                                                        |
| unpack_sequence         | 64.7 ns                                                | 43.4 ns: 1.49x faster                                                        |
| genshi_text             | 30.3 ms                                                | 20.8 ms: 1.46x faster                                                        |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.46 ms: 1.43x faster                                                        |
| coroutines              | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                        |
| logging_simple          | 8.07 us                                                | 5.67 us: 1.42x faster                                                        |
| logging_format          | 8.91 us                                                | 6.26 us: 1.42x faster                                                        |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.42x faster                                                        |
| django_template         | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                        |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.41x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.87 ms: 1.41x faster                                                        |
| html5lib                | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                        |
| chameleon               | 9.06 ms                                                | 6.51 ms: 1.39x faster                                                        |
| pprint_safe_repr        | 955 ms                                                 | 690 ms: 1.38x faster                                                         |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                        |
| 2to3                    | 336 ms                                                 | 246 ms: 1.37x faster                                                         |
| async_tree_none         | 717 ms                                                 | 525 ms: 1.37x faster                                                         |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.36x faster                                                       |
| regex_compile           | 177 ms                                                 | 131 ms: 1.35x faster                                                         |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                        |
| scimark_fft             | 424 ms                                                 | 313 ms: 1.35x faster                                                         |
| thrift                  | 1.03 ms                                                | 766 us: 1.35x faster                                                         |
| async_tree_memoization  | 854 ms                                                 | 633 ms: 1.35x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.35x faster                                                       |
| xml_etree_process       | 74.9 ms                                                | 55.9 ms: 1.34x faster                                                        |
| tornado_http            | 127 ms                                                 | 95.1 ms: 1.34x faster                                                        |
| deepcopy                | 442 us                                                 | 333 us: 1.33x faster                                                         |
| genshi_xml              | 63.3 ms                                                | 48.1 ms: 1.32x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 103 ms: 1.31x faster                                                         |
| deepcopy_reduce         | 3.82 us                                                | 2.92 us: 1.31x faster                                                        |
| mypy2                   | 428 ms                                                 | 330 ms: 1.30x faster                                                         |
| fannkuch                | 486 ms                                                 | 376 ms: 1.29x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                | 50.6 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                 | 750 ms: 1.27x faster                                                         |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                       |
| nqueens                 | 100 ms                                                 | 81.2 ms: 1.23x faster                                                        |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.23x faster                                                        |
| sympy_str               | 328 ms                                                 | 270 ms: 1.22x faster                                                         |
| json_loads              | 28.8 us                                                | 23.9 us: 1.21x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 789 us: 1.20x faster                                                         |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                                         |
| dulwich_log             | 75.9 ms                                                | 63.4 ms: 1.20x faster                                                        |
| sympy_expand            | 545 ms                                                 | 456 ms: 1.19x faster                                                         |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.7 ms: 1.19x faster                                                        |
| json                    | 5.42 ms                                                | 4.61 ms: 1.17x faster                                                        |
| sympy_sum               | 185 ms                                                 | 158 ms: 1.17x faster                                                         |
| xml_etree_generate      | 94.2 ms                                                | 80.6 ms: 1.17x faster                                                        |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                                        |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.3 ms: 1.13x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| pickle_list             | 4.56 us                                                | 4.12 us: 1.11x faster                                                        |
| djangocms               | 35.9 us                                                | 32.5 us: 1.11x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.10x faster                                                         |
| meteor_contest          | 115 ms                                                 | 106 ms: 1.08x faster                                                         |
| regex_dna               | 222 ms                                                 | 211 ms: 1.05x faster                                                         |
| async_generators        | 425 ms                                                 | 410 ms: 1.04x faster                                                         |
| telco                   | 6.54 ms                                                | 6.32 ms: 1.04x faster                                                        |
| unpickle                | 14.1 us                                                | 13.7 us: 1.03x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.75 sec: 1.03x faster                                                       |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                                        |
| gc_traversal            | 3.84 ms                                                | 3.91 ms: 1.02x slower                                                        |
| unpickle_list           | 4.82 us                                                | 4.97 us: 1.03x slower                                                        |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                         |
| regex_effbot            | 3.23 ms                                                | 3.38 ms: 1.05x slower                                                        |
| python_startup_no_site  | 5.82 ms                                                | 6.49 ms: 1.12x slower                                                        |
| pickle_dict             | 27.3 us                                                | 30.9 us: 1.13x slower                                                        |
| coverage                | 72.8 ms                                                | 98.1 ms: 1.35x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x
