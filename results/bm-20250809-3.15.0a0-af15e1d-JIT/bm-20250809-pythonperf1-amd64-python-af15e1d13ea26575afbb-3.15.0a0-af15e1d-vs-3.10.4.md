# Results vs. 3.10.4

- fork: python
- ref: af15e1d13ea26575afbb
- machine: windows-amd64
- commit hash: af15e1d
- commit date: 2025-08-09
- overall geometric mean: 1.317x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 389 ms: 2.85x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 205 ms: 2.56x faster                                                       |
| async_tree_none         | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 332 ms: 1.92x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.44x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.9 ms: 1.37x faster                                                      |
| nbody          | 71.3 ms                                                     | 52.8 ms: 1.35x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.7 ms: 1.36x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.7 ms: 1.13x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 105 us: 1.75x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 5.39 ms: 1.70x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.09 sec: 1.53x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 204 us: 1.32x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.7 ms: 1.25x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.1 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.2 ms: 1.03x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.28x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.9 ms: 1.29x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.8 ms: 1.30x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.38 ms: 1.68x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                      |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.19x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.0 ms: 1.17x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.26x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 389 ms: 2.85x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 205 ms: 2.56x faster                                                       |
| async_tree_none          | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.1 ms: 2.36x faster                                                      |
| mdp                      | 1.78 sec                                                    | 800 ms: 2.23x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 332 ms: 1.92x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.85x faster                                                      |
| go                       | 139 ms                                                      | 75.7 ms: 1.84x faster                                                      |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 105 us: 1.75x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.3 ns: 1.71x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.39 ms: 1.70x faster                                                      |
| richards_super           | 52.2 ms                                                     | 30.8 ms: 1.70x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.38 ms: 1.68x faster                                                      |
| generators               | 32.4 ms                                                     | 19.7 ms: 1.64x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.1 us: 1.59x faster                                                      |
| raytrace                 | 273 ms                                                      | 174 ms: 1.57x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.3 ms: 1.56x faster                                                      |
| pyflate                  | 409 ms                                                      | 263 ms: 1.56x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.55x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.09 sec: 1.53x faster                                                     |
| chaos                    | 61.7 ms                                                     | 40.3 ms: 1.53x faster                                                      |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 57.2 ms: 1.50x faster                                                      |
| scimark_sor              | 106 ms                                                      | 74.5 ms: 1.42x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.06 ms: 1.41x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.6 ms: 1.38x faster                                                      |
| float                    | 61.7 ms                                                     | 44.9 ms: 1.37x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 893 ms: 1.37x faster                                                       |
| regex_compile            | 106 ms                                                      | 77.7 ms: 1.36x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.3 ms: 1.35x faster                                                      |
| nbody                    | 71.3 ms                                                     | 52.8 ms: 1.35x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 440 ms: 1.35x faster                                                       |
| pycparser                | 930 ms                                                      | 694 ms: 1.34x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 204 us: 1.32x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 35.7 ms: 1.25x faster                                                      |
| thrift                   | 617 us                                                      | 496 us: 1.24x faster                                                       |
| scimark_fft              | 187 ms                                                      | 151 ms: 1.24x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.9 ms: 1.23x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.5 ms: 1.22x faster                                                      |
| fannkuch                 | 256 ms                                                      | 209 ms: 1.22x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.82 us: 1.21x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.7 ms: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.19x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.18x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.0 ms: 1.17x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.33 ms: 1.17x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 66.2 ms: 1.17x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.7 ms: 1.13x faster                                                      |
| sympy_str                | 194 ms                                                      | 173 ms: 1.13x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 59.9 ms: 1.11x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                      |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 51.1 ms: 1.09x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.7 ms: 1.09x faster                                                      |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.08x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 71.6 ms: 1.06x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.43 us: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.04 us: 1.03x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.2 ms: 1.03x faster                                                      |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| json                     | 3.14 ms                                                     | 3.10 ms: 1.01x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| async_generators         | 222 ms                                                      | 250 ms: 1.13x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.75 ms: 1.21x slower                                                      |
| coverage                 | 39.0 ms                                                     | 48.5 ms: 1.24x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.9 ms: 1.29x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.8 ms: 1.30x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.14 ms: 1.52x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.67x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.32x faster                                                               |
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250809-3.15.0a0-af15e1d-JIT/bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.317x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown