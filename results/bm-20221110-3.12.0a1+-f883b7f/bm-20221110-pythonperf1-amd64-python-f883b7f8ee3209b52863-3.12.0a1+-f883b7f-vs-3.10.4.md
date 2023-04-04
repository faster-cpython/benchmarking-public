
# Results vs. 3.10.4

- fork: python
- ref: f883b7f8ee3209b52863
- machine: windows-amd64
- commit hash: f883b7f
- commit date: 2022-11-10
- overall geometric mean: 1.14x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 200 ms: 1.15x faster                                                        |
| chameleon      | 5.77 ms                                                                  | 4.97 ms: 1.16x faster                                                       |
| docutils       | 1.83 sec                                                                 | 1.59 sec: 1.15x faster                                                      |
| html5lib       | 47.3 ms                                                                  | 36.2 ms: 1.31x faster                                                       |
| tornado_http   | 106 ms                                                                   | 93.2 ms: 1.14x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.18x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.5 ms                                                                  | 62.7 ms: 1.14x faster                                                       |
| float          | 59.5 ms                                                                  | 52.3 ms: 1.14x faster                                                       |
| pidigits       | 145 ms                                                                   | 150 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 87.2 ms: 1.19x faster                                                       |
| regex_v8       | 15.1 ms                                                                  | 14.0 ms: 1.08x faster                                                       |
| regex_dna      | 131 ms                                                                   | 122 ms: 1.07x faster                                                        |
| regex_effbot   | 1.64 ms                                                                  | 1.60 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.00 ms                                                                  | 5.48 ms: 1.64x faster                                                       |
| pickle_pure_python   | 264 us                                                                   | 190 us: 1.39x faster                                                        |
| unpickle_pure_python | 179 us                                                                   | 148 us: 1.21x faster                                                        |
| xml_etree_process    | 43.0 ms                                                                  | 36.6 ms: 1.18x faster                                                       |
| unpickle             | 8.88 us                                                                  | 8.06 us: 1.10x faster                                                       |
| json_loads           | 14.2 us                                                                  | 13.1 us: 1.08x faster                                                       |
| xml_etree_parse      | 95.6 ms                                                                  | 90.9 ms: 1.05x faster                                                       |
| unpickle_list        | 2.71 us                                                                  | 2.60 us: 1.05x faster                                                       |
| xml_etree_generate   | 53.8 ms                                                                  | 52.2 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 62.5 ms                                                                  | 63.9 ms: 1.02x slower                                                       |
| pickle               | 6.67 us                                                                  | 7.14 us: 1.07x slower                                                       |
| pickle_list          | 2.57 us                                                                  | 2.82 us: 1.10x slower                                                       |
| pickle_dict          | 16.7 us                                                                  | 19.1 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                                    | 1.09x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 18.9 ms: 1.02x faster                                                       |
| python_startup_no_site | 14.8 ms                                                                  | 15.8 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                                    | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.69 ms                                                                  | 6.58 ms: 1.32x faster                                                       |
| django_template | 29.2 ms                                                                  | 22.1 ms: 1.32x faster                                                       |
| genshi_text     | 18.5 ms                                                                  | 16.3 ms: 1.14x faster                                                       |
| genshi_xml      | 38.8 ms                                                                  | 35.9 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                                    | 1.21x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 2.37 ms: 1.75x faster                                                       |
| json_dumps              | 9.00 ms                                                                  | 5.48 ms: 1.64x faster                                                       |
| go                      | 143 ms                                                                   | 89.7 ms: 1.60x faster                                                       |
| richards                | 41.0 ms                                                                  | 26.8 ms: 1.53x faster                                                       |
| mypy2                   | 337 ms                                                                   | 225 ms: 1.50x faster                                                        |
| logging_silent          | 94.6 ns                                                                  | 64.1 ns: 1.48x faster                                                       |
| raytrace                | 267 ms                                                                   | 190 ms: 1.41x faster                                                        |
| scimark_sor             | 104 ms                                                                   | 73.7 ms: 1.40x faster                                                       |
| pickle_pure_python      | 264 us                                                                   | 190 us: 1.39x faster                                                        |
| scimark_monte_carlo     | 56.0 ms                                                                  | 41.3 ms: 1.36x faster                                                       |
| crypto_pyaes            | 61.4 ms                                                                  | 45.3 ms: 1.36x faster                                                       |
| sqlglot_transpile       | 1.47 ms                                                                  | 1.09 ms: 1.35x faster                                                       |
| scimark_lu              | 83.9 ms                                                                  | 62.4 ms: 1.35x faster                                                       |
| pyflate                 | 388 ms                                                                   | 290 ms: 1.34x faster                                                        |
| mako                    | 8.69 ms                                                                  | 6.58 ms: 1.32x faster                                                       |
| django_template         | 29.2 ms                                                                  | 22.1 ms: 1.32x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                                  | 924 us: 1.32x faster                                                        |
| thrift                  | 632 us                                                                   | 479 us: 1.32x faster                                                        |
| async_tree_io           | 1.02 sec                                                                 | 782 ms: 1.31x faster                                                        |
| pycparser               | 873 ms                                                                   | 669 ms: 1.31x faster                                                        |
| html5lib                | 47.3 ms                                                                  | 36.2 ms: 1.31x faster                                                       |
| chaos                   | 58.4 ms                                                                  | 45.4 ms: 1.29x faster                                                       |
| hexiom                  | 5.45 ms                                                                  | 4.34 ms: 1.26x faster                                                       |
| async_tree_none         | 414 ms                                                                   | 330 ms: 1.26x faster                                                        |
| async_tree_memoization  | 485 ms                                                                   | 389 ms: 1.25x faster                                                        |
| pprint_safe_repr        | 593 ms                                                                   | 485 ms: 1.22x faster                                                        |
| pprint_pformat          | 1.23 sec                                                                 | 1.01 sec: 1.22x faster                                                      |
| unpack_sequence         | 39.4 ns                                                                  | 32.4 ns: 1.21x faster                                                       |
| unpickle_pure_python    | 179 us                                                                   | 148 us: 1.21x faster                                                        |
| async_generators        | 214 ms                                                                   | 177 ms: 1.21x faster                                                        |
| regex_compile           | 103 ms                                                                   | 87.2 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 510 ms: 1.19x faster                                                        |
| sqlglot_optimize        | 38.7 ms                                                                  | 32.6 ms: 1.19x faster                                                       |
| xml_etree_process       | 43.0 ms                                                                  | 36.6 ms: 1.18x faster                                                       |
| json                    | 3.18 ms                                                                  | 2.70 ms: 1.18x faster                                                       |
| chameleon               | 5.77 ms                                                                  | 4.97 ms: 1.16x faster                                                       |
| dask                    | 310 ms                                                                   | 268 ms: 1.16x faster                                                        |
| deepcopy_memo           | 28.4 us                                                                  | 24.7 us: 1.15x faster                                                       |
| docutils                | 1.83 sec                                                                 | 1.59 sec: 1.15x faster                                                      |
| 2to3                    | 229 ms                                                                   | 200 ms: 1.15x faster                                                        |
| tornado_http            | 106 ms                                                                   | 93.2 ms: 1.14x faster                                                       |
| genshi_text             | 18.5 ms                                                                  | 16.3 ms: 1.14x faster                                                       |
| nbody                   | 71.5 ms                                                                  | 62.7 ms: 1.14x faster                                                       |
| float                   | 59.5 ms                                                                  | 52.3 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.36 ms: 1.13x faster                                                       |
| bench_thread_pool       | 953 us                                                                   | 843 us: 1.13x faster                                                        |
| create_gc_cycles        | 764 us                                                                   | 688 us: 1.11x faster                                                        |
| sympy_integrate         | 14.7 ms                                                                  | 13.3 ms: 1.10x faster                                                       |
| unpickle                | 8.88 us                                                                  | 8.06 us: 1.10x faster                                                       |
| spectral_norm           | 74.3 ms                                                                  | 67.5 ms: 1.10x faster                                                       |
| sympy_expand            | 313 ms                                                                   | 285 ms: 1.10x faster                                                        |
| sqlglot_normalize       | 201 ms                                                                   | 184 ms: 1.09x faster                                                        |
| scimark_fft             | 187 ms                                                                   | 172 ms: 1.09x faster                                                        |
| genshi_xml              | 38.8 ms                                                                  | 35.9 ms: 1.08x faster                                                       |
| json_loads              | 14.2 us                                                                  | 13.1 us: 1.08x faster                                                       |
| regex_v8                | 15.1 ms                                                                  | 14.0 ms: 1.08x faster                                                       |
| coroutines              | 15.6 ms                                                                  | 14.5 ms: 1.08x faster                                                       |
| regex_dna               | 131 ms                                                                   | 122 ms: 1.07x faster                                                        |
| deepcopy_reduce         | 2.18 us                                                                  | 2.03 us: 1.07x faster                                                       |
| dulwich_log             | 47.0 ms                                                                  | 43.8 ms: 1.07x faster                                                       |
| deepcopy                | 256 us                                                                   | 241 us: 1.06x faster                                                        |
| meteor_contest          | 74.3 ms                                                                  | 70.5 ms: 1.05x faster                                                       |
| xml_etree_parse         | 95.6 ms                                                                  | 90.9 ms: 1.05x faster                                                       |
| nqueens                 | 64.8 ms                                                                  | 61.8 ms: 1.05x faster                                                       |
| sympy_sum               | 102 ms                                                                   | 97.5 ms: 1.05x faster                                                       |
| unpickle_list           | 2.71 us                                                                  | 2.60 us: 1.05x faster                                                       |
| sympy_str               | 189 ms                                                                   | 183 ms: 1.03x faster                                                        |
| xml_etree_generate      | 53.8 ms                                                                  | 52.2 ms: 1.03x faster                                                       |
| sqlite_synth            | 1.85 us                                                                  | 1.79 us: 1.03x faster                                                       |
| regex_effbot            | 1.64 ms                                                                  | 1.60 ms: 1.03x faster                                                       |
| pathlib                 | 75.2 ms                                                                  | 73.5 ms: 1.02x faster                                                       |
| python_startup          | 19.3 ms                                                                  | 18.9 ms: 1.02x faster                                                       |
| fannkuch                | 252 ms                                                                   | 247 ms: 1.02x faster                                                        |
| mdp                     | 1.60 sec                                                                 | 1.57 sec: 1.02x faster                                                      |
| xml_etree_iterparse     | 62.5 ms                                                                  | 63.9 ms: 1.02x slower                                                       |
| telco                   | 3.77 ms                                                                  | 3.86 ms: 1.03x slower                                                       |
| pidigits                | 145 ms                                                                   | 150 ms: 1.04x slower                                                        |
| python_startup_no_site  | 14.8 ms                                                                  | 15.8 ms: 1.07x slower                                                       |
| bench_mp_pool           | 59.2 ms                                                                  | 63.2 ms: 1.07x slower                                                       |
| pickle                  | 6.67 us                                                                  | 7.14 us: 1.07x slower                                                       |
| generators              | 31.4 ms                                                                  | 33.6 ms: 1.07x slower                                                       |
| asyncio_tcp             | 664 ms                                                                   | 714 ms: 1.08x slower                                                        |
| logging_simple          | 6.12 us                                                                  | 6.60 us: 1.08x slower                                                       |
| logging_format          | 6.53 us                                                                  | 7.05 us: 1.08x slower                                                       |
| pickle_list             | 2.57 us                                                                  | 2.82 us: 1.10x slower                                                       |
| gc_traversal            | 1.33 ms                                                                  | 1.48 ms: 1.11x slower                                                       |
| pickle_dict             | 16.7 us                                                                  | 19.1 us: 1.14x slower                                                       |
| coverage                | 37.5 ms                                                                  | 54.2 ms: 1.45x slower                                                       |
| Geometric mean          | (ref)                                                                    | 1.14x faster                                                                |

Benchmark hidden because not significant (1): comprehensions
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
