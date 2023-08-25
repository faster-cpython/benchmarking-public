
# Results vs. 3.10.4

- fork: iritkatriel
- ref: remove_JUMP_IF_FALSE
- machine: linux-x86_64
- commit hash: 12595f6
- commit date: 2023-03-21
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 249 ms: 1.35x faster                                                        |
| chameleon      | 9.06 ms                                                | 6.56 ms: 1.38x faster                                                       |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                      |
| html5lib       | 85.9 ms                                                | 60.8 ms: 1.41x faster                                                       |
| tornado_http   | 127 ms                                                 | 91.5 ms: 1.39x faster                                                       |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.2 ms: 1.62x faster                                                       |
| float          | 111 ms                                                 | 73.2 ms: 1.51x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                        |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                       |
| regex_dna      | 222 ms                                                 | 201 ms: 1.10x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.59 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 287 us: 1.59x faster                                                        |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.51x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.51 ms: 1.42x faster                                                       |
| xml_etree_process    | 74.9 ms                                                | 56.8 ms: 1.32x faster                                                       |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 81.6 ms: 1.15x faster                                                       |
| pickle_list          | 4.56 us                                                | 4.08 us: 1.12x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                        |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                       |
| unpickle_list        | 4.82 us                                                | 5.01 us: 1.04x slower                                                       |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.87 ms: 1.60x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.50 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                       |
| genshi_text     | 30.3 ms                                                | 21.8 ms: 1.39x faster                                                       |
| django_template | 45.9 ms                                                | 33.2 ms: 1.38x faster                                                       |
| genshi_xml      | 63.3 ms                                                | 46.8 ms: 1.35x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.2 ms: 2.63x faster                                                       |
| deltablue               | 7.42 ms                                                | 3.18 ms: 2.33x faster                                                       |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.88x faster                                                        |
| asyncio_tcp             | 925 ms                                                 | 512 ms: 1.81x faster                                                        |
| logging_silent          | 175 ns                                                 | 98.4 ns: 1.78x faster                                                       |
| richards                | 74.9 ms                                                | 43.5 ms: 1.72x faster                                                       |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                                        |
| spectral_norm           | 150 ms                                                 | 88.6 ms: 1.69x faster                                                       |
| pyflate                 | 673 ms                                                 | 407 ms: 1.65x faster                                                        |
| raytrace                | 464 ms                                                 | 283 ms: 1.64x faster                                                        |
| scimark_monte_carlo     | 108 ms                                                 | 66.2 ms: 1.64x faster                                                       |
| nbody                   | 142 ms                                                 | 87.2 ms: 1.62x faster                                                       |
| crypto_pyaes            | 118 ms                                                 | 73.4 ms: 1.61x faster                                                       |
| chaos                   | 106 ms                                                 | 66.6 ms: 1.60x faster                                                       |
| python_startup          | 14.2 ms                                                | 8.87 ms: 1.60x faster                                                       |
| pickle_pure_python      | 455 us                                                 | 287 us: 1.59x faster                                                        |
| hexiom                  | 9.53 ms                                                | 6.11 ms: 1.56x faster                                                       |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.51x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 34.6 us: 1.51x faster                                                       |
| float                   | 111 ms                                                 | 73.2 ms: 1.51x faster                                                       |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                                        |
| mako                    | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                       |
| unpack_sequence         | 64.7 ns                                                | 44.2 ns: 1.47x faster                                                       |
| coroutines              | 31.8 ms                                                | 22.0 ms: 1.45x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.51 ms: 1.42x faster                                                       |
| sqlglot_parse           | 2.06 ms                                                | 1.45 ms: 1.42x faster                                                       |
| html5lib                | 85.9 ms                                                | 60.8 ms: 1.41x faster                                                       |
| logging_format          | 8.91 us                                                | 6.32 us: 1.41x faster                                                       |
| sqlglot_transpile       | 2.45 ms                                                | 1.74 ms: 1.40x faster                                                       |
| logging_simple          | 8.07 us                                                | 5.78 us: 1.40x faster                                                       |
| genshi_text             | 30.3 ms                                                | 21.8 ms: 1.39x faster                                                       |
| tornado_http            | 127 ms                                                 | 91.5 ms: 1.39x faster                                                       |
| chameleon               | 9.06 ms                                                | 6.56 ms: 1.38x faster                                                       |
| django_template         | 45.9 ms                                                | 33.2 ms: 1.38x faster                                                       |
| scimark_fft             | 424 ms                                                 | 309 ms: 1.37x faster                                                        |
| pprint_pformat          | 1.99 sec                                               | 1.45 sec: 1.37x faster                                                      |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.36x faster                                                      |
| async_tree_none         | 717 ms                                                 | 527 ms: 1.36x faster                                                        |
| 2to3                    | 336 ms                                                 | 249 ms: 1.35x faster                                                        |
| genshi_xml              | 63.3 ms                                                | 46.8 ms: 1.35x faster                                                       |
| pprint_safe_repr        | 955 ms                                                 | 711 ms: 1.34x faster                                                        |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                       |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                                        |
| thrift                  | 1.03 ms                                                | 773 us: 1.34x faster                                                        |
| pycparser               | 1.50 sec                                               | 1.13 sec: 1.33x faster                                                      |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                        |
| xml_etree_process       | 74.9 ms                                                | 56.8 ms: 1.32x faster                                                       |
| fannkuch                | 486 ms                                                 | 371 ms: 1.31x faster                                                        |
| mypy2                   | 428 ms                                                 | 333 ms: 1.29x faster                                                        |
| async_tree_memoization  | 854 ms                                                 | 666 ms: 1.28x faster                                                        |
| deepcopy_reduce         | 3.82 us                                                | 2.98 us: 1.28x faster                                                       |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                 | 746 ms: 1.27x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                | 51.5 ms: 1.27x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.32 ms: 1.26x faster                                                       |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                      |
| nqueens                 | 100 ms                                                 | 80.8 ms: 1.24x faster                                                       |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 788 us: 1.20x faster                                                        |
| dulwich_log             | 75.9 ms                                                | 63.3 ms: 1.20x faster                                                       |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                                       |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                       |
| sympy_expand            | 545 ms                                                 | 459 ms: 1.19x faster                                                        |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.9 ms: 1.18x faster                                                       |
| json                    | 5.42 ms                                                | 4.61 ms: 1.17x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.43 sec: 1.16x faster                                                      |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 81.6 ms: 1.15x faster                                                       |
| regex_v8                | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                       |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.13x faster                                                       |
| sqlite_synth            | 2.93 us                                                | 2.61 us: 1.12x faster                                                       |
| comprehensions          | 26.8 us                                                | 23.9 us: 1.12x faster                                                       |
| pickle_list             | 4.56 us                                                | 4.08 us: 1.12x faster                                                       |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.12x faster                                                       |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                        |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                                        |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                                       |
| regex_dna               | 222 ms                                                 | 201 ms: 1.10x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                        |
| async_generators        | 425 ms                                                 | 411 ms: 1.03x faster                                                        |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                       |
| gc_traversal            | 3.84 ms                                                | 3.83 ms: 1.00x faster                                                       |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                       |
| unpickle_list           | 4.82 us                                                | 5.01 us: 1.04x slower                                                       |
| regex_effbot            | 3.23 ms                                                | 3.59 ms: 1.11x slower                                                       |
| python_startup_no_site  | 5.82 ms                                                | 6.50 ms: 1.12x slower                                                       |
| pickle_dict             | 27.3 us                                                | 30.8 us: 1.13x slower                                                       |
| dask                    | 423 ms                                                 | 508 ms: 1.20x slower                                                        |
| coverage                | 72.8 ms                                                | 94.9 ms: 1.30x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (2): unpickle, telco
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x
