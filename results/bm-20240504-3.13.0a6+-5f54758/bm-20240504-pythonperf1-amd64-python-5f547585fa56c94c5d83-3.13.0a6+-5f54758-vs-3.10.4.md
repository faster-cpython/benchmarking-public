# Results vs. 3.10.4

- fork: python
- ref: 5f547585fa56c94c5d83
- machine: windows-amd64
- commit hash: 5f54758
- commit date: 2024-05-04
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 207 ms: 1.19x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.64 ms: 1.25x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.17x faster                                                      |
| html5lib       | 51.0 ms                                                     | 35.8 ms: 1.42x faster                                                       |
| tornado_http   | 108 ms                                                      | 81.8 ms: 1.33x faster                                                       |
| Geometric mean | (ref)                                                       | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 219 ms: 1.99x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 268 ms: 1.96x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 585 ms: 1.90x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 388 ms: 1.64x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 49.9 ms: 1.24x faster                                                       |
| nbody          | 71.3 ms                                                     | 66.1 ms: 1.08x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.6 ms: 1.37x faster                                                       |
| regex_dna      | 136 ms                                                      | 124 ms: 1.10x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 17.6 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.61 ms: 1.63x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 176 us: 1.53x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 125 us: 1.46x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 36.9 ms: 1.21x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 91.0 ms: 1.06x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.58 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 53.9 ms: 1.03x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.75 us: 1.02x slower                                                       |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                       |
| pickle               | 6.85 us                                                     | 7.22 us: 1.05x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.4 us: 1.07x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.05 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.1 ms: 1.03x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.42 ms: 1.41x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 14.5 ms: 1.37x faster                                                       |
| django_template | 28.9 ms                                                     | 21.5 ms: 1.34x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 31.5 ms: 1.30x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 100.0 us: 3.36x faster                                                      |
| deltablue                | 4.19 ms                                                     | 1.86 ms: 2.25x faster                                                       |
| async_tree_none          | 435 ms                                                      | 219 ms: 1.99x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 268 ms: 1.96x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 585 ms: 1.90x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 50.3 ns: 1.88x faster                                                       |
| richards_super           | 52.2 ms                                                     | 29.3 ms: 1.78x faster                                                       |
| raytrace                 | 273 ms                                                      | 156 ms: 1.75x faster                                                        |
| generators               | 32.4 ms                                                     | 18.6 ms: 1.74x faster                                                       |
| pylint                   | 350 ms                                                      | 207 ms: 1.69x faster                                                        |
| go                       | 139 ms                                                      | 84.0 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 388 ms: 1.64x faster                                                        |
| richards                 | 42.4 ms                                                     | 25.9 ms: 1.64x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.61 ms: 1.63x faster                                                       |
| chaos                    | 61.7 ms                                                     | 38.0 ms: 1.62x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.61x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 757 us: 1.60x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 476 ms: 1.54x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 176 us: 1.53x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 963 us: 1.53x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 3.79 ms: 1.51x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 56.8 ms: 1.51x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 125 us: 1.46x faster                                                        |
| pyflate                  | 409 ms                                                      | 283 ms: 1.45x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 35.8 ms: 1.42x faster                                                       |
| scimark_sor              | 106 ms                                                      | 74.7 ms: 1.42x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.4 ms: 1.42x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.42 ms: 1.41x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 14.5 ms: 1.37x faster                                                       |
| regex_compile            | 106 ms                                                      | 77.6 ms: 1.37x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.31 sec: 1.36x faster                                                      |
| django_template          | 28.9 ms                                                     | 21.5 ms: 1.34x faster                                                       |
| tornado_http             | 108 ms                                                      | 81.8 ms: 1.33x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.61 sec: 1.32x faster                                                      |
| mypy2                    | 555 ms                                                      | 423 ms: 1.31x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 31.5 ms: 1.30x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 22.3 us: 1.29x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 48.6 ms: 1.29x faster                                                       |
| coroutines               | 16.0 ms                                                     | 12.6 ms: 1.27x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 964 ms: 1.27x faster                                                        |
| sympy_sum                | 107 ms                                                      | 84.6 ms: 1.27x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.1 ms: 1.26x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 473 ms: 1.25x faster                                                        |
| chameleon                | 5.79 ms                                                     | 4.64 ms: 1.25x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                                       |
| float                    | 61.7 ms                                                     | 49.9 ms: 1.24x faster                                                       |
| pycparser                | 930 ms                                                      | 754 ms: 1.23x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 62.8 ms: 1.23x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 32.6 ms: 1.22x faster                                                       |
| sympy_str                | 194 ms                                                      | 161 ms: 1.21x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 36.9 ms: 1.21x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 171 ms: 1.20x faster                                                        |
| deepcopy                 | 255 us                                                      | 214 us: 1.19x faster                                                        |
| 2to3                     | 246 ms                                                      | 207 ms: 1.19x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.17x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 818 us: 1.17x faster                                                        |
| sympy_expand             | 314 ms                                                      | 271 ms: 1.16x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 57.8 ms: 1.15x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                                       |
| aiohttp                  | 995 us                                                      | 900 us: 1.11x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.11 us: 1.11x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.67 us: 1.10x faster                                                       |
| regex_dna                | 136 ms                                                      | 124 ms: 1.10x faster                                                        |
| nbody                    | 71.3 ms                                                     | 66.1 ms: 1.08x faster                                                       |
| scimark_fft              | 187 ms                                                      | 176 ms: 1.07x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 91.0 ms: 1.06x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.57 ms: 1.06x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.58 us: 1.06x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 72.1 ms: 1.05x faster                                                       |
| fannkuch                 | 256 ms                                                      | 243 ms: 1.05x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 53.9 ms: 1.03x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                       |
| python_startup           | 20.6 ms                                                     | 20.1 ms: 1.03x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| unpickle_list            | 2.71 us                                                     | 2.75 us: 1.02x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 64.7 ms: 1.04x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 79.1 ms: 1.05x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.22 us: 1.05x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.4 us: 1.07x slower                                                       |
| json                     | 3.14 ms                                                     | 3.38 ms: 1.08x slower                                                       |
| async_generators         | 222 ms                                                      | 244 ms: 1.10x slower                                                        |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                       |
| coverage                 | 39.0 ms                                                     | 43.2 ms: 1.11x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.05 us: 1.11x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 906 us: 1.13x slower                                                        |
| regex_v8                 | 15.4 ms                                                     | 17.6 ms: 1.14x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.81 ms: 1.22x slower                                                       |
| thrift                   | 617 us                                                      | 8.09 ms: 13.10x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                                |

Benchmark hidden because not significant (2): flaskblogging, dask
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240504-3.13.0a6+-5f54758/bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown