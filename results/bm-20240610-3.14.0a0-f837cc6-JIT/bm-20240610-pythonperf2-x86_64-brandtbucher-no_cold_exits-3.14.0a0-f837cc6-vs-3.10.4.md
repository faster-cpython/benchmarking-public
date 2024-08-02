# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-x86_64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 304 ms: 1.15x faster                                                       |
| docutils       | 3.41 sec                                                     | 3.09 sec: 1.10x faster                                                     |
| html5lib       | 94.6 ms                                                      | 73.3 ms: 1.29x faster                                                      |
| tornado_http   | 157 ms                                                       | 122 ms: 1.28x faster                                                       |
| Geometric mean | (ref)                                                        | 1.21x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 377 ms: 1.84x faster                                                       |
| async_tree_io           | 1.60 sec                                                     | 886 ms: 1.80x faster                                                       |
| async_tree_memoization  | 819 ms                                                       | 476 ms: 1.72x faster                                                       |
| async_tree_cpu_io_mixed | 936 ms                                                       | 620 ms: 1.51x faster                                                       |
| Geometric mean          | (ref)                                                        | 1.71x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 84.1 ms: 1.59x faster                                                      |
| float          | 111 ms                                                       | 75.5 ms: 1.47x faster                                                      |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                        | 1.37x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 136 ms: 1.40x faster                                                       |
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                                       |
| regex_v8       | 27.2 ms                                                      | 26.5 ms: 1.02x faster                                                      |
| regex_effbot   | 3.09 ms                                                      | 3.49 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                        | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 315 us: 1.45x faster                                                       |
| unpickle_pure_python | 312 us                                                       | 217 us: 1.44x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.10 sec: 1.38x faster                                                     |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.35x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 58.6 ms: 1.30x faster                                                      |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                      |
| xml_etree_generate   | 92.3 ms                                                      | 81.8 ms: 1.13x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 99.0 ms: 1.12x faster                                                      |
| pickle_dict          | 29.5 us                                                      | 31.1 us: 1.05x slower                                                      |
| unpickle_list        | 4.65 us                                                      | 4.93 us: 1.06x slower                                                      |
| pickle               | 9.89 us                                                      | 10.5 us: 1.06x slower                                                      |
| pickle_list          | 4.12 us                                                      | 4.48 us: 1.09x slower                                                      |
| unpickle             | 13.5 us                                                      | 16.0 us: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.2 ms: 1.15x slower                                                      |
| python_startup_no_site | 7.33 ms                                                      | 8.86 ms: 1.21x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.18x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.15 ms: 1.61x faster                                                      |
| django_template | 50.2 ms                                                      | 41.0 ms: 1.22x faster                                                      |
| genshi_text     | 31.4 ms                                                      | 28.1 ms: 1.12x faster                                                      |
| genshi_xml      | 63.3 ms                                                      | 64.9 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.21x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 187 us: 2.87x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 381 ms: 2.05x faster                                                       |
| deltablue                | 7.50 ms                                                      | 3.74 ms: 2.01x faster                                                      |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                     |
| async_tree_none          | 692 ms                                                       | 377 ms: 1.84x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 886 ms: 1.80x faster                                                       |
| richards_super           | 90.6 ms                                                      | 51.3 ms: 1.77x faster                                                      |
| richards                 | 75.1 ms                                                      | 43.2 ms: 1.74x faster                                                      |
| async_tree_memoization   | 819 ms                                                       | 476 ms: 1.72x faster                                                       |
| raytrace                 | 489 ms                                                       | 286 ms: 1.71x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 70.5 ms: 1.69x faster                                                      |
| spectral_norm            | 139 ms                                                       | 83.0 ms: 1.68x faster                                                      |
| chaos                    | 109 ms                                                       | 65.7 ms: 1.65x faster                                                      |
| generators               | 57.3 ms                                                      | 34.8 ms: 1.65x faster                                                      |
| logging_silent           | 167 ns                                                       | 102 ns: 1.64x faster                                                       |
| go                       | 262 ms                                                       | 161 ms: 1.62x faster                                                       |
| pyflate                  | 733 ms                                                       | 453 ms: 1.62x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.15 ms: 1.61x faster                                                      |
| scimark_monte_carlo      | 107 ms                                                       | 67.3 ms: 1.60x faster                                                      |
| nbody                    | 134 ms                                                       | 84.1 ms: 1.59x faster                                                      |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.58x faster                                                      |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 620 ms: 1.51x faster                                                       |
| pylint                   | 566 ms                                                       | 377 ms: 1.50x faster                                                       |
| comprehensions           | 26.7 us                                                      | 18.1 us: 1.48x faster                                                      |
| sqlglot_transpile        | 2.68 ms                                                      | 1.82 ms: 1.47x faster                                                      |
| float                    | 111 ms                                                       | 75.5 ms: 1.47x faster                                                      |
| pickle_pure_python       | 455 us                                                       | 315 us: 1.45x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.44x faster                                                       |
| fannkuch                 | 483 ms                                                       | 336 ms: 1.44x faster                                                       |
| scimark_lu               | 167 ms                                                       | 117 ms: 1.43x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.68 ms: 1.41x faster                                                      |
| regex_compile            | 190 ms                                                       | 136 ms: 1.40x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.39 us: 1.39x faster                                                      |
| coroutines               | 30.3 ms                                                      | 21.9 ms: 1.39x faster                                                      |
| tomli_loads              | 2.92 sec                                                     | 2.10 sec: 1.38x faster                                                     |
| logging_format           | 9.64 us                                                      | 7.02 us: 1.37x faster                                                      |
| deepcopy_memo            | 49.8 us                                                      | 36.5 us: 1.36x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.35x faster                                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.34x faster                                                     |
| bench_mp_pool            | 6.37 ms                                                      | 4.77 ms: 1.33x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 787 ms: 1.33x faster                                                       |
| scimark_sor              | 180 ms                                                       | 137 ms: 1.32x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.2 ms: 1.32x faster                                                      |
| pycparser                | 1.67 sec                                                     | 1.28 sec: 1.30x faster                                                     |
| xml_etree_process        | 75.9 ms                                                      | 58.6 ms: 1.30x faster                                                      |
| thrift                   | 1.18 ms                                                      | 910 us: 1.29x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 73.3 ms: 1.29x faster                                                      |
| tornado_http             | 157 ms                                                       | 122 ms: 1.28x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 65.4 ms: 1.24x faster                                                      |
| scimark_fft              | 361 ms                                                       | 293 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.13 ms: 1.23x faster                                                      |
| django_template          | 50.2 ms                                                      | 41.0 ms: 1.22x faster                                                      |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                      |
| nqueens                  | 115 ms                                                       | 94.9 ms: 1.21x faster                                                      |
| bench_thread_pool        | 1.14 ms                                                      | 965 us: 1.18x faster                                                       |
| sympy_sum                | 193 ms                                                       | 164 ms: 1.18x faster                                                       |
| dask                     | 472 ms                                                       | 401 ms: 1.18x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.56 sec: 1.18x faster                                                     |
| sympy_str                | 360 ms                                                       | 310 ms: 1.16x faster                                                       |
| 2to3                     | 350 ms                                                       | 304 ms: 1.15x faster                                                       |
| deepcopy                 | 468 us                                                       | 408 us: 1.15x faster                                                       |
| sympy_expand             | 600 ms                                                       | 525 ms: 1.14x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 81.8 ms: 1.13x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 28.1 ms: 1.12x faster                                                      |
| xml_etree_iterparse      | 110 ms                                                       | 99.0 ms: 1.12x faster                                                      |
| sympy_integrate          | 28.2 ms                                                      | 25.4 ms: 1.11x faster                                                      |
| sqlglot_normalize        | 144 ms                                                       | 130 ms: 1.11x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.09 sec: 1.10x faster                                                     |
| deepcopy_reduce          | 4.01 us                                                      | 3.64 us: 1.10x faster                                                      |
| json                     | 5.86 ms                                                      | 5.34 ms: 1.10x faster                                                      |
| sqlglot_optimize         | 70.1 ms                                                      | 64.0 ms: 1.10x faster                                                      |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                                       |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                       |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.77 us: 1.08x faster                                                      |
| async_generators         | 421 ms                                                       | 391 ms: 1.08x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 26.5 ms: 1.02x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 64.9 ms: 1.03x slower                                                      |
| pickle_dict              | 29.5 us                                                      | 31.1 us: 1.05x slower                                                      |
| unpickle_list            | 4.65 us                                                      | 4.93 us: 1.06x slower                                                      |
| pickle                   | 9.89 us                                                      | 10.5 us: 1.06x slower                                                      |
| pickle_list              | 4.12 us                                                      | 4.48 us: 1.09x slower                                                      |
| create_gc_cycles         | 1.76 ms                                                      | 1.97 ms: 1.12x slower                                                      |
| regex_effbot             | 3.09 ms                                                      | 3.49 ms: 1.13x slower                                                      |
| telco                    | 7.23 ms                                                      | 8.23 ms: 1.14x slower                                                      |
| python_startup           | 11.5 ms                                                      | 13.2 ms: 1.15x slower                                                      |
| unpickle                 | 13.5 us                                                      | 16.0 us: 1.18x slower                                                      |
| python_startup_no_site   | 7.33 ms                                                      | 8.86 ms: 1.21x slower                                                      |
| coverage                 | 63.3 ms                                                      | 79.6 ms: 1.26x slower                                                      |
| gc_traversal             | 3.42 ms                                                      | 4.88 ms: 1.43x slower                                                      |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240610-3.14.0a0-f837cc6-JIT/bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.20x