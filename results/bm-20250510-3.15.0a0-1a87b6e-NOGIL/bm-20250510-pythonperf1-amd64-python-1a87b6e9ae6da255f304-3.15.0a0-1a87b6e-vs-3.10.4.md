# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-amd64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.166x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.91 sec: 1.51x slower                                                     |
| html5lib       | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 350 ms: 3.17x faster                                                       |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.56x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 208 ms: 2.53x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 331 ms: 1.92x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.51x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.6 ms: 1.35x faster                                                      |
| pidigits       | 149 ms                                                      | 139 ms: 1.07x faster                                                       |
| nbody          | 71.3 ms                                                     | 76.9 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                       |
| regex_compile  | 106 ms                                                      | 91.4 ms: 1.16x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 13.4 ms: 1.15x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 7.28 ms: 1.26x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 152 us: 1.21x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 228 us: 1.18x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.0 ms: 1.10x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 91.7 ms: 1.06x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 44.8 ms: 1.01x slower                                                      |
| unpickle             | 9.09 us                                                     | 10.0 us: 1.10x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 62.2 ms: 1.12x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.17 us: 1.17x slower                                                      |
| json_loads           | 14.0 us                                                     | 16.7 us: 1.19x slower                                                      |
| pickle               | 6.85 us                                                     | 8.17 us: 1.19x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 21.2 us: 1.23x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.41 us: 1.24x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.58 sec: 1.54x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 20.1 ms: 1.29x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 37.6 ms: 1.09x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.4 ms: 1.08x faster                                                      |
| mako            | 9.03 ms                                                     | 9.69 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.05x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 350 ms: 3.17x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 130 us: 2.58x faster                                                       |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.56x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 208 ms: 2.53x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.0 ms: 2.37x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 331 ms: 1.92x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.30 ms: 1.82x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.03 sec: 1.72x faster                                                     |
| pylint                   | 350 ms                                                      | 203 ms: 1.72x faster                                                       |
| go                       | 139 ms                                                      | 90.7 ms: 1.53x faster                                                      |
| generators               | 32.4 ms                                                     | 22.6 ms: 1.43x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.36 us: 1.41x faster                                                      |
| chaos                    | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                      |
| richards_super           | 52.2 ms                                                     | 37.4 ms: 1.40x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.8 us: 1.39x faster                                                      |
| float                    | 61.7 ms                                                     | 45.6 ms: 1.35x faster                                                      |
| raytrace                 | 273 ms                                                      | 205 ms: 1.33x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 64.4 ms: 1.33x faster                                                      |
| pycparser                | 930 ms                                                      | 706 ms: 1.32x faster                                                       |
| richards                 | 42.4 ms                                                     | 32.2 ms: 1.32x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                      |
| pyflate                  | 409 ms                                                      | 313 ms: 1.31x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 562 ms: 1.30x faster                                                       |
| deepcopy                 | 255 us                                                      | 197 us: 1.30x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.8 us: 1.29x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.54 ms: 1.26x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 7.28 ms: 1.26x faster                                                      |
| scimark_sor              | 106 ms                                                      | 84.7 ms: 1.25x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.1 ms: 1.22x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.5 ms: 1.22x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 63.8 ms: 1.21x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 152 us: 1.21x faster                                                       |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.4 ms: 1.18x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 228 us: 1.18x faster                                                       |
| regex_compile            | 106 ms                                                      | 91.4 ms: 1.16x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.4 ms: 1.15x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 55.7 ms: 1.12x faster                                                      |
| sympy_sum                | 107 ms                                                      | 96.7 ms: 1.11x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.0 ms: 1.10x faster                                                      |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 37.6 ms: 1.09x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.1 ms: 1.09x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 18.4 ms: 1.08x faster                                                      |
| thrift                   | 617 us                                                      | 577 us: 1.07x faster                                                       |
| pidigits                 | 149 ms                                                      | 139 ms: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.08 us: 1.06x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 91.7 ms: 1.06x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 561 ms: 1.05x faster                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.36 ms: 1.04x faster                                                      |
| sympy_str                | 194 ms                                                      | 187 ms: 1.04x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 44.8 ms: 1.01x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 40.3 ns: 1.02x slower                                                      |
| json                     | 3.14 ms                                                     | 3.19 ms: 1.02x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 68.2 ms: 1.02x slower                                                      |
| sympy_expand             | 314 ms                                                      | 325 ms: 1.03x slower                                                       |
| scimark_fft              | 187 ms                                                      | 200 ms: 1.07x slower                                                       |
| mako                     | 9.03 ms                                                     | 9.69 ms: 1.07x slower                                                      |
| nbody                    | 71.3 ms                                                     | 76.9 ms: 1.08x slower                                                      |
| logging_format           | 6.76 us                                                     | 7.30 us: 1.08x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.94 ms: 1.08x slower                                                      |
| unpickle                 | 9.09 us                                                     | 10.0 us: 1.10x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.88 us: 1.11x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 62.2 ms: 1.12x slower                                                      |
| fannkuch                 | 256 ms                                                      | 293 ms: 1.15x slower                                                       |
| bench_thread_pool        | 958 us                                                      | 1.10 ms: 1.15x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 88.1 ms: 1.16x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.17 us: 1.17x slower                                                      |
| async_generators         | 222 ms                                                      | 260 ms: 1.17x slower                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.50 sec: 1.18x slower                                                     |
| json_loads               | 14.0 us                                                     | 16.7 us: 1.19x slower                                                      |
| pickle                   | 6.85 us                                                     | 8.17 us: 1.19x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 21.2 us: 1.23x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.41 us: 1.24x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 79.5 ms: 1.28x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.1 ms: 1.29x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.08 ms: 1.34x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.30 ms: 1.35x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.74 sec: 1.43x slower                                                     |
| docutils                 | 1.92 sec                                                    | 2.91 sec: 1.51x slower                                                     |
| tomli_loads              | 1.67 sec                                                    | 2.58 sec: 1.54x slower                                                     |
| coverage                 | 39.0 ms                                                     | 68.2 ms: 1.75x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 368 ns: 3.89x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.10x faster                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.166x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown