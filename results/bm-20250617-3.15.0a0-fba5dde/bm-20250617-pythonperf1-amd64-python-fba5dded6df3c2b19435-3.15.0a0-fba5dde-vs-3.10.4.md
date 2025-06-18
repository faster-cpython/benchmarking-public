# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.130x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 295 ms: 1.20x slower                                                       |
| docutils       | 1.92 sec                                                    | 2.08 sec: 1.08x slower                                                     |
| html5lib       | 51.0 ms                                                     | 51.5 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 546 ms: 2.03x faster                                                       |
| async_tree_none         | 435 ms                                                      | 242 ms: 1.79x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 295 ms: 1.78x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 440 ms: 1.45x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.75x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| float          | 61.7 ms                                                     | 76.0 ms: 1.23x slower                                                      |
| nbody          | 71.3 ms                                                     | 99.6 ms: 1.40x slower                                                      |
| Geometric mean | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 117 ms: 1.17x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.73 ms: 1.04x slower                                                      |
| regex_v8       | 15.4 ms                                                     | 17.0 ms: 1.10x slower                                                      |
| regex_compile  | 106 ms                                                      | 122 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 8.83 ms: 1.04x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 108 ms: 1.12x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 3.07 us: 1.13x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.02 sec: 1.21x slower                                                     |
| unpickle             | 9.09 us                                                     | 11.5 us: 1.27x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 22.7 us: 1.32x slower                                                      |
| pickle_pure_python   | 270 us                                                      | 358 us: 1.33x slower                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 89.5 ms: 1.38x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.79 us: 1.38x slower                                                      |
| pickle               | 6.85 us                                                     | 9.61 us: 1.40x slower                                                      |
| xml_etree_process    | 44.5 ms                                                     | 64.0 ms: 1.44x slower                                                      |
| unpickle_pure_python | 183 us                                                      | 275 us: 1.50x slower                                                       |
| json_loads           | 14.0 us                                                     | 21.1 us: 1.50x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 89.3 ms: 1.61x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.31x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.0 ms: 1.29x slower                                                      |
| python_startup         | 20.6 ms                                                     | 27.2 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 41.0 ms                                                     | 48.3 ms: 1.18x slower                                                      |
| genshi_text     | 19.8 ms                                                     | 23.3 ms: 1.18x slower                                                      |
| django_template | 28.9 ms                                                     | 36.3 ms: 1.25x slower                                                      |
| mako            | 9.03 ms                                                     | 12.4 ms: 1.37x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.24x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                  | 75.7 ms                                                     | 34.3 ms: 2.21x faster                                                      |
| typing_runtime_protocols | 336 us                                                      | 153 us: 2.20x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 546 ms: 2.03x faster                                                       |
| async_tree_none          | 435 ms                                                      | 242 ms: 1.79x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 295 ms: 1.78x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.15 sec: 1.55x faster                                                     |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 440 ms: 1.45x faster                                                       |
| pylint                   | 350 ms                                                      | 247 ms: 1.42x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.49 sec: 1.41x faster                                                     |
| asyncio_tcp              | 732 ms                                                      | 554 ms: 1.32x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.17x faster                                                       |
| go                       | 139 ms                                                      | 131 ms: 1.06x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 8.83 ms: 1.04x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.86 us: 1.03x faster                                                      |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 50.8 ms: 1.01x slower                                                      |
| html5lib                 | 51.0 ms                                                     | 51.5 ms: 1.01x slower                                                      |
| deltablue                | 4.19 ms                                                     | 4.29 ms: 1.02x slower                                                      |
| deepcopy                 | 255 us                                                      | 262 us: 1.02x slower                                                       |
| chaos                    | 61.7 ms                                                     | 64.0 ms: 1.04x slower                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.73 ms: 1.04x slower                                                      |
| pycparser                | 930 ms                                                      | 974 ms: 1.05x slower                                                       |
| sympy_sum                | 107 ms                                                      | 115 ms: 1.07x slower                                                       |
| sympy_integrate          | 15.3 ms                                                     | 16.4 ms: 1.08x slower                                                      |
| docutils                 | 1.92 sec                                                    | 2.08 sec: 1.08x slower                                                     |
| richards_super           | 52.2 ms                                                     | 57.0 ms: 1.09x slower                                                      |
| raytrace                 | 273 ms                                                      | 300 ms: 1.10x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 17.0 ms: 1.10x slower                                                      |
| pyflate                  | 409 ms                                                      | 453 ms: 1.11x slower                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 108 ms: 1.12x slower                                                       |
| thrift                   | 617 us                                                      | 692 us: 1.12x slower                                                       |
| generators               | 32.4 ms                                                     | 36.6 ms: 1.13x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.07 us: 1.13x slower                                                      |
| deepcopy_memo            | 28.8 us                                                     | 33.0 us: 1.15x slower                                                      |
| regex_compile            | 106 ms                                                      | 122 ms: 1.15x slower                                                       |
| comprehensions           | 16.5 us                                                     | 19.3 us: 1.17x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 48.3 ms: 1.18x slower                                                      |
| genshi_text              | 19.8 ms                                                     | 23.3 ms: 1.18x slower                                                      |
| sympy_str                | 194 ms                                                      | 231 ms: 1.19x slower                                                       |
| richards                 | 42.4 ms                                                     | 50.5 ms: 1.19x slower                                                      |
| 2to3                     | 246 ms                                                      | 295 ms: 1.20x slower                                                       |
| tomli_loads              | 1.67 sec                                                    | 2.02 sec: 1.21x slower                                                     |
| meteor_contest           | 75.9 ms                                                     | 92.3 ms: 1.22x slower                                                      |
| scimark_sor              | 106 ms                                                      | 130 ms: 1.22x slower                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.71 us: 1.23x slower                                                      |
| float                    | 61.7 ms                                                     | 76.0 ms: 1.23x slower                                                      |
| django_template          | 28.9 ms                                                     | 36.3 ms: 1.25x slower                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 71.9 ms: 1.26x slower                                                      |
| sympy_expand             | 314 ms                                                      | 396 ms: 1.26x slower                                                       |
| unpickle                 | 9.09 us                                                     | 11.5 us: 1.27x slower                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 79.7 ms: 1.27x slower                                                      |
| hexiom                   | 5.74 ms                                                     | 7.36 ms: 1.28x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.0 ms: 1.29x slower                                                      |
| python_startup           | 20.6 ms                                                     | 27.2 ms: 1.32x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 22.7 us: 1.32x slower                                                      |
| json                     | 3.14 ms                                                     | 4.17 ms: 1.33x slower                                                      |
| pickle_pure_python       | 270 us                                                      | 358 us: 1.33x slower                                                       |
| mako                     | 9.03 ms                                                     | 12.4 ms: 1.37x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 91.5 ms: 1.37x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 89.5 ms: 1.38x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.79 us: 1.38x slower                                                      |
| scimark_lu               | 85.8 ms                                                     | 119 ms: 1.39x slower                                                       |
| nbody                    | 71.3 ms                                                     | 99.6 ms: 1.40x slower                                                      |
| pickle                   | 6.85 us                                                     | 9.61 us: 1.40x slower                                                      |
| scimark_fft              | 187 ms                                                      | 265 ms: 1.41x slower                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.74 sec: 1.43x slower                                                     |
| spectral_norm            | 77.3 ms                                                     | 111 ms: 1.44x slower                                                       |
| xml_etree_process        | 44.5 ms                                                     | 64.0 ms: 1.44x slower                                                      |
| logging_format           | 6.76 us                                                     | 9.74 us: 1.44x slower                                                      |
| pprint_safe_repr         | 592 ms                                                      | 854 ms: 1.44x slower                                                       |
| logging_simple           | 6.22 us                                                     | 9.25 us: 1.49x slower                                                      |
| async_generators         | 222 ms                                                      | 332 ms: 1.50x slower                                                       |
| unpickle_pure_python     | 183 us                                                      | 275 us: 1.50x slower                                                       |
| json_loads               | 14.0 us                                                     | 21.1 us: 1.50x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 4.16 ms: 1.53x slower                                                      |
| coroutines               | 16.0 ms                                                     | 24.7 ms: 1.54x slower                                                      |
| telco                    | 3.94 ms                                                     | 6.25 ms: 1.59x slower                                                      |
| fannkuch                 | 256 ms                                                      | 406 ms: 1.59x slower                                                       |
| coverage                 | 39.0 ms                                                     | 62.3 ms: 1.60x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 89.3 ms: 1.61x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 105 ms: 1.69x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.48 ms: 1.85x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 77.9 ns: 1.97x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 3.05 ms: 2.16x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 494 ns: 5.22x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.17x slower                                                               |

Benchmark hidden because not significant (1): bench_thread_pool
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.130x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: unknown