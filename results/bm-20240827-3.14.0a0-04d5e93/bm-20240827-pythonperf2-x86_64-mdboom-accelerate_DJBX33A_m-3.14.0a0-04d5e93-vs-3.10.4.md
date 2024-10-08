# Results vs. 3.10.4

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: linux-x86_64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                      |
| html5lib       | 94.6 ms                                                      | 72.5 ms: 1.30x faster                                                       |
| tornado_http   | 157 ms                                                       | 117 ms: 1.34x faster                                                        |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 317 ms: 2.18x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 397 ms: 2.06x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 814 ms: 1.96x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 568 ms: 1.65x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.95x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 86.7 ms: 1.55x faster                                                       |
| float          | 111 ms                                                       | 78.4 ms: 1.42x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 142 ms: 1.34x faster                                                        |
| regex_dna      | 261 ms                                                       | 233 ms: 1.12x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.53 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 212 us: 1.47x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 318 us: 1.43x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 60.1 ms: 1.26x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.37 sec: 1.23x faster                                                      |
| json_loads           | 30.3 us                                                      | 24.8 us: 1.22x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.09x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 86.7 ms: 1.06x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.24x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.08 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| django_template | 50.2 ms                                                      | 39.6 ms: 1.27x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 26.1 ms: 1.20x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 57.9 ms: 1.09x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.24x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 176 us: 3.05x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.39 ms: 2.21x faster                                                       |
| async_tree_none          | 692 ms                                                       | 317 ms: 2.18x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 367 ms: 2.12x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 397 ms: 2.06x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 814 ms: 1.96x faster                                                        |
| generators               | 57.3 ms                                                      | 29.5 ms: 1.94x faster                                                       |
| raytrace                 | 489 ms                                                       | 270 ms: 1.81x faster                                                        |
| chaos                    | 109 ms                                                       | 61.2 ms: 1.77x faster                                                       |
| scimark_lu               | 167 ms                                                       | 94.6 ms: 1.76x faster                                                       |
| logging_silent           | 167 ns                                                       | 97.3 ns: 1.72x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 65.1 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 568 ms: 1.65x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 30.3 us: 1.64x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 72.9 ms: 1.64x faster                                                       |
| deepcopy                 | 468 us                                                       | 287 us: 1.63x faster                                                        |
| pylint                   | 566 ms                                                       | 350 ms: 1.62x faster                                                        |
| richards_super           | 90.6 ms                                                      | 56.9 ms: 1.59x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.0 us: 1.57x faster                                                       |
| nbody                    | 134 ms                                                       | 86.7 ms: 1.55x faster                                                       |
| pyflate                  | 733 ms                                                       | 479 ms: 1.53x faster                                                        |
| scimark_sor              | 180 ms                                                       | 119 ms: 1.52x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.23 ms: 1.51x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                                       |
| richards                 | 75.1 ms                                                      | 51.0 ms: 1.47x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 212 us: 1.47x faster                                                        |
| spectral_norm            | 139 ms                                                       | 97.0 ms: 1.43x faster                                                       |
| go                       | 262 ms                                                       | 183 ms: 1.43x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 318 us: 1.43x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| float                    | 111 ms                                                       | 78.4 ms: 1.42x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.29 us: 1.41x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.84 us: 1.41x faster                                                       |
| thrift                   | 1.18 ms                                                      | 837 us: 1.40x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.7 ms: 1.40x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                                       |
| fannkuch                 | 483 ms                                                       | 354 ms: 1.36x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.69 ms: 1.36x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                                       |
| regex_compile            | 190 ms                                                       | 142 ms: 1.34x faster                                                        |
| tornado_http             | 157 ms                                                       | 117 ms: 1.34x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.34x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 858 us: 1.33x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.31x faster                                                      |
| nqueens                  | 115 ms                                                       | 87.9 ms: 1.31x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 804 ms: 1.31x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 72.5 ms: 1.30x faster                                                       |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.27x faster                                                        |
| django_template          | 50.2 ms                                                      | 39.6 ms: 1.27x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 60.1 ms: 1.26x faster                                                       |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                                        |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.37 sec: 1.23x faster                                                      |
| sympy_integrate          | 28.2 ms                                                      | 22.9 ms: 1.23x faster                                                       |
| json_loads               | 30.3 us                                                      | 24.8 us: 1.22x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.22x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 58.1 ms: 1.21x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 26.1 ms: 1.20x faster                                                       |
| sympy_expand             | 600 ms                                                       | 501 ms: 1.20x faster                                                        |
| scimark_fft              | 361 ms                                                       | 303 ms: 1.19x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.52 sec: 1.19x faster                                                      |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.37 ms: 1.16x faster                                                       |
| async_generators         | 421 ms                                                       | 362 ms: 1.16x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                      |
| regex_dna                | 261 ms                                                       | 233 ms: 1.12x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.12x faster                                                        |
| json                     | 5.86 ms                                                      | 5.34 ms: 1.10x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.09x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 57.9 ms: 1.09x faster                                                       |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 86.7 ms: 1.06x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.98 ms: 1.13x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.53 ms: 1.14x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.33 ms: 1.15x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.08 ms: 1.24x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.38 ms: 1.28x slower                                                       |
| coverage                 | 63.3 ms                                                      | 82.6 ms: 1.31x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240827-3.14.0a0-04d5e93/bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.13x