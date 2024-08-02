# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a3
- machine: linux-aarch64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 305 ms: 1.25x faster                                         |
| chameleon      | 10.8 ms                                                               | 8.98 ms: 1.21x faster                                        |
| docutils       | 3.53 sec                                                              | 2.90 sec: 1.22x faster                                       |
| html5lib       | 86.5 ms                                                               | 66.2 ms: 1.31x faster                                        |
| tornado_http   | 178 ms                                                                | 137 ms: 1.30x faster                                         |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 582 ms: 1.63x faster                                         |
| async_tree_io           | 2.28 sec                                                              | 1.45 sec: 1.58x faster                                       |
| async_tree_memoization  | 1.13 sec                                                              | 745 ms: 1.52x faster                                         |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 888 ms: 1.43x faster                                         |
| Geometric mean          | (ref)                                                                 | 1.54x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 104 ms: 1.60x faster                                         |
| float          | 135 ms                                                                | 91.0 ms: 1.48x faster                                        |
| pidigits       | 235 ms                                                                | 233 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                                 | 1.34x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                         |
| regex_v8       | 32.2 ms                                                               | 30.1 ms: 1.07x faster                                        |
| regex_dna      | 257 ms                                                                | 255 ms: 1.01x faster                                         |
| regex_effbot   | 4.25 ms                                                               | 4.65 ms: 1.09x slower                                        |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 347 us: 1.52x faster                                         |
| unpickle_pure_python | 366 us                                                                | 256 us: 1.43x faster                                         |
| json_dumps           | 16.7 ms                                                               | 12.5 ms: 1.34x faster                                        |
| tomli_loads          | 3.36 sec                                                              | 2.59 sec: 1.30x faster                                       |
| xml_etree_process    | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                        |
| unpickle_list        | 6.99 us                                                               | 6.45 us: 1.08x faster                                        |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                         |
| xml_etree_parse      | 212 ms                                                                | 206 ms: 1.03x faster                                         |
| xml_etree_iterparse  | 156 ms                                                                | 152 ms: 1.03x faster                                         |
| json_loads           | 30.9 us                                                               | 31.1 us: 1.00x slower                                        |
| pickle_list          | 5.24 us                                                               | 5.28 us: 1.01x slower                                        |
| pickle_dict          | 35.1 us                                                               | 37.3 us: 1.06x slower                                        |
| pickle               | 12.5 us                                                               | 13.4 us: 1.07x slower                                        |
| unpickle             | 17.5 us                                                               | 19.6 us: 1.12x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.1 ms: 1.08x slower                                        |
| python_startup_no_site | 6.89 ms                                                               | 10.3 ms: 1.50x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.27x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.9 ms: 1.47x faster                                        |
| django_template | 53.3 ms                                                               | 40.7 ms: 1.31x faster                                        |
| genshi_text     | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                        |
| genshi_xml      | 69.8 ms                                                               | 60.8 ms: 1.15x faster                                        |
| Geometric mean  | (ref)                                                                 | 1.30x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 135 us: 4.91x faster                                         |
| deltablue                | 8.94 ms                                                               | 3.98 ms: 2.25x faster                                        |
| bench_mp_pool            | 14.5 ms                                                               | 6.98 ms: 2.08x faster                                        |
| raytrace                 | 573 ms                                                                | 296 ms: 1.94x faster                                         |
| generators               | 68.1 ms                                                               | 36.0 ms: 1.89x faster                                        |
| chaos                    | 121 ms                                                                | 66.7 ms: 1.82x faster                                        |
| richards_super           | 107 ms                                                                | 60.9 ms: 1.76x faster                                        |
| sqlglot_parse            | 2.40 ms                                                               | 1.36 ms: 1.76x faster                                        |
| crypto_pyaes             | 134 ms                                                                | 77.3 ms: 1.73x faster                                        |
| asyncio_tcp              | 944 ms                                                                | 562 ms: 1.68x faster                                         |
| comprehensions           | 33.1 us                                                               | 19.8 us: 1.68x faster                                        |
| richards                 | 91.7 ms                                                               | 55.0 ms: 1.67x faster                                        |
| scimark_lu               | 227 ms                                                                | 137 ms: 1.66x faster                                         |
| sqlglot_transpile        | 2.84 ms                                                               | 1.72 ms: 1.66x faster                                        |
| logging_silent           | 222 ns                                                                | 134 ns: 1.65x faster                                         |
| go                       | 264 ms                                                                | 161 ms: 1.64x faster                                         |
| async_tree_none          | 950 ms                                                                | 582 ms: 1.63x faster                                         |
| nbody                    | 166 ms                                                                | 104 ms: 1.60x faster                                         |
| async_tree_io            | 2.28 sec                                                              | 1.45 sec: 1.58x faster                                       |
| scimark_monte_carlo      | 128 ms                                                                | 83.5 ms: 1.53x faster                                        |
| hexiom                   | 10.9 ms                                                               | 7.14 ms: 1.53x faster                                        |
| pickle_pure_python       | 529 us                                                                | 347 us: 1.52x faster                                         |
| async_tree_memoization   | 1.13 sec                                                              | 745 ms: 1.52x faster                                         |
| scimark_sor              | 246 ms                                                                | 163 ms: 1.51x faster                                         |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.22 sec: 1.48x faster                                       |
| float                    | 135 ms                                                                | 91.0 ms: 1.48x faster                                        |
| mako                     | 18.9 ms                                                               | 12.9 ms: 1.47x faster                                        |
| pylint                   | 485 ms                                                                | 333 ms: 1.46x faster                                         |
| spectral_norm            | 186 ms                                                                | 129 ms: 1.45x faster                                         |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 888 ms: 1.43x faster                                         |
| unpickle_pure_python     | 366 us                                                                | 256 us: 1.43x faster                                         |
| pyflate                  | 795 ms                                                                | 562 ms: 1.42x faster                                         |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                         |
| thrift                   | 1.26 ms                                                               | 925 us: 1.36x faster                                         |
| logging_simple           | 9.78 us                                                               | 7.26 us: 1.35x faster                                        |
| json_dumps               | 16.7 ms                                                               | 12.5 ms: 1.34x faster                                        |
| pycparser                | 1.69 sec                                                              | 1.27 sec: 1.33x faster                                       |
| logging_format           | 10.6 us                                                               | 8.00 us: 1.33x faster                                        |
| sympy_sum                | 184 ms                                                                | 139 ms: 1.32x faster                                         |
| django_template          | 53.3 ms                                                               | 40.7 ms: 1.31x faster                                        |
| html5lib                 | 86.5 ms                                                               | 66.2 ms: 1.31x faster                                        |
| tornado_http             | 178 ms                                                                | 137 ms: 1.30x faster                                         |
| sympy_integrate          | 26.5 ms                                                               | 20.5 ms: 1.30x faster                                        |
| tomli_loads              | 3.36 sec                                                              | 2.59 sec: 1.30x faster                                       |
| genshi_text              | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                        |
| sqlglot_normalize        | 156 ms                                                                | 123 ms: 1.27x faster                                         |
| sympy_str                | 329 ms                                                                | 259 ms: 1.27x faster                                         |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.27x faster                                        |
| deepcopy_memo            | 61.7 us                                                               | 49.3 us: 1.25x faster                                        |
| 2to3                     | 381 ms                                                                | 305 ms: 1.25x faster                                         |
| sqlglot_optimize         | 75.4 ms                                                               | 60.7 ms: 1.24x faster                                        |
| xml_etree_process        | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                        |
| pprint_pformat           | 2.36 sec                                                              | 1.91 sec: 1.23x faster                                       |
| pprint_safe_repr         | 1.15 sec                                                              | 936 ms: 1.23x faster                                         |
| nqueens                  | 117 ms                                                                | 96.4 ms: 1.22x faster                                        |
| bench_thread_pool        | 1.59 ms                                                               | 1.31 ms: 1.22x faster                                        |
| docutils                 | 3.53 sec                                                              | 2.90 sec: 1.22x faster                                       |
| gunicorn                 | 1.45 ms                                                               | 1.19 ms: 1.21x faster                                        |
| sympy_expand             | 543 ms                                                                | 448 ms: 1.21x faster                                         |
| chameleon                | 10.8 ms                                                               | 8.98 ms: 1.21x faster                                        |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.34 ms: 1.20x faster                                        |
| dulwich_log              | 73.5 ms                                                               | 61.3 ms: 1.20x faster                                        |
| fannkuch                 | 546 ms                                                                | 456 ms: 1.20x faster                                         |
| aiohttp                  | 1.39 ms                                                               | 1.16 ms: 1.19x faster                                        |
| create_gc_cycles         | 2.26 ms                                                               | 1.91 ms: 1.18x faster                                        |
| scimark_fft              | 500 ms                                                                | 430 ms: 1.16x faster                                         |
| deepcopy                 | 511 us                                                                | 444 us: 1.15x faster                                         |
| genshi_xml               | 69.8 ms                                                               | 60.8 ms: 1.15x faster                                        |
| deepcopy_reduce          | 4.60 us                                                               | 4.04 us: 1.14x faster                                        |
| mdp                      | 3.70 sec                                                              | 3.32 sec: 1.11x faster                                       |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.11x faster                                         |
| sqlite_synth             | 4.12 us                                                               | 3.75 us: 1.10x faster                                        |
| pathlib                  | 26.3 ms                                                               | 24.1 ms: 1.09x faster                                        |
| unpickle_list            | 6.99 us                                                               | 6.45 us: 1.08x faster                                        |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                         |
| regex_v8                 | 32.2 ms                                                               | 30.1 ms: 1.07x faster                                        |
| flaskblogging            | 4.83 ms                                                               | 4.56 ms: 1.06x faster                                        |
| json                     | 5.88 ms                                                               | 5.59 ms: 1.05x faster                                        |
| xml_etree_parse          | 212 ms                                                                | 206 ms: 1.03x faster                                         |
| xml_etree_iterparse      | 156 ms                                                                | 152 ms: 1.03x faster                                         |
| pidigits                 | 235 ms                                                                | 233 ms: 1.01x faster                                         |
| regex_dna                | 257 ms                                                                | 255 ms: 1.01x faster                                         |
| json_loads               | 30.9 us                                                               | 31.1 us: 1.00x slower                                        |
| pickle_list              | 5.24 us                                                               | 5.28 us: 1.01x slower                                        |
| gc_traversal             | 4.15 ms                                                               | 4.36 ms: 1.05x slower                                        |
| async_generators         | 452 ms                                                                | 480 ms: 1.06x slower                                         |
| pickle_dict              | 35.1 us                                                               | 37.3 us: 1.06x slower                                        |
| pickle                   | 12.5 us                                                               | 13.4 us: 1.07x slower                                        |
| python_startup           | 11.2 ms                                                               | 12.1 ms: 1.08x slower                                        |
| regex_effbot             | 4.25 ms                                                               | 4.65 ms: 1.09x slower                                        |
| unpickle                 | 17.5 us                                                               | 19.6 us: 1.12x slower                                        |
| telco                    | 8.49 ms                                                               | 9.69 ms: 1.14x slower                                        |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                         |
| python_startup_no_site   | 6.89 ms                                                               | 10.3 ms: 1.50x slower                                        |
| Geometric mean           | (ref)                                                                 | 1.29x faster                                                 |

Benchmark hidden because not significant (2): mypy2, asyncio_websockets
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.08x