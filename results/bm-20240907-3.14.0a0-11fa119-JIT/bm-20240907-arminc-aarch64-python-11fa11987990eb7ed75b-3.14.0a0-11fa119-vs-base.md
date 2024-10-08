# Results vs. base

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.12x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                                                                            | 380 ms: 1.29x slower                                                                                                  |
| docutils       | 3.05 sec                                                                                                          | 3.94 sec: 1.29x slower                                                                                                |
| html5lib       | 63.1 ms                                                                                                           | 70.2 ms: 1.11x slower                                                                                                 |
| tornado_http   | 124 ms                                                                                                            | 147 ms: 1.18x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.22x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|-------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg        | 1.18 sec                                                                                                          | 1.15 sec: 1.02x faster                                                                                                |
| async_tree_cpu_io_mixed | 733 ms                                                                                                            | 748 ms: 1.02x slower                                                                                                  |
| asyncio_tcp_ssl         | 2.20 sec                                                                                                          | 2.25 sec: 1.02x slower                                                                                                |
| async_tree_memoization  | 556 ms                                                                                                            | 570 ms: 1.02x slower                                                                                                  |
| async_generators        | 487 ms                                                                                                            | 504 ms: 1.03x slower                                                                                                  |
| async_tree_io           | 1.13 sec                                                                                                          | 1.18 sec: 1.05x slower                                                                                                |
| async_tree_none         | 423 ms                                                                                                            | 457 ms: 1.08x slower                                                                                                  |
| asyncio_tcp             | 574 ms                                                                                                            | 625 ms: 1.09x slower                                                                                                  |
| Geometric mean          | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, coroutines, asyncio_websockets, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 92.7 ms                                                                                                           | 89.1 ms: 1.04x faster                                                                                                 |
| nbody          | 109 ms                                                                                                            | 114 ms: 1.04x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 252 ms                                                                                                            | 254 ms: 1.01x slower                                                                                                  |
| regex_v8       | 30.3 ms                                                                                                           | 31.1 ms: 1.03x slower                                                                                                 |
| regex_compile  | 125 ms                                                                                                            | 188 ms: 1.51x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.12x slower                                                                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.65 sec                                                                                                          | 2.61 sec: 1.01x faster                                                                                                |
| xml_etree_parse      | 186 ms                                                                                                            | 187 ms: 1.01x slower                                                                                                  |
| pickle               | 13.5 us                                                                                                           | 13.7 us: 1.01x slower                                                                                                 |
| unpickle_pure_python | 255 us                                                                                                            | 265 us: 1.04x slower                                                                                                  |
| pickle_pure_python   | 361 us                                                                                                            | 393 us: 1.09x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (9): unpickle_list, xml_etree_generate, pickle_dict, json_loads, xml_etree_process, pickle_list, xml_etree_iterparse, unpickle, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.83 ms                                                                                                           | 8.90 ms: 1.01x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.4 ms                                                                                                           | 13.2 ms: 1.01x faster                                                                                                 |
| django_template | 41.7 ms                                                                                                           | 51.4 ms: 1.23x slower                                                                                                 |
| genshi_text     | 27.5 ms                                                                                                           | 34.1 ms: 1.24x slower                                                                                                 |
| genshi_xml      | 60.6 ms                                                                                                           | 80.1 ms: 1.32x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.19x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|--------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| scimark_sor              | 158 ms                                                                                                            | 150 ms: 1.05x faster                                                                                                  |
| float                    | 92.7 ms                                                                                                           | 89.1 ms: 1.04x faster                                                                                                 |
| async_tree_io_tg         | 1.18 sec                                                                                                          | 1.15 sec: 1.02x faster                                                                                                |
| deepcopy_memo            | 38.0 us                                                                                                           | 37.3 us: 1.02x faster                                                                                                 |
| tomli_loads              | 2.65 sec                                                                                                          | 2.61 sec: 1.01x faster                                                                                                |
| mako                     | 13.4 ms                                                                                                           | 13.2 ms: 1.01x faster                                                                                                 |
| xml_etree_parse          | 186 ms                                                                                                            | 187 ms: 1.01x slower                                                                                                  |
| python_startup_no_site   | 8.83 ms                                                                                                           | 8.90 ms: 1.01x slower                                                                                                 |
| regex_dna                | 252 ms                                                                                                            | 254 ms: 1.01x slower                                                                                                  |
| pickle                   | 13.5 us                                                                                                           | 13.7 us: 1.01x slower                                                                                                 |
| create_gc_cycles         | 2.30 ms                                                                                                           | 2.33 ms: 1.01x slower                                                                                                 |
| async_tree_cpu_io_mixed  | 733 ms                                                                                                            | 748 ms: 1.02x slower                                                                                                  |
| asyncio_tcp_ssl          | 2.20 sec                                                                                                          | 2.25 sec: 1.02x slower                                                                                                |
| bpe_tokeniser            | 5.83 sec                                                                                                          | 5.96 sec: 1.02x slower                                                                                                |
| async_tree_memoization   | 556 ms                                                                                                            | 570 ms: 1.02x slower                                                                                                  |
| regex_v8                 | 30.3 ms                                                                                                           | 31.1 ms: 1.03x slower                                                                                                 |
| logging_silent           | 133 ns                                                                                                            | 137 ns: 1.03x slower                                                                                                  |
| json                     | 5.70 ms                                                                                                           | 5.88 ms: 1.03x slower                                                                                                 |
| async_generators         | 487 ms                                                                                                            | 504 ms: 1.03x slower                                                                                                  |
| spectral_norm            | 140 ms                                                                                                            | 146 ms: 1.04x slower                                                                                                  |
| scimark_fft              | 443 ms                                                                                                            | 460 ms: 1.04x slower                                                                                                  |
| unpickle_pure_python     | 255 us                                                                                                            | 265 us: 1.04x slower                                                                                                  |
| mdp                      | 3.34 sec                                                                                                          | 3.47 sec: 1.04x slower                                                                                                |
| telco                    | 9.99 ms                                                                                                           | 10.4 ms: 1.04x slower                                                                                                 |
| thrift                   | 931 us                                                                                                            | 971 us: 1.04x slower                                                                                                  |
| nbody                    | 109 ms                                                                                                            | 114 ms: 1.04x slower                                                                                                  |
| async_tree_io            | 1.13 sec                                                                                                          | 1.18 sec: 1.05x slower                                                                                                |
| pathlib                  | 21.0 ms                                                                                                           | 22.0 ms: 1.05x slower                                                                                                 |
| logging_format           | 7.62 us                                                                                                           | 8.09 us: 1.06x slower                                                                                                 |
| bench_thread_pool        | 1.24 ms                                                                                                           | 1.32 ms: 1.06x slower                                                                                                 |
| logging_simple           | 6.95 us                                                                                                           | 7.42 us: 1.07x slower                                                                                                 |
| scimark_sparse_mat_mult  | 6.38 ms                                                                                                           | 6.82 ms: 1.07x slower                                                                                                 |
| crypto_pyaes             | 83.4 ms                                                                                                           | 89.3 ms: 1.07x slower                                                                                                 |
| async_tree_none          | 423 ms                                                                                                            | 457 ms: 1.08x slower                                                                                                  |
| pickle_pure_python       | 361 us                                                                                                            | 393 us: 1.09x slower                                                                                                  |
| asyncio_tcp              | 574 ms                                                                                                            | 625 ms: 1.09x slower                                                                                                  |
| deepcopy_reduce          | 3.45 us                                                                                                           | 3.80 us: 1.10x slower                                                                                                 |
| fannkuch                 | 456 ms                                                                                                            | 504 ms: 1.10x slower                                                                                                  |
| meteor_contest           | 112 ms                                                                                                            | 124 ms: 1.11x slower                                                                                                  |
| pyflate                  | 566 ms                                                                                                            | 627 ms: 1.11x slower                                                                                                  |
| deltablue                | 3.91 ms                                                                                                           | 4.34 ms: 1.11x slower                                                                                                 |
| typing_runtime_protocols | 192 us                                                                                                            | 214 us: 1.11x slower                                                                                                  |
| html5lib                 | 63.1 ms                                                                                                           | 70.2 ms: 1.11x slower                                                                                                 |
| bench_mp_pool            | 7.02 ms                                                                                                           | 7.82 ms: 1.11x slower                                                                                                 |
| scimark_lu               | 134 ms                                                                                                            | 151 ms: 1.12x slower                                                                                                  |
| scimark_monte_carlo      | 82.0 ms                                                                                                           | 93.7 ms: 1.14x slower                                                                                                 |
| raytrace                 | 301 ms                                                                                                            | 352 ms: 1.17x slower                                                                                                  |
| deepcopy                 | 332 us                                                                                                            | 388 us: 1.17x slower                                                                                                  |
| sqlglot_normalize        | 127 ms                                                                                                            | 149 ms: 1.17x slower                                                                                                  |
| tornado_http             | 124 ms                                                                                                            | 147 ms: 1.18x slower                                                                                                  |
| comprehensions           | 20.4 us                                                                                                           | 24.6 us: 1.20x slower                                                                                                 |
| pycparser                | 1.23 sec                                                                                                          | 1.49 sec: 1.21x slower                                                                                                |
| sqlglot_parse            | 1.42 ms                                                                                                           | 1.73 ms: 1.22x slower                                                                                                 |
| django_template          | 41.7 ms                                                                                                           | 51.4 ms: 1.23x slower                                                                                                 |
| genshi_text              | 27.5 ms                                                                                                           | 34.1 ms: 1.24x slower                                                                                                 |
| sqlglot_optimize         | 62.5 ms                                                                                                           | 77.4 ms: 1.24x slower                                                                                                 |
| nqueens                  | 98.6 ms                                                                                                           | 124 ms: 1.26x slower                                                                                                  |
| richards_super           | 59.5 ms                                                                                                           | 75.0 ms: 1.26x slower                                                                                                 |
| richards                 | 52.8 ms                                                                                                           | 66.8 ms: 1.27x slower                                                                                                 |
| sqlglot_transpile        | 1.73 ms                                                                                                           | 2.19 ms: 1.27x slower                                                                                                 |
| docutils                 | 3.05 sec                                                                                                          | 3.94 sec: 1.29x slower                                                                                                |
| 2to3                     | 293 ms                                                                                                            | 380 ms: 1.29x slower                                                                                                  |
| pylint                   | 359 ms                                                                                                            | 466 ms: 1.30x slower                                                                                                  |
| sympy_expand             | 464 ms                                                                                                            | 606 ms: 1.31x slower                                                                                                  |
| dulwich_log              | 58.8 ms                                                                                                           | 77.7 ms: 1.32x slower                                                                                                 |
| genshi_xml               | 60.6 ms                                                                                                           | 80.1 ms: 1.32x slower                                                                                                 |
| chaos                    | 68.5 ms                                                                                                           | 91.4 ms: 1.33x slower                                                                                                 |
| pprint_safe_repr         | 914 ms                                                                                                            | 1.25 sec: 1.37x slower                                                                                                |
| go                       | 138 ms                                                                                                            | 188 ms: 1.37x slower                                                                                                  |
| pprint_pformat           | 1.89 sec                                                                                                          | 2.59 sec: 1.37x slower                                                                                                |
| sympy_integrate          | 20.8 ms                                                                                                           | 28.5 ms: 1.38x slower                                                                                                 |
| sympy_str                | 265 ms                                                                                                            | 366 ms: 1.38x slower                                                                                                  |
| hexiom                   | 7.17 ms                                                                                                           | 10.2 ms: 1.42x slower                                                                                                 |
| sympy_sum                | 143 ms                                                                                                            | 214 ms: 1.50x slower                                                                                                  |
| regex_compile            | 125 ms                                                                                                            | 188 ms: 1.51x slower                                                                                                  |
| generators               | 35.1 ms                                                                                                           | 57.3 ms: 1.63x slower                                                                                                 |
| unpack_sequence          | 54.0 ns                                                                                                           | 149 ns: 2.75x slower                                                                                                  |
| Geometric mean           | (ref)                                                                                                             | 1.12x slower                                                                                                          |

Benchmark hidden because not significant (20): async_tree_cpu_io_mixed_tg, unpickle_list, sqlite_synth, python_startup, xml_etree_generate, pickle_dict, json_loads, pidigits, coroutines, coverage, xml_etree_process, asyncio_websockets, pickle_list, xml_etree_iterparse, gc_traversal, unpickle, regex_effbot, async_tree_memoization_tg, json_dumps, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.09x