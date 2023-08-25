
# Results vs. 3.10.4

- fork: faster-cpython
- ref: check_refcnt_in_bina
- machine: linux-x86_64
- commit hash: c29d369
- commit date: 2023-02-27
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 248 ms: 1.36x faster                                                             |
| chameleon      | 9.06 ms                                                | 6.51 ms: 1.39x faster                                                            |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                           |
| html5lib       | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                            |
| tornado_http   | 127 ms                                                 | 94.3 ms: 1.35x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.7 ms: 1.58x faster                                                            |
| float          | 111 ms                                                 | 72.2 ms: 1.53x faster                                                            |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                                             |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                            |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                                             |
| regex_effbot   | 3.23 ms                                                | 3.36 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 284 us: 1.60x faster                                                             |
| unpickle_pure_python | 300 us                                                 | 196 us: 1.53x faster                                                             |
| json_dumps           | 13.5 ms                                                | 9.62 ms: 1.41x faster                                                            |
| xml_etree_process    | 74.9 ms                                                | 54.9 ms: 1.37x faster                                                            |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                                            |
| xml_etree_generate   | 94.2 ms                                                | 79.7 ms: 1.18x faster                                                            |
| xml_etree_iterparse  | 111 ms                                                 | 98.7 ms: 1.13x faster                                                            |
| pickle_list          | 4.56 us                                                | 4.12 us: 1.11x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                                            |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.03x slower                                                            |
| pickle_dict          | 27.3 us                                                | 30.7 us: 1.13x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.98 ms: 1.58x faster                                                            |
| python_startup_no_site | 5.82 ms                                                | 6.51 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.92 ms: 1.49x faster                                                            |
| genshi_text     | 30.3 ms                                                | 20.9 ms: 1.45x faster                                                            |
| django_template | 45.9 ms                                                | 33.1 ms: 1.39x faster                                                            |
| genshi_xml      | 63.3 ms                                                | 46.8 ms: 1.35x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.7 ms: 2.59x faster                                                            |
| deltablue               | 7.42 ms                                                | 3.11 ms: 2.38x faster                                                            |
| scimark_sor             | 197 ms                                                 | 103 ms: 1.91x faster                                                             |
| logging_silent          | 175 ns                                                 | 92.6 ns: 1.89x faster                                                            |
| asyncio_tcp             | 925 ms                                                 | 503 ms: 1.84x faster                                                             |
| richards                | 74.9 ms                                                | 40.9 ms: 1.83x faster                                                            |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                                             |
| spectral_norm           | 150 ms                                                 | 87.7 ms: 1.71x faster                                                            |
| raytrace                | 464 ms                                                 | 278 ms: 1.67x faster                                                             |
| pyflate                 | 673 ms                                                 | 407 ms: 1.66x faster                                                             |
| crypto_pyaes            | 118 ms                                                 | 73.5 ms: 1.61x faster                                                            |
| pickle_pure_python      | 455 us                                                 | 284 us: 1.60x faster                                                             |
| scimark_monte_carlo     | 108 ms                                                 | 68.0 ms: 1.59x faster                                                            |
| nbody                   | 142 ms                                                 | 89.7 ms: 1.58x faster                                                            |
| python_startup          | 14.2 ms                                                | 8.98 ms: 1.58x faster                                                            |
| hexiom                  | 9.53 ms                                                | 6.08 ms: 1.57x faster                                                            |
| chaos                   | 106 ms                                                 | 68.4 ms: 1.55x faster                                                            |
| unpickle_pure_python    | 300 us                                                 | 196 us: 1.53x faster                                                             |
| float                   | 111 ms                                                 | 72.2 ms: 1.53x faster                                                            |
| deepcopy_memo           | 52.3 us                                                | 34.4 us: 1.52x faster                                                            |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.52x faster                                                             |
| mako                    | 14.8 ms                                                | 9.92 ms: 1.49x faster                                                            |
| unpack_sequence         | 64.7 ns                                                | 44.3 ns: 1.46x faster                                                            |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.45x faster                                                            |
| genshi_text             | 30.3 ms                                                | 20.9 ms: 1.45x faster                                                            |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                            |
| scimark_fft             | 424 ms                                                 | 300 ms: 1.41x faster                                                             |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.41x faster                                                           |
| json_dumps              | 13.5 ms                                                | 9.62 ms: 1.41x faster                                                            |
| logging_format          | 8.91 us                                                | 6.34 us: 1.41x faster                                                            |
| coroutines              | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                            |
| html5lib                | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 1.27 sec: 1.40x faster                                                           |
| pprint_safe_repr        | 955 ms                                                 | 685 ms: 1.39x faster                                                             |
| chameleon               | 9.06 ms                                                | 6.51 ms: 1.39x faster                                                            |
| logging_simple          | 8.07 us                                                | 5.81 us: 1.39x faster                                                            |
| django_template         | 45.9 ms                                                | 33.1 ms: 1.39x faster                                                            |
| async_tree_none         | 717 ms                                                 | 521 ms: 1.38x faster                                                             |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.37x faster                                                           |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                            |
| thrift                  | 1.03 ms                                                | 756 us: 1.37x faster                                                             |
| xml_etree_process       | 74.9 ms                                                | 54.9 ms: 1.37x faster                                                            |
| 2to3                    | 336 ms                                                 | 248 ms: 1.36x faster                                                             |
| genshi_xml              | 63.3 ms                                                | 46.8 ms: 1.35x faster                                                            |
| tornado_http            | 127 ms                                                 | 94.3 ms: 1.35x faster                                                            |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.35x faster                                                            |
| fannkuch                | 486 ms                                                 | 361 ms: 1.34x faster                                                             |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                                             |
| deepcopy                | 442 us                                                 | 333 us: 1.33x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 645 ms: 1.32x faster                                                             |
| sqlglot_normalize       | 135 ms                                                 | 103 ms: 1.31x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.17 ms: 1.31x faster                                                            |
| async_tree_cpu_io_mixed | 951 ms                                                 | 732 ms: 1.30x faster                                                             |
| mypy2                   | 428 ms                                                 | 331 ms: 1.29x faster                                                             |
| sqlglot_optimize        | 65.3 ms                                                | 50.5 ms: 1.29x faster                                                            |
| deepcopy_reduce         | 3.82 us                                                | 2.97 us: 1.29x faster                                                            |
| nqueens                 | 100 ms                                                 | 78.6 ms: 1.27x faster                                                            |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                           |
| bench_thread_pool       | 947 us                                                 | 784 us: 1.21x faster                                                             |
| dulwich_log             | 75.9 ms                                                | 63.2 ms: 1.20x faster                                                            |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                                            |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 139 ms: 1.19x faster                                                             |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.18x faster                                                            |
| json                    | 5.42 ms                                                | 4.57 ms: 1.18x faster                                                            |
| xml_etree_generate      | 94.2 ms                                                | 79.7 ms: 1.18x faster                                                            |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.0 ms: 1.18x faster                                                            |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                                             |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.13x faster                                                            |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                            |
| xml_etree_iterparse     | 111 ms                                                 | 98.7 ms: 1.13x faster                                                            |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                            |
| sqlite_synth            | 2.93 us                                                | 2.61 us: 1.13x faster                                                            |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.12x faster                                                             |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                                            |
| sympy_sum               | 185 ms                                                 | 167 ms: 1.11x faster                                                             |
| pickle_list             | 4.56 us                                                | 4.12 us: 1.11x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| mdp                     | 2.82 sec                                               | 2.61 sec: 1.08x faster                                                           |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                                            |
| regex_dna               | 222 ms                                                 | 209 ms: 1.06x faster                                                             |
| async_generators        | 425 ms                                                 | 410 ms: 1.04x faster                                                             |
| gc_traversal            | 3.84 ms                                                | 3.83 ms: 1.00x faster                                                            |
| unpickle_list           | 4.82 us                                                | 4.94 us: 1.03x slower                                                            |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                             |
| regex_effbot            | 3.23 ms                                                | 3.36 ms: 1.04x slower                                                            |
| python_startup_no_site  | 5.82 ms                                                | 6.51 ms: 1.12x slower                                                            |
| pickle_dict             | 27.3 us                                                | 30.7 us: 1.13x slower                                                            |
| dask                    | 423 ms                                                 | 498 ms: 1.18x slower                                                             |
| coverage                | 72.8 ms                                                | 97.5 ms: 1.34x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                     |

Benchmark hidden because not significant (3): pickle, telco, bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x
