
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime_n
- machine: linux-x86_64
- commit hash: cdd2a84
- commit date: 2023-02-21
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 247 ms: 1.36x faster                                                         |
| chameleon      | 9.06 ms                                                | 6.42 ms: 1.41x faster                                                        |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.26x faster                                                       |
| html5lib       | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                        |
| tornado_http   | 127 ms                                                 | 94.7 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.6 ms: 1.52x faster                                                        |
| nbody          | 142 ms                                                 | 96.0 ms: 1.48x faster                                                        |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.14x faster                                                        |
| regex_dna      | 222 ms                                                 | 210 ms: 1.05x faster                                                         |
| regex_effbot   | 3.23 ms                                                | 3.36 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                                         |
| unpickle_pure_python | 300 us                                                 | 195 us: 1.54x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.45 ms: 1.43x faster                                                        |
| xml_etree_process    | 74.9 ms                                                | 54.6 ms: 1.37x faster                                                        |
| json_loads           | 28.8 us                                                | 23.6 us: 1.22x faster                                                        |
| xml_etree_generate   | 94.2 ms                                                | 80.0 ms: 1.18x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 99.3 ms: 1.12x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                         |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.30 us: 1.06x faster                                                        |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.04x slower                                                        |
| pickle_dict          | 27.3 us                                                | 32.4 us: 1.19x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.81 ms: 1.61x faster                                                        |
| python_startup_no_site | 5.82 ms                                                | 6.34 ms: 1.09x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.21x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.82 ms: 1.50x faster                                                        |
| genshi_text     | 30.3 ms                                                | 20.8 ms: 1.46x faster                                                        |
| django_template | 45.9 ms                                                | 32.9 ms: 1.40x faster                                                        |
| genshi_xml      | 63.3 ms                                                | 46.5 ms: 1.36x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.5 ms: 2.60x faster                                                        |
| deltablue               | 7.42 ms                                                | 3.16 ms: 2.35x faster                                                        |
| logging_silent          | 175 ns                                                 | 92.9 ns: 1.89x faster                                                        |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.88x faster                                                         |
| asyncio_tcp             | 925 ms                                                 | 503 ms: 1.84x faster                                                         |
| richards                | 74.9 ms                                                | 42.0 ms: 1.78x faster                                                        |
| go                      | 229 ms                                                 | 135 ms: 1.69x faster                                                         |
| pyflate                 | 673 ms                                                 | 400 ms: 1.68x faster                                                         |
| raytrace                | 464 ms                                                 | 284 ms: 1.63x faster                                                         |
| scimark_monte_carlo     | 108 ms                                                 | 66.5 ms: 1.63x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 73.1 ms: 1.62x faster                                                        |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                                         |
| python_startup          | 14.2 ms                                                | 8.81 ms: 1.61x faster                                                        |
| hexiom                  | 9.53 ms                                                | 5.95 ms: 1.60x faster                                                        |
| chaos                   | 106 ms                                                 | 66.4 ms: 1.60x faster                                                        |
| spectral_norm           | 150 ms                                                 | 96.8 ms: 1.55x faster                                                        |
| unpickle_pure_python    | 300 us                                                 | 195 us: 1.54x faster                                                         |
| deepcopy_memo           | 52.3 us                                                | 34.2 us: 1.53x faster                                                        |
| float                   | 111 ms                                                 | 72.6 ms: 1.52x faster                                                        |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                         |
| unpack_sequence         | 64.7 ns                                                | 43.1 ns: 1.50x faster                                                        |
| mako                    | 14.8 ms                                                | 9.82 ms: 1.50x faster                                                        |
| nbody                   | 142 ms                                                 | 96.0 ms: 1.48x faster                                                        |
| genshi_text             | 30.3 ms                                                | 20.8 ms: 1.46x faster                                                        |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.44x faster                                                        |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.45 ms: 1.43x faster                                                        |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.43x faster                                                        |
| pprint_safe_repr        | 955 ms                                                 | 676 ms: 1.41x faster                                                         |
| chameleon               | 9.06 ms                                                | 6.42 ms: 1.41x faster                                                        |
| logging_format          | 8.91 us                                                | 6.33 us: 1.41x faster                                                        |
| html5lib                | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                        |
| coroutines              | 31.8 ms                                                | 22.8 ms: 1.40x faster                                                        |
| django_template         | 45.9 ms                                                | 32.9 ms: 1.40x faster                                                        |
| logging_simple          | 8.07 us                                                | 5.80 us: 1.39x faster                                                        |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                         |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.37x faster                                                       |
| xml_etree_process       | 74.9 ms                                                | 54.6 ms: 1.37x faster                                                        |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                        |
| async_tree_none         | 717 ms                                                 | 527 ms: 1.36x faster                                                         |
| genshi_xml              | 63.3 ms                                                | 46.5 ms: 1.36x faster                                                        |
| 2to3                    | 336 ms                                                 | 247 ms: 1.36x faster                                                         |
| thrift                  | 1.03 ms                                                | 764 us: 1.35x faster                                                         |
| scimark_fft             | 424 ms                                                 | 314 ms: 1.35x faster                                                         |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                        |
| tornado_http            | 127 ms                                                 | 94.7 ms: 1.35x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                                       |
| deepcopy                | 442 us                                                 | 329 us: 1.34x faster                                                         |
| fannkuch                | 486 ms                                                 | 364 ms: 1.33x faster                                                         |
| sqlglot_normalize       | 135 ms                                                 | 103 ms: 1.32x faster                                                         |
| deepcopy_reduce         | 3.82 us                                                | 2.93 us: 1.31x faster                                                        |
| async_tree_memoization  | 854 ms                                                 | 656 ms: 1.30x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                | 50.4 ms: 1.30x faster                                                        |
| mypy2                   | 428 ms                                                 | 332 ms: 1.29x faster                                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.23 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                 | 739 ms: 1.29x faster                                                         |
| nqueens                 | 100 ms                                                 | 78.2 ms: 1.28x faster                                                        |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.26x faster                                                       |
| json_loads              | 28.8 us                                                | 23.6 us: 1.22x faster                                                        |
| sympy_expand            | 545 ms                                                 | 453 ms: 1.20x faster                                                         |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                                         |
| dulwich_log             | 75.9 ms                                                | 63.3 ms: 1.20x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 792 us: 1.20x faster                                                         |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                        |
| json                    | 5.42 ms                                                | 4.55 ms: 1.19x faster                                                        |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.8 ms: 1.19x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 80.0 ms: 1.18x faster                                                        |
| sympy_str               | 328 ms                                                 | 284 ms: 1.16x faster                                                         |
| regex_v8                | 25.0 ms                                                | 22.1 ms: 1.14x faster                                                        |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                        |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.51 sec: 1.13x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 99.3 ms: 1.12x faster                                                        |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                         |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                         |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                         |
| djangocms               | 35.9 us                                                | 32.8 us: 1.09x faster                                                        |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                                        |
| pickle_list             | 4.56 us                                                | 4.30 us: 1.06x faster                                                        |
| regex_dna               | 222 ms                                                 | 210 ms: 1.05x faster                                                         |
| gc_traversal            | 3.84 ms                                                | 3.67 ms: 1.05x faster                                                        |
| async_generators        | 425 ms                                                 | 408 ms: 1.04x faster                                                         |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                         |
| unpickle_list           | 4.82 us                                                | 4.99 us: 1.04x slower                                                        |
| regex_effbot            | 3.23 ms                                                | 3.36 ms: 1.04x slower                                                        |
| python_startup_no_site  | 5.82 ms                                                | 6.34 ms: 1.09x slower                                                        |
| dask                    | 423 ms                                                 | 502 ms: 1.19x slower                                                         |
| pickle_dict             | 27.3 us                                                | 32.4 us: 1.19x slower                                                        |
| coverage                | 72.8 ms                                                | 96.4 ms: 1.32x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                 |

Benchmark hidden because not significant (3): telco, bench_mp_pool, pickle
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x
