
# Results vs. 3.10.4

- fork: python
- ref: e95dd40aff35775efce4
- machine: windows-amd64
- commit hash: e95dd40
- commit date: 2023-05-03
- overall geometric mean: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 206 ms: 1.11x faster                                                        |
| docutils       | 1.83 sec                                                                 | 1.60 sec: 1.14x faster                                                      |
| tornado_http   | 106 ms                                                                   | 88.9 ms: 1.20x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.15x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 59.5 ms                                                                  | 51.6 ms: 1.15x faster                                                       |
| nbody          | 71.5 ms                                                                  | 67.9 ms: 1.05x faster                                                       |
| pidigits       | 145 ms                                                                   | 152 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 84.3 ms: 1.23x faster                                                       |
| regex_dna      | 131 ms                                                                   | 117 ms: 1.12x faster                                                        |
| regex_v8       | 15.1 ms                                                                  | 13.9 ms: 1.08x faster                                                       |
| regex_effbot   | 1.64 ms                                                                  | 1.58 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.00 ms                                                                  | 5.53 ms: 1.63x faster                                                       |
| pickle_pure_python   | 264 us                                                                   | 186 us: 1.42x faster                                                        |
| unpickle_pure_python | 179 us                                                                   | 131 us: 1.37x faster                                                        |
| xml_etree_process    | 43.0 ms                                                                  | 37.1 ms: 1.16x faster                                                       |
| xml_etree_parse      | 95.6 ms                                                                  | 92.7 ms: 1.03x faster                                                       |
| unpickle             | 8.88 us                                                                  | 8.63 us: 1.03x faster                                                       |
| xml_etree_generate   | 53.8 ms                                                                  | 54.1 ms: 1.01x slower                                                       |
| pickle               | 6.67 us                                                                  | 7.00 us: 1.05x slower                                                       |
| unpickle_list        | 2.71 us                                                                  | 2.88 us: 1.06x slower                                                       |
| pickle_dict          | 16.7 us                                                                  | 18.0 us: 1.08x slower                                                       |
| pickle_list          | 2.57 us                                                                  | 2.85 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                                    | 1.08x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 18.4 ms: 1.04x faster                                                       |
| python_startup_no_site | 14.8 ms                                                                  | 15.5 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                                    | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-----------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 8.69 ms                                                                  | 6.42 ms: 1.35x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 2.03 ms: 2.04x faster                                                       |
| go                      | 143 ms                                                                   | 84.7 ms: 1.69x faster                                                       |
| richards                | 41.0 ms                                                                  | 24.6 ms: 1.67x faster                                                       |
| logging_silent          | 94.6 ns                                                                  | 57.6 ns: 1.64x faster                                                       |
| json_dumps              | 9.00 ms                                                                  | 5.53 ms: 1.63x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                                  | 768 us: 1.59x faster                                                        |
| generators              | 31.4 ms                                                                  | 20.0 ms: 1.57x faster                                                       |
| mypy2                   | 337 ms                                                                   | 215 ms: 1.57x faster                                                        |
| sqlglot_transpile       | 1.47 ms                                                                  | 977 us: 1.50x faster                                                        |
| scimark_lu              | 83.9 ms                                                                  | 57.5 ms: 1.46x faster                                                       |
| raytrace                | 267 ms                                                                   | 186 ms: 1.43x faster                                                        |
| asyncio_tcp             | 664 ms                                                                   | 464 ms: 1.43x faster                                                        |
| async_tree_io           | 1.02 sec                                                                 | 715 ms: 1.43x faster                                                        |
| pickle_pure_python      | 264 us                                                                   | 186 us: 1.42x faster                                                        |
| async_tree_none         | 414 ms                                                                   | 295 ms: 1.40x faster                                                        |
| async_tree_memoization  | 485 ms                                                                   | 345 ms: 1.40x faster                                                        |
| hexiom                  | 5.45 ms                                                                  | 3.90 ms: 1.40x faster                                                       |
| scimark_sor             | 104 ms                                                                   | 74.5 ms: 1.39x faster                                                       |
| pyflate                 | 388 ms                                                                   | 282 ms: 1.38x faster                                                        |
| unpickle_pure_python    | 179 us                                                                   | 131 us: 1.37x faster                                                        |
| scimark_monte_carlo     | 56.0 ms                                                                  | 41.0 ms: 1.37x faster                                                       |
| mako                    | 8.69 ms                                                                  | 6.42 ms: 1.35x faster                                                       |
| chaos                   | 58.4 ms                                                                  | 43.5 ms: 1.34x faster                                                       |
| pycparser               | 873 ms                                                                   | 658 ms: 1.33x faster                                                        |
| crypto_pyaes            | 61.4 ms                                                                  | 46.5 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 468 ms: 1.29x faster                                                        |
| deepcopy_memo           | 28.4 us                                                                  | 23.1 us: 1.23x faster                                                       |
| regex_compile           | 103 ms                                                                   | 84.3 ms: 1.23x faster                                                       |
| spectral_norm           | 74.3 ms                                                                  | 61.8 ms: 1.20x faster                                                       |
| tornado_http            | 106 ms                                                                   | 88.9 ms: 1.20x faster                                                       |
| pprint_pformat          | 1.23 sec                                                                 | 1.03 sec: 1.19x faster                                                      |
| pprint_safe_repr        | 593 ms                                                                   | 500 ms: 1.19x faster                                                        |
| unpack_sequence         | 39.4 ns                                                                  | 33.8 ns: 1.17x faster                                                       |
| xml_etree_process       | 43.0 ms                                                                  | 37.1 ms: 1.16x faster                                                       |
| float                   | 59.5 ms                                                                  | 51.6 ms: 1.15x faster                                                       |
| mdp                     | 1.60 sec                                                                 | 1.39 sec: 1.15x faster                                                      |
| sqlglot_optimize        | 38.7 ms                                                                  | 33.8 ms: 1.15x faster                                                       |
| docutils                | 1.83 sec                                                                 | 1.60 sec: 1.14x faster                                                      |
| bench_thread_pool       | 953 us                                                                   | 835 us: 1.14x faster                                                        |
| nqueens                 | 64.8 ms                                                                  | 57.0 ms: 1.14x faster                                                       |
| regex_dna               | 131 ms                                                                   | 117 ms: 1.12x faster                                                        |
| coroutines              | 15.6 ms                                                                  | 14.0 ms: 1.12x faster                                                       |
| 2to3                    | 229 ms                                                                   | 206 ms: 1.11x faster                                                        |
| create_gc_cycles        | 764 us                                                                   | 689 us: 1.11x faster                                                        |
| dulwich_log             | 47.0 ms                                                                  | 42.4 ms: 1.11x faster                                                       |
| json                    | 3.18 ms                                                                  | 2.88 ms: 1.10x faster                                                       |
| sqlglot_normalize       | 201 ms                                                                   | 182 ms: 1.10x faster                                                        |
| deepcopy                | 256 us                                                                   | 235 us: 1.09x faster                                                        |
| deepcopy_reduce         | 2.18 us                                                                  | 2.00 us: 1.09x faster                                                       |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.45 ms: 1.09x faster                                                       |
| scimark_fft             | 187 ms                                                                   | 172 ms: 1.09x faster                                                        |
| fannkuch                | 252 ms                                                                   | 232 ms: 1.09x faster                                                        |
| sqlite_synth            | 1.85 us                                                                  | 1.70 us: 1.08x faster                                                       |
| regex_v8                | 15.1 ms                                                                  | 13.9 ms: 1.08x faster                                                       |
| nbody                   | 71.5 ms                                                                  | 67.9 ms: 1.05x faster                                                       |
| python_startup          | 19.3 ms                                                                  | 18.4 ms: 1.04x faster                                                       |
| regex_effbot            | 1.64 ms                                                                  | 1.58 ms: 1.04x faster                                                       |
| xml_etree_parse         | 95.6 ms                                                                  | 92.7 ms: 1.03x faster                                                       |
| unpickle                | 8.88 us                                                                  | 8.63 us: 1.03x faster                                                       |
| comprehensions          | 16.0 us                                                                  | 15.5 us: 1.03x faster                                                       |
| xml_etree_generate      | 53.8 ms                                                                  | 54.1 ms: 1.01x slower                                                       |
| logging_simple          | 6.12 us                                                                  | 6.24 us: 1.02x slower                                                       |
| logging_format          | 6.53 us                                                                  | 6.81 us: 1.04x slower                                                       |
| async_generators        | 214 ms                                                                   | 224 ms: 1.05x slower                                                        |
| python_startup_no_site  | 14.8 ms                                                                  | 15.5 ms: 1.05x slower                                                       |
| pidigits                | 145 ms                                                                   | 152 ms: 1.05x slower                                                        |
| pickle                  | 6.67 us                                                                  | 7.00 us: 1.05x slower                                                       |
| meteor_contest          | 74.3 ms                                                                  | 78.7 ms: 1.06x slower                                                       |
| unpickle_list           | 2.71 us                                                                  | 2.88 us: 1.06x slower                                                       |
| gc_traversal            | 1.33 ms                                                                  | 1.44 ms: 1.08x slower                                                       |
| pickle_dict             | 16.7 us                                                                  | 18.0 us: 1.08x slower                                                       |
| pathlib                 | 75.2 ms                                                                  | 81.9 ms: 1.09x slower                                                       |
| telco                   | 3.77 ms                                                                  | 4.16 ms: 1.10x slower                                                       |
| pickle_list             | 2.57 us                                                                  | 2.85 us: 1.11x slower                                                       |
| bench_mp_pool           | 59.2 ms                                                                  | 67.4 ms: 1.14x slower                                                       |
| dask                    | 310 ms                                                                   | 357 ms: 1.15x slower                                                        |
| coverage                | 37.5 ms                                                                  | 53.3 ms: 1.42x slower                                                       |
| Geometric mean          | (ref)                                                                    | 1.17x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
