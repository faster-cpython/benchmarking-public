
# Results vs. 3.10.4

- fork: gvanrossum
- ref: tagged_ptrs
- machine: linux-x86_64
- commit hash: 3b7866f
- commit date: 2023-03-05
- overall geometric mean: 1.26x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 255 ms: 1.32x faster                                              |
| chameleon      | 9.06 ms                                                | 6.64 ms: 1.36x faster                                             |
| docutils       | 3.17 sec                                               | 2.59 sec: 1.22x faster                                            |
| html5lib       | 85.9 ms                                                | 63.2 ms: 1.36x faster                                             |
| tornado_http   | 127 ms                                                 | 96.0 ms: 1.33x faster                                             |
| Geometric mean | (ref)                                                  | 1.32x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 111 ms                                                 | 76.0 ms: 1.45x faster                                             |
| nbody          | 142 ms                                                 | 101 ms: 1.41x faster                                              |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                  | 1.26x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 138 ms: 1.28x faster                                              |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.12x faster                                             |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                              |
| regex_effbot   | 3.23 ms                                                | 3.36 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                  | 1.10x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 297 us: 1.54x faster                                              |
| unpickle_pure_python | 300 us                                                 | 208 us: 1.45x faster                                              |
| json_dumps           | 13.5 ms                                                | 9.58 ms: 1.41x faster                                             |
| xml_etree_process    | 74.9 ms                                                | 57.4 ms: 1.31x faster                                             |
| json_loads           | 28.8 us                                                | 23.7 us: 1.21x faster                                             |
| xml_etree_generate   | 94.2 ms                                                | 83.1 ms: 1.13x faster                                             |
| xml_etree_iterparse  | 111 ms                                                 | 101 ms: 1.10x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                              |
| pickle_list          | 4.56 us                                                | 4.24 us: 1.07x faster                                             |
| unpickle             | 14.1 us                                                | 13.7 us: 1.03x faster                                             |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                             |
| unpickle_list        | 4.82 us                                                | 5.11 us: 1.06x slower                                             |
| pickle_dict          | 27.3 us                                                | 31.3 us: 1.15x slower                                             |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.02 ms: 1.57x faster                                             |
| python_startup_no_site | 5.82 ms                                                | 6.54 ms: 1.12x slower                                             |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.5 ms: 1.41x faster                                             |
| genshi_text     | 30.3 ms                                                | 22.0 ms: 1.38x faster                                             |
| django_template | 45.9 ms                                                | 34.3 ms: 1.34x faster                                             |
| genshi_xml      | 63.3 ms                                                | 49.7 ms: 1.27x faster                                             |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 31.3 ms: 2.45x faster                                             |
| deltablue               | 7.42 ms                                                | 3.34 ms: 2.22x faster                                             |
| asyncio_tcp             | 925 ms                                                 | 505 ms: 1.83x faster                                              |
| logging_silent          | 175 ns                                                 | 98.7 ns: 1.77x faster                                             |
| scimark_sor             | 197 ms                                                 | 115 ms: 1.71x faster                                              |
| richards                | 74.9 ms                                                | 44.3 ms: 1.69x faster                                             |
| go                      | 229 ms                                                 | 140 ms: 1.64x faster                                              |
| pyflate                 | 673 ms                                                 | 420 ms: 1.60x faster                                              |
| python_startup          | 14.2 ms                                                | 9.02 ms: 1.57x faster                                             |
| crypto_pyaes            | 118 ms                                                 | 75.9 ms: 1.56x faster                                             |
| raytrace                | 464 ms                                                 | 299 ms: 1.55x faster                                              |
| pickle_pure_python      | 455 us                                                 | 297 us: 1.54x faster                                              |
| scimark_monte_carlo     | 108 ms                                                 | 70.9 ms: 1.53x faster                                             |
| chaos                   | 106 ms                                                 | 70.7 ms: 1.50x faster                                             |
| spectral_norm           | 150 ms                                                 | 102 ms: 1.47x faster                                              |
| hexiom                  | 9.53 ms                                                | 6.49 ms: 1.47x faster                                             |
| float                   | 111 ms                                                 | 76.0 ms: 1.45x faster                                             |
| unpickle_pure_python    | 300 us                                                 | 208 us: 1.45x faster                                              |
| unpack_sequence         | 64.7 ns                                                | 44.8 ns: 1.44x faster                                             |
| scimark_lu              | 163 ms                                                 | 115 ms: 1.42x faster                                              |
| deepcopy_memo           | 52.3 us                                                | 36.8 us: 1.42x faster                                             |
| json_dumps              | 13.5 ms                                                | 9.58 ms: 1.41x faster                                             |
| mako                    | 14.8 ms                                                | 10.5 ms: 1.41x faster                                             |
| nbody                   | 142 ms                                                 | 101 ms: 1.41x faster                                              |
| sqlglot_parse           | 2.06 ms                                                | 1.48 ms: 1.39x faster                                             |
| genshi_text             | 30.3 ms                                                | 22.0 ms: 1.38x faster                                             |
| logging_format          | 8.91 us                                                | 6.46 us: 1.38x faster                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.78 ms: 1.37x faster                                             |
| pprint_pformat          | 1.99 sec                                               | 1.45 sec: 1.37x faster                                            |
| chameleon               | 9.06 ms                                                | 6.64 ms: 1.36x faster                                             |
| logging_simple          | 8.07 us                                                | 5.92 us: 1.36x faster                                             |
| html5lib                | 85.9 ms                                                | 63.2 ms: 1.36x faster                                             |
| async_tree_none         | 717 ms                                                 | 529 ms: 1.36x faster                                              |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.35x faster                                            |
| aiohttp                 | 1.38 ms                                                | 1.02 ms: 1.35x faster                                             |
| pprint_safe_repr        | 955 ms                                                 | 710 ms: 1.35x faster                                              |
| django_template         | 45.9 ms                                                | 34.3 ms: 1.34x faster                                             |
| tornado_http            | 127 ms                                                 | 96.0 ms: 1.33x faster                                             |
| gunicorn                | 1.46 ms                                                | 1.10 ms: 1.33x faster                                             |
| coroutines              | 31.8 ms                                                | 24.0 ms: 1.32x faster                                             |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.32x faster                                            |
| thrift                  | 1.03 ms                                                | 783 us: 1.32x faster                                              |
| 2to3                    | 336 ms                                                 | 255 ms: 1.32x faster                                              |
| xml_etree_process       | 74.9 ms                                                | 57.4 ms: 1.31x faster                                             |
| regex_compile           | 177 ms                                                 | 138 ms: 1.28x faster                                              |
| deepcopy                | 442 us                                                 | 346 us: 1.28x faster                                              |
| genshi_xml              | 63.3 ms                                                | 49.7 ms: 1.27x faster                                             |
| async_tree_memoization  | 854 ms                                                 | 670 ms: 1.27x faster                                              |
| async_tree_cpu_io_mixed | 951 ms                                                 | 750 ms: 1.27x faster                                              |
| fannkuch                | 486 ms                                                 | 385 ms: 1.26x faster                                              |
| mypy2                   | 428 ms                                                 | 340 ms: 1.26x faster                                              |
| sqlglot_normalize       | 135 ms                                                 | 108 ms: 1.26x faster                                              |
| scimark_fft             | 424 ms                                                 | 337 ms: 1.26x faster                                              |
| sqlglot_optimize        | 65.3 ms                                                | 52.6 ms: 1.24x faster                                             |
| deepcopy_reduce         | 3.82 us                                                | 3.12 us: 1.23x faster                                             |
| docutils                | 3.17 sec                                               | 2.59 sec: 1.22x faster                                            |
| json_loads              | 28.8 us                                                | 23.7 us: 1.21x faster                                             |
| json                    | 5.42 ms                                                | 4.56 ms: 1.19x faster                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 140 ms: 1.18x faster                                              |
| dulwich_log             | 75.9 ms                                                | 64.3 ms: 1.18x faster                                             |
| bench_thread_pool       | 947 us                                                 | 808 us: 1.17x faster                                              |
| sympy_expand            | 545 ms                                                 | 467 ms: 1.17x faster                                              |
| sympy_integrate         | 24.3 ms                                                | 20.9 ms: 1.16x faster                                             |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.3 ms: 1.16x faster                                             |
| nqueens                 | 100 ms                                                 | 86.7 ms: 1.15x faster                                             |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                             |
| xml_etree_generate      | 94.2 ms                                                | 83.1 ms: 1.13x faster                                             |
| sympy_str               | 328 ms                                                 | 291 ms: 1.13x faster                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.86 ms: 1.12x faster                                             |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                             |
| sqlite_synth            | 2.93 us                                                | 2.63 us: 1.12x faster                                             |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.12x faster                                             |
| xml_etree_iterparse     | 111 ms                                                 | 101 ms: 1.10x faster                                              |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                              |
| sympy_sum               | 185 ms                                                 | 169 ms: 1.09x faster                                              |
| djangocms               | 35.9 us                                                | 33.1 us: 1.09x faster                                             |
| pickle_list             | 4.56 us                                                | 4.24 us: 1.07x faster                                             |
| regex_dna               | 222 ms                                                 | 207 ms: 1.07x faster                                              |
| comprehensions          | 26.8 us                                                | 25.2 us: 1.07x faster                                             |
| mdp                     | 2.82 sec                                               | 2.66 sec: 1.06x faster                                            |
| unpickle                | 14.1 us                                                | 13.7 us: 1.03x faster                                             |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                             |
| async_generators        | 425 ms                                                 | 423 ms: 1.00x faster                                              |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                              |
| regex_effbot            | 3.23 ms                                                | 3.36 ms: 1.04x slower                                             |
| gc_traversal            | 3.84 ms                                                | 4.07 ms: 1.06x slower                                             |
| unpickle_list           | 4.82 us                                                | 5.11 us: 1.06x slower                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.54 ms: 1.12x slower                                             |
| pickle_dict             | 27.3 us                                                | 31.3 us: 1.15x slower                                             |
| dask                    | 423 ms                                                 | 517 ms: 1.22x slower                                              |
| coverage                | 72.8 ms                                                | 97.0 ms: 1.33x slower                                             |
| Geometric mean          | (ref)                                                  | 1.26x faster                                                      |

Benchmark hidden because not significant (2): bench_mp_pool, telco
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x
