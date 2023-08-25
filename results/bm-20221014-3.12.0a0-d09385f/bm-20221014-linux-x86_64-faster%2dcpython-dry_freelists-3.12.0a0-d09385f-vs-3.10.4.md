
# Results vs. 3.10.4

- fork: faster-cpython
- ref: dry_freelists
- machine: linux-x86_64
- commit hash: d09385f
- commit date: 2022-10-14
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 248 ms: 1.35x faster                                                     |
| chameleon      | 9.06 ms                                                | 6.46 ms: 1.40x faster                                                    |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                   |
| html5lib       | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                    |
| tornado_http   | 127 ms                                                 | 92.8 ms: 1.37x faster                                                    |
| Geometric mean | (ref)                                                  | 1.37x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.1 ms: 1.53x faster                                                    |
| nbody          | 142 ms                                                 | 95.2 ms: 1.49x faster                                                    |
| pidigits       | 190 ms                                                 | 206 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                  | 1.28x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                     |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                    |
| regex_dna      | 222 ms                                                 | 218 ms: 1.02x faster                                                     |
| regex_effbot   | 3.23 ms                                                | 3.43 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                  | 1.11x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 287 us: 1.59x faster                                                     |
| unpickle_pure_python | 300 us                                                 | 203 us: 1.48x faster                                                     |
| json_dumps           | 13.5 ms                                                | 9.30 ms: 1.46x faster                                                    |
| xml_etree_process    | 74.9 ms                                                | 53.9 ms: 1.39x faster                                                    |
| xml_etree_generate   | 94.2 ms                                                | 75.6 ms: 1.25x faster                                                    |
| json_loads           | 28.8 us                                                | 23.4 us: 1.23x faster                                                    |
| pickle_list          | 4.56 us                                                | 4.10 us: 1.11x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                     |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                                    |
| xml_etree_parse      | 163 ms                                                 | 158 ms: 1.04x faster                                                     |
| unpickle_list        | 4.82 us                                                | 4.96 us: 1.03x slower                                                    |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                             |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.41 ms: 1.68x faster                                                    |
| python_startup_no_site | 5.82 ms                                                | 5.94 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.28x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.89 ms: 1.49x faster                                                    |
| genshi_text     | 30.3 ms                                                | 20.8 ms: 1.46x faster                                                    |
| django_template | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                    |
| genshi_xml      | 63.3 ms                                                | 49.1 ms: 1.29x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.27 ms: 2.27x faster                                                    |
| logging_silent          | 175 ns                                                 | 92.5 ns: 1.89x faster                                                    |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                                     |
| richards                | 74.9 ms                                                | 42.3 ms: 1.77x faster                                                    |
| go                      | 229 ms                                                 | 131 ms: 1.75x faster                                                     |
| pyflate                 | 673 ms                                                 | 400 ms: 1.68x faster                                                     |
| python_startup          | 14.2 ms                                                | 8.41 ms: 1.68x faster                                                    |
| scimark_monte_carlo     | 108 ms                                                 | 65.9 ms: 1.64x faster                                                    |
| chaos                   | 106 ms                                                 | 66.2 ms: 1.60x faster                                                    |
| raytrace                | 464 ms                                                 | 290 ms: 1.60x faster                                                     |
| pickle_pure_python      | 455 us                                                 | 287 us: 1.59x faster                                                     |
| hexiom                  | 9.53 ms                                                | 6.08 ms: 1.57x faster                                                    |
| crypto_pyaes            | 118 ms                                                 | 75.9 ms: 1.56x faster                                                    |
| sqlglot_parse           | 2.06 ms                                                | 1.34 ms: 1.53x faster                                                    |
| float                   | 111 ms                                                 | 72.1 ms: 1.53x faster                                                    |
| deepcopy_memo           | 52.3 us                                                | 34.7 us: 1.51x faster                                                    |
| sqlglot_transpile       | 2.45 ms                                                | 1.63 ms: 1.50x faster                                                    |
| mako                    | 14.8 ms                                                | 9.89 ms: 1.49x faster                                                    |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.49x faster                                                     |
| nbody                   | 142 ms                                                 | 95.2 ms: 1.49x faster                                                    |
| unpickle_pure_python    | 300 us                                                 | 203 us: 1.48x faster                                                     |
| spectral_norm           | 150 ms                                                 | 102 ms: 1.47x faster                                                     |
| unpack_sequence         | 64.7 ns                                                | 44.0 ns: 1.47x faster                                                    |
| genshi_text             | 30.3 ms                                                | 20.8 ms: 1.46x faster                                                    |
| json_dumps              | 13.5 ms                                                | 9.30 ms: 1.46x faster                                                    |
| html5lib                | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                    |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                                   |
| pprint_safe_repr        | 955 ms                                                 | 670 ms: 1.42x faster                                                     |
| django_template         | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                    |
| chameleon               | 9.06 ms                                                | 6.46 ms: 1.40x faster                                                    |
| logging_simple          | 8.07 us                                                | 5.76 us: 1.40x faster                                                    |
| logging_format          | 8.91 us                                                | 6.37 us: 1.40x faster                                                    |
| async_tree_none         | 717 ms                                                 | 514 ms: 1.40x faster                                                     |
| aiohttp                 | 1.38 ms                                                | 991 us: 1.40x faster                                                     |
| thrift                  | 1.03 ms                                                | 742 us: 1.39x faster                                                     |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                     |
| xml_etree_process       | 74.9 ms                                                | 53.9 ms: 1.39x faster                                                    |
| tornado_http            | 127 ms                                                 | 92.8 ms: 1.37x faster                                                    |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                                    |
| 2to3                    | 336 ms                                                 | 248 ms: 1.35x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.35x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                                   |
| scimark_fft             | 424 ms                                                 | 315 ms: 1.35x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.05 ms: 1.35x faster                                                    |
| async_tree_memoization  | 854 ms                                                 | 636 ms: 1.34x faster                                                     |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                                     |
| fannkuch                | 486 ms                                                 | 366 ms: 1.33x faster                                                     |
| async_tree_cpu_io_mixed | 951 ms                                                 | 724 ms: 1.31x faster                                                     |
| deepcopy_reduce         | 3.82 us                                                | 2.92 us: 1.31x faster                                                    |
| coroutines              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                    |
| genshi_xml              | 63.3 ms                                                | 49.1 ms: 1.29x faster                                                    |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                     |
| sqlglot_optimize        | 65.3 ms                                                | 51.5 ms: 1.27x faster                                                    |
| nqueens                 | 100 ms                                                 | 78.9 ms: 1.27x faster                                                    |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                   |
| sqlalchemy_imperative   | 21.2 ms                                                | 16.7 ms: 1.27x faster                                                    |
| xml_etree_generate      | 94.2 ms                                                | 75.6 ms: 1.25x faster                                                    |
| sqlalchemy_declarative  | 165 ms                                                 | 133 ms: 1.25x faster                                                     |
| json_loads              | 28.8 us                                                | 23.4 us: 1.23x faster                                                    |
| async_generators        | 425 ms                                                 | 349 ms: 1.22x faster                                                     |
| bench_thread_pool       | 947 us                                                 | 782 us: 1.21x faster                                                     |
| json                    | 5.42 ms                                                | 4.48 ms: 1.21x faster                                                    |
| dulwich_log             | 75.9 ms                                                | 62.8 ms: 1.21x faster                                                    |
| sympy_expand            | 545 ms                                                 | 453 ms: 1.20x faster                                                     |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.20x faster                                                    |
| sympy_str               | 328 ms                                                 | 280 ms: 1.17x faster                                                     |
| pylint                  | 525 ms                                                 | 453 ms: 1.16x faster                                                     |
| create_gc_cycles        | 1.67 ms                                                | 1.44 ms: 1.16x faster                                                    |
| sqlite_synth            | 2.93 us                                                | 2.56 us: 1.14x faster                                                    |
| sympy_sum               | 185 ms                                                 | 162 ms: 1.14x faster                                                     |
| regex_v8                | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                    |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                    |
| pickle_list             | 4.56 us                                                | 4.10 us: 1.11x faster                                                    |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                                    |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                                     |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                     |
| mdp                     | 2.82 sec                                               | 2.59 sec: 1.09x faster                                                   |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                                    |
| asyncio_tcp             | 925 ms                                                 | 872 ms: 1.06x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 158 ms: 1.04x faster                                                     |
| generators              | 76.8 ms                                                | 75.4 ms: 1.02x faster                                                    |
| regex_dna               | 222 ms                                                 | 218 ms: 1.02x faster                                                     |
| python_startup_no_site  | 5.82 ms                                                | 5.94 ms: 1.02x slower                                                    |
| unpickle_list           | 4.82 us                                                | 4.96 us: 1.03x slower                                                    |
| gc_traversal            | 3.84 ms                                                | 4.03 ms: 1.05x slower                                                    |
| regex_effbot            | 3.23 ms                                                | 3.43 ms: 1.06x slower                                                    |
| pidigits                | 190 ms                                                 | 206 ms: 1.08x slower                                                     |
| pickle_dict             | 27.3 us                                                | 31.1 us: 1.14x slower                                                    |
| dask                    | 423 ms                                                 | 496 ms: 1.17x slower                                                     |
| coverage                | 72.8 ms                                                | 98.3 ms: 1.35x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                             |

Benchmark hidden because not significant (3): pickle, bench_mp_pool, telco
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221014-3.12.0a0-d09385f/bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x
