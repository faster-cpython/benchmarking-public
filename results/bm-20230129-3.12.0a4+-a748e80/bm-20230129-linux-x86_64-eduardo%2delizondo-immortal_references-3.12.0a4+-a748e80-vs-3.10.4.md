
# Results vs. 3.10.4

- fork: eduardo-elizondo
- ref: immortal_references
- machine: linux-x86_64
- commit hash: a748e80
- commit date: 2023-01-29
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 269 ms: 1.25x faster                                                              |
| chameleon      | 9.06 ms                                                | 6.91 ms: 1.31x faster                                                             |
| docutils       | 3.17 sec                                               | 2.70 sec: 1.18x faster                                                            |
| html5lib       | 85.9 ms                                                | 64.7 ms: 1.33x faster                                                             |
| tornado_http   | 127 ms                                                 | 106 ms: 1.20x faster                                                              |
| Geometric mean | (ref)                                                  | 1.25x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 98.0 ms: 1.44x faster                                                             |
| float          | 111 ms                                                 | 79.1 ms: 1.40x faster                                                             |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 142 ms: 1.24x faster                                                              |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                             |
| regex_dna      | 222 ms                                                 | 206 ms: 1.08x faster                                                              |
| regex_effbot   | 3.23 ms                                                | 3.68 ms: 1.14x slower                                                             |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 311 us: 1.47x faster                                                              |
| unpickle_pure_python | 300 us                                                 | 214 us: 1.40x faster                                                              |
| json_dumps           | 13.5 ms                                                | 9.76 ms: 1.39x faster                                                             |
| xml_etree_process    | 74.9 ms                                                | 57.8 ms: 1.30x faster                                                             |
| xml_etree_generate   | 94.2 ms                                                | 81.6 ms: 1.15x faster                                                             |
| json_loads           | 28.8 us                                                | 26.6 us: 1.08x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                              |
| unpickle             | 14.1 us                                                | 13.4 us: 1.06x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 107 ms: 1.05x faster                                                              |
| pickle               | 10.3 us                                                | 10.4 us: 1.02x slower                                                             |
| pickle_dict          | 27.3 us                                                | 30.6 us: 1.12x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                      |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.13 ms: 1.55x faster                                                             |
| python_startup_no_site | 5.82 ms                                                | 6.56 ms: 1.13x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.2 ms: 1.44x faster                                                             |
| genshi_text     | 30.3 ms                                                | 22.5 ms: 1.35x faster                                                             |
| django_template | 45.9 ms                                                | 34.8 ms: 1.32x faster                                                             |
| genshi_xml      | 63.3 ms                                                | 50.5 ms: 1.25x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.51 ms: 2.11x faster                                                             |
| logging_silent          | 175 ns                                                 | 94.6 ns: 1.85x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 516 ms: 1.79x faster                                                              |
| richards                | 74.9 ms                                                | 43.2 ms: 1.73x faster                                                             |
| go                      | 229 ms                                                 | 133 ms: 1.72x faster                                                              |
| scimark_sor             | 197 ms                                                 | 117 ms: 1.69x faster                                                              |
| pyflate                 | 673 ms                                                 | 423 ms: 1.59x faster                                                              |
| chaos                   | 106 ms                                                 | 67.1 ms: 1.58x faster                                                             |
| hexiom                  | 9.53 ms                                                | 6.12 ms: 1.56x faster                                                             |
| python_startup          | 14.2 ms                                                | 9.13 ms: 1.55x faster                                                             |
| crypto_pyaes            | 118 ms                                                 | 76.9 ms: 1.54x faster                                                             |
| scimark_monte_carlo     | 108 ms                                                 | 70.7 ms: 1.53x faster                                                             |
| raytrace                | 464 ms                                                 | 307 ms: 1.51x faster                                                              |
| pickle_pure_python      | 455 us                                                 | 311 us: 1.47x faster                                                              |
| scimark_lu              | 163 ms                                                 | 113 ms: 1.45x faster                                                              |
| nbody                   | 142 ms                                                 | 98.0 ms: 1.44x faster                                                             |
| mako                    | 14.8 ms                                                | 10.2 ms: 1.44x faster                                                             |
| spectral_norm           | 150 ms                                                 | 105 ms: 1.43x faster                                                              |
| unpickle_pure_python    | 300 us                                                 | 214 us: 1.40x faster                                                              |
| float                   | 111 ms                                                 | 79.1 ms: 1.40x faster                                                             |
| json_dumps              | 13.5 ms                                                | 9.76 ms: 1.39x faster                                                             |
| deepcopy_memo           | 52.3 us                                                | 38.1 us: 1.38x faster                                                             |
| unpack_sequence         | 64.7 ns                                                | 47.3 ns: 1.37x faster                                                             |
| thrift                  | 1.03 ms                                                | 761 us: 1.36x faster                                                              |
| genshi_text             | 30.3 ms                                                | 22.5 ms: 1.35x faster                                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.54 ms: 1.34x faster                                                             |
| async_tree_none         | 717 ms                                                 | 540 ms: 1.33x faster                                                              |
| html5lib                | 85.9 ms                                                | 64.7 ms: 1.33x faster                                                             |
| pprint_pformat          | 1.99 sec                                               | 1.50 sec: 1.32x faster                                                            |
| django_template         | 45.9 ms                                                | 34.8 ms: 1.32x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.35 sec: 1.32x faster                                                            |
| comprehensions          | 26.8 us                                                | 20.4 us: 1.32x faster                                                             |
| fannkuch                | 486 ms                                                 | 370 ms: 1.31x faster                                                              |
| chameleon               | 9.06 ms                                                | 6.91 ms: 1.31x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.87 ms: 1.31x faster                                                             |
| pprint_safe_repr        | 955 ms                                                 | 736 ms: 1.30x faster                                                              |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.30x faster                                                            |
| xml_etree_process       | 74.9 ms                                                | 57.8 ms: 1.30x faster                                                             |
| nqueens                 | 100 ms                                                 | 78.1 ms: 1.28x faster                                                             |
| logging_format          | 8.91 us                                                | 7.05 us: 1.26x faster                                                             |
| logging_simple          | 8.07 us                                                | 6.40 us: 1.26x faster                                                             |
| genshi_xml              | 63.3 ms                                                | 50.5 ms: 1.25x faster                                                             |
| 2to3                    | 336 ms                                                 | 269 ms: 1.25x faster                                                              |
| async_tree_memoization  | 854 ms                                                 | 687 ms: 1.24x faster                                                              |
| regex_compile           | 177 ms                                                 | 142 ms: 1.24x faster                                                              |
| async_tree_cpu_io_mixed | 951 ms                                                 | 770 ms: 1.24x faster                                                              |
| coroutines              | 31.8 ms                                                | 25.9 ms: 1.23x faster                                                             |
| deepcopy_reduce         | 3.82 us                                                | 3.12 us: 1.22x faster                                                             |
| deepcopy                | 442 us                                                 | 363 us: 1.22x faster                                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.49 ms: 1.22x faster                                                             |
| tornado_http            | 127 ms                                                 | 106 ms: 1.20x faster                                                              |
| mypy2                   | 428 ms                                                 | 360 ms: 1.19x faster                                                              |
| scimark_fft             | 424 ms                                                 | 357 ms: 1.19x faster                                                              |
| sqlglot_optimize        | 65.3 ms                                                | 55.4 ms: 1.18x faster                                                             |
| sqlglot_normalize       | 135 ms                                                 | 115 ms: 1.18x faster                                                              |
| docutils                | 3.17 sec                                               | 2.70 sec: 1.18x faster                                                            |
| async_generators        | 425 ms                                                 | 362 ms: 1.17x faster                                                              |
| xml_etree_generate      | 94.2 ms                                                | 81.6 ms: 1.15x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                             |
| sympy_integrate         | 24.3 ms                                                | 21.3 ms: 1.14x faster                                                             |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                             |
| bench_thread_pool       | 947 us                                                 | 838 us: 1.13x faster                                                              |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                             |
| mdp                     | 2.82 sec                                               | 2.54 sec: 1.11x faster                                                            |
| dulwich_log             | 75.9 ms                                                | 68.4 ms: 1.11x faster                                                             |
| dask                    | 423 ms                                                 | 385 ms: 1.10x faster                                                              |
| sympy_expand            | 545 ms                                                 | 499 ms: 1.09x faster                                                              |
| sympy_str               | 328 ms                                                 | 302 ms: 1.09x faster                                                              |
| djangocms               | 35.9 us                                                | 33.1 us: 1.08x faster                                                             |
| json_loads              | 28.8 us                                                | 26.6 us: 1.08x faster                                                             |
| pathlib                 | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                             |
| regex_dna               | 222 ms                                                 | 206 ms: 1.08x faster                                                              |
| sympy_sum               | 185 ms                                                 | 172 ms: 1.07x faster                                                              |
| xml_etree_parse         | 163 ms                                                 | 154 ms: 1.06x faster                                                              |
| unpickle                | 14.1 us                                                | 13.4 us: 1.06x faster                                                             |
| json                    | 5.42 ms                                                | 5.14 ms: 1.05x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                 | 107 ms: 1.05x faster                                                              |
| meteor_contest          | 115 ms                                                 | 111 ms: 1.04x faster                                                              |
| pickle                  | 10.3 us                                                | 10.4 us: 1.02x slower                                                             |
| telco                   | 6.54 ms                                                | 6.67 ms: 1.02x slower                                                             |
| gc_traversal            | 3.84 ms                                                | 4.29 ms: 1.12x slower                                                             |
| pickle_dict             | 27.3 us                                                | 30.6 us: 1.12x slower                                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.56 ms: 1.13x slower                                                             |
| regex_effbot            | 3.23 ms                                                | 3.68 ms: 1.14x slower                                                             |
| coverage                | 72.8 ms                                                | 102 ms: 1.40x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.24x faster                                                                      |

Benchmark hidden because not significant (5): pidigits, generators, bench_mp_pool, unpickle_list, pickle_list
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x
