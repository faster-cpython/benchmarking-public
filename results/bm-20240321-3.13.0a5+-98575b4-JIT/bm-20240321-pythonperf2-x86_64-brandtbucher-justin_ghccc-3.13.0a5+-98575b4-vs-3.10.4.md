# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_ghccc
- machine: linux-x86_64
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.10x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 331 ms: 1.06x faster                                                       |
| chameleon      | 9.44 ms                                                      | 7.32 ms: 1.29x faster                                                      |
| docutils       | 3.41 sec                                                     | 4.68 sec: 1.37x slower                                                     |
| html5lib       | 94.6 ms                                                      | 81.5 ms: 1.16x faster                                                      |
| tornado_http   | 157 ms                                                       | 128 ms: 1.23x faster                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 936 ms                                                       | 3.26 sec: 3.48x slower                                                     |
| async_tree_none         | 692 ms                                                       | 2.68 sec: 3.88x slower                                                     |
| async_tree_memoization  | 819 ms                                                       | 3.39 sec: 4.13x slower                                                     |
| async_tree_io           | 1.60 sec                                                     | 9.59 sec: 6.00x slower                                                     |
| Geometric mean          | (ref)                                                        | 4.28x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 83.6 ms: 1.60x faster                                                      |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                                       |
| float          | 111 ms                                                       | 149 ms: 1.34x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 144 ms: 1.32x faster                                                       |
| regex_dna      | 261 ms                                                       | 247 ms: 1.06x faster                                                       |
| regex_v8       | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                      |
| regex_effbot   | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                        | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 313 us: 1.45x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                                     |
| unpickle_pure_python | 312 us                                                       | 226 us: 1.38x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                      |
| json_loads           | 30.3 us                                                      | 24.9 us: 1.22x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 68.4 ms: 1.11x faster                                                      |
| unpickle_list        | 4.65 us                                                      | 4.58 us: 1.01x faster                                                      |
| xml_etree_generate   | 92.3 ms                                                      | 98.6 ms: 1.07x slower                                                      |
| pickle               | 9.89 us                                                      | 10.9 us: 1.10x slower                                                      |
| pickle_list          | 4.12 us                                                      | 4.55 us: 1.11x slower                                                      |
| unpickle             | 13.5 us                                                      | 15.3 us: 1.13x slower                                                      |
| pickle_dict          | 29.5 us                                                      | 33.6 us: 1.14x slower                                                      |
| xml_etree_parse      | 160 ms                                                       | 202 ms: 1.26x slower                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 162 ms: 1.46x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 14.5 ms: 1.26x slower                                                      |
| python_startup_no_site | 7.33 ms                                                      | 12.6 ms: 1.71x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.47x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.30 ms: 1.58x faster                                                      |
| django_template | 50.2 ms                                                      | 39.8 ms: 1.26x faster                                                      |
| genshi_text     | 31.4 ms                                                      | 29.1 ms: 1.08x faster                                                      |
| genshi_xml      | 63.3 ms                                                      | 68.1 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.19x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 119 us: 4.50x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 368 ms: 2.12x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                     |
| deltablue                | 7.50 ms                                                      | 4.04 ms: 1.85x faster                                                      |
| generators               | 57.3 ms                                                      | 33.0 ms: 1.74x faster                                                      |
| chaos                    | 109 ms                                                       | 63.4 ms: 1.71x faster                                                      |
| logging_silent           | 167 ns                                                       | 98.0 ns: 1.71x faster                                                      |
| spectral_norm            | 139 ms                                                       | 82.8 ms: 1.68x faster                                                      |
| crypto_pyaes             | 119 ms                                                       | 72.2 ms: 1.65x faster                                                      |
| raytrace                 | 489 ms                                                       | 301 ms: 1.63x faster                                                       |
| nbody                    | 134 ms                                                       | 83.6 ms: 1.60x faster                                                      |
| mako                     | 14.7 ms                                                      | 9.30 ms: 1.58x faster                                                      |
| richards_super           | 90.6 ms                                                      | 57.9 ms: 1.57x faster                                                      |
| scimark_monte_carlo      | 107 ms                                                       | 69.6 ms: 1.54x faster                                                      |
| go                       | 262 ms                                                       | 175 ms: 1.50x faster                                                       |
| richards                 | 75.1 ms                                                      | 51.2 ms: 1.47x faster                                                      |
| pyflate                  | 733 ms                                                       | 501 ms: 1.46x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 313 us: 1.45x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.55 ms: 1.45x faster                                                      |
| comprehensions           | 26.7 us                                                      | 18.8 us: 1.42x faster                                                      |
| tomli_loads              | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                                     |
| hexiom                   | 9.42 ms                                                      | 6.80 ms: 1.38x faster                                                      |
| unpickle_pure_python     | 312 us                                                       | 226 us: 1.38x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                      |
| coroutines               | 30.3 ms                                                      | 22.4 ms: 1.35x faster                                                      |
| fannkuch                 | 483 ms                                                       | 359 ms: 1.35x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.60 us: 1.34x faster                                                      |
| bench_mp_pool            | 6.37 ms                                                      | 4.79 ms: 1.33x faster                                                      |
| sqlglot_transpile        | 2.68 ms                                                      | 2.03 ms: 1.32x faster                                                      |
| scimark_lu               | 167 ms                                                       | 126 ms: 1.32x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.30 us: 1.32x faster                                                      |
| regex_compile            | 190 ms                                                       | 144 ms: 1.32x faster                                                       |
| thrift                   | 1.18 ms                                                      | 893 us: 1.32x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 37.8 us: 1.32x faster                                                      |
| chameleon                | 9.44 ms                                                      | 7.32 ms: 1.29x faster                                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.69 sec: 1.27x faster                                                     |
| pprint_safe_repr         | 1.05 sec                                                     | 827 ms: 1.27x faster                                                       |
| django_template          | 50.2 ms                                                      | 39.8 ms: 1.26x faster                                                      |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.05 ms: 1.25x faster                                                      |
| scimark_fft              | 361 ms                                                       | 292 ms: 1.24x faster                                                       |
| tornado_http             | 157 ms                                                       | 128 ms: 1.23x faster                                                       |
| json_loads               | 30.3 us                                                      | 24.9 us: 1.22x faster                                                      |
| bench_thread_pool        | 1.14 ms                                                      | 938 us: 1.22x faster                                                       |
| sympy_sum                | 193 ms                                                       | 160 ms: 1.21x faster                                                       |
| scimark_sor              | 180 ms                                                       | 151 ms: 1.20x faster                                                       |
| deepcopy                 | 468 us                                                       | 391 us: 1.20x faster                                                       |
| sympy_str                | 360 ms                                                       | 303 ms: 1.19x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 121 ms: 1.18x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.39 us: 1.18x faster                                                      |
| dulwich_log              | 81.1 ms                                                      | 69.0 ms: 1.18x faster                                                      |
| nqueens                  | 115 ms                                                       | 98.2 ms: 1.17x faster                                                      |
| html5lib                 | 94.6 ms                                                      | 81.5 ms: 1.16x faster                                                      |
| sympy_expand             | 600 ms                                                       | 521 ms: 1.15x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 24.5 ms: 1.15x faster                                                      |
| mdp                      | 3.01 sec                                                     | 2.65 sec: 1.13x faster                                                     |
| sqlite_synth             | 2.99 us                                                      | 2.69 us: 1.11x faster                                                      |
| pathlib                  | 21.4 ms                                                      | 19.2 ms: 1.11x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 68.4 ms: 1.11x faster                                                      |
| create_gc_cycles         | 1.76 ms                                                      | 1.60 ms: 1.10x faster                                                      |
| sqlglot_optimize         | 70.1 ms                                                      | 64.3 ms: 1.09x faster                                                      |
| genshi_text              | 31.4 ms                                                      | 29.1 ms: 1.08x faster                                                      |
| json                     | 5.86 ms                                                      | 5.45 ms: 1.08x faster                                                      |
| mypy2                    | 933 ms                                                       | 867 ms: 1.08x faster                                                       |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.07x faster                                                       |
| 2to3                     | 350 ms                                                       | 331 ms: 1.06x faster                                                       |
| regex_dna                | 261 ms                                                       | 247 ms: 1.06x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                      |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                                       |
| gunicorn                 | 1.16 ms                                                      | 1.12 ms: 1.03x faster                                                      |
| aiohttp                  | 1.19 ms                                                      | 1.16 ms: 1.02x faster                                                      |
| unpickle_list            | 4.65 us                                                      | 4.58 us: 1.01x faster                                                      |
| pycparser                | 1.67 sec                                                     | 1.65 sec: 1.01x faster                                                     |
| xml_etree_generate       | 92.3 ms                                                      | 98.6 ms: 1.07x slower                                                      |
| genshi_xml               | 63.3 ms                                                      | 68.1 ms: 1.08x slower                                                      |
| pickle                   | 9.89 us                                                      | 10.9 us: 1.10x slower                                                      |
| pickle_list              | 4.12 us                                                      | 4.55 us: 1.11x slower                                                      |
| telco                    | 7.23 ms                                                      | 8.00 ms: 1.11x slower                                                      |
| regex_effbot             | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                      |
| async_generators         | 421 ms                                                       | 474 ms: 1.13x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.3 us: 1.13x slower                                                      |
| pickle_dict              | 29.5 us                                                      | 33.6 us: 1.14x slower                                                      |
| gc_traversal             | 3.42 ms                                                      | 3.99 ms: 1.17x slower                                                      |
| python_startup           | 11.5 ms                                                      | 14.5 ms: 1.26x slower                                                      |
| xml_etree_parse          | 160 ms                                                       | 202 ms: 1.26x slower                                                       |
| coverage                 | 63.3 ms                                                      | 83.0 ms: 1.31x slower                                                      |
| float                    | 111 ms                                                       | 149 ms: 1.34x slower                                                       |
| docutils                 | 3.41 sec                                                     | 4.68 sec: 1.37x slower                                                     |
| xml_etree_iterparse      | 110 ms                                                       | 162 ms: 1.46x slower                                                       |
| pylint                   | 566 ms                                                       | 835 ms: 1.48x slower                                                       |
| dask                     | 472 ms                                                       | 708 ms: 1.50x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 12.6 ms: 1.71x slower                                                      |
| unpack_sequence          | 59.9 ns                                                      | 118 ns: 1.97x slower                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 3.26 sec: 3.48x slower                                                     |
| async_tree_none          | 692 ms                                                       | 2.68 sec: 3.88x slower                                                     |
| async_tree_memoization   | 819 ms                                                       | 3.39 sec: 4.13x slower                                                     |
| async_tree_io            | 1.60 sec                                                     | 9.59 sec: 6.00x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.10x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240321-3.13.0a5+-98575b4-JIT/bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.06x


# Memory

- memory change: 1.23x