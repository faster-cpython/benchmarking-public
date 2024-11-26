# Results vs. base

- fork: brandtbucher
- ref: jump_backoff
- machine: windows-x86
- commit hash: 2e7a174
- commit date: 2024-11-13
- overall geometric mean: 1.010x faster
- HPT reliability: 94.07%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 294 ms                                                                          | 267 ms: 1.10x faster                                                          |
| docutils       | 2.15 sec                                                                        | 2.08 sec: 1.03x faster                                                        |
| html5lib       | 49.4 ms                                                                         | 48.9 ms: 1.01x faster                                                         |
| sphinx         | 908 ms                                                                          | 875 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                                           | 1.05x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 221 ms                                                                          | 213 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed    | 497 ms                                                                          | 487 ms: 1.02x faster                                                          |
| async_tree_io              | 567 ms                                                                          | 559 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg | 467 ms                                                                          | 460 ms: 1.01x faster                                                          |
| async_tree_io_tg           | 568 ms                                                                          | 561 ms: 1.01x faster                                                          |
| asyncio_websockets         | 365 ms                                                                          | 362 ms: 1.01x faster                                                          |
| async_generators           | 322 ms                                                                          | 324 ms: 1.01x slower                                                          |
| async_tree_none            | 241 ms                                                                          | 244 ms: 1.02x slower                                                          |
| Geometric mean             | (ref)                                                                           | 1.01x faster                                                                  |

Benchmark hidden because not significant (3): async_tree_memoization_tg, coroutines, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 55.3 ms                                                                         | 55.6 ms: 1.00x slower                                                         |
| pidigits       | 201 ms                                                                          | 203 ms: 1.01x slower                                                          |
| nbody          | 97.0 ms                                                                         | 100 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                                           | 1.02x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 122 ms                                                                          | 117 ms: 1.05x faster                                                          |
| regex_v8       | 16.5 ms                                                                         | 16.1 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                                           | 1.02x faster                                                                  |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_loads           | 21.4 us                                                                         | 20.7 us: 1.03x faster                                                         |
| xml_etree_iterparse  | 70.2 ms                                                                         | 68.0 ms: 1.03x faster                                                         |
| xml_etree_process    | 55.3 ms                                                                         | 53.9 ms: 1.03x faster                                                         |
| xml_etree_parse      | 114 ms                                                                          | 112 ms: 1.02x faster                                                          |
| xml_etree_generate   | 74.3 ms                                                                         | 73.3 ms: 1.01x faster                                                         |
| tomli_loads          | 1.81 sec                                                                        | 1.85 sec: 1.02x slower                                                        |
| unpickle_pure_python | 188 us                                                                          | 208 us: 1.11x slower                                                          |
| Geometric mean       | (ref)                                                                           | 1.00x slower                                                                  |

Benchmark hidden because not significant (2): pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|------------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 19.4 ms                                                                         | 19.2 ms: 1.01x faster                                                         |
| Geometric mean         | (ref)                                                                           | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|-----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 27.1 ms                                                                         | 25.8 ms: 1.05x faster                                                         |
| genshi_xml      | 58.0 ms                                                                         | 56.5 ms: 1.03x faster                                                         |
| django_template | 36.5 ms                                                                         | 36.0 ms: 1.01x faster                                                         |
| mako            | 7.32 ms                                                                         | 7.37 ms: 1.01x slower                                                         |
| Geometric mean  | (ref)                                                                           | 1.02x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pylint                     | 293 ms                                                                          | 258 ms: 1.14x faster                                                          |
| sqlglot_optimize           | 57.2 ms                                                                         | 51.5 ms: 1.11x faster                                                         |
| sympy_integrate            | 19.6 ms                                                                         | 17.6 ms: 1.11x faster                                                         |
| 2to3                       | 294 ms                                                                          | 267 ms: 1.10x faster                                                          |
| bench_mp_pool              | 92.8 ms                                                                         | 86.3 ms: 1.08x faster                                                         |
| sympy_sum                  | 125 ms                                                                          | 117 ms: 1.07x faster                                                          |
| json                       | 4.63 ms                                                                         | 4.39 ms: 1.05x faster                                                         |
| genshi_text                | 27.1 ms                                                                         | 25.8 ms: 1.05x faster                                                         |
| sqlglot_normalize          | 116 ms                                                                          | 110 ms: 1.05x faster                                                          |
| regex_compile              | 122 ms                                                                          | 117 ms: 1.05x faster                                                          |
| scimark_fft                | 255 ms                                                                          | 244 ms: 1.05x faster                                                          |
| sphinx                     | 908 ms                                                                          | 875 ms: 1.04x faster                                                          |
| async_tree_none_tg         | 221 ms                                                                          | 213 ms: 1.04x faster                                                          |
| json_loads                 | 21.4 us                                                                         | 20.7 us: 1.03x faster                                                         |
| docutils                   | 2.15 sec                                                                        | 2.08 sec: 1.03x faster                                                        |
| comprehensions             | 18.8 us                                                                         | 18.2 us: 1.03x faster                                                         |
| sqlglot_transpile          | 1.52 ms                                                                         | 1.47 ms: 1.03x faster                                                         |
| xml_etree_iterparse        | 70.2 ms                                                                         | 68.0 ms: 1.03x faster                                                         |
| sympy_str                  | 250 ms                                                                          | 243 ms: 1.03x faster                                                          |
| genshi_xml                 | 58.0 ms                                                                         | 56.5 ms: 1.03x faster                                                         |
| xml_etree_process          | 55.3 ms                                                                         | 53.9 ms: 1.03x faster                                                         |
| scimark_sparse_mat_mult    | 3.27 ms                                                                         | 3.19 ms: 1.03x faster                                                         |
| crypto_pyaes               | 67.5 ms                                                                         | 65.9 ms: 1.02x faster                                                         |
| regex_v8                   | 16.5 ms                                                                         | 16.1 ms: 1.02x faster                                                         |
| raytrace                   | 314 ms                                                                          | 308 ms: 1.02x faster                                                          |
| generators                 | 36.3 ms                                                                         | 35.6 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed    | 497 ms                                                                          | 487 ms: 1.02x faster                                                          |
| xml_etree_parse            | 114 ms                                                                          | 112 ms: 1.02x faster                                                          |
| deepcopy_memo              | 23.4 us                                                                         | 23.1 us: 1.02x faster                                                         |
| async_tree_io              | 567 ms                                                                          | 559 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg | 467 ms                                                                          | 460 ms: 1.01x faster                                                          |
| python_startup_no_site     | 19.4 ms                                                                         | 19.2 ms: 1.01x faster                                                         |
| xml_etree_generate         | 74.3 ms                                                                         | 73.3 ms: 1.01x faster                                                         |
| django_template            | 36.5 ms                                                                         | 36.0 ms: 1.01x faster                                                         |
| async_tree_io_tg           | 568 ms                                                                          | 561 ms: 1.01x faster                                                          |
| pycparser                  | 933 ms                                                                          | 922 ms: 1.01x faster                                                          |
| richards                   | 43.6 ms                                                                         | 43.1 ms: 1.01x faster                                                         |
| html5lib                   | 49.4 ms                                                                         | 48.9 ms: 1.01x faster                                                         |
| thrift                     | 784 us                                                                          | 776 us: 1.01x faster                                                          |
| asyncio_websockets         | 365 ms                                                                          | 362 ms: 1.01x faster                                                          |
| go                         | 127 ms                                                                          | 125 ms: 1.01x faster                                                          |
| hexiom                     | 7.28 ms                                                                         | 7.21 ms: 1.01x faster                                                         |
| bpe_tokeniser              | 3.78 sec                                                                        | 3.76 sec: 1.01x faster                                                        |
| connected_components       | 289 ms                                                                          | 287 ms: 1.01x faster                                                          |
| dulwich_log                | 49.8 ms                                                                         | 49.5 ms: 1.01x faster                                                         |
| scimark_monte_carlo        | 62.5 ms                                                                         | 62.1 ms: 1.01x faster                                                         |
| sympy_expand               | 425 ms                                                                          | 424 ms: 1.00x faster                                                          |
| chaos                      | 65.1 ms                                                                         | 65.3 ms: 1.00x slower                                                         |
| float                      | 55.3 ms                                                                         | 55.6 ms: 1.00x slower                                                         |
| deltablue                  | 3.22 ms                                                                         | 3.23 ms: 1.01x slower                                                         |
| async_generators           | 322 ms                                                                          | 324 ms: 1.01x slower                                                          |
| nqueens                    | 97.1 ms                                                                         | 97.8 ms: 1.01x slower                                                         |
| pprint_safe_repr           | 735 ms                                                                          | 740 ms: 1.01x slower                                                          |
| richards_super             | 49.0 ms                                                                         | 49.4 ms: 1.01x slower                                                         |
| pidigits                   | 201 ms                                                                          | 203 ms: 1.01x slower                                                          |
| mako                       | 7.32 ms                                                                         | 7.37 ms: 1.01x slower                                                         |
| deepcopy                   | 275 us                                                                          | 277 us: 1.01x slower                                                          |
| sqlglot_parse              | 1.17 ms                                                                         | 1.18 ms: 1.01x slower                                                         |
| meteor_contest             | 89.0 ms                                                                         | 89.8 ms: 1.01x slower                                                         |
| logging_format             | 8.92 us                                                                         | 9.04 us: 1.01x slower                                                         |
| shortest_path              | 317 ms                                                                          | 322 ms: 1.01x slower                                                          |
| logging_simple             | 8.26 us                                                                         | 8.39 us: 1.01x slower                                                         |
| async_tree_none            | 241 ms                                                                          | 244 ms: 1.02x slower                                                          |
| deepcopy_reduce            | 2.77 us                                                                         | 2.82 us: 1.02x slower                                                         |
| pprint_pformat             | 1.49 sec                                                                        | 1.52 sec: 1.02x slower                                                        |
| spectral_norm              | 82.5 ms                                                                         | 84.3 ms: 1.02x slower                                                         |
| tomli_loads                | 1.81 sec                                                                        | 1.85 sec: 1.02x slower                                                        |
| typing_runtime_protocols   | 164 us                                                                          | 168 us: 1.02x slower                                                          |
| scimark_sor                | 98.9 ms                                                                         | 101 ms: 1.02x slower                                                          |
| telco                      | 7.01 ms                                                                         | 7.18 ms: 1.03x slower                                                         |
| nbody                      | 97.0 ms                                                                         | 100 ms: 1.04x slower                                                          |
| sqlite_synth               | 1.94 us                                                                         | 2.01 us: 1.04x slower                                                         |
| mdp                        | 1.87 sec                                                                        | 1.95 sec: 1.04x slower                                                        |
| scimark_lu                 | 71.9 ms                                                                         | 75.9 ms: 1.06x slower                                                         |
| logging_silent             | 78.1 ns                                                                         | 86.0 ns: 1.10x slower                                                         |
| unpickle_pure_python       | 188 us                                                                          | 208 us: 1.11x slower                                                          |
| Geometric mean             | (ref)                                                                           | 1.01x faster                                                                  |

Benchmark hidden because not significant (16): async_tree_memoization_tg, regex_dna, python_startup, create_gc_cycles, regex_effbot, coroutines, pickle_pure_python, gc_traversal, pathlib, bench_thread_pool, coverage, json_dumps, fannkuch, k_core, pyflate, async_tree_memoization

- Geometric mean (including insignificant results): 1.010x faster
# HPT report

- Reliability score: 94.07% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown