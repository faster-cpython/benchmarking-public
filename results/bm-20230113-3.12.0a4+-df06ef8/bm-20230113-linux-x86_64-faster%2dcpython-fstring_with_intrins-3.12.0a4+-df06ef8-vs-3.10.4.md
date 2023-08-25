
# Results vs. 3.10.4

- fork: faster-cpython
- ref: fstring_with_intrins
- machine: linux-x86_64
- commit hash: df06ef8
- commit date: 2023-01-13
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                             |
| chameleon      | 9.06 ms                                                | 6.37 ms: 1.42x faster                                                            |
| docutils       | 3.17 sec                                               | 2.51 sec: 1.26x faster                                                           |
| html5lib       | 85.9 ms                                                | 60.2 ms: 1.43x faster                                                            |
| tornado_http   | 127 ms                                                 | 93.4 ms: 1.36x faster                                                            |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.2 ms: 1.53x faster                                                            |
| nbody          | 142 ms                                                 | 93.7 ms: 1.51x faster                                                            |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                                             |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                            |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                                             |
| regex_effbot   | 3.23 ms                                                | 3.58 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                                             |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.52x faster                                                             |
| json_dumps           | 13.5 ms                                                | 9.46 ms: 1.43x faster                                                            |
| xml_etree_process    | 74.9 ms                                                | 53.8 ms: 1.39x faster                                                            |
| xml_etree_generate   | 94.2 ms                                                | 77.5 ms: 1.22x faster                                                            |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                                            |
| pickle_list          | 4.56 us                                                | 4.10 us: 1.11x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                                             |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                                            |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                                             |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                                            |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                                            |
| pickle_dict          | 27.3 us                                                | 30.7 us: 1.13x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.57 ms: 1.65x faster                                                            |
| python_startup_no_site | 5.82 ms                                                | 6.13 ms: 1.05x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.75 ms: 1.51x faster                                                            |
| genshi_text     | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                            |
| django_template | 45.9 ms                                                | 32.2 ms: 1.42x faster                                                            |
| genshi_xml      | 63.3 ms                                                | 46.5 ms: 1.36x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.32x faster                                                            |
| logging_silent          | 175 ns                                                 | 91.5 ns: 1.91x faster                                                            |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 504 ms: 1.84x faster                                                             |
| richards                | 74.9 ms                                                | 42.3 ms: 1.77x faster                                                            |
| go                      | 229 ms                                                 | 134 ms: 1.72x faster                                                             |
| pyflate                 | 673 ms                                                 | 394 ms: 1.71x faster                                                             |
| scimark_monte_carlo     | 108 ms                                                 | 64.3 ms: 1.68x faster                                                            |
| python_startup          | 14.2 ms                                                | 8.57 ms: 1.65x faster                                                            |
| raytrace                | 464 ms                                                 | 287 ms: 1.61x faster                                                             |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                                             |
| hexiom                  | 9.53 ms                                                | 5.95 ms: 1.60x faster                                                            |
| crypto_pyaes            | 118 ms                                                 | 74.3 ms: 1.59x faster                                                            |
| chaos                   | 106 ms                                                 | 66.9 ms: 1.59x faster                                                            |
| deepcopy_memo           | 52.3 us                                                | 33.5 us: 1.56x faster                                                            |
| spectral_norm           | 150 ms                                                 | 97.6 ms: 1.54x faster                                                            |
| float                   | 111 ms                                                 | 72.2 ms: 1.53x faster                                                            |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.52x faster                                                             |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                             |
| mako                    | 14.8 ms                                                | 9.75 ms: 1.51x faster                                                            |
| nbody                   | 142 ms                                                 | 93.7 ms: 1.51x faster                                                            |
| unpack_sequence         | 64.7 ns                                                | 43.0 ns: 1.51x faster                                                            |
| genshi_text             | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                            |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.47x faster                                                            |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                                           |
| sqlglot_transpile       | 2.45 ms                                                | 1.69 ms: 1.45x faster                                                            |
| pprint_safe_repr        | 955 ms                                                 | 666 ms: 1.43x faster                                                             |
| json_dumps              | 13.5 ms                                                | 9.46 ms: 1.43x faster                                                            |
| html5lib                | 85.9 ms                                                | 60.2 ms: 1.43x faster                                                            |
| django_template         | 45.9 ms                                                | 32.2 ms: 1.42x faster                                                            |
| chameleon               | 9.06 ms                                                | 6.37 ms: 1.42x faster                                                            |
| logging_simple          | 8.07 us                                                | 5.71 us: 1.41x faster                                                            |
| logging_format          | 8.91 us                                                | 6.31 us: 1.41x faster                                                            |
| xml_etree_process       | 74.9 ms                                                | 53.8 ms: 1.39x faster                                                            |
| thrift                  | 1.03 ms                                                | 746 us: 1.39x faster                                                             |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                                            |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.38x faster                                                           |
| async_tree_none         | 717 ms                                                 | 523 ms: 1.37x faster                                                             |
| tornado_http            | 127 ms                                                 | 93.4 ms: 1.36x faster                                                            |
| genshi_xml              | 63.3 ms                                                | 46.5 ms: 1.36x faster                                                            |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.01 ms: 1.36x faster                                                            |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                                             |
| scimark_fft             | 424 ms                                                 | 312 ms: 1.36x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.34x faster                                                           |
| deepcopy                | 442 us                                                 | 332 us: 1.33x faster                                                             |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                             |
| fannkuch                | 486 ms                                                 | 366 ms: 1.33x faster                                                             |
| deepcopy_reduce         | 3.82 us                                                | 2.89 us: 1.32x faster                                                            |
| async_tree_memoization  | 854 ms                                                 | 656 ms: 1.30x faster                                                             |
| coroutines              | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                            |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                             |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed | 951 ms                                                 | 745 ms: 1.28x faster                                                             |
| docutils                | 3.17 sec                                               | 2.51 sec: 1.26x faster                                                           |
| nqueens                 | 100 ms                                                 | 79.4 ms: 1.26x faster                                                            |
| dulwich_log             | 75.9 ms                                                | 61.6 ms: 1.23x faster                                                            |
| bench_thread_pool       | 947 us                                                 | 778 us: 1.22x faster                                                             |
| xml_etree_generate      | 94.2 ms                                                | 77.5 ms: 1.22x faster                                                            |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                                            |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.20x faster                                                            |
| async_generators        | 425 ms                                                 | 355 ms: 1.20x faster                                                             |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                                             |
| sympy_str               | 328 ms                                                 | 281 ms: 1.17x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                            |
| json                    | 5.42 ms                                                | 4.72 ms: 1.15x faster                                                            |
| sqlite_synth            | 2.93 us                                                | 2.56 us: 1.14x faster                                                            |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                                            |
| mdp                     | 2.82 sec                                               | 2.47 sec: 1.14x faster                                                           |
| sympy_sum               | 185 ms                                                 | 164 ms: 1.13x faster                                                             |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                            |
| pickle_list             | 4.56 us                                                | 4.10 us: 1.11x faster                                                            |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                             |
| djangocms               | 35.9 us                                                | 32.8 us: 1.10x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                                             |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                                            |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.06x faster                                                             |
| regex_dna               | 222 ms                                                 | 210 ms: 1.06x faster                                                             |
| telco                   | 6.54 ms                                                | 6.24 ms: 1.05x faster                                                            |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                                            |
| gc_traversal            | 3.84 ms                                                | 3.79 ms: 1.01x faster                                                            |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                             |
| generators              | 76.8 ms                                                | 77.2 ms: 1.01x slower                                                            |
| unpickle_list           | 4.82 us                                                | 4.97 us: 1.03x slower                                                            |
| python_startup_no_site  | 5.82 ms                                                | 6.13 ms: 1.05x slower                                                            |
| regex_effbot            | 3.23 ms                                                | 3.58 ms: 1.11x slower                                                            |
| pickle_dict             | 27.3 us                                                | 30.7 us: 1.13x slower                                                            |
| dask                    | 423 ms                                                 | 496 ms: 1.17x slower                                                             |
| coverage                | 72.8 ms                                                | 99.6 ms: 1.37x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                     |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230113-3.12.0a4+-df06ef8/bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
