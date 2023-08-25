
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_binary_subscr
- machine: linux-x86_64
- commit hash: 8b9f269
- commit date: 2023-03-23
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                         |
| chameleon      | 9.06 ms                                                | 6.41 ms: 1.41x faster                                                        |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                       |
| html5lib       | 85.9 ms                                                | 61.9 ms: 1.39x faster                                                        |
| tornado_http   | 127 ms                                                 | 91.2 ms: 1.40x faster                                                        |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.5 ms: 1.62x faster                                                        |
| float          | 111 ms                                                 | 73.3 ms: 1.51x faster                                                        |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                         |
| regex_v8       | 25.0 ms                                                | 21.4 ms: 1.17x faster                                                        |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                                         |
| regex_effbot   | 3.23 ms                                                | 3.50 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                                         |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.65 ms: 1.40x faster                                                        |
| xml_etree_process    | 74.9 ms                                                | 55.7 ms: 1.34x faster                                                        |
| json_loads           | 28.8 us                                                | 24.4 us: 1.18x faster                                                        |
| xml_etree_generate   | 94.2 ms                                                | 80.8 ms: 1.17x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 99.3 ms: 1.12x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                         |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.36 us: 1.04x faster                                                        |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                        |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.04x slower                                                        |
| pickle_dict          | 27.3 us                                                | 31.5 us: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.79 ms: 1.61x faster                                                        |
| python_startup_no_site | 5.82 ms                                                | 6.49 ms: 1.11x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.99 ms: 1.48x faster                                                        |
| genshi_text     | 30.3 ms                                                | 21.4 ms: 1.41x faster                                                        |
| django_template | 45.9 ms                                                | 33.3 ms: 1.38x faster                                                        |
| genshi_xml      | 63.3 ms                                                | 47.7 ms: 1.33x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.9 ms: 2.57x faster                                                        |
| deltablue               | 7.42 ms                                                | 3.24 ms: 2.29x faster                                                        |
| asyncio_tcp             | 925 ms                                                 | 506 ms: 1.83x faster                                                         |
| logging_silent          | 175 ns                                                 | 96.6 ns: 1.81x faster                                                        |
| scimark_sor             | 197 ms                                                 | 112 ms: 1.75x faster                                                         |
| richards                | 74.9 ms                                                | 44.3 ms: 1.69x faster                                                        |
| raytrace                | 464 ms                                                 | 285 ms: 1.63x faster                                                         |
| pyflate                 | 673 ms                                                 | 414 ms: 1.63x faster                                                         |
| nbody                   | 142 ms                                                 | 87.5 ms: 1.62x faster                                                        |
| go                      | 229 ms                                                 | 142 ms: 1.61x faster                                                         |
| python_startup          | 14.2 ms                                                | 8.79 ms: 1.61x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 73.8 ms: 1.61x faster                                                        |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                                         |
| spectral_norm           | 150 ms                                                 | 94.4 ms: 1.59x faster                                                        |
| scimark_monte_carlo     | 108 ms                                                 | 68.3 ms: 1.58x faster                                                        |
| hexiom                  | 9.53 ms                                                | 6.08 ms: 1.57x faster                                                        |
| chaos                   | 106 ms                                                 | 68.2 ms: 1.56x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 34.4 us: 1.52x faster                                                        |
| unpack_sequence         | 64.7 ns                                                | 42.8 ns: 1.51x faster                                                        |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                                         |
| float                   | 111 ms                                                 | 73.3 ms: 1.51x faster                                                        |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                                         |
| mako                    | 14.8 ms                                                | 9.99 ms: 1.48x faster                                                        |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                                        |
| sqlglot_transpile       | 2.45 ms                                                | 1.73 ms: 1.42x faster                                                        |
| genshi_text             | 30.3 ms                                                | 21.4 ms: 1.41x faster                                                        |
| chameleon               | 9.06 ms                                                | 6.41 ms: 1.41x faster                                                        |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.41x faster                                                       |
| logging_simple          | 8.07 us                                                | 5.73 us: 1.41x faster                                                        |
| pprint_safe_repr        | 955 ms                                                 | 678 ms: 1.41x faster                                                         |
| logging_format          | 8.91 us                                                | 6.34 us: 1.41x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.65 ms: 1.40x faster                                                        |
| tornado_http            | 127 ms                                                 | 91.2 ms: 1.40x faster                                                        |
| html5lib                | 85.9 ms                                                | 61.9 ms: 1.39x faster                                                        |
| django_template         | 45.9 ms                                                | 33.3 ms: 1.38x faster                                                        |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                        |
| async_tree_none         | 717 ms                                                 | 523 ms: 1.37x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                                       |
| scimark_fft             | 424 ms                                                 | 310 ms: 1.37x faster                                                         |
| coroutines              | 31.8 ms                                                | 23.4 ms: 1.36x faster                                                        |
| deepcopy                | 442 us                                                 | 326 us: 1.36x faster                                                         |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                                       |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                        |
| xml_etree_process       | 74.9 ms                                                | 55.7 ms: 1.34x faster                                                        |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                         |
| genshi_xml              | 63.3 ms                                                | 47.7 ms: 1.33x faster                                                        |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                         |
| async_tree_memoization  | 854 ms                                                 | 649 ms: 1.32x faster                                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.18 ms: 1.30x faster                                                        |
| thrift                  | 1.03 ms                                                | 793 us: 1.30x faster                                                         |
| async_tree_cpu_io_mixed | 951 ms                                                 | 740 ms: 1.29x faster                                                         |
| deepcopy_reduce         | 3.82 us                                                | 2.98 us: 1.28x faster                                                        |
| mypy2                   | 428 ms                                                 | 335 ms: 1.28x faster                                                         |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                | 51.4 ms: 1.27x faster                                                        |
| fannkuch                | 486 ms                                                 | 388 ms: 1.25x faster                                                         |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                       |
| nqueens                 | 100 ms                                                 | 81.6 ms: 1.23x faster                                                        |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                         |
| bench_thread_pool       | 947 us                                                 | 789 us: 1.20x faster                                                         |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.7 ms: 1.20x faster                                                        |
| dulwich_log             | 75.9 ms                                                | 63.8 ms: 1.19x faster                                                        |
| json_loads              | 28.8 us                                                | 24.4 us: 1.18x faster                                                        |
| sympy_expand            | 545 ms                                                 | 463 ms: 1.18x faster                                                         |
| sympy_integrate         | 24.3 ms                                                | 20.6 ms: 1.18x faster                                                        |
| regex_v8                | 25.0 ms                                                | 21.4 ms: 1.17x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 80.8 ms: 1.17x faster                                                        |
| json                    | 5.42 ms                                                | 4.70 ms: 1.15x faster                                                        |
| sympy_str               | 328 ms                                                 | 286 ms: 1.15x faster                                                         |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 99.3 ms: 1.12x faster                                                        |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.12x faster                                                         |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.52 sec: 1.12x faster                                                       |
| comprehensions          | 26.8 us                                                | 24.0 us: 1.12x faster                                                        |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                         |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                                        |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                         |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                                         |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                                        |
| gc_traversal            | 3.84 ms                                                | 3.66 ms: 1.05x faster                                                        |
| pickle_list             | 4.56 us                                                | 4.36 us: 1.04x faster                                                        |
| async_generators        | 425 ms                                                 | 415 ms: 1.02x faster                                                         |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                         |
| telco                   | 6.54 ms                                                | 6.49 ms: 1.01x faster                                                        |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                                        |
| unpickle_list           | 4.82 us                                                | 4.99 us: 1.04x slower                                                        |
| regex_effbot            | 3.23 ms                                                | 3.50 ms: 1.08x slower                                                        |
| python_startup_no_site  | 5.82 ms                                                | 6.49 ms: 1.11x slower                                                        |
| pickle_dict             | 27.3 us                                                | 31.5 us: 1.15x slower                                                        |
| dask                    | 423 ms                                                 | 508 ms: 1.20x slower                                                         |
| coverage                | 72.8 ms                                                | 95.7 ms: 1.32x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x
