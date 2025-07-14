# Results vs. 3.10.4

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-x86_64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.332x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 67.6 ms: 1.40x faster                                                       |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 628 ms: 2.54x faster                                                        |
| async_tree_none         | 692 ms                                                       | 276 ms: 2.51x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 334 ms: 2.46x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 502 ms: 1.86x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 63.5 ms: 1.75x faster                                                       |
| nbody          | 134 ms                                                       | 98.2 ms: 1.37x faster                                                       |
| pidigits       | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 131 ms: 1.45x faster                                                        |
| regex_dna      | 261 ms                                                       | 225 ms: 1.16x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 24.1 ms: 1.13x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 196 us: 1.59x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.91 sec: 1.52x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 55.5 ms: 1.37x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 335 us: 1.36x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.5 us: 1.19x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 139 ms: 1.15x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 80.1 ms: 1.15x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 97.7 ms: 1.13x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 5.05 us: 1.09x slower                                                       |
| unpickle             | 13.5 us                                                      | 14.9 us: 1.11x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 33.5 us: 1.14x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.00 us: 1.21x slower                                                       |
| pickle               | 9.89 us                                                      | 12.2 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.86 ms: 1.21x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.73 ms: 1.51x faster                                                       |
| django_template | 50.2 ms                                                      | 35.4 ms: 1.42x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 22.7 ms: 1.38x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 53.8 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.37x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 169 us: 3.18x faster                                                        |
| deltablue                | 7.50 ms                                                      | 2.88 ms: 2.60x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 628 ms: 2.54x faster                                                        |
| async_tree_none          | 692 ms                                                       | 276 ms: 2.51x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 334 ms: 2.46x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.28 sec: 2.35x faster                                                      |
| richards_super           | 90.6 ms                                                      | 40.5 ms: 2.24x faster                                                       |
| richards                 | 75.1 ms                                                      | 35.2 ms: 2.13x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 372 ms: 2.10x faster                                                        |
| go                       | 262 ms                                                       | 126 ms: 2.08x faster                                                        |
| generators               | 57.3 ms                                                      | 29.1 ms: 1.97x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.96x faster                                                      |
| deepcopy_memo            | 49.8 us                                                      | 25.9 us: 1.93x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 502 ms: 1.86x faster                                                        |
| chaos                    | 109 ms                                                       | 60.2 ms: 1.80x faster                                                       |
| logging_silent           | 167 ns                                                       | 93.2 ns: 1.80x faster                                                       |
| spectral_norm            | 139 ms                                                       | 78.3 ms: 1.78x faster                                                       |
| pylint                   | 566 ms                                                       | 323 ms: 1.75x faster                                                        |
| float                    | 111 ms                                                       | 63.5 ms: 1.75x faster                                                       |
| pyflate                  | 733 ms                                                       | 419 ms: 1.75x faster                                                        |
| scimark_lu               | 167 ms                                                       | 95.8 ms: 1.74x faster                                                       |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.74x faster                                                        |
| raytrace                 | 489 ms                                                       | 293 ms: 1.67x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 64.5 ms: 1.67x faster                                                       |
| deepcopy                 | 468 us                                                       | 282 us: 1.66x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 196 us: 1.59x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.54x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 77.7 ms: 1.53x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.91 sec: 1.52x faster                                                      |
| hexiom                   | 9.42 ms                                                      | 6.19 ms: 1.52x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.73 ms: 1.51x faster                                                       |
| regex_compile            | 190 ms                                                       | 131 ms: 1.45x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.14 us: 1.45x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.69 us: 1.44x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.50 sec: 1.43x faster                                                      |
| django_template          | 50.2 ms                                                      | 35.4 ms: 1.42x faster                                                       |
| thrift                   | 1.18 ms                                                      | 831 us: 1.41x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 744 ms: 1.41x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 67.6 ms: 1.40x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 22.7 ms: 1.38x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 58.8 ms: 1.38x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 55.5 ms: 1.37x faster                                                       |
| nbody                    | 134 ms                                                       | 98.2 ms: 1.37x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 335 us: 1.36x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.97 us: 1.35x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.5 ms: 1.35x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                      |
| fannkuch                 | 483 ms                                                       | 372 ms: 1.30x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                       |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.2 ms: 1.27x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.9 ms: 1.26x faster                                                       |
| sympy_str                | 360 ms                                                       | 289 ms: 1.25x faster                                                        |
| nqueens                  | 115 ms                                                       | 93.6 ms: 1.23x faster                                                       |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                                        |
| scimark_fft              | 361 ms                                                       | 297 ms: 1.22x faster                                                        |
| sympy_expand             | 600 ms                                                       | 494 ms: 1.22x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.5 us: 1.19x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 53.8 ms: 1.18x faster                                                       |
| unpack_sequence          | 59.9 ns                                                      | 51.0 ns: 1.17x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| regex_dna                | 261 ms                                                       | 225 ms: 1.16x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 139 ms: 1.15x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 80.1 ms: 1.15x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 993 us: 1.15x faster                                                        |
| meteor_contest           | 138 ms                                                       | 122 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.7 ms: 1.13x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 24.1 ms: 1.13x faster                                                       |
| json                     | 5.86 ms                                                      | 5.30 ms: 1.11x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.06x faster                                                       |
| pidigits                 | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.87 ms: 1.04x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 383 ms: 1.02x faster                                                        |
| async_generators         | 421 ms                                                       | 443 ms: 1.05x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.05 us: 1.09x slower                                                       |
| unpickle                 | 13.5 us                                                      | 14.9 us: 1.11x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 33.5 us: 1.14x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.86 ms: 1.21x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.00 us: 1.21x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.2 us: 1.23x slower                                                       |
| coverage                 | 63.3 ms                                                      | 81.2 ms: 1.28x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.92 ms: 1.66x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.75 ms: 1.98x slower                                                       |
| telco                    | 7.23 ms                                                      | 160 ms: 22.20x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 1.27 sec: 199.90x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.332x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.41x