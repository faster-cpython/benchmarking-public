
# Results vs. 3.10.4

- fork: faster-cpython
- ref: nogil_latest
- machine: linux-x86_64
- commit hash: 1d39009
- commit date: 2023-04-16
- overall geometric mean: 1.19x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 290 ms: 1.16x faster                                                    |
| chameleon      | 9.06 ms                                                | 7.81 ms: 1.16x faster                                                   |
| docutils       | 3.17 sec                                               | 3.15 sec: 1.01x faster                                                  |
| html5lib       | 85.9 ms                                                | 69.2 ms: 1.24x faster                                                   |
| Geometric mean | (ref)                                                  | 1.14x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 111 ms                                                 | 65.9 ms: 1.68x faster                                                   |
| nbody          | 142 ms                                                 | 107 ms: 1.32x faster                                                    |
| pidigits       | 190 ms                                                 | 186 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.31x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.0 ms                                                | 21.1 ms: 1.19x faster                                                   |
| regex_compile  | 177 ms                                                 | 152 ms: 1.16x faster                                                    |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                                    |
| regex_effbot   | 3.23 ms                                                | 3.46 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 321 us: 1.42x faster                                                    |
| unpickle_pure_python | 300 us                                                 | 229 us: 1.31x faster                                                    |
| json_dumps           | 13.5 ms                                                | 10.4 ms: 1.30x faster                                                   |
| xml_etree_process    | 74.9 ms                                                | 61.3 ms: 1.22x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 137 ms: 1.19x faster                                                    |
| xml_etree_generate   | 94.2 ms                                                | 83.7 ms: 1.12x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.33 us: 1.05x faster                                                   |
| json_loads           | 28.8 us                                                | 28.0 us: 1.03x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 114 ms: 1.02x slower                                                    |
| unpickle_list        | 4.82 us                                                | 5.20 us: 1.08x slower                                                   |
| unpickle             | 14.1 us                                                | 15.5 us: 1.09x slower                                                   |
| pickle_dict          | 27.3 us                                                | 30.0 us: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                            |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.18 ms: 1.54x faster                                                   |
| python_startup_no_site | 5.82 ms                                                | 6.59 ms: 1.13x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 30.3 ms                                                | 24.4 ms: 1.25x faster                                                   |
| django_template | 45.9 ms                                                | 37.4 ms: 1.23x faster                                                   |
| genshi_xml      | 63.3 ms                                                | 52.0 ms: 1.22x faster                                                   |
| mako            | 14.8 ms                                                | 13.2 ms: 1.11x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.88x faster                                                    |
| async_tree_none         | 717 ms                                                 | 311 ms: 2.30x faster                                                    |
| async_tree_memoization  | 854 ms                                                 | 381 ms: 2.24x faster                                                    |
| deltablue               | 7.42 ms                                                | 3.91 ms: 1.89x faster                                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 534 ms: 1.78x faster                                                    |
| asyncio_tcp             | 925 ms                                                 | 525 ms: 1.76x faster                                                    |
| logging_silent          | 175 ns                                                 | 104 ns: 1.69x faster                                                    |
| float                   | 111 ms                                                 | 65.9 ms: 1.68x faster                                                   |
| scimark_sor             | 197 ms                                                 | 123 ms: 1.60x faster                                                    |
| go                      | 229 ms                                                 | 146 ms: 1.57x faster                                                    |
| richards                | 74.9 ms                                                | 48.4 ms: 1.55x faster                                                   |
| python_startup          | 14.2 ms                                                | 9.18 ms: 1.54x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 81.8 ms: 1.45x faster                                                   |
| pyflate                 | 673 ms                                                 | 470 ms: 1.43x faster                                                    |
| chaos                   | 106 ms                                                 | 74.6 ms: 1.42x faster                                                   |
| pickle_pure_python      | 455 us                                                 | 321 us: 1.42x faster                                                    |
| scimark_monte_carlo     | 108 ms                                                 | 76.4 ms: 1.42x faster                                                   |
| hexiom                  | 9.53 ms                                                | 6.89 ms: 1.38x faster                                                   |
| raytrace                | 464 ms                                                 | 346 ms: 1.34x faster                                                    |
| spectral_norm           | 150 ms                                                 | 112 ms: 1.34x faster                                                    |
| nbody                   | 142 ms                                                 | 107 ms: 1.32x faster                                                    |
| unpickle_pure_python    | 300 us                                                 | 229 us: 1.31x faster                                                    |
| deepcopy_memo           | 52.3 us                                                | 40.1 us: 1.31x faster                                                   |
| json_dumps              | 13.5 ms                                                | 10.4 ms: 1.30x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.30x faster                                                  |
| scimark_lu              | 163 ms                                                 | 128 ms: 1.28x faster                                                    |
| pprint_pformat          | 1.99 sec                                               | 1.58 sec: 1.26x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 765 ms: 1.25x faster                                                    |
| genshi_text             | 30.3 ms                                                | 24.4 ms: 1.25x faster                                                   |
| html5lib                | 85.9 ms                                                | 69.2 ms: 1.24x faster                                                   |
| django_template         | 45.9 ms                                                | 37.4 ms: 1.23x faster                                                   |
| xml_etree_process       | 74.9 ms                                                | 61.3 ms: 1.22x faster                                                   |
| genshi_xml              | 63.3 ms                                                | 52.0 ms: 1.22x faster                                                   |
| thrift                  | 1.03 ms                                                | 851 us: 1.21x faster                                                    |
| regex_v8                | 25.0 ms                                                | 21.1 ms: 1.19x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 137 ms: 1.19x faster                                                    |
| coroutines              | 31.8 ms                                                | 26.8 ms: 1.19x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 115 ms: 1.18x faster                                                    |
| deepcopy                | 442 us                                                 | 375 us: 1.18x faster                                                    |
| sqlglot_transpile       | 2.45 ms                                                | 2.10 ms: 1.17x faster                                                   |
| nqueens                 | 100 ms                                                 | 85.8 ms: 1.17x faster                                                   |
| regex_compile           | 177 ms                                                 | 152 ms: 1.16x faster                                                    |
| logging_format          | 8.91 us                                                | 7.66 us: 1.16x faster                                                   |
| chameleon               | 9.06 ms                                                | 7.81 ms: 1.16x faster                                                   |
| 2to3                    | 336 ms                                                 | 290 ms: 1.16x faster                                                    |
| logging_simple          | 8.07 us                                                | 7.00 us: 1.15x faster                                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.79 ms: 1.15x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 57.1 ms: 1.14x faster                                                   |
| async_generators        | 425 ms                                                 | 377 ms: 1.13x faster                                                    |
| xml_etree_generate      | 94.2 ms                                                | 83.7 ms: 1.12x faster                                                   |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                   |
| deepcopy_reduce         | 3.82 us                                                | 3.42 us: 1.12x faster                                                   |
| dulwich_log             | 75.9 ms                                                | 68.1 ms: 1.12x faster                                                   |
| fannkuch                | 486 ms                                                 | 436 ms: 1.11x faster                                                    |
| mako                    | 14.8 ms                                                | 13.2 ms: 1.11x faster                                                   |
| unpack_sequence         | 64.7 ns                                                | 58.1 ns: 1.11x faster                                                   |
| scimark_fft             | 424 ms                                                 | 383 ms: 1.11x faster                                                    |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.94 ms: 1.10x faster                                                   |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                                   |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                                    |
| json                    | 5.42 ms                                                | 5.06 ms: 1.07x faster                                                   |
| sympy_integrate         | 24.3 ms                                                | 22.8 ms: 1.06x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.33 us: 1.05x faster                                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.59 ms: 1.05x faster                                                   |
| gc_traversal            | 3.84 ms                                                | 3.67 ms: 1.05x faster                                                   |
| json_loads              | 28.8 us                                                | 28.0 us: 1.03x faster                                                   |
| pidigits                | 190 ms                                                 | 186 ms: 1.02x faster                                                    |
| comprehensions          | 26.8 us                                                | 26.3 us: 1.02x faster                                                   |
| sympy_expand            | 545 ms                                                 | 537 ms: 1.01x faster                                                    |
| mdp                     | 2.82 sec                                               | 2.79 sec: 1.01x faster                                                  |
| docutils                | 3.17 sec                                               | 3.15 sec: 1.01x faster                                                  |
| bench_mp_pool           | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 114 ms: 1.02x slower                                                    |
| generators              | 76.8 ms                                                | 78.8 ms: 1.03x slower                                                   |
| sympy_sum               | 185 ms                                                 | 192 ms: 1.04x slower                                                    |
| djangocms               | 35.9 us                                                | 37.9 us: 1.05x slower                                                   |
| telco                   | 6.54 ms                                                | 6.92 ms: 1.06x slower                                                   |
| mypy2                   | 428 ms                                                 | 457 ms: 1.07x slower                                                    |
| regex_effbot            | 3.23 ms                                                | 3.46 ms: 1.07x slower                                                   |
| unpickle_list           | 4.82 us                                                | 5.20 us: 1.08x slower                                                   |
| meteor_contest          | 115 ms                                                 | 124 ms: 1.08x slower                                                    |
| unpickle                | 14.1 us                                                | 15.5 us: 1.09x slower                                                   |
| pickle_dict             | 27.3 us                                                | 30.0 us: 1.10x slower                                                   |
| python_startup_no_site  | 5.82 ms                                                | 6.59 ms: 1.13x slower                                                   |
| coverage                | 72.8 ms                                                | 109 ms: 1.50x slower                                                    |
| bench_thread_pool       | 947 us                                                 | 1.64 ms: 1.74x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.19x faster                                                            |

Benchmark hidden because not significant (2): pickle, sympy_str
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x
