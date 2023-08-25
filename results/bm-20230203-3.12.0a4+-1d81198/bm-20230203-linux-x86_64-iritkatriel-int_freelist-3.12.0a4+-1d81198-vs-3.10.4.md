
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 1d81198
- commit date: 2023-02-03
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                                |
| chameleon      | 9.06 ms                                                | 6.28 ms: 1.44x faster                                               |
| docutils       | 3.17 sec                                               | 2.51 sec: 1.27x faster                                              |
| html5lib       | 85.9 ms                                                | 60.0 ms: 1.43x faster                                               |
| tornado_http   | 127 ms                                                 | 93.7 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.37x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 111 ms                                                 | 73.2 ms: 1.51x faster                                               |
| nbody          | 142 ms                                                 | 95.8 ms: 1.48x faster                                               |
| pidigits       | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                               |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.51 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.11x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.60x faster                                                |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.52x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.43 ms: 1.44x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 53.4 ms: 1.40x faster                                               |
| xml_etree_generate   | 94.2 ms                                                | 77.4 ms: 1.22x faster                                               |
| json_loads           | 28.8 us                                                | 23.9 us: 1.20x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.12x faster                                                |
| unpickle             | 14.1 us                                                | 12.9 us: 1.09x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| pickle_list          | 4.56 us                                                | 4.23 us: 1.08x faster                                               |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                               |
| unpickle_list        | 4.82 us                                                | 5.05 us: 1.05x slower                                               |
| pickle_dict          | 27.3 us                                                | 31.3 us: 1.15x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.93 ms: 1.58x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.47 ms: 1.11x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.60 ms: 1.54x faster                                               |
| genshi_text     | 30.3 ms                                                | 20.3 ms: 1.49x faster                                               |
| django_template | 45.9 ms                                                | 32.3 ms: 1.42x faster                                               |
| genshi_xml      | 63.3 ms                                                | 47.3 ms: 1.34x faster                                               |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.22 ms: 2.30x faster                                               |
| logging_silent          | 175 ns                                                 | 91.9 ns: 1.90x faster                                               |
| asyncio_tcp             | 925 ms                                                 | 496 ms: 1.87x faster                                                |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                |
| richards                | 74.9 ms                                                | 42.0 ms: 1.78x faster                                               |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                                |
| chaos                   | 106 ms                                                 | 63.7 ms: 1.67x faster                                               |
| scimark_monte_carlo     | 108 ms                                                 | 66.8 ms: 1.62x faster                                               |
| pyflate                 | 673 ms                                                 | 416 ms: 1.62x faster                                                |
| raytrace                | 464 ms                                                 | 289 ms: 1.60x faster                                                |
| hexiom                  | 9.53 ms                                                | 5.96 ms: 1.60x faster                                               |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.60x faster                                                |
| python_startup          | 14.2 ms                                                | 8.93 ms: 1.58x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 76.0 ms: 1.56x faster                                               |
| mako                    | 14.8 ms                                                | 9.60 ms: 1.54x faster                                               |
| deepcopy_memo           | 52.3 us                                                | 34.2 us: 1.53x faster                                               |
| spectral_norm           | 150 ms                                                 | 98.2 ms: 1.53x faster                                               |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.52x faster                                                |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.52x faster                                                |
| float                   | 111 ms                                                 | 73.2 ms: 1.51x faster                                               |
| genshi_text             | 30.3 ms                                                | 20.3 ms: 1.49x faster                                               |
| nbody                   | 142 ms                                                 | 95.8 ms: 1.48x faster                                               |
| unpack_sequence         | 64.7 ns                                                | 43.9 ns: 1.47x faster                                               |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.47x faster                                               |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                              |
| chameleon               | 9.06 ms                                                | 6.28 ms: 1.44x faster                                               |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.43 ms: 1.44x faster                                               |
| html5lib                | 85.9 ms                                                | 60.0 ms: 1.43x faster                                               |
| pprint_safe_repr        | 955 ms                                                 | 671 ms: 1.42x faster                                                |
| django_template         | 45.9 ms                                                | 32.3 ms: 1.42x faster                                               |
| logging_format          | 8.91 us                                                | 6.32 us: 1.41x faster                                               |
| logging_simple          | 8.07 us                                                | 5.73 us: 1.41x faster                                               |
| xml_etree_process       | 74.9 ms                                                | 53.4 ms: 1.40x faster                                               |
| aiohttp                 | 1.38 ms                                                | 993 us: 1.39x faster                                                |
| thrift                  | 1.03 ms                                                | 747 us: 1.38x faster                                                |
| gunicorn                | 1.46 ms                                                | 1.06 ms: 1.38x faster                                               |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                |
| scimark_fft             | 424 ms                                                 | 308 ms: 1.37x faster                                                |
| async_tree_none         | 717 ms                                                 | 522 ms: 1.37x faster                                                |
| tornado_http            | 127 ms                                                 | 93.7 ms: 1.36x faster                                               |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.02 ms: 1.36x faster                                               |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.34x faster                                              |
| genshi_xml              | 63.3 ms                                                | 47.3 ms: 1.34x faster                                               |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                                |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                                |
| pycparser               | 1.50 sec                                               | 1.13 sec: 1.32x faster                                              |
| async_tree_memoization  | 854 ms                                                 | 647 ms: 1.32x faster                                                |
| nqueens                 | 100 ms                                                 | 75.7 ms: 1.32x faster                                               |
| fannkuch                | 486 ms                                                 | 369 ms: 1.32x faster                                                |
| coroutines              | 31.8 ms                                                | 24.3 ms: 1.31x faster                                               |
| deepcopy_reduce         | 3.82 us                                                | 2.96 us: 1.29x faster                                               |
| sqlglot_optimize        | 65.3 ms                                                | 51.4 ms: 1.27x faster                                               |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                                |
| docutils                | 3.17 sec                                               | 2.51 sec: 1.27x faster                                              |
| async_tree_cpu_io_mixed | 951 ms                                                 | 753 ms: 1.26x faster                                                |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.22x faster                                               |
| dulwich_log             | 75.9 ms                                                | 62.3 ms: 1.22x faster                                               |
| xml_etree_generate      | 94.2 ms                                                | 77.4 ms: 1.22x faster                                               |
| sympy_str               | 328 ms                                                 | 271 ms: 1.21x faster                                                |
| bench_thread_pool       | 947 us                                                 | 782 us: 1.21x faster                                                |
| json_loads              | 28.8 us                                                | 23.9 us: 1.20x faster                                               |
| async_generators        | 425 ms                                                 | 354 ms: 1.20x faster                                                |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                                |
| sympy_sum               | 185 ms                                                 | 155 ms: 1.19x faster                                                |
| sqlite_synth            | 2.93 us                                                | 2.54 us: 1.15x faster                                               |
| create_gc_cycles        | 1.67 ms                                                | 1.45 ms: 1.15x faster                                               |
| json                    | 5.42 ms                                                | 4.76 ms: 1.14x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.13x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.12x faster                                                |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                               |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                               |
| mdp                     | 2.82 sec                                               | 2.57 sec: 1.10x faster                                              |
| unpickle                | 14.1 us                                                | 12.9 us: 1.09x faster                                               |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| pickle_list             | 4.56 us                                                | 4.23 us: 1.08x faster                                               |
| regex_dna               | 222 ms                                                 | 209 ms: 1.06x faster                                                |
| telco                   | 6.54 ms                                                | 6.37 ms: 1.03x faster                                               |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                               |
| pidigits                | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| generators              | 76.8 ms                                                | 77.1 ms: 1.00x slower                                               |
| unpickle_list           | 4.82 us                                                | 5.05 us: 1.05x slower                                               |
| gc_traversal            | 3.84 ms                                                | 4.05 ms: 1.05x slower                                               |
| regex_effbot            | 3.23 ms                                                | 3.51 ms: 1.09x slower                                               |
| python_startup_no_site  | 5.82 ms                                                | 6.47 ms: 1.11x slower                                               |
| pickle_dict             | 27.3 us                                                | 31.3 us: 1.15x slower                                               |
| dask                    | 423 ms                                                 | 494 ms: 1.17x slower                                                |
| coverage                | 72.8 ms                                                | 96.4 ms: 1.32x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230203-3.12.0a4+-1d81198/bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-1d81198.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
