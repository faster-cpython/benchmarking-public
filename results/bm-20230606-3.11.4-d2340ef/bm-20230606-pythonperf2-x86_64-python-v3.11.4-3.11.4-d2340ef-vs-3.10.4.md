
# Results vs. 3.10.4

- fork: python
- ref: v3.11.4
- machine: linux-x86_64
- commit hash: d2340ef
- commit date: 2023-06-06
- overall geometric mean: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf2-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                         |
| chameleon      | 9.72 ms                                                      | 7.63 ms: 1.27x faster                                        |
| docutils       | 3.40 sec                                                     | 2.83 sec: 1.20x faster                                       |
| html5lib       | 94.6 ms                                                      | 71.5 ms: 1.32x faster                                        |
| tornado_http   | 152 ms                                                       | 121 ms: 1.26x faster                                         |
| Geometric mean | (ref)                                                        | 1.26x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf2-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 110 ms                                                       | 73.8 ms: 1.49x faster                                        |
| nbody          | 137 ms                                                       | 95.6 ms: 1.44x faster                                        |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                         |
| Geometric mean | (ref)                                                        | 1.32x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf2-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 155 ms: 1.25x faster                                         |
| regex_dna      | 259 ms                                                       | 231 ms: 1.12x faster                                         |
| regex_v8       | 26.6 ms                                                      | 24.5 ms: 1.09x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.46 ms: 1.16x slower                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf2-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 321 us: 1.43x faster                                         |
| xml_etree_process    | 76.0 ms                                                      | 56.3 ms: 1.35x faster                                        |
| unpickle_pure_python | 321 us                                                       | 243 us: 1.32x faster                                         |
| tomli_loads          | 2.97 sec                                                     | 2.27 sec: 1.31x faster                                       |
| xml_etree_generate   | 94.6 ms                                                      | 81.0 ms: 1.17x faster                                        |
| pickle_list          | 4.11 us                                                      | 3.70 us: 1.11x faster                                        |
| unpickle             | 14.2 us                                                      | 13.0 us: 1.09x faster                                        |
| json_dumps           | 14.2 ms                                                      | 13.4 ms: 1.06x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                         |
| json_loads           | 30.0 us                                                      | 28.4 us: 1.05x faster                                        |
| xml_etree_parse      | 162 ms                                                       | 159 ms: 1.02x faster                                         |
| pickle_dict          | 30.0 us                                                      | 29.7 us: 1.01x faster                                        |
| unpickle_list        | 4.49 us                                                      | 4.69 us: 1.04x slower                                        |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf2-x86_64-python-v3.11.4-3.11.4-d2340ef |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.7 ms: 1.08x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 7.72 ms: 1.05x slower                                        |
| Geometric mean         | (ref)                                                        | 1.01x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf2-x86_64-python-v3.11.4-3.11.4-d2340ef |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                        |
| django_template | 51.5 ms                                                      | 39.7 ms: 1.30x faster                                        |
| genshi_text     | 31.5 ms                                                      | 25.6 ms: 1.23x faster                                        |
| genshi_xml      | 64.7 ms                                                      | 57.9 ms: 1.12x faster                                        |
| Geometric mean  | (ref)                                                        | 1.25x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-pythonperf2-x86_64-python-v3.11.4-3.11.4-d2340ef |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deltablue                | 7.47 ms                                                      | 4.06 ms: 1.84x faster                                        |
| logging_silent           | 166 ns                                                       | 101 ns: 1.64x faster                                         |
| scimark_monte_carlo      | 109 ms                                                       | 69.5 ms: 1.58x faster                                        |
| raytrace                 | 488 ms                                                       | 311 ms: 1.57x faster                                         |
| bench_mp_pool            | 7.18 ms                                                      | 4.58 ms: 1.57x faster                                        |
| scimark_sor              | 177 ms                                                       | 115 ms: 1.54x faster                                         |
| go                       | 259 ms                                                       | 170 ms: 1.52x faster                                         |
| pyflate                  | 697 ms                                                       | 458 ms: 1.52x faster                                         |
| float                    | 110 ms                                                       | 73.8 ms: 1.49x faster                                        |
| sqlglot_parse            | 2.26 ms                                                      | 1.55 ms: 1.46x faster                                        |
| spectral_norm            | 136 ms                                                       | 94.1 ms: 1.45x faster                                        |
| scimark_lu               | 164 ms                                                       | 113 ms: 1.44x faster                                         |
| nbody                    | 137 ms                                                       | 95.6 ms: 1.44x faster                                        |
| chaos                    | 107 ms                                                       | 75.0 ms: 1.43x faster                                        |
| pickle_pure_python       | 457 us                                                       | 321 us: 1.43x faster                                         |
| crypto_pyaes             | 118 ms                                                       | 83.1 ms: 1.42x faster                                        |
| richards                 | 74.1 ms                                                      | 52.2 ms: 1.42x faster                                        |
| sqlglot_transpile        | 2.71 ms                                                      | 1.91 ms: 1.42x faster                                        |
| richards_super           | 90.8 ms                                                      | 65.2 ms: 1.39x faster                                        |
| async_tree_io            | 1.61 sec                                                     | 1.17 sec: 1.37x faster                                       |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                        |
| xml_etree_process        | 76.0 ms                                                      | 56.3 ms: 1.35x faster                                        |
| hexiom                   | 9.52 ms                                                      | 7.06 ms: 1.35x faster                                        |
| async_tree_none          | 700 ms                                                       | 522 ms: 1.34x faster                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 784 ms: 1.34x faster                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                       |
| html5lib                 | 94.6 ms                                                      | 71.5 ms: 1.32x faster                                        |
| unpickle_pure_python     | 321 us                                                       | 243 us: 1.32x faster                                         |
| async_generators         | 422 ms                                                       | 322 ms: 1.31x faster                                         |
| tomli_loads              | 2.97 sec                                                     | 2.27 sec: 1.31x faster                                       |
| async_tree_memoization   | 824 ms                                                       | 630 ms: 1.31x faster                                         |
| unpack_sequence          | 59.5 ns                                                      | 45.6 ns: 1.31x faster                                        |
| pycparser                | 1.66 sec                                                     | 1.28 sec: 1.30x faster                                       |
| django_template          | 51.5 ms                                                      | 39.7 ms: 1.30x faster                                        |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.01 ms: 1.29x faster                                        |
| deepcopy_memo            | 48.9 us                                                      | 38.1 us: 1.28x faster                                        |
| scimark_fft              | 359 ms                                                       | 281 ms: 1.28x faster                                         |
| thrift                   | 1.16 ms                                                      | 912 us: 1.28x faster                                         |
| chameleon                | 9.72 ms                                                      | 7.63 ms: 1.27x faster                                        |
| logging_simple           | 8.90 us                                                      | 7.05 us: 1.26x faster                                        |
| logging_format           | 9.57 us                                                      | 7.58 us: 1.26x faster                                        |
| tornado_http             | 152 ms                                                       | 121 ms: 1.26x faster                                         |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 758 ms: 1.26x faster                                         |
| regex_compile            | 194 ms                                                       | 155 ms: 1.25x faster                                         |
| aiohttp                  | 1.21 ms                                                      | 980 us: 1.23x faster                                         |
| genshi_text              | 31.5 ms                                                      | 25.6 ms: 1.23x faster                                        |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                         |
| sqlalchemy_declarative   | 187 ms                                                       | 154 ms: 1.21x faster                                         |
| docutils                 | 3.40 sec                                                     | 2.83 sec: 1.20x faster                                       |
| gunicorn                 | 1.17 ms                                                      | 981 us: 1.20x faster                                         |
| sqlglot_optimize         | 70.3 ms                                                      | 58.7 ms: 1.20x faster                                        |
| sqlite_synth             | 2.97 us                                                      | 2.48 us: 1.20x faster                                        |
| deepcopy_reduce          | 4.03 us                                                      | 3.39 us: 1.19x faster                                        |
| sqlglot_normalize        | 144 ms                                                       | 122 ms: 1.19x faster                                         |
| dulwich_log              | 80.1 ms                                                      | 67.6 ms: 1.18x faster                                        |
| deepcopy                 | 454 us                                                       | 387 us: 1.17x faster                                         |
| xml_etree_generate       | 94.6 ms                                                      | 81.0 ms: 1.17x faster                                        |
| sqlalchemy_imperative    | 22.6 ms                                                      | 19.6 ms: 1.15x faster                                        |
| dask                     | 463 ms                                                       | 402 ms: 1.15x faster                                         |
| pathlib                  | 21.7 ms                                                      | 18.9 ms: 1.15x faster                                        |
| nqueens                  | 112 ms                                                       | 98.5 ms: 1.14x faster                                        |
| bench_thread_pool        | 1.14 ms                                                      | 995 us: 1.14x faster                                         |
| flaskblogging            | 4.39 ms                                                      | 3.87 ms: 1.13x faster                                        |
| fannkuch                 | 496 ms                                                       | 441 ms: 1.13x faster                                         |
| regex_dna                | 259 ms                                                       | 231 ms: 1.12x faster                                         |
| create_gc_cycles         | 1.82 ms                                                      | 1.63 ms: 1.12x faster                                        |
| genshi_xml               | 64.7 ms                                                      | 57.9 ms: 1.12x faster                                        |
| pickle_list              | 4.11 us                                                      | 3.70 us: 1.11x faster                                        |
| pylint                   | 562 ms                                                       | 510 ms: 1.10x faster                                         |
| sympy_integrate          | 28.1 ms                                                      | 25.6 ms: 1.09x faster                                        |
| coroutines               | 30.4 ms                                                      | 27.8 ms: 1.09x faster                                        |
| unpickle                 | 14.2 us                                                      | 13.0 us: 1.09x faster                                        |
| sympy_expand             | 599 ms                                                       | 550 ms: 1.09x faster                                         |
| regex_v8                 | 26.6 ms                                                      | 24.5 ms: 1.09x faster                                        |
| json                     | 5.96 ms                                                      | 5.48 ms: 1.09x faster                                        |
| comprehensions           | 26.9 us                                                      | 24.9 us: 1.08x faster                                        |
| python_startup           | 11.5 ms                                                      | 10.7 ms: 1.08x faster                                        |
| pidigits                 | 271 ms                                                       | 252 ms: 1.07x faster                                         |
| sympy_str                | 358 ms                                                       | 334 ms: 1.07x faster                                         |
| generators               | 58.0 ms                                                      | 54.7 ms: 1.06x faster                                        |
| mdp                      | 3.03 sec                                                     | 2.86 sec: 1.06x faster                                       |
| json_dumps               | 14.2 ms                                                      | 13.4 ms: 1.06x faster                                        |
| telco                    | 7.14 ms                                                      | 6.75 ms: 1.06x faster                                        |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                         |
| json_loads               | 30.0 us                                                      | 28.4 us: 1.05x faster                                        |
| meteor_contest           | 137 ms                                                       | 130 ms: 1.05x faster                                         |
| sympy_sum                | 193 ms                                                       | 183 ms: 1.05x faster                                         |
| asyncio_tcp              | 782 ms                                                       | 751 ms: 1.04x faster                                         |
| xml_etree_parse          | 162 ms                                                       | 159 ms: 1.02x faster                                         |
| pickle_dict              | 30.0 us                                                      | 29.7 us: 1.01x faster                                        |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 3.07 sec: 1.01x faster                                       |
| typing_runtime_protocols | 523 us                                                       | 525 us: 1.01x slower                                         |
| unpickle_list            | 4.49 us                                                      | 4.69 us: 1.04x slower                                        |
| python_startup_no_site   | 7.32 ms                                                      | 7.72 ms: 1.05x slower                                        |
| gc_traversal             | 3.45 ms                                                      | 3.70 ms: 1.07x slower                                        |
| mypy2                    | 466 ms                                                       | 535 ms: 1.15x slower                                         |
| regex_effbot             | 2.99 ms                                                      | 3.46 ms: 1.16x slower                                        |
| Geometric mean           | (ref)                                                        | 1.21x faster                                                 |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: coverage
