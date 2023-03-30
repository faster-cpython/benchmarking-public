
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0b3
- machine: windows-amd64
- commit hash: eb0004c
- commit date: 2022-06-01
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 212 ms: 1.08x faster                                            |
| chameleon      | 5.77 ms                                                                  | 5.63 ms: 1.03x faster                                           |
| docutils       | 1.83 sec                                                                 | 1.66 sec: 1.10x faster                                          |
| html5lib       | 47.3 ms                                                                  | 41.2 ms: 1.15x faster                                           |
| tornado_http   | 106 ms                                                                   | 94.8 ms: 1.12x faster                                           |
| Geometric mean | (ref)                                                                    | 1.10x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 59.5 ms                                                                  | 57.2 ms: 1.04x faster                                           |
| pidigits       | 145 ms                                                                   | 154 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 94.2 ms: 1.10x faster                                           |
| regex_dna      | 131 ms                                                                   | 127 ms: 1.03x faster                                            |
| regex_effbot   | 1.64 ms                                                                  | 1.62 ms: 1.02x faster                                           |
| regex_v8       | 15.1 ms                                                                  | 15.2 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                    | 1.03x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 264 us                                                                   | 212 us: 1.24x faster                                            |
| unpickle_pure_python | 179 us                                                                   | 158 us: 1.14x faster                                            |
| json_dumps           | 9.00 ms                                                                  | 7.98 ms: 1.13x faster                                           |
| xml_etree_process    | 43.0 ms                                                                  | 38.9 ms: 1.11x faster                                           |
| unpickle             | 8.88 us                                                                  | 8.33 us: 1.07x faster                                           |
| xml_etree_iterparse  | 62.5 ms                                                                  | 63.3 ms: 1.01x slower                                           |
| xml_etree_parse      | 95.6 ms                                                                  | 97.4 ms: 1.02x slower                                           |
| pickle               | 6.67 us                                                                  | 6.83 us: 1.02x slower                                           |
| xml_etree_generate   | 53.8 ms                                                                  | 55.8 ms: 1.04x slower                                           |
| pickle_dict          | 16.7 us                                                                  | 17.7 us: 1.06x slower                                           |
| pickle_list          | 2.57 us                                                                  | 2.81 us: 1.10x slower                                           |
| Geometric mean       | (ref)                                                                    | 1.03x faster                                                    |

Benchmark hidden because not significant (2): unpickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 14.8 ms                                                                  | 16.4 ms: 1.10x slower                                           |
| Geometric mean         | (ref)                                                                    | 1.05x slower                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 8.69 ms                                                                  | 7.38 ms: 1.18x faster                                           |
| django_template | 29.2 ms                                                                  | 25.4 ms: 1.15x faster                                           |
| genshi_xml      | 38.8 ms                                                                  | 41.0 ms: 1.06x slower                                           |
| Geometric mean  | (ref)                                                                    | 1.06x faster                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220601-pythonperf1-amd64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 2.78 ms: 1.49x faster                                           |
| go                      | 143 ms                                                                   | 104 ms: 1.38x faster                                            |
| richards                | 41.0 ms                                                                  | 30.7 ms: 1.34x faster                                           |
| scimark_sor             | 104 ms                                                                   | 77.7 ms: 1.33x faster                                           |
| scimark_lu              | 83.9 ms                                                                  | 63.6 ms: 1.32x faster                                           |
| async_tree_io           | 1.02 sec                                                                 | 781 ms: 1.31x faster                                            |
| logging_silent          | 94.6 ns                                                                  | 72.7 ns: 1.30x faster                                           |
| pickle_pure_python      | 264 us                                                                   | 212 us: 1.24x faster                                            |
| raytrace                | 267 ms                                                                   | 215 ms: 1.24x faster                                            |
| scimark_monte_carlo     | 56.0 ms                                                                  | 45.4 ms: 1.23x faster                                           |
| thrift                  | 632 us                                                                   | 514 us: 1.23x faster                                            |
| async_tree_none         | 414 ms                                                                   | 339 ms: 1.22x faster                                            |
| pyflate                 | 388 ms                                                                   | 318 ms: 1.22x faster                                            |
| crypto_pyaes            | 61.4 ms                                                                  | 50.9 ms: 1.21x faster                                           |
| async_tree_memoization  | 485 ms                                                                   | 402 ms: 1.21x faster                                            |
| pycparser               | 873 ms                                                                   | 735 ms: 1.19x faster                                            |
| mako                    | 8.69 ms                                                                  | 7.38 ms: 1.18x faster                                           |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 519 ms: 1.16x faster                                            |
| mypy2                   | 337 ms                                                                   | 293 ms: 1.15x faster                                            |
| django_template         | 29.2 ms                                                                  | 25.4 ms: 1.15x faster                                           |
| html5lib                | 47.3 ms                                                                  | 41.2 ms: 1.15x faster                                           |
| unpickle_pure_python    | 179 us                                                                   | 158 us: 1.14x faster                                            |
| hexiom                  | 5.45 ms                                                                  | 4.82 ms: 1.13x faster                                           |
| chaos                   | 58.4 ms                                                                  | 51.8 ms: 1.13x faster                                           |
| json_dumps              | 9.00 ms                                                                  | 7.98 ms: 1.13x faster                                           |
| tornado_http            | 106 ms                                                                   | 94.8 ms: 1.12x faster                                           |
| sqlalchemy_declarative  | 96.4 ms                                                                  | 86.0 ms: 1.12x faster                                           |
| async_generators        | 214 ms                                                                   | 192 ms: 1.12x faster                                            |
| create_gc_cycles        | 764 us                                                                   | 686 us: 1.11x faster                                            |
| xml_etree_process       | 43.0 ms                                                                  | 38.9 ms: 1.11x faster                                           |
| dask                    | 310 ms                                                                   | 281 ms: 1.10x faster                                            |
| docutils                | 1.83 sec                                                                 | 1.66 sec: 1.10x faster                                          |
| regex_compile           | 103 ms                                                                   | 94.2 ms: 1.10x faster                                           |
| pprint_safe_repr        | 593 ms                                                                   | 541 ms: 1.10x faster                                            |
| sqlalchemy_imperative   | 11.3 ms                                                                  | 10.3 ms: 1.09x faster                                           |
| deepcopy_memo           | 28.4 us                                                                  | 26.0 us: 1.09x faster                                           |
| pprint_pformat          | 1.23 sec                                                                 | 1.12 sec: 1.09x faster                                          |
| 2to3                    | 229 ms                                                                   | 212 ms: 1.08x faster                                            |
| sqlglot_optimize        | 38.7 ms                                                                  | 35.9 ms: 1.08x faster                                           |
| aiohttp                 | 968 us                                                                   | 897 us: 1.08x faster                                            |
| bench_thread_pool       | 953 us                                                                   | 890 us: 1.07x faster                                            |
| unpack_sequence         | 39.4 ns                                                                  | 36.8 ns: 1.07x faster                                           |
| unpickle                | 8.88 us                                                                  | 8.33 us: 1.07x faster                                           |
| sqlite_synth            | 1.85 us                                                                  | 1.74 us: 1.06x faster                                           |
| sqlglot_transpile       | 1.47 ms                                                                  | 1.41 ms: 1.04x faster                                           |
| float                   | 59.5 ms                                                                  | 57.2 ms: 1.04x faster                                           |
| spectral_norm           | 74.3 ms                                                                  | 71.4 ms: 1.04x faster                                           |
| dulwich_log             | 47.0 ms                                                                  | 45.5 ms: 1.03x faster                                           |
| regex_dna               | 131 ms                                                                   | 127 ms: 1.03x faster                                            |
| sympy_integrate         | 14.7 ms                                                                  | 14.2 ms: 1.03x faster                                           |
| logging_simple          | 6.12 us                                                                  | 5.96 us: 1.03x faster                                           |
| chameleon               | 5.77 ms                                                                  | 5.63 ms: 1.03x faster                                           |
| sympy_expand            | 313 ms                                                                   | 306 ms: 1.02x faster                                            |
| pathlib                 | 75.2 ms                                                                  | 73.6 ms: 1.02x faster                                           |
| pylint                  | 337 ms                                                                   | 331 ms: 1.02x faster                                            |
| sympy_sum               | 102 ms                                                                   | 100 ms: 1.02x faster                                            |
| logging_format          | 6.53 us                                                                  | 6.43 us: 1.02x faster                                           |
| regex_effbot            | 1.64 ms                                                                  | 1.62 ms: 1.02x faster                                           |
| sqlglot_normalize       | 201 ms                                                                   | 198 ms: 1.01x faster                                            |
| sqlglot_parse           | 1.22 ms                                                                  | 1.21 ms: 1.01x faster                                           |
| regex_v8                | 15.1 ms                                                                  | 15.2 ms: 1.01x slower                                           |
| scimark_fft             | 187 ms                                                                   | 188 ms: 1.01x slower                                            |
| xml_etree_iterparse     | 62.5 ms                                                                  | 63.3 ms: 1.01x slower                                           |
| deepcopy_reduce         | 2.18 us                                                                  | 2.22 us: 1.02x slower                                           |
| xml_etree_parse         | 95.6 ms                                                                  | 97.4 ms: 1.02x slower                                           |
| pickle                  | 6.67 us                                                                  | 6.83 us: 1.02x slower                                           |
| deepcopy                | 256 us                                                                   | 265 us: 1.03x slower                                            |
| mdp                     | 1.60 sec                                                                 | 1.66 sec: 1.03x slower                                          |
| xml_etree_generate      | 53.8 ms                                                                  | 55.8 ms: 1.04x slower                                           |
| meteor_contest          | 74.3 ms                                                                  | 77.1 ms: 1.04x slower                                           |
| genshi_xml              | 38.8 ms                                                                  | 41.0 ms: 1.06x slower                                           |
| pidigits                | 145 ms                                                                   | 154 ms: 1.06x slower                                            |
| pickle_dict             | 16.7 us                                                                  | 17.7 us: 1.06x slower                                           |
| nqueens                 | 64.8 ms                                                                  | 71.0 ms: 1.09x slower                                           |
| telco                   | 3.77 ms                                                                  | 4.13 ms: 1.10x slower                                           |
| pickle_list             | 2.57 us                                                                  | 2.81 us: 1.10x slower                                           |
| fannkuch                | 252 ms                                                                   | 278 ms: 1.10x slower                                            |
| python_startup_no_site  | 14.8 ms                                                                  | 16.4 ms: 1.10x slower                                           |
| gc_traversal            | 1.33 ms                                                                  | 1.49 ms: 1.12x slower                                           |
| generators              | 31.4 ms                                                                  | 35.4 ms: 1.13x slower                                           |
| bench_mp_pool           | 59.2 ms                                                                  | 67.0 ms: 1.13x slower                                           |
| asyncio_tcp             | 664 ms                                                                   | 762 ms: 1.15x slower                                            |
| comprehensions          | 16.0 us                                                                  | 18.7 us: 1.17x slower                                           |
| coverage                | 37.5 ms                                                                  | 108 ms: 2.87x slower                                            |
| Geometric mean          | (ref)                                                                    | 1.05x faster                                                    |

Benchmark hidden because not significant (10): unpickle_list, json_loads, genshi_text, flaskblogging, coroutines, scimark_sparse_mat_mult, python_startup, sympy_str, nbody, json
