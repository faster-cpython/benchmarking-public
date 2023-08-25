
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 933012e
- commit date: 2023-01-18
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 249 ms: 1.35x faster                                                        |
| chameleon      | 9.06 ms                                                | 6.37 ms: 1.42x faster                                                       |
| docutils       | 3.17 sec                                               | 2.48 sec: 1.28x faster                                                      |
| html5lib       | 85.9 ms                                                | 59.8 ms: 1.44x faster                                                       |
| tornado_http   | 127 ms                                                 | 94.3 ms: 1.35x faster                                                       |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.3 ms: 1.53x faster                                                       |
| nbody          | 142 ms                                                 | 94.1 ms: 1.50x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                        |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                       |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.51 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 280 us: 1.63x faster                                                        |
| unpickle_pure_python | 300 us                                                 | 196 us: 1.53x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.32 ms: 1.45x faster                                                       |
| xml_etree_process    | 74.9 ms                                                | 54.1 ms: 1.39x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 78.5 ms: 1.20x faster                                                       |
| json_loads           | 28.8 us                                                | 24.1 us: 1.20x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.21 us: 1.08x faster                                                       |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                       |
| unpickle_list        | 4.82 us                                                | 5.09 us: 1.06x slower                                                       |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.85 ms: 1.60x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.39 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.21x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.50 ms: 1.55x faster                                                       |
| genshi_text     | 30.3 ms                                                | 20.0 ms: 1.51x faster                                                       |
| django_template | 45.9 ms                                                | 32.3 ms: 1.42x faster                                                       |
| genshi_xml      | 63.3 ms                                                | 46.0 ms: 1.38x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.20 ms: 2.32x faster                                                       |
| logging_silent          | 175 ns                                                 | 90.4 ns: 1.94x faster                                                       |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                                        |
| asyncio_tcp             | 925 ms                                                 | 497 ms: 1.86x faster                                                        |
| richards                | 74.9 ms                                                | 42.2 ms: 1.78x faster                                                       |
| go                      | 229 ms                                                 | 134 ms: 1.72x faster                                                        |
| pyflate                 | 673 ms                                                 | 399 ms: 1.69x faster                                                        |
| chaos                   | 106 ms                                                 | 63.3 ms: 1.68x faster                                                       |
| scimark_monte_carlo     | 108 ms                                                 | 65.9 ms: 1.64x faster                                                       |
| raytrace                | 464 ms                                                 | 283 ms: 1.64x faster                                                        |
| pickle_pure_python      | 455 us                                                 | 280 us: 1.63x faster                                                        |
| python_startup          | 14.2 ms                                                | 8.85 ms: 1.60x faster                                                       |
| crypto_pyaes            | 118 ms                                                 | 74.1 ms: 1.60x faster                                                       |
| hexiom                  | 9.53 ms                                                | 5.96 ms: 1.60x faster                                                       |
| mako                    | 14.8 ms                                                | 9.50 ms: 1.55x faster                                                       |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.55x faster                                                        |
| spectral_norm           | 150 ms                                                 | 97.4 ms: 1.54x faster                                                       |
| unpickle_pure_python    | 300 us                                                 | 196 us: 1.53x faster                                                        |
| float                   | 111 ms                                                 | 72.3 ms: 1.53x faster                                                       |
| deepcopy_memo           | 52.3 us                                                | 34.4 us: 1.52x faster                                                       |
| genshi_text             | 30.3 ms                                                | 20.0 ms: 1.51x faster                                                       |
| nbody                   | 142 ms                                                 | 94.1 ms: 1.50x faster                                                       |
| unpack_sequence         | 64.7 ns                                                | 44.0 ns: 1.47x faster                                                       |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.32 ms: 1.45x faster                                                       |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                                      |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                                       |
| logging_format          | 8.91 us                                                | 6.18 us: 1.44x faster                                                       |
| logging_simple          | 8.07 us                                                | 5.62 us: 1.44x faster                                                       |
| html5lib                | 85.9 ms                                                | 59.8 ms: 1.44x faster                                                       |
| pprint_safe_repr        | 955 ms                                                 | 670 ms: 1.43x faster                                                        |
| django_template         | 45.9 ms                                                | 32.3 ms: 1.42x faster                                                       |
| chameleon               | 9.06 ms                                                | 6.37 ms: 1.42x faster                                                       |
| scimark_fft             | 424 ms                                                 | 301 ms: 1.41x faster                                                        |
| thrift                  | 1.03 ms                                                | 739 us: 1.40x faster                                                        |
| aiohttp                 | 1.38 ms                                                | 991 us: 1.40x faster                                                        |
| pycparser               | 1.50 sec                                               | 1.08 sec: 1.39x faster                                                      |
| xml_etree_process       | 74.9 ms                                                | 54.1 ms: 1.39x faster                                                       |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.96 ms: 1.38x faster                                                       |
| gunicorn                | 1.46 ms                                                | 1.06 ms: 1.38x faster                                                       |
| genshi_xml              | 63.3 ms                                                | 46.0 ms: 1.38x faster                                                       |
| async_tree_none         | 717 ms                                                 | 527 ms: 1.36x faster                                                        |
| deepcopy                | 442 us                                                 | 325 us: 1.36x faster                                                        |
| tornado_http            | 127 ms                                                 | 94.3 ms: 1.35x faster                                                       |
| 2to3                    | 336 ms                                                 | 249 ms: 1.35x faster                                                        |
| fannkuch                | 486 ms                                                 | 362 ms: 1.34x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                                      |
| async_tree_memoization  | 854 ms                                                 | 639 ms: 1.34x faster                                                        |
| deepcopy_reduce         | 3.82 us                                                | 2.92 us: 1.31x faster                                                       |
| nqueens                 | 100 ms                                                 | 77.2 ms: 1.30x faster                                                       |
| docutils                | 3.17 sec                                               | 2.48 sec: 1.28x faster                                                      |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                | 51.4 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed | 951 ms                                                 | 751 ms: 1.27x faster                                                        |
| sympy_integrate         | 24.3 ms                                                | 19.7 ms: 1.23x faster                                                       |
| coroutines              | 31.8 ms                                                | 26.0 ms: 1.23x faster                                                       |
| async_generators        | 425 ms                                                 | 349 ms: 1.22x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 779 us: 1.22x faster                                                        |
| sympy_str               | 328 ms                                                 | 270 ms: 1.21x faster                                                        |
| dulwich_log             | 75.9 ms                                                | 62.9 ms: 1.21x faster                                                       |
| sympy_expand            | 545 ms                                                 | 453 ms: 1.20x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 78.5 ms: 1.20x faster                                                       |
| json_loads              | 28.8 us                                                | 24.1 us: 1.20x faster                                                       |
| sympy_sum               | 185 ms                                                 | 155 ms: 1.19x faster                                                        |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                       |
| json                    | 5.42 ms                                                | 4.64 ms: 1.17x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.44 sec: 1.15x faster                                                      |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                                       |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                       |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                                       |
| djangocms               | 35.9 us                                                | 31.9 us: 1.13x faster                                                       |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                        |
| gc_traversal            | 3.84 ms                                                | 3.51 ms: 1.09x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                        |
| pickle_list             | 4.56 us                                                | 4.21 us: 1.08x faster                                                       |
| regex_dna               | 222 ms                                                 | 207 ms: 1.07x faster                                                        |
| telco                   | 6.54 ms                                                | 6.42 ms: 1.02x faster                                                       |
| generators              | 76.8 ms                                                | 76.0 ms: 1.01x faster                                                       |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                       |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| unpickle_list           | 4.82 us                                                | 5.09 us: 1.06x slower                                                       |
| regex_effbot            | 3.23 ms                                                | 3.51 ms: 1.09x slower                                                       |
| python_startup_no_site  | 5.82 ms                                                | 6.39 ms: 1.10x slower                                                       |
| pickle_dict             | 27.3 us                                                | 31.6 us: 1.16x slower                                                       |
| dask                    | 423 ms                                                 | 496 ms: 1.17x slower                                                        |
| coverage                | 72.8 ms                                                | 96.1 ms: 1.32x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230118-3.12.0a4+-933012e/bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.27x
