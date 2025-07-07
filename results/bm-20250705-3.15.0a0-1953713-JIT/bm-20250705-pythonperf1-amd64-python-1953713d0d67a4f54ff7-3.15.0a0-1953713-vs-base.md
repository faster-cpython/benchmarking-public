# Results vs. base

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.030x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json | results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 220 ms                                                                                                               | 218 ms: 1.01x faster                                                                                                     |
| docutils       | 1.61 sec                                                                                                             | 1.65 sec: 1.02x slower                                                                                                   |
| html5lib       | 38.7 ms                                                                                                              | 38.3 ms: 1.01x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.00x slower                                                                                                             |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json | results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets        | 164 ms                                                                                                               | 157 ms: 1.05x faster                                                                                                     |
| async_tree_none_tg        | 168 ms                                                                                                               | 165 ms: 1.01x faster                                                                                                     |
| async_tree_none           | 169 ms                                                                                                               | 168 ms: 1.01x faster                                                                                                     |
| coroutines                | 14.3 ms                                                                                                              | 14.4 ms: 1.01x slower                                                                                                    |
| async_tree_memoization_tg | 208 ms                                                                                                               | 211 ms: 1.01x slower                                                                                                     |
| async_generators          | 233 ms                                                                                                               | 244 ms: 1.05x slower                                                                                                     |
| asyncio_tcp_ssl           | 1.33 sec                                                                                                             | 1.44 sec: 1.08x slower                                                                                                   |
| asyncio_tcp               | 449 ms                                                                                                               | 528 ms: 1.18x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json | results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 64.3 ms                                                                                                              | 52.3 ms: 1.23x faster                                                                                                    |
| float          | 43.9 ms                                                                                                              | 42.8 ms: 1.03x faster                                                                                                    |
| pidigits       | 145 ms                                                                                                               | 146 ms: 1.01x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.08x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json | results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 14.5 ms                                                                                                              | 14.2 ms: 1.02x faster                                                                                                    |
| regex_compile  | 80.2 ms                                                                                                              | 78.6 ms: 1.02x faster                                                                                                    |
| regex_dna      | 121 ms                                                                                                               | 119 ms: 1.02x faster                                                                                                     |
| regex_effbot   | 1.57 ms                                                                                                              | 1.56 ms: 1.01x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json | results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.41 sec                                                                                                             | 1.11 sec: 1.27x faster                                                                                                   |
| unpickle_pure_python | 134 us                                                                                                               | 106 us: 1.26x faster                                                                                                     |
| xml_etree_generate   | 56.5 ms                                                                                                              | 50.3 ms: 1.12x faster                                                                                                    |
| xml_etree_process    | 38.9 ms                                                                                                              | 35.2 ms: 1.11x faster                                                                                                    |
| pickle               | 7.99 us                                                                                                              | 7.55 us: 1.06x faster                                                                                                    |
| pickle_pure_python   | 213 us                                                                                                               | 203 us: 1.05x faster                                                                                                     |
| json_dumps           | 6.41 ms                                                                                                              | 6.11 ms: 1.05x faster                                                                                                    |
| xml_etree_iterparse  | 64.7 ms                                                                                                              | 62.8 ms: 1.03x faster                                                                                                    |
| xml_etree_parse      | 89.1 ms                                                                                                              | 86.8 ms: 1.03x faster                                                                                                    |
| pickle_list          | 3.33 us                                                                                                              | 3.30 us: 1.01x faster                                                                                                    |
| pickle_dict          | 19.5 us                                                                                                              | 19.3 us: 1.01x faster                                                                                                    |
| json_loads           | 14.2 us                                                                                                              | 14.4 us: 1.01x slower                                                                                                    |
| unpickle_list        | 2.76 us                                                                                                              | 2.83 us: 1.02x slower                                                                                                    |
| unpickle             | 8.47 us                                                                                                              | 8.73 us: 1.03x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.06x faster                                                                                                             |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json | results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.85 ms                                                                                                              | 5.44 ms: 1.26x faster                                                                                                    |
| genshi_text     | 15.6 ms                                                                                                              | 15.5 ms: 1.01x faster                                                                                                    |
| django_template | 23.7 ms                                                                                                              | 24.4 ms: 1.03x slower                                                                                                    |
| genshi_xml      | 33.8 ms                                                                                                              | 34.8 ms: 1.03x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.05x faster                                                                                                             |

All benchmarks:
===============

| Benchmark                 | results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json | results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads               | 1.41 sec                                                                                                             | 1.11 sec: 1.27x faster                                                                                                   |
| unpickle_pure_python      | 134 us                                                                                                               | 106 us: 1.26x faster                                                                                                     |
| mako                      | 6.85 ms                                                                                                              | 5.44 ms: 1.26x faster                                                                                                    |
| nbody                     | 64.3 ms                                                                                                              | 52.3 ms: 1.23x faster                                                                                                    |
| fannkuch                  | 270 ms                                                                                                               | 224 ms: 1.21x faster                                                                                                     |
| scimark_fft               | 180 ms                                                                                                               | 151 ms: 1.19x faster                                                                                                     |
| pyflate                   | 292 ms                                                                                                               | 252 ms: 1.16x faster                                                                                                     |
| bpe_tokeniser             | 2.97 sec                                                                                                             | 2.61 sec: 1.14x faster                                                                                                   |
| xml_etree_generate        | 56.5 ms                                                                                                              | 50.3 ms: 1.12x faster                                                                                                    |
| xml_etree_process         | 38.9 ms                                                                                                              | 35.2 ms: 1.11x faster                                                                                                    |
| pprint_safe_repr          | 493 ms                                                                                                               | 449 ms: 1.10x faster                                                                                                     |
| scimark_sparse_mat_mult   | 2.49 ms                                                                                                              | 2.27 ms: 1.10x faster                                                                                                    |
| pprint_pformat            | 1.01 sec                                                                                                             | 927 ms: 1.09x faster                                                                                                     |
| telco                     | 4.54 ms                                                                                                              | 4.25 ms: 1.07x faster                                                                                                    |
| k_core                    | 1.71 sec                                                                                                             | 1.61 sec: 1.06x faster                                                                                                   |
| pickle                    | 7.99 us                                                                                                              | 7.55 us: 1.06x faster                                                                                                    |
| sqlglot_v2_parse          | 825 us                                                                                                               | 780 us: 1.06x faster                                                                                                     |
| pickle_pure_python        | 213 us                                                                                                               | 203 us: 1.05x faster                                                                                                     |
| deltablue                 | 2.25 ms                                                                                                              | 2.13 ms: 1.05x faster                                                                                                    |
| json_dumps                | 6.41 ms                                                                                                              | 6.11 ms: 1.05x faster                                                                                                    |
| asyncio_websockets        | 164 ms                                                                                                               | 157 ms: 1.05x faster                                                                                                     |
| sqlglot_v2_transpile      | 1.03 ms                                                                                                              | 988 us: 1.04x faster                                                                                                     |
| crypto_pyaes              | 48.2 ms                                                                                                              | 46.3 ms: 1.04x faster                                                                                                    |
| go                        | 77.7 ms                                                                                                              | 75.0 ms: 1.04x faster                                                                                                    |
| comprehensions            | 10.9 us                                                                                                              | 10.5 us: 1.03x faster                                                                                                    |
| nqueens                   | 61.5 ms                                                                                                              | 59.6 ms: 1.03x faster                                                                                                    |
| meteor_contest            | 73.2 ms                                                                                                              | 71.0 ms: 1.03x faster                                                                                                    |
| xml_etree_iterparse       | 64.7 ms                                                                                                              | 62.8 ms: 1.03x faster                                                                                                    |
| chaos                     | 40.7 ms                                                                                                              | 39.5 ms: 1.03x faster                                                                                                    |
| connected_components      | 334 ms                                                                                                               | 324 ms: 1.03x faster                                                                                                     |
| spectral_norm             | 63.9 ms                                                                                                              | 62.1 ms: 1.03x faster                                                                                                    |
| scimark_sor               | 77.4 ms                                                                                                              | 75.2 ms: 1.03x faster                                                                                                    |
| xml_etree_parse           | 89.1 ms                                                                                                              | 86.8 ms: 1.03x faster                                                                                                    |
| pycparser                 | 714 ms                                                                                                               | 696 ms: 1.03x faster                                                                                                     |
| float                     | 43.9 ms                                                                                                              | 42.8 ms: 1.03x faster                                                                                                    |
| mdp                       | 817 ms                                                                                                               | 798 ms: 1.02x faster                                                                                                     |
| hexiom                    | 4.16 ms                                                                                                              | 4.06 ms: 1.02x faster                                                                                                    |
| logging_silent            | 55.5 ns                                                                                                              | 54.2 ns: 1.02x faster                                                                                                    |
| logging_simple            | 6.26 us                                                                                                              | 6.12 us: 1.02x faster                                                                                                    |
| regex_v8                  | 14.5 ms                                                                                                              | 14.2 ms: 1.02x faster                                                                                                    |
| shortest_path             | 364 ms                                                                                                               | 356 ms: 1.02x faster                                                                                                     |
| richards                  | 27.0 ms                                                                                                              | 26.4 ms: 1.02x faster                                                                                                    |
| regex_compile             | 80.2 ms                                                                                                              | 78.6 ms: 1.02x faster                                                                                                    |
| logging_format            | 6.71 us                                                                                                              | 6.61 us: 1.02x faster                                                                                                    |
| regex_dna                 | 121 ms                                                                                                               | 119 ms: 1.02x faster                                                                                                     |
| richards_super            | 30.8 ms                                                                                                              | 30.3 ms: 1.02x faster                                                                                                    |
| thrift                    | 493 us                                                                                                               | 486 us: 1.01x faster                                                                                                     |
| deepcopy_reduce           | 1.83 us                                                                                                              | 1.80 us: 1.01x faster                                                                                                    |
| async_tree_none_tg        | 168 ms                                                                                                               | 165 ms: 1.01x faster                                                                                                     |
| regex_effbot              | 1.57 ms                                                                                                              | 1.56 ms: 1.01x faster                                                                                                    |
| html5lib                  | 38.7 ms                                                                                                              | 38.3 ms: 1.01x faster                                                                                                    |
| async_tree_none           | 169 ms                                                                                                               | 168 ms: 1.01x faster                                                                                                     |
| pickle_list               | 3.33 us                                                                                                              | 3.30 us: 1.01x faster                                                                                                    |
| pickle_dict               | 19.5 us                                                                                                              | 19.3 us: 1.01x faster                                                                                                    |
| 2to3                      | 220 ms                                                                                                               | 218 ms: 1.01x faster                                                                                                     |
| genshi_text               | 15.6 ms                                                                                                              | 15.5 ms: 1.01x faster                                                                                                    |
| deepcopy                  | 169 us                                                                                                               | 168 us: 1.01x faster                                                                                                     |
| raytrace                  | 178 ms                                                                                                               | 177 ms: 1.00x faster                                                                                                     |
| generators                | 19.4 ms                                                                                                              | 19.5 ms: 1.01x slower                                                                                                    |
| coroutines                | 14.3 ms                                                                                                              | 14.4 ms: 1.01x slower                                                                                                    |
| sqlglot_v2_normalize      | 70.2 ms                                                                                                              | 70.7 ms: 1.01x slower                                                                                                    |
| sympy_str                 | 168 ms                                                                                                               | 169 ms: 1.01x slower                                                                                                     |
| dulwich_log               | 40.6 ms                                                                                                              | 40.8 ms: 1.01x slower                                                                                                    |
| pathlib                   | 31.6 ms                                                                                                              | 31.9 ms: 1.01x slower                                                                                                    |
| pidigits                  | 145 ms                                                                                                               | 146 ms: 1.01x slower                                                                                                     |
| sqlglot_v2_optimize       | 33.9 ms                                                                                                              | 34.2 ms: 1.01x slower                                                                                                    |
| async_tree_memoization_tg | 208 ms                                                                                                               | 211 ms: 1.01x slower                                                                                                     |
| scimark_monte_carlo       | 40.8 ms                                                                                                              | 41.3 ms: 1.01x slower                                                                                                    |
| json_loads                | 14.2 us                                                                                                              | 14.4 us: 1.01x slower                                                                                                    |
| coverage                  | 50.7 ms                                                                                                              | 51.6 ms: 1.02x slower                                                                                                    |
| sympy_integrate           | 12.4 ms                                                                                                              | 12.6 ms: 1.02x slower                                                                                                    |
| unpickle_list             | 2.76 us                                                                                                              | 2.83 us: 1.02x slower                                                                                                    |
| subparsers                | 16.6 ms                                                                                                              | 17.0 ms: 1.02x slower                                                                                                    |
| sympy_expand              | 286 ms                                                                                                               | 292 ms: 1.02x slower                                                                                                     |
| deepcopy_memo             | 18.5 us                                                                                                              | 18.9 us: 1.02x slower                                                                                                    |
| docutils                  | 1.61 sec                                                                                                             | 1.65 sec: 1.02x slower                                                                                                   |
| django_template           | 23.7 ms                                                                                                              | 24.4 ms: 1.03x slower                                                                                                    |
| genshi_xml                | 33.8 ms                                                                                                              | 34.8 ms: 1.03x slower                                                                                                    |
| unpickle                  | 8.47 us                                                                                                              | 8.73 us: 1.03x slower                                                                                                    |
| many_optionals            | 429 us                                                                                                               | 444 us: 1.03x slower                                                                                                     |
| async_generators          | 233 ms                                                                                                               | 244 ms: 1.05x slower                                                                                                     |
| sqlite_synth              | 1.58 us                                                                                                              | 1.65 us: 1.05x slower                                                                                                    |
| scimark_lu                | 57.8 ms                                                                                                              | 60.7 ms: 1.05x slower                                                                                                    |
| json                      | 2.93 ms                                                                                                              | 3.11 ms: 1.06x slower                                                                                                    |
| asyncio_tcp_ssl           | 1.33 sec                                                                                                             | 1.44 sec: 1.08x slower                                                                                                   |
| asyncio_tcp               | 449 ms                                                                                                               | 528 ms: 1.18x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmark hidden because not significant (16): async_tree_io_tg, async_tree_memoization, python_startup, async_tree_cpu_io_mixed_tg, unpack_sequence, bench_mp_pool, async_tree_cpu_io_mixed, sympy_sum, create_gc_cycles, python_startup_no_site, typing_runtime_protocols, bench_thread_pool, sphinx, async_tree_io, pylint, gc_traversal

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown