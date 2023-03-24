
# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_predict
- machine: windows-amd64
- commit hash: ed869aa
- commit date: 2023-03-23
- overall geometric mean: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 196 ms: 1.17x faster                                                        |
| chameleon      | 5.77 ms                                                                  | 4.54 ms: 1.27x faster                                                       |
| docutils       | 1.83 sec                                                                 | 1.52 sec: 1.20x faster                                                      |
| html5lib       | 47.3 ms                                                                  | 35.8 ms: 1.32x faster                                                       |
| tornado_http   | 106 ms                                                                   | 87.2 ms: 1.22x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.24x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.5 ms                                                                  | 56.6 ms: 1.26x faster                                                       |
| float          | 59.5 ms                                                                  | 47.2 ms: 1.26x faster                                                       |
| pidigits       | 145 ms                                                                   | 145 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                    | 1.17x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 82.3 ms: 1.26x faster                                                       |
| regex_v8       | 15.1 ms                                                                  | 13.5 ms: 1.12x faster                                                       |
| regex_dna      | 131 ms                                                                   | 121 ms: 1.09x faster                                                        |
| regex_effbot   | 1.64 ms                                                                  | 1.70 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                    | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.00 ms                                                                  | 5.41 ms: 1.66x faster                                                       |
| pickle_pure_python   | 264 us                                                                   | 175 us: 1.51x faster                                                        |
| unpickle_pure_python | 179 us                                                                   | 127 us: 1.41x faster                                                        |
| xml_etree_process    | 43.0 ms                                                                  | 35.7 ms: 1.21x faster                                                       |
| unpickle             | 8.88 us                                                                  | 8.01 us: 1.11x faster                                                       |
| xml_etree_parse      | 95.6 ms                                                                  | 90.4 ms: 1.06x faster                                                       |
| json_loads           | 14.2 us                                                                  | 13.5 us: 1.05x faster                                                       |
| xml_etree_generate   | 53.8 ms                                                                  | 51.8 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 62.5 ms                                                                  | 61.7 ms: 1.01x faster                                                       |
| pickle               | 6.67 us                                                                  | 6.78 us: 1.02x slower                                                       |
| pickle_list          | 2.57 us                                                                  | 2.82 us: 1.10x slower                                                       |
| pickle_dict          | 16.7 us                                                                  | 18.6 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                                    | 1.12x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 18.2 ms: 1.06x faster                                                       |
| python_startup_no_site | 14.8 ms                                                                  | 15.4 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                                    | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 29.2 ms                                                                  | 20.5 ms: 1.43x faster                                                       |
| mako            | 8.69 ms                                                                  | 6.21 ms: 1.40x faster                                                       |
| genshi_text     | 18.5 ms                                                                  | 13.5 ms: 1.37x faster                                                       |
| genshi_xml      | 38.8 ms                                                                  | 30.5 ms: 1.27x faster                                                       |
| Geometric mean  | (ref)                                                                    | 1.37x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 1.98 ms: 2.09x faster                                                       |
| json_dumps              | 9.00 ms                                                                  | 5.41 ms: 1.66x faster                                                       |
| go                      | 143 ms                                                                   | 87.3 ms: 1.64x faster                                                       |
| logging_silent          | 94.6 ns                                                                  | 57.7 ns: 1.64x faster                                                       |
| mypy2                   | 337 ms                                                                   | 211 ms: 1.60x faster                                                        |
| raytrace                | 267 ms                                                                   | 172 ms: 1.55x faster                                                        |
| scimark_lu              | 83.9 ms                                                                  | 54.4 ms: 1.54x faster                                                       |
| richards                | 41.0 ms                                                                  | 26.7 ms: 1.54x faster                                                       |
| pickle_pure_python      | 264 us                                                                   | 175 us: 1.51x faster                                                        |
| generators              | 31.4 ms                                                                  | 21.2 ms: 1.48x faster                                                       |
| django_template         | 29.2 ms                                                                  | 20.5 ms: 1.43x faster                                                       |
| chaos                   | 58.4 ms                                                                  | 41.2 ms: 1.42x faster                                                       |
| unpickle_pure_python    | 179 us                                                                   | 127 us: 1.41x faster                                                        |
| asyncio_tcp             | 664 ms                                                                   | 471 ms: 1.41x faster                                                        |
| unpack_sequence         | 39.4 ns                                                                  | 28.1 ns: 1.40x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                                  | 871 us: 1.40x faster                                                        |
| hexiom                  | 5.45 ms                                                                  | 3.90 ms: 1.40x faster                                                       |
| mako                    | 8.69 ms                                                                  | 6.21 ms: 1.40x faster                                                       |
| async_tree_none         | 414 ms                                                                   | 296 ms: 1.40x faster                                                        |
| async_tree_io           | 1.02 sec                                                                 | 736 ms: 1.39x faster                                                        |
| sqlglot_transpile       | 1.47 ms                                                                  | 1.06 ms: 1.39x faster                                                       |
| scimark_sor             | 104 ms                                                                   | 74.8 ms: 1.38x faster                                                       |
| thrift                  | 632 us                                                                   | 457 us: 1.38x faster                                                        |
| pyflate                 | 388 ms                                                                   | 282 ms: 1.38x faster                                                        |
| async_tree_memoization  | 485 ms                                                                   | 353 ms: 1.37x faster                                                        |
| genshi_text             | 18.5 ms                                                                  | 13.5 ms: 1.37x faster                                                       |
| scimark_monte_carlo     | 56.0 ms                                                                  | 41.1 ms: 1.36x faster                                                       |
| crypto_pyaes            | 61.4 ms                                                                  | 45.2 ms: 1.36x faster                                                       |
| pycparser               | 873 ms                                                                   | 653 ms: 1.34x faster                                                        |
| html5lib                | 47.3 ms                                                                  | 35.8 ms: 1.32x faster                                                       |
| pprint_pformat          | 1.23 sec                                                                 | 936 ms: 1.31x faster                                                        |
| deepcopy_memo           | 28.4 us                                                                  | 21.9 us: 1.30x faster                                                       |
| pprint_safe_repr        | 593 ms                                                                   | 462 ms: 1.28x faster                                                        |
| chameleon               | 5.77 ms                                                                  | 4.54 ms: 1.27x faster                                                       |
| genshi_xml              | 38.8 ms                                                                  | 30.5 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 478 ms: 1.26x faster                                                        |
| nbody                   | 71.5 ms                                                                  | 56.6 ms: 1.26x faster                                                       |
| float                   | 59.5 ms                                                                  | 47.2 ms: 1.26x faster                                                       |
| regex_compile           | 103 ms                                                                   | 82.3 ms: 1.26x faster                                                       |
| sqlglot_optimize        | 38.7 ms                                                                  | 31.4 ms: 1.23x faster                                                       |
| tornado_http            | 106 ms                                                                   | 87.2 ms: 1.22x faster                                                       |
| xml_etree_process       | 43.0 ms                                                                  | 35.7 ms: 1.21x faster                                                       |
| docutils                | 1.83 sec                                                                 | 1.52 sec: 1.20x faster                                                      |
| sqlglot_normalize       | 201 ms                                                                   | 168 ms: 1.19x faster                                                        |
| deepcopy                | 256 us                                                                   | 215 us: 1.19x faster                                                        |
| json                    | 3.18 ms                                                                  | 2.70 ms: 1.18x faster                                                       |
| deepcopy_reduce         | 2.18 us                                                                  | 1.86 us: 1.18x faster                                                       |
| 2to3                    | 229 ms                                                                   | 196 ms: 1.17x faster                                                        |
| spectral_norm           | 74.3 ms                                                                  | 63.6 ms: 1.17x faster                                                       |
| sympy_expand            | 313 ms                                                                   | 270 ms: 1.16x faster                                                        |
| bench_thread_pool       | 953 us                                                                   | 825 us: 1.15x faster                                                        |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.32 ms: 1.15x faster                                                       |
| sympy_integrate         | 14.7 ms                                                                  | 12.8 ms: 1.15x faster                                                       |
| nqueens                 | 64.8 ms                                                                  | 57.5 ms: 1.13x faster                                                       |
| regex_v8                | 15.1 ms                                                                  | 13.5 ms: 1.12x faster                                                       |
| scimark_fft             | 187 ms                                                                   | 167 ms: 1.12x faster                                                        |
| mdp                     | 1.60 sec                                                                 | 1.44 sec: 1.11x faster                                                      |
| unpickle                | 8.88 us                                                                  | 8.01 us: 1.11x faster                                                       |
| sympy_str               | 189 ms                                                                   | 171 ms: 1.11x faster                                                        |
| create_gc_cycles        | 764 us                                                                   | 698 us: 1.09x faster                                                        |
| coroutines              | 15.6 ms                                                                  | 14.3 ms: 1.09x faster                                                       |
| dulwich_log             | 47.0 ms                                                                  | 43.2 ms: 1.09x faster                                                       |
| regex_dna               | 131 ms                                                                   | 121 ms: 1.09x faster                                                        |
| fannkuch                | 252 ms                                                                   | 233 ms: 1.08x faster                                                        |
| meteor_contest          | 74.3 ms                                                                  | 69.8 ms: 1.06x faster                                                       |
| sympy_sum               | 102 ms                                                                   | 96.3 ms: 1.06x faster                                                       |
| python_startup          | 19.3 ms                                                                  | 18.2 ms: 1.06x faster                                                       |
| xml_etree_parse         | 95.6 ms                                                                  | 90.4 ms: 1.06x faster                                                       |
| json_loads              | 14.2 us                                                                  | 13.5 us: 1.05x faster                                                       |
| comprehensions          | 16.0 us                                                                  | 15.2 us: 1.05x faster                                                       |
| xml_etree_generate      | 53.8 ms                                                                  | 51.8 ms: 1.04x faster                                                       |
| sqlite_synth            | 1.85 us                                                                  | 1.78 us: 1.04x faster                                                       |
| async_generators        | 214 ms                                                                   | 208 ms: 1.03x faster                                                        |
| xml_etree_iterparse     | 62.5 ms                                                                  | 61.7 ms: 1.01x faster                                                       |
| logging_format          | 6.53 us                                                                  | 6.46 us: 1.01x faster                                                       |
| pidigits                | 145 ms                                                                   | 145 ms: 1.00x faster                                                        |
| telco                   | 3.77 ms                                                                  | 3.80 ms: 1.01x slower                                                       |
| pickle                  | 6.67 us                                                                  | 6.78 us: 1.02x slower                                                       |
| regex_effbot            | 1.64 ms                                                                  | 1.70 ms: 1.03x slower                                                       |
| python_startup_no_site  | 14.8 ms                                                                  | 15.4 ms: 1.04x slower                                                       |
| bench_mp_pool           | 59.2 ms                                                                  | 64.5 ms: 1.09x slower                                                       |
| gc_traversal            | 1.33 ms                                                                  | 1.46 ms: 1.10x slower                                                       |
| pathlib                 | 75.2 ms                                                                  | 82.7 ms: 1.10x slower                                                       |
| pickle_list             | 2.57 us                                                                  | 2.82 us: 1.10x slower                                                       |
| pickle_dict             | 16.7 us                                                                  | 18.6 us: 1.12x slower                                                       |
| dask                    | 310 ms                                                                   | 355 ms: 1.14x slower                                                        |
| coverage                | 37.5 ms                                                                  | 52.9 ms: 1.41x slower                                                       |
| Geometric mean          | (ref)                                                                    | 1.20x faster                                                                |

Benchmark hidden because not significant (2): logging_simple, unpickle_list
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
