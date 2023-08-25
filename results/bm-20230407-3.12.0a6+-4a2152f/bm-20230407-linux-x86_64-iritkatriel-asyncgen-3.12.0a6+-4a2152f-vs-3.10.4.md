
# Results vs. 3.10.4

- fork: iritkatriel
- ref: asyncgen
- machine: linux-x86_64
- commit hash: 4a2152f
- commit date: 2023-04-07
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                            |
| chameleon      | 9.06 ms                                                | 6.54 ms: 1.39x faster                                           |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                          |
| html5lib       | 85.9 ms                                                | 62.0 ms: 1.38x faster                                           |
| tornado_http   | 127 ms                                                 | 90.9 ms: 1.40x faster                                           |
| Geometric mean | (ref)                                                  | 1.35x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.4 ms: 1.62x faster                                           |
| float          | 111 ms                                                 | 74.4 ms: 1.48x faster                                           |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                  | 1.34x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                            |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                           |
| regex_dna      | 222 ms                                                 | 213 ms: 1.04x faster                                            |
| regex_effbot   | 3.23 ms                                                | 3.74 ms: 1.16x slower                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 287 us: 1.59x faster                                            |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.51x faster                                            |
| json_dumps           | 13.5 ms                                                | 9.59 ms: 1.41x faster                                           |
| xml_etree_process    | 74.9 ms                                                | 55.0 ms: 1.36x faster                                           |
| json_loads           | 28.8 us                                                | 24.3 us: 1.19x faster                                           |
| xml_etree_generate   | 94.2 ms                                                | 80.6 ms: 1.17x faster                                           |
| xml_etree_iterparse  | 111 ms                                                 | 99.4 ms: 1.12x faster                                           |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                            |
| pickle_list          | 4.56 us                                                | 4.24 us: 1.07x faster                                           |
| unpickle             | 14.1 us                                                | 13.4 us: 1.05x faster                                           |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                           |
| unpickle_list        | 4.82 us                                                | 4.98 us: 1.03x slower                                           |
| pickle_dict          | 27.3 us                                                | 32.2 us: 1.18x slower                                           |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.84 ms: 1.60x faster                                           |
| python_startup_no_site | 5.82 ms                                                | 6.52 ms: 1.12x slower                                           |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.97 ms: 1.48x faster                                           |
| genshi_text     | 30.3 ms                                                | 21.6 ms: 1.40x faster                                           |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                           |
| genshi_xml      | 63.3 ms                                                | 47.8 ms: 1.32x faster                                           |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                    |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.6 ms: 2.59x faster                                           |
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.33x faster                                           |
| logging_silent          | 175 ns                                                 | 94.5 ns: 1.85x faster                                           |
| asyncio_tcp             | 925 ms                                                 | 507 ms: 1.82x faster                                            |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.78x faster                                            |
| richards                | 74.9 ms                                                | 44.3 ms: 1.69x faster                                           |
| raytrace                | 464 ms                                                 | 280 ms: 1.66x faster                                            |
| go                      | 229 ms                                                 | 140 ms: 1.64x faster                                            |
| nbody                   | 142 ms                                                 | 87.4 ms: 1.62x faster                                           |
| chaos                   | 106 ms                                                 | 66.3 ms: 1.60x faster                                           |
| python_startup          | 14.2 ms                                                | 8.84 ms: 1.60x faster                                           |
| pyflate                 | 673 ms                                                 | 421 ms: 1.60x faster                                            |
| crypto_pyaes            | 118 ms                                                 | 74.0 ms: 1.60x faster                                           |
| pickle_pure_python      | 455 us                                                 | 287 us: 1.59x faster                                            |
| hexiom                  | 9.53 ms                                                | 6.04 ms: 1.58x faster                                           |
| scimark_monte_carlo     | 108 ms                                                 | 68.9 ms: 1.57x faster                                           |
| spectral_norm           | 150 ms                                                 | 96.2 ms: 1.56x faster                                           |
| deepcopy_memo           | 52.3 us                                                | 34.0 us: 1.54x faster                                           |
| unpack_sequence         | 64.7 ns                                                | 42.7 ns: 1.52x faster                                           |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.51x faster                                            |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                            |
| float                   | 111 ms                                                 | 74.4 ms: 1.48x faster                                           |
| mako                    | 14.8 ms                                                | 9.97 ms: 1.48x faster                                           |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                           |
| logging_format          | 8.91 us                                                | 6.25 us: 1.43x faster                                           |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.42x faster                                           |
| logging_simple          | 8.07 us                                                | 5.70 us: 1.42x faster                                           |
| json_dumps              | 13.5 ms                                                | 9.59 ms: 1.41x faster                                           |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.40x faster                                          |
| genshi_text             | 30.3 ms                                                | 21.6 ms: 1.40x faster                                           |
| tornado_http            | 127 ms                                                 | 90.9 ms: 1.40x faster                                           |
| django_template         | 45.9 ms                                                | 33.0 ms: 1.39x faster                                           |
| pprint_safe_repr        | 955 ms                                                 | 687 ms: 1.39x faster                                            |
| chameleon               | 9.06 ms                                                | 6.54 ms: 1.39x faster                                           |
| html5lib                | 85.9 ms                                                | 62.0 ms: 1.38x faster                                           |
| scimark_fft             | 424 ms                                                 | 307 ms: 1.38x faster                                            |
| deepcopy                | 442 us                                                 | 322 us: 1.37x faster                                            |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                           |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                          |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                            |
| coroutines              | 31.8 ms                                                | 23.3 ms: 1.37x faster                                           |
| xml_etree_process       | 74.9 ms                                                | 55.0 ms: 1.36x faster                                           |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                           |
| async_tree_memoization  | 854 ms                                                 | 637 ms: 1.34x faster                                            |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                            |
| thrift                  | 1.03 ms                                                | 781 us: 1.32x faster                                            |
| genshi_xml              | 63.3 ms                                                | 47.8 ms: 1.32x faster                                           |
| deepcopy_reduce         | 3.82 us                                                | 2.90 us: 1.32x faster                                           |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                            |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.31x faster                                          |
| mypy2                   | 428 ms                                                 | 332 ms: 1.29x faster                                            |
| async_tree_cpu_io_mixed | 951 ms                                                 | 739 ms: 1.29x faster                                            |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                            |
| sqlglot_optimize        | 65.3 ms                                                | 51.2 ms: 1.28x faster                                           |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.33 ms: 1.26x faster                                           |
| nqueens                 | 100 ms                                                 | 80.1 ms: 1.25x faster                                           |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                          |
| fannkuch                | 486 ms                                                 | 394 ms: 1.23x faster                                            |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                            |
| dulwich_log             | 75.9 ms                                                | 63.0 ms: 1.21x faster                                           |
| bench_thread_pool       | 947 us                                                 | 790 us: 1.20x faster                                            |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.7 ms: 1.19x faster                                           |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                           |
| sympy_expand            | 545 ms                                                 | 460 ms: 1.19x faster                                            |
| json_loads              | 28.8 us                                                | 24.3 us: 1.19x faster                                           |
| xml_etree_generate      | 94.2 ms                                                | 80.6 ms: 1.17x faster                                           |
| json                    | 5.42 ms                                                | 4.65 ms: 1.16x faster                                           |
| sympy_str               | 328 ms                                                 | 284 ms: 1.16x faster                                            |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                           |
| mdp                     | 2.82 sec                                               | 2.50 sec: 1.13x faster                                          |
| comprehensions          | 26.8 us                                                | 23.8 us: 1.13x faster                                           |
| sqlite_synth            | 2.93 us                                                | 2.61 us: 1.12x faster                                           |
| xml_etree_iterparse     | 111 ms                                                 | 99.4 ms: 1.12x faster                                           |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.12x faster                                            |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                           |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                            |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.11x faster                                           |
| djangocms               | 35.9 us                                                | 32.5 us: 1.11x faster                                           |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                            |
| pickle_list             | 4.56 us                                                | 4.24 us: 1.07x faster                                           |
| unpickle                | 14.1 us                                                | 13.4 us: 1.05x faster                                           |
| async_generators        | 425 ms                                                 | 407 ms: 1.04x faster                                            |
| regex_dna               | 222 ms                                                 | 213 ms: 1.04x faster                                            |
| telco                   | 6.54 ms                                                | 6.46 ms: 1.01x faster                                           |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                            |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                           |
| unpickle_list           | 4.82 us                                                | 4.98 us: 1.03x slower                                           |
| python_startup_no_site  | 5.82 ms                                                | 6.52 ms: 1.12x slower                                           |
| gc_traversal            | 3.84 ms                                                | 4.32 ms: 1.12x slower                                           |
| regex_effbot            | 3.23 ms                                                | 3.74 ms: 1.16x slower                                           |
| pickle_dict             | 27.3 us                                                | 32.2 us: 1.18x slower                                           |
| dask                    | 423 ms                                                 | 509 ms: 1.21x slower                                            |
| coverage                | 72.8 ms                                                | 95.4 ms: 1.31x slower                                           |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
