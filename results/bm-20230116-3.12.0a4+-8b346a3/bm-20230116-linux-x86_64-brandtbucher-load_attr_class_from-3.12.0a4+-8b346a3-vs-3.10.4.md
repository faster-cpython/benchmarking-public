
# Results vs. 3.10.4

- fork: brandtbucher
- ref: load_attr_class_from
- machine: linux-x86_64
- commit hash: 8b346a3
- commit date: 2023-01-16
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                                         |
| chameleon      | 9.06 ms                                                | 6.33 ms: 1.43x faster                                                        |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                       |
| html5lib       | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                        |
| tornado_http   | 127 ms                                                 | 94.4 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 71.8 ms: 1.54x faster                                                        |
| nbody          | 142 ms                                                 | 93.6 ms: 1.51x faster                                                        |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                        |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                                         |
| regex_effbot   | 3.23 ms                                                | 3.47 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 272 us: 1.67x faster                                                         |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.53x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.28 ms: 1.46x faster                                                        |
| xml_etree_process    | 74.9 ms                                                | 54.1 ms: 1.38x faster                                                        |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                                        |
| xml_etree_generate   | 94.2 ms                                                | 78.4 ms: 1.20x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.10 us: 1.11x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                         |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                                        |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                        |
| unpickle_list        | 4.82 us                                                | 5.03 us: 1.04x slower                                                        |
| pickle_dict          | 27.3 us                                                | 30.5 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.93 ms: 1.59x faster                                                        |
| python_startup_no_site | 5.82 ms                                                | 6.46 ms: 1.11x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.58 ms: 1.54x faster                                                        |
| genshi_text     | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                        |
| django_template | 45.9 ms                                                | 32.3 ms: 1.42x faster                                                        |
| genshi_xml      | 63.3 ms                                                | 47.1 ms: 1.35x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                                        |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                                         |
| logging_silent          | 175 ns                                                 | 93.6 ns: 1.87x faster                                                        |
| asyncio_tcp             | 925 ms                                                 | 495 ms: 1.87x faster                                                         |
| richards                | 74.9 ms                                                | 42.3 ms: 1.77x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 67.2 ms: 1.76x faster                                                        |
| scimark_monte_carlo     | 108 ms                                                 | 62.1 ms: 1.74x faster                                                        |
| go                      | 229 ms                                                 | 133 ms: 1.72x faster                                                         |
| pickle_pure_python      | 455 us                                                 | 272 us: 1.67x faster                                                         |
| pyflate                 | 673 ms                                                 | 403 ms: 1.67x faster                                                         |
| chaos                   | 106 ms                                                 | 64.8 ms: 1.64x faster                                                        |
| raytrace                | 464 ms                                                 | 283 ms: 1.64x faster                                                         |
| hexiom                  | 9.53 ms                                                | 5.98 ms: 1.59x faster                                                        |
| python_startup          | 14.2 ms                                                | 8.93 ms: 1.59x faster                                                        |
| spectral_norm           | 150 ms                                                 | 95.9 ms: 1.56x faster                                                        |
| unpack_sequence         | 64.7 ns                                                | 41.6 ns: 1.55x faster                                                        |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.54x faster                                                         |
| mako                    | 14.8 ms                                                | 9.58 ms: 1.54x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 34.0 us: 1.54x faster                                                        |
| float                   | 111 ms                                                 | 71.8 ms: 1.54x faster                                                        |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.53x faster                                                         |
| nbody                   | 142 ms                                                 | 93.6 ms: 1.51x faster                                                        |
| genshi_text             | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.28 ms: 1.46x faster                                                        |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.45x faster                                                        |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                                        |
| chameleon               | 9.06 ms                                                | 6.33 ms: 1.43x faster                                                        |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                                       |
| html5lib                | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                        |
| django_template         | 45.9 ms                                                | 32.3 ms: 1.42x faster                                                        |
| logging_simple          | 8.07 us                                                | 5.69 us: 1.42x faster                                                        |
| logging_format          | 8.91 us                                                | 6.31 us: 1.41x faster                                                        |
| scimark_fft             | 424 ms                                                 | 300 ms: 1.41x faster                                                         |
| pprint_safe_repr        | 955 ms                                                 | 679 ms: 1.41x faster                                                         |
| aiohttp                 | 1.38 ms                                                | 994 us: 1.39x faster                                                         |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                         |
| thrift                  | 1.03 ms                                                | 745 us: 1.39x faster                                                         |
| xml_etree_process       | 74.9 ms                                                | 54.1 ms: 1.38x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.97 ms: 1.37x faster                                                        |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                                         |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.37x faster                                                        |
| async_tree_memoization  | 854 ms                                                 | 629 ms: 1.36x faster                                                         |
| deepcopy                | 442 us                                                 | 326 us: 1.35x faster                                                         |
| tornado_http            | 127 ms                                                 | 94.4 ms: 1.35x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.35x faster                                                       |
| genshi_xml              | 63.3 ms                                                | 47.1 ms: 1.35x faster                                                        |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                                         |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.31x faster                                                       |
| fannkuch                | 486 ms                                                 | 371 ms: 1.31x faster                                                         |
| deepcopy_reduce         | 3.82 us                                                | 2.95 us: 1.30x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                | 50.9 ms: 1.28x faster                                                        |
| nqueens                 | 100 ms                                                 | 78.0 ms: 1.28x faster                                                        |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                       |
| coroutines              | 31.8 ms                                                | 25.3 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                 | 756 ms: 1.26x faster                                                         |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.23x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 774 us: 1.22x faster                                                         |
| sympy_str               | 328 ms                                                 | 269 ms: 1.22x faster                                                         |
| async_generators        | 425 ms                                                 | 349 ms: 1.22x faster                                                         |
| dulwich_log             | 75.9 ms                                                | 62.5 ms: 1.22x faster                                                        |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 78.4 ms: 1.20x faster                                                        |
| sympy_expand            | 545 ms                                                 | 456 ms: 1.19x faster                                                         |
| json                    | 5.42 ms                                                | 4.57 ms: 1.19x faster                                                        |
| sympy_sum               | 185 ms                                                 | 156 ms: 1.18x faster                                                         |
| mdp                     | 2.82 sec                                               | 2.46 sec: 1.15x faster                                                       |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.15x faster                                                        |
| sqlite_synth            | 2.93 us                                                | 2.57 us: 1.14x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                        |
| djangocms               | 35.9 us                                                | 32.1 us: 1.12x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                        |
| pickle_list             | 4.56 us                                                | 4.10 us: 1.11x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                         |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.09x faster                                                         |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                                        |
| regex_dna               | 222 ms                                                 | 210 ms: 1.06x faster                                                         |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                        |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                        |
| generators              | 76.8 ms                                                | 77.2 ms: 1.01x slower                                                        |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                         |
| unpickle_list           | 4.82 us                                                | 5.03 us: 1.04x slower                                                        |
| regex_effbot            | 3.23 ms                                                | 3.47 ms: 1.08x slower                                                        |
| gc_traversal            | 3.84 ms                                                | 4.16 ms: 1.08x slower                                                        |
| python_startup_no_site  | 5.82 ms                                                | 6.46 ms: 1.11x slower                                                        |
| pickle_dict             | 27.3 us                                                | 30.5 us: 1.12x slower                                                        |
| dask                    | 423 ms                                                 | 501 ms: 1.19x slower                                                         |
| coverage                | 72.8 ms                                                | 96.0 ms: 1.32x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                 |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230116-3.12.0a4+-8b346a3/bm-20230116-linux-x86_64-brandtbucher-load_attr_class_from-3.12.0a4+-8b346a3.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
