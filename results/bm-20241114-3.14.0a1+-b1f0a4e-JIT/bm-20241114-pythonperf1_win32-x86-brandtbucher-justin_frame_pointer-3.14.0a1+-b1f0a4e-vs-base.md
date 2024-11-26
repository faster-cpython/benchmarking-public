# Results vs. base

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: windows-x86
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.034x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                                          | 298 ms: 1.02x slower                                                                  |
| docutils       | 2.14 sec                                                                        | 2.17 sec: 1.01x slower                                                                |
| html5lib       | 49.9 ms                                                                         | 47.6 ms: 1.05x faster                                                                 |
| sphinx         | 901 ms                                                                          | 914 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                                           | 1.00x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|--------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| asyncio_websockets | 365 ms                                                                          | 352 ms: 1.04x faster                                                                  |
| coroutines         | 16.5 ms                                                                         | 16.7 ms: 1.01x slower                                                                 |
| async_tree_io      | 547 ms                                                                          | 554 ms: 1.01x slower                                                                  |
| async_tree_none    | 245 ms                                                                          | 250 ms: 1.02x slower                                                                  |
| async_generators   | 330 ms                                                                          | 342 ms: 1.04x slower                                                                  |
| Geometric mean     | (ref)                                                                           | 1.01x slower                                                                          |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                                         | 59.5 ms: 1.07x slower                                                                 |
| nbody          | 98.5 ms                                                                         | 124 ms: 1.26x slower                                                                  |
| Geometric mean | (ref)                                                                           | 1.10x slower                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                                         | 15.9 ms: 1.00x slower                                                                 |
| regex_effbot   | 1.81 ms                                                                         | 1.83 ms: 1.01x slower                                                                 |
| regex_compile  | 121 ms                                                                          | 126 ms: 1.04x slower                                                                  |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 192 us                                                                          | 190 us: 1.01x faster                                                                  |
| xml_etree_iterparse  | 70.0 ms                                                                         | 70.7 ms: 1.01x slower                                                                 |
| json_loads           | 21.4 us                                                                         | 21.9 us: 1.02x slower                                                                 |
| json_dumps           | 8.80 ms                                                                         | 9.18 ms: 1.04x slower                                                                 |
| pickle_pure_python   | 301 us                                                                          | 315 us: 1.05x slower                                                                  |
| xml_etree_generate   | 71.8 ms                                                                         | 76.0 ms: 1.06x slower                                                                 |
| xml_etree_process    | 53.6 ms                                                                         | 58.0 ms: 1.08x slower                                                                 |
| tomli_loads          | 1.83 sec                                                                        | 1.98 sec: 1.09x slower                                                                |
| Geometric mean       | (ref)                                                                           | 1.04x slower                                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 26.8 ms                                                                         | 25.7 ms: 1.05x faster                                                                 |
| python_startup_no_site | 20.3 ms                                                                         | 19.6 ms: 1.03x faster                                                                 |
| Geometric mean         | (ref)                                                                           | 1.04x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| django_template | 36.3 ms                                                                         | 37.1 ms: 1.02x slower                                                                 |
| genshi_text     | 26.4 ms                                                                         | 27.3 ms: 1.03x slower                                                                 |
| genshi_xml      | 58.5 ms                                                                         | 61.2 ms: 1.05x slower                                                                 |
| mako            | 7.39 ms                                                                         | 7.83 ms: 1.06x slower                                                                 |
| Geometric mean  | (ref)                                                                           | 1.04x slower                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|--------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| richards_super           | 51.3 ms                                                                         | 48.8 ms: 1.05x faster                                                                 |
| html5lib                 | 49.9 ms                                                                         | 47.6 ms: 1.05x faster                                                                 |
| python_startup           | 26.8 ms                                                                         | 25.7 ms: 1.05x faster                                                                 |
| asyncio_websockets       | 365 ms                                                                          | 352 ms: 1.04x faster                                                                  |
| python_startup_no_site   | 20.3 ms                                                                         | 19.6 ms: 1.03x faster                                                                 |
| richards                 | 45.5 ms                                                                         | 45.0 ms: 1.01x faster                                                                 |
| unpickle_pure_python     | 192 us                                                                          | 190 us: 1.01x faster                                                                  |
| regex_v8                 | 15.8 ms                                                                         | 15.9 ms: 1.00x slower                                                                 |
| coverage                 | 52.1 ms                                                                         | 52.3 ms: 1.01x slower                                                                 |
| xml_etree_iterparse      | 70.0 ms                                                                         | 70.7 ms: 1.01x slower                                                                 |
| coroutines               | 16.5 ms                                                                         | 16.7 ms: 1.01x slower                                                                 |
| logging_format           | 8.85 us                                                                         | 8.95 us: 1.01x slower                                                                 |
| regex_effbot             | 1.81 ms                                                                         | 1.83 ms: 1.01x slower                                                                 |
| pathlib                  | 82.0 ms                                                                         | 83.1 ms: 1.01x slower                                                                 |
| async_tree_io            | 547 ms                                                                          | 554 ms: 1.01x slower                                                                  |
| sympy_integrate          | 19.5 ms                                                                         | 19.7 ms: 1.01x slower                                                                 |
| docutils                 | 2.14 sec                                                                        | 2.17 sec: 1.01x slower                                                                |
| sphinx                   | 901 ms                                                                          | 914 ms: 1.01x slower                                                                  |
| thrift                   | 779 us                                                                          | 791 us: 1.02x slower                                                                  |
| 2to3                     | 293 ms                                                                          | 298 ms: 1.02x slower                                                                  |
| json_loads               | 21.4 us                                                                         | 21.9 us: 1.02x slower                                                                 |
| k_core                   | 2.05 sec                                                                        | 2.09 sec: 1.02x slower                                                                |
| sympy_expand             | 422 ms                                                                          | 430 ms: 1.02x slower                                                                  |
| django_template          | 36.3 ms                                                                         | 37.1 ms: 1.02x slower                                                                 |
| sympy_sum                | 125 ms                                                                          | 128 ms: 1.02x slower                                                                  |
| async_tree_none          | 245 ms                                                                          | 250 ms: 1.02x slower                                                                  |
| pycparser                | 931 ms                                                                          | 951 ms: 1.02x slower                                                                  |
| go                       | 127 ms                                                                          | 130 ms: 1.02x slower                                                                  |
| mdp                      | 1.89 sec                                                                        | 1.93 sec: 1.02x slower                                                                |
| shortest_path            | 317 ms                                                                          | 326 ms: 1.03x slower                                                                  |
| sqlglot_normalize        | 115 ms                                                                          | 118 ms: 1.03x slower                                                                  |
| meteor_contest           | 90.4 ms                                                                         | 93.1 ms: 1.03x slower                                                                 |
| sympy_str                | 248 ms                                                                          | 256 ms: 1.03x slower                                                                  |
| connected_components     | 288 ms                                                                          | 297 ms: 1.03x slower                                                                  |
| sqlglot_transpile        | 1.53 ms                                                                         | 1.58 ms: 1.03x slower                                                                 |
| genshi_text              | 26.4 ms                                                                         | 27.3 ms: 1.03x slower                                                                 |
| async_generators         | 330 ms                                                                          | 342 ms: 1.04x slower                                                                  |
| regex_compile            | 121 ms                                                                          | 126 ms: 1.04x slower                                                                  |
| dulwich_log              | 49.3 ms                                                                         | 51.3 ms: 1.04x slower                                                                 |
| deltablue                | 3.29 ms                                                                         | 3.42 ms: 1.04x slower                                                                 |
| json_dumps               | 8.80 ms                                                                         | 9.18 ms: 1.04x slower                                                                 |
| sqlglot_parse            | 1.18 ms                                                                         | 1.23 ms: 1.05x slower                                                                 |
| genshi_xml               | 58.5 ms                                                                         | 61.2 ms: 1.05x slower                                                                 |
| pickle_pure_python       | 301 us                                                                          | 315 us: 1.05x slower                                                                  |
| sqlglot_optimize         | 56.6 ms                                                                         | 59.3 ms: 1.05x slower                                                                 |
| json                     | 4.40 ms                                                                         | 4.61 ms: 1.05x slower                                                                 |
| bpe_tokeniser            | 3.96 sec                                                                        | 4.17 sec: 1.05x slower                                                                |
| pyflate                  | 398 ms                                                                          | 419 ms: 1.05x slower                                                                  |
| deepcopy_reduce          | 2.76 us                                                                         | 2.91 us: 1.05x slower                                                                 |
| typing_runtime_protocols | 167 us                                                                          | 176 us: 1.06x slower                                                                  |
| pprint_safe_repr         | 743 ms                                                                          | 787 ms: 1.06x slower                                                                  |
| mako                     | 7.39 ms                                                                         | 7.83 ms: 1.06x slower                                                                 |
| xml_etree_generate       | 71.8 ms                                                                         | 76.0 ms: 1.06x slower                                                                 |
| deepcopy                 | 274 us                                                                          | 292 us: 1.06x slower                                                                  |
| generators               | 35.8 ms                                                                         | 38.2 ms: 1.07x slower                                                                 |
| float                    | 55.8 ms                                                                         | 59.5 ms: 1.07x slower                                                                 |
| comprehensions           | 18.4 us                                                                         | 19.7 us: 1.07x slower                                                                 |
| scimark_lu               | 69.7 ms                                                                         | 74.5 ms: 1.07x slower                                                                 |
| nqueens                  | 97.0 ms                                                                         | 104 ms: 1.07x slower                                                                  |
| pprint_pformat           | 1.50 sec                                                                        | 1.61 sec: 1.08x slower                                                                |
| logging_silent           | 76.9 ns                                                                         | 83.2 ns: 1.08x slower                                                                 |
| xml_etree_process        | 53.6 ms                                                                         | 58.0 ms: 1.08x slower                                                                 |
| hexiom                   | 7.19 ms                                                                         | 7.80 ms: 1.08x slower                                                                 |
| tomli_loads              | 1.83 sec                                                                        | 1.98 sec: 1.09x slower                                                                |
| scimark_monte_carlo      | 62.1 ms                                                                         | 67.5 ms: 1.09x slower                                                                 |
| deepcopy_memo            | 23.8 us                                                                         | 25.9 us: 1.09x slower                                                                 |
| telco                    | 7.08 ms                                                                         | 7.71 ms: 1.09x slower                                                                 |
| scimark_sparse_mat_mult  | 3.22 ms                                                                         | 3.51 ms: 1.09x slower                                                                 |
| crypto_pyaes             | 67.1 ms                                                                         | 73.4 ms: 1.09x slower                                                                 |
| scimark_sor              | 99.7 ms                                                                         | 112 ms: 1.12x slower                                                                  |
| chaos                    | 63.3 ms                                                                         | 71.7 ms: 1.13x slower                                                                 |
| fannkuch                 | 326 ms                                                                          | 372 ms: 1.14x slower                                                                  |
| spectral_norm            | 79.2 ms                                                                         | 91.1 ms: 1.15x slower                                                                 |
| scimark_fft              | 247 ms                                                                          | 288 ms: 1.16x slower                                                                  |
| nbody                    | 98.5 ms                                                                         | 124 ms: 1.26x slower                                                                  |
| Geometric mean           | (ref)                                                                           | 1.04x slower                                                                          |

Benchmark hidden because not significant (19): create_gc_cycles, bench_mp_pool, subparsers, gc_traversal, regex_dna, async_tree_none_tg, async_tree_memoization_tg, sqlite_synth, logging_simple, async_tree_cpu_io_mixed_tg, pidigits, raytrace, xml_etree_parse, bench_thread_pool, many_optionals, async_tree_io_tg, pylint, async_tree_cpu_io_mixed, async_tree_memoization

- Geometric mean (including insignificant results): 1.034x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown