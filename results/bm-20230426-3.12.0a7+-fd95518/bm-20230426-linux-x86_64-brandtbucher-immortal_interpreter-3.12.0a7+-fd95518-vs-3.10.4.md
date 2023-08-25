
# Results vs. 3.10.4

- fork: brandtbucher
- ref: immortal_interpreter
- machine: linux-x86_64
- commit hash: fd95518
- commit date: 2023-04-26
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 269 ms: 1.25x faster                                                         |
| chameleon      | 9.06 ms                                                | 7.01 ms: 1.29x faster                                                        |
| docutils       | 3.17 sec                                               | 2.72 sec: 1.16x faster                                                       |
| html5lib       | 85.9 ms                                                | 65.6 ms: 1.31x faster                                                        |
| tornado_http   | 127 ms                                                 | 106 ms: 1.21x faster                                                         |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.5 ms: 1.60x faster                                                        |
| float          | 111 ms                                                 | 81.1 ms: 1.36x faster                                                        |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 143 ms: 1.24x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                        |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                                         |
| regex_effbot   | 3.23 ms                                                | 3.49 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 315 us: 1.45x faster                                                         |
| unpickle_pure_python | 300 us                                                 | 216 us: 1.39x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.92 ms: 1.36x faster                                                        |
| xml_etree_process    | 74.9 ms                                                | 58.8 ms: 1.28x faster                                                        |
| json_loads           | 28.8 us                                                | 25.6 us: 1.13x faster                                                        |
| xml_etree_generate   | 94.2 ms                                                | 84.6 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                                         |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                         |
| pickle_list          | 4.56 us                                                | 4.52 us: 1.01x faster                                                        |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                                        |
| unpickle_list        | 4.82 us                                                | 4.91 us: 1.02x slower                                                        |
| unpickle             | 14.1 us                                                | 14.7 us: 1.04x slower                                                        |
| pickle_dict          | 27.3 us                                                | 30.9 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.13 ms: 1.55x faster                                                        |
| python_startup_no_site | 5.82 ms                                                | 6.69 ms: 1.15x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                        |
| genshi_text     | 30.3 ms                                                | 22.8 ms: 1.33x faster                                                        |
| django_template | 45.9 ms                                                | 34.7 ms: 1.32x faster                                                        |
| genshi_xml      | 63.3 ms                                                | 51.6 ms: 1.23x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 31.2 ms: 2.46x faster                                                        |
| deltablue               | 7.42 ms                                                | 3.53 ms: 2.10x faster                                                        |
| asyncio_tcp             | 925 ms                                                 | 505 ms: 1.83x faster                                                         |
| logging_silent          | 175 ns                                                 | 99.0 ns: 1.77x faster                                                        |
| richards                | 74.9 ms                                                | 43.4 ms: 1.73x faster                                                        |
| go                      | 229 ms                                                 | 139 ms: 1.65x faster                                                         |
| scimark_sor             | 197 ms                                                 | 122 ms: 1.61x faster                                                         |
| nbody                   | 142 ms                                                 | 88.5 ms: 1.60x faster                                                        |
| sqlglot_parse           | 2.06 ms                                                | 1.32 ms: 1.55x faster                                                        |
| hexiom                  | 9.53 ms                                                | 6.13 ms: 1.55x faster                                                        |
| python_startup          | 14.2 ms                                                | 9.13 ms: 1.55x faster                                                        |
| raytrace                | 464 ms                                                 | 300 ms: 1.54x faster                                                         |
| chaos                   | 106 ms                                                 | 69.2 ms: 1.53x faster                                                        |
| scimark_monte_carlo     | 108 ms                                                 | 71.3 ms: 1.52x faster                                                        |
| pyflate                 | 673 ms                                                 | 446 ms: 1.51x faster                                                         |
| sqlglot_transpile       | 2.45 ms                                                | 1.65 ms: 1.48x faster                                                        |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.48x faster                                                         |
| crypto_pyaes            | 118 ms                                                 | 80.5 ms: 1.47x faster                                                        |
| pickle_pure_python      | 455 us                                                 | 315 us: 1.45x faster                                                         |
| spectral_norm           | 150 ms                                                 | 105 ms: 1.43x faster                                                         |
| unpickle_pure_python    | 300 us                                                 | 216 us: 1.39x faster                                                         |
| coroutines              | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 1.28 sec: 1.38x faster                                                       |
| mako                    | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.92 ms: 1.36x faster                                                        |
| float                   | 111 ms                                                 | 81.1 ms: 1.36x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 38.5 us: 1.36x faster                                                        |
| async_tree_none         | 717 ms                                                 | 528 ms: 1.36x faster                                                         |
| pprint_pformat          | 1.99 sec                                               | 1.47 sec: 1.35x faster                                                       |
| genshi_text             | 30.3 ms                                                | 22.8 ms: 1.33x faster                                                        |
| django_template         | 45.9 ms                                                | 34.7 ms: 1.32x faster                                                        |
| pprint_safe_repr        | 955 ms                                                 | 724 ms: 1.32x faster                                                         |
| async_tree_memoization  | 854 ms                                                 | 650 ms: 1.31x faster                                                         |
| html5lib                | 85.9 ms                                                | 65.6 ms: 1.31x faster                                                        |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                       |
| fannkuch                | 486 ms                                                 | 374 ms: 1.30x faster                                                         |
| logging_simple          | 8.07 us                                                | 6.22 us: 1.30x faster                                                        |
| chameleon               | 9.06 ms                                                | 7.01 ms: 1.29x faster                                                        |
| thrift                  | 1.03 ms                                                | 800 us: 1.29x faster                                                         |
| logging_format          | 8.91 us                                                | 6.96 us: 1.28x faster                                                        |
| xml_etree_process       | 74.9 ms                                                | 58.8 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                 | 750 ms: 1.27x faster                                                         |
| nqueens                 | 100 ms                                                 | 79.8 ms: 1.25x faster                                                        |
| 2to3                    | 336 ms                                                 | 269 ms: 1.25x faster                                                         |
| regex_compile           | 177 ms                                                 | 143 ms: 1.24x faster                                                         |
| mypy2                   | 428 ms                                                 | 349 ms: 1.23x faster                                                         |
| genshi_xml              | 63.3 ms                                                | 51.6 ms: 1.23x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 112 ms: 1.21x faster                                                         |
| deepcopy                | 442 us                                                 | 366 us: 1.21x faster                                                         |
| tornado_http            | 127 ms                                                 | 106 ms: 1.21x faster                                                         |
| scimark_fft             | 424 ms                                                 | 352 ms: 1.20x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                | 54.3 ms: 1.20x faster                                                        |
| deepcopy_reduce         | 3.82 us                                                | 3.19 us: 1.20x faster                                                        |
| unpack_sequence         | 64.7 ns                                                | 54.1 ns: 1.20x faster                                                        |
| docutils                | 3.17 sec                                               | 2.72 sec: 1.16x faster                                                       |
| comprehensions          | 26.8 us                                                | 23.4 us: 1.15x faster                                                        |
| sqlalchemy_declarative  | 165 ms                                                 | 146 ms: 1.14x faster                                                         |
| bench_thread_pool       | 947 us                                                 | 835 us: 1.13x faster                                                         |
| json_loads              | 28.8 us                                                | 25.6 us: 1.13x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.85 ms: 1.13x faster                                                        |
| dulwich_log             | 75.9 ms                                                | 67.8 ms: 1.12x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                        |
| pylint                  | 525 ms                                                 | 471 ms: 1.11x faster                                                         |
| xml_etree_generate      | 94.2 ms                                                | 84.6 ms: 1.11x faster                                                        |
| sympy_integrate         | 24.3 ms                                                | 21.9 ms: 1.11x faster                                                        |
| create_gc_cycles        | 1.67 ms                                                | 1.51 ms: 1.11x faster                                                        |
| json                    | 5.42 ms                                                | 4.91 ms: 1.10x faster                                                        |
| sympy_expand            | 545 ms                                                 | 498 ms: 1.09x faster                                                         |
| mdp                     | 2.82 sec                                               | 2.59 sec: 1.09x faster                                                       |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.5 ms: 1.09x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.09x faster                                                         |
| pathlib                 | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                        |
| sqlite_synth            | 2.93 us                                                | 2.71 us: 1.08x faster                                                        |
| djangocms               | 35.9 us                                                | 33.3 us: 1.08x faster                                                        |
| regex_dna               | 222 ms                                                 | 207 ms: 1.07x faster                                                         |
| xml_etree_parse         | 163 ms                                                 | 154 ms: 1.06x faster                                                         |
| sympy_str               | 328 ms                                                 | 311 ms: 1.06x faster                                                         |
| meteor_contest          | 115 ms                                                 | 112 ms: 1.02x faster                                                         |
| pickle_list             | 4.56 us                                                | 4.52 us: 1.01x faster                                                        |
| sympy_sum               | 185 ms                                                 | 183 ms: 1.01x faster                                                         |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                                         |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                                        |
| unpickle_list           | 4.82 us                                                | 4.91 us: 1.02x slower                                                        |
| async_generators        | 425 ms                                                 | 437 ms: 1.03x slower                                                         |
| unpickle                | 14.1 us                                                | 14.7 us: 1.04x slower                                                        |
| gc_traversal            | 3.84 ms                                                | 3.99 ms: 1.04x slower                                                        |
| telco                   | 6.54 ms                                                | 6.90 ms: 1.06x slower                                                        |
| regex_effbot            | 3.23 ms                                                | 3.49 ms: 1.08x slower                                                        |
| pickle_dict             | 27.3 us                                                | 30.9 us: 1.13x slower                                                        |
| python_startup_no_site  | 5.82 ms                                                | 6.69 ms: 1.15x slower                                                        |
| dask                    | 423 ms                                                 | 539 ms: 1.28x slower                                                         |
| coverage                | 72.8 ms                                                | 100 ms: 1.38x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.23x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x
