# Results vs. 3.10.4

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.308x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.17x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 394 ms: 2.81x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 211 ms: 2.49x faster                                                       |
| async_tree_none         | 435 ms                                                      | 180 ms: 2.41x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 335 ms: 1.90x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.38x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.7 ms: 1.38x faster                                                      |
| nbody          | 71.3 ms                                                     | 60.5 ms: 1.18x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.9 ms: 1.36x faster                                                      |
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.5 ms: 1.14x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 105 us: 1.75x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.10 sec: 1.52x faster                                                     |
| json_dumps           | 9.16 ms                                                     | 6.13 ms: 1.49x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.5 ms: 1.25x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 86.7 ms: 1.12x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 50.3 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.5 ms: 1.04x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.79 us: 1.03x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.91 us: 1.07x slower                                                      |
| pickle               | 6.85 us                                                     | 7.84 us: 1.14x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.6 us: 1.20x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.35 us: 1.22x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.0 ms: 1.29x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.35 ms: 1.69x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                                      |
| django_template | 28.9 ms                                                     | 24.8 ms: 1.16x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.18x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 394 ms: 2.81x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 211 ms: 2.49x faster                                                       |
| async_tree_none          | 435 ms                                                      | 180 ms: 2.41x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.5 ms: 2.32x faster                                                      |
| mdp                      | 1.78 sec                                                    | 819 ms: 2.17x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.17 ms: 1.93x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 335 ms: 1.90x faster                                                       |
| go                       | 139 ms                                                      | 77.0 ms: 1.80x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 105 us: 1.75x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.9 ns: 1.72x faster                                                      |
| pylint                   | 350 ms                                                      | 204 ms: 1.72x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.6 ms: 1.70x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.35 ms: 1.69x faster                                                      |
| generators               | 32.4 ms                                                     | 19.8 ms: 1.64x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 17.8 us: 1.61x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.0 ms: 1.57x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.8 us: 1.53x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.10 sec: 1.52x faster                                                     |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                       |
| raytrace                 | 273 ms                                                      | 182 ms: 1.50x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.13 ms: 1.49x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.41 sec: 1.49x faster                                                     |
| pyflate                  | 409 ms                                                      | 275 ms: 1.49x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 57.9 ms: 1.48x faster                                                      |
| chaos                    | 61.7 ms                                                     | 42.7 ms: 1.44x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.2 ms: 1.42x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 527 ms: 1.39x faster                                                       |
| float                    | 61.7 ms                                                     | 44.7 ms: 1.38x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.17 ms: 1.38x faster                                                      |
| scimark_sor              | 106 ms                                                      | 77.3 ms: 1.37x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 45.8 ms: 1.37x faster                                                      |
| regex_compile            | 106 ms                                                      | 77.9 ms: 1.36x faster                                                      |
| pycparser                | 930 ms                                                      | 698 ms: 1.33x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 930 ms: 1.31x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 454 ms: 1.30x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| scimark_fft              | 187 ms                                                      | 149 ms: 1.26x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.5 ms: 1.25x faster                                                      |
| thrift                   | 617 us                                                      | 498 us: 1.24x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.23x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.3 ms: 1.22x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.2 ms: 1.21x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.25 ms: 1.21x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.7 ms: 1.20x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 65.4 ms: 1.18x faster                                                      |
| nbody                    | 71.3 ms                                                     | 60.5 ms: 1.18x faster                                                      |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.17x faster                                                     |
| django_template          | 28.9 ms                                                     | 24.8 ms: 1.16x faster                                                      |
| fannkuch                 | 256 ms                                                      | 220 ms: 1.16x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.5 ms: 1.14x faster                                                      |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 86.7 ms: 1.12x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 861 us: 1.11x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 35.8 ns: 1.11x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 50.3 ms: 1.10x faster                                                      |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 61.0 ms: 1.09x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.8 ms: 1.08x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 71.0 ms: 1.07x faster                                                      |
| sympy_expand             | 314 ms                                                      | 299 ms: 1.05x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.48 us: 1.04x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.5 ms: 1.04x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.79 us: 1.03x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.07 us: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.91 us: 1.07x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.27 ms: 1.08x slower                                                      |
| async_generators         | 222 ms                                                      | 247 ms: 1.11x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.84 us: 1.14x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.6 us: 1.20x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.35 us: 1.22x slower                                                      |
| coverage                 | 39.0 ms                                                     | 48.5 ms: 1.24x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.0 ms: 1.29x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.14 ms: 1.52x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 95.6 ms: 1.54x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.30 ms: 1.63x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (2): json, json_loads
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.308x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown