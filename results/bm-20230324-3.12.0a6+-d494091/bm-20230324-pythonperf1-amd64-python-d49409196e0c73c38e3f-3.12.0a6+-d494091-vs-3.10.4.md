
# Results vs. 3.10.4

- fork: python
- ref: d49409196e0c73c38e3f
- machine: windows-amd64
- commit hash: d494091
- commit date: 2023-03-24
- overall geometric mean: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 194 ms: 1.18x faster                                                        |
| chameleon      | 5.77 ms                                                                  | 4.30 ms: 1.34x faster                                                       |
| docutils       | 1.83 sec                                                                 | 1.51 sec: 1.21x faster                                                      |
| html5lib       | 47.3 ms                                                                  | 35.5 ms: 1.33x faster                                                       |
| tornado_http   | 106 ms                                                                   | 86.7 ms: 1.23x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 59.5 ms                                                                  | 46.0 ms: 1.29x faster                                                       |
| nbody          | 71.5 ms                                                                  | 55.6 ms: 1.29x faster                                                       |
| pidigits       | 145 ms                                                                   | 146 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.18x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 79.6 ms: 1.30x faster                                                       |
| regex_v8       | 15.1 ms                                                                  | 13.8 ms: 1.09x faster                                                       |
| regex_dna      | 131 ms                                                                   | 122 ms: 1.07x faster                                                        |
| regex_effbot   | 1.64 ms                                                                  | 1.83 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                                    | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.00 ms                                                                  | 5.44 ms: 1.65x faster                                                       |
| pickle_pure_python   | 264 us                                                                   | 168 us: 1.57x faster                                                        |
| unpickle_pure_python | 179 us                                                                   | 117 us: 1.53x faster                                                        |
| xml_etree_process    | 43.0 ms                                                                  | 33.9 ms: 1.27x faster                                                       |
| unpickle             | 8.88 us                                                                  | 7.96 us: 1.12x faster                                                       |
| xml_etree_parse      | 95.6 ms                                                                  | 87.3 ms: 1.10x faster                                                       |
| xml_etree_generate   | 53.8 ms                                                                  | 50.0 ms: 1.08x faster                                                       |
| json_loads           | 14.2 us                                                                  | 13.4 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 62.5 ms                                                                  | 59.2 ms: 1.06x faster                                                       |
| pickle_list          | 2.57 us                                                                  | 2.78 us: 1.08x slower                                                       |
| pickle_dict          | 16.7 us                                                                  | 18.6 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                                    | 1.15x faster                                                                |

Benchmark hidden because not significant (2): unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 18.2 ms: 1.06x faster                                                       |
| python_startup_no_site | 14.8 ms                                                                  | 15.3 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                                    | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 29.2 ms                                                                  | 19.9 ms: 1.47x faster                                                       |
| mako            | 8.69 ms                                                                  | 6.10 ms: 1.43x faster                                                       |
| genshi_text     | 18.5 ms                                                                  | 13.8 ms: 1.34x faster                                                       |
| genshi_xml      | 38.8 ms                                                                  | 30.5 ms: 1.27x faster                                                       |
| Geometric mean  | (ref)                                                                    | 1.37x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 1.91 ms: 2.17x faster                                                       |
| go                      | 143 ms                                                                   | 80.6 ms: 1.78x faster                                                       |
| logging_silent          | 94.6 ns                                                                  | 54.5 ns: 1.74x faster                                                       |
| richards                | 41.0 ms                                                                  | 24.3 ms: 1.69x faster                                                       |
| scimark_lu              | 83.9 ms                                                                  | 50.5 ms: 1.66x faster                                                       |
| json_dumps              | 9.00 ms                                                                  | 5.44 ms: 1.65x faster                                                       |
| raytrace                | 267 ms                                                                   | 164 ms: 1.63x faster                                                        |
| mypy2                   | 337 ms                                                                   | 209 ms: 1.61x faster                                                        |
| pickle_pure_python      | 264 us                                                                   | 168 us: 1.57x faster                                                        |
| unpickle_pure_python    | 179 us                                                                   | 117 us: 1.53x faster                                                        |
| generators              | 31.4 ms                                                                  | 20.9 ms: 1.51x faster                                                       |
| hexiom                  | 5.45 ms                                                                  | 3.66 ms: 1.49x faster                                                       |
| chaos                   | 58.4 ms                                                                  | 39.6 ms: 1.48x faster                                                       |
| scimark_sor             | 104 ms                                                                   | 70.6 ms: 1.47x faster                                                       |
| django_template         | 29.2 ms                                                                  | 19.9 ms: 1.47x faster                                                       |
| deepcopy_memo           | 28.4 us                                                                  | 19.6 us: 1.45x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                                  | 843 us: 1.45x faster                                                        |
| unpack_sequence         | 39.4 ns                                                                  | 27.4 ns: 1.44x faster                                                       |
| pyflate                 | 388 ms                                                                   | 271 ms: 1.43x faster                                                        |
| mako                    | 8.69 ms                                                                  | 6.10 ms: 1.43x faster                                                       |
| scimark_monte_carlo     | 56.0 ms                                                                  | 39.3 ms: 1.42x faster                                                       |
| sqlglot_transpile       | 1.47 ms                                                                  | 1.03 ms: 1.42x faster                                                       |
| async_tree_io           | 1.02 sec                                                                 | 723 ms: 1.41x faster                                                        |
| asyncio_tcp             | 664 ms                                                                   | 469 ms: 1.41x faster                                                        |
| async_tree_none         | 414 ms                                                                   | 295 ms: 1.40x faster                                                        |
| async_tree_memoization  | 485 ms                                                                   | 349 ms: 1.39x faster                                                        |
| crypto_pyaes            | 61.4 ms                                                                  | 44.3 ms: 1.39x faster                                                       |
| thrift                  | 632 us                                                                   | 459 us: 1.38x faster                                                        |
| pycparser               | 873 ms                                                                   | 640 ms: 1.36x faster                                                        |
| pprint_pformat          | 1.23 sec                                                                 | 902 ms: 1.36x faster                                                        |
| chameleon               | 5.77 ms                                                                  | 4.30 ms: 1.34x faster                                                       |
| genshi_text             | 18.5 ms                                                                  | 13.8 ms: 1.34x faster                                                       |
| pprint_safe_repr        | 593 ms                                                                   | 443 ms: 1.34x faster                                                        |
| html5lib                | 47.3 ms                                                                  | 35.5 ms: 1.33x faster                                                       |
| regex_compile           | 103 ms                                                                   | 79.6 ms: 1.30x faster                                                       |
| float                   | 59.5 ms                                                                  | 46.0 ms: 1.29x faster                                                       |
| nbody                   | 71.5 ms                                                                  | 55.6 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 473 ms: 1.28x faster                                                        |
| xml_etree_process       | 43.0 ms                                                                  | 33.9 ms: 1.27x faster                                                       |
| genshi_xml              | 38.8 ms                                                                  | 30.5 ms: 1.27x faster                                                       |
| sqlglot_optimize        | 38.7 ms                                                                  | 30.8 ms: 1.26x faster                                                       |
| deepcopy                | 256 us                                                                   | 204 us: 1.25x faster                                                        |
| tornado_http            | 106 ms                                                                   | 86.7 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.20 ms: 1.22x faster                                                       |
| spectral_norm           | 74.3 ms                                                                  | 61.1 ms: 1.22x faster                                                       |
| sqlglot_normalize       | 201 ms                                                                   | 166 ms: 1.21x faster                                                        |
| docutils                | 1.83 sec                                                                 | 1.51 sec: 1.21x faster                                                      |
| deepcopy_reduce         | 2.18 us                                                                  | 1.82 us: 1.20x faster                                                       |
| nqueens                 | 64.8 ms                                                                  | 54.1 ms: 1.20x faster                                                       |
| mdp                     | 1.60 sec                                                                 | 1.36 sec: 1.18x faster                                                      |
| 2to3                    | 229 ms                                                                   | 194 ms: 1.18x faster                                                        |
| json                    | 3.18 ms                                                                  | 2.71 ms: 1.18x faster                                                       |
| scimark_fft             | 187 ms                                                                   | 159 ms: 1.18x faster                                                        |
| bench_thread_pool       | 953 us                                                                   | 818 us: 1.16x faster                                                        |
| sympy_expand            | 313 ms                                                                   | 271 ms: 1.16x faster                                                        |
| sympy_integrate         | 14.7 ms                                                                  | 12.8 ms: 1.15x faster                                                       |
| fannkuch                | 252 ms                                                                   | 222 ms: 1.13x faster                                                        |
| coroutines              | 15.6 ms                                                                  | 13.9 ms: 1.12x faster                                                       |
| unpickle                | 8.88 us                                                                  | 7.96 us: 1.12x faster                                                       |
| dulwich_log             | 47.0 ms                                                                  | 42.1 ms: 1.12x faster                                                       |
| sympy_str               | 189 ms                                                                   | 169 ms: 1.11x faster                                                        |
| create_gc_cycles        | 764 us                                                                   | 698 us: 1.10x faster                                                        |
| xml_etree_parse         | 95.6 ms                                                                  | 87.3 ms: 1.10x faster                                                       |
| regex_v8                | 15.1 ms                                                                  | 13.8 ms: 1.09x faster                                                       |
| comprehensions          | 16.0 us                                                                  | 14.8 us: 1.08x faster                                                       |
| xml_etree_generate      | 53.8 ms                                                                  | 50.0 ms: 1.08x faster                                                       |
| regex_dna               | 131 ms                                                                   | 122 ms: 1.07x faster                                                        |
| sympy_sum               | 102 ms                                                                   | 95.6 ms: 1.07x faster                                                       |
| async_generators        | 214 ms                                                                   | 202 ms: 1.06x faster                                                        |
| json_loads              | 14.2 us                                                                  | 13.4 us: 1.06x faster                                                       |
| python_startup          | 19.3 ms                                                                  | 18.2 ms: 1.06x faster                                                       |
| xml_etree_iterparse     | 62.5 ms                                                                  | 59.2 ms: 1.06x faster                                                       |
| meteor_contest          | 74.3 ms                                                                  | 70.4 ms: 1.05x faster                                                       |
| sqlite_synth            | 1.85 us                                                                  | 1.76 us: 1.05x faster                                                       |
| logging_simple          | 6.12 us                                                                  | 5.91 us: 1.04x faster                                                       |
| logging_format          | 6.53 us                                                                  | 6.41 us: 1.02x faster                                                       |
| pidigits                | 145 ms                                                                   | 146 ms: 1.01x slower                                                        |
| telco                   | 3.77 ms                                                                  | 3.85 ms: 1.02x slower                                                       |
| python_startup_no_site  | 14.8 ms                                                                  | 15.3 ms: 1.03x slower                                                       |
| pickle_list             | 2.57 us                                                                  | 2.78 us: 1.08x slower                                                       |
| pathlib                 | 75.2 ms                                                                  | 82.2 ms: 1.09x slower                                                       |
| bench_mp_pool           | 59.2 ms                                                                  | 64.8 ms: 1.10x slower                                                       |
| gc_traversal            | 1.33 ms                                                                  | 1.47 ms: 1.11x slower                                                       |
| pickle_dict             | 16.7 us                                                                  | 18.6 us: 1.11x slower                                                       |
| regex_effbot            | 1.64 ms                                                                  | 1.83 ms: 1.12x slower                                                       |
| dask                    | 310 ms                                                                   | 353 ms: 1.14x slower                                                        |
| coverage                | 37.5 ms                                                                  | 50.1 ms: 1.34x slower                                                       |
| Geometric mean          | (ref)                                                                    | 1.23x faster                                                                |

Benchmark hidden because not significant (2): unpickle_list, pickle
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
