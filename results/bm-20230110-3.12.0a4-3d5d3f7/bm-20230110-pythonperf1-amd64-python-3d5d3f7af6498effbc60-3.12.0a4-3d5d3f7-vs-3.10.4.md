
# Results vs. 3.10.4

- fork: python
- ref: 3d5d3f7af6498effbc60
- machine: windows-amd64
- commit hash: 3d5d3f7
- commit date: 2023-01-10
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 193 ms: 1.19x faster                                                       |
| chameleon      | 5.77 ms                                                                  | 4.39 ms: 1.32x faster                                                      |
| docutils       | 1.83 sec                                                                 | 1.48 sec: 1.24x faster                                                     |
| html5lib       | 47.3 ms                                                                  | 33.7 ms: 1.40x faster                                                      |
| Geometric mean | (ref)                                                                    | 1.28x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 59.5 ms                                                                  | 47.2 ms: 1.26x faster                                                      |
| nbody          | 71.5 ms                                                                  | 59.5 ms: 1.20x faster                                                      |
| pidigits       | 145 ms                                                                   | 145 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                    | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 78.8 ms: 1.31x faster                                                      |
| regex_v8       | 15.1 ms                                                                  | 13.6 ms: 1.11x faster                                                      |
| regex_dna      | 131 ms                                                                   | 120 ms: 1.09x faster                                                       |
| regex_effbot   | 1.64 ms                                                                  | 1.59 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                                    | 1.13x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.00 ms                                                                  | 5.10 ms: 1.77x faster                                                      |
| pickle_pure_python   | 264 us                                                                   | 169 us: 1.56x faster                                                       |
| unpickle_pure_python | 179 us                                                                   | 119 us: 1.50x faster                                                       |
| xml_etree_process    | 43.0 ms                                                                  | 33.8 ms: 1.27x faster                                                      |
| json_loads           | 14.2 us                                                                  | 12.4 us: 1.14x faster                                                      |
| xml_etree_generate   | 53.8 ms                                                                  | 48.3 ms: 1.11x faster                                                      |
| xml_etree_parse      | 95.6 ms                                                                  | 86.5 ms: 1.10x faster                                                      |
| unpickle_list        | 2.71 us                                                                  | 2.59 us: 1.05x faster                                                      |
| xml_etree_iterparse  | 62.5 ms                                                                  | 60.1 ms: 1.04x faster                                                      |
| pickle               | 6.67 us                                                                  | 6.55 us: 1.02x faster                                                      |
| pickle_dict          | 16.7 us                                                                  | 18.2 us: 1.09x slower                                                      |
| pickle_list          | 2.57 us                                                                  | 2.81 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                                    | 1.16x faster                                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 18.1 ms: 1.06x faster                                                      |
| python_startup_no_site | 14.8 ms                                                                  | 15.2 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                                    | 1.02x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 8.69 ms                                                                  | 6.05 ms: 1.44x faster                                                      |
| django_template | 29.2 ms                                                                  | 20.7 ms: 1.41x faster                                                      |
| genshi_text     | 18.5 ms                                                                  | 13.3 ms: 1.40x faster                                                      |
| genshi_xml      | 38.8 ms                                                                  | 30.5 ms: 1.27x faster                                                      |
| Geometric mean  | (ref)                                                                    | 1.38x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 1.94 ms: 2.14x faster                                                      |
| go                      | 143 ms                                                                   | 80.4 ms: 1.78x faster                                                      |
| json_dumps              | 9.00 ms                                                                  | 5.10 ms: 1.77x faster                                                      |
| logging_silent          | 94.6 ns                                                                  | 54.2 ns: 1.75x faster                                                      |
| richards                | 41.0 ms                                                                  | 24.0 ms: 1.71x faster                                                      |
| scimark_sor             | 104 ms                                                                   | 63.7 ms: 1.63x faster                                                      |
| mypy2                   | 337 ms                                                                   | 209 ms: 1.61x faster                                                       |
| raytrace                | 267 ms                                                                   | 171 ms: 1.56x faster                                                       |
| pickle_pure_python      | 264 us                                                                   | 169 us: 1.56x faster                                                       |
| unpickle_pure_python    | 179 us                                                                   | 119 us: 1.50x faster                                                       |
| unpack_sequence         | 39.4 ns                                                                  | 26.2 ns: 1.50x faster                                                      |
| scimark_lu              | 83.9 ms                                                                  | 56.0 ms: 1.50x faster                                                      |
| scimark_monte_carlo     | 56.0 ms                                                                  | 38.0 ms: 1.47x faster                                                      |
| pyflate                 | 388 ms                                                                   | 263 ms: 1.47x faster                                                       |
| hexiom                  | 5.45 ms                                                                  | 3.77 ms: 1.45x faster                                                      |
| sqlglot_transpile       | 1.47 ms                                                                  | 1.02 ms: 1.44x faster                                                      |
| sqlglot_parse           | 1.22 ms                                                                  | 848 us: 1.44x faster                                                       |
| mako                    | 8.69 ms                                                                  | 6.05 ms: 1.44x faster                                                      |
| asyncio_tcp             | 664 ms                                                                   | 466 ms: 1.42x faster                                                       |
| async_tree_memoization  | 485 ms                                                                   | 342 ms: 1.42x faster                                                       |
| django_template         | 29.2 ms                                                                  | 20.7 ms: 1.41x faster                                                      |
| async_tree_none         | 414 ms                                                                   | 295 ms: 1.40x faster                                                       |
| html5lib                | 47.3 ms                                                                  | 33.7 ms: 1.40x faster                                                      |
| genshi_text             | 18.5 ms                                                                  | 13.3 ms: 1.40x faster                                                      |
| deepcopy_memo           | 28.4 us                                                                  | 20.4 us: 1.39x faster                                                      |
| pycparser               | 873 ms                                                                   | 628 ms: 1.39x faster                                                       |
| chaos                   | 58.4 ms                                                                  | 42.1 ms: 1.39x faster                                                      |
| async_tree_io           | 1.02 sec                                                                 | 742 ms: 1.38x faster                                                       |
| thrift                  | 632 us                                                                   | 463 us: 1.37x faster                                                       |
| crypto_pyaes            | 61.4 ms                                                                  | 45.9 ms: 1.34x faster                                                      |
| pprint_pformat          | 1.23 sec                                                                 | 918 ms: 1.34x faster                                                       |
| pprint_safe_repr        | 593 ms                                                                   | 448 ms: 1.32x faster                                                       |
| chameleon               | 5.77 ms                                                                  | 4.39 ms: 1.32x faster                                                      |
| regex_compile           | 103 ms                                                                   | 78.8 ms: 1.31x faster                                                      |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 465 ms: 1.30x faster                                                       |
| deepcopy                | 256 us                                                                   | 199 us: 1.28x faster                                                       |
| xml_etree_process       | 43.0 ms                                                                  | 33.8 ms: 1.27x faster                                                      |
| genshi_xml              | 38.8 ms                                                                  | 30.5 ms: 1.27x faster                                                      |
| async_generators        | 214 ms                                                                   | 169 ms: 1.27x faster                                                       |
| dask                    | 310 ms                                                                   | 246 ms: 1.26x faster                                                       |
| sqlglot_optimize        | 38.7 ms                                                                  | 30.6 ms: 1.26x faster                                                      |
| float                   | 59.5 ms                                                                  | 47.2 ms: 1.26x faster                                                      |
| docutils                | 1.83 sec                                                                 | 1.48 sec: 1.24x faster                                                     |
| deepcopy_reduce         | 2.18 us                                                                  | 1.78 us: 1.23x faster                                                      |
| json                    | 3.18 ms                                                                  | 2.61 ms: 1.22x faster                                                      |
| nbody                   | 71.5 ms                                                                  | 59.5 ms: 1.20x faster                                                      |
| sqlglot_normalize       | 201 ms                                                                   | 168 ms: 1.19x faster                                                       |
| bench_thread_pool       | 953 us                                                                   | 798 us: 1.19x faster                                                       |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.25 ms: 1.19x faster                                                      |
| 2to3                    | 229 ms                                                                   | 193 ms: 1.19x faster                                                       |
| spectral_norm           | 74.3 ms                                                                  | 62.8 ms: 1.18x faster                                                      |
| dulwich_log             | 47.0 ms                                                                  | 40.1 ms: 1.17x faster                                                      |
| sympy_integrate         | 14.7 ms                                                                  | 12.6 ms: 1.17x faster                                                      |
| sympy_expand            | 313 ms                                                                   | 269 ms: 1.16x faster                                                       |
| fannkuch                | 252 ms                                                                   | 217 ms: 1.16x faster                                                       |
| create_gc_cycles        | 764 us                                                                   | 661 us: 1.16x faster                                                       |
| json_loads              | 14.2 us                                                                  | 12.4 us: 1.14x faster                                                      |
| nqueens                 | 64.8 ms                                                                  | 57.3 ms: 1.13x faster                                                      |
| coroutines              | 15.6 ms                                                                  | 13.9 ms: 1.12x faster                                                      |
| scimark_fft             | 187 ms                                                                   | 167 ms: 1.12x faster                                                       |
| sympy_str               | 189 ms                                                                   | 168 ms: 1.12x faster                                                       |
| xml_etree_generate      | 53.8 ms                                                                  | 48.3 ms: 1.11x faster                                                      |
| sympy_sum               | 102 ms                                                                   | 92.0 ms: 1.11x faster                                                      |
| regex_v8                | 15.1 ms                                                                  | 13.6 ms: 1.11x faster                                                      |
| xml_etree_parse         | 95.6 ms                                                                  | 86.5 ms: 1.10x faster                                                      |
| meteor_contest          | 74.3 ms                                                                  | 67.9 ms: 1.09x faster                                                      |
| regex_dna               | 131 ms                                                                   | 120 ms: 1.09x faster                                                       |
| sqlite_synth            | 1.85 us                                                                  | 1.72 us: 1.08x faster                                                      |
| comprehensions          | 16.0 us                                                                  | 15.0 us: 1.07x faster                                                      |
| python_startup          | 19.3 ms                                                                  | 18.1 ms: 1.06x faster                                                      |
| mdp                     | 1.60 sec                                                                 | 1.51 sec: 1.06x faster                                                     |
| telco                   | 3.77 ms                                                                  | 3.59 ms: 1.05x faster                                                      |
| unpickle_list           | 2.71 us                                                                  | 2.59 us: 1.05x faster                                                      |
| logging_simple          | 6.12 us                                                                  | 5.84 us: 1.05x faster                                                      |
| xml_etree_iterparse     | 62.5 ms                                                                  | 60.1 ms: 1.04x faster                                                      |
| logging_format          | 6.53 us                                                                  | 6.29 us: 1.04x faster                                                      |
| regex_effbot            | 1.64 ms                                                                  | 1.59 ms: 1.03x faster                                                      |
| pathlib                 | 75.2 ms                                                                  | 73.2 ms: 1.03x faster                                                      |
| pickle                  | 6.67 us                                                                  | 6.55 us: 1.02x faster                                                      |
| pidigits                | 145 ms                                                                   | 145 ms: 1.00x slower                                                       |
| python_startup_no_site  | 14.8 ms                                                                  | 15.2 ms: 1.03x slower                                                      |
| bench_mp_pool           | 59.2 ms                                                                  | 61.1 ms: 1.03x slower                                                      |
| generators              | 31.4 ms                                                                  | 33.1 ms: 1.05x slower                                                      |
| gc_traversal            | 1.33 ms                                                                  | 1.43 ms: 1.08x slower                                                      |
| pickle_dict             | 16.7 us                                                                  | 18.2 us: 1.09x slower                                                      |
| pickle_list             | 2.57 us                                                                  | 2.81 us: 1.09x slower                                                      |
| coverage                | 37.5 ms                                                                  | 52.5 ms: 1.40x slower                                                      |
| Geometric mean          | (ref)                                                                    | 1.24x faster                                                               |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
