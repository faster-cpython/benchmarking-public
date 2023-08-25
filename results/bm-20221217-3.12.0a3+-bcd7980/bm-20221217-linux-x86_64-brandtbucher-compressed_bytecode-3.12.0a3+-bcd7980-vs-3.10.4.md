
# Results vs. 3.10.4

- fork: brandtbucher
- ref: compressed_bytecode
- machine: linux-x86_64
- commit hash: bcd7980
- commit date: 2022-12-17
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                        |
| chameleon      | 9.06 ms                                                | 6.43 ms: 1.41x faster                                                       |
| docutils       | 3.17 sec                                               | 2.49 sec: 1.27x faster                                                      |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                       |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.3 ms: 1.53x faster                                                       |
| nbody          | 142 ms                                                 | 93.6 ms: 1.51x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                                        |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                       |
| regex_dna      | 222 ms                                                 | 219 ms: 1.01x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.58 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.61x faster                                                        |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.49 ms: 1.43x faster                                                       |
| xml_etree_process    | 74.9 ms                                                | 53.6 ms: 1.40x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 77.2 ms: 1.22x faster                                                       |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                                       |
| pickle_list          | 4.56 us                                                | 4.12 us: 1.11x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                        |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                                       |
| unpickle_list        | 4.82 us                                                | 5.12 us: 1.06x slower                                                       |
| pickle_dict          | 27.3 us                                                | 30.6 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.50 ms: 1.67x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.08 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.72 ms: 1.52x faster                                                       |
| genshi_text     | 30.3 ms                                                | 21.3 ms: 1.42x faster                                                       |
| django_template | 45.9 ms                                                | 32.9 ms: 1.39x faster                                                       |
| genshi_xml      | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.22 ms: 2.30x faster                                                       |
| logging_silent          | 175 ns                                                 | 92.1 ns: 1.90x faster                                                       |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                                        |
| richards                | 74.9 ms                                                | 41.6 ms: 1.80x faster                                                       |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                                        |
| python_startup          | 14.2 ms                                                | 8.50 ms: 1.67x faster                                                       |
| raytrace                | 464 ms                                                 | 280 ms: 1.66x faster                                                        |
| pyflate                 | 673 ms                                                 | 407 ms: 1.65x faster                                                        |
| scimark_monte_carlo     | 108 ms                                                 | 66.1 ms: 1.64x faster                                                       |
| pickle_pure_python      | 455 us                                                 | 282 us: 1.61x faster                                                        |
| chaos                   | 106 ms                                                 | 66.1 ms: 1.61x faster                                                       |
| crypto_pyaes            | 118 ms                                                 | 74.1 ms: 1.60x faster                                                       |
| hexiom                  | 9.53 ms                                                | 6.08 ms: 1.57x faster                                                       |
| deepcopy_memo           | 52.3 us                                                | 33.5 us: 1.56x faster                                                       |
| spectral_norm           | 150 ms                                                 | 96.1 ms: 1.56x faster                                                       |
| unpack_sequence         | 64.7 ns                                                | 41.6 ns: 1.56x faster                                                       |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.53x faster                                                        |
| float                   | 111 ms                                                 | 72.3 ms: 1.53x faster                                                       |
| mako                    | 14.8 ms                                                | 9.72 ms: 1.52x faster                                                       |
| nbody                   | 142 ms                                                 | 93.6 ms: 1.51x faster                                                       |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                                        |
| sqlglot_parse           | 2.06 ms                                                | 1.39 ms: 1.48x faster                                                       |
| sqlglot_transpile       | 2.45 ms                                                | 1.69 ms: 1.45x faster                                                       |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.49 ms: 1.43x faster                                                       |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                                      |
| genshi_text             | 30.3 ms                                                | 21.3 ms: 1.42x faster                                                       |
| logging_format          | 8.91 us                                                | 6.28 us: 1.42x faster                                                       |
| logging_simple          | 8.07 us                                                | 5.69 us: 1.42x faster                                                       |
| chameleon               | 9.06 ms                                                | 6.43 ms: 1.41x faster                                                       |
| pprint_safe_repr        | 955 ms                                                 | 677 ms: 1.41x faster                                                        |
| xml_etree_process       | 74.9 ms                                                | 53.6 ms: 1.40x faster                                                       |
| django_template         | 45.9 ms                                                | 32.9 ms: 1.39x faster                                                       |
| thrift                  | 1.03 ms                                                | 745 us: 1.39x faster                                                        |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                                        |
| deepcopy                | 442 us                                                 | 326 us: 1.35x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.03 ms: 1.35x faster                                                       |
| genshi_xml              | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                       |
| async_tree_memoization  | 854 ms                                                 | 635 ms: 1.35x faster                                                        |
| async_tree_none         | 717 ms                                                 | 533 ms: 1.35x faster                                                        |
| scimark_fft             | 424 ms                                                 | 315 ms: 1.34x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                                      |
| pycparser               | 1.50 sec                                               | 1.13 sec: 1.33x faster                                                      |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                        |
| deepcopy_reduce         | 3.82 us                                                | 2.88 us: 1.33x faster                                                       |
| fannkuch                | 486 ms                                                 | 372 ms: 1.31x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                | 50.5 ms: 1.29x faster                                                       |
| coroutines              | 31.8 ms                                                | 25.0 ms: 1.28x faster                                                       |
| nqueens                 | 100 ms                                                 | 78.5 ms: 1.27x faster                                                       |
| docutils                | 3.17 sec                                               | 2.49 sec: 1.27x faster                                                      |
| async_tree_cpu_io_mixed | 951 ms                                                 | 765 ms: 1.24x faster                                                        |
| dulwich_log             | 75.9 ms                                                | 62.0 ms: 1.22x faster                                                       |
| bench_thread_pool       | 947 us                                                 | 774 us: 1.22x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 77.2 ms: 1.22x faster                                                       |
| sympy_expand            | 545 ms                                                 | 449 ms: 1.21x faster                                                        |
| sympy_integrate         | 24.3 ms                                                | 20.2 ms: 1.20x faster                                                       |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                                       |
| async_generators        | 425 ms                                                 | 355 ms: 1.20x faster                                                        |
| sympy_str               | 328 ms                                                 | 282 ms: 1.17x faster                                                        |
| sympy_sum               | 185 ms                                                 | 161 ms: 1.15x faster                                                        |
| sqlite_synth            | 2.93 us                                                | 2.56 us: 1.15x faster                                                       |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                                       |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                       |
| json                    | 5.42 ms                                                | 4.80 ms: 1.13x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.54 sec: 1.11x faster                                                      |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                        |
| pickle_list             | 4.56 us                                                | 4.12 us: 1.11x faster                                                       |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                                       |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                        |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                                       |
| telco                   | 6.54 ms                                                | 6.17 ms: 1.06x faster                                                       |
| regex_dna               | 222 ms                                                 | 219 ms: 1.01x faster                                                        |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                       |
| generators              | 76.8 ms                                                | 77.6 ms: 1.01x slower                                                       |
| python_startup_no_site  | 5.82 ms                                                | 6.08 ms: 1.05x slower                                                       |
| unpickle_list           | 4.82 us                                                | 5.12 us: 1.06x slower                                                       |
| regex_effbot            | 3.23 ms                                                | 3.58 ms: 1.11x slower                                                       |
| pickle_dict             | 27.3 us                                                | 30.6 us: 1.12x slower                                                       |
| coverage                | 72.8 ms                                                | 99.4 ms: 1.37x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221217-3.12.0a3+-bcd7980/bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x
