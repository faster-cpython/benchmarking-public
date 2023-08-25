
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 5609e30
- commit date: 2023-02-03
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                |
| chameleon      | 9.06 ms                                                | 6.21 ms: 1.46x faster                                               |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                              |
| html5lib       | 85.9 ms                                                | 59.9 ms: 1.43x faster                                               |
| tornado_http   | 127 ms                                                 | 93.6 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.37x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 111 ms                                                 | 73.1 ms: 1.51x faster                                               |
| nbody          | 142 ms                                                 | 96.7 ms: 1.46x faster                                               |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                               |
| regex_dna      | 222 ms                                                 | 217 ms: 1.02x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.77 ms: 1.17x slower                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 284 us: 1.61x faster                                                |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.52x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.41 ms: 1.44x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 53.4 ms: 1.40x faster                                               |
| json_loads           | 28.8 us                                                | 23.4 us: 1.23x faster                                               |
| xml_etree_generate   | 94.2 ms                                                | 77.5 ms: 1.21x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 145 ms: 1.12x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.10x faster                                                |
| pickle_list          | 4.56 us                                                | 4.22 us: 1.08x faster                                               |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                               |
| pickle               | 10.3 us                                                | 10.1 us: 1.01x faster                                               |
| unpickle_list        | 4.82 us                                                | 5.15 us: 1.07x slower                                               |
| pickle_dict          | 27.3 us                                                | 31.8 us: 1.17x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.97 ms: 1.58x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.50 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.47 ms: 1.56x faster                                               |
| django_template | 45.9 ms                                                | 32.1 ms: 1.43x faster                                               |
| genshi_text     | 30.3 ms                                                | 21.3 ms: 1.42x faster                                               |
| genshi_xml      | 63.3 ms                                                | 47.5 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.18 ms: 2.34x faster                                               |
| logging_silent          | 175 ns                                                 | 92.8 ns: 1.89x faster                                               |
| asyncio_tcp             | 925 ms                                                 | 492 ms: 1.88x faster                                                |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                |
| richards                | 74.9 ms                                                | 41.9 ms: 1.79x faster                                               |
| go                      | 229 ms                                                 | 132 ms: 1.73x faster                                                |
| chaos                   | 106 ms                                                 | 63.7 ms: 1.67x faster                                               |
| pyflate                 | 673 ms                                                 | 410 ms: 1.64x faster                                                |
| raytrace                | 464 ms                                                 | 284 ms: 1.63x faster                                                |
| scimark_monte_carlo     | 108 ms                                                 | 67.0 ms: 1.62x faster                                               |
| hexiom                  | 9.53 ms                                                | 5.93 ms: 1.61x faster                                               |
| pickle_pure_python      | 455 us                                                 | 284 us: 1.61x faster                                                |
| python_startup          | 14.2 ms                                                | 8.97 ms: 1.58x faster                                               |
| mako                    | 14.8 ms                                                | 9.47 ms: 1.56x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 76.1 ms: 1.56x faster                                               |
| spectral_norm           | 150 ms                                                 | 96.6 ms: 1.55x faster                                               |
| deepcopy_memo           | 52.3 us                                                | 33.9 us: 1.54x faster                                               |
| unpack_sequence         | 64.7 ns                                                | 42.5 ns: 1.52x faster                                               |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.52x faster                                                |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                |
| float                   | 111 ms                                                 | 73.1 ms: 1.51x faster                                               |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.47x faster                                               |
| nbody                   | 142 ms                                                 | 96.7 ms: 1.46x faster                                               |
| chameleon               | 9.06 ms                                                | 6.21 ms: 1.46x faster                                               |
| sqlglot_transpile       | 2.45 ms                                                | 1.69 ms: 1.45x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.41 ms: 1.44x faster                                               |
| html5lib                | 85.9 ms                                                | 59.9 ms: 1.43x faster                                               |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.43x faster                                              |
| django_template         | 45.9 ms                                                | 32.1 ms: 1.43x faster                                               |
| logging_simple          | 8.07 us                                                | 5.67 us: 1.42x faster                                               |
| genshi_text             | 30.3 ms                                                | 21.3 ms: 1.42x faster                                               |
| logging_format          | 8.91 us                                                | 6.26 us: 1.42x faster                                               |
| pprint_safe_repr        | 955 ms                                                 | 676 ms: 1.41x faster                                                |
| xml_etree_process       | 74.9 ms                                                | 53.4 ms: 1.40x faster                                               |
| thrift                  | 1.03 ms                                                | 740 us: 1.40x faster                                                |
| scimark_fft             | 424 ms                                                 | 304 ms: 1.39x faster                                                |
| aiohttp                 | 1.38 ms                                                | 995 us: 1.39x faster                                                |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                                |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                               |
| tornado_http            | 127 ms                                                 | 93.6 ms: 1.36x faster                                               |
| deepcopy                | 442 us                                                 | 326 us: 1.35x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.04 ms: 1.35x faster                                               |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                              |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                |
| genshi_xml              | 63.3 ms                                                | 47.5 ms: 1.33x faster                                               |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.32x faster                                              |
| fannkuch                | 486 ms                                                 | 368 ms: 1.32x faster                                                |
| coroutines              | 31.8 ms                                                | 24.1 ms: 1.32x faster                                               |
| deepcopy_reduce         | 3.82 us                                                | 2.92 us: 1.31x faster                                               |
| nqueens                 | 100 ms                                                 | 77.2 ms: 1.30x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 660 ms: 1.29x faster                                                |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 51.1 ms: 1.28x faster                                               |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                              |
| async_tree_cpu_io_mixed | 951 ms                                                 | 754 ms: 1.26x faster                                                |
| json_loads              | 28.8 us                                                | 23.4 us: 1.23x faster                                               |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.23x faster                                               |
| bench_thread_pool       | 947 us                                                 | 777 us: 1.22x faster                                                |
| dulwich_log             | 75.9 ms                                                | 62.4 ms: 1.22x faster                                               |
| sympy_str               | 328 ms                                                 | 270 ms: 1.22x faster                                                |
| xml_etree_generate      | 94.2 ms                                                | 77.5 ms: 1.21x faster                                               |
| async_generators        | 425 ms                                                 | 353 ms: 1.20x faster                                                |
| sympy_expand            | 545 ms                                                 | 455 ms: 1.20x faster                                                |
| sympy_sum               | 185 ms                                                 | 155 ms: 1.19x faster                                                |
| json                    | 5.42 ms                                                | 4.59 ms: 1.18x faster                                               |
| sqlite_synth            | 2.93 us                                                | 2.54 us: 1.16x faster                                               |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                               |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 145 ms: 1.12x faster                                                |
| mdp                     | 2.82 sec                                               | 2.51 sec: 1.12x faster                                              |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                               |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.10x faster                                                |
| pickle_list             | 4.56 us                                                | 4.22 us: 1.08x faster                                               |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                               |
| regex_dna               | 222 ms                                                 | 217 ms: 1.02x faster                                                |
| telco                   | 6.54 ms                                                | 6.42 ms: 1.02x faster                                               |
| pickle                  | 10.3 us                                                | 10.1 us: 1.01x faster                                               |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x slower                                                |
| generators              | 76.8 ms                                                | 77.7 ms: 1.01x slower                                               |
| gc_traversal            | 3.84 ms                                                | 3.93 ms: 1.02x slower                                               |
| unpickle_list           | 4.82 us                                                | 5.15 us: 1.07x slower                                               |
| python_startup_no_site  | 5.82 ms                                                | 6.50 ms: 1.12x slower                                               |
| pickle_dict             | 27.3 us                                                | 31.8 us: 1.17x slower                                               |
| regex_effbot            | 3.23 ms                                                | 3.77 ms: 1.17x slower                                               |
| dask                    | 423 ms                                                 | 494 ms: 1.17x slower                                                |
| coverage                | 72.8 ms                                                | 94.8 ms: 1.30x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230203-3.12.0a4+-5609e30/bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x
