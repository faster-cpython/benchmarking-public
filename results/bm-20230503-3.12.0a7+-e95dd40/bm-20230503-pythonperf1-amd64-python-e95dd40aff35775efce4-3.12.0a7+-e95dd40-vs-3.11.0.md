
# Results vs. 3.11.0

- fork: python
- ref: e95dd40aff35775efce4
- machine: windows-amd64
- commit hash: e95dd40
- commit date: 2023-05-03
- overall geometric mean: 1.06x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 204 ms                                                                   | 206 ms: 1.01x slower                                                        |
| tornado_http   | 91.8 ms                                                                  | 88.9 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.9 ms                                                                  | 67.9 ms: 1.04x faster                                                       |
| float          | 53.3 ms                                                                  | 51.6 ms: 1.03x faster                                                       |
| pidigits       | 147 ms                                                                   | 152 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 89.7 ms                                                                  | 84.3 ms: 1.06x faster                                                       |
| regex_effbot   | 1.63 ms                                                                  | 1.58 ms: 1.03x faster                                                       |
| regex_dna      | 115 ms                                                                   | 117 ms: 1.02x slower                                                        |
| regex_v8       | 13.5 ms                                                                  | 13.9 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.71 ms                                                                  | 5.53 ms: 1.39x faster                                                       |
| unpickle_pure_python | 150 us                                                                   | 131 us: 1.14x faster                                                        |
| pickle_pure_python   | 203 us                                                                   | 186 us: 1.09x faster                                                        |
| pickle_dict          | 18.6 us                                                                  | 18.0 us: 1.03x faster                                                       |
| xml_etree_process    | 36.6 ms                                                                  | 37.1 ms: 1.01x slower                                                       |
| xml_etree_generate   | 52.3 ms                                                                  | 54.1 ms: 1.04x slower                                                       |
| pickle_list          | 2.70 us                                                                  | 2.85 us: 1.05x slower                                                       |
| json_loads           | 13.5 us                                                                  | 14.3 us: 1.06x slower                                                       |
| unpickle             | 8.01 us                                                                  | 8.63 us: 1.08x slower                                                       |
| pickle               | 6.47 us                                                                  | 7.00 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                                    | 1.02x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.4 ms                                                                  | 15.5 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-----------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 7.20 ms                                                                  | 6.42 ms: 1.12x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 33.5 ms                                                                  | 20.0 ms: 1.68x faster                                                       |
| asyncio_tcp             | 674 ms                                                                   | 464 ms: 1.45x faster                                                        |
| json_dumps              | 7.71 ms                                                                  | 5.53 ms: 1.39x faster                                                       |
| deltablue               | 2.68 ms                                                                  | 2.03 ms: 1.32x faster                                                       |
| richards                | 32.1 ms                                                                  | 24.6 ms: 1.30x faster                                                       |
| mypy2                   | 276 ms                                                                   | 215 ms: 1.28x faster                                                        |
| unpack_sequence         | 43.1 ns                                                                  | 33.8 ns: 1.28x faster                                                       |
| logging_silent          | 71.0 ns                                                                  | 57.6 ns: 1.23x faster                                                       |
| sqlglot_parse           | 929 us                                                                   | 768 us: 1.21x faster                                                        |
| mdp                     | 1.67 sec                                                                 | 1.39 sec: 1.20x faster                                                      |
| spectral_norm           | 71.8 ms                                                                  | 61.8 ms: 1.16x faster                                                       |
| sqlglot_transpile       | 1.13 ms                                                                  | 977 us: 1.16x faster                                                        |
| go                      | 97.5 ms                                                                  | 84.7 ms: 1.15x faster                                                       |
| hexiom                  | 4.46 ms                                                                  | 3.90 ms: 1.14x faster                                                       |
| nqueens                 | 65.1 ms                                                                  | 57.0 ms: 1.14x faster                                                       |
| unpickle_pure_python    | 150 us                                                                   | 131 us: 1.14x faster                                                        |
| mako                    | 7.20 ms                                                                  | 6.42 ms: 1.12x faster                                                       |
| scimark_monte_carlo     | 45.8 ms                                                                  | 41.0 ms: 1.12x faster                                                       |
| json                    | 3.20 ms                                                                  | 2.88 ms: 1.11x faster                                                       |
| raytrace                | 206 ms                                                                   | 186 ms: 1.11x faster                                                        |
| fannkuch                | 255 ms                                                                   | 232 ms: 1.10x faster                                                        |
| deepcopy_memo           | 25.3 us                                                                  | 23.1 us: 1.10x faster                                                       |
| async_tree_cpu_io_mixed | 512 ms                                                                   | 468 ms: 1.09x faster                                                        |
| pickle_pure_python      | 203 us                                                                   | 186 us: 1.09x faster                                                        |
| scimark_lu              | 62.8 ms                                                                  | 57.5 ms: 1.09x faster                                                       |
| chaos                   | 47.3 ms                                                                  | 43.5 ms: 1.09x faster                                                       |
| async_tree_memoization  | 374 ms                                                                   | 345 ms: 1.08x faster                                                        |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.45 ms: 1.07x faster                                                       |
| pyflate                 | 302 ms                                                                   | 282 ms: 1.07x faster                                                        |
| regex_compile           | 89.7 ms                                                                  | 84.3 ms: 1.06x faster                                                       |
| scimark_fft             | 183 ms                                                                   | 172 ms: 1.06x faster                                                        |
| async_tree_none         | 313 ms                                                                   | 295 ms: 1.06x faster                                                        |
| coroutines              | 14.8 ms                                                                  | 14.0 ms: 1.06x faster                                                       |
| logging_simple          | 6.60 us                                                                  | 6.24 us: 1.06x faster                                                       |
| logging_format          | 7.13 us                                                                  | 6.81 us: 1.05x faster                                                       |
| nbody                   | 70.9 ms                                                                  | 67.9 ms: 1.04x faster                                                       |
| scimark_sor             | 77.7 ms                                                                  | 74.5 ms: 1.04x faster                                                       |
| pycparser               | 686 ms                                                                   | 658 ms: 1.04x faster                                                        |
| async_tree_io           | 744 ms                                                                   | 715 ms: 1.04x faster                                                        |
| crypto_pyaes            | 48.3 ms                                                                  | 46.5 ms: 1.04x faster                                                       |
| coverage                | 55.3 ms                                                                  | 53.3 ms: 1.04x faster                                                       |
| sqlglot_normalize       | 189 ms                                                                   | 182 ms: 1.04x faster                                                        |
| regex_effbot            | 1.63 ms                                                                  | 1.58 ms: 1.03x faster                                                       |
| tornado_http            | 91.8 ms                                                                  | 88.9 ms: 1.03x faster                                                       |
| pickle_dict             | 18.6 us                                                                  | 18.0 us: 1.03x faster                                                       |
| float                   | 53.3 ms                                                                  | 51.6 ms: 1.03x faster                                                       |
| deepcopy_reduce         | 2.06 us                                                                  | 2.00 us: 1.03x faster                                                       |
| bench_thread_pool       | 856 us                                                                   | 835 us: 1.03x faster                                                        |
| dulwich_log             | 43.4 ms                                                                  | 42.4 ms: 1.02x faster                                                       |
| pprint_safe_repr        | 512 ms                                                                   | 500 ms: 1.02x faster                                                        |
| sqlglot_optimize        | 34.5 ms                                                                  | 33.8 ms: 1.02x faster                                                       |
| deepcopy                | 240 us                                                                   | 235 us: 1.02x faster                                                        |
| pprint_pformat          | 1.05 sec                                                                 | 1.03 sec: 1.01x faster                                                      |
| python_startup_no_site  | 15.4 ms                                                                  | 15.5 ms: 1.01x slower                                                       |
| comprehensions          | 15.4 us                                                                  | 15.5 us: 1.01x slower                                                       |
| 2to3                    | 204 ms                                                                   | 206 ms: 1.01x slower                                                        |
| xml_etree_process       | 36.6 ms                                                                  | 37.1 ms: 1.01x slower                                                       |
| sqlite_synth            | 1.67 us                                                                  | 1.70 us: 1.02x slower                                                       |
| regex_dna               | 115 ms                                                                   | 117 ms: 1.02x slower                                                        |
| gc_traversal            | 1.40 ms                                                                  | 1.44 ms: 1.02x slower                                                       |
| regex_v8                | 13.5 ms                                                                  | 13.9 ms: 1.03x slower                                                       |
| create_gc_cycles        | 666 us                                                                   | 689 us: 1.03x slower                                                        |
| xml_etree_generate      | 52.3 ms                                                                  | 54.1 ms: 1.04x slower                                                       |
| pidigits                | 147 ms                                                                   | 152 ms: 1.04x slower                                                        |
| pickle_list             | 2.70 us                                                                  | 2.85 us: 1.05x slower                                                       |
| meteor_contest          | 74.4 ms                                                                  | 78.7 ms: 1.06x slower                                                       |
| telco                   | 3.93 ms                                                                  | 4.16 ms: 1.06x slower                                                       |
| json_loads              | 13.5 us                                                                  | 14.3 us: 1.06x slower                                                       |
| unpickle                | 8.01 us                                                                  | 8.63 us: 1.08x slower                                                       |
| pickle                  | 6.47 us                                                                  | 7.00 us: 1.08x slower                                                       |
| bench_mp_pool           | 61.2 ms                                                                  | 67.4 ms: 1.10x slower                                                       |
| pathlib                 | 72.9 ms                                                                  | 81.9 ms: 1.12x slower                                                       |
| async_generators        | 180 ms                                                                   | 224 ms: 1.24x slower                                                        |
| dask                    | 267 ms                                                                   | 357 ms: 1.34x slower                                                        |
| Geometric mean          | (ref)                                                                    | 1.06x faster                                                                |

Benchmark hidden because not significant (5): python_startup, docutils, xml_etree_parse, xml_etree_iterparse, unpickle_list
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
