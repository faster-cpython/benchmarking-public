
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: immortalize_empty_ke
- machine: linux-x86_64
- commit hash: e472d94
- commit date: 2023-05-06
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 270 ms: 1.25x faster                                                              |
| docutils       | 3.17 sec                                               | 2.72 sec: 1.17x faster                                                            |
| tornado_http   | 127 ms                                                 | 103 ms: 1.24x faster                                                              |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.1 ms: 1.52x faster                                                             |
| float          | 111 ms                                                 | 82.0 ms: 1.35x faster                                                             |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                  | 1.25x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 146 ms: 1.21x faster                                                              |
| regex_v8       | 25.0 ms                                                | 22.8 ms: 1.10x faster                                                             |
| regex_dna      | 222 ms                                                 | 211 ms: 1.05x faster                                                              |
| regex_effbot   | 3.23 ms                                                | 3.74 ms: 1.16x slower                                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 318 us: 1.43x faster                                                              |
| unpickle_pure_python | 300 us                                                 | 218 us: 1.38x faster                                                              |
| json_dumps           | 13.5 ms                                                | 9.99 ms: 1.35x faster                                                             |
| xml_etree_process    | 74.9 ms                                                | 59.9 ms: 1.25x faster                                                             |
| json_loads           | 28.8 us                                                | 25.5 us: 1.13x faster                                                             |
| xml_etree_generate   | 94.2 ms                                                | 85.9 ms: 1.10x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.08x faster                                                              |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.05x faster                                                              |
| pickle_list          | 4.56 us                                                | 4.58 us: 1.01x slower                                                             |
| unpickle_list        | 4.82 us                                                | 4.95 us: 1.03x slower                                                             |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                             |
| unpickle             | 14.1 us                                                | 15.7 us: 1.11x slower                                                             |
| pickle_dict          | 27.3 us                                                | 31.4 us: 1.15x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.19 ms: 1.54x faster                                                             |
| python_startup_no_site | 5.82 ms                                                | 6.70 ms: 1.15x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.40x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 31.1 ms: 2.47x faster                                                             |
| deltablue               | 7.42 ms                                                | 3.58 ms: 2.07x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 513 ms: 1.80x faster                                                              |
| richards                | 74.9 ms                                                | 44.3 ms: 1.69x faster                                                             |
| go                      | 229 ms                                                 | 137 ms: 1.67x faster                                                              |
| logging_silent          | 175 ns                                                 | 106 ns: 1.65x faster                                                              |
| scimark_sor             | 197 ms                                                 | 123 ms: 1.60x faster                                                              |
| chaos                   | 106 ms                                                 | 68.6 ms: 1.55x faster                                                             |
| python_startup          | 14.2 ms                                                | 9.19 ms: 1.54x faster                                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.34 ms: 1.54x faster                                                             |
| hexiom                  | 9.53 ms                                                | 6.21 ms: 1.54x faster                                                             |
| nbody                   | 142 ms                                                 | 93.1 ms: 1.52x faster                                                             |
| pyflate                 | 673 ms                                                 | 443 ms: 1.52x faster                                                              |
| raytrace                | 464 ms                                                 | 310 ms: 1.49x faster                                                              |
| crypto_pyaes            | 118 ms                                                 | 79.6 ms: 1.49x faster                                                             |
| spectral_norm           | 150 ms                                                 | 101 ms: 1.48x faster                                                              |
| scimark_monte_carlo     | 108 ms                                                 | 73.0 ms: 1.48x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.66 ms: 1.47x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.23 sec: 1.44x faster                                                            |
| pickle_pure_python      | 455 us                                                 | 318 us: 1.43x faster                                                              |
| async_tree_none         | 717 ms                                                 | 504 ms: 1.42x faster                                                              |
| scimark_lu              | 163 ms                                                 | 115 ms: 1.42x faster                                                              |
| coroutines              | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                             |
| mako                    | 14.8 ms                                                | 10.6 ms: 1.40x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 615 ms: 1.39x faster                                                              |
| deepcopy_memo           | 52.3 us                                                | 37.8 us: 1.39x faster                                                             |
| unpickle_pure_python    | 300 us                                                 | 218 us: 1.38x faster                                                              |
| json_dumps              | 13.5 ms                                                | 9.99 ms: 1.35x faster                                                             |
| unpack_sequence         | 64.7 ns                                                | 47.9 ns: 1.35x faster                                                             |
| float                   | 111 ms                                                 | 82.0 ms: 1.35x faster                                                             |
| async_tree_cpu_io_mixed | 951 ms                                                 | 725 ms: 1.31x faster                                                              |
| fannkuch                | 486 ms                                                 | 372 ms: 1.31x faster                                                              |
| pprint_pformat          | 1.99 sec                                               | 1.53 sec: 1.30x faster                                                            |
| pprint_safe_repr        | 955 ms                                                 | 744 ms: 1.28x faster                                                              |
| xml_etree_process       | 74.9 ms                                                | 59.9 ms: 1.25x faster                                                             |
| nqueens                 | 100 ms                                                 | 80.1 ms: 1.25x faster                                                             |
| 2to3                    | 336 ms                                                 | 270 ms: 1.25x faster                                                              |
| tornado_http            | 127 ms                                                 | 103 ms: 1.24x faster                                                              |
| pycparser               | 1.50 sec                                               | 1.21 sec: 1.24x faster                                                            |
| deepcopy                | 442 us                                                 | 361 us: 1.22x faster                                                              |
| logging_simple          | 8.07 us                                                | 6.61 us: 1.22x faster                                                             |
| logging_format          | 8.91 us                                                | 7.31 us: 1.22x faster                                                             |
| regex_compile           | 177 ms                                                 | 146 ms: 1.21x faster                                                              |
| mypy2                   | 428 ms                                                 | 354 ms: 1.21x faster                                                              |
| deepcopy_reduce         | 3.82 us                                                | 3.17 us: 1.21x faster                                                             |
| sqlglot_normalize       | 135 ms                                                 | 112 ms: 1.20x faster                                                              |
| scimark_fft             | 424 ms                                                 | 355 ms: 1.19x faster                                                              |
| sqlglot_optimize        | 65.3 ms                                                | 55.1 ms: 1.19x faster                                                             |
| docutils                | 3.17 sec                                               | 2.72 sec: 1.17x faster                                                            |
| comprehensions          | 26.8 us                                                | 23.2 us: 1.16x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.74 ms: 1.15x faster                                                             |
| bench_thread_pool       | 947 us                                                 | 834 us: 1.14x faster                                                              |
| json_loads              | 28.8 us                                                | 25.5 us: 1.13x faster                                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 146 ms: 1.13x faster                                                              |
| json                    | 5.42 ms                                                | 4.81 ms: 1.13x faster                                                             |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                             |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.9 ms: 1.12x faster                                                             |
| dulwich_log             | 75.9 ms                                                | 68.4 ms: 1.11x faster                                                             |
| mdp                     | 2.82 sec                                               | 2.56 sec: 1.10x faster                                                            |
| regex_v8                | 25.0 ms                                                | 22.8 ms: 1.10x faster                                                             |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                                              |
| xml_etree_generate      | 94.2 ms                                                | 85.9 ms: 1.10x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.08x faster                                                              |
| sqlite_synth            | 2.93 us                                                | 2.78 us: 1.05x faster                                                             |
| regex_dna               | 222 ms                                                 | 211 ms: 1.05x faster                                                              |
| xml_etree_parse         | 163 ms                                                 | 156 ms: 1.05x faster                                                              |
| pathlib                 | 20.0 ms                                                | 19.3 ms: 1.04x faster                                                             |
| pickle_list             | 4.56 us                                                | 4.58 us: 1.01x slower                                                             |
| unpickle_list           | 4.82 us                                                | 4.95 us: 1.03x slower                                                             |
| gc_traversal            | 3.84 ms                                                | 3.97 ms: 1.03x slower                                                             |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                              |
| pickle                  | 10.3 us                                                | 10.7 us: 1.04x slower                                                             |
| async_generators        | 425 ms                                                 | 449 ms: 1.06x slower                                                              |
| telco                   | 6.54 ms                                                | 7.00 ms: 1.07x slower                                                             |
| unpickle                | 14.1 us                                                | 15.7 us: 1.11x slower                                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.70 ms: 1.15x slower                                                             |
| pickle_dict             | 27.3 us                                                | 31.4 us: 1.15x slower                                                             |
| regex_effbot            | 3.23 ms                                                | 3.74 ms: 1.16x slower                                                             |
| dask                    | 423 ms                                                 | 538 ms: 1.27x slower                                                              |
| coverage                | 72.8 ms                                                | 102 ms: 1.40x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.24x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x
