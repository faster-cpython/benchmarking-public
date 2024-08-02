# Results vs. 3.10.4

- fork: python
- ref: a19bb261a327e1008f21
- machine: windows-amd64
- commit hash: a19bb26
- commit date: 2024-06-15
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 207 ms: 1.19x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.71 ms: 1.23x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                      |
| html5lib       | 51.0 ms                                                     | 35.5 ms: 1.44x faster                                                       |
| tornado_http   | 108 ms                                                      | 82.1 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                       | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 217 ms: 2.00x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 263 ms: 2.00x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 584 ms: 1.90x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 385 ms: 1.66x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.88x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 50.9 ms: 1.21x faster                                                       |
| nbody          | 71.3 ms                                                     | 69.4 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.0 ms: 1.38x faster                                                       |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.51 ms: 1.66x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 176 us: 1.53x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 124 us: 1.48x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 36.8 ms: 1.21x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 91.3 ms: 1.06x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 53.5 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.79 us: 1.03x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.66 us: 1.02x faster                                                       |
| pickle               | 6.85 us                                                     | 7.27 us: 1.06x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.02 us: 1.10x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 19.2 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.2 ms: 1.02x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.1 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.39 ms: 1.41x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 14.8 ms: 1.34x faster                                                       |
| django_template | 28.9 ms                                                     | 21.9 ms: 1.32x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 31.1 ms: 1.32x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.35x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.22x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.89 ms: 2.21x faster                                                       |
| async_tree_none          | 435 ms                                                      | 217 ms: 2.00x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 263 ms: 2.00x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 584 ms: 1.90x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 53.0 ns: 1.79x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.1 ms: 1.74x faster                                                       |
| raytrace                 | 273 ms                                                      | 159 ms: 1.71x faster                                                        |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                                        |
| go                       | 139 ms                                                      | 82.5 ms: 1.68x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.51 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 385 ms: 1.66x faster                                                        |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.62x faster                                                       |
| chaos                    | 61.7 ms                                                     | 38.2 ms: 1.62x faster                                                       |
| generators               | 32.4 ms                                                     | 20.1 ms: 1.61x faster                                                       |
| richards                 | 42.4 ms                                                     | 26.6 ms: 1.59x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 765 us: 1.59x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 54.0 ms: 1.59x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.70 ms: 1.55x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 474 ms: 1.54x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 176 us: 1.53x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 975 us: 1.51x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 124 us: 1.48x faster                                                        |
| pyflate                  | 409 ms                                                      | 281 ms: 1.46x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 35.5 ms: 1.44x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.39 ms: 1.41x faster                                                       |
| scimark_sor              | 106 ms                                                      | 75.5 ms: 1.41x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 44.8 ms: 1.40x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.6 ms: 1.38x faster                                                       |
| regex_compile            | 106 ms                                                      | 77.0 ms: 1.38x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.54 sec: 1.37x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 14.8 ms: 1.34x faster                                                       |
| django_template          | 28.9 ms                                                     | 21.9 ms: 1.32x faster                                                       |
| tornado_http             | 108 ms                                                      | 82.1 ms: 1.32x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 31.1 ms: 1.32x faster                                                       |
| mypy2                    | 555 ms                                                      | 423 ms: 1.31x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 38.9 ms: 1.30x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.39 sec: 1.28x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 22.6 us: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 734 ms: 1.27x faster                                                        |
| sympy_sum                | 107 ms                                                      | 84.9 ms: 1.26x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 763 us: 1.26x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 62.0 ms: 1.25x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 980 ms: 1.24x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 476 ms: 1.24x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                       |
| chameleon                | 5.79 ms                                                     | 4.71 ms: 1.23x faster                                                       |
| float                    | 61.7 ms                                                     | 50.9 ms: 1.21x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.8 ms: 1.21x faster                                                       |
| sympy_str                | 194 ms                                                      | 162 ms: 1.20x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.20x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 33.3 ms: 1.20x faster                                                       |
| 2to3                     | 246 ms                                                      | 207 ms: 1.19x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 57.0 ms: 1.17x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 176 ms: 1.17x faster                                                        |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                        |
| deepcopy                 | 255 us                                                      | 223 us: 1.14x faster                                                        |
| sympy_expand             | 314 ms                                                      | 275 ms: 1.14x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.46 ms: 1.11x faster                                                       |
| aiohttp                  | 995 us                                                      | 899 us: 1.11x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.20 us: 1.09x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.05 us: 1.08x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.79 us: 1.07x faster                                                       |
| scimark_fft              | 187 ms                                                      | 175 ms: 1.07x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 91.3 ms: 1.06x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 71.6 ms: 1.06x faster                                                       |
| fannkuch                 | 256 ms                                                      | 241 ms: 1.06x faster                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 53.5 ms: 1.04x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.79 us: 1.03x faster                                                       |
| nbody                    | 71.3 ms                                                     | 69.4 ms: 1.03x faster                                                       |
| python_startup           | 20.6 ms                                                     | 20.2 ms: 1.02x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.66 us: 1.02x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 75.1 ms: 1.01x faster                                                       |
| flaskblogging            | 2.03 sec                                                    | 2.03 sec: 1.00x slower                                                      |
| async_generators         | 222 ms                                                      | 223 ms: 1.01x slower                                                        |
| bench_mp_pool            | 62.0 ms                                                     | 64.5 ms: 1.04x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.1 ms: 1.04x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.27 us: 1.06x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.02 us: 1.10x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 19.2 us: 1.12x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 913 us: 1.14x slower                                                        |
| coverage                 | 39.0 ms                                                     | 45.4 ms: 1.16x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.76 ms: 1.21x slower                                                       |
| thrift                   | 617 us                                                      | 7.96 ms: 12.89x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                                |

Benchmark hidden because not significant (4): json, json_loads, pidigits, regex_v8
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240615-3.13.0b2+-a19bb26/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown