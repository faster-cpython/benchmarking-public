
# Results vs. 3.10.4

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: fd42c63
- commit date: 2023-03-09
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                         |
| chameleon      | 9.06 ms                                                | 6.41 ms: 1.41x faster                                                        |
| docutils       | 3.17 sec                                               | 2.58 sec: 1.23x faster                                                       |
| html5lib       | 85.9 ms                                                | 62.8 ms: 1.37x faster                                                        |
| tornado_http   | 127 ms                                                 | 94.9 ms: 1.34x faster                                                        |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.9 ms: 1.51x faster                                                        |
| float          | 111 ms                                                 | 74.7 ms: 1.48x faster                                                        |
| pidigits       | 190 ms                                                 | 193 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                         |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.15x faster                                                        |
| regex_dna      | 222 ms                                                 | 199 ms: 1.11x faster                                                         |
| regex_effbot   | 3.23 ms                                                | 3.53 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 290 us: 1.57x faster                                                         |
| unpickle_pure_python | 300 us                                                 | 207 us: 1.45x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.42 ms: 1.44x faster                                                        |
| xml_etree_process    | 74.9 ms                                                | 55.6 ms: 1.35x faster                                                        |
| json_loads           | 28.8 us                                                | 23.9 us: 1.21x faster                                                        |
| xml_etree_generate   | 94.2 ms                                                | 81.9 ms: 1.15x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.07 us: 1.12x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                         |
| unpickle             | 14.1 us                                                | 13.4 us: 1.06x faster                                                        |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.02x slower                                                        |
| pickle_dict          | 27.3 us                                                | 30.7 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.02 ms: 1.57x faster                                                        |
| python_startup_no_site | 5.82 ms                                                | 6.54 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.2 ms: 1.44x faster                                                        |
| genshi_text     | 30.3 ms                                                | 21.7 ms: 1.40x faster                                                        |
| django_template | 45.9 ms                                                | 33.5 ms: 1.37x faster                                                        |
| genshi_xml      | 63.3 ms                                                | 47.9 ms: 1.32x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.9 ms: 2.48x faster                                                        |
| deltablue               | 7.42 ms                                                | 3.28 ms: 2.26x faster                                                        |
| asyncio_tcp             | 925 ms                                                 | 504 ms: 1.84x faster                                                         |
| logging_silent          | 175 ns                                                 | 97.2 ns: 1.80x faster                                                        |
| scimark_sor             | 197 ms                                                 | 110 ms: 1.79x faster                                                         |
| richards                | 74.9 ms                                                | 43.8 ms: 1.71x faster                                                        |
| go                      | 229 ms                                                 | 140 ms: 1.64x faster                                                         |
| pyflate                 | 673 ms                                                 | 412 ms: 1.63x faster                                                         |
| crypto_pyaes            | 118 ms                                                 | 73.1 ms: 1.62x faster                                                        |
| raytrace                | 464 ms                                                 | 287 ms: 1.61x faster                                                         |
| chaos                   | 106 ms                                                 | 66.6 ms: 1.60x faster                                                        |
| scimark_monte_carlo     | 108 ms                                                 | 68.3 ms: 1.58x faster                                                        |
| pickle_pure_python      | 455 us                                                 | 290 us: 1.57x faster                                                         |
| spectral_norm           | 150 ms                                                 | 95.6 ms: 1.57x faster                                                        |
| python_startup          | 14.2 ms                                                | 9.02 ms: 1.57x faster                                                        |
| hexiom                  | 9.53 ms                                                | 6.10 ms: 1.56x faster                                                        |
| unpack_sequence         | 64.7 ns                                                | 42.7 ns: 1.52x faster                                                        |
| nbody                   | 142 ms                                                 | 93.9 ms: 1.51x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 35.0 us: 1.49x faster                                                        |
| float                   | 111 ms                                                 | 74.7 ms: 1.48x faster                                                        |
| unpickle_pure_python    | 300 us                                                 | 207 us: 1.45x faster                                                         |
| scimark_lu              | 163 ms                                                 | 113 ms: 1.45x faster                                                         |
| mako                    | 14.8 ms                                                | 10.2 ms: 1.44x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.42 ms: 1.44x faster                                                        |
| sqlglot_parse           | 2.06 ms                                                | 1.46 ms: 1.41x faster                                                        |
| chameleon               | 9.06 ms                                                | 6.41 ms: 1.41x faster                                                        |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.41x faster                                                       |
| sqlglot_transpile       | 2.45 ms                                                | 1.74 ms: 1.40x faster                                                        |
| genshi_text             | 30.3 ms                                                | 21.7 ms: 1.40x faster                                                        |
| pprint_safe_repr        | 955 ms                                                 | 686 ms: 1.39x faster                                                         |
| logging_format          | 8.91 us                                                | 6.41 us: 1.39x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.38x faster                                                       |
| logging_simple          | 8.07 us                                                | 5.87 us: 1.38x faster                                                        |
| django_template         | 45.9 ms                                                | 33.5 ms: 1.37x faster                                                        |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                        |
| html5lib                | 85.9 ms                                                | 62.8 ms: 1.37x faster                                                        |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                                         |
| coroutines              | 31.8 ms                                                | 23.5 ms: 1.35x faster                                                        |
| thrift                  | 1.03 ms                                                | 765 us: 1.35x faster                                                         |
| xml_etree_process       | 74.9 ms                                                | 55.6 ms: 1.35x faster                                                        |
| pycparser               | 1.50 sec                                               | 1.12 sec: 1.34x faster                                                       |
| tornado_http            | 127 ms                                                 | 94.9 ms: 1.34x faster                                                        |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                        |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                         |
| genshi_xml              | 63.3 ms                                                | 47.9 ms: 1.32x faster                                                        |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                                         |
| deepcopy                | 442 us                                                 | 337 us: 1.31x faster                                                         |
| async_tree_memoization  | 854 ms                                                 | 655 ms: 1.30x faster                                                         |
| scimark_fft             | 424 ms                                                 | 326 ms: 1.30x faster                                                         |
| fannkuch                | 486 ms                                                 | 375 ms: 1.30x faster                                                         |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                         |
| mypy2                   | 428 ms                                                 | 332 ms: 1.29x faster                                                         |
| deepcopy_reduce         | 3.82 us                                                | 2.99 us: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                 | 745 ms: 1.28x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                | 51.4 ms: 1.27x faster                                                        |
| docutils                | 3.17 sec                                               | 2.58 sec: 1.23x faster                                                       |
| nqueens                 | 100 ms                                                 | 82.9 ms: 1.21x faster                                                        |
| json_loads              | 28.8 us                                                | 23.9 us: 1.21x faster                                                        |
| dulwich_log             | 75.9 ms                                                | 63.5 ms: 1.20x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 795 us: 1.19x faster                                                         |
| sqlalchemy_declarative  | 165 ms                                                 | 140 ms: 1.18x faster                                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.62 ms: 1.18x faster                                                        |
| json                    | 5.42 ms                                                | 4.60 ms: 1.18x faster                                                        |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.0 ms: 1.18x faster                                                        |
| sympy_expand            | 545 ms                                                 | 465 ms: 1.17x faster                                                         |
| sympy_integrate         | 24.3 ms                                                | 20.7 ms: 1.17x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 81.9 ms: 1.15x faster                                                        |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.15x faster                                                        |
| sympy_str               | 328 ms                                                 | 288 ms: 1.14x faster                                                         |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                        |
| sqlite_synth            | 2.93 us                                                | 2.61 us: 1.12x faster                                                        |
| pickle_list             | 4.56 us                                                | 4.07 us: 1.12x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                        |
| regex_dna               | 222 ms                                                 | 199 ms: 1.11x faster                                                         |
| comprehensions          | 26.8 us                                                | 24.2 us: 1.11x faster                                                        |
| sympy_sum               | 185 ms                                                 | 167 ms: 1.11x faster                                                         |
| djangocms               | 35.9 us                                                | 32.5 us: 1.10x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                                         |
| mdp                     | 2.82 sec                                               | 2.61 sec: 1.08x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                                         |
| unpickle                | 14.1 us                                                | 13.4 us: 1.06x faster                                                        |
| telco                   | 6.54 ms                                                | 6.44 ms: 1.02x faster                                                        |
| async_generators        | 425 ms                                                 | 420 ms: 1.01x faster                                                         |
| pidigits                | 190 ms                                                 | 193 ms: 1.02x slower                                                         |
| unpickle_list           | 4.82 us                                                | 4.94 us: 1.02x slower                                                        |
| gc_traversal            | 3.84 ms                                                | 4.19 ms: 1.09x slower                                                        |
| regex_effbot            | 3.23 ms                                                | 3.53 ms: 1.09x slower                                                        |
| python_startup_no_site  | 5.82 ms                                                | 6.54 ms: 1.12x slower                                                        |
| pickle_dict             | 27.3 us                                                | 30.7 us: 1.13x slower                                                        |
| dask                    | 423 ms                                                 | 513 ms: 1.21x slower                                                         |
| coverage                | 72.8 ms                                                | 96.5 ms: 1.33x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                 |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.23x
