# Results vs. 3.10.4

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.302x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.15x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 391 ms: 2.83x faster                                                       |
| async_tree_none         | 435 ms                                                      | 167 ms: 2.61x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 204 ms: 2.57x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.46x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                      |
| nbody          | 71.3 ms                                                     | 54.7 ms: 1.30x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.1 ms: 1.34x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 107 us: 1.71x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.14 sec: 1.47x faster                                                     |
| json_dumps           | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 204 us: 1.32x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 36.1 ms: 1.23x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.1 ms: 1.09x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.61 us: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.7 ms: 1.05x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.77 us: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                      |
| pickle               | 6.85 us                                                     | 7.88 us: 1.15x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.1 us: 1.17x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.39 us: 1.23x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.5 ms: 1.24x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.35 ms: 1.69x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                                      |
| django_template | 28.9 ms                                                     | 25.0 ms: 1.15x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.3 ms: 1.13x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.29x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.21x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 391 ms: 2.83x faster                                                       |
| async_tree_none          | 435 ms                                                      | 167 ms: 2.61x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 204 ms: 2.57x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 30.1 ms: 2.51x faster                                                      |
| mdp                      | 1.78 sec                                                    | 800 ms: 2.23x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.24 ms: 1.87x faster                                                      |
| go                       | 139 ms                                                      | 78.2 ms: 1.78x faster                                                      |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 107 us: 1.71x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.7 ns: 1.70x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.35 ms: 1.69x faster                                                      |
| richards_super           | 52.2 ms                                                     | 31.4 ms: 1.66x faster                                                      |
| pyflate                  | 409 ms                                                      | 252 ms: 1.62x faster                                                       |
| generators               | 32.4 ms                                                     | 20.3 ms: 1.59x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.56x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.4 ms: 1.55x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.7 us: 1.54x faster                                                      |
| raytrace                 | 273 ms                                                      | 182 ms: 1.50x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.3 ms: 1.50x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.42 sec: 1.48x faster                                                     |
| deepcopy                 | 255 us                                                      | 173 us: 1.47x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.14 sec: 1.47x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 521 ms: 1.40x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.12 ms: 1.40x faster                                                      |
| float                    | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 45.4 ms: 1.38x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 62.4 ms: 1.37x faster                                                      |
| regex_compile            | 106 ms                                                      | 79.1 ms: 1.34x faster                                                      |
| pycparser                | 930 ms                                                      | 696 ms: 1.34x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.3 ms: 1.32x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 204 us: 1.32x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                      |
| scimark_sor              | 106 ms                                                      | 80.6 ms: 1.32x faster                                                      |
| nbody                    | 71.3 ms                                                     | 54.7 ms: 1.30x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 458 ms: 1.29x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 944 ms: 1.29x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 40.5 ms: 1.25x faster                                                      |
| thrift                   | 617 us                                                      | 501 us: 1.23x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.1 ms: 1.23x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.23x faster                                                      |
| scimark_fft              | 187 ms                                                      | 153 ms: 1.23x faster                                                       |
| sympy_sum                | 107 ms                                                      | 87.6 ms: 1.22x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.25 ms: 1.21x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.7 ms: 1.20x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.20x faster                                                      |
| fannkuch                 | 256 ms                                                      | 220 ms: 1.16x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.0 ms: 1.15x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.15x faster                                                     |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 67.3 ms: 1.15x faster                                                      |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.3 ms: 1.13x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 59.7 ms: 1.12x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 861 us: 1.11x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                      |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.7 ms: 1.09x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 51.1 ms: 1.09x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 70.9 ms: 1.07x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.61 us: 1.06x faster                                                      |
| sympy_expand             | 314 ms                                                      | 298 ms: 1.06x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.7 ms: 1.05x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 37.7 ns: 1.05x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.57 us: 1.03x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| json                     | 3.14 ms                                                     | 3.05 ms: 1.03x faster                                                      |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.16 us: 1.01x faster                                                      |
| unpickle_list            | 2.71 us                                                     | 2.77 us: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.41 ms: 1.12x slower                                                      |
| async_generators         | 222 ms                                                      | 252 ms: 1.14x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.88 us: 1.15x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.1 us: 1.17x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.39 us: 1.23x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.5 ms: 1.24x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                      |
| coverage                 | 39.0 ms                                                     | 50.9 ms: 1.31x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.13 ms: 1.51x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 94.4 ms: 1.52x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.31 ms: 1.63x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.302x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown