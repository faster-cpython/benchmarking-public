# Results vs. 3.10.4

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-amd64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 208 ms: 1.18x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.71 ms: 1.23x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                      |
| html5lib       | 51.0 ms                                                     | 35.2 ms: 1.45x faster                                                       |
| tornado_http   | 108 ms                                                      | 81.6 ms: 1.33x faster                                                       |
| Geometric mean | (ref)                                                       | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 216 ms: 2.01x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 265 ms: 1.99x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 588 ms: 1.89x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 390 ms: 1.64x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 48.2 ms: 1.28x faster                                                       |
| nbody          | 71.3 ms                                                     | 66.2 ms: 1.08x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 76.9 ms: 1.38x faster                                                       |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.57 ms: 1.64x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 173 us: 1.56x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 120 us: 1.53x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.35 sec: 1.24x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.45 us: 1.08x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 91.3 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 52.9 ms: 1.05x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.62 us: 1.03x faster                                                       |
| pickle               | 6.85 us                                                     | 7.18 us: 1.05x slower                                                       |
| pickle_list          | 2.75 us                                                     | 2.94 us: 1.07x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 19.4 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.2 ms: 1.02x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.28 ms: 1.44x faster                                                       |
| django_template | 28.9 ms                                                     | 21.1 ms: 1.37x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 14.5 ms: 1.37x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 31.7 ms: 1.30x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.37x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 100 us: 3.36x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.90 ms: 2.21x faster                                                       |
| async_tree_none          | 435 ms                                                      | 216 ms: 2.01x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 265 ms: 1.99x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 588 ms: 1.89x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 52.8 ns: 1.79x faster                                                       |
| richards_super           | 52.2 ms                                                     | 29.3 ms: 1.78x faster                                                       |
| pylint                   | 350 ms                                                      | 206 ms: 1.70x faster                                                        |
| raytrace                 | 273 ms                                                      | 161 ms: 1.70x faster                                                        |
| generators               | 32.4 ms                                                     | 19.3 ms: 1.67x faster                                                       |
| go                       | 139 ms                                                      | 83.5 ms: 1.66x faster                                                       |
| richards                 | 42.4 ms                                                     | 25.8 ms: 1.65x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.57 ms: 1.64x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.1 us: 1.64x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 390 ms: 1.64x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 749 us: 1.62x faster                                                        |
| chaos                    | 61.7 ms                                                     | 38.2 ms: 1.61x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 53.7 ms: 1.60x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.64 ms: 1.58x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 173 us: 1.56x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 954 us: 1.55x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 120 us: 1.53x faster                                                        |
| pyflate                  | 409 ms                                                      | 276 ms: 1.48x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.1 ms: 1.46x faster                                                       |
| scimark_sor              | 106 ms                                                      | 73.1 ms: 1.45x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 35.2 ms: 1.45x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.28 ms: 1.44x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 44.9 ms: 1.39x faster                                                       |
| regex_compile            | 106 ms                                                      | 76.9 ms: 1.38x faster                                                       |
| django_template          | 28.9 ms                                                     | 21.1 ms: 1.37x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 14.5 ms: 1.37x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.55 sec: 1.36x faster                                                      |
| pycparser                | 930 ms                                                      | 697 ms: 1.34x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.33 sec: 1.33x faster                                                      |
| mypy2                    | 555 ms                                                      | 417 ms: 1.33x faster                                                        |
| tornado_http             | 108 ms                                                      | 81.6 ms: 1.33x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.7 us: 1.32x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 31.7 ms: 1.30x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 566 ms: 1.29x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 39.1 ms: 1.29x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 60.1 ms: 1.28x faster                                                       |
| float                    | 61.7 ms                                                     | 48.2 ms: 1.28x faster                                                       |
| sympy_sum                | 107 ms                                                      | 83.8 ms: 1.28x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 959 ms: 1.27x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 467 ms: 1.27x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 12.1 ms: 1.26x faster                                                       |
| coroutines               | 16.0 ms                                                     | 12.7 ms: 1.26x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.35 sec: 1.24x faster                                                      |
| sympy_str                | 194 ms                                                      | 158 ms: 1.23x faster                                                        |
| chameleon                | 5.79 ms                                                     | 4.71 ms: 1.23x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 32.6 ms: 1.22x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 170 ms: 1.21x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 55.5 ms: 1.20x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 808 us: 1.19x faster                                                        |
| 2to3                     | 246 ms                                                      | 208 ms: 1.18x faster                                                        |
| sympy_expand             | 314 ms                                                      | 267 ms: 1.18x faster                                                        |
| deepcopy                 | 255 us                                                      | 218 us: 1.17x faster                                                        |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.39 ms: 1.14x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.97 us: 1.12x faster                                                       |
| aiohttp                  | 995 us                                                      | 894 us: 1.11x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.12 us: 1.10x faster                                                       |
| scimark_fft              | 187 ms                                                      | 172 ms: 1.09x faster                                                        |
| logging_simple           | 6.22 us                                                     | 5.73 us: 1.09x faster                                                       |
| nbody                    | 71.3 ms                                                     | 66.2 ms: 1.08x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.45 us: 1.08x faster                                                       |
| fannkuch                 | 256 ms                                                      | 238 ms: 1.07x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 71.0 ms: 1.07x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 91.3 ms: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 52.9 ms: 1.05x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.62 us: 1.03x faster                                                       |
| python_startup           | 20.6 ms                                                     | 20.2 ms: 1.02x faster                                                       |
| flaskblogging            | 2.03 sec                                                    | 2.03 sec: 1.00x slower                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.00x slower                                                        |
| async_generators         | 222 ms                                                      | 226 ms: 1.02x slower                                                        |
| pathlib                  | 75.7 ms                                                     | 79.3 ms: 1.05x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.18 us: 1.05x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 66.2 ms: 1.07x slower                                                       |
| pickle_list              | 2.75 us                                                     | 2.94 us: 1.07x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                       |
| coverage                 | 39.0 ms                                                     | 43.5 ms: 1.11x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 19.4 us: 1.13x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 903 us: 1.13x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.59 ms: 1.16x slower                                                       |
| thrift                   | 617 us                                                      | 8.07 ms: 13.08x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                |

Benchmark hidden because not significant (3): json_loads, json, regex_v8
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown