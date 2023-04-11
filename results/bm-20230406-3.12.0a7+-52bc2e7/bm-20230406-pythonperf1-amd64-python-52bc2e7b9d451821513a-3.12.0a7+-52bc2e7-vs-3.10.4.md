
# Results vs. 3.10.4

- fork: python
- ref: 52bc2e7b9d451821513a
- machine: windows-amd64
- commit hash: 52bc2e7
- commit date: 2023-04-06
- overall geometric mean: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 202 ms: 1.14x faster                                                        |
| chameleon      | 5.77 ms                                                                  | 4.75 ms: 1.22x faster                                                       |
| docutils       | 1.83 sec                                                                 | 1.57 sec: 1.16x faster                                                      |
| html5lib       | 47.3 ms                                                                  | 36.4 ms: 1.30x faster                                                       |
| tornado_http   | 106 ms                                                                   | 86.4 ms: 1.23x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.5 ms                                                                  | 57.8 ms: 1.24x faster                                                       |
| float          | 59.5 ms                                                                  | 48.6 ms: 1.22x faster                                                       |
| pidigits       | 145 ms                                                                   | 148 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 82.3 ms: 1.26x faster                                                       |
| regex_dna      | 131 ms                                                                   | 117 ms: 1.12x faster                                                        |
| regex_v8       | 15.1 ms                                                                  | 13.8 ms: 1.10x faster                                                       |
| regex_effbot   | 1.64 ms                                                                  | 1.56 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.00 ms                                                                  | 5.36 ms: 1.68x faster                                                       |
| pickle_pure_python   | 264 us                                                                   | 176 us: 1.50x faster                                                        |
| unpickle_pure_python | 179 us                                                                   | 129 us: 1.39x faster                                                        |
| xml_etree_process    | 43.0 ms                                                                  | 36.8 ms: 1.17x faster                                                       |
| json_loads           | 14.2 us                                                                  | 12.8 us: 1.11x faster                                                       |
| unpickle             | 8.88 us                                                                  | 8.10 us: 1.10x faster                                                       |
| xml_etree_parse      | 95.6 ms                                                                  | 90.9 ms: 1.05x faster                                                       |
| xml_etree_generate   | 53.8 ms                                                                  | 51.9 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 62.5 ms                                                                  | 60.9 ms: 1.03x faster                                                       |
| unpickle_list        | 2.71 us                                                                  | 2.77 us: 1.02x slower                                                       |
| pickle               | 6.67 us                                                                  | 6.97 us: 1.05x slower                                                       |
| pickle_list          | 2.57 us                                                                  | 2.78 us: 1.08x slower                                                       |
| pickle_dict          | 16.7 us                                                                  | 19.1 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                                    | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 18.9 ms: 1.02x faster                                                       |
| python_startup_no_site | 14.8 ms                                                                  | 16.0 ms: 1.08x slower                                                       |
| Geometric mean         | (ref)                                                                    | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.69 ms                                                                  | 6.15 ms: 1.41x faster                                                       |
| genshi_text     | 18.5 ms                                                                  | 13.7 ms: 1.36x faster                                                       |
| django_template | 29.2 ms                                                                  | 21.7 ms: 1.35x faster                                                       |
| genshi_xml      | 38.8 ms                                                                  | 30.8 ms: 1.26x faster                                                       |
| Geometric mean  | (ref)                                                                    | 1.34x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 1.97 ms: 2.10x faster                                                       |
| go                      | 143 ms                                                                   | 83.9 ms: 1.71x faster                                                       |
| logging_silent          | 94.6 ns                                                                  | 55.8 ns: 1.70x faster                                                       |
| json_dumps              | 9.00 ms                                                                  | 5.36 ms: 1.68x faster                                                       |
| richards                | 41.0 ms                                                                  | 25.5 ms: 1.61x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                                  | 773 us: 1.58x faster                                                        |
| scimark_lu              | 83.9 ms                                                                  | 53.9 ms: 1.56x faster                                                       |
| mypy2                   | 337 ms                                                                   | 218 ms: 1.54x faster                                                        |
| sqlglot_transpile       | 1.47 ms                                                                  | 964 us: 1.53x faster                                                        |
| generators              | 31.4 ms                                                                  | 20.9 ms: 1.50x faster                                                       |
| pickle_pure_python      | 264 us                                                                   | 176 us: 1.50x faster                                                        |
| raytrace                | 267 ms                                                                   | 178 ms: 1.50x faster                                                        |
| unpack_sequence         | 39.4 ns                                                                  | 27.4 ns: 1.43x faster                                                       |
| chaos                   | 58.4 ms                                                                  | 41.2 ms: 1.42x faster                                                       |
| scimark_sor             | 104 ms                                                                   | 73.1 ms: 1.42x faster                                                       |
| hexiom                  | 5.45 ms                                                                  | 3.86 ms: 1.41x faster                                                       |
| mako                    | 8.69 ms                                                                  | 6.15 ms: 1.41x faster                                                       |
| unpickle_pure_python    | 179 us                                                                   | 129 us: 1.39x faster                                                        |
| asyncio_tcp             | 664 ms                                                                   | 482 ms: 1.38x faster                                                        |
| async_tree_none         | 414 ms                                                                   | 302 ms: 1.37x faster                                                        |
| crypto_pyaes            | 61.4 ms                                                                  | 45.0 ms: 1.37x faster                                                       |
| pyflate                 | 388 ms                                                                   | 285 ms: 1.36x faster                                                        |
| scimark_monte_carlo     | 56.0 ms                                                                  | 41.2 ms: 1.36x faster                                                       |
| genshi_text             | 18.5 ms                                                                  | 13.7 ms: 1.36x faster                                                       |
| django_template         | 29.2 ms                                                                  | 21.7 ms: 1.35x faster                                                       |
| thrift                  | 632 us                                                                   | 469 us: 1.35x faster                                                        |
| async_tree_memoization  | 485 ms                                                                   | 361 ms: 1.35x faster                                                        |
| async_tree_io           | 1.02 sec                                                                 | 762 ms: 1.34x faster                                                        |
| pycparser               | 873 ms                                                                   | 657 ms: 1.33x faster                                                        |
| html5lib                | 47.3 ms                                                                  | 36.4 ms: 1.30x faster                                                       |
| deepcopy_memo           | 28.4 us                                                                  | 22.2 us: 1.28x faster                                                       |
| pprint_pformat          | 1.23 sec                                                                 | 969 ms: 1.27x faster                                                        |
| genshi_xml              | 38.8 ms                                                                  | 30.8 ms: 1.26x faster                                                       |
| regex_compile           | 103 ms                                                                   | 82.3 ms: 1.26x faster                                                       |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.13 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 482 ms: 1.25x faster                                                        |
| spectral_norm           | 74.3 ms                                                                  | 59.8 ms: 1.24x faster                                                       |
| pprint_safe_repr        | 593 ms                                                                   | 478 ms: 1.24x faster                                                        |
| nbody                   | 71.5 ms                                                                  | 57.8 ms: 1.24x faster                                                       |
| sqlglot_optimize        | 38.7 ms                                                                  | 31.3 ms: 1.24x faster                                                       |
| tornado_http            | 106 ms                                                                   | 86.4 ms: 1.23x faster                                                       |
| float                   | 59.5 ms                                                                  | 48.6 ms: 1.22x faster                                                       |
| chameleon               | 5.77 ms                                                                  | 4.75 ms: 1.22x faster                                                       |
| deepcopy                | 256 us                                                                   | 215 us: 1.19x faster                                                        |
| sqlglot_normalize       | 201 ms                                                                   | 171 ms: 1.18x faster                                                        |
| xml_etree_process       | 43.0 ms                                                                  | 36.8 ms: 1.17x faster                                                       |
| json                    | 3.18 ms                                                                  | 2.72 ms: 1.17x faster                                                       |
| mdp                     | 1.60 sec                                                                 | 1.37 sec: 1.17x faster                                                      |
| docutils                | 1.83 sec                                                                 | 1.57 sec: 1.16x faster                                                      |
| scimark_fft             | 187 ms                                                                   | 162 ms: 1.16x faster                                                        |
| deepcopy_reduce         | 2.18 us                                                                  | 1.90 us: 1.15x faster                                                       |
| comprehensions          | 16.0 us                                                                  | 13.9 us: 1.15x faster                                                       |
| 2to3                    | 229 ms                                                                   | 202 ms: 1.14x faster                                                        |
| coroutines              | 15.6 ms                                                                  | 13.8 ms: 1.14x faster                                                       |
| bench_thread_pool       | 953 us                                                                   | 845 us: 1.13x faster                                                        |
| regex_dna               | 131 ms                                                                   | 117 ms: 1.12x faster                                                        |
| sympy_expand            | 313 ms                                                                   | 280 ms: 1.12x faster                                                        |
| json_loads              | 14.2 us                                                                  | 12.8 us: 1.11x faster                                                       |
| dulwich_log             | 47.0 ms                                                                  | 42.6 ms: 1.10x faster                                                       |
| sympy_integrate         | 14.7 ms                                                                  | 13.3 ms: 1.10x faster                                                       |
| unpickle                | 8.88 us                                                                  | 8.10 us: 1.10x faster                                                       |
| regex_v8                | 15.1 ms                                                                  | 13.8 ms: 1.10x faster                                                       |
| create_gc_cycles        | 764 us                                                                   | 702 us: 1.09x faster                                                        |
| sympy_str               | 189 ms                                                                   | 175 ms: 1.08x faster                                                        |
| nqueens                 | 64.8 ms                                                                  | 60.3 ms: 1.08x faster                                                       |
| fannkuch                | 252 ms                                                                   | 235 ms: 1.07x faster                                                        |
| regex_effbot            | 1.64 ms                                                                  | 1.56 ms: 1.05x faster                                                       |
| xml_etree_parse         | 95.6 ms                                                                  | 90.9 ms: 1.05x faster                                                       |
| sympy_sum               | 102 ms                                                                   | 98.5 ms: 1.04x faster                                                       |
| xml_etree_generate      | 53.8 ms                                                                  | 51.9 ms: 1.04x faster                                                       |
| meteor_contest          | 74.3 ms                                                                  | 72.1 ms: 1.03x faster                                                       |
| xml_etree_iterparse     | 62.5 ms                                                                  | 60.9 ms: 1.03x faster                                                       |
| python_startup          | 19.3 ms                                                                  | 18.9 ms: 1.02x faster                                                       |
| async_generators        | 214 ms                                                                   | 213 ms: 1.01x faster                                                        |
| logging_simple          | 6.12 us                                                                  | 6.20 us: 1.01x slower                                                       |
| unpickle_list           | 2.71 us                                                                  | 2.77 us: 1.02x slower                                                       |
| pidigits                | 145 ms                                                                   | 148 ms: 1.02x slower                                                        |
| telco                   | 3.77 ms                                                                  | 3.88 ms: 1.03x slower                                                       |
| pickle                  | 6.67 us                                                                  | 6.97 us: 1.05x slower                                                       |
| python_startup_no_site  | 14.8 ms                                                                  | 16.0 ms: 1.08x slower                                                       |
| pickle_list             | 2.57 us                                                                  | 2.78 us: 1.08x slower                                                       |
| gc_traversal            | 1.33 ms                                                                  | 1.49 ms: 1.12x slower                                                       |
| bench_mp_pool           | 59.2 ms                                                                  | 66.9 ms: 1.13x slower                                                       |
| pickle_dict             | 16.7 us                                                                  | 19.1 us: 1.14x slower                                                       |
| pathlib                 | 75.2 ms                                                                  | 86.6 ms: 1.15x slower                                                       |
| dask                    | 310 ms                                                                   | 358 ms: 1.15x slower                                                        |
| coverage                | 37.5 ms                                                                  | 52.8 ms: 1.41x slower                                                       |
| Geometric mean          | (ref)                                                                    | 1.20x faster                                                                |

Benchmark hidden because not significant (2): logging_format, sqlite_synth
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
