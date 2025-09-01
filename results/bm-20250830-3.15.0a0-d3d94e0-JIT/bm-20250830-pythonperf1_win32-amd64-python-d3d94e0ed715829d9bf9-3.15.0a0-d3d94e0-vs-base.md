# Results vs. base

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.042x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                                                                                     | 217 ms: 1.01x faster                                                                                                           |
| sphinx         | 636 ms                                                                                                                     | 624 ms: 1.02x faster                                                                                                           |
| Geometric mean | (ref)                                                                                                                      | 1.01x faster                                                                                                                   |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|-------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none         | 174 ms                                                                                                                     | 169 ms: 1.03x faster                                                                                                           |
| async_tree_none_tg      | 171 ms                                                                                                                     | 167 ms: 1.03x faster                                                                                                           |
| async_tree_cpu_io_mixed | 326 ms                                                                                                                     | 330 ms: 1.01x slower                                                                                                           |
| asyncio_tcp_ssl         | 1.32 sec                                                                                                                   | 1.35 sec: 1.03x slower                                                                                                         |
| asyncio_tcp             | 446 ms                                                                                                                     | 467 ms: 1.05x slower                                                                                                           |
| async_generators        | 226 ms                                                                                                                     | 242 ms: 1.07x slower                                                                                                           |
| Geometric mean          | (ref)                                                                                                                      | 1.01x slower                                                                                                                   |

Benchmark hidden because not significant (7): async_tree_io_tg, coroutines, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                                                                                    | 55.8 ms: 1.17x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.05x faster                                                                                                                   |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 80.8 ms                                                                                                                    | 78.2 ms: 1.03x faster                                                                                                          |
| regex_effbot   | 1.52 ms                                                                                                                    | 1.53 ms: 1.01x slower                                                                                                          |
| regex_dna      | 116 ms                                                                                                                     | 117 ms: 1.01x slower                                                                                                           |
| regex_v8       | 13.3 ms                                                                                                                    | 13.8 ms: 1.03x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.00x slower                                                                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 140 us                                                                                                                     | 107 us: 1.31x faster                                                                                                           |
| tomli_loads          | 1.41 sec                                                                                                                   | 1.10 sec: 1.28x faster                                                                                                         |
| xml_etree_generate   | 56.9 ms                                                                                                                    | 49.1 ms: 1.16x faster                                                                                                          |
| xml_etree_process    | 39.8 ms                                                                                                                    | 34.9 ms: 1.14x faster                                                                                                          |
| pickle               | 8.12 us                                                                                                                    | 7.42 us: 1.09x faster                                                                                                          |
| pickle_pure_python   | 218 us                                                                                                                     | 201 us: 1.08x faster                                                                                                           |
| xml_etree_iterparse  | 64.7 ms                                                                                                                    | 61.1 ms: 1.06x faster                                                                                                          |
| unpickle_list        | 2.83 us                                                                                                                    | 2.72 us: 1.04x faster                                                                                                          |
| pickle_dict          | 19.7 us                                                                                                                    | 19.0 us: 1.03x faster                                                                                                          |
| xml_etree_parse      | 87.8 ms                                                                                                                    | 85.3 ms: 1.03x faster                                                                                                          |
| json_loads           | 14.3 us                                                                                                                    | 14.0 us: 1.02x faster                                                                                                          |
| json_dumps           | 5.45 ms                                                                                                                    | 5.36 ms: 1.02x faster                                                                                                          |
| pickle_list          | 3.32 us                                                                                                                    | 3.27 us: 1.01x faster                                                                                                          |
| Geometric mean       | (ref)                                                                                                                      | 1.09x faster                                                                                                                   |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.7 ms                                                                                                                    | 19.2 ms: 1.03x faster                                                                                                          |
| python_startup         | 25.8 ms                                                                                                                    | 25.5 ms: 1.01x faster                                                                                                          |
| Geometric mean         | (ref)                                                                                                                      | 1.02x faster                                                                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.79 ms                                                                                                                    | 5.34 ms: 1.27x faster                                                                                                          |
| django_template | 24.5 ms                                                                                                                    | 24.0 ms: 1.02x faster                                                                                                          |
| genshi_text     | 15.4 ms                                                                                                                    | 15.5 ms: 1.01x slower                                                                                                          |
| genshi_xml      | 33.9 ms                                                                                                                    | 34.6 ms: 1.02x slower                                                                                                          |
| Geometric mean  | (ref)                                                                                                                      | 1.06x faster                                                                                                                   |

All benchmarks:
===============

| Benchmark                | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|--------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| fannkuch                 | 267 ms                                                                                                                     | 201 ms: 1.33x faster                                                                                                           |
| unpickle_pure_python     | 140 us                                                                                                                     | 107 us: 1.31x faster                                                                                                           |
| tomli_loads              | 1.41 sec                                                                                                                   | 1.10 sec: 1.28x faster                                                                                                         |
| mako                     | 6.79 ms                                                                                                                    | 5.34 ms: 1.27x faster                                                                                                          |
| scimark_fft              | 181 ms                                                                                                                     | 147 ms: 1.23x faster                                                                                                           |
| pprint_pformat           | 1.03 sec                                                                                                                   | 868 ms: 1.19x faster                                                                                                           |
| pprint_safe_repr         | 506 ms                                                                                                                     | 429 ms: 1.18x faster                                                                                                           |
| nbody                    | 65.5 ms                                                                                                                    | 55.8 ms: 1.17x faster                                                                                                          |
| xml_etree_generate       | 56.9 ms                                                                                                                    | 49.1 ms: 1.16x faster                                                                                                          |
| pyflate                  | 298 ms                                                                                                                     | 257 ms: 1.16x faster                                                                                                           |
| bpe_tokeniser            | 2.90 sec                                                                                                                   | 2.52 sec: 1.15x faster                                                                                                         |
| scimark_sparse_mat_mult  | 2.58 ms                                                                                                                    | 2.25 ms: 1.15x faster                                                                                                          |
| xml_etree_process        | 39.8 ms                                                                                                                    | 34.9 ms: 1.14x faster                                                                                                          |
| telco                    | 4.16 ms                                                                                                                    | 3.75 ms: 1.11x faster                                                                                                          |
| pickle                   | 8.12 us                                                                                                                    | 7.42 us: 1.09x faster                                                                                                          |
| sqlglot_v2_parse         | 842 us                                                                                                                     | 772 us: 1.09x faster                                                                                                           |
| pickle_pure_python       | 218 us                                                                                                                     | 201 us: 1.08x faster                                                                                                           |
| k_core                   | 1.72 sec                                                                                                                   | 1.59 sec: 1.08x faster                                                                                                         |
| sqlglot_v2_transpile     | 1.04 ms                                                                                                                    | 968 us: 1.08x faster                                                                                                           |
| logging_silent           | 57.3 ns                                                                                                                    | 53.6 ns: 1.07x faster                                                                                                          |
| comprehensions           | 11.0 us                                                                                                                    | 10.4 us: 1.06x faster                                                                                                          |
| crypto_pyaes             | 47.4 ms                                                                                                                    | 44.6 ms: 1.06x faster                                                                                                          |
| xml_etree_iterparse      | 64.7 ms                                                                                                                    | 61.1 ms: 1.06x faster                                                                                                          |
| connected_components     | 333 ms                                                                                                                     | 316 ms: 1.06x faster                                                                                                           |
| richards                 | 28.4 ms                                                                                                                    | 27.0 ms: 1.05x faster                                                                                                          |
| spectral_norm            | 64.8 ms                                                                                                                    | 61.9 ms: 1.05x faster                                                                                                          |
| shortest_path            | 364 ms                                                                                                                     | 350 ms: 1.04x faster                                                                                                           |
| json                     | 2.99 ms                                                                                                                    | 2.88 ms: 1.04x faster                                                                                                          |
| unpickle_list            | 2.83 us                                                                                                                    | 2.72 us: 1.04x faster                                                                                                          |
| nqueens                  | 61.1 ms                                                                                                                    | 58.9 ms: 1.04x faster                                                                                                          |
| sqlite_synth             | 1.60 us                                                                                                                    | 1.55 us: 1.04x faster                                                                                                          |
| dulwich_log              | 40.1 ms                                                                                                                    | 38.7 ms: 1.04x faster                                                                                                          |
| pickle_dict              | 19.7 us                                                                                                                    | 19.0 us: 1.03x faster                                                                                                          |
| regex_compile            | 80.8 ms                                                                                                                    | 78.2 ms: 1.03x faster                                                                                                          |
| pycparser                | 711 ms                                                                                                                     | 688 ms: 1.03x faster                                                                                                           |
| logging_simple           | 6.10 us                                                                                                                    | 5.92 us: 1.03x faster                                                                                                          |
| mdp                      | 815 ms                                                                                                                     | 791 ms: 1.03x faster                                                                                                           |
| xml_etree_parse          | 87.8 ms                                                                                                                    | 85.3 ms: 1.03x faster                                                                                                          |
| sympy_sum                | 87.8 ms                                                                                                                    | 85.4 ms: 1.03x faster                                                                                                          |
| python_startup_no_site   | 19.7 ms                                                                                                                    | 19.2 ms: 1.03x faster                                                                                                          |
| async_tree_none          | 174 ms                                                                                                                     | 169 ms: 1.03x faster                                                                                                           |
| async_tree_none_tg       | 171 ms                                                                                                                     | 167 ms: 1.03x faster                                                                                                           |
| chaos                    | 41.0 ms                                                                                                                    | 40.0 ms: 1.02x faster                                                                                                          |
| scimark_monte_carlo      | 41.0 ms                                                                                                                    | 40.1 ms: 1.02x faster                                                                                                          |
| raytrace                 | 178 ms                                                                                                                     | 174 ms: 1.02x faster                                                                                                           |
| richards_super           | 31.4 ms                                                                                                                    | 30.7 ms: 1.02x faster                                                                                                          |
| typing_runtime_protocols | 105 us                                                                                                                     | 102 us: 1.02x faster                                                                                                           |
| json_loads               | 14.3 us                                                                                                                    | 14.0 us: 1.02x faster                                                                                                          |
| sphinx                   | 636 ms                                                                                                                     | 624 ms: 1.02x faster                                                                                                           |
| meteor_contest           | 72.6 ms                                                                                                                    | 71.2 ms: 1.02x faster                                                                                                          |
| create_gc_cycles         | 1.29 ms                                                                                                                    | 1.27 ms: 1.02x faster                                                                                                          |
| django_template          | 24.5 ms                                                                                                                    | 24.0 ms: 1.02x faster                                                                                                          |
| json_dumps               | 5.45 ms                                                                                                                    | 5.36 ms: 1.02x faster                                                                                                          |
| deltablue                | 2.23 ms                                                                                                                    | 2.20 ms: 1.02x faster                                                                                                          |
| deepcopy                 | 173 us                                                                                                                     | 171 us: 1.02x faster                                                                                                           |
| pickle_list              | 3.32 us                                                                                                                    | 3.27 us: 1.01x faster                                                                                                          |
| sympy_integrate          | 12.6 ms                                                                                                                    | 12.4 ms: 1.01x faster                                                                                                          |
| logging_format           | 6.47 us                                                                                                                    | 6.39 us: 1.01x faster                                                                                                          |
| pathlib                  | 29.8 ms                                                                                                                    | 29.5 ms: 1.01x faster                                                                                                          |
| sqlglot_v2_normalize     | 71.0 ms                                                                                                                    | 70.2 ms: 1.01x faster                                                                                                          |
| python_startup           | 25.8 ms                                                                                                                    | 25.5 ms: 1.01x faster                                                                                                          |
| 2to3                     | 218 ms                                                                                                                     | 217 ms: 1.01x faster                                                                                                           |
| bench_mp_pool            | 93.3 ms                                                                                                                    | 92.6 ms: 1.01x faster                                                                                                          |
| coverage                 | 49.7 ms                                                                                                                    | 49.4 ms: 1.01x faster                                                                                                          |
| genshi_text              | 15.4 ms                                                                                                                    | 15.5 ms: 1.01x slower                                                                                                          |
| generators               | 19.1 ms                                                                                                                    | 19.3 ms: 1.01x slower                                                                                                          |
| regex_effbot             | 1.52 ms                                                                                                                    | 1.53 ms: 1.01x slower                                                                                                          |
| regex_dna                | 116 ms                                                                                                                     | 117 ms: 1.01x slower                                                                                                           |
| async_tree_cpu_io_mixed  | 326 ms                                                                                                                     | 330 ms: 1.01x slower                                                                                                           |
| many_optionals           | 543 us                                                                                                                     | 553 us: 1.02x slower                                                                                                           |
| genshi_xml               | 33.9 ms                                                                                                                    | 34.6 ms: 1.02x slower                                                                                                          |
| scimark_lu               | 58.4 ms                                                                                                                    | 59.7 ms: 1.02x slower                                                                                                          |
| deepcopy_memo            | 19.5 us                                                                                                                    | 19.9 us: 1.02x slower                                                                                                          |
| asyncio_tcp_ssl          | 1.32 sec                                                                                                                   | 1.35 sec: 1.03x slower                                                                                                         |
| regex_v8                 | 13.3 ms                                                                                                                    | 13.8 ms: 1.03x slower                                                                                                          |
| asyncio_tcp              | 446 ms                                                                                                                     | 467 ms: 1.05x slower                                                                                                           |
| async_generators         | 226 ms                                                                                                                     | 242 ms: 1.07x slower                                                                                                           |
| unpack_sequence          | 33.0 ns                                                                                                                    | 36.0 ns: 1.09x slower                                                                                                          |
| Geometric mean           | (ref)                                                                                                                      | 1.04x faster                                                                                                                   |

Benchmark hidden because not significant (24): pylint, bench_thread_pool, sympy_str, deepcopy_reduce, async_tree_io_tg, subparsers, coroutines, docutils, scimark_sor, html5lib, go, asyncio_websockets, hexiom, float, pidigits, async_tree_cpu_io_mixed_tg, thrift, unpickle, async_tree_io, sympy_expand, async_tree_memoization_tg, async_tree_memoization, sqlglot_v2_optimize, gc_traversal

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown