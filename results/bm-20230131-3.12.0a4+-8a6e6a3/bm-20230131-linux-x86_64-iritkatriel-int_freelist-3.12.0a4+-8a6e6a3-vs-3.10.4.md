
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 8a6e6a3
- commit date: 2023-01-31
- overall geometric mean: 1.28x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                                |
| chameleon      | 9.06 ms                                                | 6.37 ms: 1.42x faster                                               |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                              |
| html5lib       | 85.9 ms                                                | 61.6 ms: 1.40x faster                                               |
| tornado_http   | 127 ms                                                 | 95.3 ms: 1.34x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 111 ms                                                 | 73.8 ms: 1.50x faster                                               |
| nbody          | 142 ms                                                 | 96.3 ms: 1.47x faster                                               |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                               |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.47 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.13x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                                |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.52x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.50 ms: 1.42x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 53.6 ms: 1.40x faster                                               |
| xml_etree_generate   | 94.2 ms                                                | 77.4 ms: 1.22x faster                                               |
| json_loads           | 28.8 us                                                | 24.7 us: 1.17x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| pickle_list          | 4.56 us                                                | 4.23 us: 1.08x faster                                               |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                               |
| unpickle             | 14.1 us                                                | 14.0 us: 1.01x faster                                               |
| unpickle_list        | 4.82 us                                                | 4.93 us: 1.02x slower                                               |
| pickle_dict          | 27.3 us                                                | 31.8 us: 1.17x slower                                               |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.97 ms: 1.58x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.49 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.80 ms: 1.51x faster                                               |
| genshi_text     | 30.3 ms                                                | 20.6 ms: 1.47x faster                                               |
| django_template | 45.9 ms                                                | 33.1 ms: 1.39x faster                                               |
| genshi_xml      | 63.3 ms                                                | 47.4 ms: 1.34x faster                                               |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.25 ms: 2.29x faster                                               |
| logging_silent          | 175 ns                                                 | 92.4 ns: 1.89x faster                                               |
| asyncio_tcp             | 925 ms                                                 | 498 ms: 1.86x faster                                                |
| richards                | 74.9 ms                                                | 43.2 ms: 1.73x faster                                               |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                                |
| chaos                   | 106 ms                                                 | 64.4 ms: 1.65x faster                                               |
| scimark_monte_carlo     | 108 ms                                                 | 66.4 ms: 1.63x faster                                               |
| scimark_sor             | 197 ms                                                 | 123 ms: 1.60x faster                                                |
| raytrace                | 464 ms                                                 | 291 ms: 1.60x faster                                                |
| hexiom                  | 9.53 ms                                                | 5.98 ms: 1.59x faster                                               |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                                |
| python_startup          | 14.2 ms                                                | 8.97 ms: 1.58x faster                                               |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                                |
| unpack_sequence         | 64.7 ns                                                | 42.7 ns: 1.52x faster                                               |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.52x faster                                                |
| mako                    | 14.8 ms                                                | 9.80 ms: 1.51x faster                                               |
| deepcopy_memo           | 52.3 us                                                | 34.9 us: 1.50x faster                                               |
| float                   | 111 ms                                                 | 73.8 ms: 1.50x faster                                               |
| nbody                   | 142 ms                                                 | 96.3 ms: 1.47x faster                                               |
| genshi_text             | 30.3 ms                                                | 20.6 ms: 1.47x faster                                               |
| pyflate                 | 673 ms                                                 | 461 ms: 1.46x faster                                                |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                              |
| pprint_safe_repr        | 955 ms                                                 | 669 ms: 1.43x faster                                                |
| json_dumps              | 13.5 ms                                                | 9.50 ms: 1.42x faster                                               |
| chameleon               | 9.06 ms                                                | 6.37 ms: 1.42x faster                                               |
| logging_format          | 8.91 us                                                | 6.35 us: 1.40x faster                                               |
| xml_etree_process       | 74.9 ms                                                | 53.6 ms: 1.40x faster                                               |
| html5lib                | 85.9 ms                                                | 61.6 ms: 1.40x faster                                               |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                |
| logging_simple          | 8.07 us                                                | 5.79 us: 1.39x faster                                               |
| sqlglot_parse           | 2.06 ms                                                | 1.48 ms: 1.39x faster                                               |
| django_template         | 45.9 ms                                                | 33.1 ms: 1.39x faster                                               |
| thrift                  | 1.03 ms                                                | 751 us: 1.38x faster                                                |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                               |
| sqlglot_transpile       | 2.45 ms                                                | 1.78 ms: 1.37x faster                                               |
| async_tree_none         | 717 ms                                                 | 528 ms: 1.36x faster                                                |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                               |
| fannkuch                | 486 ms                                                 | 360 ms: 1.35x faster                                                |
| pycparser               | 1.50 sec                                               | 1.12 sec: 1.34x faster                                              |
| tornado_http            | 127 ms                                                 | 95.3 ms: 1.34x faster                                               |
| genshi_xml              | 63.3 ms                                                | 47.4 ms: 1.34x faster                                               |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.33x faster                                              |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                                |
| deepcopy                | 442 us                                                 | 331 us: 1.33x faster                                                |
| crypto_pyaes            | 118 ms                                                 | 90.0 ms: 1.32x faster                                               |
| nqueens                 | 100 ms                                                 | 76.2 ms: 1.31x faster                                               |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                |
| async_tree_memoization  | 854 ms                                                 | 659 ms: 1.30x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                               |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                              |
| deepcopy_reduce         | 3.82 us                                                | 3.02 us: 1.27x faster                                               |
| coroutines              | 31.8 ms                                                | 25.3 ms: 1.26x faster                                               |
| async_tree_cpu_io_mixed | 951 ms                                                 | 761 ms: 1.25x faster                                                |
| sympy_integrate         | 24.3 ms                                                | 19.7 ms: 1.23x faster                                               |
| xml_etree_generate      | 94.2 ms                                                | 77.4 ms: 1.22x faster                                               |
| sympy_str               | 328 ms                                                 | 271 ms: 1.21x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.55 ms: 1.20x faster                                               |
| sympy_sum               | 185 ms                                                 | 156 ms: 1.19x faster                                                |
| sympy_expand            | 545 ms                                                 | 459 ms: 1.19x faster                                                |
| bench_thread_pool       | 947 us                                                 | 801 us: 1.18x faster                                                |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                               |
| dulwich_log             | 75.9 ms                                                | 64.4 ms: 1.18x faster                                               |
| json_loads              | 28.8 us                                                | 24.7 us: 1.17x faster                                               |
| json                    | 5.42 ms                                                | 4.69 ms: 1.16x faster                                               |
| async_generators        | 425 ms                                                 | 369 ms: 1.15x faster                                                |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                               |
| mdp                     | 2.82 sec                                               | 2.53 sec: 1.11x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                               |
| sqlite_synth            | 2.93 us                                                | 2.68 us: 1.09x faster                                               |
| scimark_fft             | 424 ms                                                 | 390 ms: 1.09x faster                                                |
| spectral_norm           | 150 ms                                                 | 138 ms: 1.09x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| pickle_list             | 4.56 us                                                | 4.23 us: 1.08x faster                                               |
| regex_dna               | 222 ms                                                 | 208 ms: 1.07x faster                                                |
| pathlib                 | 20.0 ms                                                | 18.9 ms: 1.06x faster                                               |
| telco                   | 6.54 ms                                                | 6.43 ms: 1.02x faster                                               |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                               |
| gc_traversal            | 3.84 ms                                                | 3.81 ms: 1.01x faster                                               |
| unpickle                | 14.1 us                                                | 14.0 us: 1.01x faster                                               |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| unpickle_list           | 4.82 us                                                | 4.93 us: 1.02x slower                                               |
| regex_effbot            | 3.23 ms                                                | 3.47 ms: 1.07x slower                                               |
| generators              | 76.8 ms                                                | 83.5 ms: 1.09x slower                                               |
| python_startup_no_site  | 5.82 ms                                                | 6.49 ms: 1.12x slower                                               |
| pickle_dict             | 27.3 us                                                | 31.8 us: 1.17x slower                                               |
| dask                    | 423 ms                                                 | 525 ms: 1.24x slower                                                |
| coverage                | 72.8 ms                                                | 96.1 ms: 1.32x slower                                               |
| Geometric mean          | (ref)                                                  | 1.28x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230131-3.12.0a4+-8a6e6a3/bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.22x
