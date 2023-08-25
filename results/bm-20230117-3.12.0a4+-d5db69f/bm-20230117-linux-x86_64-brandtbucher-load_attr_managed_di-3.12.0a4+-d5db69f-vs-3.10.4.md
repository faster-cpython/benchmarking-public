
# Results vs. 3.10.4

- fork: brandtbucher
- ref: load_attr_managed_di
- machine: linux-x86_64
- commit hash: d5db69f
- commit date: 2023-01-17
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 250 ms: 1.34x faster                                                         |
| chameleon      | 9.06 ms                                                | 6.37 ms: 1.42x faster                                                        |
| docutils       | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                       |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                        |
| tornado_http   | 127 ms                                                 | 94.0 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.7 ms: 1.53x faster                                                        |
| float          | 111 ms                                                 | 72.8 ms: 1.52x faster                                                        |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 126 ms: 1.40x faster                                                         |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                        |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                                         |
| regex_effbot   | 3.23 ms                                                | 3.60 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 284 us: 1.60x faster                                                         |
| unpickle_pure_python | 300 us                                                 | 196 us: 1.53x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.42 ms: 1.44x faster                                                        |
| xml_etree_process    | 74.9 ms                                                | 53.5 ms: 1.40x faster                                                        |
| xml_etree_generate   | 94.2 ms                                                | 77.3 ms: 1.22x faster                                                        |
| json_loads           | 28.8 us                                                | 23.9 us: 1.21x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.08 us: 1.12x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                                         |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                                        |
| unpickle_list        | 4.82 us                                                | 5.07 us: 1.05x slower                                                        |
| pickle_dict          | 27.3 us                                                | 31.0 us: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.97 ms: 1.58x faster                                                        |
| python_startup_no_site | 5.82 ms                                                | 6.49 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.56 ms: 1.54x faster                                                        |
| genshi_text     | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                        |
| django_template | 45.9 ms                                                | 33.2 ms: 1.38x faster                                                        |
| genshi_xml      | 63.3 ms                                                | 46.8 ms: 1.35x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.32x faster                                                        |
| logging_silent          | 175 ns                                                 | 92.1 ns: 1.90x faster                                                        |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                                         |
| asyncio_tcp             | 925 ms                                                 | 498 ms: 1.86x faster                                                         |
| richards                | 74.9 ms                                                | 43.1 ms: 1.74x faster                                                        |
| pyflate                 | 673 ms                                                 | 405 ms: 1.66x faster                                                         |
| scimark_monte_carlo     | 108 ms                                                 | 65.5 ms: 1.65x faster                                                        |
| chaos                   | 106 ms                                                 | 64.7 ms: 1.64x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 73.0 ms: 1.62x faster                                                        |
| raytrace                | 464 ms                                                 | 286 ms: 1.62x faster                                                         |
| pickle_pure_python      | 455 us                                                 | 284 us: 1.60x faster                                                         |
| hexiom                  | 9.53 ms                                                | 5.99 ms: 1.59x faster                                                        |
| python_startup          | 14.2 ms                                                | 8.97 ms: 1.58x faster                                                        |
| unpack_sequence         | 64.7 ns                                                | 41.7 ns: 1.55x faster                                                        |
| scimark_lu              | 163 ms                                                 | 105 ms: 1.55x faster                                                         |
| mako                    | 14.8 ms                                                | 9.56 ms: 1.54x faster                                                        |
| unpickle_pure_python    | 300 us                                                 | 196 us: 1.53x faster                                                         |
| deepcopy_memo           | 52.3 us                                                | 34.2 us: 1.53x faster                                                        |
| nbody                   | 142 ms                                                 | 92.7 ms: 1.53x faster                                                        |
| float                   | 111 ms                                                 | 72.8 ms: 1.52x faster                                                        |
| spectral_norm           | 150 ms                                                 | 99.2 ms: 1.51x faster                                                        |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                                        |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                        |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.42 ms: 1.44x faster                                                        |
| logging_format          | 8.91 us                                                | 6.20 us: 1.44x faster                                                        |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                                       |
| genshi_text             | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                        |
| logging_simple          | 8.07 us                                                | 5.65 us: 1.43x faster                                                        |
| pprint_safe_repr        | 955 ms                                                 | 671 ms: 1.42x faster                                                         |
| chameleon               | 9.06 ms                                                | 6.37 ms: 1.42x faster                                                        |
| scimark_fft             | 424 ms                                                 | 303 ms: 1.40x faster                                                         |
| regex_compile           | 177 ms                                                 | 126 ms: 1.40x faster                                                         |
| xml_etree_process       | 74.9 ms                                                | 53.5 ms: 1.40x faster                                                        |
| aiohttp                 | 1.38 ms                                                | 990 us: 1.40x faster                                                         |
| thrift                  | 1.03 ms                                                | 742 us: 1.39x faster                                                         |
| async_tree_memoization  | 854 ms                                                 | 616 ms: 1.39x faster                                                         |
| django_template         | 45.9 ms                                                | 33.2 ms: 1.38x faster                                                        |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.37x faster                                                        |
| async_tree_none         | 717 ms                                                 | 525 ms: 1.37x faster                                                         |
| deepcopy                | 442 us                                                 | 325 us: 1.36x faster                                                         |
| tornado_http            | 127 ms                                                 | 94.0 ms: 1.36x faster                                                        |
| genshi_xml              | 63.3 ms                                                | 46.8 ms: 1.35x faster                                                        |
| 2to3                    | 336 ms                                                 | 250 ms: 1.34x faster                                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.06 ms: 1.34x faster                                                        |
| pycparser               | 1.50 sec                                               | 1.12 sec: 1.34x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.34x faster                                                       |
| deepcopy_reduce         | 3.82 us                                                | 2.94 us: 1.30x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                         |
| go                      | 229 ms                                                 | 178 ms: 1.29x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                                        |
| fannkuch                | 486 ms                                                 | 382 ms: 1.27x faster                                                         |
| nqueens                 | 100 ms                                                 | 78.6 ms: 1.27x faster                                                        |
| docutils                | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                       |
| coroutines              | 31.8 ms                                                | 25.3 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                 | 761 ms: 1.25x faster                                                         |
| sympy_integrate         | 24.3 ms                                                | 19.6 ms: 1.24x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 773 us: 1.23x faster                                                         |
| sympy_str               | 328 ms                                                 | 268 ms: 1.23x faster                                                         |
| dulwich_log             | 75.9 ms                                                | 62.3 ms: 1.22x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 77.3 ms: 1.22x faster                                                        |
| sympy_expand            | 545 ms                                                 | 449 ms: 1.21x faster                                                         |
| json_loads              | 28.8 us                                                | 23.9 us: 1.21x faster                                                        |
| async_generators        | 425 ms                                                 | 353 ms: 1.21x faster                                                         |
| sympy_sum               | 185 ms                                                 | 154 ms: 1.20x faster                                                         |
| json                    | 5.42 ms                                                | 4.56 ms: 1.19x faster                                                        |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                        |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                        |
| sqlite_synth            | 2.93 us                                                | 2.61 us: 1.13x faster                                                        |
| pickle_list             | 4.56 us                                                | 4.08 us: 1.12x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                        |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                         |
| mdp                     | 2.82 sec                                               | 2.57 sec: 1.10x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.09x faster                                                         |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                                        |
| regex_dna               | 222 ms                                                 | 208 ms: 1.07x faster                                                         |
| telco                   | 6.54 ms                                                | 6.41 ms: 1.02x faster                                                        |
| gc_traversal            | 3.84 ms                                                | 3.81 ms: 1.01x faster                                                        |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                         |
| unpickle_list           | 4.82 us                                                | 5.07 us: 1.05x slower                                                        |
| regex_effbot            | 3.23 ms                                                | 3.60 ms: 1.11x slower                                                        |
| python_startup_no_site  | 5.82 ms                                                | 6.49 ms: 1.12x slower                                                        |
| pickle_dict             | 27.3 us                                                | 31.0 us: 1.14x slower                                                        |
| dask                    | 423 ms                                                 | 504 ms: 1.19x slower                                                         |
| coverage                | 72.8 ms                                                | 97.1 ms: 1.33x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (3): pickle, generators, bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230117-3.12.0a4+-d5db69f/bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x
