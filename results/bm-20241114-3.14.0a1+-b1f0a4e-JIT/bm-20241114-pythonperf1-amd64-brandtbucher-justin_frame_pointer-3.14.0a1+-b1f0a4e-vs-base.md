# Results vs. base

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: windows-amd64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.023x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 243 ms                                                                      | 248 ms: 1.02x slower                                                              |
| docutils       | 1.89 sec                                                                    | 1.90 sec: 1.00x slower                                                            |
| html5lib       | 39.4 ms                                                                     | 39.1 ms: 1.01x faster                                                             |
| sphinx         | 760 ms                                                                      | 772 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_websockets     | 317 ms                                                                      | 305 ms: 1.04x faster                                                              |
| async_generators       | 267 ms                                                                      | 263 ms: 1.02x faster                                                              |
| async_tree_io_tg       | 574 ms                                                                      | 587 ms: 1.02x slower                                                              |
| async_tree_none_tg     | 204 ms                                                                      | 209 ms: 1.02x slower                                                              |
| async_tree_io          | 517 ms                                                                      | 532 ms: 1.03x slower                                                              |
| async_tree_memoization | 253 ms                                                                      | 262 ms: 1.03x slower                                                              |
| async_tree_none        | 204 ms                                                                      | 212 ms: 1.04x slower                                                              |
| coroutines             | 13.4 ms                                                                     | 14.1 ms: 1.05x slower                                                             |
| Geometric mean         | (ref)                                                                       | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 147 ms                                                                      | 148 ms: 1.00x slower                                                              |
| float          | 47.1 ms                                                                     | 48.4 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 91.2 ms                                                                     | 93.3 ms: 1.02x slower                                                             |
| regex_effbot   | 1.55 ms                                                                     | 1.59 ms: 1.03x slower                                                             |
| regex_dna      | 116 ms                                                                      | 121 ms: 1.05x slower                                                              |
| regex_v8       | 14.5 ms                                                                     | 15.4 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                                       | 1.04x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                                     | 14.3 us: 1.01x slower                                                             |
| xml_etree_parse      | 92.8 ms                                                                     | 93.9 ms: 1.01x slower                                                             |
| tomli_loads          | 1.28 sec                                                                    | 1.30 sec: 1.02x slower                                                            |
| xml_etree_iterparse  | 62.0 ms                                                                     | 63.0 ms: 1.02x slower                                                             |
| xml_etree_generate   | 50.5 ms                                                                     | 51.8 ms: 1.03x slower                                                             |
| pickle_pure_python   | 207 us                                                                      | 214 us: 1.04x slower                                                              |
| unpickle_pure_python | 144 us                                                                      | 149 us: 1.04x slower                                                              |
| xml_etree_process    | 35.6 ms                                                                     | 37.1 ms: 1.04x slower                                                             |
| Geometric mean       | (ref)                                                                       | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 17.6 ms                                                                     | 18.0 ms: 1.02x slower                                                             |
| Geometric mean         | (ref)                                                                       | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 27.3 ms                                                                     | 26.9 ms: 1.01x faster                                                             |
| genshi_xml      | 46.8 ms                                                                     | 46.4 ms: 1.01x faster                                                             |
| mako            | 5.06 ms                                                                     | 5.44 ms: 1.08x slower                                                             |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|--------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_websockets       | 317 ms                                                                      | 305 ms: 1.04x faster                                                              |
| async_generators         | 267 ms                                                                      | 263 ms: 1.02x faster                                                              |
| django_template          | 27.3 ms                                                                     | 26.9 ms: 1.01x faster                                                             |
| genshi_xml               | 46.8 ms                                                                     | 46.4 ms: 1.01x faster                                                             |
| html5lib                 | 39.4 ms                                                                     | 39.1 ms: 1.01x faster                                                             |
| mdp                      | 1.54 sec                                                                    | 1.53 sec: 1.00x faster                                                            |
| fannkuch                 | 244 ms                                                                      | 243 ms: 1.00x faster                                                              |
| docutils                 | 1.89 sec                                                                    | 1.90 sec: 1.00x slower                                                            |
| pidigits                 | 147 ms                                                                      | 148 ms: 1.00x slower                                                              |
| sqlite_synth             | 1.59 us                                                                     | 1.59 us: 1.00x slower                                                             |
| bench_mp_pool            | 87.1 ms                                                                     | 87.6 ms: 1.01x slower                                                             |
| many_optionals           | 494 us                                                                      | 497 us: 1.01x slower                                                              |
| richards_super           | 38.6 ms                                                                     | 39.0 ms: 1.01x slower                                                             |
| json_loads               | 14.2 us                                                                     | 14.3 us: 1.01x slower                                                             |
| coverage                 | 46.1 ms                                                                     | 46.5 ms: 1.01x slower                                                             |
| xml_etree_parse          | 92.8 ms                                                                     | 93.9 ms: 1.01x slower                                                             |
| k_core                   | 2.41 sec                                                                    | 2.44 sec: 1.01x slower                                                            |
| sqlglot_transpile        | 1.18 ms                                                                     | 1.20 ms: 1.01x slower                                                             |
| richards                 | 34.5 ms                                                                     | 35.0 ms: 1.01x slower                                                             |
| connected_components     | 312 ms                                                                      | 316 ms: 1.01x slower                                                              |
| sphinx                   | 760 ms                                                                      | 772 ms: 1.02x slower                                                              |
| tomli_loads              | 1.28 sec                                                                    | 1.30 sec: 1.02x slower                                                            |
| xml_etree_iterparse      | 62.0 ms                                                                     | 63.0 ms: 1.02x slower                                                             |
| typing_runtime_protocols | 113 us                                                                      | 115 us: 1.02x slower                                                              |
| 2to3                     | 243 ms                                                                      | 248 ms: 1.02x slower                                                              |
| pycparser                | 720 ms                                                                      | 734 ms: 1.02x slower                                                              |
| python_startup_no_site   | 17.6 ms                                                                     | 18.0 ms: 1.02x slower                                                             |
| sympy_sum                | 102 ms                                                                      | 104 ms: 1.02x slower                                                              |
| async_tree_io_tg         | 574 ms                                                                      | 587 ms: 1.02x slower                                                              |
| sympy_integrate          | 15.7 ms                                                                     | 16.0 ms: 1.02x slower                                                             |
| logging_simple           | 6.11 us                                                                     | 6.25 us: 1.02x slower                                                             |
| regex_compile            | 91.2 ms                                                                     | 93.3 ms: 1.02x slower                                                             |
| sympy_expand             | 323 ms                                                                      | 331 ms: 1.02x slower                                                              |
| logging_format           | 6.52 us                                                                     | 6.68 us: 1.02x slower                                                             |
| subparsers               | 15.8 ms                                                                     | 16.2 ms: 1.02x slower                                                             |
| async_tree_none_tg       | 204 ms                                                                      | 209 ms: 1.02x slower                                                              |
| regex_effbot             | 1.55 ms                                                                     | 1.59 ms: 1.03x slower                                                             |
| scimark_sparse_mat_mult  | 2.25 ms                                                                     | 2.31 ms: 1.03x slower                                                             |
| bpe_tokeniser            | 2.68 sec                                                                    | 2.75 sec: 1.03x slower                                                            |
| xml_etree_generate       | 50.5 ms                                                                     | 51.8 ms: 1.03x slower                                                             |
| sqlglot_optimize         | 42.5 ms                                                                     | 43.6 ms: 1.03x slower                                                             |
| float                    | 47.1 ms                                                                     | 48.4 ms: 1.03x slower                                                             |
| sympy_str                | 190 ms                                                                      | 196 ms: 1.03x slower                                                              |
| spectral_norm            | 54.1 ms                                                                     | 55.7 ms: 1.03x slower                                                             |
| async_tree_io            | 517 ms                                                                      | 532 ms: 1.03x slower                                                              |
| sqlglot_parse            | 888 us                                                                      | 915 us: 1.03x slower                                                              |
| deepcopy                 | 191 us                                                                      | 197 us: 1.03x slower                                                              |
| async_tree_memoization   | 253 ms                                                                      | 262 ms: 1.03x slower                                                              |
| sqlglot_normalize        | 207 ms                                                                      | 214 ms: 1.03x slower                                                              |
| deltablue                | 2.35 ms                                                                     | 2.43 ms: 1.03x slower                                                             |
| pickle_pure_python       | 207 us                                                                      | 214 us: 1.04x slower                                                              |
| telco                    | 4.46 ms                                                                     | 4.62 ms: 1.04x slower                                                             |
| unpickle_pure_python     | 144 us                                                                      | 149 us: 1.04x slower                                                              |
| async_tree_none          | 204 ms                                                                      | 212 ms: 1.04x slower                                                              |
| chaos                    | 40.9 ms                                                                     | 42.6 ms: 1.04x slower                                                             |
| xml_etree_process        | 35.6 ms                                                                     | 37.1 ms: 1.04x slower                                                             |
| pyflate                  | 303 ms                                                                      | 317 ms: 1.05x slower                                                              |
| regex_dna                | 116 ms                                                                      | 121 ms: 1.05x slower                                                              |
| raytrace                 | 214 ms                                                                      | 225 ms: 1.05x slower                                                              |
| crypto_pyaes             | 40.3 ms                                                                     | 42.3 ms: 1.05x slower                                                             |
| deepcopy_memo            | 16.7 us                                                                     | 17.6 us: 1.05x slower                                                             |
| pprint_safe_repr         | 455 ms                                                                      | 478 ms: 1.05x slower                                                              |
| go                       | 91.2 ms                                                                     | 95.9 ms: 1.05x slower                                                             |
| coroutines               | 13.4 ms                                                                     | 14.1 ms: 1.05x slower                                                             |
| scimark_monte_carlo      | 37.0 ms                                                                     | 39.2 ms: 1.06x slower                                                             |
| scimark_fft              | 157 ms                                                                      | 166 ms: 1.06x slower                                                              |
| nqueens                  | 63.2 ms                                                                     | 67.0 ms: 1.06x slower                                                             |
| deepcopy_reduce          | 1.87 us                                                                     | 1.98 us: 1.06x slower                                                             |
| pprint_pformat           | 922 ms                                                                      | 979 ms: 1.06x slower                                                              |
| hexiom                   | 5.20 ms                                                                     | 5.53 ms: 1.06x slower                                                             |
| regex_v8                 | 14.5 ms                                                                     | 15.4 ms: 1.06x slower                                                             |
| mako                     | 5.06 ms                                                                     | 5.44 ms: 1.08x slower                                                             |
| logging_silent           | 55.0 ns                                                                     | 59.2 ns: 1.08x slower                                                             |
| comprehensions           | 11.8 us                                                                     | 12.7 us: 1.08x slower                                                             |
| scimark_sor              | 63.3 ms                                                                     | 68.9 ms: 1.09x slower                                                             |
| scimark_lu               | 51.8 ms                                                                     | 57.4 ms: 1.11x slower                                                             |
| generators               | 22.5 ms                                                                     | 25.3 ms: 1.12x slower                                                             |
| Geometric mean           | (ref)                                                                       | 1.02x slower                                                                      |

Benchmark hidden because not significant (17): create_gc_cycles, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, gc_traversal, json_dumps, json, python_startup, thrift, dulwich_log, pathlib, shortest_path, meteor_contest, bench_thread_pool, nbody, genshi_text, async_tree_memoization_tg, pylint

- Geometric mean (including insignificant results): 1.023x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown