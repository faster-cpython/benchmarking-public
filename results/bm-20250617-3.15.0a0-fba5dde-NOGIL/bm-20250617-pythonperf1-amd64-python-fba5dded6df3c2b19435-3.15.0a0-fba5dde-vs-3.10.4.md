# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.314x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 337 ms: 1.37x slower                                                       |
| docutils       | 1.92 sec                                                    | 4.24 sec: 2.21x slower                                                     |
| html5lib       | 51.0 ms                                                     | 63.3 ms: 1.24x slower                                                      |
| Geometric mean | (ref)                                                       | 1.55x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 583 ms: 1.90x faster                                                       |
| async_tree_none         | 435 ms                                                      | 275 ms: 1.58x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 336 ms: 1.57x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 486 ms: 1.31x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.58x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 149 ms                                                      | 140 ms: 1.06x faster                                                       |
| float          | 61.7 ms                                                     | 97.6 ms: 1.58x slower                                                      |
| nbody          | 71.3 ms                                                     | 183 ms: 2.57x slower                                                       |
| Geometric mean | (ref)                                                       | 1.56x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 113 ms: 1.21x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 16.8 ms: 1.09x slower                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.81 ms: 1.09x slower                                                      |
| regex_compile  | 106 ms                                                      | 161 ms: 1.52x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 9.51 ms: 1.04x slower                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 113 ms: 1.16x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 22.0 us: 1.28x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.53 us: 1.30x slower                                                      |
| unpickle             | 9.09 us                                                     | 11.9 us: 1.31x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.82 us: 1.39x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 92.7 ms: 1.43x slower                                                      |
| pickle               | 6.85 us                                                     | 9.91 us: 1.45x slower                                                      |
| json_loads           | 14.0 us                                                     | 23.2 us: 1.66x slower                                                      |
| pickle_pure_python   | 270 us                                                      | 452 us: 1.68x slower                                                       |
| xml_etree_process    | 44.5 ms                                                     | 80.0 ms: 1.80x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 108 ms: 1.95x slower                                                       |
| unpickle_pure_python | 183 us                                                      | 358 us: 1.95x slower                                                       |
| tomli_loads          | 1.67 sec                                                    | 5.05 sec: 3.02x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.54x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.3 ms: 1.31x slower                                                      |
| python_startup         | 20.6 ms                                                     | 27.7 ms: 1.34x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.33x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 45.6 ms: 1.58x slower                                                      |
| genshi_xml      | 41.0 ms                                                     | 66.3 ms: 1.62x slower                                                      |
| genshi_text     | 19.8 ms                                                     | 33.7 ms: 1.70x slower                                                      |
| mako            | 9.03 ms                                                     | 16.4 ms: 1.82x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.68x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                  | 75.7 ms                                                     | 35.4 ms: 2.14x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 583 ms: 1.90x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 199 us: 1.69x faster                                                       |
| async_tree_none          | 435 ms                                                      | 275 ms: 1.58x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 336 ms: 1.57x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 486 ms: 1.31x faster                                                       |
| pylint                   | 350 ms                                                      | 283 ms: 1.24x faster                                                       |
| regex_dna                | 136 ms                                                      | 113 ms: 1.21x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 615 ms: 1.19x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.70 us: 1.12x faster                                                      |
| pidigits                 | 149 ms                                                      | 140 ms: 1.06x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 9.51 ms: 1.04x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 16.8 ms: 1.09x slower                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.81 ms: 1.09x slower                                                      |
| dulwich_log              | 50.5 ms                                                     | 56.5 ms: 1.12x slower                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 113 ms: 1.16x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.72 ms: 1.22x slower                                                      |
| html5lib                 | 51.0 ms                                                     | 63.3 ms: 1.24x slower                                                      |
| mdp                      | 1.78 sec                                                    | 2.22 sec: 1.25x slower                                                     |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.70 sec: 1.28x slower                                                     |
| pickle_dict              | 17.2 us                                                     | 22.0 us: 1.28x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.24 ms: 1.30x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.53 us: 1.30x slower                                                      |
| generators               | 32.4 ms                                                     | 42.4 ms: 1.31x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.3 ms: 1.31x slower                                                      |
| deepcopy                 | 255 us                                                      | 336 us: 1.31x slower                                                       |
| unpickle                 | 9.09 us                                                     | 11.9 us: 1.31x slower                                                      |
| sympy_sum                | 107 ms                                                      | 143 ms: 1.34x slower                                                       |
| python_startup           | 20.6 ms                                                     | 27.7 ms: 1.34x slower                                                      |
| json                     | 3.14 ms                                                     | 4.23 ms: 1.35x slower                                                      |
| 2to3                     | 246 ms                                                      | 337 ms: 1.37x slower                                                       |
| sympy_integrate          | 15.3 ms                                                     | 21.0 ms: 1.37x slower                                                      |
| thrift                   | 617 us                                                      | 848 us: 1.37x slower                                                       |
| go                       | 139 ms                                                      | 192 ms: 1.38x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.82 us: 1.39x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.11 ms: 1.39x slower                                                      |
| deltablue                | 4.19 ms                                                     | 5.93 ms: 1.42x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 92.7 ms: 1.43x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 89.8 ms: 1.45x slower                                                      |
| pickle                   | 6.85 us                                                     | 9.91 us: 1.45x slower                                                      |
| sympy_str                | 194 ms                                                      | 291 ms: 1.50x slower                                                       |
| pyflate                  | 409 ms                                                      | 614 ms: 1.50x slower                                                       |
| richards_super           | 52.2 ms                                                     | 79.1 ms: 1.51x slower                                                      |
| deepcopy_memo            | 28.8 us                                                     | 43.6 us: 1.52x slower                                                      |
| regex_compile            | 106 ms                                                      | 161 ms: 1.52x slower                                                       |
| raytrace                 | 273 ms                                                      | 419 ms: 1.53x slower                                                       |
| comprehensions           | 16.5 us                                                     | 25.5 us: 1.54x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 118 ms: 1.55x slower                                                       |
| chaos                    | 61.7 ms                                                     | 96.8 ms: 1.57x slower                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 3.47 us: 1.58x slower                                                      |
| django_template          | 28.9 ms                                                     | 45.6 ms: 1.58x slower                                                      |
| float                    | 61.7 ms                                                     | 97.6 ms: 1.58x slower                                                      |
| sympy_expand             | 314 ms                                                      | 499 ms: 1.59x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 66.3 ms: 1.62x slower                                                      |
| richards                 | 42.4 ms                                                     | 70.3 ms: 1.66x slower                                                      |
| json_loads               | 14.0 us                                                     | 23.2 us: 1.66x slower                                                      |
| pickle_pure_python       | 270 us                                                      | 452 us: 1.68x slower                                                       |
| genshi_text              | 19.8 ms                                                     | 33.7 ms: 1.70x slower                                                      |
| logging_format           | 6.76 us                                                     | 11.6 us: 1.72x slower                                                      |
| scimark_sor              | 106 ms                                                      | 189 ms: 1.78x slower                                                       |
| logging_simple           | 6.22 us                                                     | 11.1 us: 1.78x slower                                                      |
| xml_etree_process        | 44.5 ms                                                     | 80.0 ms: 1.80x slower                                                      |
| mako                     | 9.03 ms                                                     | 16.4 ms: 1.82x slower                                                      |
| pycparser                | 930 ms                                                      | 1.70 sec: 1.82x slower                                                     |
| hexiom                   | 5.74 ms                                                     | 10.6 ms: 1.84x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 124 ms: 1.87x slower                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 107 ms: 1.87x slower                                                       |
| async_generators         | 222 ms                                                      | 415 ms: 1.87x slower                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 118 ms: 1.89x slower                                                       |
| scimark_lu               | 85.8 ms                                                     | 164 ms: 1.92x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 108 ms: 1.95x slower                                                       |
| unpickle_pure_python     | 183 us                                                      | 358 us: 1.95x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 80.8 ns: 2.04x slower                                                      |
| telco                    | 3.94 ms                                                     | 8.06 ms: 2.04x slower                                                      |
| spectral_norm            | 77.3 ms                                                     | 164 ms: 2.12x slower                                                       |
| coroutines               | 16.0 ms                                                     | 33.9 ms: 2.12x slower                                                      |
| coverage                 | 39.0 ms                                                     | 83.9 ms: 2.15x slower                                                      |
| docutils                 | 1.92 sec                                                    | 4.24 sec: 2.21x slower                                                     |
| fannkuch                 | 256 ms                                                      | 573 ms: 2.24x slower                                                       |
| scimark_fft              | 187 ms                                                      | 424 ms: 2.26x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 6.58 ms: 2.42x slower                                                      |
| pprint_safe_repr         | 592 ms                                                      | 1.47 sec: 2.49x slower                                                     |
| nbody                    | 71.3 ms                                                     | 183 ms: 2.57x slower                                                       |
| tomli_loads              | 1.67 sec                                                    | 5.05 sec: 3.02x slower                                                     |
| pprint_pformat           | 1.22 sec                                                    | 4.23 sec: 3.47x slower                                                     |
| logging_silent           | 94.6 ns                                                     | 586 ns: 6.20x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.47x slower                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.314x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.47x
- 95% likely to have a slowdown of 1.44x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: unknown