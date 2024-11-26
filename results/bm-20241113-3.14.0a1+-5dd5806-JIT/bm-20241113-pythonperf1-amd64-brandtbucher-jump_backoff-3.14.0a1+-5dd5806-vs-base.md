# Results vs. base

- fork: brandtbucher
- ref: jump_backoff
- machine: windows-amd64
- commit hash: 5dd5806
- commit date: 2024-11-13
- overall geometric mean: 1.012x faster
- HPT reliability: 97.62%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 245 ms                                                                      | 229 ms: 1.07x faster                                                      |
| docutils       | 1.89 sec                                                                    | 1.84 sec: 1.03x faster                                                    |
| sphinx         | 763 ms                                                                      | 737 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                              |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg     | 219 ms                                                                      | 205 ms: 1.07x faster                                                      |
| asyncio_websockets     | 311 ms                                                                      | 292 ms: 1.06x faster                                                      |
| async_tree_io          | 553 ms                                                                      | 544 ms: 1.02x faster                                                      |
| async_tree_none        | 209 ms                                                                      | 214 ms: 1.03x slower                                                      |
| async_tree_memoization | 262 ms                                                                      | 276 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                              |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_generators, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 147 ms                                                                      | 147 ms: 1.01x slower                                                      |
| nbody          | 52.8 ms                                                                     | 56.7 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 90.2 ms                                                                     | 87.6 ms: 1.03x faster                                                     |
| regex_effbot   | 1.54 ms                                                                     | 1.60 ms: 1.03x slower                                                     |
| regex_dna      | 116 ms                                                                      | 121 ms: 1.05x slower                                                      |
| regex_v8       | 14.6 ms                                                                     | 15.7 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 147 us                                                                      | 109 us: 1.35x faster                                                      |
| json_dumps           | 6.38 ms                                                                     | 6.20 ms: 1.03x faster                                                     |
| xml_etree_generate   | 51.0 ms                                                                     | 49.7 ms: 1.03x faster                                                     |
| xml_etree_process    | 36.3 ms                                                                     | 35.5 ms: 1.02x faster                                                     |
| tomli_loads          | 1.27 sec                                                                    | 1.26 sec: 1.01x faster                                                    |
| xml_etree_parse      | 92.7 ms                                                                     | 93.3 ms: 1.01x slower                                                     |
| json_loads           | 14.3 us                                                                     | 14.7 us: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                                       | 1.04x faster                                                              |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 17.7 ms                                                                     | 18.0 ms: 1.02x slower                                                     |
| python_startup         | 23.3 ms                                                                     | 24.0 ms: 1.03x slower                                                     |
| Geometric mean         | (ref)                                                                       | 1.02x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml     | 46.0 ms                                                                     | 44.0 ms: 1.05x faster                                                     |
| genshi_text    | 19.2 ms                                                                     | 18.4 ms: 1.04x faster                                                     |
| mako           | 5.18 ms                                                                     | 5.12 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python     | 147 us                                                                      | 109 us: 1.35x faster                                                      |
| pylint                   | 277 ms                                                                      | 244 ms: 1.13x faster                                                      |
| sympy_integrate          | 15.6 ms                                                                     | 13.9 ms: 1.12x faster                                                     |
| sqlglot_optimize         | 42.9 ms                                                                     | 38.7 ms: 1.11x faster                                                     |
| sympy_sum                | 102 ms                                                                      | 94.9 ms: 1.07x faster                                                     |
| async_tree_none_tg       | 219 ms                                                                      | 205 ms: 1.07x faster                                                      |
| 2to3                     | 245 ms                                                                      | 229 ms: 1.07x faster                                                      |
| asyncio_websockets       | 311 ms                                                                      | 292 ms: 1.06x faster                                                      |
| pyflate                  | 313 ms                                                                      | 296 ms: 1.06x faster                                                      |
| sqlglot_transpile        | 1.18 ms                                                                     | 1.13 ms: 1.05x faster                                                     |
| raytrace                 | 225 ms                                                                      | 214 ms: 1.05x faster                                                      |
| genshi_xml               | 46.0 ms                                                                     | 44.0 ms: 1.05x faster                                                     |
| richards_super           | 39.4 ms                                                                     | 37.7 ms: 1.04x faster                                                     |
| telco                    | 4.43 ms                                                                     | 4.25 ms: 1.04x faster                                                     |
| genshi_text              | 19.2 ms                                                                     | 18.4 ms: 1.04x faster                                                     |
| richards                 | 35.2 ms                                                                     | 33.9 ms: 1.04x faster                                                     |
| pycparser                | 718 ms                                                                      | 693 ms: 1.04x faster                                                      |
| sphinx                   | 763 ms                                                                      | 737 ms: 1.04x faster                                                      |
| sympy_str                | 190 ms                                                                      | 184 ms: 1.03x faster                                                      |
| regex_compile            | 90.2 ms                                                                     | 87.6 ms: 1.03x faster                                                     |
| hexiom                   | 5.19 ms                                                                     | 5.05 ms: 1.03x faster                                                     |
| typing_runtime_protocols | 117 us                                                                      | 114 us: 1.03x faster                                                      |
| json_dumps               | 6.38 ms                                                                     | 6.20 ms: 1.03x faster                                                     |
| xml_etree_generate       | 51.0 ms                                                                     | 49.7 ms: 1.03x faster                                                     |
| chaos                    | 41.4 ms                                                                     | 40.4 ms: 1.03x faster                                                     |
| nqueens                  | 65.7 ms                                                                     | 64.1 ms: 1.03x faster                                                     |
| docutils                 | 1.89 sec                                                                    | 1.84 sec: 1.03x faster                                                    |
| xml_etree_process        | 36.3 ms                                                                     | 35.5 ms: 1.02x faster                                                     |
| sqlglot_parse            | 899 us                                                                      | 878 us: 1.02x faster                                                      |
| generators               | 22.8 ms                                                                     | 22.3 ms: 1.02x faster                                                     |
| connected_components     | 316 ms                                                                      | 310 ms: 1.02x faster                                                      |
| bench_thread_pool        | 822 us                                                                      | 807 us: 1.02x faster                                                      |
| async_tree_io            | 553 ms                                                                      | 544 ms: 1.02x faster                                                      |
| meteor_contest           | 72.9 ms                                                                     | 71.8 ms: 1.02x faster                                                     |
| scimark_lu               | 54.2 ms                                                                     | 53.3 ms: 1.02x faster                                                     |
| mako                     | 5.18 ms                                                                     | 5.12 ms: 1.01x faster                                                     |
| sqlglot_normalize        | 210 ms                                                                      | 208 ms: 1.01x faster                                                      |
| deltablue                | 2.36 ms                                                                     | 2.34 ms: 1.01x faster                                                     |
| scimark_sor              | 64.1 ms                                                                     | 63.5 ms: 1.01x faster                                                     |
| sympy_expand             | 322 ms                                                                      | 320 ms: 1.01x faster                                                      |
| tomli_loads              | 1.27 sec                                                                    | 1.26 sec: 1.01x faster                                                    |
| scimark_monte_carlo      | 36.9 ms                                                                     | 36.7 ms: 1.00x faster                                                     |
| scimark_sparse_mat_mult  | 2.22 ms                                                                     | 2.21 ms: 1.00x faster                                                     |
| sqlite_synth             | 1.57 us                                                                     | 1.58 us: 1.00x slower                                                     |
| pidigits                 | 147 ms                                                                      | 147 ms: 1.01x slower                                                      |
| xml_etree_parse          | 92.7 ms                                                                     | 93.3 ms: 1.01x slower                                                     |
| crypto_pyaes             | 39.6 ms                                                                     | 39.9 ms: 1.01x slower                                                     |
| dulwich_log              | 39.8 ms                                                                     | 40.4 ms: 1.01x slower                                                     |
| json                     | 2.94 ms                                                                     | 2.99 ms: 1.02x slower                                                     |
| coverage                 | 47.8 ms                                                                     | 48.7 ms: 1.02x slower                                                     |
| logging_format           | 6.56 us                                                                     | 6.68 us: 1.02x slower                                                     |
| python_startup_no_site   | 17.7 ms                                                                     | 18.0 ms: 1.02x slower                                                     |
| pprint_pformat           | 924 ms                                                                      | 944 ms: 1.02x slower                                                      |
| logging_simple           | 6.10 us                                                                     | 6.25 us: 1.02x slower                                                     |
| go                       | 91.0 ms                                                                     | 93.1 ms: 1.02x slower                                                     |
| json_loads               | 14.3 us                                                                     | 14.7 us: 1.02x slower                                                     |
| mdp                      | 1.59 sec                                                                    | 1.63 sec: 1.02x slower                                                    |
| async_tree_none          | 209 ms                                                                      | 214 ms: 1.03x slower                                                      |
| python_startup           | 23.3 ms                                                                     | 24.0 ms: 1.03x slower                                                     |
| deepcopy                 | 186 us                                                                      | 192 us: 1.03x slower                                                      |
| pprint_safe_repr         | 452 ms                                                                      | 467 ms: 1.03x slower                                                      |
| regex_effbot             | 1.54 ms                                                                     | 1.60 ms: 1.03x slower                                                     |
| deepcopy_memo            | 16.2 us                                                                     | 16.8 us: 1.04x slower                                                     |
| bpe_tokeniser            | 2.69 sec                                                                    | 2.80 sec: 1.04x slower                                                    |
| thrift                   | 527 us                                                                      | 552 us: 1.05x slower                                                      |
| regex_dna                | 116 ms                                                                      | 121 ms: 1.05x slower                                                      |
| async_tree_memoization   | 262 ms                                                                      | 276 ms: 1.05x slower                                                      |
| logging_silent           | 54.6 ns                                                                     | 57.9 ns: 1.06x slower                                                     |
| fannkuch                 | 243 ms                                                                      | 258 ms: 1.06x slower                                                      |
| regex_v8                 | 14.6 ms                                                                     | 15.7 ms: 1.07x slower                                                     |
| nbody                    | 52.8 ms                                                                     | 56.7 ms: 1.07x slower                                                     |
| Geometric mean           | (ref)                                                                       | 1.01x faster                                                              |

Benchmark hidden because not significant (21): async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_cpu_io_mixed_tg, django_template, async_tree_memoization_tg, bench_mp_pool, create_gc_cycles, deepcopy_reduce, xml_etree_iterparse, float, async_generators, pathlib, pickle_pure_python, html5lib, shortest_path, gc_traversal, scimark_fft, comprehensions, spectral_norm, coroutines, k_core

- Geometric mean (including insignificant results): 1.012x faster
# HPT report

- Reliability score: 97.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown