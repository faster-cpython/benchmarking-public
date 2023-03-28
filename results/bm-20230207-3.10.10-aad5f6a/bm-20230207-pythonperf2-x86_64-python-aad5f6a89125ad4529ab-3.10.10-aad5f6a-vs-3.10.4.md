
# Results vs. 3.10.4

- fork: python
- ref: aad5f6a89125ad4529ab
- machine: linux-x86_64
- commit hash: aad5f6a
- commit date: 2023-02-07
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 351 ms: 1.00x faster                                                       |
| chameleon      | 9.62 ms                                                      | 9.41 ms: 1.02x faster                                                      |
| docutils       | 3.41 sec                                                     | 3.45 sec: 1.01x slower                                                     |
| html5lib       | 96.3 ms                                                      | 94.4 ms: 1.02x faster                                                      |
| tornado_http   | 151 ms                                                       | 159 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 111 ms: 1.01x slower                                                       |
| nbody          | 132 ms                                                       | 138 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 260 ms: 1.00x faster                                                       |
| regex_compile  | 191 ms                                                       | 192 ms: 1.01x slower                                                       |
| regex_v8       | 26.0 ms                                                      | 27.2 ms: 1.05x slower                                                      |
| regex_effbot   | 2.99 ms                                                      | 3.49 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                        | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|---------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads          | 30.3 us                                                      | 30.0 us: 1.01x faster                                                      |
| json_dumps          | 14.3 ms                                                      | 14.4 ms: 1.01x slower                                                      |
| pickle_list         | 4.11 us                                                      | 4.17 us: 1.01x slower                                                      |
| pickle_pure_python  | 451 us                                                       | 461 us: 1.02x slower                                                       |
| xml_etree_parse     | 160 ms                                                       | 164 ms: 1.02x slower                                                       |
| unpickle            | 13.3 us                                                      | 13.7 us: 1.03x slower                                                      |
| xml_etree_iterparse | 109 ms                                                       | 113 ms: 1.04x slower                                                       |
| pickle_dict         | 29.5 us                                                      | 32.1 us: 1.09x slower                                                      |
| Geometric mean      | (ref)                                                        | 1.02x slower                                                               |

Benchmark hidden because not significant (5): unpickle_list, xml_etree_generate, xml_etree_process, pickle, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.32 ms                                                      | 7.34 ms: 1.00x slower                                                      |
| python_startup         | 11.5 ms                                                      | 11.5 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 63.5 ms                                                      | 62.5 ms: 1.02x faster                                                      |
| mako            | 14.7 ms                                                      | 14.7 ms: 1.01x faster                                                      |
| genshi_text     | 31.7 ms                                                      | 32.0 ms: 1.01x slower                                                      |
| django_template | 52.0 ms                                                      | 53.6 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coverage                | 71.1 ms                                                      | 63.3 ms: 1.12x faster                                                      |
| fannkuch                | 496 ms                                                       | 470 ms: 1.06x faster                                                       |
| pyflate                 | 731 ms                                                       | 696 ms: 1.05x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 1.11 ms: 1.03x faster                                                      |
| logging_simple          | 9.24 us                                                      | 8.96 us: 1.03x faster                                                      |
| logging_format          | 9.94 us                                                      | 9.67 us: 1.03x faster                                                      |
| aiohttp                 | 1.18 ms                                                      | 1.15 ms: 1.03x faster                                                      |
| coroutines              | 30.6 ms                                                      | 29.9 ms: 1.02x faster                                                      |
| chameleon               | 9.62 ms                                                      | 9.41 ms: 1.02x faster                                                      |
| html5lib                | 96.3 ms                                                      | 94.4 ms: 1.02x faster                                                      |
| meteor_contest          | 142 ms                                                       | 139 ms: 1.02x faster                                                       |
| gunicorn                | 1.15 ms                                                      | 1.13 ms: 1.02x faster                                                      |
| genshi_xml              | 63.5 ms                                                      | 62.5 ms: 1.02x faster                                                      |
| go                      | 264 ms                                                       | 260 ms: 1.01x faster                                                       |
| thrift                  | 1.23 ms                                                      | 1.21 ms: 1.01x faster                                                      |
| richards                | 73.9 ms                                                      | 72.9 ms: 1.01x faster                                                      |
| deltablue               | 7.54 ms                                                      | 7.45 ms: 1.01x faster                                                      |
| sqlglot_normalize       | 147 ms                                                       | 146 ms: 1.01x faster                                                       |
| json_loads              | 30.3 us                                                      | 30.0 us: 1.01x faster                                                      |
| asyncio_tcp             | 787 ms                                                       | 779 ms: 1.01x faster                                                       |
| comprehensions          | 27.3 us                                                      | 27.0 us: 1.01x faster                                                      |
| pprint_pformat          | 2.12 sec                                                     | 2.11 sec: 1.01x faster                                                     |
| sqlglot_optimize        | 70.1 ms                                                      | 69.6 ms: 1.01x faster                                                      |
| json                    | 5.94 ms                                                      | 5.91 ms: 1.01x faster                                                      |
| mako                    | 14.7 ms                                                      | 14.7 ms: 1.01x faster                                                      |
| regex_dna               | 261 ms                                                       | 260 ms: 1.00x faster                                                       |
| hexiom                  | 9.54 ms                                                      | 9.49 ms: 1.00x faster                                                      |
| 2to3                    | 352 ms                                                       | 351 ms: 1.00x faster                                                       |
| async_generators        | 419 ms                                                       | 417 ms: 1.00x faster                                                       |
| crypto_pyaes            | 119 ms                                                       | 118 ms: 1.00x faster                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.34 ms: 1.00x slower                                                      |
| python_startup          | 11.5 ms                                                      | 11.5 ms: 1.00x slower                                                      |
| async_tree_io           | 1.61 sec                                                     | 1.62 sec: 1.01x slower                                                     |
| sqlglot_transpile       | 2.69 ms                                                      | 2.70 ms: 1.01x slower                                                      |
| regex_compile           | 191 ms                                                       | 192 ms: 1.01x slower                                                       |
| mypy2                   | 466 ms                                                       | 469 ms: 1.01x slower                                                       |
| dulwich_log             | 80.5 ms                                                      | 81.1 ms: 1.01x slower                                                      |
| sympy_expand            | 603 ms                                                       | 608 ms: 1.01x slower                                                       |
| raytrace                | 491 ms                                                       | 495 ms: 1.01x slower                                                       |
| chaos                   | 108 ms                                                       | 109 ms: 1.01x slower                                                       |
| genshi_text             | 31.7 ms                                                      | 32.0 ms: 1.01x slower                                                      |
| scimark_monte_carlo     | 109 ms                                                       | 110 ms: 1.01x slower                                                       |
| docutils                | 3.41 sec                                                     | 3.45 sec: 1.01x slower                                                     |
| json_dumps              | 14.3 ms                                                      | 14.4 ms: 1.01x slower                                                      |
| async_tree_memoization  | 822 ms                                                       | 832 ms: 1.01x slower                                                       |
| float                   | 109 ms                                                       | 111 ms: 1.01x slower                                                       |
| sympy_integrate         | 28.1 ms                                                      | 28.5 ms: 1.01x slower                                                      |
| dask                    | 478 ms                                                       | 484 ms: 1.01x slower                                                       |
| pickle_list             | 4.11 us                                                      | 4.17 us: 1.01x slower                                                      |
| deepcopy_memo           | 49.2 us                                                      | 50.0 us: 1.02x slower                                                      |
| telco                   | 7.14 ms                                                      | 7.25 ms: 1.02x slower                                                      |
| sympy_str               | 358 ms                                                       | 364 ms: 1.02x slower                                                       |
| async_tree_none         | 698 ms                                                       | 711 ms: 1.02x slower                                                       |
| pylint                  | 562 ms                                                       | 572 ms: 1.02x slower                                                       |
| deepcopy                | 457 us                                                       | 466 us: 1.02x slower                                                       |
| pickle_pure_python      | 451 us                                                       | 461 us: 1.02x slower                                                       |
| xml_etree_parse         | 160 ms                                                       | 164 ms: 1.02x slower                                                       |
| unpickle                | 13.3 us                                                      | 13.7 us: 1.03x slower                                                      |
| django_template         | 52.0 ms                                                      | 53.6 ms: 1.03x slower                                                      |
| sympy_sum               | 193 ms                                                       | 199 ms: 1.03x slower                                                       |
| mdp                     | 2.95 sec                                                     | 3.05 sec: 1.03x slower                                                     |
| deepcopy_reduce         | 3.91 us                                                      | 4.05 us: 1.03x slower                                                      |
| scimark_lu              | 164 ms                                                       | 170 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 5.28 ms: 1.04x slower                                                      |
| xml_etree_iterparse     | 109 ms                                                       | 113 ms: 1.04x slower                                                       |
| nbody                   | 132 ms                                                       | 138 ms: 1.04x slower                                                       |
| regex_v8                | 26.0 ms                                                      | 27.2 ms: 1.05x slower                                                      |
| tornado_http            | 151 ms                                                       | 159 ms: 1.06x slower                                                       |
| scimark_fft             | 359 ms                                                       | 383 ms: 1.07x slower                                                       |
| pickle_dict             | 29.5 us                                                      | 32.1 us: 1.09x slower                                                      |
| regex_effbot            | 2.99 ms                                                      | 3.49 ms: 1.17x slower                                                      |
| gc_traversal            | 3.46 ms                                                      | 4.12 ms: 1.19x slower                                                      |
| Geometric mean          | (ref)                                                        | 1.01x slower                                                               |

Benchmark hidden because not significant (23): unpack_sequence, nqueens, sqlalchemy_declarative, unpickle_list, xml_etree_generate, scimark_sor, xml_etree_process, spectral_norm, generators, pickle, sqlalchemy_imperative, pidigits, pathlib, pprint_safe_repr, async_tree_cpu_io_mixed, sqlglot_parse, flaskblogging, create_gc_cycles, unpickle_pure_python, sqlite_synth, logging_silent, pycparser, bench_mp_pool
