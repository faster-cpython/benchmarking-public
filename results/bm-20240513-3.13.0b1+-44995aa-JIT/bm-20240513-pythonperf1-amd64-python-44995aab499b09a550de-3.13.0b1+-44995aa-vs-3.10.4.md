# Results vs. 3.10.4

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-amd64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 234 ms: 1.05x faster                                                        |
| chameleon      | 5.79 ms                                                     | 5.07 ms: 1.14x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.79 sec: 1.07x faster                                                      |
| html5lib       | 51.0 ms                                                     | 37.0 ms: 1.38x faster                                                       |
| tornado_http   | 108 ms                                                      | 85.9 ms: 1.26x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 226 ms: 1.93x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 278 ms: 1.89x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 600 ms: 1.85x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 399 ms: 1.60x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.81x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                                       |
| nbody          | 71.3 ms                                                     | 51.5 ms: 1.38x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 88.6 ms: 1.20x faster                                                       |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.70 ms: 1.61x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 174 us: 1.55x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 126 us: 1.45x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.0 ms: 1.08x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 51.6 ms: 1.08x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.3 ms: 1.07x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.60 us: 1.06x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 17.6 us: 1.02x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.82 us: 1.04x slower                                                       |
| pickle               | 6.85 us                                                     | 7.17 us: 1.05x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.05 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 18.2 ms: 1.18x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 4.93 ms: 1.83x faster                                                       |
| django_template | 28.9 ms                                                     | 25.8 ms: 1.12x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 45.6 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 2.99x faster                                                        |
| async_tree_none          | 435 ms                                                      | 226 ms: 1.93x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 278 ms: 1.89x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 600 ms: 1.85x faster                                                        |
| mako                     | 9.03 ms                                                     | 4.93 ms: 1.83x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.37 ms: 1.77x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 44.1 ms: 1.75x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.9 ns: 1.69x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.61x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.70 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 399 ms: 1.60x faster                                                        |
| pyflate                  | 409 ms                                                      | 257 ms: 1.59x faster                                                        |
| richards_super           | 52.2 ms                                                     | 33.0 ms: 1.58x faster                                                       |
| chaos                    | 61.7 ms                                                     | 39.2 ms: 1.58x faster                                                       |
| raytrace                 | 273 ms                                                      | 175 ms: 1.56x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 174 us: 1.55x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 41.0 ms: 1.53x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 800 us: 1.52x faster                                                        |
| generators               | 32.4 ms                                                     | 21.6 ms: 1.50x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.2 ms: 1.50x faster                                                       |
| go                       | 139 ms                                                      | 93.6 ms: 1.48x faster                                                       |
| pylint                   | 350 ms                                                      | 238 ms: 1.47x faster                                                        |
| richards                 | 42.4 ms                                                     | 29.1 ms: 1.46x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 126 us: 1.45x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.03 ms: 1.43x faster                                                       |
| float                    | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 20.6 us: 1.40x faster                                                       |
| nbody                    | 71.3 ms                                                     | 51.5 ms: 1.38x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 37.0 ms: 1.38x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.58 sec: 1.34x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 446 ms: 1.33x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 924 ms: 1.32x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.10 ms: 1.30x faster                                                       |
| scimark_sor              | 106 ms                                                      | 82.2 ms: 1.29x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 572 ms: 1.28x faster                                                        |
| tornado_http             | 108 ms                                                      | 85.9 ms: 1.26x faster                                                       |
| scimark_fft              | 187 ms                                                      | 150 ms: 1.25x faster                                                        |
| pycparser                | 930 ms                                                      | 756 ms: 1.23x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.67 ms: 1.23x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.46 sec: 1.22x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.21x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.1 ms: 1.20x faster                                                       |
| regex_compile            | 106 ms                                                      | 88.6 ms: 1.20x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 72.2 ms: 1.19x faster                                                       |
| fannkuch                 | 256 ms                                                      | 216 ms: 1.19x faster                                                        |
| sympy_sum                | 107 ms                                                      | 93.1 ms: 1.15x faster                                                       |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                        |
| chameleon                | 5.79 ms                                                     | 5.07 ms: 1.14x faster                                                       |
| mypy2                    | 555 ms                                                      | 488 ms: 1.14x faster                                                        |
| django_template          | 28.9 ms                                                     | 25.8 ms: 1.12x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 14.0 ms: 1.09x faster                                                       |
| sympy_str                | 194 ms                                                      | 179 ms: 1.09x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 61.4 ms: 1.08x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.7 ms: 1.08x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.0 ms: 1.08x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 51.6 ms: 1.08x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.79 sec: 1.07x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.29 us: 1.07x faster                                                       |
| deepcopy                 | 255 us                                                      | 238 us: 1.07x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 90.3 ms: 1.07x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.87 us: 1.06x faster                                                       |
| aiohttp                  | 995 us                                                      | 940 us: 1.06x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.60 us: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| 2to3                     | 246 ms                                                      | 234 ms: 1.05x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 72.8 ms: 1.04x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.14 us: 1.03x faster                                                       |
| sympy_expand             | 314 ms                                                      | 311 ms: 1.01x faster                                                        |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 17.6 us: 1.02x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.82 us: 1.04x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.17 us: 1.05x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 80.2 ms: 1.06x slower                                                       |
| python_startup           | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.05 us: 1.11x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 45.6 ms: 1.11x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.11x slower                                                       |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                        |
| coverage                 | 39.0 ms                                                     | 44.5 ms: 1.14x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 920 us: 1.15x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.55 ms: 1.15x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.2 ms: 1.18x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 73.9 ms: 1.19x slower                                                       |
| thrift                   | 617 us                                                      | 9.28 ms: 15.03x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (4): json, bench_thread_pool, flaskblogging, regex_v8
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown