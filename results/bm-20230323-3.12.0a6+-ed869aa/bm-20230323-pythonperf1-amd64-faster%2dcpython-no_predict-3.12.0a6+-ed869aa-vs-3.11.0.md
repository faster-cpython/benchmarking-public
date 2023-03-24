
# Results vs. 3.11.0

- fork: faster-cpython
- ref: no_predict
- machine: windows-amd64
- commit hash: ed869aa
- commit date: 2023-03-23
- overall geometric mean: 1.09x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 204 ms                                                                   | 196 ms: 1.04x faster                                                        |
| chameleon      | 5.15 ms                                                                  | 4.54 ms: 1.14x faster                                                       |
| docutils       | 1.59 sec                                                                 | 1.52 sec: 1.05x faster                                                      |
| html5lib       | 38.5 ms                                                                  | 35.8 ms: 1.08x faster                                                       |
| tornado_http   | 91.8 ms                                                                  | 87.2 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.07x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.9 ms                                                                  | 56.6 ms: 1.25x faster                                                       |
| float          | 53.3 ms                                                                  | 47.2 ms: 1.13x faster                                                       |
| pidigits       | 147 ms                                                                   | 145 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                    | 1.13x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 89.7 ms                                                                  | 82.3 ms: 1.09x faster                                                       |
| regex_effbot   | 1.63 ms                                                                  | 1.70 ms: 1.04x slower                                                       |
| regex_dna      | 115 ms                                                                   | 121 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.71 ms                                                                  | 5.41 ms: 1.42x faster                                                       |
| unpickle_pure_python | 150 us                                                                   | 127 us: 1.18x faster                                                        |
| pickle_pure_python   | 203 us                                                                   | 175 us: 1.16x faster                                                        |
| unpickle_list        | 2.80 us                                                                  | 2.72 us: 1.03x faster                                                       |
| xml_etree_process    | 36.6 ms                                                                  | 35.7 ms: 1.02x faster                                                       |
| xml_etree_parse      | 92.1 ms                                                                  | 90.4 ms: 1.02x faster                                                       |
| xml_etree_generate   | 52.3 ms                                                                  | 51.8 ms: 1.01x faster                                                       |
| json_loads           | 13.5 us                                                                  | 13.5 us: 1.00x faster                                                       |
| pickle_list          | 2.70 us                                                                  | 2.82 us: 1.04x slower                                                       |
| pickle               | 6.47 us                                                                  | 6.78 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                                    | 1.05x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_iterparse, unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 18.4 ms                                                                  | 18.2 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.3 ms                                                                  | 13.5 ms: 1.27x faster                                                       |
| genshi_xml      | 38.0 ms                                                                  | 30.5 ms: 1.25x faster                                                       |
| django_template | 23.9 ms                                                                  | 20.5 ms: 1.17x faster                                                       |
| mako            | 7.20 ms                                                                  | 6.21 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                                    | 1.21x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 33.5 ms                                                                  | 21.2 ms: 1.58x faster                                                       |
| unpack_sequence         | 43.1 ns                                                                  | 28.1 ns: 1.53x faster                                                       |
| asyncio_tcp             | 674 ms                                                                   | 471 ms: 1.43x faster                                                        |
| json_dumps              | 7.71 ms                                                                  | 5.41 ms: 1.42x faster                                                       |
| deltablue               | 2.68 ms                                                                  | 1.98 ms: 1.35x faster                                                       |
| mypy2                   | 276 ms                                                                   | 211 ms: 1.31x faster                                                        |
| genshi_text             | 17.3 ms                                                                  | 13.5 ms: 1.27x faster                                                       |
| nbody                   | 70.9 ms                                                                  | 56.6 ms: 1.25x faster                                                       |
| genshi_xml              | 38.0 ms                                                                  | 30.5 ms: 1.25x faster                                                       |
| logging_silent          | 71.0 ns                                                                  | 57.7 ns: 1.23x faster                                                       |
| richards                | 32.1 ms                                                                  | 26.7 ms: 1.20x faster                                                       |
| raytrace                | 206 ms                                                                   | 172 ms: 1.20x faster                                                        |
| json                    | 3.20 ms                                                                  | 2.70 ms: 1.19x faster                                                       |
| unpickle_pure_python    | 150 us                                                                   | 127 us: 1.18x faster                                                        |
| django_template         | 23.9 ms                                                                  | 20.5 ms: 1.17x faster                                                       |
| pickle_pure_python      | 203 us                                                                   | 175 us: 1.16x faster                                                        |
| mdp                     | 1.67 sec                                                                 | 1.44 sec: 1.16x faster                                                      |
| mako                    | 7.20 ms                                                                  | 6.21 ms: 1.16x faster                                                       |
| deepcopy_memo           | 25.3 us                                                                  | 21.9 us: 1.16x faster                                                       |
| scimark_lu              | 62.8 ms                                                                  | 54.4 ms: 1.15x faster                                                       |
| chaos                   | 47.3 ms                                                                  | 41.2 ms: 1.15x faster                                                       |
| hexiom                  | 4.46 ms                                                                  | 3.90 ms: 1.14x faster                                                       |
| chameleon               | 5.15 ms                                                                  | 4.54 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult | 2.63 ms                                                                  | 2.32 ms: 1.13x faster                                                       |
| nqueens                 | 65.1 ms                                                                  | 57.5 ms: 1.13x faster                                                       |
| spectral_norm           | 71.8 ms                                                                  | 63.6 ms: 1.13x faster                                                       |
| float                   | 53.3 ms                                                                  | 47.2 ms: 1.13x faster                                                       |
| pprint_pformat          | 1.05 sec                                                                 | 936 ms: 1.12x faster                                                        |
| sqlglot_normalize       | 189 ms                                                                   | 168 ms: 1.12x faster                                                        |
| go                      | 97.5 ms                                                                  | 87.3 ms: 1.12x faster                                                       |
| deepcopy                | 240 us                                                                   | 215 us: 1.12x faster                                                        |
| scimark_monte_carlo     | 45.8 ms                                                                  | 41.1 ms: 1.11x faster                                                       |
| deepcopy_reduce         | 2.06 us                                                                  | 1.86 us: 1.11x faster                                                       |
| pprint_safe_repr        | 512 ms                                                                   | 462 ms: 1.11x faster                                                        |
| sympy_expand            | 298 ms                                                                   | 270 ms: 1.11x faster                                                        |
| logging_format          | 7.13 us                                                                  | 6.46 us: 1.10x faster                                                       |
| sqlglot_optimize        | 34.5 ms                                                                  | 31.4 ms: 1.10x faster                                                       |
| fannkuch                | 255 ms                                                                   | 233 ms: 1.10x faster                                                        |
| scimark_fft             | 183 ms                                                                   | 167 ms: 1.09x faster                                                        |
| regex_compile           | 89.7 ms                                                                  | 82.3 ms: 1.09x faster                                                       |
| logging_simple          | 6.60 us                                                                  | 6.10 us: 1.08x faster                                                       |
| sympy_str               | 184 ms                                                                   | 171 ms: 1.08x faster                                                        |
| html5lib                | 38.5 ms                                                                  | 35.8 ms: 1.08x faster                                                       |
| pyflate                 | 302 ms                                                                   | 282 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed | 512 ms                                                                   | 478 ms: 1.07x faster                                                        |
| sympy_integrate         | 13.7 ms                                                                  | 12.8 ms: 1.07x faster                                                       |
| crypto_pyaes            | 48.3 ms                                                                  | 45.2 ms: 1.07x faster                                                       |
| sqlglot_transpile       | 1.13 ms                                                                  | 1.06 ms: 1.07x faster                                                       |
| sqlglot_parse           | 929 us                                                                   | 871 us: 1.07x faster                                                        |
| meteor_contest          | 74.4 ms                                                                  | 69.8 ms: 1.07x faster                                                       |
| thrift                  | 487 us                                                                   | 457 us: 1.06x faster                                                        |
| async_tree_memoization  | 374 ms                                                                   | 353 ms: 1.06x faster                                                        |
| async_tree_none         | 313 ms                                                                   | 296 ms: 1.06x faster                                                        |
| tornado_http            | 91.8 ms                                                                  | 87.2 ms: 1.05x faster                                                       |
| pycparser               | 686 ms                                                                   | 653 ms: 1.05x faster                                                        |
| docutils                | 1.59 sec                                                                 | 1.52 sec: 1.05x faster                                                      |
| coverage                | 55.3 ms                                                                  | 52.9 ms: 1.05x faster                                                       |
| scimark_sor             | 77.7 ms                                                                  | 74.8 ms: 1.04x faster                                                       |
| 2to3                    | 204 ms                                                                   | 196 ms: 1.04x faster                                                        |
| bench_thread_pool       | 856 us                                                                   | 825 us: 1.04x faster                                                        |
| telco                   | 3.93 ms                                                                  | 3.80 ms: 1.03x faster                                                       |
| coroutines              | 14.8 ms                                                                  | 14.3 ms: 1.03x faster                                                       |
| unpickle_list           | 2.80 us                                                                  | 2.72 us: 1.03x faster                                                       |
| sympy_sum               | 98.9 ms                                                                  | 96.3 ms: 1.03x faster                                                       |
| xml_etree_process       | 36.6 ms                                                                  | 35.7 ms: 1.02x faster                                                       |
| xml_etree_parse         | 92.1 ms                                                                  | 90.4 ms: 1.02x faster                                                       |
| pidigits                | 147 ms                                                                   | 145 ms: 1.01x faster                                                        |
| python_startup          | 18.4 ms                                                                  | 18.2 ms: 1.01x faster                                                       |
| xml_etree_generate      | 52.3 ms                                                                  | 51.8 ms: 1.01x faster                                                       |
| async_tree_io           | 744 ms                                                                   | 736 ms: 1.01x faster                                                        |
| comprehensions          | 15.4 us                                                                  | 15.2 us: 1.01x faster                                                       |
| dulwich_log             | 43.4 ms                                                                  | 43.2 ms: 1.01x faster                                                       |
| json_loads              | 13.5 us                                                                  | 13.5 us: 1.00x faster                                                       |
| gc_traversal            | 1.40 ms                                                                  | 1.46 ms: 1.04x slower                                                       |
| regex_effbot            | 1.63 ms                                                                  | 1.70 ms: 1.04x slower                                                       |
| pickle_list             | 2.70 us                                                                  | 2.82 us: 1.04x slower                                                       |
| regex_dna               | 115 ms                                                                   | 121 ms: 1.05x slower                                                        |
| pickle                  | 6.47 us                                                                  | 6.78 us: 1.05x slower                                                       |
| create_gc_cycles        | 666 us                                                                   | 698 us: 1.05x slower                                                        |
| bench_mp_pool           | 61.2 ms                                                                  | 64.5 ms: 1.05x slower                                                       |
| sqlite_synth            | 1.67 us                                                                  | 1.78 us: 1.06x slower                                                       |
| pathlib                 | 72.9 ms                                                                  | 82.7 ms: 1.13x slower                                                       |
| async_generators        | 180 ms                                                                   | 208 ms: 1.15x slower                                                        |
| dask                    | 267 ms                                                                   | 355 ms: 1.33x slower                                                        |
| Geometric mean          | (ref)                                                                    | 1.09x faster                                                                |

Benchmark hidden because not significant (5): regex_v8, xml_etree_iterparse, unpickle, pickle_dict, python_startup_no_site
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
