# Results vs. base

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-aarch64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.02x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                   | 373 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                |

Benchmark hidden because not significant (4): docutils, html5lib, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp     | 629 ms                                                                   | 618 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl | 2.27 sec                                                                 | 2.26 sec: 1.01x faster                                                      |
| Geometric mean  | (ref)                                                                    | 1.00x slower                                                                |

Benchmark hidden because not significant (11): async_generators, asyncio_websockets, async_tree_io_tg, async_tree_none_tg, async_tree_io, async_tree_none, coroutines, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 98.0 ms                                                                  | 91.9 ms: 1.07x faster                                                       |
| nbody          | 115 ms                                                                   | 108 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                                    | 1.04x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 169 ms                                                                   | 165 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                                |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.64 sec                                                                 | 2.49 sec: 1.06x faster                                                      |
| xml_etree_process    | 80.5 ms                                                                  | 78.0 ms: 1.03x faster                                                       |
| pickle_pure_python   | 389 us                                                                   | 377 us: 1.03x faster                                                        |
| xml_etree_generate   | 111 ms                                                                   | 109 ms: 1.02x faster                                                        |
| pickle_list          | 5.26 us                                                                  | 5.19 us: 1.01x faster                                                       |
| unpickle_pure_python | 268 us                                                                   | 264 us: 1.01x faster                                                        |
| unpickle             | 19.0 us                                                                  | 19.2 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                                    | 1.01x faster                                                                |

Benchmark hidden because not significant (7): unpickle_list, xml_etree_iterparse, pickle_dict, json_loads, pickle, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.74 ms                                                                  | 8.83 ms: 1.01x slower                                                       |
| python_startup         | 14.6 ms                                                                  | 14.8 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 51.1 ms                                                                  | 49.0 ms: 1.04x faster                                                       |
| genshi_text     | 33.5 ms                                                                  | 32.2 ms: 1.04x faster                                                       |
| genshi_xml      | 81.5 ms                                                                  | 78.6 ms: 1.04x faster                                                       |
| mako            | 13.1 ms                                                                  | 12.8 ms: 1.03x faster                                                       |
| Geometric mean  | (ref)                                                                    | 1.04x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|--------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators               | 59.0 ms                                                                  | 48.3 ms: 1.22x faster                                                       |
| unpack_sequence          | 145 ns                                                                   | 129 ns: 1.12x faster                                                        |
| deltablue                | 4.52 ms                                                                  | 4.15 ms: 1.09x faster                                                       |
| crypto_pyaes             | 90.2 ms                                                                  | 83.0 ms: 1.09x faster                                                       |
| chaos                    | 85.0 ms                                                                  | 78.8 ms: 1.08x faster                                                       |
| scimark_fft              | 456 ms                                                                   | 424 ms: 1.08x faster                                                        |
| hexiom                   | 10.2 ms                                                                  | 9.54 ms: 1.07x faster                                                       |
| fannkuch                 | 495 ms                                                                   | 463 ms: 1.07x faster                                                        |
| sqlglot_parse            | 1.70 ms                                                                  | 1.59 ms: 1.07x faster                                                       |
| float                    | 98.0 ms                                                                  | 91.9 ms: 1.07x faster                                                       |
| spectral_norm            | 155 ms                                                                   | 146 ms: 1.06x faster                                                        |
| tomli_loads              | 2.64 sec                                                                 | 2.49 sec: 1.06x faster                                                      |
| nbody                    | 115 ms                                                                   | 108 ms: 1.06x faster                                                        |
| comprehensions           | 24.7 us                                                                  | 23.3 us: 1.06x faster                                                       |
| richards                 | 64.3 ms                                                                  | 60.9 ms: 1.06x faster                                                       |
| pyflate                  | 612 ms                                                                   | 581 ms: 1.05x faster                                                        |
| richards_super           | 71.5 ms                                                                  | 67.9 ms: 1.05x faster                                                       |
| pprint_pformat           | 2.54 sec                                                                 | 2.42 sec: 1.05x faster                                                      |
| deepcopy_reduce          | 3.96 us                                                                  | 3.78 us: 1.05x faster                                                       |
| scimark_monte_carlo      | 90.1 ms                                                                  | 86.4 ms: 1.04x faster                                                       |
| django_template          | 51.1 ms                                                                  | 49.0 ms: 1.04x faster                                                       |
| sqlglot_transpile        | 2.18 ms                                                                  | 2.10 ms: 1.04x faster                                                       |
| bpe_tokeniser            | 5.92 sec                                                                 | 5.69 sec: 1.04x faster                                                      |
| meteor_contest           | 125 ms                                                                   | 120 ms: 1.04x faster                                                        |
| nqueens                  | 122 ms                                                                   | 117 ms: 1.04x faster                                                        |
| genshi_text              | 33.5 ms                                                                  | 32.2 ms: 1.04x faster                                                       |
| genshi_xml               | 81.5 ms                                                                  | 78.6 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult  | 7.19 ms                                                                  | 6.94 ms: 1.04x faster                                                       |
| xml_etree_process        | 80.5 ms                                                                  | 78.0 ms: 1.03x faster                                                       |
| sqlglot_optimize         | 81.8 ms                                                                  | 79.3 ms: 1.03x faster                                                       |
| sqlite_synth             | 3.92 us                                                                  | 3.80 us: 1.03x faster                                                       |
| sympy_str                | 358 ms                                                                   | 347 ms: 1.03x faster                                                        |
| sqlglot_normalize        | 156 ms                                                                   | 151 ms: 1.03x faster                                                        |
| mako                     | 13.1 ms                                                                  | 12.8 ms: 1.03x faster                                                       |
| deepcopy                 | 377 us                                                                   | 366 us: 1.03x faster                                                        |
| pickle_pure_python       | 389 us                                                                   | 377 us: 1.03x faster                                                        |
| go                       | 184 ms                                                                   | 179 ms: 1.03x faster                                                        |
| pprint_safe_repr         | 1.20 sec                                                                 | 1.17 sec: 1.03x faster                                                      |
| regex_compile            | 169 ms                                                                   | 165 ms: 1.02x faster                                                        |
| raytrace                 | 358 ms                                                                   | 350 ms: 1.02x faster                                                        |
| 2to3                     | 381 ms                                                                   | 373 ms: 1.02x faster                                                        |
| scimark_lu               | 151 ms                                                                   | 148 ms: 1.02x faster                                                        |
| xml_etree_generate       | 111 ms                                                                   | 109 ms: 1.02x faster                                                        |
| sympy_expand             | 592 ms                                                                   | 580 ms: 1.02x faster                                                        |
| deepcopy_memo            | 38.9 us                                                                  | 38.1 us: 1.02x faster                                                       |
| json                     | 5.60 ms                                                                  | 5.48 ms: 1.02x faster                                                       |
| pycparser                | 1.48 sec                                                                 | 1.45 sec: 1.02x faster                                                      |
| typing_runtime_protocols | 214 us                                                                   | 210 us: 1.02x faster                                                        |
| sympy_sum                | 215 ms                                                                   | 211 ms: 1.02x faster                                                        |
| asyncio_tcp              | 629 ms                                                                   | 618 ms: 1.02x faster                                                        |
| logging_simple           | 7.47 us                                                                  | 7.35 us: 1.02x faster                                                       |
| pickle_list              | 5.26 us                                                                  | 5.19 us: 1.01x faster                                                       |
| unpickle_pure_python     | 268 us                                                                   | 264 us: 1.01x faster                                                        |
| logging_silent           | 132 ns                                                                   | 131 ns: 1.01x faster                                                        |
| mdp                      | 3.49 sec                                                                 | 3.46 sec: 1.01x faster                                                      |
| asyncio_tcp_ssl          | 2.27 sec                                                                 | 2.26 sec: 1.01x faster                                                      |
| python_startup_no_site   | 8.74 ms                                                                  | 8.83 ms: 1.01x slower                                                       |
| unpickle                 | 19.0 us                                                                  | 19.2 us: 1.01x slower                                                       |
| python_startup           | 14.6 ms                                                                  | 14.8 ms: 1.01x slower                                                       |
| thrift                   | 957 us                                                                   | 977 us: 1.02x slower                                                        |
| dulwich_log              | 78.0 ms                                                                  | 80.8 ms: 1.04x slower                                                       |
| pathlib                  | 21.6 ms                                                                  | 22.6 ms: 1.05x slower                                                       |
| bench_mp_pool            | 1.59 sec                                                                 | 2.16 sec: 1.36x slower                                                      |
| Geometric mean           | (ref)                                                                    | 1.02x faster                                                                |

Benchmark hidden because not significant (35): logging_format, gc_traversal, pylint, coverage, telco, async_generators, html5lib, unpickle_list, xml_etree_iterparse, sympy_integrate, pickle_dict, json_loads, asyncio_websockets, sphinx, pickle, docutils, json_dumps, pidigits, bench_thread_pool, async_tree_io_tg, regex_dna, async_tree_none_tg, create_gc_cycles, async_tree_io, regex_effbot, async_tree_none, coroutines, async_tree_cpu_io_mixed, scimark_sor, xml_etree_parse, async_tree_memoization, regex_v8, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, tornado_http

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x