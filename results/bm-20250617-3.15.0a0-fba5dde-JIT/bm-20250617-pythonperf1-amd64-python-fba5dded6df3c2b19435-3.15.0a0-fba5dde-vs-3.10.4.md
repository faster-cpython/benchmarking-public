# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.085x slower
- HPT reliability: 99.89%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 289 ms: 1.18x slower                                                       |
| docutils       | 1.92 sec                                                    | 2.12 sec: 1.10x slower                                                     |
| html5lib       | 51.0 ms                                                     | 52.9 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 536 ms: 2.07x faster                                                       |
| async_tree_none         | 435 ms                                                      | 236 ms: 1.85x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 289 ms: 1.82x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 432 ms: 1.48x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.79x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 53.7 ms: 1.33x faster                                                      |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| float          | 61.7 ms                                                     | 78.5 ms: 1.27x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.73 ms: 1.04x slower                                                      |
| regex_v8       | 15.4 ms                                                     | 16.6 ms: 1.08x slower                                                      |
| regex_compile  | 106 ms                                                      | 122 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 157 us: 1.17x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                     |
| json_dumps           | 9.16 ms                                                     | 8.67 ms: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 106 ms: 1.09x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 3.12 us: 1.15x slower                                                      |
| xml_etree_process    | 44.5 ms                                                     | 53.2 ms: 1.20x slower                                                      |
| pickle_pure_python   | 270 us                                                      | 328 us: 1.22x slower                                                       |
| unpickle             | 9.09 us                                                     | 11.7 us: 1.29x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 72.7 ms: 1.31x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 22.7 us: 1.32x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 87.2 ms: 1.34x slower                                                      |
| pickle               | 6.85 us                                                     | 9.70 us: 1.42x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.94 us: 1.43x slower                                                      |
| json_loads           | 14.0 us                                                     | 20.8 us: 1.48x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.20x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.9 ms: 1.28x slower                                                      |
| python_startup         | 20.6 ms                                                     | 27.3 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.13 ms: 1.27x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 51.5 ms: 1.26x slower                                                      |
| genshi_text     | 19.8 ms                                                     | 25.5 ms: 1.29x slower                                                      |
| django_template | 28.9 ms                                                     | 38.7 ms: 1.34x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 145 us: 2.32x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 34.4 ms: 2.20x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 536 ms: 2.07x faster                                                       |
| async_tree_none          | 435 ms                                                      | 236 ms: 1.85x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 289 ms: 1.82x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 432 ms: 1.48x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.21 sec: 1.48x faster                                                     |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.51 sec: 1.40x faster                                                     |
| pylint                   | 350 ms                                                      | 254 ms: 1.38x faster                                                       |
| nbody                    | 71.3 ms                                                     | 53.7 ms: 1.33x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 552 ms: 1.33x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.13 ms: 1.27x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 157 us: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.74 us: 1.10x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 8.67 ms: 1.06x faster                                                      |
| pyflate                  | 409 ms                                                      | 390 ms: 1.05x faster                                                       |
| comprehensions           | 16.5 us                                                     | 15.9 us: 1.04x faster                                                      |
| go                       | 139 ms                                                      | 137 ms: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| scimark_fft              | 187 ms                                                      | 185 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.70 ms: 1.01x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 52.1 ms: 1.03x slower                                                      |
| pycparser                | 930 ms                                                      | 964 ms: 1.04x slower                                                       |
| html5lib                 | 51.0 ms                                                     | 52.9 ms: 1.04x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 995 us: 1.04x slower                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.73 ms: 1.04x slower                                                      |
| chaos                    | 61.7 ms                                                     | 65.7 ms: 1.06x slower                                                      |
| deepcopy                 | 255 us                                                      | 273 us: 1.07x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 16.6 ms: 1.08x slower                                                      |
| deltablue                | 4.19 ms                                                     | 4.52 ms: 1.08x slower                                                      |
| sympy_sum                | 107 ms                                                      | 116 ms: 1.09x slower                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 106 ms: 1.09x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 83.0 ms: 1.09x slower                                                      |
| docutils                 | 1.92 sec                                                    | 2.12 sec: 1.10x slower                                                     |
| fannkuch                 | 256 ms                                                      | 282 ms: 1.10x slower                                                       |
| sympy_integrate          | 15.3 ms                                                     | 17.0 ms: 1.11x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.37 sec: 1.12x slower                                                     |
| raytrace                 | 273 ms                                                      | 307 ms: 1.12x slower                                                       |
| pprint_safe_repr         | 592 ms                                                      | 667 ms: 1.13x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 3.12 us: 1.15x slower                                                      |
| regex_compile            | 106 ms                                                      | 122 ms: 1.15x slower                                                       |
| thrift                   | 617 us                                                      | 714 us: 1.16x slower                                                       |
| richards_super           | 52.2 ms                                                     | 60.9 ms: 1.17x slower                                                      |
| 2to3                     | 246 ms                                                      | 289 ms: 1.18x slower                                                       |
| generators               | 32.4 ms                                                     | 38.3 ms: 1.18x slower                                                      |
| xml_etree_process        | 44.5 ms                                                     | 53.2 ms: 1.20x slower                                                      |
| pickle_pure_python       | 270 us                                                      | 328 us: 1.22x slower                                                       |
| sympy_str                | 194 ms                                                      | 238 ms: 1.22x slower                                                       |
| deepcopy_memo            | 28.8 us                                                     | 35.6 us: 1.24x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 51.5 ms: 1.26x slower                                                      |
| float                    | 61.7 ms                                                     | 78.5 ms: 1.27x slower                                                      |
| richards                 | 42.4 ms                                                     | 54.1 ms: 1.28x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.9 ms: 1.28x slower                                                      |
| unpickle                 | 9.09 us                                                     | 11.7 us: 1.29x slower                                                      |
| scimark_sor              | 106 ms                                                      | 137 ms: 1.29x slower                                                       |
| genshi_text              | 19.8 ms                                                     | 25.5 ms: 1.29x slower                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.84 us: 1.29x slower                                                      |
| json                     | 3.14 ms                                                     | 4.07 ms: 1.30x slower                                                      |
| sympy_expand             | 314 ms                                                      | 409 ms: 1.30x slower                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 74.6 ms: 1.30x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 72.7 ms: 1.31x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 22.7 us: 1.32x slower                                                      |
| python_startup           | 20.6 ms                                                     | 27.3 ms: 1.32x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.27 ms: 1.34x slower                                                      |
| django_template          | 28.9 ms                                                     | 38.7 ms: 1.34x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 87.2 ms: 1.34x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 91.2 ms: 1.37x slower                                                      |
| hexiom                   | 5.74 ms                                                     | 8.03 ms: 1.40x slower                                                      |
| pickle                   | 6.85 us                                                     | 9.70 us: 1.42x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.94 us: 1.43x slower                                                      |
| scimark_lu               | 85.8 ms                                                     | 126 ms: 1.47x slower                                                       |
| json_loads               | 14.0 us                                                     | 20.8 us: 1.48x slower                                                      |
| spectral_norm            | 77.3 ms                                                     | 115 ms: 1.49x slower                                                       |
| logging_format           | 6.76 us                                                     | 10.1 us: 1.50x slower                                                      |
| logging_simple           | 6.22 us                                                     | 9.56 us: 1.54x slower                                                      |
| async_generators         | 222 ms                                                      | 355 ms: 1.60x slower                                                       |
| coverage                 | 39.0 ms                                                     | 62.9 ms: 1.61x slower                                                      |
| coroutines               | 16.0 ms                                                     | 26.8 ms: 1.67x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 105 ms: 1.70x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.47 ms: 1.84x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 77.8 ns: 1.96x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 3.02 ms: 2.14x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 509 ns: 5.38x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.13x slower                                                               |

Benchmark hidden because not significant (1): crypto_pyaes
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.085x slower

# HPT report

- Reliability score: 99.89% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown