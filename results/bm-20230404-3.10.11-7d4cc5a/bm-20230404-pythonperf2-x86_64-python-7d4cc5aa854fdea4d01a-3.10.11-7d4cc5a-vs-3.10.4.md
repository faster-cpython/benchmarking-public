
# Results vs. 3.10.4

- fork: python
- ref: 7d4cc5aa854fdea4d01a
- machine: linux-x86_64
- commit hash: 7d4cc5a
- commit date: 2023-04-04
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 350 ms: 1.01x faster                                                       |
| chameleon      | 9.62 ms                                                      | 9.41 ms: 1.02x faster                                                      |
| docutils       | 3.41 sec                                                     | 3.42 sec: 1.00x slower                                                     |
| html5lib       | 96.3 ms                                                      | 93.6 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                        | 1.01x faster                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 271 ms: 1.00x slower                                                       |
| float          | 109 ms                                                       | 110 ms: 1.01x slower                                                       |
| nbody          | 132 ms                                                       | 137 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 259 ms: 1.01x faster                                                       |
| regex_compile  | 191 ms                                                       | 191 ms: 1.00x slower                                                       |
| regex_v8       | 26.0 ms                                                      | 27.1 ms: 1.04x slower                                                      |
| regex_effbot   | 2.99 ms                                                      | 3.25 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                        | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_list        | 4.73 us                                                      | 4.61 us: 1.03x faster                                                      |
| pickle_list          | 4.11 us                                                      | 4.04 us: 1.02x faster                                                      |
| unpickle_pure_python | 318 us                                                       | 313 us: 1.02x faster                                                       |
| xml_etree_process    | 77.6 ms                                                      | 76.5 ms: 1.01x faster                                                      |
| xml_etree_generate   | 94.1 ms                                                      | 92.8 ms: 1.01x faster                                                      |
| json_loads           | 30.3 us                                                      | 30.2 us: 1.00x faster                                                      |
| pickle_pure_python   | 451 us                                                       | 454 us: 1.01x slower                                                       |
| json_dumps           | 14.3 ms                                                      | 14.4 ms: 1.01x slower                                                      |
| pickle_dict          | 29.5 us                                                      | 31.1 us: 1.05x slower                                                      |
| unpickle             | 13.3 us                                                      | 14.1 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                               |

Benchmark hidden because not significant (3): xml_etree_parse, pickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.32 ms                                                      | 7.35 ms: 1.00x slower                                                      |
| python_startup         | 11.5 ms                                                      | 11.5 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 14.9 ms: 1.01x slower                                                      |
| django_template | 52.0 ms                                                      | 53.2 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                               |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coverage                | 71.1 ms                                                      | 63.5 ms: 1.12x faster                                                      |
| pyflate                 | 731 ms                                                       | 693 ms: 1.05x faster                                                       |
| thrift                  | 1.23 ms                                                      | 1.17 ms: 1.05x faster                                                      |
| dask                    | 478 ms                                                       | 459 ms: 1.04x faster                                                       |
| fannkuch                | 496 ms                                                       | 477 ms: 1.04x faster                                                       |
| logging_format          | 9.94 us                                                      | 9.57 us: 1.04x faster                                                      |
| logging_simple          | 9.24 us                                                      | 8.94 us: 1.03x faster                                                      |
| crypto_pyaes            | 119 ms                                                       | 115 ms: 1.03x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 1.10 ms: 1.03x faster                                                      |
| pycparser               | 1.66 sec                                                     | 1.61 sec: 1.03x faster                                                     |
| html5lib                | 96.3 ms                                                      | 93.6 ms: 1.03x faster                                                      |
| chaos                   | 108 ms                                                       | 105 ms: 1.03x faster                                                       |
| unpickle_list           | 4.73 us                                                      | 4.61 us: 1.03x faster                                                      |
| meteor_contest          | 142 ms                                                       | 139 ms: 1.02x faster                                                       |
| chameleon               | 9.62 ms                                                      | 9.41 ms: 1.02x faster                                                      |
| aiohttp                 | 1.18 ms                                                      | 1.15 ms: 1.02x faster                                                      |
| sqlglot_normalize       | 147 ms                                                       | 144 ms: 1.02x faster                                                       |
| pickle_list             | 4.11 us                                                      | 4.04 us: 1.02x faster                                                      |
| gunicorn                | 1.15 ms                                                      | 1.13 ms: 1.02x faster                                                      |
| scimark_lu              | 164 ms                                                       | 161 ms: 1.02x faster                                                       |
| unpickle_pure_python    | 318 us                                                       | 313 us: 1.02x faster                                                       |
| sqlglot_optimize        | 70.1 ms                                                      | 69.1 ms: 1.01x faster                                                      |
| xml_etree_process       | 77.6 ms                                                      | 76.5 ms: 1.01x faster                                                      |
| xml_etree_generate      | 94.1 ms                                                      | 92.8 ms: 1.01x faster                                                      |
| deltablue               | 7.54 ms                                                      | 7.44 ms: 1.01x faster                                                      |
| coroutines              | 30.6 ms                                                      | 30.2 ms: 1.01x faster                                                      |
| hexiom                  | 9.54 ms                                                      | 9.43 ms: 1.01x faster                                                      |
| pathlib                 | 21.3 ms                                                      | 21.0 ms: 1.01x faster                                                      |
| nqueens                 | 114 ms                                                       | 112 ms: 1.01x faster                                                       |
| flaskblogging           | 4.37 ms                                                      | 4.33 ms: 1.01x faster                                                      |
| regex_dna               | 261 ms                                                       | 259 ms: 1.01x faster                                                       |
| spectral_norm           | 138 ms                                                       | 137 ms: 1.01x faster                                                       |
| asyncio_tcp             | 787 ms                                                       | 781 ms: 1.01x faster                                                       |
| 2to3                    | 352 ms                                                       | 350 ms: 1.01x faster                                                       |
| comprehensions          | 27.3 us                                                      | 27.1 us: 1.01x faster                                                      |
| dulwich_log             | 80.5 ms                                                      | 80.1 ms: 1.00x faster                                                      |
| async_tree_io           | 1.61 sec                                                     | 1.61 sec: 1.00x faster                                                     |
| json_loads              | 30.3 us                                                      | 30.2 us: 1.00x faster                                                      |
| regex_compile           | 191 ms                                                       | 191 ms: 1.00x slower                                                       |
| pidigits                | 271 ms                                                       | 271 ms: 1.00x slower                                                       |
| docutils                | 3.41 sec                                                     | 3.42 sec: 1.00x slower                                                     |
| python_startup_no_site  | 7.32 ms                                                      | 7.35 ms: 1.00x slower                                                      |
| telco                   | 7.14 ms                                                      | 7.16 ms: 1.00x slower                                                      |
| sqlalchemy_imperative   | 22.9 ms                                                      | 23.0 ms: 1.00x slower                                                      |
| json                    | 5.94 ms                                                      | 5.97 ms: 1.00x slower                                                      |
| python_startup          | 11.5 ms                                                      | 11.5 ms: 1.01x slower                                                      |
| pickle_pure_python      | 451 us                                                       | 454 us: 1.01x slower                                                       |
| async_tree_memoization  | 822 ms                                                       | 827 ms: 1.01x slower                                                       |
| float                   | 109 ms                                                       | 110 ms: 1.01x slower                                                       |
| mypy2                   | 466 ms                                                       | 470 ms: 1.01x slower                                                       |
| pprint_safe_repr        | 1.03 sec                                                     | 1.03 sec: 1.01x slower                                                     |
| richards                | 73.9 ms                                                      | 74.5 ms: 1.01x slower                                                      |
| pprint_pformat          | 2.12 sec                                                     | 2.14 sec: 1.01x slower                                                     |
| mako                    | 14.7 ms                                                      | 14.9 ms: 1.01x slower                                                      |
| sympy_integrate         | 28.1 ms                                                      | 28.4 ms: 1.01x slower                                                      |
| json_dumps              | 14.3 ms                                                      | 14.4 ms: 1.01x slower                                                      |
| generators              | 57.0 ms                                                      | 57.8 ms: 1.01x slower                                                      |
| scimark_monte_carlo     | 109 ms                                                       | 110 ms: 1.02x slower                                                       |
| deepcopy                | 457 us                                                       | 465 us: 1.02x slower                                                       |
| deepcopy_reduce         | 3.91 us                                                      | 3.99 us: 1.02x slower                                                      |
| pylint                  | 562 ms                                                       | 572 ms: 1.02x slower                                                       |
| sympy_expand            | 603 ms                                                       | 615 ms: 1.02x slower                                                       |
| django_template         | 52.0 ms                                                      | 53.2 ms: 1.02x slower                                                      |
| sympy_str               | 358 ms                                                       | 366 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 5.22 ms: 1.02x slower                                                      |
| sympy_sum               | 193 ms                                                       | 199 ms: 1.03x slower                                                       |
| nbody                   | 132 ms                                                       | 137 ms: 1.04x slower                                                       |
| deepcopy_memo           | 49.2 us                                                      | 51.1 us: 1.04x slower                                                      |
| regex_v8                | 26.0 ms                                                      | 27.1 ms: 1.04x slower                                                      |
| pickle_dict             | 29.5 us                                                      | 31.1 us: 1.05x slower                                                      |
| mdp                     | 2.95 sec                                                     | 3.12 sec: 1.06x slower                                                     |
| unpickle                | 13.3 us                                                      | 14.1 us: 1.06x slower                                                      |
| gc_traversal            | 3.46 ms                                                      | 3.68 ms: 1.06x slower                                                      |
| regex_effbot            | 2.99 ms                                                      | 3.25 ms: 1.09x slower                                                      |
| Geometric mean          | (ref)                                                        | 1.00x faster                                                               |

Benchmark hidden because not significant (21): bench_mp_pool, unpack_sequence, async_tree_none, scimark_sor, async_generators, tornado_http, xml_etree_parse, raytrace, pickle, sqlalchemy_declarative, async_tree_cpu_io_mixed, sqlglot_transpile, xml_etree_iterparse, scimark_fft, sqlite_synth, genshi_text, go, genshi_xml, sqlglot_parse, logging_silent, create_gc_cycles
