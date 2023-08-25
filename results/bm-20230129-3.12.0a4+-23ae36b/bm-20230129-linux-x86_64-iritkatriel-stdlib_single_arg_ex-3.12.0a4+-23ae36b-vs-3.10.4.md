
# Results vs. 3.10.4

- fork: iritkatriel
- ref: stdlib_single_arg_ex
- machine: linux-x86_64
- commit hash: 23ae36b
- commit date: 2023-01-29
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                        |
| chameleon      | 9.06 ms                                                | 6.36 ms: 1.43x faster                                                       |
| docutils       | 3.17 sec                                               | 2.48 sec: 1.28x faster                                                      |
| html5lib       | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                       |
| tornado_http   | 127 ms                                                 | 93.8 ms: 1.36x faster                                                       |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 73.8 ms: 1.50x faster                                                       |
| nbody          | 142 ms                                                 | 95.6 ms: 1.48x faster                                                       |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                                        |
| regex_v8       | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                       |
| regex_dna      | 222 ms                                                 | 202 ms: 1.10x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.38 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                                        |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.36 ms: 1.45x faster                                                       |
| xml_etree_process    | 74.9 ms                                                | 53.2 ms: 1.41x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 77.1 ms: 1.22x faster                                                       |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                        |
| unpickle             | 14.1 us                                                | 13.0 us: 1.09x faster                                                       |
| pickle_list          | 4.56 us                                                | 4.22 us: 1.08x faster                                                       |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                       |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.03x slower                                                       |
| pickle_dict          | 27.3 us                                                | 31.0 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.93 ms: 1.58x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.46 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.85 ms: 1.50x faster                                                       |
| genshi_text     | 30.3 ms                                                | 20.3 ms: 1.50x faster                                                       |
| django_template | 45.9 ms                                                | 32.3 ms: 1.42x faster                                                       |
| genshi_xml      | 63.3 ms                                                | 47.5 ms: 1.33x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.20 ms: 2.32x faster                                                       |
| logging_silent          | 175 ns                                                 | 90.0 ns: 1.94x faster                                                       |
| asyncio_tcp             | 925 ms                                                 | 495 ms: 1.87x faster                                                        |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                        |
| richards                | 74.9 ms                                                | 41.9 ms: 1.79x faster                                                       |
| go                      | 229 ms                                                 | 133 ms: 1.72x faster                                                        |
| pyflate                 | 673 ms                                                 | 406 ms: 1.66x faster                                                        |
| raytrace                | 464 ms                                                 | 280 ms: 1.66x faster                                                        |
| chaos                   | 106 ms                                                 | 64.5 ms: 1.65x faster                                                       |
| scimark_monte_carlo     | 108 ms                                                 | 66.1 ms: 1.64x faster                                                       |
| hexiom                  | 9.53 ms                                                | 5.86 ms: 1.63x faster                                                       |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 74.0 ms: 1.60x faster                                                       |
| spectral_norm           | 150 ms                                                 | 94.4 ms: 1.59x faster                                                       |
| python_startup          | 14.2 ms                                                | 8.93 ms: 1.58x faster                                                       |
| deepcopy_memo           | 52.3 us                                                | 34.1 us: 1.54x faster                                                       |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                                        |
| unpack_sequence         | 64.7 ns                                                | 42.5 ns: 1.52x faster                                                       |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                                        |
| float                   | 111 ms                                                 | 73.8 ms: 1.50x faster                                                       |
| mako                    | 14.8 ms                                                | 9.85 ms: 1.50x faster                                                       |
| genshi_text             | 30.3 ms                                                | 20.3 ms: 1.50x faster                                                       |
| nbody                   | 142 ms                                                 | 95.6 ms: 1.48x faster                                                       |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.47x faster                                                       |
| pprint_pformat          | 1.99 sec                                               | 1.36 sec: 1.46x faster                                                      |
| sqlglot_transpile       | 2.45 ms                                                | 1.69 ms: 1.45x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.36 ms: 1.45x faster                                                       |
| html5lib                | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                       |
| chameleon               | 9.06 ms                                                | 6.36 ms: 1.43x faster                                                       |
| pprint_safe_repr        | 955 ms                                                 | 670 ms: 1.42x faster                                                        |
| django_template         | 45.9 ms                                                | 32.3 ms: 1.42x faster                                                       |
| logging_format          | 8.91 us                                                | 6.31 us: 1.41x faster                                                       |
| logging_simple          | 8.07 us                                                | 5.72 us: 1.41x faster                                                       |
| xml_etree_process       | 74.9 ms                                                | 53.2 ms: 1.41x faster                                                       |
| aiohttp                 | 1.38 ms                                                | 992 us: 1.39x faster                                                        |
| scimark_fft             | 424 ms                                                 | 305 ms: 1.39x faster                                                        |
| thrift                  | 1.03 ms                                                | 745 us: 1.39x faster                                                        |
| pycparser               | 1.50 sec                                               | 1.08 sec: 1.39x faster                                                      |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                                        |
| gunicorn                | 1.46 ms                                                | 1.06 ms: 1.37x faster                                                       |
| async_tree_none         | 717 ms                                                 | 522 ms: 1.37x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.36x faster                                                      |
| tornado_http            | 127 ms                                                 | 93.8 ms: 1.36x faster                                                       |
| fannkuch                | 486 ms                                                 | 358 ms: 1.36x faster                                                        |
| async_tree_memoization  | 854 ms                                                 | 630 ms: 1.36x faster                                                        |
| deepcopy                | 442 us                                                 | 327 us: 1.35x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.06 ms: 1.34x faster                                                       |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                        |
| genshi_xml              | 63.3 ms                                                | 47.5 ms: 1.33x faster                                                       |
| deepcopy_reduce         | 3.82 us                                                | 2.95 us: 1.30x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 50.7 ms: 1.29x faster                                                       |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                        |
| coroutines              | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                       |
| docutils                | 3.17 sec                                               | 2.48 sec: 1.28x faster                                                      |
| nqueens                 | 100 ms                                                 | 79.1 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed | 951 ms                                                 | 755 ms: 1.26x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 761 us: 1.24x faster                                                        |
| sympy_integrate         | 24.3 ms                                                | 19.7 ms: 1.23x faster                                                       |
| dulwich_log             | 75.9 ms                                                | 62.1 ms: 1.22x faster                                                       |
| xml_etree_generate      | 94.2 ms                                                | 77.1 ms: 1.22x faster                                                       |
| sympy_str               | 328 ms                                                 | 269 ms: 1.22x faster                                                        |
| async_generators        | 425 ms                                                 | 350 ms: 1.21x faster                                                        |
| sympy_expand            | 545 ms                                                 | 451 ms: 1.21x faster                                                        |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                                       |
| regex_v8                | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                       |
| sympy_sum               | 185 ms                                                 | 156 ms: 1.19x faster                                                        |
| json                    | 5.42 ms                                                | 4.58 ms: 1.18x faster                                                       |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                       |
| djangocms               | 35.9 us                                                | 32.0 us: 1.12x faster                                                       |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                       |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                       |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                        |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                        |
| regex_dna               | 222 ms                                                 | 202 ms: 1.10x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.57 sec: 1.10x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                        |
| unpickle                | 14.1 us                                                | 13.0 us: 1.09x faster                                                       |
| pickle_list             | 4.56 us                                                | 4.22 us: 1.08x faster                                                       |
| telco                   | 6.54 ms                                                | 6.38 ms: 1.03x faster                                                       |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                       |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                       |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                        |
| unpickle_list           | 4.82 us                                                | 4.94 us: 1.03x slower                                                       |
| regex_effbot            | 3.23 ms                                                | 3.38 ms: 1.05x slower                                                       |
| python_startup_no_site  | 5.82 ms                                                | 6.46 ms: 1.11x slower                                                       |
| gc_traversal            | 3.84 ms                                                | 4.29 ms: 1.12x slower                                                       |
| pickle_dict             | 27.3 us                                                | 31.0 us: 1.14x slower                                                       |
| dask                    | 423 ms                                                 | 492 ms: 1.17x slower                                                        |
| coverage                | 72.8 ms                                                | 98.3 ms: 1.35x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                |

Benchmark hidden because not significant (1): generators
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230129-3.12.0a4+-23ae36b/bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.27x
