
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime_n
- machine: linux-x86_64
- commit hash: b201b6d
- commit date: 2023-03-24
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                         |
| chameleon      | 9.06 ms                                                | 6.51 ms: 1.39x faster                                                        |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                       |
| html5lib       | 85.9 ms                                                | 62.6 ms: 1.37x faster                                                        |
| tornado_http   | 127 ms                                                 | 91.6 ms: 1.39x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.6 ms: 1.60x faster                                                        |
| float          | 111 ms                                                 | 74.4 ms: 1.49x faster                                                        |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.31x faster                                                         |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.18x faster                                                        |
| regex_dna      | 222 ms                                                 | 202 ms: 1.10x faster                                                         |
| regex_effbot   | 3.23 ms                                                | 3.41 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 294 us: 1.55x faster                                                         |
| unpickle_pure_python | 300 us                                                 | 202 us: 1.49x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.73 ms: 1.39x faster                                                        |
| xml_etree_process    | 74.9 ms                                                | 56.5 ms: 1.33x faster                                                        |
| json_loads           | 28.8 us                                                | 24.5 us: 1.17x faster                                                        |
| xml_etree_generate   | 94.2 ms                                                | 81.1 ms: 1.16x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 99.9 ms: 1.12x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| pickle_list          | 4.56 us                                                | 4.20 us: 1.09x faster                                                        |
| unpickle_list        | 4.82 us                                                | 4.92 us: 1.02x slower                                                        |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                        |
| pickle_dict          | 27.3 us                                                | 31.7 us: 1.16x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.65 ms: 1.64x faster                                                        |
| python_startup_no_site | 5.82 ms                                                | 6.34 ms: 1.09x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.23x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.1 ms: 1.46x faster                                                        |
| django_template | 45.9 ms                                                | 33.9 ms: 1.36x faster                                                        |
| genshi_text     | 30.3 ms                                                | 22.5 ms: 1.35x faster                                                        |
| genshi_xml      | 63.3 ms                                                | 48.5 ms: 1.31x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.1 ms: 2.64x faster                                                        |
| deltablue               | 7.42 ms                                                | 3.26 ms: 2.28x faster                                                        |
| asyncio_tcp             | 925 ms                                                 | 509 ms: 1.82x faster                                                         |
| logging_silent          | 175 ns                                                 | 96.5 ns: 1.81x faster                                                        |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.77x faster                                                         |
| richards                | 74.9 ms                                                | 44.2 ms: 1.70x faster                                                        |
| spectral_norm           | 150 ms                                                 | 91.1 ms: 1.65x faster                                                        |
| python_startup          | 14.2 ms                                                | 8.65 ms: 1.64x faster                                                        |
| raytrace                | 464 ms                                                 | 284 ms: 1.63x faster                                                         |
| go                      | 229 ms                                                 | 141 ms: 1.63x faster                                                         |
| scimark_monte_carlo     | 108 ms                                                 | 67.4 ms: 1.61x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 73.8 ms: 1.60x faster                                                        |
| nbody                   | 142 ms                                                 | 88.6 ms: 1.60x faster                                                        |
| chaos                   | 106 ms                                                 | 66.9 ms: 1.59x faster                                                        |
| pyflate                 | 673 ms                                                 | 427 ms: 1.58x faster                                                         |
| hexiom                  | 9.53 ms                                                | 6.06 ms: 1.57x faster                                                        |
| pickle_pure_python      | 455 us                                                 | 294 us: 1.55x faster                                                         |
| deepcopy_memo           | 52.3 us                                                | 34.4 us: 1.52x faster                                                        |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                                         |
| unpickle_pure_python    | 300 us                                                 | 202 us: 1.49x faster                                                         |
| float                   | 111 ms                                                 | 74.4 ms: 1.49x faster                                                        |
| mako                    | 14.8 ms                                                | 10.1 ms: 1.46x faster                                                        |
| unpack_sequence         | 64.7 ns                                                | 44.4 ns: 1.46x faster                                                        |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.43x faster                                                        |
| sqlglot_transpile       | 2.45 ms                                                | 1.73 ms: 1.41x faster                                                        |
| pprint_pformat          | 1.99 sec                                               | 1.42 sec: 1.39x faster                                                       |
| chameleon               | 9.06 ms                                                | 6.51 ms: 1.39x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.73 ms: 1.39x faster                                                        |
| tornado_http            | 127 ms                                                 | 91.6 ms: 1.39x faster                                                        |
| scimark_fft             | 424 ms                                                 | 308 ms: 1.38x faster                                                         |
| html5lib                | 85.9 ms                                                | 62.6 ms: 1.37x faster                                                        |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                        |
| pprint_safe_repr        | 955 ms                                                 | 700 ms: 1.36x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.36x faster                                                       |
| async_tree_none         | 717 ms                                                 | 527 ms: 1.36x faster                                                         |
| django_template         | 45.9 ms                                                | 33.9 ms: 1.36x faster                                                        |
| logging_format          | 8.91 us                                                | 6.58 us: 1.35x faster                                                        |
| genshi_text             | 30.3 ms                                                | 22.5 ms: 1.35x faster                                                        |
| pycparser               | 1.50 sec                                               | 1.12 sec: 1.35x faster                                                       |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                        |
| logging_simple          | 8.07 us                                                | 6.05 us: 1.33x faster                                                        |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                         |
| xml_etree_process       | 74.9 ms                                                | 56.5 ms: 1.33x faster                                                        |
| deepcopy                | 442 us                                                 | 333 us: 1.33x faster                                                         |
| coroutines              | 31.8 ms                                                | 24.1 ms: 1.32x faster                                                        |
| async_tree_memoization  | 854 ms                                                 | 651 ms: 1.31x faster                                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.17 ms: 1.31x faster                                                        |
| genshi_xml              | 63.3 ms                                                | 48.5 ms: 1.31x faster                                                        |
| regex_compile           | 177 ms                                                 | 136 ms: 1.31x faster                                                         |
| thrift                  | 1.03 ms                                                | 795 us: 1.30x faster                                                         |
| async_tree_cpu_io_mixed | 951 ms                                                 | 740 ms: 1.28x faster                                                         |
| mypy2                   | 428 ms                                                 | 335 ms: 1.28x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                | 51.6 ms: 1.27x faster                                                        |
| fannkuch                | 486 ms                                                 | 384 ms: 1.26x faster                                                         |
| deepcopy_reduce         | 3.82 us                                                | 3.04 us: 1.26x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 108 ms: 1.26x faster                                                         |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                       |
| nqueens                 | 100 ms                                                 | 80.6 ms: 1.24x faster                                                        |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                                         |
| dulwich_log             | 75.9 ms                                                | 63.6 ms: 1.19x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 794 us: 1.19x faster                                                         |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.18x faster                                                        |
| json_loads              | 28.8 us                                                | 24.5 us: 1.17x faster                                                        |
| sympy_integrate         | 24.3 ms                                                | 20.8 ms: 1.17x faster                                                        |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.1 ms: 1.17x faster                                                        |
| sympy_expand            | 545 ms                                                 | 467 ms: 1.17x faster                                                         |
| json                    | 5.42 ms                                                | 4.65 ms: 1.16x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 81.1 ms: 1.16x faster                                                        |
| sympy_str               | 328 ms                                                 | 288 ms: 1.14x faster                                                         |
| comprehensions          | 26.8 us                                                | 23.7 us: 1.13x faster                                                        |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                                        |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 99.9 ms: 1.12x faster                                                        |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                         |
| djangocms               | 35.9 us                                                | 32.5 us: 1.11x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.55 sec: 1.11x faster                                                       |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| regex_dna               | 222 ms                                                 | 202 ms: 1.10x faster                                                         |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                                        |
| sympy_sum               | 185 ms                                                 | 168 ms: 1.10x faster                                                         |
| pickle_list             | 4.56 us                                                | 4.20 us: 1.09x faster                                                        |
| async_generators        | 425 ms                                                 | 409 ms: 1.04x faster                                                         |
| telco                   | 6.54 ms                                                | 6.48 ms: 1.01x faster                                                        |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                         |
| unpickle_list           | 4.82 us                                                | 4.92 us: 1.02x slower                                                        |
| gc_traversal            | 3.84 ms                                                | 3.93 ms: 1.02x slower                                                        |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                                        |
| regex_effbot            | 3.23 ms                                                | 3.41 ms: 1.06x slower                                                        |
| python_startup_no_site  | 5.82 ms                                                | 6.34 ms: 1.09x slower                                                        |
| pickle_dict             | 27.3 us                                                | 31.7 us: 1.16x slower                                                        |
| dask                    | 423 ms                                                 | 515 ms: 1.22x slower                                                         |
| coverage                | 72.8 ms                                                | 96.3 ms: 1.32x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                 |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x
