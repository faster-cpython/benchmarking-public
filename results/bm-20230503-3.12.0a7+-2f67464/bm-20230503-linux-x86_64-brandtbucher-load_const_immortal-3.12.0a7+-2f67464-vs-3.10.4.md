
# Results vs. 3.10.4

- fork: brandtbucher
- ref: load_const_immortal
- machine: linux-x86_64
- commit hash: 2f67464
- commit date: 2023-05-03
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 270 ms: 1.24x faster                                                        |
| docutils       | 3.17 sec                                               | 2.76 sec: 1.15x faster                                                      |
| tornado_http   | 127 ms                                                 | 99.8 ms: 1.28x faster                                                       |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.2 ms: 1.59x faster                                                       |
| float          | 111 ms                                                 | 81.9 ms: 1.35x faster                                                       |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 146 ms: 1.21x faster                                                        |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                       |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.55 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 318 us: 1.43x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.86 ms: 1.37x faster                                                       |
| unpickle_pure_python | 300 us                                                 | 219 us: 1.37x faster                                                        |
| xml_etree_process    | 74.9 ms                                                | 60.4 ms: 1.24x faster                                                       |
| json_loads           | 28.8 us                                                | 26.0 us: 1.11x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 86.3 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.06x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.48 us: 1.02x faster                                                       |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.02x slower                                                       |
| pickle               | 10.3 us                                                | 10.8 us: 1.05x slower                                                       |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                                       |
| pickle_dict          | 27.3 us                                                | 32.1 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.16 ms: 1.54x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.68 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 31.0 ms: 2.48x faster                                                       |
| deltablue               | 7.42 ms                                                | 3.57 ms: 2.08x faster                                                       |
| asyncio_tcp             | 925 ms                                                 | 510 ms: 1.81x faster                                                        |
| logging_silent          | 175 ns                                                 | 102 ns: 1.72x faster                                                        |
| go                      | 229 ms                                                 | 137 ms: 1.68x faster                                                        |
| richards                | 74.9 ms                                                | 45.4 ms: 1.65x faster                                                       |
| scimark_sor             | 197 ms                                                 | 123 ms: 1.60x faster                                                        |
| nbody                   | 142 ms                                                 | 89.2 ms: 1.59x faster                                                       |
| python_startup          | 14.2 ms                                                | 9.16 ms: 1.54x faster                                                       |
| chaos                   | 106 ms                                                 | 69.4 ms: 1.53x faster                                                       |
| sqlglot_parse           | 2.06 ms                                                | 1.35 ms: 1.53x faster                                                       |
| raytrace                | 464 ms                                                 | 306 ms: 1.52x faster                                                        |
| hexiom                  | 9.53 ms                                                | 6.30 ms: 1.51x faster                                                       |
| pyflate                 | 673 ms                                                 | 450 ms: 1.49x faster                                                        |
| scimark_monte_carlo     | 108 ms                                                 | 73.4 ms: 1.48x faster                                                       |
| crypto_pyaes            | 118 ms                                                 | 80.5 ms: 1.47x faster                                                       |
| sqlglot_transpile       | 2.45 ms                                                | 1.67 ms: 1.47x faster                                                       |
| scimark_lu              | 163 ms                                                 | 113 ms: 1.45x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 1.24 sec: 1.44x faster                                                      |
| pickle_pure_python      | 455 us                                                 | 318 us: 1.43x faster                                                        |
| async_tree_none         | 717 ms                                                 | 500 ms: 1.43x faster                                                        |
| coroutines              | 31.8 ms                                                | 22.3 ms: 1.42x faster                                                       |
| spectral_norm           | 150 ms                                                 | 108 ms: 1.39x faster                                                        |
| async_tree_memoization  | 854 ms                                                 | 615 ms: 1.39x faster                                                        |
| mako                    | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.86 ms: 1.37x faster                                                       |
| unpickle_pure_python    | 300 us                                                 | 219 us: 1.37x faster                                                        |
| float                   | 111 ms                                                 | 81.9 ms: 1.35x faster                                                       |
| deepcopy_memo           | 52.3 us                                                | 38.8 us: 1.35x faster                                                       |
| async_tree_cpu_io_mixed | 951 ms                                                 | 722 ms: 1.32x faster                                                        |
| pprint_pformat          | 1.99 sec                                               | 1.51 sec: 1.31x faster                                                      |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                      |
| unpack_sequence         | 64.7 ns                                                | 50.0 ns: 1.29x faster                                                       |
| pprint_safe_repr        | 955 ms                                                 | 740 ms: 1.29x faster                                                        |
| fannkuch                | 486 ms                                                 | 379 ms: 1.28x faster                                                        |
| logging_simple          | 8.07 us                                                | 6.31 us: 1.28x faster                                                       |
| tornado_http            | 127 ms                                                 | 99.8 ms: 1.28x faster                                                       |
| logging_format          | 8.91 us                                                | 7.08 us: 1.26x faster                                                       |
| 2to3                    | 336 ms                                                 | 270 ms: 1.24x faster                                                        |
| xml_etree_process       | 74.9 ms                                                | 60.4 ms: 1.24x faster                                                       |
| mypy2                   | 428 ms                                                 | 354 ms: 1.21x faster                                                        |
| regex_compile           | 177 ms                                                 | 146 ms: 1.21x faster                                                        |
| deepcopy                | 442 us                                                 | 367 us: 1.21x faster                                                        |
| nqueens                 | 100 ms                                                 | 83.3 ms: 1.20x faster                                                       |
| scimark_fft             | 424 ms                                                 | 353 ms: 1.20x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 113 ms: 1.20x faster                                                        |
| deepcopy_reduce         | 3.82 us                                                | 3.23 us: 1.19x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 55.4 ms: 1.18x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.74 ms: 1.15x faster                                                       |
| docutils                | 3.17 sec                                               | 2.76 sec: 1.15x faster                                                      |
| comprehensions          | 26.8 us                                                | 23.5 us: 1.14x faster                                                       |
| bench_thread_pool       | 947 us                                                 | 833 us: 1.14x faster                                                        |
| sqlalchemy_declarative  | 165 ms                                                 | 147 ms: 1.13x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                       |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                       |
| dulwich_log             | 75.9 ms                                                | 68.0 ms: 1.12x faster                                                       |
| json_loads              | 28.8 us                                                | 26.0 us: 1.11x faster                                                       |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.3 ms: 1.10x faster                                                       |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                                        |
| sqlite_synth            | 2.93 us                                                | 2.68 us: 1.09x faster                                                       |
| xml_etree_generate      | 94.2 ms                                                | 86.3 ms: 1.09x faster                                                       |
| json                    | 5.42 ms                                                | 4.98 ms: 1.09x faster                                                       |
| pathlib                 | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.62 sec: 1.08x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 153 ms: 1.06x faster                                                        |
| regex_dna               | 222 ms                                                 | 209 ms: 1.06x faster                                                        |
| pickle_list             | 4.56 us                                                | 4.48 us: 1.02x faster                                                       |
| unpickle_list           | 4.82 us                                                | 4.94 us: 1.02x slower                                                       |
| gc_traversal            | 3.84 ms                                                | 3.94 ms: 1.03x slower                                                       |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                        |
| pickle                  | 10.3 us                                                | 10.8 us: 1.05x slower                                                       |
| unpickle                | 14.1 us                                                | 15.0 us: 1.06x slower                                                       |
| async_generators        | 425 ms                                                 | 455 ms: 1.07x slower                                                        |
| telco                   | 6.54 ms                                                | 7.05 ms: 1.08x slower                                                       |
| regex_effbot            | 3.23 ms                                                | 3.55 ms: 1.10x slower                                                       |
| python_startup_no_site  | 5.82 ms                                                | 6.68 ms: 1.15x slower                                                       |
| pickle_dict             | 27.3 us                                                | 32.1 us: 1.18x slower                                                       |
| dask                    | 423 ms                                                 | 542 ms: 1.28x slower                                                        |
| coverage                | 72.8 ms                                                | 102 ms: 1.41x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.24x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x
