# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-aarch64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 356 ms: 1.17x slower                                                   |
| docutils       | 3.10 sec                                                     | 3.53 sec: 1.14x slower                                                 |
| html5lib       | 66.1 ms                                                      | 70.7 ms: 1.07x slower                                                  |
| tornado_http   | 128 ms                                                       | 138 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                        | 1.11x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization | 645 ms                                                       | 665 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                           |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 90.1 ms: 1.01x faster                                                  |
| nbody          | 114 ms                                                       | 117 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.0 ms: 1.04x faster                                                  |
| regex_compile  | 128 ms                                                       | 176 ms: 1.37x slower                                                   |
| Geometric mean | (ref)                                                        | 1.07x slower                                                           |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 19.3 us: 1.02x faster                                                  |
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.01x faster                                                   |
| json_dumps           | 13.1 ms                                                      | 13.2 ms: 1.00x slower                                                  |
| xml_etree_iterparse  | 147 ms                                                       | 148 ms: 1.01x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                                 |
| unpickle_list        | 6.52 us                                                      | 6.67 us: 1.02x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 275 us: 1.10x slower                                                   |
| pickle_pure_python   | 359 us                                                       | 413 us: 1.15x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                           |

Benchmark hidden because not significant (6): xml_etree_parse, xml_etree_process, pickle_list, pickle_dict, pickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 12.8 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                        | 1.00x faster                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                  |
| django_template | 42.3 ms                                                      | 49.1 ms: 1.16x slower                                                  |
| genshi_text     | 27.4 ms                                                      | 34.0 ms: 1.24x slower                                                  |
| genshi_xml      | 60.4 ms                                                      | 81.1 ms: 1.34x slower                                                  |
| Geometric mean  | (ref)                                                        | 1.17x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo            | 50.8 us                                                      | 48.8 us: 1.04x faster                                                  |
| regex_v8                 | 31.1 ms                                                      | 30.0 ms: 1.04x faster                                                  |
| pathlib                  | 22.8 ms                                                      | 22.2 ms: 1.02x faster                                                  |
| mako                     | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                  |
| unpickle                 | 19.8 us                                                      | 19.3 us: 1.02x faster                                                  |
| thrift                   | 962 us                                                       | 944 us: 1.02x faster                                                   |
| python_startup           | 13.0 ms                                                      | 12.8 ms: 1.01x faster                                                  |
| float                    | 91.4 ms                                                      | 90.1 ms: 1.01x faster                                                  |
| xml_etree_generate       | 114 ms                                                       | 112 ms: 1.01x faster                                                   |
| json_dumps               | 13.1 ms                                                      | 13.2 ms: 1.00x slower                                                  |
| xml_etree_iterparse      | 147 ms                                                       | 148 ms: 1.01x slower                                                   |
| tomli_loads              | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                                 |
| asyncio_tcp_ssl          | 2.21 sec                                                     | 2.24 sec: 1.01x slower                                                 |
| nbody                    | 114 ms                                                       | 117 ms: 1.02x slower                                                   |
| unpickle_list            | 6.52 us                                                      | 6.67 us: 1.02x slower                                                  |
| coverage                 | 98.4 ms                                                      | 101 ms: 1.02x slower                                                   |
| generators               | 37.1 ms                                                      | 38.2 ms: 1.03x slower                                                  |
| mdp                      | 3.33 sec                                                     | 3.42 sec: 1.03x slower                                                 |
| meteor_contest           | 113 ms                                                       | 117 ms: 1.03x slower                                                   |
| async_tree_memoization   | 645 ms                                                       | 665 ms: 1.03x slower                                                   |
| spectral_norm            | 141 ms                                                       | 146 ms: 1.03x slower                                                   |
| scimark_fft              | 445 ms                                                       | 460 ms: 1.03x slower                                                   |
| logging_silent           | 133 ns                                                       | 139 ns: 1.04x slower                                                   |
| async_generators         | 488 ms                                                       | 512 ms: 1.05x slower                                                   |
| dask                     | 370 ms                                                       | 390 ms: 1.05x slower                                                   |
| bench_thread_pool        | 1.26 ms                                                      | 1.33 ms: 1.05x slower                                                  |
| fannkuch                 | 451 ms                                                       | 476 ms: 1.06x slower                                                   |
| scimark_sparse_mat_mult  | 6.55 ms                                                      | 6.94 ms: 1.06x slower                                                  |
| html5lib                 | 66.1 ms                                                      | 70.7 ms: 1.07x slower                                                  |
| typing_runtime_protocols | 193 us                                                       | 208 us: 1.07x slower                                                   |
| pyflate                  | 557 ms                                                       | 598 ms: 1.07x slower                                                   |
| asyncio_tcp              | 584 ms                                                       | 630 ms: 1.08x slower                                                   |
| tornado_http             | 128 ms                                                       | 138 ms: 1.08x slower                                                   |
| crypto_pyaes             | 82.0 ms                                                      | 88.8 ms: 1.08x slower                                                  |
| deepcopy                 | 448 us                                                       | 490 us: 1.09x slower                                                   |
| raytrace                 | 297 ms                                                       | 325 ms: 1.09x slower                                                   |
| unpickle_pure_python     | 251 us                                                       | 275 us: 1.10x slower                                                   |
| sqlglot_normalize        | 129 ms                                                       | 142 ms: 1.10x slower                                                   |
| scimark_monte_carlo      | 82.3 ms                                                      | 90.6 ms: 1.10x slower                                                  |
| sqlglot_optimize         | 62.6 ms                                                      | 69.1 ms: 1.10x slower                                                  |
| scimark_sor              | 159 ms                                                       | 176 ms: 1.10x slower                                                   |
| pycparser                | 1.22 sec                                                     | 1.35 sec: 1.11x slower                                                 |
| go                       | 161 ms                                                       | 179 ms: 1.11x slower                                                   |
| sqlglot_parse            | 1.42 ms                                                      | 1.59 ms: 1.12x slower                                                  |
| comprehensions           | 20.5 us                                                      | 23.1 us: 1.12x slower                                                  |
| bench_mp_pool            | 7.03 ms                                                      | 8.01 ms: 1.14x slower                                                  |
| docutils                 | 3.10 sec                                                     | 3.53 sec: 1.14x slower                                                 |
| pickle_pure_python       | 359 us                                                       | 413 us: 1.15x slower                                                   |
| deepcopy_reduce          | 4.04 us                                                      | 4.65 us: 1.15x slower                                                  |
| django_template          | 42.3 ms                                                      | 49.1 ms: 1.16x slower                                                  |
| sympy_expand             | 457 ms                                                       | 534 ms: 1.17x slower                                                   |
| 2to3                     | 305 ms                                                       | 356 ms: 1.17x slower                                                   |
| nqueens                  | 98.9 ms                                                      | 116 ms: 1.17x slower                                                   |
| sqlglot_transpile        | 1.71 ms                                                      | 2.03 ms: 1.19x slower                                                  |
| deltablue                | 3.88 ms                                                      | 4.61 ms: 1.19x slower                                                  |
| pprint_safe_repr         | 933 ms                                                       | 1.12 sec: 1.20x slower                                                 |
| sympy_str                | 265 ms                                                       | 319 ms: 1.20x slower                                                   |
| pprint_pformat           | 1.93 sec                                                     | 2.32 sec: 1.20x slower                                                 |
| dulwich_log              | 58.5 ms                                                      | 70.6 ms: 1.21x slower                                                  |
| genshi_text              | 27.4 ms                                                      | 34.0 ms: 1.24x slower                                                  |
| sympy_integrate          | 20.9 ms                                                      | 25.9 ms: 1.24x slower                                                  |
| pylint                   | 337 ms                                                       | 421 ms: 1.25x slower                                                   |
| hexiom                   | 7.08 ms                                                      | 8.96 ms: 1.27x slower                                                  |
| chaos                    | 68.3 ms                                                      | 88.2 ms: 1.29x slower                                                  |
| scimark_lu               | 141 ms                                                       | 183 ms: 1.30x slower                                                   |
| sympy_sum                | 144 ms                                                       | 187 ms: 1.30x slower                                                   |
| genshi_xml               | 60.4 ms                                                      | 81.1 ms: 1.34x slower                                                  |
| regex_compile            | 128 ms                                                       | 176 ms: 1.37x slower                                                   |
| Geometric mean           | (ref)                                                        | 1.07x slower                                                           |

Benchmark hidden because not significant (28): xml_etree_parse, xml_etree_process, richards, regex_effbot, telco, regex_dna, richards_super, coroutines, pickle_list, pickle_dict, pidigits, gc_traversal, async_tree_io_tg, async_tree_io, pickle, async_tree_cpu_io_mixed_tg, async_tree_none, sqlite_synth, async_tree_none_tg, async_tree_memoization_tg, asyncio_websockets, create_gc_cycles, logging_format, python_startup_no_site, json_loads, async_tree_cpu_io_mixed, json, logging_simple
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.07x