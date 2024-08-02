# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b2
- machine: windows-amd64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 229 ms: 1.07x faster                                            |
| chameleon      | 5.79 ms                                                     | 5.00 ms: 1.16x faster                                           |
| docutils       | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                          |
| html5lib       | 51.0 ms                                                     | 37.9 ms: 1.35x faster                                           |
| tornado_http   | 108 ms                                                      | 86.1 ms: 1.26x faster                                           |
| Geometric mean | (ref)                                                       | 1.18x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 227 ms: 1.92x faster                                            |
| async_tree_io           | 1.11 sec                                                    | 579 ms: 1.92x faster                                            |
| async_tree_memoization  | 526 ms                                                      | 278 ms: 1.89x faster                                            |
| async_tree_cpu_io_mixed | 638 ms                                                      | 392 ms: 1.63x faster                                            |
| Geometric mean          | (ref)                                                       | 1.83x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                           |
| nbody          | 71.3 ms                                                     | 53.1 ms: 1.34x faster                                           |
| Geometric mean | (ref)                                                       | 1.23x faster                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 88.9 ms: 1.19x faster                                           |
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                            |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                           |
| Geometric mean | (ref)                                                       | 1.11x faster                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.70 ms: 1.61x faster                                           |
| pickle_pure_python   | 270 us                                                      | 175 us: 1.54x faster                                            |
| unpickle_pure_python | 183 us                                                      | 130 us: 1.41x faster                                            |
| tomli_loads          | 1.67 sec                                                    | 1.24 sec: 1.35x faster                                          |
| xml_etree_process    | 44.5 ms                                                     | 36.8 ms: 1.21x faster                                           |
| xml_etree_generate   | 55.5 ms                                                     | 51.4 ms: 1.08x faster                                           |
| xml_etree_parse      | 96.8 ms                                                     | 90.3 ms: 1.07x faster                                           |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.2 ms: 1.06x faster                                           |
| unpickle             | 9.09 us                                                     | 8.73 us: 1.04x faster                                           |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                           |
| unpickle_list        | 2.71 us                                                     | 2.78 us: 1.02x slower                                           |
| pickle_dict          | 17.2 us                                                     | 17.6 us: 1.02x slower                                           |
| pickle_list          | 2.75 us                                                     | 2.85 us: 1.04x slower                                           |
| pickle               | 6.85 us                                                     | 7.27 us: 1.06x slower                                           |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.7 ms: 1.10x slower                                           |
| python_startup_no_site | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                           |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.13 ms: 1.76x faster                                           |
| django_template | 28.9 ms                                                     | 25.4 ms: 1.14x faster                                           |
| genshi_text     | 19.8 ms                                                     | 17.9 ms: 1.10x faster                                           |
| genshi_xml      | 41.0 ms                                                     | 44.2 ms: 1.08x slower                                           |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.98x faster                                            |
| async_tree_none          | 435 ms                                                      | 227 ms: 1.92x faster                                            |
| async_tree_io            | 1.11 sec                                                    | 579 ms: 1.92x faster                                            |
| async_tree_memoization   | 526 ms                                                      | 278 ms: 1.89x faster                                            |
| deltablue                | 4.19 ms                                                     | 2.37 ms: 1.77x faster                                           |
| mako                     | 9.03 ms                                                     | 5.13 ms: 1.76x faster                                           |
| logging_silent           | 94.6 ns                                                     | 55.3 ns: 1.71x faster                                           |
| spectral_norm            | 77.3 ms                                                     | 45.3 ms: 1.70x faster                                           |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 392 ms: 1.63x faster                                            |
| json_dumps               | 9.16 ms                                                     | 5.70 ms: 1.61x faster                                           |
| pyflate                  | 409 ms                                                      | 257 ms: 1.59x faster                                            |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.59x faster                                           |
| chaos                    | 61.7 ms                                                     | 39.2 ms: 1.58x faster                                           |
| richards_super           | 52.2 ms                                                     | 33.5 ms: 1.56x faster                                           |
| raytrace                 | 273 ms                                                      | 176 ms: 1.55x faster                                            |
| pickle_pure_python       | 270 us                                                      | 175 us: 1.54x faster                                            |
| asyncio_tcp              | 732 ms                                                      | 479 ms: 1.53x faster                                            |
| generators               | 32.4 ms                                                     | 21.2 ms: 1.53x faster                                           |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.7 ms: 1.52x faster                                           |
| sqlglot_parse            | 1.22 ms                                                     | 801 us: 1.52x faster                                            |
| crypto_pyaes             | 62.5 ms                                                     | 41.5 ms: 1.51x faster                                           |
| pylint                   | 350 ms                                                      | 235 ms: 1.49x faster                                            |
| go                       | 139 ms                                                      | 93.8 ms: 1.48x faster                                           |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.43 sec: 1.47x faster                                          |
| richards                 | 42.4 ms                                                     | 29.7 ms: 1.43x faster                                           |
| sqlglot_transpile        | 1.48 ms                                                     | 1.04 ms: 1.42x faster                                           |
| unpickle_pure_python     | 183 us                                                      | 130 us: 1.41x faster                                            |
| float                    | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                           |
| deepcopy_memo            | 28.8 us                                                     | 20.9 us: 1.37x faster                                           |
| tomli_loads              | 1.67 sec                                                    | 1.24 sec: 1.35x faster                                          |
| html5lib                 | 51.0 ms                                                     | 37.9 ms: 1.35x faster                                           |
| nbody                    | 71.3 ms                                                     | 53.1 ms: 1.34x faster                                           |
| pprint_pformat           | 1.22 sec                                                    | 946 ms: 1.29x faster                                            |
| pprint_safe_repr         | 592 ms                                                      | 461 ms: 1.29x faster                                            |
| scimark_sor              | 106 ms                                                      | 83.5 ms: 1.27x faster                                           |
| tornado_http             | 108 ms                                                      | 86.1 ms: 1.26x faster                                           |
| dulwich_log              | 50.5 ms                                                     | 40.2 ms: 1.26x faster                                           |
| pycparser                | 930 ms                                                      | 741 ms: 1.26x faster                                            |
| scimark_fft              | 187 ms                                                      | 150 ms: 1.25x faster                                            |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.19 ms: 1.24x faster                                           |
| scimark_lu               | 85.8 ms                                                     | 69.4 ms: 1.24x faster                                           |
| hexiom                   | 5.74 ms                                                     | 4.72 ms: 1.22x faster                                           |
| xml_etree_process        | 44.5 ms                                                     | 36.8 ms: 1.21x faster                                           |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.21x faster                                           |
| bench_thread_pool        | 958 us                                                      | 793 us: 1.21x faster                                            |
| regex_compile            | 106 ms                                                      | 88.9 ms: 1.19x faster                                           |
| fannkuch                 | 256 ms                                                      | 215 ms: 1.19x faster                                            |
| mdp                      | 1.78 sec                                                    | 1.51 sec: 1.18x faster                                          |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                            |
| chameleon                | 5.79 ms                                                     | 5.00 ms: 1.16x faster                                           |
| mypy2                    | 555 ms                                                      | 486 ms: 1.14x faster                                            |
| sympy_sum                | 107 ms                                                      | 93.9 ms: 1.14x faster                                           |
| django_template          | 28.9 ms                                                     | 25.4 ms: 1.14x faster                                           |
| sqlite_synth             | 1.91 us                                                     | 1.69 us: 1.13x faster                                           |
| genshi_text              | 19.8 ms                                                     | 17.9 ms: 1.10x faster                                           |
| json                     | 3.14 ms                                                     | 2.88 ms: 1.09x faster                                           |
| nqueens                  | 66.6 ms                                                     | 61.4 ms: 1.09x faster                                           |
| sympy_integrate          | 15.3 ms                                                     | 14.1 ms: 1.08x faster                                           |
| docutils                 | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                          |
| xml_etree_generate       | 55.5 ms                                                     | 51.4 ms: 1.08x faster                                           |
| sqlglot_optimize         | 39.8 ms                                                     | 37.0 ms: 1.08x faster                                           |
| sympy_str                | 194 ms                                                      | 181 ms: 1.07x faster                                            |
| xml_etree_parse          | 96.8 ms                                                     | 90.3 ms: 1.07x faster                                           |
| 2to3                     | 246 ms                                                      | 229 ms: 1.07x faster                                            |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                           |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.2 ms: 1.06x faster                                           |
| deepcopy                 | 255 us                                                      | 241 us: 1.06x faster                                            |
| meteor_contest           | 75.9 ms                                                     | 72.0 ms: 1.05x faster                                           |
| logging_format           | 6.76 us                                                     | 6.42 us: 1.05x faster                                           |
| logging_simple           | 6.22 us                                                     | 5.91 us: 1.05x faster                                           |
| aiohttp                  | 995 us                                                      | 954 us: 1.04x faster                                            |
| unpickle                 | 9.09 us                                                     | 8.73 us: 1.04x faster                                           |
| deepcopy_reduce          | 2.20 us                                                     | 2.13 us: 1.03x faster                                           |
| flaskblogging            | 2.03 sec                                                    | 2.03 sec: 1.00x slower                                          |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                           |
| sympy_expand             | 314 ms                                                      | 317 ms: 1.01x slower                                            |
| pathlib                  | 75.7 ms                                                     | 76.3 ms: 1.01x slower                                           |
| unpickle_list            | 2.71 us                                                     | 2.78 us: 1.02x slower                                           |
| pickle_dict              | 17.2 us                                                     | 17.6 us: 1.02x slower                                           |
| pickle_list              | 2.75 us                                                     | 2.85 us: 1.04x slower                                           |
| pickle                   | 6.85 us                                                     | 7.27 us: 1.06x slower                                           |
| genshi_xml               | 41.0 ms                                                     | 44.2 ms: 1.08x slower                                           |
| python_startup           | 20.6 ms                                                     | 22.7 ms: 1.10x slower                                           |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                           |
| telco                    | 3.94 ms                                                     | 4.46 ms: 1.13x slower                                           |
| async_generators         | 222 ms                                                      | 252 ms: 1.14x slower                                            |
| create_gc_cycles         | 800 us                                                      | 912 us: 1.14x slower                                            |
| bench_mp_pool            | 62.0 ms                                                     | 72.0 ms: 1.16x slower                                           |
| coverage                 | 39.0 ms                                                     | 45.5 ms: 1.17x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                           |
| thrift                   | 617 us                                                      | 9.21 ms: 14.92x slower                                          |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                    |

Benchmark hidden because not significant (2): regex_v8, pidigits
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown