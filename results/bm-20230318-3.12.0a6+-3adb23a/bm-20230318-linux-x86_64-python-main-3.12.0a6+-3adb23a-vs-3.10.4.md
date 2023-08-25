
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3adb23a
- commit date: 2023-03-18
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 249 ms: 1.35x faster                                   |
| chameleon      | 9.06 ms                                                | 6.35 ms: 1.43x faster                                  |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.25x faster                                 |
| html5lib       | 85.9 ms                                                | 61.2 ms: 1.40x faster                                  |
| tornado_http   | 127 ms                                                 | 91.2 ms: 1.40x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 86.0 ms: 1.65x faster                                  |
| float          | 111 ms                                                 | 73.9 ms: 1.50x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                  |
| regex_dna      | 222 ms                                                 | 201 ms: 1.10x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.63 ms: 1.12x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 284 us: 1.60x faster                                   |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.51x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.57 ms: 1.41x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 55.2 ms: 1.36x faster                                  |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 80.4 ms: 1.17x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.10x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                   |
| pickle_list          | 4.56 us                                                | 4.26 us: 1.07x faster                                  |
| unpickle             | 14.1 us                                                | 13.5 us: 1.05x faster                                  |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                  |
| unpickle_list        | 4.82 us                                                | 5.00 us: 1.04x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.3 us: 1.15x slower                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.91 ms: 1.59x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.52 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.1 ms: 1.47x faster                                  |
| genshi_text     | 30.3 ms                                                | 21.0 ms: 1.44x faster                                  |
| django_template | 45.9 ms                                                | 32.9 ms: 1.39x faster                                  |
| genshi_xml      | 63.3 ms                                                | 47.1 ms: 1.34x faster                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-linux-x86_64-python-main-3.12.0a6+-3adb23a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.3 ms: 2.62x faster                                  |
| deltablue               | 7.42 ms                                                | 3.17 ms: 2.34x faster                                  |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                   |
| logging_silent          | 175 ns                                                 | 94.9 ns: 1.85x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 507 ms: 1.82x faster                                   |
| richards                | 74.9 ms                                                | 41.9 ms: 1.79x faster                                  |
| go                      | 229 ms                                                 | 137 ms: 1.68x faster                                   |
| raytrace                | 464 ms                                                 | 280 ms: 1.65x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 65.7 ms: 1.65x faster                                  |
| nbody                   | 142 ms                                                 | 86.0 ms: 1.65x faster                                  |
| pyflate                 | 673 ms                                                 | 414 ms: 1.62x faster                                   |
| spectral_norm           | 150 ms                                                 | 92.7 ms: 1.62x faster                                  |
| chaos                   | 106 ms                                                 | 66.0 ms: 1.61x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 73.7 ms: 1.61x faster                                  |
| pickle_pure_python      | 455 us                                                 | 284 us: 1.60x faster                                   |
| python_startup          | 14.2 ms                                                | 8.91 ms: 1.59x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.11 ms: 1.56x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 34.2 us: 1.53x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.51x faster                                   |
| unpack_sequence         | 64.7 ns                                                | 43.2 ns: 1.50x faster                                  |
| float                   | 111 ms                                                 | 73.9 ms: 1.50x faster                                  |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.49x faster                                   |
| mako                    | 14.8 ms                                                | 10.1 ms: 1.47x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                  |
| genshi_text             | 30.3 ms                                                | 21.0 ms: 1.44x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                  |
| chameleon               | 9.06 ms                                                | 6.35 ms: 1.43x faster                                  |
| logging_simple          | 8.07 us                                                | 5.69 us: 1.42x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.57 ms: 1.41x faster                                  |
| logging_format          | 8.91 us                                                | 6.31 us: 1.41x faster                                  |
| scimark_fft             | 424 ms                                                 | 300 ms: 1.41x faster                                   |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.41x faster                                 |
| html5lib                | 85.9 ms                                                | 61.2 ms: 1.40x faster                                  |
| coroutines              | 31.8 ms                                                | 22.8 ms: 1.40x faster                                  |
| tornado_http            | 127 ms                                                 | 91.2 ms: 1.40x faster                                  |
| django_template         | 45.9 ms                                                | 32.9 ms: 1.39x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 686 ms: 1.39x faster                                   |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                  |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.37x faster                                 |
| async_tree_none         | 717 ms                                                 | 523 ms: 1.37x faster                                   |
| deepcopy                | 442 us                                                 | 323 us: 1.37x faster                                   |
| xml_etree_process       | 74.9 ms                                                | 55.2 ms: 1.36x faster                                  |
| 2to3                    | 336 ms                                                 | 249 ms: 1.35x faster                                   |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                 |
| genshi_xml              | 63.3 ms                                                | 47.1 ms: 1.34x faster                                  |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                  |
| thrift                  | 1.03 ms                                                | 771 us: 1.34x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 644 ms: 1.33x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.90 us: 1.32x faster                                  |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.15 ms: 1.31x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 103 ms: 1.31x faster                                   |
| mypy2                   | 428 ms                                                 | 332 ms: 1.29x faster                                   |
| fannkuch                | 486 ms                                                 | 377 ms: 1.29x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.9 ms: 1.28x faster                                  |
| nqueens                 | 100 ms                                                 | 77.9 ms: 1.28x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 747 ms: 1.27x faster                                   |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.25x faster                                 |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                   |
| bench_thread_pool       | 947 us                                                 | 785 us: 1.21x faster                                   |
| dulwich_log             | 75.9 ms                                                | 63.0 ms: 1.21x faster                                  |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                  |
| sympy_expand            | 545 ms                                                 | 458 ms: 1.19x faster                                   |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.8 ms: 1.19x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                  |
| json                    | 5.42 ms                                                | 4.62 ms: 1.17x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 80.4 ms: 1.17x faster                                  |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                  |
| comprehensions          | 26.8 us                                                | 23.8 us: 1.13x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.12x faster                                  |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                   |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                   |
| regex_dna               | 222 ms                                                 | 201 ms: 1.10x faster                                   |
| djangocms               | 35.9 us                                                | 32.7 us: 1.10x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.10x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                   |
| mdp                     | 2.82 sec                                               | 2.61 sec: 1.08x faster                                 |
| pickle_list             | 4.56 us                                                | 4.26 us: 1.07x faster                                  |
| unpickle                | 14.1 us                                                | 13.5 us: 1.05x faster                                  |
| async_generators        | 425 ms                                                 | 413 ms: 1.03x faster                                   |
| telco                   | 6.54 ms                                                | 6.43 ms: 1.02x faster                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                  |
| gc_traversal            | 3.84 ms                                                | 3.90 ms: 1.02x slower                                  |
| unpickle_list           | 4.82 us                                                | 5.00 us: 1.04x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.52 ms: 1.12x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.63 ms: 1.12x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.3 us: 1.15x slower                                  |
| dask                    | 423 ms                                                 | 501 ms: 1.19x slower                                   |
| coverage                | 72.8 ms                                                | 97.0 ms: 1.33x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x
