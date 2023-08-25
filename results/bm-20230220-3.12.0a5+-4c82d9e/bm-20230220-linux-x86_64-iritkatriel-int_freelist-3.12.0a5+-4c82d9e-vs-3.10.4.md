
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 4c82d9e
- commit date: 2023-02-20
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                |
| chameleon      | 9.06 ms                                                | 6.25 ms: 1.45x faster                                               |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.25x faster                                              |
| html5lib       | 85.9 ms                                                | 61.7 ms: 1.39x faster                                               |
| tornado_http   | 127 ms                                                 | 93.8 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.2 ms: 1.53x faster                                               |
| nbody          | 142 ms                                                 | 94.6 ms: 1.50x faster                                               |
| pidigits       | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                               |
| regex_dna      | 222 ms                                                 | 199 ms: 1.12x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.46 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.14x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 290 us: 1.57x faster                                                |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.53x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.44 ms: 1.43x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 57.2 ms: 1.31x faster                                               |
| json_loads           | 28.8 us                                                | 23.8 us: 1.21x faster                                               |
| xml_etree_generate   | 94.2 ms                                                | 82.2 ms: 1.15x faster                                               |
| pickle_list          | 4.56 us                                                | 4.08 us: 1.12x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.10x faster                                                |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                               |
| pickle               | 10.3 us                                                | 10.0 us: 1.03x faster                                               |
| pickle_dict          | 27.3 us                                                | 29.7 us: 1.09x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.95 ms: 1.58x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.50 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.51 ms: 1.55x faster                                               |
| genshi_text     | 30.3 ms                                                | 20.7 ms: 1.47x faster                                               |
| django_template | 45.9 ms                                                | 32.9 ms: 1.39x faster                                               |
| genshi_xml      | 63.3 ms                                                | 47.6 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.20 ms: 2.32x faster                                               |
| logging_silent          | 175 ns                                                 | 91.6 ns: 1.91x faster                                               |
| asyncio_tcp             | 925 ms                                                 | 496 ms: 1.86x faster                                                |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                |
| richards                | 74.9 ms                                                | 42.0 ms: 1.78x faster                                               |
| go                      | 229 ms                                                 | 136 ms: 1.69x faster                                                |
| pyflate                 | 673 ms                                                 | 398 ms: 1.69x faster                                                |
| scimark_monte_carlo     | 108 ms                                                 | 65.3 ms: 1.66x faster                                               |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                                |
| chaos                   | 106 ms                                                 | 65.0 ms: 1.64x faster                                               |
| spectral_norm           | 150 ms                                                 | 93.8 ms: 1.60x faster                                               |
| hexiom                  | 9.53 ms                                                | 5.98 ms: 1.59x faster                                               |
| python_startup          | 14.2 ms                                                | 8.95 ms: 1.58x faster                                               |
| pickle_pure_python      | 455 us                                                 | 290 us: 1.57x faster                                                |
| mako                    | 14.8 ms                                                | 9.51 ms: 1.55x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 76.4 ms: 1.55x faster                                               |
| float                   | 111 ms                                                 | 72.2 ms: 1.53x faster                                               |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.53x faster                                                |
| unpack_sequence         | 64.7 ns                                                | 42.5 ns: 1.52x faster                                               |
| deepcopy_memo           | 52.3 us                                                | 34.7 us: 1.51x faster                                               |
| nbody                   | 142 ms                                                 | 94.6 ms: 1.50x faster                                               |
| scimark_lu              | 163 ms                                                 | 111 ms: 1.47x faster                                                |
| genshi_text             | 30.3 ms                                                | 20.7 ms: 1.47x faster                                               |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                               |
| chameleon               | 9.06 ms                                                | 6.25 ms: 1.45x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.44 ms: 1.43x faster                                               |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                               |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                              |
| logging_format          | 8.91 us                                                | 6.27 us: 1.42x faster                                               |
| logging_simple          | 8.07 us                                                | 5.75 us: 1.40x faster                                               |
| scimark_fft             | 424 ms                                                 | 303 ms: 1.40x faster                                                |
| pprint_safe_repr        | 955 ms                                                 | 685 ms: 1.39x faster                                                |
| django_template         | 45.9 ms                                                | 32.9 ms: 1.39x faster                                               |
| html5lib                | 85.9 ms                                                | 61.7 ms: 1.39x faster                                               |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                |
| aiohttp                 | 1.38 ms                                                | 997 us: 1.39x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.96 ms: 1.38x faster                                               |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.37x faster                                               |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.36x faster                                              |
| thrift                  | 1.03 ms                                                | 758 us: 1.36x faster                                                |
| tornado_http            | 127 ms                                                 | 93.8 ms: 1.36x faster                                               |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.35x faster                                              |
| async_tree_none         | 717 ms                                                 | 532 ms: 1.35x faster                                                |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                |
| genshi_xml              | 63.3 ms                                                | 47.6 ms: 1.33x faster                                               |
| deepcopy                | 442 us                                                 | 332 us: 1.33x faster                                                |
| fannkuch                | 486 ms                                                 | 370 ms: 1.31x faster                                                |
| xml_etree_process       | 74.9 ms                                                | 57.2 ms: 1.31x faster                                               |
| deepcopy_reduce         | 3.82 us                                                | 2.93 us: 1.31x faster                                               |
| mypy2                   | 428 ms                                                 | 331 ms: 1.30x faster                                                |
| async_tree_memoization  | 854 ms                                                 | 666 ms: 1.28x faster                                                |
| nqueens                 | 100 ms                                                 | 78.2 ms: 1.28x faster                                               |
| sqlglot_normalize       | 135 ms                                                 | 107 ms: 1.27x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 51.7 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed | 951 ms                                                 | 759 ms: 1.25x faster                                                |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.25x faster                                              |
| coroutines              | 31.8 ms                                                | 25.7 ms: 1.24x faster                                               |
| dulwich_log             | 75.9 ms                                                | 62.0 ms: 1.22x faster                                               |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.22x faster                                               |
| sympy_str               | 328 ms                                                 | 270 ms: 1.22x faster                                                |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                |
| bench_thread_pool       | 947 us                                                 | 783 us: 1.21x faster                                                |
| json_loads              | 28.8 us                                                | 23.8 us: 1.21x faster                                               |
| sympy_expand            | 545 ms                                                 | 458 ms: 1.19x faster                                                |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.9 ms: 1.19x faster                                               |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                               |
| sympy_sum               | 185 ms                                                 | 158 ms: 1.17x faster                                                |
| json                    | 5.42 ms                                                | 4.63 ms: 1.17x faster                                               |
| sqlite_synth            | 2.93 us                                                | 2.56 us: 1.15x faster                                               |
| xml_etree_generate      | 94.2 ms                                                | 82.2 ms: 1.15x faster                                               |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                               |
| mdp                     | 2.82 sec                                               | 2.52 sec: 1.12x faster                                              |
| djangocms               | 35.9 us                                                | 32.2 us: 1.12x faster                                               |
| regex_dna               | 222 ms                                                 | 199 ms: 1.12x faster                                                |
| pickle_list             | 4.56 us                                                | 4.08 us: 1.12x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.10x faster                                                |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.09x faster                                                |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                               |
| pickle                  | 10.3 us                                                | 10.0 us: 1.03x faster                                               |
| telco                   | 6.54 ms                                                | 6.38 ms: 1.03x faster                                               |
| async_generators        | 425 ms                                                 | 423 ms: 1.01x faster                                                |
| pidigits                | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| generators              | 76.8 ms                                                | 77.3 ms: 1.01x slower                                               |
| regex_effbot            | 3.23 ms                                                | 3.46 ms: 1.07x slower                                               |
| pickle_dict             | 27.3 us                                                | 29.7 us: 1.09x slower                                               |
| gc_traversal            | 3.84 ms                                                | 4.29 ms: 1.12x slower                                               |
| python_startup_no_site  | 5.82 ms                                                | 6.50 ms: 1.12x slower                                               |
| coverage                | 72.8 ms                                                | 97.9 ms: 1.35x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (2): unpickle_list, bench_mp_pool
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x
