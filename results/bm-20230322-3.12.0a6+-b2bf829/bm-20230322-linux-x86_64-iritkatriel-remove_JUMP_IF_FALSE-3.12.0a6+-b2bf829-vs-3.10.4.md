
# Results vs. 3.10.4

- fork: iritkatriel
- ref: remove_JUMP_IF_FALSE
- machine: linux-x86_64
- commit hash: b2bf829
- commit date: 2023-03-22
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 248 ms: 1.35x faster                                                        |
| chameleon      | 9.06 ms                                                | 6.39 ms: 1.42x faster                                                       |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                      |
| html5lib       | 85.9 ms                                                | 60.8 ms: 1.41x faster                                                       |
| tornado_http   | 127 ms                                                 | 91.3 ms: 1.40x faster                                                       |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.1 ms: 1.63x faster                                                       |
| float          | 111 ms                                                 | 74.1 ms: 1.49x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                        |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                       |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.43 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 285 us: 1.60x faster                                                        |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.52x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.46 ms: 1.43x faster                                                       |
| xml_etree_process    | 74.9 ms                                                | 56.1 ms: 1.33x faster                                                       |
| json_loads           | 28.8 us                                                | 23.9 us: 1.20x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 80.7 ms: 1.17x faster                                                       |
| pickle_list          | 4.56 us                                                | 4.11 us: 1.11x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                        |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                       |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.04x slower                                                       |
| pickle_dict          | 27.3 us                                                | 31.9 us: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.81 ms: 1.61x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.51 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.94 ms: 1.49x faster                                                       |
| genshi_text     | 30.3 ms                                                | 21.7 ms: 1.40x faster                                                       |
| django_template | 45.9 ms                                                | 33.4 ms: 1.38x faster                                                       |
| genshi_xml      | 63.3 ms                                                | 47.4 ms: 1.34x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.0 ms: 2.65x faster                                                       |
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                                       |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                        |
| asyncio_tcp             | 925 ms                                                 | 506 ms: 1.83x faster                                                        |
| logging_silent          | 175 ns                                                 | 96.6 ns: 1.81x faster                                                       |
| richards                | 74.9 ms                                                | 43.9 ms: 1.71x faster                                                       |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                                        |
| spectral_norm           | 150 ms                                                 | 89.6 ms: 1.67x faster                                                       |
| scimark_monte_carlo     | 108 ms                                                 | 64.7 ms: 1.67x faster                                                       |
| pyflate                 | 673 ms                                                 | 407 ms: 1.65x faster                                                        |
| raytrace                | 464 ms                                                 | 284 ms: 1.63x faster                                                        |
| chaos                   | 106 ms                                                 | 65.4 ms: 1.63x faster                                                       |
| nbody                   | 142 ms                                                 | 87.1 ms: 1.63x faster                                                       |
| python_startup          | 14.2 ms                                                | 8.81 ms: 1.61x faster                                                       |
| crypto_pyaes            | 118 ms                                                 | 74.1 ms: 1.60x faster                                                       |
| pickle_pure_python      | 455 us                                                 | 285 us: 1.60x faster                                                        |
| hexiom                  | 9.53 ms                                                | 6.11 ms: 1.56x faster                                                       |
| deepcopy_memo           | 52.3 us                                                | 33.7 us: 1.55x faster                                                       |
| unpack_sequence         | 64.7 ns                                                | 42.0 ns: 1.54x faster                                                       |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.52x faster                                                        |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                        |
| float                   | 111 ms                                                 | 74.1 ms: 1.49x faster                                                       |
| mako                    | 14.8 ms                                                | 9.94 ms: 1.49x faster                                                       |
| scimark_fft             | 424 ms                                                 | 296 ms: 1.43x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.46 ms: 1.43x faster                                                       |
| coroutines              | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                       |
| chameleon               | 9.06 ms                                                | 6.39 ms: 1.42x faster                                                       |
| sqlglot_parse           | 2.06 ms                                                | 1.45 ms: 1.42x faster                                                       |
| html5lib                | 85.9 ms                                                | 60.8 ms: 1.41x faster                                                       |
| sqlglot_transpile       | 2.45 ms                                                | 1.75 ms: 1.40x faster                                                       |
| genshi_text             | 30.3 ms                                                | 21.7 ms: 1.40x faster                                                       |
| tornado_http            | 127 ms                                                 | 91.3 ms: 1.40x faster                                                       |
| logging_format          | 8.91 us                                                | 6.41 us: 1.39x faster                                                       |
| pprint_pformat          | 1.99 sec                                               | 1.43 sec: 1.39x faster                                                      |
| django_template         | 45.9 ms                                                | 33.4 ms: 1.38x faster                                                       |
| logging_simple          | 8.07 us                                                | 5.87 us: 1.37x faster                                                       |
| pprint_safe_repr        | 955 ms                                                 | 695 ms: 1.37x faster                                                        |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                                      |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                                        |
| deepcopy                | 442 us                                                 | 326 us: 1.36x faster                                                        |
| 2to3                    | 336 ms                                                 | 248 ms: 1.35x faster                                                        |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                       |
| pycparser               | 1.50 sec                                               | 1.12 sec: 1.34x faster                                                      |
| genshi_xml              | 63.3 ms                                                | 47.4 ms: 1.34x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.08 ms: 1.34x faster                                                       |
| xml_etree_process       | 74.9 ms                                                | 56.1 ms: 1.33x faster                                                       |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                        |
| thrift                  | 1.03 ms                                                | 780 us: 1.33x faster                                                        |
| deepcopy_reduce         | 3.82 us                                                | 2.92 us: 1.31x faster                                                       |
| async_tree_memoization  | 854 ms                                                 | 653 ms: 1.31x faster                                                        |
| fannkuch                | 486 ms                                                 | 372 ms: 1.31x faster                                                        |
| mypy2                   | 428 ms                                                 | 333 ms: 1.29x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                 | 743 ms: 1.28x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                | 51.4 ms: 1.27x faster                                                       |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                      |
| nqueens                 | 100 ms                                                 | 80.9 ms: 1.24x faster                                                       |
| json_loads              | 28.8 us                                                | 23.9 us: 1.20x faster                                                       |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.6 ms: 1.20x faster                                                       |
| dulwich_log             | 75.9 ms                                                | 63.3 ms: 1.20x faster                                                       |
| bench_thread_pool       | 947 us                                                 | 790 us: 1.20x faster                                                        |
| json                    | 5.42 ms                                                | 4.54 ms: 1.19x faster                                                       |
| sqlalchemy_declarative  | 165 ms                                                 | 139 ms: 1.19x faster                                                        |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                       |
| sympy_expand            | 545 ms                                                 | 459 ms: 1.19x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 80.7 ms: 1.17x faster                                                       |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                                        |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                       |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                                       |
| comprehensions          | 26.8 us                                                | 23.7 us: 1.13x faster                                                       |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                       |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                       |
| sympy_sum               | 185 ms                                                 | 165 ms: 1.12x faster                                                        |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                                       |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                        |
| pickle_list             | 4.56 us                                                | 4.11 us: 1.11x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.55 sec: 1.11x faster                                                      |
| regex_dna               | 222 ms                                                 | 203 ms: 1.09x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 153 ms: 1.07x faster                                                        |
| async_generators        | 425 ms                                                 | 413 ms: 1.03x faster                                                        |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                       |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| telco                   | 6.54 ms                                                | 6.60 ms: 1.01x slower                                                       |
| gc_traversal            | 3.84 ms                                                | 3.98 ms: 1.03x slower                                                       |
| unpickle_list           | 4.82 us                                                | 4.99 us: 1.04x slower                                                       |
| regex_effbot            | 3.23 ms                                                | 3.43 ms: 1.06x slower                                                       |
| python_startup_no_site  | 5.82 ms                                                | 6.51 ms: 1.12x slower                                                       |
| pickle_dict             | 27.3 us                                                | 31.9 us: 1.17x slower                                                       |
| dask                    | 423 ms                                                 | 503 ms: 1.19x slower                                                        |
| coverage                | 72.8 ms                                                | 95.9 ms: 1.32x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x
