# Results vs. base

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.051x faster
- HPT reliability: 82.60%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 295 ms                                                                                                               | 289 ms: 1.02x faster                                                                                                     |
| docutils       | 2.08 sec                                                                                                             | 2.12 sec: 1.02x slower                                                                                                   |
| html5lib       | 51.5 ms                                                                                                              | 52.9 ms: 1.03x slower                                                                                                    |
| sphinx         | 838 ms                                                                                                               | 860 ms: 1.03x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none            | 242 ms                                                                                                               | 236 ms: 1.03x faster                                                                                                     |
| async_tree_none_tg         | 235 ms                                                                                                               | 229 ms: 1.03x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 438 ms                                                                                                               | 428 ms: 1.02x faster                                                                                                     |
| async_tree_memoization     | 295 ms                                                                                                               | 289 ms: 1.02x faster                                                                                                     |
| async_tree_io              | 546 ms                                                                                                               | 536 ms: 1.02x faster                                                                                                     |
| async_tree_cpu_io_mixed    | 440 ms                                                                                                               | 432 ms: 1.02x faster                                                                                                     |
| async_tree_memoization_tg  | 292 ms                                                                                                               | 288 ms: 1.02x faster                                                                                                     |
| async_tree_io_tg           | 561 ms                                                                                                               | 554 ms: 1.01x faster                                                                                                     |
| asyncio_tcp_ssl            | 1.49 sec                                                                                                             | 1.51 sec: 1.01x slower                                                                                                   |
| async_generators           | 332 ms                                                                                                               | 355 ms: 1.07x slower                                                                                                     |
| coroutines                 | 24.7 ms                                                                                                              | 26.8 ms: 1.09x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                                | 1.00x faster                                                                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 99.6 ms                                                                                                              | 53.7 ms: 1.86x faster                                                                                                    |
| float          | 76.0 ms                                                                                                              | 78.5 ms: 1.03x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.21x faster                                                                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 17.0 ms                                                                                                              | 16.6 ms: 1.02x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.00x faster                                                                                                             |

Benchmark hidden because not significant (3): regex_effbot, regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 275 us                                                                                                               | 157 us: 1.75x faster                                                                                                     |
| tomli_loads          | 2.02 sec                                                                                                             | 1.58 sec: 1.28x faster                                                                                                   |
| xml_etree_generate   | 89.3 ms                                                                                                              | 72.7 ms: 1.23x faster                                                                                                    |
| xml_etree_process    | 64.0 ms                                                                                                              | 53.2 ms: 1.20x faster                                                                                                    |
| pickle_pure_python   | 358 us                                                                                                               | 328 us: 1.09x faster                                                                                                     |
| xml_etree_iterparse  | 89.5 ms                                                                                                              | 87.2 ms: 1.03x faster                                                                                                    |
| xml_etree_parse      | 108 ms                                                                                                               | 106 ms: 1.02x faster                                                                                                     |
| json_dumps           | 8.83 ms                                                                                                              | 8.67 ms: 1.02x faster                                                                                                    |
| json_loads           | 21.1 us                                                                                                              | 20.8 us: 1.01x faster                                                                                                    |
| pickle               | 9.61 us                                                                                                              | 9.70 us: 1.01x slower                                                                                                    |
| unpickle             | 11.5 us                                                                                                              | 11.7 us: 1.02x slower                                                                                                    |
| unpickle_list        | 3.07 us                                                                                                              | 3.12 us: 1.02x slower                                                                                                    |
| pickle_list          | 3.79 us                                                                                                              | 3.94 us: 1.04x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.10x faster                                                                                                             |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 12.4 ms                                                                                                              | 7.13 ms: 1.73x faster                                                                                                    |
| genshi_xml      | 48.3 ms                                                                                                              | 51.5 ms: 1.07x slower                                                                                                    |
| django_template | 36.3 ms                                                                                                              | 38.7 ms: 1.07x slower                                                                                                    |
| genshi_text     | 23.3 ms                                                                                                              | 25.5 ms: 1.09x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.09x faster                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json | results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody                      | 99.6 ms                                                                                                              | 53.7 ms: 1.86x faster                                                                                                    |
| unpickle_pure_python       | 275 us                                                                                                               | 157 us: 1.75x faster                                                                                                     |
| mako                       | 12.4 ms                                                                                                              | 7.13 ms: 1.73x faster                                                                                                    |
| scimark_sparse_mat_mult    | 4.16 ms                                                                                                              | 2.70 ms: 1.54x faster                                                                                                    |
| fannkuch                   | 406 ms                                                                                                               | 282 ms: 1.44x faster                                                                                                     |
| scimark_fft                | 265 ms                                                                                                               | 185 ms: 1.43x faster                                                                                                     |
| bpe_tokeniser              | 4.28 sec                                                                                                             | 3.09 sec: 1.38x faster                                                                                                   |
| pprint_safe_repr           | 854 ms                                                                                                               | 667 ms: 1.28x faster                                                                                                     |
| tomli_loads                | 2.02 sec                                                                                                             | 1.58 sec: 1.28x faster                                                                                                   |
| pprint_pformat             | 1.74 sec                                                                                                             | 1.37 sec: 1.27x faster                                                                                                   |
| crypto_pyaes               | 79.7 ms                                                                                                              | 62.7 ms: 1.27x faster                                                                                                    |
| xml_etree_generate         | 89.3 ms                                                                                                              | 72.7 ms: 1.23x faster                                                                                                    |
| comprehensions             | 19.3 us                                                                                                              | 15.9 us: 1.22x faster                                                                                                    |
| xml_etree_process          | 64.0 ms                                                                                                              | 53.2 ms: 1.20x faster                                                                                                    |
| telco                      | 6.25 ms                                                                                                              | 5.27 ms: 1.19x faster                                                                                                    |
| sqlglot_v2_parse           | 1.34 ms                                                                                                              | 1.15 ms: 1.17x faster                                                                                                    |
| pyflate                    | 453 ms                                                                                                               | 390 ms: 1.16x faster                                                                                                     |
| sqlglot_v2_transpile       | 1.61 ms                                                                                                              | 1.43 ms: 1.12x faster                                                                                                    |
| meteor_contest             | 92.3 ms                                                                                                              | 83.0 ms: 1.11x faster                                                                                                    |
| pickle_pure_python         | 358 us                                                                                                               | 328 us: 1.09x faster                                                                                                     |
| k_core                     | 1.81 sec                                                                                                             | 1.67 sec: 1.08x faster                                                                                                   |
| connected_components       | 347 ms                                                                                                               | 324 ms: 1.07x faster                                                                                                     |
| sqlite_synth               | 1.86 us                                                                                                              | 1.74 us: 1.07x faster                                                                                                    |
| typing_runtime_protocols   | 153 us                                                                                                               | 145 us: 1.05x faster                                                                                                     |
| shortest_path              | 380 ms                                                                                                               | 365 ms: 1.04x faster                                                                                                     |
| async_tree_none            | 242 ms                                                                                                               | 236 ms: 1.03x faster                                                                                                     |
| xml_etree_iterparse        | 89.5 ms                                                                                                              | 87.2 ms: 1.03x faster                                                                                                    |
| async_tree_none_tg         | 235 ms                                                                                                               | 229 ms: 1.03x faster                                                                                                     |
| xml_etree_parse            | 108 ms                                                                                                               | 106 ms: 1.02x faster                                                                                                     |
| json                       | 4.17 ms                                                                                                              | 4.07 ms: 1.02x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 438 ms                                                                                                               | 428 ms: 1.02x faster                                                                                                     |
| 2to3                       | 295 ms                                                                                                               | 289 ms: 1.02x faster                                                                                                     |
| regex_v8                   | 17.0 ms                                                                                                              | 16.6 ms: 1.02x faster                                                                                                    |
| async_tree_memoization     | 295 ms                                                                                                               | 289 ms: 1.02x faster                                                                                                     |
| async_tree_io              | 546 ms                                                                                                               | 536 ms: 1.02x faster                                                                                                     |
| json_dumps                 | 8.83 ms                                                                                                              | 8.67 ms: 1.02x faster                                                                                                    |
| async_tree_cpu_io_mixed    | 440 ms                                                                                                               | 432 ms: 1.02x faster                                                                                                     |
| async_tree_memoization_tg  | 292 ms                                                                                                               | 288 ms: 1.02x faster                                                                                                     |
| json_loads                 | 21.1 us                                                                                                              | 20.8 us: 1.01x faster                                                                                                    |
| async_tree_io_tg           | 561 ms                                                                                                               | 554 ms: 1.01x faster                                                                                                     |
| pycparser                  | 974 ms                                                                                                               | 964 ms: 1.01x faster                                                                                                     |
| sqlglot_v2_optimize        | 49.8 ms                                                                                                              | 50.2 ms: 1.01x slower                                                                                                    |
| pickle                     | 9.61 us                                                                                                              | 9.70 us: 1.01x slower                                                                                                    |
| asyncio_tcp_ssl            | 1.49 sec                                                                                                             | 1.51 sec: 1.01x slower                                                                                                   |
| coverage                   | 62.3 ms                                                                                                              | 62.9 ms: 1.01x slower                                                                                                    |
| unpickle                   | 11.5 us                                                                                                              | 11.7 us: 1.02x slower                                                                                                    |
| sympy_sum                  | 115 ms                                                                                                               | 116 ms: 1.02x slower                                                                                                     |
| unpickle_list              | 3.07 us                                                                                                              | 3.12 us: 1.02x slower                                                                                                    |
| sqlglot_v2_normalize       | 104 ms                                                                                                               | 105 ms: 1.02x slower                                                                                                     |
| docutils                   | 2.08 sec                                                                                                             | 2.12 sec: 1.02x slower                                                                                                   |
| raytrace                   | 300 ms                                                                                                               | 307 ms: 1.02x slower                                                                                                     |
| dulwich_log                | 50.8 ms                                                                                                              | 52.1 ms: 1.03x slower                                                                                                    |
| sphinx                     | 838 ms                                                                                                               | 860 ms: 1.03x slower                                                                                                     |
| chaos                      | 64.0 ms                                                                                                              | 65.7 ms: 1.03x slower                                                                                                    |
| html5lib                   | 51.5 ms                                                                                                              | 52.9 ms: 1.03x slower                                                                                                    |
| pylint                     | 247 ms                                                                                                               | 254 ms: 1.03x slower                                                                                                     |
| subparsers                 | 22.3 ms                                                                                                              | 23.0 ms: 1.03x slower                                                                                                    |
| sympy_str                  | 231 ms                                                                                                               | 238 ms: 1.03x slower                                                                                                     |
| logging_silent             | 494 ns                                                                                                               | 509 ns: 1.03x slower                                                                                                     |
| thrift                     | 692 us                                                                                                               | 714 us: 1.03x slower                                                                                                     |
| sympy_expand               | 396 ms                                                                                                               | 409 ms: 1.03x slower                                                                                                     |
| float                      | 76.0 ms                                                                                                              | 78.5 ms: 1.03x slower                                                                                                    |
| logging_simple             | 9.25 us                                                                                                              | 9.56 us: 1.03x slower                                                                                                    |
| sympy_integrate            | 16.4 ms                                                                                                              | 17.0 ms: 1.03x slower                                                                                                    |
| spectral_norm              | 111 ms                                                                                                               | 115 ms: 1.04x slower                                                                                                     |
| scimark_monte_carlo        | 71.9 ms                                                                                                              | 74.6 ms: 1.04x slower                                                                                                    |
| logging_format             | 9.74 us                                                                                                              | 10.1 us: 1.04x slower                                                                                                    |
| pickle_list                | 3.79 us                                                                                                              | 3.94 us: 1.04x slower                                                                                                    |
| go                         | 131 ms                                                                                                               | 137 ms: 1.04x slower                                                                                                     |
| deepcopy                   | 262 us                                                                                                               | 273 us: 1.04x slower                                                                                                     |
| many_optionals             | 547 us                                                                                                               | 572 us: 1.04x slower                                                                                                     |
| generators                 | 36.6 ms                                                                                                              | 38.3 ms: 1.05x slower                                                                                                    |
| deepcopy_reduce            | 2.71 us                                                                                                              | 2.84 us: 1.05x slower                                                                                                    |
| mdp                        | 1.15 sec                                                                                                             | 1.21 sec: 1.05x slower                                                                                                   |
| deltablue                  | 4.29 ms                                                                                                              | 4.52 ms: 1.05x slower                                                                                                    |
| scimark_sor                | 130 ms                                                                                                               | 137 ms: 1.06x slower                                                                                                     |
| scimark_lu                 | 119 ms                                                                                                               | 126 ms: 1.06x slower                                                                                                     |
| genshi_xml                 | 48.3 ms                                                                                                              | 51.5 ms: 1.07x slower                                                                                                    |
| django_template            | 36.3 ms                                                                                                              | 38.7 ms: 1.07x slower                                                                                                    |
| richards_super             | 57.0 ms                                                                                                              | 60.9 ms: 1.07x slower                                                                                                    |
| async_generators           | 332 ms                                                                                                               | 355 ms: 1.07x slower                                                                                                     |
| richards                   | 50.5 ms                                                                                                              | 54.1 ms: 1.07x slower                                                                                                    |
| deepcopy_memo              | 33.0 us                                                                                                              | 35.6 us: 1.08x slower                                                                                                    |
| coroutines                 | 24.7 ms                                                                                                              | 26.8 ms: 1.09x slower                                                                                                    |
| hexiom                     | 7.36 ms                                                                                                              | 8.03 ms: 1.09x slower                                                                                                    |
| genshi_text                | 23.3 ms                                                                                                              | 25.5 ms: 1.09x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                                | 1.04x faster                                                                                                             |

Benchmark hidden because not significant (16): gc_traversal, python_startup_no_site, asyncio_websockets, asyncio_tcp, create_gc_cycles, nqueens, unpack_sequence, regex_effbot, regex_compile, pidigits, pathlib, bench_mp_pool, pickle_dict, regex_dna, python_startup, bench_thread_pool

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 82.60% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown