
# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_small_ints
- machine: linux-x86_64
- commit hash: 5403a06
- commit date: 2023-02-25
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 249 ms: 1.35x faster                                                      |
| chameleon      | 9.06 ms                                                | 6.46 ms: 1.40x faster                                                     |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                    |
| html5lib       | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                     |
| tornado_http   | 127 ms                                                 | 94.6 ms: 1.35x faster                                                     |
| Geometric mean | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 74.9 ms: 1.48x faster                                                     |
| nbody          | 142 ms                                                 | 96.1 ms: 1.47x faster                                                     |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                      |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.15x faster                                                     |
| regex_dna      | 222 ms                                                 | 206 ms: 1.08x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.69 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.53x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.28 ms: 1.46x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 55.0 ms: 1.36x faster                                                     |
| json_loads           | 28.8 us                                                | 23.5 us: 1.23x faster                                                     |
| xml_etree_generate   | 94.2 ms                                                | 80.6 ms: 1.17x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 99.2 ms: 1.12x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                      |
| unpickle             | 14.1 us                                                | 13.2 us: 1.08x faster                                                     |
| pickle_list          | 4.56 us                                                | 4.25 us: 1.07x faster                                                     |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                                     |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                                     |
| pickle_dict          | 27.3 us                                                | 31.5 us: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.07 ms: 1.56x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.57 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                     |
| genshi_text     | 30.3 ms                                                | 20.9 ms: 1.45x faster                                                     |
| django_template | 45.9 ms                                                | 33.3 ms: 1.38x faster                                                     |
| genshi_xml      | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.8 ms: 2.49x faster                                                     |
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.33x faster                                                     |
| logging_silent          | 175 ns                                                 | 93.4 ns: 1.87x faster                                                     |
| asyncio_tcp             | 925 ms                                                 | 500 ms: 1.85x faster                                                      |
| richards                | 74.9 ms                                                | 41.4 ms: 1.81x faster                                                     |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.76x faster                                                      |
| go                      | 229 ms                                                 | 139 ms: 1.64x faster                                                      |
| raytrace                | 464 ms                                                 | 282 ms: 1.64x faster                                                      |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                                      |
| scimark_monte_carlo     | 108 ms                                                 | 68.7 ms: 1.58x faster                                                     |
| python_startup          | 14.2 ms                                                | 9.07 ms: 1.56x faster                                                     |
| pyflate                 | 673 ms                                                 | 435 ms: 1.55x faster                                                      |
| deepcopy_memo           | 52.3 us                                                | 33.9 us: 1.54x faster                                                     |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.53x faster                                                      |
| hexiom                  | 9.53 ms                                                | 6.27 ms: 1.52x faster                                                     |
| crypto_pyaes            | 118 ms                                                 | 78.4 ms: 1.51x faster                                                     |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                      |
| chaos                   | 106 ms                                                 | 70.8 ms: 1.50x faster                                                     |
| float                   | 111 ms                                                 | 74.9 ms: 1.48x faster                                                     |
| nbody                   | 142 ms                                                 | 96.1 ms: 1.47x faster                                                     |
| mako                    | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                     |
| json_dumps              | 13.5 ms                                                | 9.28 ms: 1.46x faster                                                     |
| genshi_text             | 30.3 ms                                                | 20.9 ms: 1.45x faster                                                     |
| unpack_sequence         | 64.7 ns                                                | 44.7 ns: 1.45x faster                                                     |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.43x faster                                                     |
| spectral_norm           | 150 ms                                                 | 105 ms: 1.43x faster                                                      |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                                    |
| sqlglot_transpile       | 2.45 ms                                                | 1.73 ms: 1.42x faster                                                     |
| chameleon               | 9.06 ms                                                | 6.46 ms: 1.40x faster                                                     |
| pprint_safe_repr        | 955 ms                                                 | 681 ms: 1.40x faster                                                      |
| html5lib                | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                     |
| logging_format          | 8.91 us                                                | 6.37 us: 1.40x faster                                                     |
| logging_simple          | 8.07 us                                                | 5.81 us: 1.39x faster                                                     |
| django_template         | 45.9 ms                                                | 33.3 ms: 1.38x faster                                                     |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.38x faster                                                    |
| async_tree_none         | 717 ms                                                 | 523 ms: 1.37x faster                                                      |
| xml_etree_process       | 74.9 ms                                                | 55.0 ms: 1.36x faster                                                     |
| thrift                  | 1.03 ms                                                | 761 us: 1.36x faster                                                      |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                     |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                                    |
| 2to3                    | 336 ms                                                 | 249 ms: 1.35x faster                                                      |
| genshi_xml              | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                     |
| tornado_http            | 127 ms                                                 | 94.6 ms: 1.35x faster                                                     |
| deepcopy                | 442 us                                                 | 329 us: 1.34x faster                                                      |
| scimark_fft             | 424 ms                                                 | 321 ms: 1.32x faster                                                      |
| coroutines              | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                     |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                                      |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                      |
| deepcopy_reduce         | 3.82 us                                                | 2.95 us: 1.30x faster                                                     |
| mypy2                   | 428 ms                                                 | 331 ms: 1.29x faster                                                      |
| sqlglot_optimize        | 65.3 ms                                                | 50.5 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed | 951 ms                                                 | 743 ms: 1.28x faster                                                      |
| async_tree_memoization  | 854 ms                                                 | 670 ms: 1.27x faster                                                      |
| fannkuch                | 486 ms                                                 | 389 ms: 1.25x faster                                                      |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                    |
| json_loads              | 28.8 us                                                | 23.5 us: 1.23x faster                                                     |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                      |
| dulwich_log             | 75.9 ms                                                | 62.8 ms: 1.21x faster                                                     |
| nqueens                 | 100 ms                                                 | 82.9 ms: 1.21x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.52 ms: 1.21x faster                                                     |
| bench_thread_pool       | 947 us                                                 | 787 us: 1.20x faster                                                      |
| sympy_expand            | 545 ms                                                 | 453 ms: 1.20x faster                                                      |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.8 ms: 1.19x faster                                                     |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.19x faster                                                     |
| json                    | 5.42 ms                                                | 4.60 ms: 1.18x faster                                                     |
| xml_etree_generate      | 94.2 ms                                                | 80.6 ms: 1.17x faster                                                     |
| sympy_str               | 328 ms                                                 | 282 ms: 1.16x faster                                                      |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.15x faster                                                     |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                     |
| xml_etree_iterparse     | 111 ms                                                 | 99.2 ms: 1.12x faster                                                     |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                     |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.11x faster                                                     |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                      |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                                     |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                      |
| regex_dna               | 222 ms                                                 | 206 ms: 1.08x faster                                                      |
| unpickle                | 14.1 us                                                | 13.2 us: 1.08x faster                                                     |
| pickle_list             | 4.56 us                                                | 4.25 us: 1.07x faster                                                     |
| mdp                     | 2.82 sec                                               | 2.65 sec: 1.07x faster                                                    |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                                     |
| async_generators        | 425 ms                                                 | 422 ms: 1.01x faster                                                      |
| gc_traversal            | 3.84 ms                                                | 3.83 ms: 1.00x faster                                                     |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                                      |
| unpickle_list           | 4.82 us                                                | 4.97 us: 1.03x slower                                                     |
| python_startup_no_site  | 5.82 ms                                                | 6.57 ms: 1.13x slower                                                     |
| regex_effbot            | 3.23 ms                                                | 3.69 ms: 1.14x slower                                                     |
| pickle_dict             | 27.3 us                                                | 31.5 us: 1.16x slower                                                     |
| dask                    | 423 ms                                                 | 506 ms: 1.20x slower                                                      |
| coverage                | 72.8 ms                                                | 99.6 ms: 1.37x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                              |

Benchmark hidden because not significant (2): telco, bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
