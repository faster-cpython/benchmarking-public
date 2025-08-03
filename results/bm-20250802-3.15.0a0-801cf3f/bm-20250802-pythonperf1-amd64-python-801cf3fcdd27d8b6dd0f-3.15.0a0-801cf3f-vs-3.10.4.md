# Results vs. 3.10.4

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.247x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.3 ms: 1.27x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 405 ms: 2.74x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 215 ms: 2.44x faster                                                       |
| async_tree_none         | 435 ms                                                      | 188 ms: 2.31x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 347 ms: 1.84x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.31x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.2 ms: 1.33x faster                                                      |
| nbody          | 71.3 ms                                                     | 67.0 ms: 1.06x faster                                                      |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.2 ms: 1.31x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.21 ms: 1.48x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 144 us: 1.27x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 223 us: 1.21x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 40.7 ms: 1.09x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.67 us: 1.05x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.4 ms: 1.05x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 68.0 ms: 1.05x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 58.6 ms: 1.05x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.03 us: 1.12x slower                                                      |
| pickle               | 6.85 us                                                     | 7.90 us: 1.15x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.2 us: 1.17x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.28 us: 1.19x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.9 ms: 1.31x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 20.3 ms: 1.31x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.67 ms: 1.36x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.9 ms: 1.24x faster                                                      |
| django_template | 28.9 ms                                                     | 24.6 ms: 1.18x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.2 ms: 1.13x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.22x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.19x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 405 ms: 2.74x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 215 ms: 2.44x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.5 ms: 2.32x faster                                                      |
| async_tree_none          | 435 ms                                                      | 188 ms: 2.31x faster                                                       |
| mdp                      | 1.78 sec                                                    | 834 ms: 2.13x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.22 ms: 1.88x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 347 ms: 1.84x faster                                                       |
| go                       | 139 ms                                                      | 80.7 ms: 1.72x faster                                                      |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 56.6 ns: 1.67x faster                                                      |
| generators               | 32.4 ms                                                     | 20.0 ms: 1.62x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.1 us: 1.59x faster                                                      |
| richards_super           | 52.2 ms                                                     | 33.0 ms: 1.58x faster                                                      |
| raytrace                 | 273 ms                                                      | 179 ms: 1.53x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.42 sec: 1.48x faster                                                     |
| richards                 | 42.4 ms                                                     | 28.6 ms: 1.48x faster                                                      |
| deepcopy                 | 255 us                                                      | 172 us: 1.48x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.2 us: 1.48x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.21 ms: 1.48x faster                                                      |
| chaos                    | 61.7 ms                                                     | 42.0 ms: 1.47x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 507 ms: 1.44x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.2 ms: 1.39x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 62.2 ms: 1.38x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.67 ms: 1.36x faster                                                      |
| pyflate                  | 409 ms                                                      | 302 ms: 1.35x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.25 ms: 1.35x faster                                                      |
| scimark_sor              | 106 ms                                                      | 79.3 ms: 1.34x faster                                                      |
| float                    | 61.7 ms                                                     | 46.2 ms: 1.33x faster                                                      |
| regex_compile            | 106 ms                                                      | 81.2 ms: 1.31x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 48.9 ms: 1.28x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 144 us: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 732 ms: 1.27x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.3 ms: 1.27x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.9 ms: 1.24x faster                                                      |
| thrift                   | 617 us                                                      | 503 us: 1.23x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.21x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 223 us: 1.21x faster                                                       |
| sympy_sum                | 107 ms                                                      | 88.9 ms: 1.20x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.6 ms: 1.18x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 33.7 ns: 1.18x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 65.9 ms: 1.17x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                     |
| tomli_loads              | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 507 ms: 1.17x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.05 sec: 1.16x faster                                                     |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 44.2 ms: 1.14x faster                                                      |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.2 ms: 1.13x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 872 us: 1.10x faster                                                       |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 40.7 ms: 1.09x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                                      |
| nbody                    | 71.3 ms                                                     | 67.0 ms: 1.06x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.67 us: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.4 ms: 1.05x faster                                                      |
| sympy_expand             | 314 ms                                                      | 300 ms: 1.05x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 63.7 ms: 1.05x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.62 us: 1.02x faster                                                      |
| json                     | 3.14 ms                                                     | 3.07 ms: 1.02x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 74.7 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.68 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| scimark_fft              | 187 ms                                                      | 191 ms: 1.02x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 68.0 ms: 1.05x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 58.6 ms: 1.05x slower                                                      |
| async_generators         | 222 ms                                                      | 239 ms: 1.08x slower                                                       |
| fannkuch                 | 256 ms                                                      | 277 ms: 1.08x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 3.03 us: 1.12x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.90 us: 1.15x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.2 us: 1.17x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.64 ms: 1.18x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.28 us: 1.19x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.9 ms: 1.28x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.9 ms: 1.31x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.3 ms: 1.31x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.17 ms: 1.54x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 96.1 ms: 1.55x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.39 ms: 1.74x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                               |

Benchmark hidden because not significant (1): logging_simple
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.247x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown