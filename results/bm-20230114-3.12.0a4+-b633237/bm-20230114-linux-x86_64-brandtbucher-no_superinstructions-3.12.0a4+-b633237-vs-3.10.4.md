
# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_superinstructions
- machine: linux-x86_64
- commit hash: b633237
- commit date: 2023-01-14
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 255 ms: 1.32x faster                                                         |
| chameleon      | 9.06 ms                                                | 6.49 ms: 1.40x faster                                                        |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                       |
| html5lib       | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                        |
| tornado_http   | 127 ms                                                 | 94.9 ms: 1.34x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.2 ms: 1.53x faster                                                        |
| nbody          | 142 ms                                                 | 94.2 ms: 1.50x faster                                                        |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                         |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                        |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                                         |
| regex_effbot   | 3.23 ms                                                | 3.54 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 287 us: 1.59x faster                                                         |
| unpickle_pure_python | 300 us                                                 | 201 us: 1.50x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.38 ms: 1.44x faster                                                        |
| xml_etree_process    | 74.9 ms                                                | 53.7 ms: 1.39x faster                                                        |
| xml_etree_generate   | 94.2 ms                                                | 77.0 ms: 1.22x faster                                                        |
| json_loads           | 28.8 us                                                | 24.1 us: 1.20x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.02 us: 1.13x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| unpickle             | 14.1 us                                                | 12.9 us: 1.10x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                                         |
| pickle               | 10.3 us                                                | 10.0 us: 1.02x faster                                                        |
| unpickle_list        | 4.82 us                                                | 4.91 us: 1.02x slower                                                        |
| pickle_dict          | 27.3 us                                                | 29.5 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.74 ms: 1.62x faster                                                        |
| python_startup_no_site | 5.82 ms                                                | 6.30 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.22x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.89 ms: 1.49x faster                                                        |
| genshi_text     | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                        |
| django_template | 45.9 ms                                                | 32.7 ms: 1.40x faster                                                        |
| genshi_xml      | 63.3 ms                                                | 47.1 ms: 1.34x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.23 ms: 2.30x faster                                                        |
| logging_silent          | 175 ns                                                 | 91.7 ns: 1.91x faster                                                        |
| asyncio_tcp             | 925 ms                                                 | 504 ms: 1.84x faster                                                         |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                         |
| richards                | 74.9 ms                                                | 44.0 ms: 1.70x faster                                                        |
| pyflate                 | 673 ms                                                 | 398 ms: 1.69x faster                                                         |
| go                      | 229 ms                                                 | 137 ms: 1.68x faster                                                         |
| scimark_monte_carlo     | 108 ms                                                 | 66.1 ms: 1.64x faster                                                        |
| python_startup          | 14.2 ms                                                | 8.74 ms: 1.62x faster                                                        |
| raytrace                | 464 ms                                                 | 288 ms: 1.61x faster                                                         |
| pickle_pure_python      | 455 us                                                 | 287 us: 1.59x faster                                                         |
| hexiom                  | 9.53 ms                                                | 6.18 ms: 1.54x faster                                                        |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.53x faster                                                         |
| float                   | 111 ms                                                 | 72.2 ms: 1.53x faster                                                        |
| spectral_norm           | 150 ms                                                 | 98.0 ms: 1.53x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 77.7 ms: 1.52x faster                                                        |
| chaos                   | 106 ms                                                 | 70.4 ms: 1.51x faster                                                        |
| nbody                   | 142 ms                                                 | 94.2 ms: 1.50x faster                                                        |
| unpickle_pure_python    | 300 us                                                 | 201 us: 1.50x faster                                                         |
| mako                    | 14.8 ms                                                | 9.89 ms: 1.49x faster                                                        |
| genshi_text             | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                        |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.47x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 36.1 us: 1.45x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.38 ms: 1.44x faster                                                        |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                                        |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                                       |
| html5lib                | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                        |
| pprint_safe_repr        | 955 ms                                                 | 676 ms: 1.41x faster                                                         |
| django_template         | 45.9 ms                                                | 32.7 ms: 1.40x faster                                                        |
| chameleon               | 9.06 ms                                                | 6.49 ms: 1.40x faster                                                        |
| xml_etree_process       | 74.9 ms                                                | 53.7 ms: 1.39x faster                                                        |
| logging_simple          | 8.07 us                                                | 5.82 us: 1.39x faster                                                        |
| thrift                  | 1.03 ms                                                | 750 us: 1.38x faster                                                         |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                                        |
| logging_format          | 8.91 us                                                | 6.52 us: 1.37x faster                                                        |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                                       |
| async_tree_none         | 717 ms                                                 | 530 ms: 1.35x faster                                                         |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                        |
| genshi_xml              | 63.3 ms                                                | 47.1 ms: 1.34x faster                                                        |
| tornado_http            | 127 ms                                                 | 94.9 ms: 1.34x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                                       |
| scimark_fft             | 424 ms                                                 | 317 ms: 1.34x faster                                                         |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.13 ms: 1.32x faster                                                        |
| unpack_sequence         | 64.7 ns                                                | 49.0 ns: 1.32x faster                                                        |
| 2to3                    | 336 ms                                                 | 255 ms: 1.32x faster                                                         |
| deepcopy                | 442 us                                                 | 336 us: 1.31x faster                                                         |
| async_tree_memoization  | 854 ms                                                 | 658 ms: 1.30x faster                                                         |
| fannkuch                | 486 ms                                                 | 374 ms: 1.30x faster                                                         |
| deepcopy_reduce         | 3.82 us                                                | 2.95 us: 1.29x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                | 51.4 ms: 1.27x faster                                                        |
| coroutines              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                 | 749 ms: 1.27x faster                                                         |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                       |
| nqueens                 | 100 ms                                                 | 79.4 ms: 1.26x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 77.0 ms: 1.22x faster                                                        |
| dulwich_log             | 75.9 ms                                                | 62.4 ms: 1.22x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 784 us: 1.21x faster                                                         |
| json_loads              | 28.8 us                                                | 24.1 us: 1.20x faster                                                        |
| async_generators        | 425 ms                                                 | 356 ms: 1.19x faster                                                         |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.18x faster                                                        |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                        |
| sympy_expand            | 545 ms                                                 | 466 ms: 1.17x faster                                                         |
| create_gc_cycles        | 1.67 ms                                                | 1.44 ms: 1.16x faster                                                        |
| json                    | 5.42 ms                                                | 4.71 ms: 1.15x faster                                                        |
| sympy_str               | 328 ms                                                 | 288 ms: 1.14x faster                                                         |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                                        |
| pickle_list             | 4.56 us                                                | 4.02 us: 1.13x faster                                                        |
| sympy_sum               | 185 ms                                                 | 165 ms: 1.12x faster                                                         |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                         |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| unpickle                | 14.1 us                                                | 12.9 us: 1.10x faster                                                        |
| gc_traversal            | 3.84 ms                                                | 3.50 ms: 1.10x faster                                                        |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                                        |
| djangocms               | 35.9 us                                                | 32.9 us: 1.09x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.61 sec: 1.08x faster                                                       |
| regex_dna               | 222 ms                                                 | 207 ms: 1.07x faster                                                         |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.06x faster                                                         |
| generators              | 76.8 ms                                                | 74.6 ms: 1.03x faster                                                        |
| pickle                  | 10.3 us                                                | 10.0 us: 1.02x faster                                                        |
| telco                   | 6.54 ms                                                | 6.43 ms: 1.02x faster                                                        |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                         |
| unpickle_list           | 4.82 us                                                | 4.91 us: 1.02x slower                                                        |
| pickle_dict             | 27.3 us                                                | 29.5 us: 1.08x slower                                                        |
| python_startup_no_site  | 5.82 ms                                                | 6.30 ms: 1.08x slower                                                        |
| regex_effbot            | 3.23 ms                                                | 3.54 ms: 1.10x slower                                                        |
| dask                    | 423 ms                                                 | 507 ms: 1.20x slower                                                         |
| coverage                | 72.8 ms                                                | 96.2 ms: 1.32x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230114-3.12.0a4+-b633237/bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x
