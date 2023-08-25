
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: b8b1879
- commit date: 2023-02-05
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.34x faster                                                |
| chameleon      | 9.06 ms                                                | 6.34 ms: 1.43x faster                                               |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                              |
| html5lib       | 85.9 ms                                                | 60.2 ms: 1.43x faster                                               |
| tornado_http   | 127 ms                                                 | 94.3 ms: 1.35x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.9 ms: 1.52x faster                                               |
| nbody          | 142 ms                                                 | 99.5 ms: 1.42x faster                                               |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.29x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                               |
| regex_dna      | 222 ms                                                 | 214 ms: 1.04x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.62 ms: 1.12x slower                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 287 us: 1.59x faster                                                |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.51x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.51 ms: 1.42x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 53.7 ms: 1.40x faster                                               |
| json_loads           | 28.8 us                                                | 23.5 us: 1.23x faster                                               |
| xml_etree_generate   | 94.2 ms                                                | 78.1 ms: 1.21x faster                                               |
| pickle_list          | 4.56 us                                                | 4.00 us: 1.14x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                               |
| pickle               | 10.3 us                                                | 9.98 us: 1.03x faster                                               |
| pickle_dict          | 27.3 us                                                | 30.1 us: 1.11x slower                                               |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                        |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.92 ms: 1.59x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.46 ms: 1.11x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.62 ms: 1.53x faster                                               |
| genshi_text     | 30.3 ms                                                | 21.2 ms: 1.43x faster                                               |
| django_template | 45.9 ms                                                | 32.5 ms: 1.41x faster                                               |
| genshi_xml      | 63.3 ms                                                | 47.7 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                               |
| logging_silent          | 175 ns                                                 | 92.6 ns: 1.89x faster                                               |
| asyncio_tcp             | 925 ms                                                 | 493 ms: 1.88x faster                                                |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                                |
| richards                | 74.9 ms                                                | 42.4 ms: 1.77x faster                                               |
| go                      | 229 ms                                                 | 133 ms: 1.72x faster                                                |
| chaos                   | 106 ms                                                 | 63.2 ms: 1.68x faster                                               |
| pyflate                 | 673 ms                                                 | 401 ms: 1.68x faster                                                |
| raytrace                | 464 ms                                                 | 287 ms: 1.62x faster                                                |
| scimark_monte_carlo     | 108 ms                                                 | 67.7 ms: 1.60x faster                                               |
| hexiom                  | 9.53 ms                                                | 5.98 ms: 1.59x faster                                               |
| pickle_pure_python      | 455 us                                                 | 287 us: 1.59x faster                                                |
| python_startup          | 14.2 ms                                                | 8.92 ms: 1.59x faster                                               |
| spectral_norm           | 150 ms                                                 | 95.0 ms: 1.58x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 75.2 ms: 1.57x faster                                               |
| mako                    | 14.8 ms                                                | 9.62 ms: 1.53x faster                                               |
| float                   | 111 ms                                                 | 72.9 ms: 1.52x faster                                               |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.51x faster                                                |
| deepcopy_memo           | 52.3 us                                                | 34.7 us: 1.51x faster                                               |
| unpack_sequence         | 64.7 ns                                                | 43.2 ns: 1.50x faster                                               |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.49x faster                                                |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                               |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                               |
| genshi_text             | 30.3 ms                                                | 21.2 ms: 1.43x faster                                               |
| chameleon               | 9.06 ms                                                | 6.34 ms: 1.43x faster                                               |
| html5lib                | 85.9 ms                                                | 60.2 ms: 1.43x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.51 ms: 1.42x faster                                               |
| nbody                   | 142 ms                                                 | 99.5 ms: 1.42x faster                                               |
| django_template         | 45.9 ms                                                | 32.5 ms: 1.41x faster                                               |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.41x faster                                              |
| logging_simple          | 8.07 us                                                | 5.76 us: 1.40x faster                                               |
| logging_format          | 8.91 us                                                | 6.38 us: 1.40x faster                                               |
| xml_etree_process       | 74.9 ms                                                | 53.7 ms: 1.40x faster                                               |
| thrift                  | 1.03 ms                                                | 741 us: 1.39x faster                                                |
| pprint_safe_repr        | 955 ms                                                 | 686 ms: 1.39x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.92 ms: 1.39x faster                                               |
| aiohttp                 | 1.38 ms                                                | 999 us: 1.39x faster                                                |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                                |
| scimark_fft             | 424 ms                                                 | 309 ms: 1.37x faster                                                |
| async_tree_none         | 717 ms                                                 | 527 ms: 1.36x faster                                                |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                               |
| tornado_http            | 127 ms                                                 | 94.3 ms: 1.35x faster                                               |
| 2to3                    | 336 ms                                                 | 252 ms: 1.34x faster                                                |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.34x faster                                              |
| pycparser               | 1.50 sec                                               | 1.13 sec: 1.33x faster                                              |
| genshi_xml              | 63.3 ms                                                | 47.7 ms: 1.33x faster                                               |
| fannkuch                | 486 ms                                                 | 367 ms: 1.33x faster                                                |
| deepcopy                | 442 us                                                 | 336 us: 1.31x faster                                                |
| nqueens                 | 100 ms                                                 | 77.0 ms: 1.30x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 659 ms: 1.30x faster                                                |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                                |
| coroutines              | 31.8 ms                                                | 24.9 ms: 1.28x faster                                               |
| sqlglot_optimize        | 65.3 ms                                                | 51.3 ms: 1.27x faster                                               |
| deepcopy_reduce         | 3.82 us                                                | 3.01 us: 1.27x faster                                               |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                              |
| async_tree_cpu_io_mixed | 951 ms                                                 | 762 ms: 1.25x faster                                                |
| json_loads              | 28.8 us                                                | 23.5 us: 1.23x faster                                               |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.23x faster                                               |
| dulwich_log             | 75.9 ms                                                | 62.4 ms: 1.22x faster                                               |
| async_generators        | 425 ms                                                 | 349 ms: 1.22x faster                                                |
| bench_thread_pool       | 947 us                                                 | 780 us: 1.21x faster                                                |
| sympy_str               | 328 ms                                                 | 272 ms: 1.21x faster                                                |
| xml_etree_generate      | 94.2 ms                                                | 78.1 ms: 1.21x faster                                               |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                                |
| json                    | 5.42 ms                                                | 4.55 ms: 1.19x faster                                               |
| sympy_sum               | 185 ms                                                 | 156 ms: 1.18x faster                                                |
| create_gc_cycles        | 1.67 ms                                                | 1.45 ms: 1.15x faster                                               |
| sqlite_synth            | 2.93 us                                                | 2.55 us: 1.15x faster                                               |
| pickle_list             | 4.56 us                                                | 4.00 us: 1.14x faster                                               |
| mdp                     | 2.82 sec                                               | 2.49 sec: 1.13x faster                                              |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                               |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                               |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                               |
| regex_dna               | 222 ms                                                 | 214 ms: 1.04x faster                                                |
| pickle                  | 10.3 us                                                | 9.98 us: 1.03x faster                                               |
| gc_traversal            | 3.84 ms                                                | 3.76 ms: 1.02x faster                                               |
| telco                   | 6.54 ms                                                | 6.42 ms: 1.02x faster                                               |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x slower                                                |
| pickle_dict             | 27.3 us                                                | 30.1 us: 1.11x slower                                               |
| python_startup_no_site  | 5.82 ms                                                | 6.46 ms: 1.11x slower                                               |
| regex_effbot            | 3.23 ms                                                | 3.62 ms: 1.12x slower                                               |
| dask                    | 423 ms                                                 | 497 ms: 1.18x slower                                                |
| coverage                | 72.8 ms                                                | 98.9 ms: 1.36x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (3): bench_mp_pool, generators, unpickle_list
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230205-3.12.0a4+-b8b1879/bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x
