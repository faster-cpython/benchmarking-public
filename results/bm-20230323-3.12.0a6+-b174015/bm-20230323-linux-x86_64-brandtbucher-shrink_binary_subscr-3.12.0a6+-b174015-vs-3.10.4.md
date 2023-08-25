
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_binary_subscr
- machine: linux-x86_64
- commit hash: b174015
- commit date: 2023-03-23
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 254 ms: 1.32x faster                                                         |
| chameleon      | 9.06 ms                                                | 6.52 ms: 1.39x faster                                                        |
| docutils       | 3.17 sec                                               | 2.56 sec: 1.24x faster                                                       |
| html5lib       | 85.9 ms                                                | 62.2 ms: 1.38x faster                                                        |
| tornado_http   | 127 ms                                                 | 91.4 ms: 1.39x faster                                                        |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.5 ms: 1.60x faster                                                        |
| float          | 111 ms                                                 | 74.0 ms: 1.49x faster                                                        |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                        |
| regex_dna      | 222 ms                                                 | 211 ms: 1.05x faster                                                         |
| regex_effbot   | 3.23 ms                                                | 3.53 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 287 us: 1.59x faster                                                         |
| unpickle_pure_python | 300 us                                                 | 202 us: 1.49x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.68 ms: 1.40x faster                                                        |
| xml_etree_process    | 74.9 ms                                                | 57.2 ms: 1.31x faster                                                        |
| json_loads           | 28.8 us                                                | 23.9 us: 1.21x faster                                                        |
| xml_etree_generate   | 94.2 ms                                                | 82.1 ms: 1.15x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 100.0 ms: 1.12x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.37 us: 1.04x faster                                                        |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                                        |
| unpickle_list        | 4.82 us                                                | 5.03 us: 1.04x slower                                                        |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.84 ms: 1.60x faster                                                        |
| python_startup_no_site | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.85 ms: 1.50x faster                                                        |
| genshi_text     | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                        |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                        |
| genshi_xml      | 63.3 ms                                                | 47.7 ms: 1.33x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.1 ms: 2.64x faster                                                        |
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.33x faster                                                        |
| asyncio_tcp             | 925 ms                                                 | 507 ms: 1.83x faster                                                         |
| logging_silent          | 175 ns                                                 | 97.9 ns: 1.79x faster                                                        |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.78x faster                                                         |
| richards                | 74.9 ms                                                | 42.9 ms: 1.75x faster                                                        |
| raytrace                | 464 ms                                                 | 278 ms: 1.67x faster                                                         |
| go                      | 229 ms                                                 | 140 ms: 1.64x faster                                                         |
| pyflate                 | 673 ms                                                 | 416 ms: 1.62x faster                                                         |
| crypto_pyaes            | 118 ms                                                 | 73.5 ms: 1.61x faster                                                        |
| python_startup          | 14.2 ms                                                | 8.84 ms: 1.60x faster                                                        |
| nbody                   | 142 ms                                                 | 88.5 ms: 1.60x faster                                                        |
| chaos                   | 106 ms                                                 | 66.9 ms: 1.59x faster                                                        |
| pickle_pure_python      | 455 us                                                 | 287 us: 1.59x faster                                                         |
| spectral_norm           | 150 ms                                                 | 94.5 ms: 1.59x faster                                                        |
| hexiom                  | 9.53 ms                                                | 6.03 ms: 1.58x faster                                                        |
| scimark_monte_carlo     | 108 ms                                                 | 69.1 ms: 1.57x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 34.2 us: 1.53x faster                                                        |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                                         |
| unpack_sequence         | 64.7 ns                                                | 42.4 ns: 1.53x faster                                                        |
| mako                    | 14.8 ms                                                | 9.85 ms: 1.50x faster                                                        |
| float                   | 111 ms                                                 | 74.0 ms: 1.49x faster                                                        |
| unpickle_pure_python    | 300 us                                                 | 202 us: 1.49x faster                                                         |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                                        |
| sqlglot_transpile       | 2.45 ms                                                | 1.73 ms: 1.42x faster                                                        |
| genshi_text             | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.68 ms: 1.40x faster                                                        |
| logging_format          | 8.91 us                                                | 6.38 us: 1.40x faster                                                        |
| logging_simple          | 8.07 us                                                | 5.78 us: 1.40x faster                                                        |
| pprint_pformat          | 1.99 sec                                               | 1.42 sec: 1.40x faster                                                       |
| pprint_safe_repr        | 955 ms                                                 | 685 ms: 1.39x faster                                                         |
| tornado_http            | 127 ms                                                 | 91.4 ms: 1.39x faster                                                        |
| django_template         | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                        |
| chameleon               | 9.06 ms                                                | 6.52 ms: 1.39x faster                                                        |
| scimark_fft             | 424 ms                                                 | 306 ms: 1.39x faster                                                         |
| coroutines              | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                        |
| html5lib                | 85.9 ms                                                | 62.2 ms: 1.38x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                                       |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                                         |
| aiohttp                 | 1.38 ms                                                | 1.02 ms: 1.36x faster                                                        |
| deepcopy                | 442 us                                                 | 326 us: 1.36x faster                                                         |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.33x faster                                                        |
| genshi_xml              | 63.3 ms                                                | 47.7 ms: 1.33x faster                                                        |
| 2to3                    | 336 ms                                                 | 254 ms: 1.32x faster                                                         |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.14 ms: 1.32x faster                                                        |
| xml_etree_process       | 74.9 ms                                                | 57.2 ms: 1.31x faster                                                        |
| async_tree_memoization  | 854 ms                                                 | 656 ms: 1.30x faster                                                         |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                         |
| deepcopy_reduce         | 3.82 us                                                | 2.95 us: 1.30x faster                                                        |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.30x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                                        |
| mypy2                   | 428 ms                                                 | 333 ms: 1.29x faster                                                         |
| async_tree_cpu_io_mixed | 951 ms                                                 | 746 ms: 1.27x faster                                                         |
| thrift                  | 1.03 ms                                                | 812 us: 1.27x faster                                                         |
| fannkuch                | 486 ms                                                 | 383 ms: 1.27x faster                                                         |
| docutils                | 3.17 sec                                               | 2.56 sec: 1.24x faster                                                       |
| nqueens                 | 100 ms                                                 | 82.6 ms: 1.21x faster                                                        |
| json_loads              | 28.8 us                                                | 23.9 us: 1.21x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 790 us: 1.20x faster                                                         |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                                         |
| dulwich_log             | 75.9 ms                                                | 63.6 ms: 1.19x faster                                                        |
| json                    | 5.42 ms                                                | 4.55 ms: 1.19x faster                                                        |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.18x faster                                                        |
| sympy_expand            | 545 ms                                                 | 462 ms: 1.18x faster                                                         |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.0 ms: 1.18x faster                                                        |
| sympy_str               | 328 ms                                                 | 284 ms: 1.16x faster                                                         |
| xml_etree_generate      | 94.2 ms                                                | 82.1 ms: 1.15x faster                                                        |
| comprehensions          | 26.8 us                                                | 23.7 us: 1.13x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                        |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                        |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                        |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.12x faster                                                         |
| xml_etree_iterparse     | 111 ms                                                 | 100.0 ms: 1.12x faster                                                       |
| sympy_sum               | 185 ms                                                 | 167 ms: 1.11x faster                                                         |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                                        |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.68 sec: 1.05x faster                                                       |
| regex_dna               | 222 ms                                                 | 211 ms: 1.05x faster                                                         |
| pickle_list             | 4.56 us                                                | 4.37 us: 1.04x faster                                                        |
| async_generators        | 425 ms                                                 | 409 ms: 1.04x faster                                                         |
| telco                   | 6.54 ms                                                | 6.49 ms: 1.01x faster                                                        |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                         |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                                        |
| gc_traversal            | 3.84 ms                                                | 3.90 ms: 1.01x slower                                                        |
| unpickle_list           | 4.82 us                                                | 5.03 us: 1.04x slower                                                        |
| regex_effbot            | 3.23 ms                                                | 3.53 ms: 1.09x slower                                                        |
| python_startup_no_site  | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                        |
| pickle_dict             | 27.3 us                                                | 31.1 us: 1.14x slower                                                        |
| dask                    | 423 ms                                                 | 512 ms: 1.21x slower                                                         |
| coverage                | 72.8 ms                                                | 96.1 ms: 1.32x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
