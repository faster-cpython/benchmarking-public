
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 57469f4
- commit date: 2023-01-28
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 254 ms: 1.32x faster                                                       |
| chameleon      | 9.06 ms                                                | 6.40 ms: 1.42x faster                                                      |
| docutils       | 3.17 sec                                               | 2.51 sec: 1.26x faster                                                     |
| html5lib       | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                      |
| tornado_http   | 127 ms                                                 | 94.3 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.3 ms: 1.53x faster                                                      |
| float          | 111 ms                                                 | 75.1 ms: 1.47x faster                                                      |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.31x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.35x faster                                                       |
| regex_v8       | 25.0 ms                                                | 22.7 ms: 1.10x faster                                                      |
| regex_dna      | 222 ms                                                 | 219 ms: 1.01x faster                                                       |
| regex_effbot   | 3.23 ms                                                | 3.60 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 292 us: 1.56x faster                                                       |
| unpickle_pure_python | 300 us                                                 | 208 us: 1.44x faster                                                       |
| json_dumps           | 13.5 ms                                                | 9.40 ms: 1.44x faster                                                      |
| xml_etree_process    | 74.9 ms                                                | 53.6 ms: 1.40x faster                                                      |
| xml_etree_generate   | 94.2 ms                                                | 77.5 ms: 1.21x faster                                                      |
| json_loads           | 28.8 us                                                | 23.9 us: 1.20x faster                                                      |
| pickle_list          | 4.56 us                                                | 4.06 us: 1.12x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                       |
| pickle               | 10.3 us                                                | 9.98 us: 1.03x faster                                                      |
| unpickle_list        | 4.82 us                                                | 5.07 us: 1.05x slower                                                      |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.70 ms: 1.63x faster                                                      |
| python_startup_no_site | 5.82 ms                                                | 6.23 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.23x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.44 ms: 1.56x faster                                                      |
| genshi_text     | 30.3 ms                                                | 20.6 ms: 1.47x faster                                                      |
| django_template | 45.9 ms                                                | 32.4 ms: 1.42x faster                                                      |
| genshi_xml      | 63.3 ms                                                | 46.4 ms: 1.36x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.35 ms: 2.21x faster                                                      |
| logging_silent          | 175 ns                                                 | 90.2 ns: 1.94x faster                                                      |
| asyncio_tcp             | 925 ms                                                 | 496 ms: 1.86x faster                                                       |
| richards                | 74.9 ms                                                | 42.9 ms: 1.75x faster                                                      |
| scimark_sor             | 197 ms                                                 | 118 ms: 1.66x faster                                                       |
| raytrace                | 464 ms                                                 | 282 ms: 1.64x faster                                                       |
| go                      | 229 ms                                                 | 140 ms: 1.63x faster                                                       |
| crypto_pyaes            | 118 ms                                                 | 72.6 ms: 1.63x faster                                                      |
| python_startup          | 14.2 ms                                                | 8.70 ms: 1.63x faster                                                      |
| chaos                   | 106 ms                                                 | 65.9 ms: 1.61x faster                                                      |
| scimark_monte_carlo     | 108 ms                                                 | 67.3 ms: 1.61x faster                                                      |
| mako                    | 14.8 ms                                                | 9.44 ms: 1.56x faster                                                      |
| spectral_norm           | 150 ms                                                 | 96.1 ms: 1.56x faster                                                      |
| pickle_pure_python      | 455 us                                                 | 292 us: 1.56x faster                                                       |
| pyflate                 | 673 ms                                                 | 432 ms: 1.56x faster                                                       |
| unpack_sequence         | 64.7 ns                                                | 41.7 ns: 1.55x faster                                                      |
| scimark_lu              | 163 ms                                                 | 105 ms: 1.55x faster                                                       |
| hexiom                  | 9.53 ms                                                | 6.16 ms: 1.55x faster                                                      |
| deepcopy_memo           | 52.3 us                                                | 34.0 us: 1.54x faster                                                      |
| nbody                   | 142 ms                                                 | 92.3 ms: 1.53x faster                                                      |
| genshi_text             | 30.3 ms                                                | 20.6 ms: 1.47x faster                                                      |
| float                   | 111 ms                                                 | 75.1 ms: 1.47x faster                                                      |
| unpickle_pure_python    | 300 us                                                 | 208 us: 1.44x faster                                                       |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                                      |
| json_dumps              | 13.5 ms                                                | 9.40 ms: 1.44x faster                                                      |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.42x faster                                                      |
| django_template         | 45.9 ms                                                | 32.4 ms: 1.42x faster                                                      |
| chameleon               | 9.06 ms                                                | 6.40 ms: 1.42x faster                                                      |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.41x faster                                                     |
| scimark_fft             | 424 ms                                                 | 302 ms: 1.40x faster                                                       |
| pprint_safe_repr        | 955 ms                                                 | 681 ms: 1.40x faster                                                       |
| logging_simple          | 8.07 us                                                | 5.75 us: 1.40x faster                                                      |
| xml_etree_process       | 74.9 ms                                                | 53.6 ms: 1.40x faster                                                      |
| logging_format          | 8.91 us                                                | 6.37 us: 1.40x faster                                                      |
| html5lib                | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                      |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.94 ms: 1.38x faster                                                      |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                                      |
| async_tree_none         | 717 ms                                                 | 522 ms: 1.37x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.36x faster                                                     |
| genshi_xml              | 63.3 ms                                                | 46.4 ms: 1.36x faster                                                      |
| deepcopy                | 442 us                                                 | 324 us: 1.36x faster                                                       |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                                      |
| regex_compile           | 177 ms                                                 | 131 ms: 1.35x faster                                                       |
| tornado_http            | 127 ms                                                 | 94.3 ms: 1.35x faster                                                      |
| 2to3                    | 336 ms                                                 | 254 ms: 1.32x faster                                                       |
| deepcopy_reduce         | 3.82 us                                                | 2.91 us: 1.31x faster                                                      |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.30x faster                                                     |
| async_tree_memoization  | 854 ms                                                 | 661 ms: 1.29x faster                                                       |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                       |
| nqueens                 | 100 ms                                                 | 78.0 ms: 1.28x faster                                                      |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                      |
| docutils                | 3.17 sec                                               | 2.51 sec: 1.26x faster                                                     |
| fannkuch                | 486 ms                                                 | 385 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed | 951 ms                                                 | 755 ms: 1.26x faster                                                       |
| coroutines              | 31.8 ms                                                | 26.0 ms: 1.22x faster                                                      |
| sympy_str               | 328 ms                                                 | 270 ms: 1.22x faster                                                       |
| sympy_integrate         | 24.3 ms                                                | 20.0 ms: 1.22x faster                                                      |
| xml_etree_generate      | 94.2 ms                                                | 77.5 ms: 1.21x faster                                                      |
| bench_thread_pool       | 947 us                                                 | 783 us: 1.21x faster                                                       |
| dulwich_log             | 75.9 ms                                                | 62.9 ms: 1.21x faster                                                      |
| json_loads              | 28.8 us                                                | 23.9 us: 1.20x faster                                                      |
| sympy_expand            | 545 ms                                                 | 454 ms: 1.20x faster                                                       |
| async_generators        | 425 ms                                                 | 355 ms: 1.20x faster                                                       |
| sympy_sum               | 185 ms                                                 | 156 ms: 1.18x faster                                                       |
| json                    | 5.42 ms                                                | 4.61 ms: 1.17x faster                                                      |
| mdp                     | 2.82 sec                                               | 2.45 sec: 1.15x faster                                                     |
| create_gc_cycles        | 1.67 ms                                                | 1.45 ms: 1.15x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                                      |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                                      |
| pickle_list             | 4.56 us                                                | 4.06 us: 1.12x faster                                                      |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                                      |
| regex_v8                | 25.0 ms                                                | 22.7 ms: 1.10x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                                       |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                                       |
| generators              | 76.8 ms                                                | 74.4 ms: 1.03x faster                                                      |
| telco                   | 6.54 ms                                                | 6.34 ms: 1.03x faster                                                      |
| pickle                  | 10.3 us                                                | 9.98 us: 1.03x faster                                                      |
| gc_traversal            | 3.84 ms                                                | 3.76 ms: 1.02x faster                                                      |
| regex_dna               | 222 ms                                                 | 219 ms: 1.01x faster                                                       |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                       |
| unpickle_list           | 4.82 us                                                | 5.07 us: 1.05x slower                                                      |
| python_startup_no_site  | 5.82 ms                                                | 6.23 ms: 1.07x slower                                                      |
| regex_effbot            | 3.23 ms                                                | 3.60 ms: 1.12x slower                                                      |
| pickle_dict             | 27.3 us                                                | 30.8 us: 1.13x slower                                                      |
| dask                    | 423 ms                                                 | 511 ms: 1.21x slower                                                       |
| coverage                | 72.8 ms                                                | 102 ms: 1.40x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230128-3.12.0a4+-57469f4/bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x
