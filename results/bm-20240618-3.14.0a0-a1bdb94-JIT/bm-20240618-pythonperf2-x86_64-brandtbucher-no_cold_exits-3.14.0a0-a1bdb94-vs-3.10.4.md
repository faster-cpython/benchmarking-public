# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-x86_64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 306 ms: 1.14x faster                                                       |
| docutils       | 3.41 sec                                                     | 3.12 sec: 1.09x faster                                                     |
| html5lib       | 94.6 ms                                                      | 74.6 ms: 1.27x faster                                                      |
| tornado_http   | 157 ms                                                       | 123 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                        | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 375 ms: 1.85x faster                                                       |
| async_tree_io           | 1.60 sec                                                     | 906 ms: 1.76x faster                                                       |
| async_tree_memoization  | 819 ms                                                       | 470 ms: 1.74x faster                                                       |
| async_tree_cpu_io_mixed | 936 ms                                                       | 618 ms: 1.52x faster                                                       |
| Geometric mean          | (ref)                                                        | 1.71x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 83.5 ms: 1.61x faster                                                      |
| float          | 111 ms                                                       | 74.8 ms: 1.49x faster                                                      |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                        | 1.37x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.38x faster                                                       |
| regex_dna      | 261 ms                                                       | 238 ms: 1.10x faster                                                       |
| regex_v8       | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                      |
| regex_effbot   | 3.09 ms                                                      | 3.45 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                        | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 312 us: 1.46x faster                                                       |
| unpickle_pure_python | 312 us                                                       | 220 us: 1.42x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                     |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                                      |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                                      |
| xml_etree_generate   | 92.3 ms                                                      | 80.8 ms: 1.14x faster                                                      |
| xml_etree_iterparse  | 110 ms                                                       | 99.6 ms: 1.11x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.11x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 4.85 us: 1.04x slower                                                      |
| pickle_list          | 4.12 us                                                      | 4.35 us: 1.06x slower                                                      |
| pickle_dict          | 29.5 us                                                      | 31.4 us: 1.06x slower                                                      |
| pickle               | 9.89 us                                                      | 10.6 us: 1.08x slower                                                      |
| unpickle             | 13.5 us                                                      | 15.1 us: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                      |
| python_startup_no_site | 7.33 ms                                                      | 8.94 ms: 1.22x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.24 ms: 1.59x faster                                                      |
| django_template | 50.2 ms                                                      | 41.5 ms: 1.21x faster                                                      |
| genshi_text     | 31.4 ms                                                      | 28.7 ms: 1.09x faster                                                      |
| Geometric mean  | (ref)                                                        | 1.20x faster                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 185 us: 2.90x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 380 ms: 2.05x faster                                                       |
| deltablue                | 7.50 ms                                                      | 3.69 ms: 2.03x faster                                                      |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                     |
| async_tree_none          | 692 ms                                                       | 375 ms: 1.85x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 906 ms: 1.76x faster                                                       |
| async_tree_memoization   | 819 ms                                                       | 470 ms: 1.74x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 70.4 ms: 1.69x faster                                                      |
| richards_super           | 90.6 ms                                                      | 53.7 ms: 1.69x faster                                                      |
| deepcopy_memo            | 49.8 us                                                      | 29.6 us: 1.68x faster                                                      |
| raytrace                 | 489 ms                                                       | 291 ms: 1.68x faster                                                       |
| spectral_norm            | 139 ms                                                       | 82.9 ms: 1.68x faster                                                      |
| pyflate                  | 733 ms                                                       | 442 ms: 1.66x faster                                                       |
| generators               | 57.3 ms                                                      | 34.9 ms: 1.64x faster                                                      |
| richards                 | 75.1 ms                                                      | 45.8 ms: 1.64x faster                                                      |
| chaos                    | 109 ms                                                       | 66.3 ms: 1.64x faster                                                      |
| scimark_monte_carlo      | 107 ms                                                       | 65.8 ms: 1.63x faster                                                      |
| nbody                    | 134 ms                                                       | 83.5 ms: 1.61x faster                                                      |
| logging_silent           | 167 ns                                                       | 105 ns: 1.60x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.24 ms: 1.59x faster                                                      |
| go                       | 262 ms                                                       | 166 ms: 1.58x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.44 ms: 1.56x faster                                                      |
| deepcopy                 | 468 us                                                       | 304 us: 1.54x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 618 ms: 1.52x faster                                                       |
| pylint                   | 566 ms                                                       | 380 ms: 1.49x faster                                                       |
| float                    | 111 ms                                                       | 74.8 ms: 1.49x faster                                                      |
| comprehensions           | 26.7 us                                                      | 18.2 us: 1.47x faster                                                      |
| sqlglot_transpile        | 2.68 ms                                                      | 1.84 ms: 1.46x faster                                                      |
| pickle_pure_python       | 455 us                                                       | 312 us: 1.46x faster                                                       |
| scimark_lu               | 167 ms                                                       | 116 ms: 1.44x faster                                                       |
| fannkuch                 | 483 ms                                                       | 337 ms: 1.43x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 220 us: 1.42x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.66 ms: 1.41x faster                                                      |
| logging_simple           | 8.88 us                                                      | 6.41 us: 1.38x faster                                                      |
| tomli_loads              | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                     |
| regex_compile            | 190 ms                                                       | 138 ms: 1.38x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.02 us: 1.37x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 781 ms: 1.34x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                     |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                                     |
| coroutines               | 30.3 ms                                                      | 22.8 ms: 1.33x faster                                                      |
| bench_mp_pool            | 6.37 ms                                                      | 4.81 ms: 1.33x faster                                                      |
| scimark_sor              | 180 ms                                                       | 136 ms: 1.32x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.05 us: 1.31x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                                      |
| pathlib                  | 21.4 ms                                                      | 16.3 ms: 1.31x faster                                                      |
| thrift                   | 1.18 ms                                                      | 905 us: 1.30x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 3.92 ms: 1.29x faster                                                      |
| tornado_http             | 157 ms                                                       | 123 ms: 1.27x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 74.6 ms: 1.27x faster                                                      |
| scimark_fft              | 361 ms                                                       | 293 ms: 1.24x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 925 us: 1.23x faster                                                       |
| nqueens                  | 115 ms                                                       | 93.3 ms: 1.23x faster                                                      |
| django_template          | 50.2 ms                                                      | 41.5 ms: 1.21x faster                                                      |
| dulwich_log              | 81.1 ms                                                      | 67.1 ms: 1.21x faster                                                      |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.20x faster                                                      |
| mdp                      | 3.01 sec                                                     | 2.57 sec: 1.17x faster                                                     |
| dask                     | 472 ms                                                       | 405 ms: 1.16x faster                                                       |
| sympy_sum                | 193 ms                                                       | 168 ms: 1.15x faster                                                       |
| sympy_str                | 360 ms                                                       | 314 ms: 1.15x faster                                                       |
| 2to3                     | 350 ms                                                       | 306 ms: 1.14x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 80.8 ms: 1.14x faster                                                      |
| sympy_expand             | 600 ms                                                       | 529 ms: 1.13x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 128 ms: 1.12x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 62.5 ms: 1.12x faster                                                      |
| xml_etree_iterparse      | 110 ms                                                       | 99.6 ms: 1.11x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.11x faster                                                       |
| regex_dna                | 261 ms                                                       | 238 ms: 1.10x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 25.7 ms: 1.10x faster                                                      |
| genshi_text              | 31.4 ms                                                      | 28.7 ms: 1.09x faster                                                      |
| docutils                 | 3.41 sec                                                     | 3.12 sec: 1.09x faster                                                     |
| async_generators         | 421 ms                                                       | 385 ms: 1.09x faster                                                       |
| json                     | 5.86 ms                                                      | 5.41 ms: 1.08x faster                                                      |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.79 us: 1.07x faster                                                      |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.06x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                      |
| unpickle_list            | 4.65 us                                                      | 4.85 us: 1.04x slower                                                      |
| pickle_list              | 4.12 us                                                      | 4.35 us: 1.06x slower                                                      |
| pickle_dict              | 29.5 us                                                      | 31.4 us: 1.06x slower                                                      |
| pickle                   | 9.89 us                                                      | 10.6 us: 1.08x slower                                                      |
| create_gc_cycles         | 1.76 ms                                                      | 1.92 ms: 1.09x slower                                                      |
| regex_effbot             | 3.09 ms                                                      | 3.45 ms: 1.12x slower                                                      |
| unpickle                 | 13.5 us                                                      | 15.1 us: 1.12x slower                                                      |
| telco                    | 7.23 ms                                                      | 8.17 ms: 1.13x slower                                                      |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                      |
| python_startup_no_site   | 7.33 ms                                                      | 8.94 ms: 1.22x slower                                                      |
| gc_traversal             | 3.42 ms                                                      | 4.42 ms: 1.30x slower                                                      |
| coverage                 | 63.3 ms                                                      | 83.4 ms: 1.32x slower                                                      |
| Geometric mean           | (ref)                                                        | 1.29x faster                                                               |

Benchmark hidden because not significant (2): asyncio_websockets, genshi_xml
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240618-3.14.0a0-a1bdb94-JIT/bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.20x