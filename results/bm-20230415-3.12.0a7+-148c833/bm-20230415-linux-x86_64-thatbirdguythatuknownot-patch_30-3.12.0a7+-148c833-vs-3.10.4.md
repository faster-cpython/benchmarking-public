
# Results vs. 3.10.4

- fork: thatbirdguythatuknownot
- ref: patch_30
- machine: linux-x86_64
- commit hash: 148c833
- commit date: 2023-04-15
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 249 ms: 1.35x faster                                                        |
| chameleon      | 9.06 ms                                                | 6.48 ms: 1.40x faster                                                       |
| docutils       | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                      |
| html5lib       | 85.9 ms                                                | 60.3 ms: 1.42x faster                                                       |
| tornado_http   | 127 ms                                                 | 93.0 ms: 1.37x faster                                                       |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 83.5 ms: 1.70x faster                                                       |
| float          | 111 ms                                                 | 73.7 ms: 1.50x faster                                                       |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                        |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                       |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.52 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                                        |
| unpickle_pure_python | 300 us                                                 | 202 us: 1.48x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.32 ms: 1.45x faster                                                       |
| xml_etree_process    | 74.9 ms                                                | 55.0 ms: 1.36x faster                                                       |
| json_loads           | 28.8 us                                                | 24.4 us: 1.18x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 79.8 ms: 1.18x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 99.8 ms: 1.12x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.24 us: 1.08x faster                                                       |
| unpickle             | 14.1 us                                                | 14.3 us: 1.01x slower                                                       |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                       |
| unpickle_list        | 4.82 us                                                | 5.15 us: 1.07x slower                                                       |
| pickle_dict          | 27.3 us                                                | 31.7 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.90 ms: 1.59x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.60 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.96 ms: 1.48x faster                                                       |
| genshi_text     | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                       |
| django_template | 45.9 ms                                                | 32.7 ms: 1.40x faster                                                       |
| genshi_xml      | 63.3 ms                                                | 47.1 ms: 1.34x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 28.9 ms: 2.66x faster                                                       |
| deltablue               | 7.42 ms                                                | 3.23 ms: 2.30x faster                                                       |
| asyncio_tcp             | 925 ms                                                 | 500 ms: 1.85x faster                                                        |
| logging_silent          | 175 ns                                                 | 95.8 ns: 1.83x faster                                                       |
| scimark_sor             | 197 ms                                                 | 110 ms: 1.79x faster                                                        |
| richards                | 74.9 ms                                                | 42.3 ms: 1.77x faster                                                       |
| nbody                   | 142 ms                                                 | 83.5 ms: 1.70x faster                                                       |
| sqlglot_parse           | 2.06 ms                                                | 1.22 ms: 1.69x faster                                                       |
| go                      | 229 ms                                                 | 136 ms: 1.69x faster                                                        |
| raytrace                | 464 ms                                                 | 282 ms: 1.65x faster                                                        |
| chaos                   | 106 ms                                                 | 64.8 ms: 1.64x faster                                                       |
| spectral_norm           | 150 ms                                                 | 91.4 ms: 1.64x faster                                                       |
| scimark_monte_carlo     | 108 ms                                                 | 66.2 ms: 1.64x faster                                                       |
| sqlglot_transpile       | 2.45 ms                                                | 1.50 ms: 1.63x faster                                                       |
| pyflate                 | 673 ms                                                 | 414 ms: 1.63x faster                                                        |
| hexiom                  | 9.53 ms                                                | 5.96 ms: 1.60x faster                                                       |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                                        |
| python_startup          | 14.2 ms                                                | 8.90 ms: 1.59x faster                                                       |
| crypto_pyaes            | 118 ms                                                 | 74.5 ms: 1.59x faster                                                       |
| scimark_lu              | 163 ms                                                 | 105 ms: 1.55x faster                                                        |
| unpack_sequence         | 64.7 ns                                                | 42.9 ns: 1.51x faster                                                       |
| deepcopy_memo           | 52.3 us                                                | 34.9 us: 1.50x faster                                                       |
| float                   | 111 ms                                                 | 73.7 ms: 1.50x faster                                                       |
| unpickle_pure_python    | 300 us                                                 | 202 us: 1.48x faster                                                        |
| mako                    | 14.8 ms                                                | 9.96 ms: 1.48x faster                                                       |
| coroutines              | 31.8 ms                                                | 21.7 ms: 1.46x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.32 ms: 1.45x faster                                                       |
| html5lib                | 85.9 ms                                                | 60.3 ms: 1.42x faster                                                       |
| genshi_text             | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                       |
| django_template         | 45.9 ms                                                | 32.7 ms: 1.40x faster                                                       |
| logging_simple          | 8.07 us                                                | 5.76 us: 1.40x faster                                                       |
| logging_format          | 8.91 us                                                | 6.36 us: 1.40x faster                                                       |
| chameleon               | 9.06 ms                                                | 6.48 ms: 1.40x faster                                                       |
| async_tree_none         | 717 ms                                                 | 517 ms: 1.39x faster                                                        |
| async_tree_memoization  | 854 ms                                                 | 616 ms: 1.39x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 1.28 sec: 1.39x faster                                                      |
| pprint_pformat          | 1.99 sec                                               | 1.44 sec: 1.38x faster                                                      |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                       |
| tornado_http            | 127 ms                                                 | 93.0 ms: 1.37x faster                                                       |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.37x faster                                                      |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                        |
| scimark_fft             | 424 ms                                                 | 310 ms: 1.37x faster                                                        |
| xml_etree_process       | 74.9 ms                                                | 55.0 ms: 1.36x faster                                                       |
| pprint_safe_repr        | 955 ms                                                 | 704 ms: 1.36x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.03 ms: 1.35x faster                                                       |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                       |
| 2to3                    | 336 ms                                                 | 249 ms: 1.35x faster                                                        |
| genshi_xml              | 63.3 ms                                                | 47.1 ms: 1.34x faster                                                       |
| deepcopy                | 442 us                                                 | 334 us: 1.32x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                 | 724 ms: 1.31x faster                                                        |
| thrift                  | 1.03 ms                                                | 792 us: 1.31x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                        |
| mypy2                   | 428 ms                                                 | 330 ms: 1.30x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                | 51.2 ms: 1.28x faster                                                       |
| deepcopy_reduce         | 3.82 us                                                | 3.02 us: 1.27x faster                                                       |
| docutils                | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                      |
| comprehensions          | 26.8 us                                                | 21.4 us: 1.26x faster                                                       |
| fannkuch                | 486 ms                                                 | 387 ms: 1.26x faster                                                        |
| nqueens                 | 100 ms                                                 | 81.1 ms: 1.23x faster                                                       |
| sqlalchemy_declarative  | 165 ms                                                 | 135 ms: 1.22x faster                                                        |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.3 ms: 1.22x faster                                                       |
| dulwich_log             | 75.9 ms                                                | 62.3 ms: 1.22x faster                                                       |
| bench_thread_pool       | 947 us                                                 | 786 us: 1.21x faster                                                        |
| pylint                  | 525 ms                                                 | 439 ms: 1.20x faster                                                        |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                       |
| sympy_expand            | 545 ms                                                 | 459 ms: 1.19x faster                                                        |
| json_loads              | 28.8 us                                                | 24.4 us: 1.18x faster                                                       |
| xml_etree_generate      | 94.2 ms                                                | 79.8 ms: 1.18x faster                                                       |
| sympy_str               | 328 ms                                                 | 281 ms: 1.17x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.2 ms: 1.17x faster                                                       |
| json                    | 5.42 ms                                                | 4.67 ms: 1.16x faster                                                       |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                       |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                       |
| sympy_sum               | 185 ms                                                 | 163 ms: 1.13x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 99.8 ms: 1.12x faster                                                       |
| djangocms               | 35.9 us                                                | 32.2 us: 1.12x faster                                                       |
| sqlite_synth            | 2.93 us                                                | 2.64 us: 1.11x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.55 sec: 1.11x faster                                                      |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                                        |
| pickle_list             | 4.56 us                                                | 4.24 us: 1.08x faster                                                       |
| regex_dna               | 222 ms                                                 | 207 ms: 1.07x faster                                                        |
| telco                   | 6.54 ms                                                | 6.48 ms: 1.01x faster                                                       |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                        |
| async_generators        | 425 ms                                                 | 427 ms: 1.00x slower                                                        |
| unpickle                | 14.1 us                                                | 14.3 us: 1.01x slower                                                       |
| pickle                  | 10.3 us                                                | 10.7 us: 1.04x slower                                                       |
| gc_traversal            | 3.84 ms                                                | 4.06 ms: 1.06x slower                                                       |
| unpickle_list           | 4.82 us                                                | 5.15 us: 1.07x slower                                                       |
| regex_effbot            | 3.23 ms                                                | 3.52 ms: 1.09x slower                                                       |
| python_startup_no_site  | 5.82 ms                                                | 6.60 ms: 1.13x slower                                                       |
| dask                    | 423 ms                                                 | 491 ms: 1.16x slower                                                        |
| pickle_dict             | 27.3 us                                                | 31.7 us: 1.16x slower                                                       |
| coverage                | 72.8 ms                                                | 96.8 ms: 1.33x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x
