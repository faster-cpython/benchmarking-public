
# Results vs. 3.10.4

- fork: python
- ref: ed7c3ff15680c1939fad
- machine: linux-x86_64
- commit hash: ed7c3ff
- commit date: 2022-09-11
- overall geometric mean: 1.21x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                         |
| chameleon      | 9.72 ms                                                      | 7.50 ms: 1.30x faster                                                        |
| docutils       | 3.40 sec                                                     | 2.86 sec: 1.19x faster                                                       |
| html5lib       | 94.6 ms                                                      | 73.2 ms: 1.29x faster                                                        |
| tornado_http   | 152 ms                                                       | 125 ms: 1.21x faster                                                         |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 89.6 ms: 1.53x faster                                                        |
| float          | 110 ms                                                       | 75.1 ms: 1.47x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 157 ms: 1.23x faster                                                         |
| regex_dna      | 259 ms                                                       | 225 ms: 1.15x faster                                                         |
| regex_v8       | 26.6 ms                                                      | 24.3 ms: 1.10x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.29 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 324 us: 1.41x faster                                                         |
| xml_etree_process    | 76.0 ms                                                      | 57.0 ms: 1.33x faster                                                        |
| unpickle_pure_python | 321 us                                                       | 250 us: 1.28x faster                                                         |
| xml_etree_generate   | 94.6 ms                                                      | 80.8 ms: 1.17x faster                                                        |
| pickle_list          | 4.11 us                                                      | 3.77 us: 1.09x faster                                                        |
| unpickle             | 14.2 us                                                      | 13.0 us: 1.09x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                         |
| json_loads           | 30.0 us                                                      | 28.4 us: 1.06x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 13.5 ms: 1.05x faster                                                        |
| pickle               | 9.94 us                                                      | 9.61 us: 1.03x faster                                                        |
| pickle_dict          | 30.0 us                                                      | 30.7 us: 1.02x slower                                                        |
| unpickle_list        | 4.49 us                                                      | 4.72 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.7 ms: 1.07x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 7.72 ms: 1.05x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                        |
| django_template | 51.5 ms                                                      | 39.7 ms: 1.30x faster                                                        |
| genshi_text     | 31.5 ms                                                      | 26.1 ms: 1.21x faster                                                        |
| genshi_xml      | 64.7 ms                                                      | 59.2 ms: 1.09x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.23x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 4.09 ms: 1.82x faster                                                        |
| logging_silent          | 166 ns                                                       | 101 ns: 1.64x faster                                                         |
| scimark_sor             | 177 ms                                                       | 110 ms: 1.61x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                       | 68.7 ms: 1.59x faster                                                        |
| raytrace                | 488 ms                                                       | 307 ms: 1.59x faster                                                         |
| bench_mp_pool           | 7.18 ms                                                      | 4.54 ms: 1.58x faster                                                        |
| pyflate                 | 697 ms                                                       | 450 ms: 1.55x faster                                                         |
| nbody                   | 137 ms                                                       | 89.6 ms: 1.53x faster                                                        |
| go                      | 259 ms                                                       | 172 ms: 1.51x faster                                                         |
| float                   | 110 ms                                                       | 75.1 ms: 1.47x faster                                                        |
| sqlglot_parse           | 2.26 ms                                                      | 1.56 ms: 1.44x faster                                                        |
| scimark_lu              | 164 ms                                                       | 114 ms: 1.44x faster                                                         |
| spectral_norm           | 136 ms                                                       | 95.5 ms: 1.43x faster                                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.92 ms: 1.41x faster                                                        |
| pickle_pure_python      | 457 us                                                       | 324 us: 1.41x faster                                                         |
| crypto_pyaes            | 118 ms                                                       | 84.3 ms: 1.40x faster                                                        |
| richards                | 74.1 ms                                                      | 53.5 ms: 1.38x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.37x faster                                                       |
| async_tree_none         | 700 ms                                                       | 517 ms: 1.35x faster                                                         |
| mako                    | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                        |
| hexiom                  | 9.52 ms                                                      | 7.12 ms: 1.34x faster                                                        |
| xml_etree_process       | 76.0 ms                                                      | 57.0 ms: 1.33x faster                                                        |
| pprint_safe_repr        | 1.05 sec                                                     | 791 ms: 1.33x faster                                                         |
| chaos                   | 107 ms                                                       | 81.4 ms: 1.32x faster                                                        |
| pprint_pformat          | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                                       |
| unpack_sequence         | 59.5 ns                                                      | 45.7 ns: 1.30x faster                                                        |
| django_template         | 51.5 ms                                                      | 39.7 ms: 1.30x faster                                                        |
| chameleon               | 9.72 ms                                                      | 7.50 ms: 1.30x faster                                                        |
| async_tree_memoization  | 824 ms                                                       | 636 ms: 1.30x faster                                                         |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.01 ms: 1.30x faster                                                        |
| scimark_fft             | 359 ms                                                       | 277 ms: 1.30x faster                                                         |
| html5lib                | 94.6 ms                                                      | 73.2 ms: 1.29x faster                                                        |
| async_generators        | 422 ms                                                       | 328 ms: 1.29x faster                                                         |
| thrift                  | 1.16 ms                                                      | 906 us: 1.29x faster                                                         |
| unpickle_pure_python    | 321 us                                                       | 250 us: 1.28x faster                                                         |
| async_tree_cpu_io_mixed | 952 ms                                                       | 746 ms: 1.28x faster                                                         |
| aiohttp                 | 1.21 ms                                                      | 966 us: 1.25x faster                                                         |
| gunicorn                | 1.17 ms                                                      | 941 us: 1.25x faster                                                         |
| pycparser               | 1.66 sec                                                     | 1.34 sec: 1.24x faster                                                       |
| regex_compile           | 194 ms                                                       | 157 ms: 1.23x faster                                                         |
| 2to3                    | 350 ms                                                       | 287 ms: 1.22x faster                                                         |
| tornado_http            | 152 ms                                                       | 125 ms: 1.21x faster                                                         |
| genshi_text             | 31.5 ms                                                      | 26.1 ms: 1.21x faster                                                        |
| sqlalchemy_declarative  | 187 ms                                                       | 155 ms: 1.20x faster                                                         |
| logging_simple          | 8.90 us                                                      | 7.43 us: 1.20x faster                                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 58.8 ms: 1.20x faster                                                        |
| sqlite_synth            | 2.97 us                                                      | 2.48 us: 1.19x faster                                                        |
| deepcopy_memo           | 48.9 us                                                      | 41.0 us: 1.19x faster                                                        |
| sqlglot_normalize       | 144 ms                                                       | 121 ms: 1.19x faster                                                         |
| logging_format          | 9.57 us                                                      | 8.03 us: 1.19x faster                                                        |
| docutils                | 3.40 sec                                                     | 2.86 sec: 1.19x faster                                                       |
| xml_etree_generate      | 94.6 ms                                                      | 80.8 ms: 1.17x faster                                                        |
| flaskblogging           | 4.39 ms                                                      | 3.80 ms: 1.15x faster                                                        |
| regex_dna               | 259 ms                                                       | 225 ms: 1.15x faster                                                         |
| dulwich_log             | 80.1 ms                                                      | 69.6 ms: 1.15x faster                                                        |
| deepcopy_reduce         | 4.03 us                                                      | 3.51 us: 1.15x faster                                                        |
| sqlalchemy_imperative   | 22.6 ms                                                      | 19.9 ms: 1.13x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 1.00 ms: 1.13x faster                                                        |
| pathlib                 | 21.7 ms                                                      | 19.1 ms: 1.13x faster                                                        |
| fannkuch                | 496 ms                                                       | 441 ms: 1.12x faster                                                         |
| mdp                     | 3.03 sec                                                     | 2.72 sec: 1.12x faster                                                       |
| deepcopy                | 454 us                                                       | 407 us: 1.11x faster                                                         |
| nqueens                 | 112 ms                                                       | 101 ms: 1.11x faster                                                         |
| dask                    | 463 ms                                                       | 420 ms: 1.10x faster                                                         |
| create_gc_cycles        | 1.82 ms                                                      | 1.66 ms: 1.10x faster                                                        |
| regex_v8                | 26.6 ms                                                      | 24.3 ms: 1.10x faster                                                        |
| genshi_xml              | 64.7 ms                                                      | 59.2 ms: 1.09x faster                                                        |
| coroutines              | 30.4 ms                                                      | 27.9 ms: 1.09x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.77 us: 1.09x faster                                                        |
| unpickle                | 14.2 us                                                      | 13.0 us: 1.09x faster                                                        |
| sympy_expand            | 599 ms                                                       | 553 ms: 1.08x faster                                                         |
| sympy_integrate         | 28.1 ms                                                      | 25.9 ms: 1.08x faster                                                        |
| pylint                  | 562 ms                                                       | 520 ms: 1.08x faster                                                         |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| python_startup          | 11.5 ms                                                      | 10.7 ms: 1.07x faster                                                        |
| json                    | 5.96 ms                                                      | 5.57 ms: 1.07x faster                                                        |
| generators              | 58.0 ms                                                      | 54.2 ms: 1.07x faster                                                        |
| xml_etree_iterparse     | 110 ms                                                       | 104 ms: 1.06x faster                                                         |
| sympy_str               | 358 ms                                                       | 337 ms: 1.06x faster                                                         |
| comprehensions          | 26.9 us                                                      | 25.5 us: 1.06x faster                                                        |
| json_loads              | 30.0 us                                                      | 28.4 us: 1.06x faster                                                        |
| json_dumps              | 14.2 ms                                                      | 13.5 ms: 1.05x faster                                                        |
| sympy_sum               | 193 ms                                                       | 183 ms: 1.05x faster                                                         |
| asyncio_tcp             | 782 ms                                                       | 752 ms: 1.04x faster                                                         |
| telco                   | 7.14 ms                                                      | 6.88 ms: 1.04x faster                                                        |
| pickle                  | 9.94 us                                                      | 9.61 us: 1.03x faster                                                        |
| meteor_contest          | 137 ms                                                       | 132 ms: 1.03x faster                                                         |
| pickle_dict             | 30.0 us                                                      | 30.7 us: 1.02x slower                                                        |
| unpickle_list           | 4.49 us                                                      | 4.72 us: 1.05x slower                                                        |
| gc_traversal            | 3.45 ms                                                      | 3.63 ms: 1.05x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 7.72 ms: 1.05x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.29 ms: 1.10x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.21x faster                                                                 |

Benchmark hidden because not significant (2): mypy2, xml_etree_parse
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x
