
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 697dc1e
- commit date: 2023-01-15
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                        |
| chameleon      | 9.06 ms                                                | 6.35 ms: 1.43x faster                                                       |
| docutils       | 3.17 sec                                               | 2.48 sec: 1.28x faster                                                      |
| html5lib       | 85.9 ms                                                | 60.4 ms: 1.42x faster                                                       |
| tornado_http   | 127 ms                                                 | 93.8 ms: 1.36x faster                                                       |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 71.5 ms: 1.55x faster                                                       |
| nbody          | 142 ms                                                 | 94.8 ms: 1.49x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                        |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.16x faster                                                       |
| regex_dna      | 222 ms                                                 | 211 ms: 1.05x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.51 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 279 us: 1.63x faster                                                        |
| unpickle_pure_python | 300 us                                                 | 196 us: 1.53x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.34 ms: 1.45x faster                                                       |
| xml_etree_process    | 74.9 ms                                                | 54.1 ms: 1.38x faster                                                       |
| json_loads           | 28.8 us                                                | 23.9 us: 1.21x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 78.8 ms: 1.19x faster                                                       |
| pickle_list          | 4.56 us                                                | 4.06 us: 1.12x faster                                                       |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 157 ms: 1.04x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 109 ms: 1.02x faster                                                        |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                       |
| unpickle_list        | 4.82 us                                                | 5.01 us: 1.04x slower                                                       |
| pickle_dict          | 27.3 us                                                | 29.9 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.68 ms: 1.63x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.22 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.63 ms: 1.53x faster                                                       |
| genshi_text     | 30.3 ms                                                | 20.1 ms: 1.51x faster                                                       |
| django_template | 45.9 ms                                                | 32.0 ms: 1.43x faster                                                       |
| genshi_xml      | 63.3 ms                                                | 46.1 ms: 1.37x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.33x faster                                                       |
| asyncio_tcp             | 925 ms                                                 | 485 ms: 1.91x faster                                                        |
| logging_silent          | 175 ns                                                 | 93.8 ns: 1.87x faster                                                       |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                        |
| richards                | 74.9 ms                                                | 42.0 ms: 1.78x faster                                                       |
| go                      | 229 ms                                                 | 131 ms: 1.75x faster                                                        |
| pyflate                 | 673 ms                                                 | 404 ms: 1.67x faster                                                        |
| raytrace                | 464 ms                                                 | 283 ms: 1.64x faster                                                        |
| pickle_pure_python      | 455 us                                                 | 279 us: 1.63x faster                                                        |
| python_startup          | 14.2 ms                                                | 8.68 ms: 1.63x faster                                                       |
| scimark_monte_carlo     | 108 ms                                                 | 66.4 ms: 1.63x faster                                                       |
| chaos                   | 106 ms                                                 | 65.5 ms: 1.62x faster                                                       |
| crypto_pyaes            | 118 ms                                                 | 73.3 ms: 1.62x faster                                                       |
| hexiom                  | 9.53 ms                                                | 6.03 ms: 1.58x faster                                                       |
| spectral_norm           | 150 ms                                                 | 96.0 ms: 1.56x faster                                                       |
| float                   | 111 ms                                                 | 71.5 ms: 1.55x faster                                                       |
| mako                    | 14.8 ms                                                | 9.63 ms: 1.53x faster                                                       |
| unpickle_pure_python    | 300 us                                                 | 196 us: 1.53x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 34.4 us: 1.52x faster                                                       |
| genshi_text             | 30.3 ms                                                | 20.1 ms: 1.51x faster                                                       |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                                        |
| nbody                   | 142 ms                                                 | 94.8 ms: 1.49x faster                                                       |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.47x faster                                                       |
| sqlglot_transpile       | 2.45 ms                                                | 1.68 ms: 1.45x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.34 ms: 1.45x faster                                                       |
| unpack_sequence         | 64.7 ns                                                | 44.9 ns: 1.44x faster                                                       |
| django_template         | 45.9 ms                                                | 32.0 ms: 1.43x faster                                                       |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                                      |
| logging_simple          | 8.07 us                                                | 5.65 us: 1.43x faster                                                       |
| chameleon               | 9.06 ms                                                | 6.35 ms: 1.43x faster                                                       |
| pprint_safe_repr        | 955 ms                                                 | 670 ms: 1.43x faster                                                        |
| logging_format          | 8.91 us                                                | 6.26 us: 1.42x faster                                                       |
| html5lib                | 85.9 ms                                                | 60.4 ms: 1.42x faster                                                       |
| thrift                  | 1.03 ms                                                | 742 us: 1.39x faster                                                        |
| xml_etree_process       | 74.9 ms                                                | 54.1 ms: 1.38x faster                                                       |
| aiohttp                 | 1.38 ms                                                | 999 us: 1.38x faster                                                        |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                        |
| scimark_fft             | 424 ms                                                 | 308 ms: 1.37x faster                                                        |
| genshi_xml              | 63.3 ms                                                | 46.1 ms: 1.37x faster                                                       |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                                        |
| deepcopy                | 442 us                                                 | 324 us: 1.36x faster                                                        |
| tornado_http            | 127 ms                                                 | 93.8 ms: 1.36x faster                                                       |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                                      |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.35x faster                                                      |
| fannkuch                | 486 ms                                                 | 362 ms: 1.34x faster                                                        |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                        |
| deepcopy_reduce         | 3.82 us                                                | 2.89 us: 1.32x faster                                                       |
| sqlglot_normalize       | 135 ms                                                 | 103 ms: 1.31x faster                                                        |
| async_tree_memoization  | 854 ms                                                 | 655 ms: 1.30x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                | 50.2 ms: 1.30x faster                                                       |
| coroutines              | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                       |
| docutils                | 3.17 sec                                               | 2.48 sec: 1.28x faster                                                      |
| nqueens                 | 100 ms                                                 | 78.5 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed | 951 ms                                                 | 751 ms: 1.27x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 774 us: 1.22x faster                                                        |
| dulwich_log             | 75.9 ms                                                | 62.1 ms: 1.22x faster                                                       |
| async_generators        | 425 ms                                                 | 348 ms: 1.22x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.47 ms: 1.22x faster                                                       |
| json_loads              | 28.8 us                                                | 23.9 us: 1.21x faster                                                       |
| sympy_expand            | 545 ms                                                 | 452 ms: 1.21x faster                                                        |
| sympy_integrate         | 24.3 ms                                                | 20.2 ms: 1.20x faster                                                       |
| xml_etree_generate      | 94.2 ms                                                | 78.8 ms: 1.19x faster                                                       |
| json                    | 5.42 ms                                                | 4.59 ms: 1.18x faster                                                       |
| sympy_str               | 328 ms                                                 | 281 ms: 1.17x faster                                                        |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.16x faster                                                       |
| create_gc_cycles        | 1.67 ms                                                | 1.45 ms: 1.16x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.47 sec: 1.14x faster                                                      |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                                       |
| sympy_sum               | 185 ms                                                 | 162 ms: 1.14x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                                       |
| pickle_list             | 4.56 us                                                | 4.06 us: 1.12x faster                                                       |
| djangocms               | 35.9 us                                                | 32.5 us: 1.11x faster                                                       |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                        |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                                       |
| regex_dna               | 222 ms                                                 | 211 ms: 1.05x faster                                                        |
| telco                   | 6.54 ms                                                | 6.26 ms: 1.05x faster                                                       |
| xml_etree_parse         | 163 ms                                                 | 157 ms: 1.04x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 109 ms: 1.02x faster                                                        |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                       |
| generators              | 76.8 ms                                                | 75.9 ms: 1.01x faster                                                       |
| gc_traversal            | 3.84 ms                                                | 3.81 ms: 1.01x faster                                                       |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| unpickle_list           | 4.82 us                                                | 5.01 us: 1.04x slower                                                       |
| python_startup_no_site  | 5.82 ms                                                | 6.22 ms: 1.07x slower                                                       |
| regex_effbot            | 3.23 ms                                                | 3.51 ms: 1.09x slower                                                       |
| pickle_dict             | 27.3 us                                                | 29.9 us: 1.10x slower                                                       |
| dask                    | 423 ms                                                 | 492 ms: 1.16x slower                                                        |
| coverage                | 72.8 ms                                                | 96.0 ms: 1.32x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230115-3.12.0a4+-697dc1e/bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
