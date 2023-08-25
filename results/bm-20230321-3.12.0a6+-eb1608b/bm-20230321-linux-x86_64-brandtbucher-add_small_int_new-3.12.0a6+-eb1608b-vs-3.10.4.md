
# Results vs. 3.10.4

- fork: brandtbucher
- ref: add_small_int_new
- machine: linux-x86_64
- commit hash: eb1608b
- commit date: 2023-03-21
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 250 ms: 1.34x faster                                                      |
| chameleon      | 9.06 ms                                                | 6.23 ms: 1.45x faster                                                     |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                    |
| html5lib       | 85.9 ms                                                | 60.2 ms: 1.43x faster                                                     |
| tornado_http   | 127 ms                                                 | 91.0 ms: 1.40x faster                                                     |
| Geometric mean | (ref)                                                  | 1.37x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 85.9 ms: 1.65x faster                                                     |
| float          | 111 ms                                                 | 73.9 ms: 1.50x faster                                                     |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                      |
| regex_v8       | 25.0 ms                                                | 21.6 ms: 1.16x faster                                                     |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.38 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 284 us: 1.60x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.52x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.54 ms: 1.42x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 55.3 ms: 1.35x faster                                                     |
| json_loads           | 28.8 us                                                | 24.3 us: 1.19x faster                                                     |
| xml_etree_generate   | 94.2 ms                                                | 79.8 ms: 1.18x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 98.7 ms: 1.13x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                      |
| pickle_list          | 4.56 us                                                | 4.32 us: 1.05x faster                                                     |
| unpickle             | 14.1 us                                                | 13.5 us: 1.04x faster                                                     |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                     |
| unpickle_list        | 4.82 us                                                | 4.96 us: 1.03x slower                                                     |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.90 ms: 1.59x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.51 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                     |
| genshi_text     | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                     |
| django_template | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                     |
| genshi_xml      | 63.3 ms                                                | 48.3 ms: 1.31x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.8 ms: 2.58x faster                                                     |
| deltablue               | 7.42 ms                                                | 3.15 ms: 2.35x faster                                                     |
| logging_silent          | 175 ns                                                 | 92.8 ns: 1.89x faster                                                     |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                      |
| asyncio_tcp             | 925 ms                                                 | 508 ms: 1.82x faster                                                      |
| richards                | 74.9 ms                                                | 41.7 ms: 1.80x faster                                                     |
| go                      | 229 ms                                                 | 130 ms: 1.76x faster                                                      |
| raytrace                | 464 ms                                                 | 279 ms: 1.66x faster                                                      |
| scimark_monte_carlo     | 108 ms                                                 | 65.2 ms: 1.66x faster                                                     |
| nbody                   | 142 ms                                                 | 85.9 ms: 1.65x faster                                                     |
| pyflate                 | 673 ms                                                 | 410 ms: 1.64x faster                                                      |
| chaos                   | 106 ms                                                 | 65.7 ms: 1.62x faster                                                     |
| pickle_pure_python      | 455 us                                                 | 284 us: 1.60x faster                                                      |
| python_startup          | 14.2 ms                                                | 8.90 ms: 1.59x faster                                                     |
| crypto_pyaes            | 118 ms                                                 | 74.7 ms: 1.58x faster                                                     |
| hexiom                  | 9.53 ms                                                | 6.04 ms: 1.58x faster                                                     |
| spectral_norm           | 150 ms                                                 | 95.6 ms: 1.57x faster                                                     |
| deepcopy_memo           | 52.3 us                                                | 34.1 us: 1.54x faster                                                     |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.52x faster                                                      |
| float                   | 111 ms                                                 | 73.9 ms: 1.50x faster                                                     |
| unpack_sequence         | 64.7 ns                                                | 43.5 ns: 1.49x faster                                                     |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.48x faster                                                      |
| mako                    | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                     |
| chameleon               | 9.06 ms                                                | 6.23 ms: 1.45x faster                                                     |
| logging_format          | 8.91 us                                                | 6.20 us: 1.44x faster                                                     |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                                     |
| logging_simple          | 8.07 us                                                | 5.64 us: 1.43x faster                                                     |
| genshi_text             | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                     |
| coroutines              | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                     |
| html5lib                | 85.9 ms                                                | 60.2 ms: 1.43x faster                                                     |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                                    |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.42x faster                                                     |
| json_dumps              | 13.5 ms                                                | 9.54 ms: 1.42x faster                                                     |
| django_template         | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                     |
| tornado_http            | 127 ms                                                 | 91.0 ms: 1.40x faster                                                     |
| pprint_safe_repr        | 955 ms                                                 | 689 ms: 1.39x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 1.28 sec: 1.38x faster                                                    |
| async_tree_none         | 717 ms                                                 | 521 ms: 1.38x faster                                                      |
| scimark_fft             | 424 ms                                                 | 308 ms: 1.38x faster                                                      |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                     |
| deepcopy                | 442 us                                                 | 323 us: 1.37x faster                                                      |
| async_tree_memoization  | 854 ms                                                 | 628 ms: 1.36x faster                                                      |
| xml_etree_process       | 74.9 ms                                                | 55.3 ms: 1.35x faster                                                     |
| 2to3                    | 336 ms                                                 | 250 ms: 1.34x faster                                                      |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                     |
| thrift                  | 1.03 ms                                                | 773 us: 1.34x faster                                                      |
| fannkuch                | 486 ms                                                 | 365 ms: 1.33x faster                                                      |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                      |
| deepcopy_reduce         | 3.82 us                                                | 2.90 us: 1.32x faster                                                     |
| genshi_xml              | 63.3 ms                                                | 48.3 ms: 1.31x faster                                                     |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                    |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.18 ms: 1.31x faster                                                     |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                      |
| mypy2                   | 428 ms                                                 | 333 ms: 1.29x faster                                                      |
| async_tree_cpu_io_mixed | 951 ms                                                 | 741 ms: 1.28x faster                                                      |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                     |
| nqueens                 | 100 ms                                                 | 79.4 ms: 1.26x faster                                                     |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                    |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                      |
| bench_thread_pool       | 947 us                                                 | 788 us: 1.20x faster                                                      |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.7 ms: 1.19x faster                                                     |
| dulwich_log             | 75.9 ms                                                | 63.6 ms: 1.19x faster                                                     |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                     |
| json_loads              | 28.8 us                                                | 24.3 us: 1.19x faster                                                     |
| xml_etree_generate      | 94.2 ms                                                | 79.8 ms: 1.18x faster                                                     |
| json                    | 5.42 ms                                                | 4.61 ms: 1.18x faster                                                     |
| sympy_expand            | 545 ms                                                 | 465 ms: 1.17x faster                                                      |
| mdp                     | 2.82 sec                                               | 2.43 sec: 1.16x faster                                                    |
| regex_v8                | 25.0 ms                                                | 21.6 ms: 1.16x faster                                                     |
| sympy_str               | 328 ms                                                 | 284 ms: 1.16x faster                                                      |
| comprehensions          | 26.8 us                                                | 23.3 us: 1.15x faster                                                     |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                                     |
| xml_etree_iterparse     | 111 ms                                                 | 98.7 ms: 1.13x faster                                                     |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                     |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                     |
| sympy_sum               | 185 ms                                                 | 165 ms: 1.12x faster                                                      |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                      |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                      |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                                      |
| pickle_list             | 4.56 us                                                | 4.32 us: 1.05x faster                                                     |
| unpickle                | 14.1 us                                                | 13.5 us: 1.04x faster                                                     |
| async_generators        | 425 ms                                                 | 416 ms: 1.02x faster                                                      |
| telco                   | 6.54 ms                                                | 6.42 ms: 1.02x faster                                                     |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                      |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                                     |
| unpickle_list           | 4.82 us                                                | 4.96 us: 1.03x slower                                                     |
| gc_traversal            | 3.84 ms                                                | 3.98 ms: 1.04x slower                                                     |
| regex_effbot            | 3.23 ms                                                | 3.38 ms: 1.05x slower                                                     |
| python_startup_no_site  | 5.82 ms                                                | 6.51 ms: 1.12x slower                                                     |
| pickle_dict             | 27.3 us                                                | 31.6 us: 1.16x slower                                                     |
| dask                    | 423 ms                                                 | 502 ms: 1.19x slower                                                      |
| coverage                | 72.8 ms                                                | 94.0 ms: 1.29x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x
