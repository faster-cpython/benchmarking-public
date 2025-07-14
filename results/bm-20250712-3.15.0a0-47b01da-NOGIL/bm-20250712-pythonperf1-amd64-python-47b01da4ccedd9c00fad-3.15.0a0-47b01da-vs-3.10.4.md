# Results vs. 3.10.4

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.138x faster
- HPT reliability: 99.84%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 229 ms: 1.07x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.87 sec: 1.49x slower                                                     |
| html5lib       | 51.0 ms                                                     | 41.0 ms: 1.24x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 354 ms: 3.13x faster                                                       |
| async_tree_none         | 435 ms                                                      | 172 ms: 2.53x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 211 ms: 2.49x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.49x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.9 ms: 1.34x faster                                                      |
| pidigits       | 149 ms                                                      | 137 ms: 1.09x faster                                                       |
| nbody          | 71.3 ms                                                     | 84.0 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.20x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.5 ms: 1.14x faster                                                      |
| regex_compile  | 106 ms                                                      | 94.7 ms: 1.12x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.70 ms: 1.37x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 160 us: 1.14x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 237 us: 1.14x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.2 ms: 1.10x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 91.0 ms: 1.06x faster                                                      |
| pickle_list          | 2.75 us                                                     | 3.05 us: 1.11x slower                                                      |
| unpickle             | 9.09 us                                                     | 10.1 us: 1.12x slower                                                      |
| json_loads           | 14.0 us                                                     | 15.7 us: 1.12x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 62.4 ms: 1.12x slower                                                      |
| pickle               | 6.85 us                                                     | 7.72 us: 1.13x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.06 us: 1.13x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.0 us: 1.16x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.69 sec: 1.61x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 27.5 ms: 1.05x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 39.3 ms: 1.05x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 19.0 ms: 1.04x faster                                                      |
| mako            | 9.03 ms                                                     | 9.84 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 354 ms: 3.13x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 129 us: 2.60x faster                                                       |
| async_tree_none          | 435 ms                                                      | 172 ms: 2.53x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 211 ms: 2.49x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 30.6 ms: 2.47x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 411 ms: 1.78x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.50 ms: 1.68x faster                                                      |
| pylint                   | 350 ms                                                      | 216 ms: 1.62x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.17 sec: 1.53x faster                                                     |
| logging_silent           | 94.6 ns                                                     | 62.0 ns: 1.53x faster                                                      |
| go                       | 139 ms                                                      | 92.5 ms: 1.50x faster                                                      |
| generators               | 32.4 ms                                                     | 22.4 ms: 1.44x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.33 us: 1.43x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.9 us: 1.38x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.70 ms: 1.37x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.2 us: 1.35x faster                                                      |
| float                    | 61.7 ms                                                     | 45.9 ms: 1.34x faster                                                      |
| chaos                    | 61.7 ms                                                     | 47.0 ms: 1.31x faster                                                      |
| raytrace                 | 273 ms                                                      | 213 ms: 1.28x faster                                                       |
| deepcopy                 | 255 us                                                      | 199 us: 1.28x faster                                                       |
| pycparser                | 930 ms                                                      | 731 ms: 1.27x faster                                                       |
| richards_super           | 52.2 ms                                                     | 41.1 ms: 1.27x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 68.3 ms: 1.26x faster                                                      |
| pyflate                  | 409 ms                                                      | 327 ms: 1.25x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 41.0 ms: 1.24x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.63 ms: 1.24x faster                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.15 ms: 1.23x faster                                                      |
| richards                 | 42.4 ms                                                     | 34.8 ms: 1.22x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.1 ms: 1.20x faster                                                      |
| regex_dna                | 136 ms                                                      | 114 ms: 1.20x faster                                                       |
| scimark_sor              | 106 ms                                                      | 91.6 ms: 1.16x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 160 us: 1.14x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.5 ms: 1.14x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 237 us: 1.14x faster                                                       |
| regex_compile            | 106 ms                                                      | 94.7 ms: 1.12x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.2 ms: 1.10x faster                                                      |
| pidigits                 | 149 ms                                                      | 137 ms: 1.09x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 57.7 ms: 1.08x faster                                                      |
| sympy_sum                | 107 ms                                                      | 99.0 ms: 1.08x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.2 ms: 1.08x faster                                                      |
| 2to3                     | 246 ms                                                      | 229 ms: 1.07x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 91.0 ms: 1.06x faster                                                      |
| thrift                   | 617 us                                                      | 581 us: 1.06x faster                                                       |
| coroutines               | 16.0 ms                                                     | 15.1 ms: 1.06x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 54.1 ms: 1.06x faster                                                      |
| django_template          | 28.9 ms                                                     | 27.5 ms: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 39.3 ms: 1.05x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 19.0 ms: 1.04x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 568 ms: 1.04x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 38.3 ns: 1.04x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.13 us: 1.04x faster                                                      |
| json                     | 3.14 ms                                                     | 3.05 ms: 1.03x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 76.3 ms: 1.01x faster                                                      |
| sympy_expand             | 314 ms                                                      | 324 ms: 1.03x slower                                                       |
| nqueens                  | 66.6 ms                                                     | 72.1 ms: 1.08x slower                                                      |
| mako                     | 9.03 ms                                                     | 9.84 ms: 1.09x slower                                                      |
| logging_format           | 6.76 us                                                     | 7.38 us: 1.09x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.05 us: 1.11x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.91 us: 1.11x slower                                                      |
| unpickle                 | 9.09 us                                                     | 10.1 us: 1.12x slower                                                      |
| json_loads               | 14.0 us                                                     | 15.7 us: 1.12x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 62.4 ms: 1.12x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.72 us: 1.13x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.06 us: 1.13x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.11 ms: 1.14x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.10 ms: 1.15x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 87.3 ms: 1.15x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.0 us: 1.16x slower                                                      |
| nbody                    | 71.3 ms                                                     | 84.0 ms: 1.18x slower                                                      |
| async_generators         | 222 ms                                                      | 267 ms: 1.20x slower                                                       |
| scimark_fft              | 187 ms                                                      | 226 ms: 1.20x slower                                                       |
| fannkuch                 | 256 ms                                                      | 309 ms: 1.21x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 977 us: 1.22x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 78.9 ms: 1.27x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.70 sec: 1.39x slower                                                     |
| telco                    | 3.94 ms                                                     | 5.59 ms: 1.42x slower                                                      |
| docutils                 | 1.92 sec                                                    | 2.87 sec: 1.49x slower                                                     |
| tomli_loads              | 1.67 sec                                                    | 2.69 sec: 1.61x slower                                                     |
| coverage                 | 39.0 ms                                                     | 66.9 ms: 1.72x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (3): sympy_str, xml_etree_process, asyncio_tcp_ssl
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.138x faster

# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown