
# Results vs. 3.10.4

- fork: python
- ref: 848bdbe166b71ab2ac2c
- machine: linux-x86_64
- commit hash: 848bdbe
- commit date: 2023-04-01
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.55 ms: 1.38x faster                                                  |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                 |
| html5lib       | 85.9 ms                                                | 61.5 ms: 1.40x faster                                                  |
| tornado_http   | 127 ms                                                 | 91.8 ms: 1.39x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 86.7 ms: 1.63x faster                                                  |
| float          | 111 ms                                                 | 74.7 ms: 1.48x faster                                                  |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                  |
| regex_dna      | 222 ms                                                 | 202 ms: 1.10x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.64 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 289 us: 1.57x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 201 us: 1.50x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.62 ms: 1.41x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 56.1 ms: 1.34x faster                                                  |
| json_loads           | 28.8 us                                                | 24.4 us: 1.18x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 81.3 ms: 1.16x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.10x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.24 us: 1.07x faster                                                  |
| unpickle             | 14.1 us                                                | 13.4 us: 1.06x faster                                                  |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.03x slower                                                  |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.83 ms: 1.60x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.52 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                  |
| genshi_text     | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                  |
| django_template | 45.9 ms                                                | 34.0 ms: 1.35x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.5 ms: 2.60x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.24 ms: 2.29x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 506 ms: 1.83x faster                                                   |
| logging_silent          | 175 ns                                                 | 96.1 ns: 1.82x faster                                                  |
| scimark_sor             | 197 ms                                                 | 113 ms: 1.74x faster                                                   |
| richards                | 74.9 ms                                                | 43.6 ms: 1.72x faster                                                  |
| go                      | 229 ms                                                 | 140 ms: 1.63x faster                                                   |
| raytrace                | 464 ms                                                 | 284 ms: 1.63x faster                                                   |
| nbody                   | 142 ms                                                 | 86.7 ms: 1.63x faster                                                  |
| pyflate                 | 673 ms                                                 | 417 ms: 1.62x faster                                                   |
| scimark_monte_carlo     | 108 ms                                                 | 67.1 ms: 1.61x faster                                                  |
| crypto_pyaes            | 118 ms                                                 | 73.8 ms: 1.61x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.83 ms: 1.60x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.03 ms: 1.58x faster                                                  |
| spectral_norm           | 150 ms                                                 | 95.2 ms: 1.57x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 289 us: 1.57x faster                                                   |
| chaos                   | 106 ms                                                 | 67.7 ms: 1.57x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 43.2 ns: 1.50x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 201 us: 1.50x faster                                                   |
| deepcopy_memo           | 52.3 us                                                | 35.0 us: 1.49x faster                                                  |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.49x faster                                                   |
| float                   | 111 ms                                                 | 74.7 ms: 1.48x faster                                                  |
| mako                    | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.43x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.73 ms: 1.41x faster                                                  |
| logging_format          | 8.91 us                                                | 6.31 us: 1.41x faster                                                  |
| genshi_text             | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.62 ms: 1.41x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.76 us: 1.40x faster                                                  |
| html5lib                | 85.9 ms                                                | 61.5 ms: 1.40x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.43 sec: 1.39x faster                                                 |
| tornado_http            | 127 ms                                                 | 91.8 ms: 1.39x faster                                                  |
| scimark_fft             | 424 ms                                                 | 306 ms: 1.38x faster                                                   |
| chameleon               | 9.06 ms                                                | 6.55 ms: 1.38x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 695 ms: 1.37x faster                                                   |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                                 |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.36x faster                                                 |
| django_template         | 45.9 ms                                                | 34.0 ms: 1.35x faster                                                  |
| genshi_xml              | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                  |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                  |
| deepcopy                | 442 us                                                 | 331 us: 1.34x faster                                                   |
| xml_etree_process       | 74.9 ms                                                | 56.1 ms: 1.34x faster                                                  |
| coroutines              | 31.8 ms                                                | 23.9 ms: 1.33x faster                                                  |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                   |
| thrift                  | 1.03 ms                                                | 782 us: 1.32x faster                                                   |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 658 ms: 1.30x faster                                                   |
| fannkuch                | 486 ms                                                 | 376 ms: 1.29x faster                                                   |
| mypy2                   | 428 ms                                                 | 332 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 742 ms: 1.28x faster                                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.98 us: 1.28x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.27 ms: 1.28x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.6 ms: 1.27x faster                                                  |
| nqueens                 | 100 ms                                                 | 79.8 ms: 1.25x faster                                                  |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                 |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                   |
| bench_thread_pool       | 947 us                                                 | 790 us: 1.20x faster                                                   |
| dulwich_log             | 75.9 ms                                                | 63.7 ms: 1.19x faster                                                  |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.9 ms: 1.18x faster                                                  |
| json_loads              | 28.8 us                                                | 24.4 us: 1.18x faster                                                  |
| sympy_expand            | 545 ms                                                 | 461 ms: 1.18x faster                                                   |
| xml_etree_generate      | 94.2 ms                                                | 81.3 ms: 1.16x faster                                                  |
| json                    | 5.42 ms                                                | 4.68 ms: 1.16x faster                                                  |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                  |
| sympy_str               | 328 ms                                                 | 285 ms: 1.15x faster                                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.50 sec: 1.13x faster                                                 |
| comprehensions          | 26.8 us                                                | 23.8 us: 1.13x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.63 us: 1.12x faster                                                  |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                                   |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                   |
| djangocms               | 35.9 us                                                | 32.5 us: 1.10x faster                                                  |
| regex_dna               | 222 ms                                                 | 202 ms: 1.10x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.10x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.24 us: 1.07x faster                                                  |
| unpickle                | 14.1 us                                                | 13.4 us: 1.06x faster                                                  |
| async_generators        | 425 ms                                                 | 416 ms: 1.02x faster                                                   |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                   |
| unpickle_list           | 4.82 us                                                | 4.99 us: 1.03x slower                                                  |
| gc_traversal            | 3.84 ms                                                | 4.07 ms: 1.06x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.52 ms: 1.12x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.64 ms: 1.13x slower                                                  |
| pickle_dict             | 27.3 us                                                | 31.6 us: 1.16x slower                                                  |
| dask                    | 423 ms                                                 | 514 ms: 1.22x slower                                                   |
| coverage                | 72.8 ms                                                | 98.0 ms: 1.35x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                           |

Benchmark hidden because not significant (3): telco, pickle, bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x
