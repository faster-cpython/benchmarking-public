
# Results vs. 3.10.4

- fork: python
- ref: cdde29dde90947df9bac
- machine: linux-x86_64
- commit hash: cdde29d
- commit date: 2022-11-21
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 280 ms: 1.25x faster                                                         |
| chameleon      | 9.72 ms                                                      | 7.42 ms: 1.31x faster                                                        |
| docutils       | 3.40 sec                                                     | 2.78 sec: 1.23x faster                                                       |
| html5lib       | 94.6 ms                                                      | 67.3 ms: 1.41x faster                                                        |
| tornado_http   | 152 ms                                                       | 121 ms: 1.26x faster                                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 110 ms                                                       | 73.6 ms: 1.50x faster                                                        |
| nbody          | 137 ms                                                       | 93.5 ms: 1.47x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 150 ms: 1.29x faster                                                         |
| regex_dna      | 259 ms                                                       | 227 ms: 1.14x faster                                                         |
| regex_v8       | 26.6 ms                                                      | 23.7 ms: 1.13x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.46 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 208 us: 1.54x faster                                                         |
| pickle_pure_python   | 457 us                                                       | 315 us: 1.45x faster                                                         |
| xml_etree_process    | 76.0 ms                                                      | 55.2 ms: 1.38x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                                        |
| json_loads           | 30.0 us                                                      | 24.3 us: 1.23x faster                                                        |
| xml_etree_generate   | 94.6 ms                                                      | 79.5 ms: 1.19x faster                                                        |
| xml_etree_parse      | 162 ms                                                       | 138 ms: 1.17x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.08x faster                                                         |
| unpickle             | 14.2 us                                                      | 13.4 us: 1.06x faster                                                        |
| pickle_list          | 4.11 us                                                      | 3.88 us: 1.06x faster                                                        |
| unpickle_list        | 4.49 us                                                      | 4.59 us: 1.02x slower                                                        |
| pickle_dict          | 30.0 us                                                      | 32.3 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 7.85 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| django_template | 51.5 ms                                                      | 41.0 ms: 1.26x faster                                                        |
| genshi_text     | 31.5 ms                                                      | 26.3 ms: 1.20x faster                                                        |
| genshi_xml      | 64.7 ms                                                      | 55.4 ms: 1.17x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.67 ms: 2.03x faster                                                        |
| logging_silent          | 166 ns                                                       | 99.6 ns: 1.66x faster                                                        |
| raytrace                | 488 ms                                                       | 299 ms: 1.63x faster                                                         |
| scimark_sor             | 177 ms                                                       | 109 ms: 1.63x faster                                                         |
| bench_mp_pool           | 7.18 ms                                                      | 4.42 ms: 1.63x faster                                                        |
| go                      | 259 ms                                                       | 159 ms: 1.62x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                       | 68.5 ms: 1.60x faster                                                        |
| richards                | 74.1 ms                                                      | 47.6 ms: 1.56x faster                                                        |
| pyflate                 | 697 ms                                                       | 450 ms: 1.55x faster                                                         |
| unpickle_pure_python    | 321 us                                                       | 208 us: 1.54x faster                                                         |
| float                   | 110 ms                                                       | 73.6 ms: 1.50x faster                                                        |
| sqlglot_parse           | 2.26 ms                                                      | 1.53 ms: 1.48x faster                                                        |
| nbody                   | 137 ms                                                       | 93.5 ms: 1.47x faster                                                        |
| pickle_pure_python      | 457 us                                                       | 315 us: 1.45x faster                                                         |
| scimark_lu              | 164 ms                                                       | 114 ms: 1.44x faster                                                         |
| spectral_norm           | 136 ms                                                       | 94.6 ms: 1.44x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.89 ms: 1.44x faster                                                        |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 3.65 ms: 1.42x faster                                                        |
| chaos                   | 107 ms                                                       | 75.3 ms: 1.42x faster                                                        |
| crypto_pyaes            | 118 ms                                                       | 83.6 ms: 1.41x faster                                                        |
| html5lib                | 94.6 ms                                                      | 67.3 ms: 1.41x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.39x faster                                                       |
| xml_etree_process       | 76.0 ms                                                      | 55.2 ms: 1.38x faster                                                        |
| json_dumps              | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                                        |
| async_tree_none         | 700 ms                                                       | 515 ms: 1.36x faster                                                         |
| aiohttp                 | 1.21 ms                                                      | 898 us: 1.35x faster                                                         |
| hexiom                  | 9.52 ms                                                      | 7.08 ms: 1.34x faster                                                        |
| async_tree_memoization  | 824 ms                                                       | 614 ms: 1.34x faster                                                         |
| deepcopy_memo           | 48.9 us                                                      | 36.6 us: 1.34x faster                                                        |
| pprint_safe_repr        | 1.05 sec                                                     | 788 ms: 1.33x faster                                                         |
| pprint_pformat          | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                                       |
| thrift                  | 1.16 ms                                                      | 880 us: 1.32x faster                                                         |
| gunicorn                | 1.17 ms                                                      | 889 us: 1.32x faster                                                         |
| chameleon               | 9.72 ms                                                      | 7.42 ms: 1.31x faster                                                        |
| unpack_sequence         | 59.5 ns                                                      | 45.5 ns: 1.31x faster                                                        |
| regex_compile           | 194 ms                                                       | 150 ms: 1.29x faster                                                         |
| scimark_fft             | 359 ms                                                       | 282 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed | 952 ms                                                       | 748 ms: 1.27x faster                                                         |
| async_generators        | 422 ms                                                       | 333 ms: 1.27x faster                                                         |
| pycparser               | 1.66 sec                                                     | 1.32 sec: 1.26x faster                                                       |
| tornado_http            | 152 ms                                                       | 121 ms: 1.26x faster                                                         |
| django_template         | 51.5 ms                                                      | 41.0 ms: 1.26x faster                                                        |
| logging_simple          | 8.90 us                                                      | 7.08 us: 1.26x faster                                                        |
| 2to3                    | 350 ms                                                       | 280 ms: 1.25x faster                                                         |
| logging_format          | 9.57 us                                                      | 7.65 us: 1.25x faster                                                        |
| mypy2                   | 466 ms                                                       | 374 ms: 1.25x faster                                                         |
| json_loads              | 30.0 us                                                      | 24.3 us: 1.23x faster                                                        |
| docutils                | 3.40 sec                                                     | 2.78 sec: 1.23x faster                                                       |
| deepcopy_reduce         | 4.03 us                                                      | 3.35 us: 1.20x faster                                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 58.5 ms: 1.20x faster                                                        |
| genshi_text             | 31.5 ms                                                      | 26.3 ms: 1.20x faster                                                        |
| fannkuch                | 496 ms                                                       | 416 ms: 1.19x faster                                                         |
| xml_etree_generate      | 94.6 ms                                                      | 79.5 ms: 1.19x faster                                                        |
| dulwich_log             | 80.1 ms                                                      | 67.4 ms: 1.19x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 957 us: 1.19x faster                                                         |
| sqlglot_normalize       | 144 ms                                                       | 122 ms: 1.19x faster                                                         |
| json                    | 5.96 ms                                                      | 5.07 ms: 1.18x faster                                                        |
| deepcopy                | 454 us                                                       | 388 us: 1.17x faster                                                         |
| genshi_xml              | 64.7 ms                                                      | 55.4 ms: 1.17x faster                                                        |
| xml_etree_parse         | 162 ms                                                       | 138 ms: 1.17x faster                                                         |
| sqlite_synth            | 2.97 us                                                      | 2.56 us: 1.16x faster                                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.59 ms: 1.14x faster                                                        |
| regex_dna               | 259 ms                                                       | 227 ms: 1.14x faster                                                         |
| nqueens                 | 112 ms                                                       | 99.6 ms: 1.13x faster                                                        |
| regex_v8                | 26.6 ms                                                      | 23.7 ms: 1.13x faster                                                        |
| pathlib                 | 21.7 ms                                                      | 19.3 ms: 1.12x faster                                                        |
| dask                    | 463 ms                                                       | 416 ms: 1.11x faster                                                         |
| coroutines              | 30.4 ms                                                      | 27.6 ms: 1.10x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.6 ms: 1.10x faster                                                        |
| sympy_expand            | 599 ms                                                       | 547 ms: 1.10x faster                                                         |
| mdp                     | 3.03 sec                                                     | 2.78 sec: 1.09x faster                                                       |
| xml_etree_iterparse     | 110 ms                                                       | 102 ms: 1.08x faster                                                         |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| meteor_contest          | 137 ms                                                       | 127 ms: 1.07x faster                                                         |
| sympy_str               | 358 ms                                                       | 335 ms: 1.07x faster                                                         |
| python_startup          | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.74 ms: 1.06x faster                                                        |
| unpickle                | 14.2 us                                                      | 13.4 us: 1.06x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.88 us: 1.06x faster                                                        |
| asyncio_tcp             | 782 ms                                                       | 744 ms: 1.05x faster                                                         |
| sympy_sum               | 193 ms                                                       | 185 ms: 1.04x faster                                                         |
| comprehensions          | 26.9 us                                                      | 27.5 us: 1.02x slower                                                        |
| unpickle_list           | 4.49 us                                                      | 4.59 us: 1.02x slower                                                        |
| gc_traversal            | 3.45 ms                                                      | 3.61 ms: 1.04x slower                                                        |
| generators              | 58.0 ms                                                      | 60.8 ms: 1.05x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 7.85 ms: 1.07x slower                                                        |
| pickle_dict             | 30.0 us                                                      | 32.3 us: 1.08x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.46 ms: 1.16x slower                                                        |
| coverage                | 64.0 ms                                                      | 86.9 ms: 1.36x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.24x faster                                                                 |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.19x
