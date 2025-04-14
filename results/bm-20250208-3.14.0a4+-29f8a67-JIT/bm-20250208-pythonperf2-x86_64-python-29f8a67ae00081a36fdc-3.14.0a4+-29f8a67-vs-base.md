# Results vs. base

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.016x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                                                                  | 290 ms: 1.03x slower                                                                                                        |
| docutils       | 2.86 sec                                                                                                                | 2.95 sec: 1.03x slower                                                                                                      |
| html5lib       | 66.8 ms                                                                                                                 | 67.9 ms: 1.02x slower                                                                                                       |
| sphinx         | 1.09 sec                                                                                                                | 1.11 sec: 1.01x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                   | 1.02x slower                                                                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp                | 376 ms                                                                                                                  | 364 ms: 1.03x faster                                                                                                        |
| coroutines                 | 21.0 ms                                                                                                                 | 20.8 ms: 1.01x faster                                                                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                                                                                | 1.58 sec: 1.00x faster                                                                                                      |
| async_tree_cpu_io_mixed_tg | 509 ms                                                                                                                  | 510 ms: 1.00x slower                                                                                                        |
| async_tree_memoization     | 350 ms                                                                                                                  | 352 ms: 1.00x slower                                                                                                        |
| async_tree_none_tg         | 279 ms                                                                                                                  | 280 ms: 1.01x slower                                                                                                        |
| async_tree_memoization_tg  | 337 ms                                                                                                                  | 339 ms: 1.01x slower                                                                                                        |
| async_tree_io              | 643 ms                                                                                                                  | 650 ms: 1.01x slower                                                                                                        |
| asyncio_websockets         | 387 ms                                                                                                                  | 394 ms: 1.02x slower                                                                                                        |
| async_generators           | 410 ms                                                                                                                  | 434 ms: 1.06x slower                                                                                                        |
| Geometric mean             | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmark hidden because not significant (3): async_tree_none, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| float          | 69.0 ms                                                                                                                 | 70.1 ms: 1.02x slower                                                                                                       |
| nbody          | 93.7 ms                                                                                                                 | 101 ms: 1.08x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                   | 1.03x slower                                                                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.09 ms                                                                                                                 | 3.11 ms: 1.01x slower                                                                                                       |
| regex_compile  | 135 ms                                                                                                                  | 137 ms: 1.02x slower                                                                                                        |
| regex_dna      | 236 ms                                                                                                                  | 241 ms: 1.02x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate   | 85.6 ms                                                                                                                 | 79.3 ms: 1.08x faster                                                                                                       |
| xml_etree_process    | 59.1 ms                                                                                                                 | 55.5 ms: 1.06x faster                                                                                                       |
| pickle               | 12.3 us                                                                                                                 | 12.1 us: 1.01x faster                                                                                                       |
| unpickle_list        | 4.89 us                                                                                                                 | 4.83 us: 1.01x faster                                                                                                       |
| unpickle_pure_python | 207 us                                                                                                                  | 206 us: 1.01x faster                                                                                                        |
| pickle_list          | 5.39 us                                                                                                                 | 5.36 us: 1.01x faster                                                                                                       |
| json_loads           | 26.7 us                                                                                                                 | 26.6 us: 1.00x faster                                                                                                       |
| xml_etree_iterparse  | 95.2 ms                                                                                                                 | 95.9 ms: 1.01x slower                                                                                                       |
| pickle_pure_python   | 328 us                                                                                                                  | 334 us: 1.02x slower                                                                                                        |
| json_dumps           | 11.5 ms                                                                                                                 | 11.8 ms: 1.02x slower                                                                                                       |
| pickle_dict          | 35.7 us                                                                                                                 | 37.3 us: 1.04x slower                                                                                                       |
| Geometric mean       | (ref)                                                                                                                   | 1.01x faster                                                                                                                |

Benchmark hidden because not significant (3): unpickle, tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.1 ms                                                                                                                 | 16.0 ms: 1.01x faster                                                                                                       |
| python_startup_no_site | 9.06 ms                                                                                                                 | 9.01 ms: 1.01x faster                                                                                                       |
| Geometric mean         | (ref)                                                                                                                   | 1.01x faster                                                                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                                                                                 | 9.79 ms: 1.09x faster                                                                                                       |
| django_template | 35.6 ms                                                                                                                 | 36.1 ms: 1.01x slower                                                                                                       |
| genshi_xml      | 53.9 ms                                                                                                                 | 56.6 ms: 1.05x slower                                                                                                       |
| Geometric mean  | (ref)                                                                                                                   | 1.01x faster                                                                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| mako                       | 10.7 ms                                                                                                                 | 9.79 ms: 1.09x faster                                                                                                       |
| xml_etree_generate         | 85.6 ms                                                                                                                 | 79.3 ms: 1.08x faster                                                                                                       |
| create_gc_cycles           | 2.85 ms                                                                                                                 | 2.67 ms: 1.07x faster                                                                                                       |
| xml_etree_process          | 59.1 ms                                                                                                                 | 55.5 ms: 1.06x faster                                                                                                       |
| deepcopy_memo              | 31.0 us                                                                                                                 | 29.4 us: 1.05x faster                                                                                                       |
| telco                      | 7.89 ms                                                                                                                 | 7.59 ms: 1.04x faster                                                                                                       |
| asyncio_tcp                | 376 ms                                                                                                                  | 364 ms: 1.03x faster                                                                                                        |
| connected_components       | 416 ms                                                                                                                  | 405 ms: 1.03x faster                                                                                                        |
| shortest_path              | 443 ms                                                                                                                  | 434 ms: 1.02x faster                                                                                                        |
| deepcopy_reduce            | 2.94 us                                                                                                                 | 2.89 us: 1.02x faster                                                                                                       |
| pickle                     | 12.3 us                                                                                                                 | 12.1 us: 1.01x faster                                                                                                       |
| unpickle_list              | 4.89 us                                                                                                                 | 4.83 us: 1.01x faster                                                                                                       |
| gc_traversal               | 6.37 ms                                                                                                                 | 6.29 ms: 1.01x faster                                                                                                       |
| coroutines                 | 21.0 ms                                                                                                                 | 20.8 ms: 1.01x faster                                                                                                       |
| sqlite_synth               | 2.80 us                                                                                                                 | 2.77 us: 1.01x faster                                                                                                       |
| python_startup             | 16.1 ms                                                                                                                 | 16.0 ms: 1.01x faster                                                                                                       |
| scimark_monte_carlo        | 61.5 ms                                                                                                                 | 61.1 ms: 1.01x faster                                                                                                       |
| unpickle_pure_python       | 207 us                                                                                                                  | 206 us: 1.01x faster                                                                                                        |
| pickle_list                | 5.39 us                                                                                                                 | 5.36 us: 1.01x faster                                                                                                       |
| python_startup_no_site     | 9.06 ms                                                                                                                 | 9.01 ms: 1.01x faster                                                                                                       |
| deepcopy                   | 287 us                                                                                                                  | 286 us: 1.00x faster                                                                                                        |
| scimark_lu                 | 95.0 ms                                                                                                                 | 94.6 ms: 1.00x faster                                                                                                       |
| json_loads                 | 26.7 us                                                                                                                 | 26.6 us: 1.00x faster                                                                                                       |
| logging_silent             | 97.8 ns                                                                                                                 | 97.4 ns: 1.00x faster                                                                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                                                                                | 1.58 sec: 1.00x faster                                                                                                      |
| async_tree_cpu_io_mixed_tg | 509 ms                                                                                                                  | 510 ms: 1.00x slower                                                                                                        |
| async_tree_memoization     | 350 ms                                                                                                                  | 352 ms: 1.00x slower                                                                                                        |
| xml_etree_iterparse        | 95.2 ms                                                                                                                 | 95.9 ms: 1.01x slower                                                                                                       |
| scimark_fft                | 302 ms                                                                                                                  | 304 ms: 1.01x slower                                                                                                        |
| async_tree_none_tg         | 279 ms                                                                                                                  | 280 ms: 1.01x slower                                                                                                        |
| async_tree_memoization_tg  | 337 ms                                                                                                                  | 339 ms: 1.01x slower                                                                                                        |
| regex_effbot               | 3.09 ms                                                                                                                 | 3.11 ms: 1.01x slower                                                                                                       |
| richards_super             | 51.6 ms                                                                                                                 | 52.1 ms: 1.01x slower                                                                                                       |
| scimark_sor                | 108 ms                                                                                                                  | 109 ms: 1.01x slower                                                                                                        |
| async_tree_io              | 643 ms                                                                                                                  | 650 ms: 1.01x slower                                                                                                        |
| sympy_sum                  | 153 ms                                                                                                                  | 154 ms: 1.01x slower                                                                                                        |
| sphinx                     | 1.09 sec                                                                                                                | 1.11 sec: 1.01x slower                                                                                                      |
| sqlalchemy_declarative     | 144 ms                                                                                                                  | 146 ms: 1.01x slower                                                                                                        |
| pycparser                  | 1.25 sec                                                                                                                | 1.26 sec: 1.01x slower                                                                                                      |
| chaos                      | 60.1 ms                                                                                                                 | 61.0 ms: 1.01x slower                                                                                                       |
| django_template            | 35.6 ms                                                                                                                 | 36.1 ms: 1.01x slower                                                                                                       |
| many_optionals             | 1.00 ms                                                                                                                 | 1.02 ms: 1.02x slower                                                                                                       |
| regex_compile              | 135 ms                                                                                                                  | 137 ms: 1.02x slower                                                                                                        |
| coverage                   | 79.5 ms                                                                                                                 | 80.8 ms: 1.02x slower                                                                                                       |
| html5lib                   | 66.8 ms                                                                                                                 | 67.9 ms: 1.02x slower                                                                                                       |
| float                      | 69.0 ms                                                                                                                 | 70.1 ms: 1.02x slower                                                                                                       |
| pickle_pure_python         | 328 us                                                                                                                  | 334 us: 1.02x slower                                                                                                        |
| thrift                     | 856 us                                                                                                                  | 872 us: 1.02x slower                                                                                                        |
| asyncio_websockets         | 387 ms                                                                                                                  | 394 ms: 1.02x slower                                                                                                        |
| sympy_integrate            | 23.2 ms                                                                                                                 | 23.6 ms: 1.02x slower                                                                                                       |
| bpe_tokeniser              | 4.55 sec                                                                                                                | 4.64 sec: 1.02x slower                                                                                                      |
| pathlib                    | 16.4 ms                                                                                                                 | 16.7 ms: 1.02x slower                                                                                                       |
| json_dumps                 | 11.5 ms                                                                                                                 | 11.8 ms: 1.02x slower                                                                                                       |
| generators                 | 28.5 ms                                                                                                                 | 29.1 ms: 1.02x slower                                                                                                       |
| regex_dna                  | 236 ms                                                                                                                  | 241 ms: 1.02x slower                                                                                                        |
| pylint                     | 315 ms                                                                                                                  | 322 ms: 1.02x slower                                                                                                        |
| sympy_str                  | 290 ms                                                                                                                  | 298 ms: 1.03x slower                                                                                                        |
| 2to3                       | 282 ms                                                                                                                  | 290 ms: 1.03x slower                                                                                                        |
| docutils                   | 2.86 sec                                                                                                                | 2.95 sec: 1.03x slower                                                                                                      |
| scimark_sparse_mat_mult    | 4.67 ms                                                                                                                 | 4.82 ms: 1.03x slower                                                                                                       |
| sqlglot_normalize          | 115 ms                                                                                                                  | 119 ms: 1.03x slower                                                                                                        |
| sympy_expand               | 494 ms                                                                                                                  | 512 ms: 1.04x slower                                                                                                        |
| sqlglot_transpile          | 1.73 ms                                                                                                                 | 1.79 ms: 1.04x slower                                                                                                       |
| bench_thread_pool          | 939 us                                                                                                                  | 975 us: 1.04x slower                                                                                                        |
| deltablue                  | 3.31 ms                                                                                                                 | 3.45 ms: 1.04x slower                                                                                                       |
| mdp                        | 2.49 sec                                                                                                                | 2.59 sec: 1.04x slower                                                                                                      |
| sqlglot_parse              | 1.35 ms                                                                                                                 | 1.40 ms: 1.04x slower                                                                                                       |
| pickle_dict                | 35.7 us                                                                                                                 | 37.3 us: 1.04x slower                                                                                                       |
| sqlglot_optimize           | 57.4 ms                                                                                                                 | 60.0 ms: 1.05x slower                                                                                                       |
| pprint_pformat             | 1.61 sec                                                                                                                | 1.68 sec: 1.05x slower                                                                                                      |
| pprint_safe_repr           | 781 ms                                                                                                                  | 819 ms: 1.05x slower                                                                                                        |
| pyflate                    | 426 ms                                                                                                                  | 447 ms: 1.05x slower                                                                                                        |
| genshi_xml                 | 53.9 ms                                                                                                                 | 56.6 ms: 1.05x slower                                                                                                       |
| fannkuch                   | 367 ms                                                                                                                  | 387 ms: 1.05x slower                                                                                                        |
| async_generators           | 410 ms                                                                                                                  | 434 ms: 1.06x slower                                                                                                        |
| typing_runtime_protocols   | 169 us                                                                                                                  | 180 us: 1.06x slower                                                                                                        |
| crypto_pyaes               | 72.9 ms                                                                                                                 | 77.5 ms: 1.06x slower                                                                                                       |
| raytrace                   | 276 ms                                                                                                                  | 296 ms: 1.07x slower                                                                                                        |
| meteor_contest             | 124 ms                                                                                                                  | 133 ms: 1.08x slower                                                                                                        |
| nbody                      | 93.7 ms                                                                                                                 | 101 ms: 1.08x slower                                                                                                        |
| comprehensions             | 17.2 us                                                                                                                 | 19.2 us: 1.12x slower                                                                                                       |
| nqueens                    | 88.6 ms                                                                                                                 | 99.6 ms: 1.12x slower                                                                                                       |
| unpack_sequence            | 50.4 ns                                                                                                                 | 58.3 ns: 1.16x slower                                                                                                       |
| hexiom                     | 6.06 ms                                                                                                                 | 7.05 ms: 1.16x slower                                                                                                       |
| go                         | 127 ms                                                                                                                  | 151 ms: 1.18x slower                                                                                                        |
| Geometric mean             | (ref)                                                                                                                   | 1.02x slower                                                                                                                |

Benchmark hidden because not significant (19): unpickle, k_core, genshi_text, tomli_loads, pidigits, regex_v8, logging_simple, logging_format, json, richards, sqlalchemy_imperative, dulwich_log, subparsers, async_tree_none, async_tree_cpu_io_mixed, spectral_norm, async_tree_io_tg, xml_etree_parse, bench_mp_pool

- Geometric mean (including insignificant results): 1.016x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x