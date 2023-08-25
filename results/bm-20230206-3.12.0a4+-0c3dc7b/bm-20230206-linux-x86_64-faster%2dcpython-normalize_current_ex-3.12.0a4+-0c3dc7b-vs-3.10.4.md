
# Results vs. 3.10.4

- fork: faster-cpython
- ref: normalize_current_ex
- machine: linux-x86_64
- commit hash: 0c3dc7b
- commit date: 2023-02-06
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                             |
| chameleon      | 9.06 ms                                                | 6.51 ms: 1.39x faster                                                            |
| docutils       | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                           |
| html5lib       | 85.9 ms                                                | 61.1 ms: 1.41x faster                                                            |
| tornado_http   | 127 ms                                                 | 94.4 ms: 1.35x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.5 ms: 1.52x faster                                                            |
| nbody          | 142 ms                                                 | 94.6 ms: 1.50x faster                                                            |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                             |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                            |
| regex_dna      | 222 ms                                                 | 206 ms: 1.08x faster                                                             |
| regex_effbot   | 3.23 ms                                                | 3.36 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 284 us: 1.60x faster                                                             |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.53x faster                                                             |
| json_dumps           | 13.5 ms                                                | 9.44 ms: 1.43x faster                                                            |
| xml_etree_process    | 74.9 ms                                                | 55.2 ms: 1.36x faster                                                            |
| json_loads           | 28.8 us                                                | 23.8 us: 1.21x faster                                                            |
| xml_etree_generate   | 94.2 ms                                                | 79.7 ms: 1.18x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                             |
| pickle_list          | 4.56 us                                                | 4.25 us: 1.07x faster                                                            |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                                            |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                            |
| unpickle_list        | 4.82 us                                                | 4.93 us: 1.02x slower                                                            |
| pickle_dict          | 27.3 us                                                | 32.0 us: 1.17x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.95 ms: 1.58x faster                                                            |
| python_startup_no_site | 5.82 ms                                                | 6.48 ms: 1.11x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.67 ms: 1.53x faster                                                            |
| genshi_text     | 30.3 ms                                                | 20.9 ms: 1.45x faster                                                            |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                            |
| genshi_xml      | 63.3 ms                                                | 46.7 ms: 1.36x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.20 ms: 2.32x faster                                                            |
| logging_silent          | 175 ns                                                 | 93.2 ns: 1.88x faster                                                            |
| asyncio_tcp             | 925 ms                                                 | 493 ms: 1.88x faster                                                             |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                                             |
| richards                | 74.9 ms                                                | 42.1 ms: 1.78x faster                                                            |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                                             |
| pyflate                 | 673 ms                                                 | 398 ms: 1.69x faster                                                             |
| chaos                   | 106 ms                                                 | 63.4 ms: 1.68x faster                                                            |
| scimark_monte_carlo     | 108 ms                                                 | 64.7 ms: 1.67x faster                                                            |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                                             |
| crypto_pyaes            | 118 ms                                                 | 72.8 ms: 1.63x faster                                                            |
| pickle_pure_python      | 455 us                                                 | 284 us: 1.60x faster                                                             |
| hexiom                  | 9.53 ms                                                | 5.97 ms: 1.60x faster                                                            |
| python_startup          | 14.2 ms                                                | 8.95 ms: 1.58x faster                                                            |
| spectral_norm           | 150 ms                                                 | 95.9 ms: 1.56x faster                                                            |
| unpack_sequence         | 64.7 ns                                                | 41.7 ns: 1.55x faster                                                            |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.53x faster                                                             |
| mako                    | 14.8 ms                                                | 9.67 ms: 1.53x faster                                                            |
| deepcopy_memo           | 52.3 us                                                | 34.3 us: 1.53x faster                                                            |
| float                   | 111 ms                                                 | 72.5 ms: 1.52x faster                                                            |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                                             |
| nbody                   | 142 ms                                                 | 94.6 ms: 1.50x faster                                                            |
| genshi_text             | 30.3 ms                                                | 20.9 ms: 1.45x faster                                                            |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.45x faster                                                            |
| json_dumps              | 13.5 ms                                                | 9.44 ms: 1.43x faster                                                            |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.43x faster                                                            |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                                           |
| html5lib                | 85.9 ms                                                | 61.1 ms: 1.41x faster                                                            |
| chameleon               | 9.06 ms                                                | 6.51 ms: 1.39x faster                                                            |
| django_template         | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                            |
| pprint_safe_repr        | 955 ms                                                 | 689 ms: 1.39x faster                                                             |
| scimark_fft             | 424 ms                                                 | 305 ms: 1.39x faster                                                             |
| aiohttp                 | 1.38 ms                                                | 999 us: 1.38x faster                                                             |
| logging_format          | 8.91 us                                                | 6.48 us: 1.37x faster                                                            |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                             |
| logging_simple          | 8.07 us                                                | 5.88 us: 1.37x faster                                                            |
| thrift                  | 1.03 ms                                                | 757 us: 1.37x faster                                                             |
| async_tree_none         | 717 ms                                                 | 528 ms: 1.36x faster                                                             |
| xml_etree_process       | 74.9 ms                                                | 55.2 ms: 1.36x faster                                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.01 ms: 1.36x faster                                                            |
| genshi_xml              | 63.3 ms                                                | 46.7 ms: 1.36x faster                                                            |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                            |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                                           |
| tornado_http            | 127 ms                                                 | 94.4 ms: 1.35x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                                           |
| deepcopy                | 442 us                                                 | 329 us: 1.34x faster                                                             |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 639 ms: 1.34x faster                                                             |
| fannkuch                | 486 ms                                                 | 368 ms: 1.32x faster                                                             |
| deepcopy_reduce         | 3.82 us                                                | 2.90 us: 1.32x faster                                                            |
| nqueens                 | 100 ms                                                 | 76.9 ms: 1.30x faster                                                            |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                             |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                                            |
| docutils                | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                           |
| coroutines              | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed | 951 ms                                                 | 760 ms: 1.25x faster                                                             |
| sympy_integrate         | 24.3 ms                                                | 20.0 ms: 1.22x faster                                                            |
| json_loads              | 28.8 us                                                | 23.8 us: 1.21x faster                                                            |
| sympy_str               | 328 ms                                                 | 272 ms: 1.21x faster                                                             |
| bench_thread_pool       | 947 us                                                 | 787 us: 1.20x faster                                                             |
| dulwich_log             | 75.9 ms                                                | 63.1 ms: 1.20x faster                                                            |
| sympy_expand            | 545 ms                                                 | 459 ms: 1.19x faster                                                             |
| json                    | 5.42 ms                                                | 4.57 ms: 1.18x faster                                                            |
| xml_etree_generate      | 94.2 ms                                                | 79.7 ms: 1.18x faster                                                            |
| sympy_sum               | 185 ms                                                 | 158 ms: 1.17x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                            |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                            |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                                            |
| mdp                     | 2.82 sec                                               | 2.51 sec: 1.12x faster                                                           |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                            |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                                             |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                             |
| regex_dna               | 222 ms                                                 | 206 ms: 1.08x faster                                                             |
| pickle_list             | 4.56 us                                                | 4.25 us: 1.07x faster                                                            |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                                            |
| telco                   | 6.54 ms                                                | 6.38 ms: 1.03x faster                                                            |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                            |
| gc_traversal            | 3.84 ms                                                | 3.82 ms: 1.01x faster                                                            |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                             |
| generators              | 76.8 ms                                                | 76.6 ms: 1.00x faster                                                            |
| unpickle_list           | 4.82 us                                                | 4.93 us: 1.02x slower                                                            |
| regex_effbot            | 3.23 ms                                                | 3.36 ms: 1.04x slower                                                            |
| python_startup_no_site  | 5.82 ms                                                | 6.48 ms: 1.11x slower                                                            |
| pickle_dict             | 27.3 us                                                | 32.0 us: 1.17x slower                                                            |
| dask                    | 423 ms                                                 | 500 ms: 1.18x slower                                                             |
| coverage                | 72.8 ms                                                | 96.5 ms: 1.33x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                     |

Benchmark hidden because not significant (2): async_generators, bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230206-3.12.0a4+-0c3dc7b/bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x
