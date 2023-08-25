
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: fe65f49
- commit date: 2023-01-31
- overall geometric mean: 1.28x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                |
| chameleon      | 9.06 ms                                                | 6.29 ms: 1.44x faster                                               |
| docutils       | 3.17 sec                                               | 2.51 sec: 1.26x faster                                              |
| html5lib       | 85.9 ms                                                | 61.9 ms: 1.39x faster                                               |
| tornado_http   | 127 ms                                                 | 95.0 ms: 1.34x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.8 ms: 1.52x faster                                               |
| nbody          | 142 ms                                                 | 97.9 ms: 1.45x faster                                               |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                               |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.50 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.12x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 285 us: 1.60x faster                                                |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.35 ms: 1.45x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 53.2 ms: 1.41x faster                                               |
| xml_etree_generate   | 94.2 ms                                                | 77.7 ms: 1.21x faster                                               |
| json_loads           | 28.8 us                                                | 24.6 us: 1.17x faster                                               |
| pickle_list          | 4.56 us                                                | 4.09 us: 1.11x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| unpickle             | 14.1 us                                                | 13.6 us: 1.04x faster                                               |
| unpickle_list        | 4.82 us                                                | 4.90 us: 1.02x slower                                               |
| pickle_dict          | 27.3 us                                                | 30.5 us: 1.12x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.94 ms: 1.58x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.47 ms: 1.11x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.82 ms: 1.50x faster                                               |
| genshi_text     | 30.3 ms                                                | 20.2 ms: 1.50x faster                                               |
| django_template | 45.9 ms                                                | 32.6 ms: 1.41x faster                                               |
| genshi_xml      | 63.3 ms                                                | 47.0 ms: 1.35x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.24 ms: 2.29x faster                                               |
| logging_silent          | 175 ns                                                 | 91.3 ns: 1.92x faster                                               |
| asyncio_tcp             | 925 ms                                                 | 496 ms: 1.86x faster                                                |
| richards                | 74.9 ms                                                | 43.8 ms: 1.71x faster                                               |
| go                      | 229 ms                                                 | 138 ms: 1.66x faster                                                |
| scimark_monte_carlo     | 108 ms                                                 | 67.6 ms: 1.60x faster                                               |
| chaos                   | 106 ms                                                 | 66.4 ms: 1.60x faster                                               |
| pickle_pure_python      | 455 us                                                 | 285 us: 1.60x faster                                                |
| hexiom                  | 9.53 ms                                                | 5.99 ms: 1.59x faster                                               |
| raytrace                | 464 ms                                                 | 292 ms: 1.59x faster                                                |
| python_startup          | 14.2 ms                                                | 8.94 ms: 1.58x faster                                               |
| scimark_sor             | 197 ms                                                 | 125 ms: 1.57x faster                                                |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                                |
| float                   | 111 ms                                                 | 72.8 ms: 1.52x faster                                               |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                                |
| deepcopy_memo           | 52.3 us                                                | 34.7 us: 1.51x faster                                               |
| unpack_sequence         | 64.7 ns                                                | 43.0 ns: 1.51x faster                                               |
| mako                    | 14.8 ms                                                | 9.82 ms: 1.50x faster                                               |
| genshi_text             | 30.3 ms                                                | 20.2 ms: 1.50x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.35 ms: 1.45x faster                                               |
| nbody                   | 142 ms                                                 | 97.9 ms: 1.45x faster                                               |
| chameleon               | 9.06 ms                                                | 6.29 ms: 1.44x faster                                               |
| pyflate                 | 673 ms                                                 | 467 ms: 1.44x faster                                                |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.42x faster                                              |
| logging_format          | 8.91 us                                                | 6.29 us: 1.42x faster                                               |
| logging_simple          | 8.07 us                                                | 5.72 us: 1.41x faster                                               |
| pprint_safe_repr        | 955 ms                                                 | 678 ms: 1.41x faster                                                |
| xml_etree_process       | 74.9 ms                                                | 53.2 ms: 1.41x faster                                               |
| django_template         | 45.9 ms                                                | 32.6 ms: 1.41x faster                                               |
| thrift                  | 1.03 ms                                                | 735 us: 1.41x faster                                                |
| sqlglot_parse           | 2.06 ms                                                | 1.48 ms: 1.40x faster                                               |
| html5lib                | 85.9 ms                                                | 61.9 ms: 1.39x faster                                               |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                |
| sqlglot_transpile       | 2.45 ms                                                | 1.78 ms: 1.38x faster                                               |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                               |
| async_tree_none         | 717 ms                                                 | 523 ms: 1.37x faster                                                |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.36x faster                                              |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                               |
| genshi_xml              | 63.3 ms                                                | 47.0 ms: 1.35x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 635 ms: 1.34x faster                                                |
| pycparser               | 1.50 sec                                               | 1.12 sec: 1.34x faster                                              |
| tornado_http            | 127 ms                                                 | 95.0 ms: 1.34x faster                                               |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                                |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                |
| crypto_pyaes            | 118 ms                                                 | 89.5 ms: 1.32x faster                                               |
| fannkuch                | 486 ms                                                 | 369 ms: 1.32x faster                                                |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                |
| deepcopy_reduce         | 3.82 us                                                | 2.96 us: 1.29x faster                                               |
| sqlglot_optimize        | 65.3 ms                                                | 50.7 ms: 1.29x faster                                               |
| async_tree_cpu_io_mixed | 951 ms                                                 | 752 ms: 1.27x faster                                                |
| docutils                | 3.17 sec                                               | 2.51 sec: 1.26x faster                                              |
| nqueens                 | 100 ms                                                 | 79.3 ms: 1.26x faster                                               |
| coroutines              | 31.8 ms                                                | 25.5 ms: 1.25x faster                                               |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.23x faster                                               |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.48 ms: 1.22x faster                                               |
| sympy_str               | 328 ms                                                 | 270 ms: 1.21x faster                                                |
| xml_etree_generate      | 94.2 ms                                                | 77.7 ms: 1.21x faster                                               |
| sympy_expand            | 545 ms                                                 | 453 ms: 1.20x faster                                                |
| sympy_sum               | 185 ms                                                 | 155 ms: 1.19x faster                                                |
| bench_thread_pool       | 947 us                                                 | 800 us: 1.18x faster                                                |
| dulwich_log             | 75.9 ms                                                | 64.3 ms: 1.18x faster                                               |
| json_loads              | 28.8 us                                                | 24.6 us: 1.17x faster                                               |
| json                    | 5.42 ms                                                | 4.67 ms: 1.16x faster                                               |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                               |
| create_gc_cycles        | 1.67 ms                                                | 1.45 ms: 1.15x faster                                               |
| async_generators        | 425 ms                                                 | 372 ms: 1.14x faster                                                |
| pickle_list             | 4.56 us                                                | 4.09 us: 1.11x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| djangocms               | 35.9 us                                                | 32.8 us: 1.10x faster                                               |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.09x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| sqlite_synth            | 2.93 us                                                | 2.70 us: 1.09x faster                                               |
| scimark_fft             | 424 ms                                                 | 397 ms: 1.07x faster                                                |
| spectral_norm           | 150 ms                                                 | 141 ms: 1.06x faster                                                |
| regex_dna               | 222 ms                                                 | 210 ms: 1.06x faster                                                |
| pathlib                 | 20.0 ms                                                | 19.0 ms: 1.05x faster                                               |
| unpickle                | 14.1 us                                                | 13.6 us: 1.04x faster                                               |
| mdp                     | 2.82 sec                                               | 2.72 sec: 1.04x faster                                              |
| telco                   | 6.54 ms                                                | 6.37 ms: 1.03x faster                                               |
| gc_traversal            | 3.84 ms                                                | 3.82 ms: 1.00x faster                                               |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| unpickle_list           | 4.82 us                                                | 4.90 us: 1.02x slower                                               |
| generators              | 76.8 ms                                                | 81.0 ms: 1.06x slower                                               |
| regex_effbot            | 3.23 ms                                                | 3.50 ms: 1.08x slower                                               |
| python_startup_no_site  | 5.82 ms                                                | 6.47 ms: 1.11x slower                                               |
| pickle_dict             | 27.3 us                                                | 30.5 us: 1.12x slower                                               |
| dask                    | 423 ms                                                 | 526 ms: 1.25x slower                                                |
| coverage                | 72.8 ms                                                | 95.1 ms: 1.31x slower                                               |
| Geometric mean          | (ref)                                                  | 1.28x faster                                                        |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230131-3.12.0a4+-fe65f49/bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x
