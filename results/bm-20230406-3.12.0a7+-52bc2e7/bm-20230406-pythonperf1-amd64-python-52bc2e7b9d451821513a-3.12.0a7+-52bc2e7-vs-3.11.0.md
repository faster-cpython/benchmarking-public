
# Results vs. 3.11.0

- fork: python
- ref: 52bc2e7b9d451821513a
- machine: windows-amd64
- commit hash: 52bc2e7
- commit date: 2023-04-06
- overall geometric mean: 1.08x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 204 ms                                                                   | 202 ms: 1.01x faster                                                        |
| chameleon      | 5.15 ms                                                                  | 4.75 ms: 1.09x faster                                                       |
| docutils       | 1.59 sec                                                                 | 1.57 sec: 1.01x faster                                                      |
| html5lib       | 38.5 ms                                                                  | 36.4 ms: 1.06x faster                                                       |
| tornado_http   | 91.8 ms                                                                  | 86.4 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.9 ms                                                                  | 57.8 ms: 1.23x faster                                                       |
| float          | 53.3 ms                                                                  | 48.6 ms: 1.10x faster                                                       |
| pidigits       | 147 ms                                                                   | 148 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 89.7 ms                                                                  | 82.3 ms: 1.09x faster                                                       |
| regex_effbot   | 1.63 ms                                                                  | 1.56 ms: 1.05x faster                                                       |
| regex_dna      | 115 ms                                                                   | 117 ms: 1.02x slower                                                        |
| regex_v8       | 13.5 ms                                                                  | 13.8 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                    | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.71 ms                                                                  | 5.36 ms: 1.44x faster                                                       |
| unpickle_pure_python | 150 us                                                                   | 129 us: 1.16x faster                                                        |
| pickle_pure_python   | 203 us                                                                   | 176 us: 1.16x faster                                                        |
| json_loads           | 13.5 us                                                                  | 12.8 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 61.8 ms                                                                  | 60.9 ms: 1.01x faster                                                       |
| xml_etree_parse      | 92.1 ms                                                                  | 90.9 ms: 1.01x faster                                                       |
| xml_etree_generate   | 52.3 ms                                                                  | 51.9 ms: 1.01x faster                                                       |
| pickle_dict          | 18.6 us                                                                  | 19.1 us: 1.02x slower                                                       |
| pickle_list          | 2.70 us                                                                  | 2.78 us: 1.03x slower                                                       |
| pickle               | 6.47 us                                                                  | 6.97 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                                    | 1.05x faster                                                                |

Benchmark hidden because not significant (3): unpickle_list, xml_etree_process, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 18.4 ms                                                                  | 18.9 ms: 1.03x slower                                                       |
| python_startup_no_site | 15.4 ms                                                                  | 16.0 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                                    | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.3 ms                                                                  | 13.7 ms: 1.26x faster                                                       |
| genshi_xml      | 38.0 ms                                                                  | 30.8 ms: 1.23x faster                                                       |
| mako            | 7.20 ms                                                                  | 6.15 ms: 1.17x faster                                                       |
| django_template | 23.9 ms                                                                  | 21.7 ms: 1.10x faster                                                       |
| Geometric mean  | (ref)                                                                    | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 33.5 ms                                                                  | 20.9 ms: 1.61x faster                                                       |
| unpack_sequence         | 43.1 ns                                                                  | 27.4 ns: 1.57x faster                                                       |
| json_dumps              | 7.71 ms                                                                  | 5.36 ms: 1.44x faster                                                       |
| asyncio_tcp             | 674 ms                                                                   | 482 ms: 1.40x faster                                                        |
| deltablue               | 2.68 ms                                                                  | 1.97 ms: 1.36x faster                                                       |
| logging_silent          | 71.0 ns                                                                  | 55.8 ns: 1.27x faster                                                       |
| mypy2                   | 276 ms                                                                   | 218 ms: 1.26x faster                                                        |
| genshi_text             | 17.3 ms                                                                  | 13.7 ms: 1.26x faster                                                       |
| richards                | 32.1 ms                                                                  | 25.5 ms: 1.26x faster                                                       |
| genshi_xml              | 38.0 ms                                                                  | 30.8 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.13 ms: 1.23x faster                                                       |
| nbody                   | 70.9 ms                                                                  | 57.8 ms: 1.23x faster                                                       |
| mdp                     | 1.67 sec                                                                 | 1.37 sec: 1.22x faster                                                      |
| sqlglot_parse           | 929 us                                                                   | 773 us: 1.20x faster                                                        |
| spectral_norm           | 71.8 ms                                                                  | 59.8 ms: 1.20x faster                                                       |
| json                    | 3.20 ms                                                                  | 2.72 ms: 1.18x faster                                                       |
| sqlglot_transpile       | 1.13 ms                                                                  | 964 us: 1.17x faster                                                        |
| mako                    | 7.20 ms                                                                  | 6.15 ms: 1.17x faster                                                       |
| scimark_lu              | 62.8 ms                                                                  | 53.9 ms: 1.17x faster                                                       |
| go                      | 97.5 ms                                                                  | 83.9 ms: 1.16x faster                                                       |
| unpickle_pure_python    | 150 us                                                                   | 129 us: 1.16x faster                                                        |
| raytrace                | 206 ms                                                                   | 178 ms: 1.16x faster                                                        |
| pickle_pure_python      | 203 us                                                                   | 176 us: 1.16x faster                                                        |
| hexiom                  | 4.46 ms                                                                  | 3.86 ms: 1.16x faster                                                       |
| chaos                   | 47.3 ms                                                                  | 41.2 ms: 1.15x faster                                                       |
| deepcopy_memo           | 25.3 us                                                                  | 22.2 us: 1.14x faster                                                       |
| scimark_fft             | 183 ms                                                                   | 162 ms: 1.13x faster                                                        |
| deepcopy                | 240 us                                                                   | 215 us: 1.11x faster                                                        |
| scimark_monte_carlo     | 45.8 ms                                                                  | 41.2 ms: 1.11x faster                                                       |
| comprehensions          | 15.4 us                                                                  | 13.9 us: 1.10x faster                                                       |
| sqlglot_normalize       | 189 ms                                                                   | 171 ms: 1.10x faster                                                        |
| django_template         | 23.9 ms                                                                  | 21.7 ms: 1.10x faster                                                       |
| sqlglot_optimize        | 34.5 ms                                                                  | 31.3 ms: 1.10x faster                                                       |
| float                   | 53.3 ms                                                                  | 48.6 ms: 1.10x faster                                                       |
| logging_format          | 7.13 us                                                                  | 6.52 us: 1.09x faster                                                       |
| regex_compile           | 89.7 ms                                                                  | 82.3 ms: 1.09x faster                                                       |
| fannkuch                | 255 ms                                                                   | 235 ms: 1.09x faster                                                        |
| chameleon               | 5.15 ms                                                                  | 4.75 ms: 1.09x faster                                                       |
| deepcopy_reduce         | 2.06 us                                                                  | 1.90 us: 1.08x faster                                                       |
| pprint_pformat          | 1.05 sec                                                                 | 969 ms: 1.08x faster                                                        |
| nqueens                 | 65.1 ms                                                                  | 60.3 ms: 1.08x faster                                                       |
| coroutines              | 14.8 ms                                                                  | 13.8 ms: 1.08x faster                                                       |
| crypto_pyaes            | 48.3 ms                                                                  | 45.0 ms: 1.07x faster                                                       |
| pprint_safe_repr        | 512 ms                                                                   | 478 ms: 1.07x faster                                                        |
| sympy_expand            | 298 ms                                                                   | 280 ms: 1.07x faster                                                        |
| logging_simple          | 6.60 us                                                                  | 6.20 us: 1.07x faster                                                       |
| scimark_sor             | 77.7 ms                                                                  | 73.1 ms: 1.06x faster                                                       |
| tornado_http            | 91.8 ms                                                                  | 86.4 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed | 512 ms                                                                   | 482 ms: 1.06x faster                                                        |
| pyflate                 | 302 ms                                                                   | 285 ms: 1.06x faster                                                        |
| json_loads              | 13.5 us                                                                  | 12.8 us: 1.06x faster                                                       |
| html5lib                | 38.5 ms                                                                  | 36.4 ms: 1.06x faster                                                       |
| sympy_str               | 184 ms                                                                   | 175 ms: 1.05x faster                                                        |
| coverage                | 55.3 ms                                                                  | 52.8 ms: 1.05x faster                                                       |
| regex_effbot            | 1.63 ms                                                                  | 1.56 ms: 1.05x faster                                                       |
| pycparser               | 686 ms                                                                   | 657 ms: 1.04x faster                                                        |
| async_tree_memoization  | 374 ms                                                                   | 361 ms: 1.04x faster                                                        |
| thrift                  | 487 us                                                                   | 469 us: 1.04x faster                                                        |
| async_tree_none         | 313 ms                                                                   | 302 ms: 1.04x faster                                                        |
| meteor_contest          | 74.4 ms                                                                  | 72.1 ms: 1.03x faster                                                       |
| sympy_integrate         | 13.7 ms                                                                  | 13.3 ms: 1.02x faster                                                       |
| dulwich_log             | 43.4 ms                                                                  | 42.6 ms: 1.02x faster                                                       |
| xml_etree_iterparse     | 61.8 ms                                                                  | 60.9 ms: 1.01x faster                                                       |
| docutils                | 1.59 sec                                                                 | 1.57 sec: 1.01x faster                                                      |
| xml_etree_parse         | 92.1 ms                                                                  | 90.9 ms: 1.01x faster                                                       |
| bench_thread_pool       | 856 us                                                                   | 845 us: 1.01x faster                                                        |
| telco                   | 3.93 ms                                                                  | 3.88 ms: 1.01x faster                                                       |
| 2to3                    | 204 ms                                                                   | 202 ms: 1.01x faster                                                        |
| xml_etree_generate      | 52.3 ms                                                                  | 51.9 ms: 1.01x faster                                                       |
| pidigits                | 147 ms                                                                   | 148 ms: 1.01x slower                                                        |
| regex_dna               | 115 ms                                                                   | 117 ms: 1.02x slower                                                        |
| regex_v8                | 13.5 ms                                                                  | 13.8 ms: 1.02x slower                                                       |
| pickle_dict             | 18.6 us                                                                  | 19.1 us: 1.02x slower                                                       |
| async_tree_io           | 744 ms                                                                   | 762 ms: 1.02x slower                                                        |
| python_startup          | 18.4 ms                                                                  | 18.9 ms: 1.03x slower                                                       |
| pickle_list             | 2.70 us                                                                  | 2.78 us: 1.03x slower                                                       |
| python_startup_no_site  | 15.4 ms                                                                  | 16.0 ms: 1.04x slower                                                       |
| create_gc_cycles        | 666 us                                                                   | 702 us: 1.05x slower                                                        |
| gc_traversal            | 1.40 ms                                                                  | 1.49 ms: 1.06x slower                                                       |
| pickle                  | 6.47 us                                                                  | 6.97 us: 1.08x slower                                                       |
| bench_mp_pool           | 61.2 ms                                                                  | 66.9 ms: 1.09x slower                                                       |
| sqlite_synth            | 1.67 us                                                                  | 1.85 us: 1.10x slower                                                       |
| async_generators        | 180 ms                                                                   | 213 ms: 1.18x slower                                                        |
| pathlib                 | 72.9 ms                                                                  | 86.6 ms: 1.19x slower                                                       |
| dask                    | 267 ms                                                                   | 358 ms: 1.34x slower                                                        |
| Geometric mean          | (ref)                                                                    | 1.08x faster                                                                |

Benchmark hidden because not significant (4): unpickle_list, sympy_sum, xml_etree_process, unpickle
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
