
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: afbac86
- commit date: 2023-01-17
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                                        |
| chameleon      | 9.06 ms                                                | 6.39 ms: 1.42x faster                                                       |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                      |
| html5lib       | 85.9 ms                                                | 60.3 ms: 1.42x faster                                                       |
| tornado_http   | 127 ms                                                 | 93.8 ms: 1.36x faster                                                       |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 73.0 ms: 1.51x faster                                                       |
| nbody          | 142 ms                                                 | 94.5 ms: 1.50x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                        |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                       |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.48 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 288 us: 1.58x faster                                                        |
| unpickle_pure_python | 300 us                                                 | 204 us: 1.48x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.35 ms: 1.45x faster                                                       |
| xml_etree_process    | 74.9 ms                                                | 54.4 ms: 1.38x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 78.0 ms: 1.21x faster                                                       |
| json_loads           | 28.8 us                                                | 24.1 us: 1.20x faster                                                       |
| pickle_list          | 4.56 us                                                | 4.00 us: 1.14x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                                        |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                        |
| pickle               | 10.3 us                                                | 9.93 us: 1.04x faster                                                       |
| unpickle_list        | 4.82 us                                                | 5.06 us: 1.05x slower                                                       |
| pickle_dict          | 27.3 us                                                | 29.9 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.89 ms: 1.59x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.42 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.65 ms: 1.53x faster                                                       |
| genshi_text     | 30.3 ms                                                | 20.9 ms: 1.45x faster                                                       |
| django_template | 45.9 ms                                                | 32.0 ms: 1.43x faster                                                       |
| genshi_xml      | 63.3 ms                                                | 47.4 ms: 1.33x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.22 ms: 2.30x faster                                                       |
| logging_silent          | 175 ns                                                 | 91.2 ns: 1.92x faster                                                       |
| asyncio_tcp             | 925 ms                                                 | 496 ms: 1.87x faster                                                        |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                        |
| richards                | 74.9 ms                                                | 43.0 ms: 1.74x faster                                                       |
| pyflate                 | 673 ms                                                 | 404 ms: 1.67x faster                                                        |
| go                      | 229 ms                                                 | 138 ms: 1.66x faster                                                        |
| scimark_monte_carlo     | 108 ms                                                 | 65.2 ms: 1.66x faster                                                       |
| chaos                   | 106 ms                                                 | 64.3 ms: 1.65x faster                                                       |
| raytrace                | 464 ms                                                 | 284 ms: 1.63x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 73.2 ms: 1.62x faster                                                       |
| spectral_norm           | 150 ms                                                 | 93.8 ms: 1.60x faster                                                       |
| hexiom                  | 9.53 ms                                                | 5.98 ms: 1.59x faster                                                       |
| python_startup          | 14.2 ms                                                | 8.89 ms: 1.59x faster                                                       |
| pickle_pure_python      | 455 us                                                 | 288 us: 1.58x faster                                                        |
| unpack_sequence         | 64.7 ns                                                | 41.4 ns: 1.56x faster                                                       |
| mako                    | 14.8 ms                                                | 9.65 ms: 1.53x faster                                                       |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 34.5 us: 1.52x faster                                                       |
| float                   | 111 ms                                                 | 73.0 ms: 1.51x faster                                                       |
| nbody                   | 142 ms                                                 | 94.5 ms: 1.50x faster                                                       |
| unpickle_pure_python    | 300 us                                                 | 204 us: 1.48x faster                                                        |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.47x faster                                                       |
| genshi_text             | 30.3 ms                                                | 20.9 ms: 1.45x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.35 ms: 1.45x faster                                                       |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                                       |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                                      |
| django_template         | 45.9 ms                                                | 32.0 ms: 1.43x faster                                                       |
| html5lib                | 85.9 ms                                                | 60.3 ms: 1.42x faster                                                       |
| pprint_safe_repr        | 955 ms                                                 | 671 ms: 1.42x faster                                                        |
| chameleon               | 9.06 ms                                                | 6.39 ms: 1.42x faster                                                       |
| thrift                  | 1.03 ms                                                | 739 us: 1.40x faster                                                        |
| logging_simple          | 8.07 us                                                | 5.82 us: 1.39x faster                                                       |
| scimark_fft             | 424 ms                                                 | 306 ms: 1.38x faster                                                        |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                                       |
| logging_format          | 8.91 us                                                | 6.45 us: 1.38x faster                                                       |
| xml_etree_process       | 74.9 ms                                                | 54.4 ms: 1.38x faster                                                       |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                        |
| async_tree_none         | 717 ms                                                 | 525 ms: 1.37x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.00 ms: 1.36x faster                                                       |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                                       |
| tornado_http            | 127 ms                                                 | 93.8 ms: 1.36x faster                                                       |
| deepcopy                | 442 us                                                 | 328 us: 1.35x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                                      |
| genshi_xml              | 63.3 ms                                                | 47.4 ms: 1.33x faster                                                       |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                                        |
| nqueens                 | 100 ms                                                 | 76.6 ms: 1.31x faster                                                       |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                      |
| deepcopy_reduce         | 3.82 us                                                | 2.95 us: 1.30x faster                                                       |
| async_tree_memoization  | 854 ms                                                 | 659 ms: 1.30x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                        |
| fannkuch                | 486 ms                                                 | 376 ms: 1.29x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                       |
| coroutines              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                       |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                      |
| async_tree_cpu_io_mixed | 951 ms                                                 | 752 ms: 1.26x faster                                                        |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.22x faster                                                       |
| dulwich_log             | 75.9 ms                                                | 62.2 ms: 1.22x faster                                                       |
| sympy_str               | 328 ms                                                 | 269 ms: 1.22x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 778 us: 1.22x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 78.0 ms: 1.21x faster                                                       |
| async_generators        | 425 ms                                                 | 354 ms: 1.20x faster                                                        |
| sympy_expand            | 545 ms                                                 | 454 ms: 1.20x faster                                                        |
| json_loads              | 28.8 us                                                | 24.1 us: 1.20x faster                                                       |
| sympy_sum               | 185 ms                                                 | 155 ms: 1.19x faster                                                        |
| json                    | 5.42 ms                                                | 4.66 ms: 1.16x faster                                                       |
| sqlite_synth            | 2.93 us                                                | 2.56 us: 1.14x faster                                                       |
| pickle_list             | 4.56 us                                                | 4.00 us: 1.14x faster                                                       |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                       |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                       |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                       |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                                       |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.56 sec: 1.10x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                                        |
| regex_dna               | 222 ms                                                 | 207 ms: 1.07x faster                                                        |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                                        |
| pickle                  | 10.3 us                                                | 9.93 us: 1.04x faster                                                       |
| telco                   | 6.54 ms                                                | 6.35 ms: 1.03x faster                                                       |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| generators              | 76.8 ms                                                | 76.6 ms: 1.00x faster                                                       |
| unpickle_list           | 4.82 us                                                | 5.06 us: 1.05x slower                                                       |
| regex_effbot            | 3.23 ms                                                | 3.48 ms: 1.08x slower                                                       |
| pickle_dict             | 27.3 us                                                | 29.9 us: 1.10x slower                                                       |
| python_startup_no_site  | 5.82 ms                                                | 6.42 ms: 1.10x slower                                                       |
| gc_traversal            | 3.84 ms                                                | 4.29 ms: 1.12x slower                                                       |
| dask                    | 423 ms                                                 | 497 ms: 1.18x slower                                                        |
| coverage                | 72.8 ms                                                | 93.1 ms: 1.28x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230117-3.12.0a4+-afbac86/bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.27x
