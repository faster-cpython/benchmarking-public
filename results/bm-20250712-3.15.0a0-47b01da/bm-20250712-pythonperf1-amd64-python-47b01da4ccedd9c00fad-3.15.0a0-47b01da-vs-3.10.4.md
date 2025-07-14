# Results vs. 3.10.4

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.291x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 218 ms: 1.13x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.8 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 393 ms: 2.82x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 202 ms: 2.61x faster                                                       |
| async_tree_none         | 435 ms                                                      | 168 ms: 2.59x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.46x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.9 ms: 1.44x faster                                                      |
| nbody          | 71.3 ms                                                     | 64.2 ms: 1.11x faster                                                      |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.5 ms: 1.35x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.50 ms: 1.11x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.1 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.18 ms: 1.48x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 132 us: 1.38x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 206 us: 1.31x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.35 sec: 1.24x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.4 ms: 1.16x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.8 ms: 1.10x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.41 us: 1.08x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.84 us: 1.05x slower                                                      |
| pickle               | 6.85 us                                                     | 8.08 us: 1.18x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.5 us: 1.19x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.33 us: 1.21x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.25x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.57 ms: 1.38x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                      |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.33x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 393 ms: 2.82x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 202 ms: 2.61x faster                                                       |
| async_tree_none          | 435 ms                                                      | 168 ms: 2.59x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 30.2 ms: 2.51x faster                                                      |
| mdp                      | 1.78 sec                                                    | 802 ms: 2.22x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.14 ms: 1.96x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| go                       | 139 ms                                                      | 74.6 ms: 1.86x faster                                                      |
| pylint                   | 350 ms                                                      | 195 ms: 1.80x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 55.5 ns: 1.70x faster                                                      |
| generators               | 32.4 ms                                                     | 19.2 ms: 1.69x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.9 ms: 1.58x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                      |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                       |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 57.0 ms: 1.51x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.40 sec: 1.50x faster                                                     |
| chaos                    | 61.7 ms                                                     | 41.3 ms: 1.50x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 19.3 us: 1.49x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.18 ms: 1.48x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 500 ms: 1.46x faster                                                       |
| float                    | 61.7 ms                                                     | 42.9 ms: 1.44x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.03 ms: 1.42x faster                                                      |
| scimark_sor              | 106 ms                                                      | 74.9 ms: 1.42x faster                                                      |
| pyflate                  | 409 ms                                                      | 290 ms: 1.41x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.7 ms: 1.41x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 132 us: 1.38x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.57 ms: 1.38x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.8 ms: 1.35x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.5 ms: 1.35x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.2 ms: 1.32x faster                                                      |
| pycparser                | 930 ms                                                      | 709 ms: 1.31x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 206 us: 1.31x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 40.3 ms: 1.25x faster                                                      |
| thrift                   | 617 us                                                      | 496 us: 1.25x faster                                                       |
| sympy_sum                | 107 ms                                                      | 86.3 ms: 1.24x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.35 sec: 1.24x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.01 sec: 1.21x faster                                                     |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 492 ms: 1.20x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                     |
| spectral_norm            | 77.3 ms                                                     | 64.5 ms: 1.20x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.19x faster                                                      |
| sympy_str                | 194 ms                                                      | 167 ms: 1.16x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 38.4 ms: 1.16x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.0 ms: 1.14x faster                                                      |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| 2to3                     | 246 ms                                                      | 218 ms: 1.13x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 860 us: 1.11x faster                                                       |
| nbody                    | 71.3 ms                                                     | 64.2 ms: 1.11x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.50 ms: 1.11x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 60.3 ms: 1.11x faster                                                      |
| sympy_expand             | 314 ms                                                      | 285 ms: 1.10x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 87.8 ms: 1.10x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.48 ms: 1.10x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.1 ms: 1.09x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.41 us: 1.08x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 36.9 ns: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.95 ms: 1.06x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.4 ms: 1.05x faster                                                      |
| scimark_fft              | 187 ms                                                      | 181 ms: 1.04x faster                                                       |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.71 us: 1.01x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| fannkuch                 | 256 ms                                                      | 258 ms: 1.01x slower                                                       |
| async_generators         | 222 ms                                                      | 231 ms: 1.04x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.84 us: 1.05x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.48 ms: 1.14x slower                                                      |
| pickle                   | 6.85 us                                                     | 8.08 us: 1.18x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.5 us: 1.19x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.33 us: 1.21x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.25x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                      |
| coverage                 | 39.0 ms                                                     | 50.4 ms: 1.29x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.10 ms: 1.49x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 93.9 ms: 1.51x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.31 ms: 1.63x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_iterparse, logging_simple, xml_etree_generate
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.291x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown