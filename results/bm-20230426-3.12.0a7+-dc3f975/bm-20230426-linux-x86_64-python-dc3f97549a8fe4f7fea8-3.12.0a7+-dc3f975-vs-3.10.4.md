
# Results vs. 3.10.4

- fork: python
- ref: dc3f97549a8fe4f7fea8
- machine: linux-x86_64
- commit hash: dc3f975
- commit date: 2023-04-26
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 268 ms: 1.26x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.94 ms: 1.31x faster                                                  |
| docutils       | 3.17 sec                                               | 2.70 sec: 1.17x faster                                                 |
| html5lib       | 85.9 ms                                                | 65.2 ms: 1.32x faster                                                  |
| tornado_http   | 127 ms                                                 | 105 ms: 1.22x faster                                                   |
| Geometric mean | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.2 ms: 1.61x faster                                                  |
| float          | 111 ms                                                 | 80.0 ms: 1.38x faster                                                  |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                  |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.75 ms: 1.16x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 313 us: 1.45x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 218 us: 1.38x faster                                                   |
| json_dumps           | 13.5 ms                                                | 10.0 ms: 1.35x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 58.6 ms: 1.28x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 83.9 ms: 1.12x faster                                                  |
| json_loads           | 28.8 us                                                | 25.8 us: 1.12x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.08x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.62 us: 1.01x slower                                                  |
| unpickle_list        | 4.82 us                                                | 4.90 us: 1.02x slower                                                  |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                  |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                                  |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.03 ms: 1.57x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.62 ms: 1.14x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.9 ms: 1.36x faster                                                  |
| genshi_text     | 30.3 ms                                                | 22.7 ms: 1.34x faster                                                  |
| django_template | 45.9 ms                                                | 34.7 ms: 1.32x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 51.5 ms: 1.23x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 32.4 ms: 2.37x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.53 ms: 2.10x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 507 ms: 1.82x faster                                                   |
| logging_silent          | 175 ns                                                 | 99.9 ns: 1.75x faster                                                  |
| richards                | 74.9 ms                                                | 43.4 ms: 1.73x faster                                                  |
| go                      | 229 ms                                                 | 135 ms: 1.69x faster                                                   |
| nbody                   | 142 ms                                                 | 88.2 ms: 1.61x faster                                                  |
| python_startup          | 14.2 ms                                                | 9.03 ms: 1.57x faster                                                  |
| scimark_sor             | 197 ms                                                 | 126 ms: 1.56x faster                                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.33 ms: 1.55x faster                                                  |
| raytrace                | 464 ms                                                 | 302 ms: 1.54x faster                                                   |
| chaos                   | 106 ms                                                 | 69.3 ms: 1.53x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.27 ms: 1.52x faster                                                  |
| pyflate                 | 673 ms                                                 | 451 ms: 1.49x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 79.5 ms: 1.49x faster                                                  |
| scimark_monte_carlo     | 108 ms                                                 | 73.1 ms: 1.48x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.65 ms: 1.48x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 313 us: 1.45x faster                                                   |
| scimark_lu              | 163 ms                                                 | 112 ms: 1.45x faster                                                   |
| coroutines              | 31.8 ms                                                | 22.5 ms: 1.42x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 46.6 ns: 1.39x faster                                                  |
| spectral_norm           | 150 ms                                                 | 108 ms: 1.38x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.28 sec: 1.38x faster                                                 |
| float                   | 111 ms                                                 | 80.0 ms: 1.38x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 218 us: 1.38x faster                                                   |
| async_tree_none         | 717 ms                                                 | 527 ms: 1.36x faster                                                   |
| mako                    | 14.8 ms                                                | 10.9 ms: 1.36x faster                                                  |
| json_dumps              | 13.5 ms                                                | 10.0 ms: 1.35x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 39.0 us: 1.34x faster                                                  |
| genshi_text             | 30.3 ms                                                | 22.7 ms: 1.34x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.48 sec: 1.34x faster                                                 |
| django_template         | 45.9 ms                                                | 34.7 ms: 1.32x faster                                                  |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.32x faster                                                 |
| html5lib                | 85.9 ms                                                | 65.2 ms: 1.32x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 726 ms: 1.31x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 654 ms: 1.31x faster                                                   |
| chameleon               | 9.06 ms                                                | 6.94 ms: 1.31x faster                                                  |
| logging_simple          | 8.07 us                                                | 6.24 us: 1.29x faster                                                  |
| logging_format          | 8.91 us                                                | 6.90 us: 1.29x faster                                                  |
| thrift                  | 1.03 ms                                                | 805 us: 1.28x faster                                                   |
| xml_etree_process       | 74.9 ms                                                | 58.6 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 747 ms: 1.27x faster                                                   |
| fannkuch                | 486 ms                                                 | 385 ms: 1.26x faster                                                   |
| 2to3                    | 336 ms                                                 | 268 ms: 1.26x faster                                                   |
| genshi_xml              | 63.3 ms                                                | 51.5 ms: 1.23x faster                                                  |
| mypy2                   | 428 ms                                                 | 351 ms: 1.22x faster                                                   |
| regex_compile           | 177 ms                                                 | 145 ms: 1.22x faster                                                   |
| tornado_http            | 127 ms                                                 | 105 ms: 1.22x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 111 ms: 1.21x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 54.3 ms: 1.20x faster                                                  |
| deepcopy                | 442 us                                                 | 368 us: 1.20x faster                                                   |
| deepcopy_reduce         | 3.82 us                                                | 3.22 us: 1.19x faster                                                  |
| nqueens                 | 100 ms                                                 | 84.5 ms: 1.18x faster                                                  |
| docutils                | 3.17 sec                                               | 2.70 sec: 1.17x faster                                                 |
| scimark_fft             | 424 ms                                                 | 364 ms: 1.16x faster                                                   |
| comprehensions          | 26.8 us                                                | 23.5 us: 1.14x faster                                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 836 us: 1.13x faster                                                   |
| sqlalchemy_declarative  | 165 ms                                                 | 146 ms: 1.13x faster                                                   |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 83.9 ms: 1.12x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 67.9 ms: 1.12x faster                                                  |
| json_loads              | 28.8 us                                                | 25.8 us: 1.12x faster                                                  |
| pylint                  | 525 ms                                                 | 471 ms: 1.11x faster                                                   |
| sympy_integrate         | 24.3 ms                                                | 21.9 ms: 1.11x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.1 ms: 1.11x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.57 sec: 1.10x faster                                                 |
| json                    | 5.42 ms                                                | 4.96 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 5.00 ms: 1.09x faster                                                  |
| sympy_expand            | 545 ms                                                 | 501 ms: 1.09x faster                                                   |
| regex_dna               | 222 ms                                                 | 204 ms: 1.09x faster                                                   |
| sqlite_synth            | 2.93 us                                                | 2.70 us: 1.09x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                   |
| pathlib                 | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 152 ms: 1.08x faster                                                   |
| djangocms               | 35.9 us                                                | 33.6 us: 1.07x faster                                                  |
| sympy_str               | 328 ms                                                 | 312 ms: 1.05x faster                                                   |
| gc_traversal            | 3.84 ms                                                | 3.76 ms: 1.02x faster                                                  |
| sympy_sum               | 185 ms                                                 | 182 ms: 1.02x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.62 us: 1.01x slower                                                  |
| unpickle_list           | 4.82 us                                                | 4.90 us: 1.02x slower                                                  |
| telco                   | 6.54 ms                                                | 6.78 ms: 1.04x slower                                                  |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                   |
| pickle                  | 10.3 us                                                | 10.7 us: 1.04x slower                                                  |
| async_generators        | 425 ms                                                 | 449 ms: 1.06x slower                                                   |
| unpickle                | 14.1 us                                                | 15.0 us: 1.06x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.62 ms: 1.14x slower                                                  |
| pickle_dict             | 27.3 us                                                | 31.6 us: 1.16x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.75 ms: 1.16x slower                                                  |
| dask                    | 423 ms                                                 | 541 ms: 1.28x slower                                                   |
| coverage                | 72.8 ms                                                | 99.0 ms: 1.36x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (2): bench_mp_pool, meteor_contest
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x
