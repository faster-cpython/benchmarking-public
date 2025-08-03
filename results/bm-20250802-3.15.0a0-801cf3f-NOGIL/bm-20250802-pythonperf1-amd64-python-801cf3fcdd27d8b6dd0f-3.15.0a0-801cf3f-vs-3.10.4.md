# Results vs. 3.10.4

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.133x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 232 ms: 1.06x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.97 sec: 1.55x slower                                                     |
| html5lib       | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 352 ms: 3.14x faster                                                       |
| async_tree_none         | 435 ms                                                      | 178 ms: 2.45x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 224 ms: 2.35x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 345 ms: 1.85x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.40x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.4 ms: 1.33x faster                                                      |
| pidigits       | 149 ms                                                      | 142 ms: 1.05x faster                                                       |
| nbody          | 71.3 ms                                                     | 82.2 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 112 ms: 1.21x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                      |
| regex_compile  | 106 ms                                                      | 94.4 ms: 1.12x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.51 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.72 ms: 1.36x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 157 us: 1.17x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 242 us: 1.11x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.5 ms: 1.09x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 90.6 ms: 1.07x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 44.2 ms: 1.01x faster                                                      |
| json_loads           | 14.0 us                                                     | 15.8 us: 1.13x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 63.1 ms: 1.14x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.10 us: 1.14x slower                                                      |
| unpickle             | 9.09 us                                                     | 10.6 us: 1.17x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.23 us: 1.17x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 21.2 us: 1.23x slower                                                      |
| pickle               | 6.85 us                                                     | 8.47 us: 1.24x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.77 sec: 1.66x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                      |
| python_startup         | 20.6 ms                                                     | 27.0 ms: 1.31x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 27.3 ms: 1.06x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 40.3 ms: 1.02x faster                                                      |
| mako            | 9.03 ms                                                     | 9.71 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 352 ms: 3.14x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 130 us: 2.58x faster                                                       |
| async_tree_none          | 435 ms                                                      | 178 ms: 2.45x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 224 ms: 2.35x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.7 ms: 2.31x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 345 ms: 1.85x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.48 ms: 1.69x faster                                                      |
| pylint                   | 350 ms                                                      | 208 ms: 1.68x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 62.1 ns: 1.52x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.18 sec: 1.51x faster                                                     |
| go                       | 139 ms                                                      | 92.9 ms: 1.50x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 496 ms: 1.47x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.36 us: 1.41x faster                                                      |
| generators               | 32.4 ms                                                     | 23.2 ms: 1.40x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.9 us: 1.38x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.72 ms: 1.36x faster                                                      |
| float                    | 61.7 ms                                                     | 46.4 ms: 1.33x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.5 us: 1.32x faster                                                      |
| chaos                    | 61.7 ms                                                     | 46.9 ms: 1.32x faster                                                      |
| raytrace                 | 273 ms                                                      | 211 ms: 1.29x faster                                                       |
| pycparser                | 930 ms                                                      | 731 ms: 1.27x faster                                                       |
| richards_super           | 52.2 ms                                                     | 41.3 ms: 1.26x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 68.2 ms: 1.26x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                                      |
| deepcopy                 | 255 us                                                      | 203 us: 1.26x faster                                                       |
| pyflate                  | 409 ms                                                      | 328 ms: 1.25x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.67 ms: 1.23x faster                                                      |
| regex_dna                | 136 ms                                                      | 112 ms: 1.21x faster                                                       |
| richards                 | 42.4 ms                                                     | 35.5 ms: 1.19x faster                                                      |
| scimark_sor              | 106 ms                                                      | 89.8 ms: 1.18x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.9 ms: 1.18x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 157 us: 1.17x faster                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.22 ms: 1.16x faster                                                      |
| regex_compile            | 106 ms                                                      | 94.4 ms: 1.12x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 242 us: 1.11x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 51.5 ms: 1.11x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 56.8 ms: 1.10x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.51 ms: 1.10x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.5 ms: 1.09x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.2 ms: 1.08x faster                                                      |
| thrift                   | 617 us                                                      | 577 us: 1.07x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 90.6 ms: 1.07x faster                                                      |
| django_template          | 28.9 ms                                                     | 27.3 ms: 1.06x faster                                                      |
| coroutines               | 16.0 ms                                                     | 15.1 ms: 1.06x faster                                                      |
| 2to3                     | 246 ms                                                      | 232 ms: 1.06x faster                                                       |
| pidigits                 | 149 ms                                                      | 142 ms: 1.05x faster                                                       |
| sympy_sum                | 107 ms                                                      | 102 ms: 1.05x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 567 ms: 1.04x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 74.2 ms: 1.04x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.13 us: 1.03x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 40.3 ms: 1.02x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 39.1 ns: 1.01x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 44.2 ms: 1.01x faster                                                      |
| sympy_expand             | 314 ms                                                      | 322 ms: 1.03x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.23 us: 1.07x slower                                                      |
| mako                     | 9.03 ms                                                     | 9.71 ms: 1.08x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.72 us: 1.08x slower                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.34 sec: 1.11x slower                                                     |
| nqueens                  | 66.6 ms                                                     | 74.6 ms: 1.12x slower                                                      |
| json_loads               | 14.0 us                                                     | 15.8 us: 1.13x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 63.1 ms: 1.14x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.10 us: 1.14x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.10 ms: 1.15x slower                                                      |
| fannkuch                 | 256 ms                                                      | 294 ms: 1.15x slower                                                       |
| nbody                    | 71.3 ms                                                     | 82.2 ms: 1.15x slower                                                      |
| unpickle                 | 9.09 us                                                     | 10.6 us: 1.17x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 89.1 ms: 1.17x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.23 us: 1.17x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.20 ms: 1.18x slower                                                      |
| async_generators         | 222 ms                                                      | 263 ms: 1.19x slower                                                       |
| scimark_fft              | 187 ms                                                      | 227 ms: 1.21x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 21.2 us: 1.23x slower                                                      |
| pickle                   | 6.85 us                                                     | 8.47 us: 1.24x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 80.7 ms: 1.30x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.05 ms: 1.31x slower                                                      |
| python_startup           | 20.6 ms                                                     | 27.0 ms: 1.31x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.34 ms: 1.36x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.72 sec: 1.41x slower                                                     |
| docutils                 | 1.92 sec                                                    | 2.97 sec: 1.55x slower                                                     |
| tomli_loads              | 1.67 sec                                                    | 2.77 sec: 1.66x slower                                                     |
| coverage                 | 39.0 ms                                                     | 66.3 ms: 1.70x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (3): genshi_text, sympy_str, json
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.133x faster

# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown