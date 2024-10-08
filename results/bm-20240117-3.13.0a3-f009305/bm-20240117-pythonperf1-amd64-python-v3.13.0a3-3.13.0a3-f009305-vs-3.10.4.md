# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a3
- machine: windows-amd64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 210 ms: 1.17x faster                                            |
| chameleon      | 5.79 ms                                                     | 4.91 ms: 1.18x faster                                           |
| docutils       | 1.92 sec                                                    | 1.53 sec: 1.25x faster                                          |
| html5lib       | 51.0 ms                                                     | 35.9 ms: 1.42x faster                                           |
| tornado_http   | 108 ms                                                      | 85.5 ms: 1.27x faster                                           |
| Geometric mean | (ref)                                                       | 1.25x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 263 ms: 1.65x faster                                            |
| async_tree_memoization  | 526 ms                                                      | 341 ms: 1.55x faster                                            |
| async_tree_io           | 1.11 sec                                                    | 724 ms: 1.53x faster                                            |
| async_tree_cpu_io_mixed | 638 ms                                                      | 448 ms: 1.42x faster                                            |
| Geometric mean          | (ref)                                                       | 1.54x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 52.5 ms: 1.18x faster                                           |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                            |
| nbody          | 71.3 ms                                                     | 74.1 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                       | 1.05x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.7 ms: 1.36x faster                                           |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                            |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                           |
| regex_v8       | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                       | 1.13x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.54 ms: 1.65x faster                                           |
| pickle_pure_python   | 270 us                                                      | 179 us: 1.51x faster                                            |
| unpickle_pure_python | 183 us                                                      | 128 us: 1.43x faster                                            |
| xml_etree_process    | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                           |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                          |
| unpickle             | 9.09 us                                                     | 8.42 us: 1.08x faster                                           |
| xml_etree_parse      | 96.8 ms                                                     | 93.0 ms: 1.04x faster                                           |
| xml_etree_generate   | 55.5 ms                                                     | 53.6 ms: 1.04x faster                                           |
| json_loads           | 14.0 us                                                     | 13.7 us: 1.03x faster                                           |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                           |
| pickle_list          | 2.75 us                                                     | 2.89 us: 1.05x slower                                           |
| pickle_dict          | 17.2 us                                                     | 18.2 us: 1.06x slower                                           |
| pickle               | 6.85 us                                                     | 7.31 us: 1.07x slower                                           |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.1 ms: 1.03x faster                                           |
| python_startup_no_site | 15.5 ms                                                     | 17.9 ms: 1.16x slower                                           |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.57 ms: 1.37x faster                                           |
| django_template | 28.9 ms                                                     | 21.4 ms: 1.35x faster                                           |
| genshi_text     | 19.8 ms                                                     | 16.1 ms: 1.23x faster                                           |
| genshi_xml      | 41.0 ms                                                     | 36.0 ms: 1.14x faster                                           |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 70.5 us: 4.77x faster                                           |
| deltablue                | 4.19 ms                                                     | 1.97 ms: 2.12x faster                                           |
| logging_silent           | 94.6 ns                                                     | 54.1 ns: 1.75x faster                                           |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                            |
| raytrace                 | 273 ms                                                      | 161 ms: 1.70x faster                                            |
| richards_super           | 52.2 ms                                                     | 30.8 ms: 1.69x faster                                           |
| json_dumps               | 9.16 ms                                                     | 5.54 ms: 1.65x faster                                           |
| async_tree_none          | 435 ms                                                      | 263 ms: 1.65x faster                                            |
| go                       | 139 ms                                                      | 84.9 ms: 1.64x faster                                           |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.61x faster                                           |
| sqlglot_parse            | 1.22 ms                                                     | 761 us: 1.60x faster                                            |
| asyncio_tcp              | 732 ms                                                      | 462 ms: 1.58x faster                                            |
| scimark_lu               | 85.8 ms                                                     | 54.9 ms: 1.56x faster                                           |
| chaos                    | 61.7 ms                                                     | 39.5 ms: 1.56x faster                                           |
| richards                 | 42.4 ms                                                     | 27.4 ms: 1.55x faster                                           |
| async_tree_memoization   | 526 ms                                                      | 341 ms: 1.55x faster                                            |
| async_tree_io            | 1.11 sec                                                    | 724 ms: 1.53x faster                                            |
| pickle_pure_python       | 270 us                                                      | 179 us: 1.51x faster                                            |
| hexiom                   | 5.74 ms                                                     | 3.82 ms: 1.50x faster                                           |
| sqlglot_transpile        | 1.48 ms                                                     | 981 us: 1.50x faster                                            |
| crypto_pyaes             | 62.5 ms                                                     | 42.8 ms: 1.46x faster                                           |
| generators               | 32.4 ms                                                     | 22.1 ms: 1.46x faster                                           |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.9 ms: 1.44x faster                                           |
| unpickle_pure_python     | 183 us                                                      | 128 us: 1.43x faster                                            |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 448 ms: 1.42x faster                                            |
| html5lib                 | 51.0 ms                                                     | 35.9 ms: 1.42x faster                                           |
| pyflate                  | 409 ms                                                      | 288 ms: 1.42x faster                                            |
| mako                     | 9.03 ms                                                     | 6.57 ms: 1.37x faster                                           |
| regex_compile            | 106 ms                                                      | 77.7 ms: 1.36x faster                                           |
| scimark_sor              | 106 ms                                                      | 78.0 ms: 1.36x faster                                           |
| mypy2                    | 555 ms                                                      | 409 ms: 1.36x faster                                            |
| django_template          | 28.9 ms                                                     | 21.4 ms: 1.35x faster                                           |
| pycparser                | 930 ms                                                      | 701 ms: 1.33x faster                                            |
| deepcopy_memo            | 28.8 us                                                     | 22.2 us: 1.30x faster                                           |
| sympy_sum                | 107 ms                                                      | 82.6 ms: 1.29x faster                                           |
| mdp                      | 1.78 sec                                                    | 1.40 sec: 1.27x faster                                          |
| tornado_http             | 108 ms                                                      | 85.5 ms: 1.27x faster                                           |
| spectral_norm            | 77.3 ms                                                     | 61.6 ms: 1.25x faster                                           |
| docutils                 | 1.92 sec                                                    | 1.53 sec: 1.25x faster                                          |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.25x faster                                           |
| sympy_str                | 194 ms                                                      | 156 ms: 1.25x faster                                            |
| genshi_text              | 19.8 ms                                                     | 16.1 ms: 1.23x faster                                           |
| coroutines               | 16.0 ms                                                     | 13.0 ms: 1.23x faster                                           |
| dulwich_log              | 50.5 ms                                                     | 41.1 ms: 1.23x faster                                           |
| xml_etree_process        | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                           |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                           |
| pprint_pformat           | 1.22 sec                                                    | 1.00 sec: 1.21x faster                                          |
| sqlglot_optimize         | 39.8 ms                                                     | 33.0 ms: 1.21x faster                                           |
| pprint_safe_repr         | 592 ms                                                      | 491 ms: 1.21x faster                                            |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                          |
| chameleon                | 5.79 ms                                                     | 4.91 ms: 1.18x faster                                           |
| float                    | 61.7 ms                                                     | 52.5 ms: 1.18x faster                                           |
| sympy_expand             | 314 ms                                                      | 268 ms: 1.17x faster                                            |
| sqlglot_normalize        | 205 ms                                                      | 175 ms: 1.17x faster                                            |
| 2to3                     | 246 ms                                                      | 210 ms: 1.17x faster                                            |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.83 sec: 1.15x faster                                          |
| deepcopy                 | 255 us                                                      | 223 us: 1.15x faster                                            |
| deepcopy_reduce          | 2.20 us                                                     | 1.93 us: 1.14x faster                                           |
| bench_thread_pool        | 958 us                                                      | 839 us: 1.14x faster                                            |
| genshi_xml               | 41.0 ms                                                     | 36.0 ms: 1.14x faster                                           |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                            |
| nqueens                  | 66.6 ms                                                     | 59.3 ms: 1.12x faster                                           |
| aiohttp                  | 995 us                                                      | 896 us: 1.11x faster                                            |
| create_gc_cycles         | 800 us                                                      | 732 us: 1.09x faster                                            |
| json                     | 3.14 ms                                                     | 2.88 ms: 1.09x faster                                           |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.52 ms: 1.08x faster                                           |
| unpickle                 | 9.09 us                                                     | 8.42 us: 1.08x faster                                           |
| meteor_contest           | 75.9 ms                                                     | 71.9 ms: 1.06x faster                                           |
| scimark_fft              | 187 ms                                                      | 178 ms: 1.05x faster                                            |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                           |
| logging_format           | 6.76 us                                                     | 6.47 us: 1.04x faster                                           |
| fannkuch                 | 256 ms                                                      | 245 ms: 1.04x faster                                            |
| xml_etree_parse          | 96.8 ms                                                     | 93.0 ms: 1.04x faster                                           |
| xml_etree_generate       | 55.5 ms                                                     | 53.6 ms: 1.04x faster                                           |
| logging_simple           | 6.22 us                                                     | 6.04 us: 1.03x faster                                           |
| json_loads               | 14.0 us                                                     | 13.7 us: 1.03x faster                                           |
| python_startup           | 20.6 ms                                                     | 20.1 ms: 1.03x faster                                           |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                           |
| regex_v8                 | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                           |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                            |
| async_generators         | 222 ms                                                      | 227 ms: 1.02x slower                                            |
| nbody                    | 71.3 ms                                                     | 74.1 ms: 1.04x slower                                           |
| pathlib                  | 75.7 ms                                                     | 79.3 ms: 1.05x slower                                           |
| pickle_list              | 2.75 us                                                     | 2.89 us: 1.05x slower                                           |
| pickle_dict              | 17.2 us                                                     | 18.2 us: 1.06x slower                                           |
| pickle                   | 6.85 us                                                     | 7.31 us: 1.07x slower                                           |
| bench_mp_pool            | 62.0 ms                                                     | 66.6 ms: 1.07x slower                                           |
| gc_traversal             | 1.41 ms                                                     | 1.52 ms: 1.08x slower                                           |
| coverage                 | 39.0 ms                                                     | 44.3 ms: 1.14x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 17.9 ms: 1.16x slower                                           |
| telco                    | 3.94 ms                                                     | 4.77 ms: 1.21x slower                                           |
| thrift                   | 617 us                                                      | 8.32 ms: 13.47x slower                                          |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                    |

Benchmark hidden because not significant (2): flaskblogging, unpickle_list
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown