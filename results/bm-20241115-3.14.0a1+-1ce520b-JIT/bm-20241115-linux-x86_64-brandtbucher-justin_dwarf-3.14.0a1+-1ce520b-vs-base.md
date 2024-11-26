# Results vs. base

- fork: brandtbucher
- ref: justin_dwarf
- machine: linux-x86_64
- commit hash: 1ce520b
- commit date: 2024-11-15
- overall geometric mean: 1.009x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 276 ms: 1.01x faster                                                 |
| docutils       | 2.95 sec                                                               | 3.00 sec: 1.02x slower                                               |
| html5lib       | 67.0 ms                                                                | 66.4 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                | 22.5 ms: 1.03x faster                                                |
| async_tree_io_tg           | 978 ms                                                                 | 964 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 561 ms: 1.01x faster                                                 |
| async_generators           | 456 ms                                                                 | 454 ms: 1.00x faster                                                 |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_memoization_tg, async_tree_io, async_tree_none, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x slower                                                 |
| nbody          | 82.3 ms                                                                | 83.5 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 140 ms                                                                 | 138 ms: 1.01x faster                                                 |
| regex_v8       | 24.6 ms                                                                | 24.5 ms: 1.00x faster                                                |
| regex_effbot   | 3.77 ms                                                                | 3.79 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.00 sec                                                               | 1.93 sec: 1.03x faster                                               |
| json_dumps           | 11.1 ms                                                                | 10.7 ms: 1.03x faster                                                |
| xml_etree_process    | 56.0 ms                                                                | 54.5 ms: 1.03x faster                                                |
| xml_etree_generate   | 79.6 ms                                                                | 78.6 ms: 1.01x faster                                                |
| unpickle_pure_python | 219 us                                                                 | 217 us: 1.01x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                                 | 99.9 ms: 1.01x faster                                                |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (3): xml_etree_parse, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                                | 7.11 ms: 1.00x faster                                                |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 34.3 ms                                                                | 33.4 ms: 1.02x faster                                                |
| mako            | 10.3 ms                                                                | 10.3 ms: 1.01x slower                                                |
| genshi_text     | 25.1 ms                                                                | 26.3 ms: 1.05x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                                | 4.36 ms: 1.09x faster                                                |
| generators                 | 36.6 ms                                                                | 34.3 ms: 1.07x faster                                                |
| sqlglot_optimize           | 60.3 ms                                                                | 57.4 ms: 1.05x faster                                                |
| richards                   | 40.7 ms                                                                | 38.9 ms: 1.05x faster                                                |
| tomli_loads                | 2.00 sec                                                               | 1.93 sec: 1.03x faster                                               |
| fannkuch                   | 389 ms                                                                 | 377 ms: 1.03x faster                                                 |
| coroutines                 | 23.2 ms                                                                | 22.5 ms: 1.03x faster                                                |
| go                         | 133 ms                                                                 | 129 ms: 1.03x faster                                                 |
| json_dumps                 | 11.1 ms                                                                | 10.7 ms: 1.03x faster                                                |
| bpe_tokeniser              | 4.53 sec                                                               | 4.39 sec: 1.03x faster                                               |
| comprehensions             | 17.5 us                                                                | 17.0 us: 1.03x faster                                                |
| connected_components       | 437 ms                                                                 | 425 ms: 1.03x faster                                                 |
| raytrace                   | 283 ms                                                                 | 275 ms: 1.03x faster                                                 |
| xml_etree_process          | 56.0 ms                                                                | 54.5 ms: 1.03x faster                                                |
| richards_super             | 47.1 ms                                                                | 45.8 ms: 1.03x faster                                                |
| sqlglot_normalize          | 114 ms                                                                 | 112 ms: 1.02x faster                                                 |
| django_template            | 34.3 ms                                                                | 33.4 ms: 1.02x faster                                                |
| pprint_pformat             | 1.51 sec                                                               | 1.48 sec: 1.02x faster                                               |
| meteor_contest             | 109 ms                                                                 | 107 ms: 1.02x faster                                                 |
| typing_runtime_protocols   | 170 us                                                                 | 167 us: 1.02x faster                                                 |
| sympy_sum                  | 176 ms                                                                 | 173 ms: 1.02x faster                                                 |
| k_core                     | 3.62 sec                                                               | 3.56 sec: 1.02x faster                                               |
| shortest_path              | 482 ms                                                                 | 474 ms: 1.02x faster                                                 |
| deepcopy_memo              | 29.6 us                                                                | 29.2 us: 1.02x faster                                                |
| pprint_safe_repr           | 724 ms                                                                 | 713 ms: 1.02x faster                                                 |
| hexiom                     | 7.08 ms                                                                | 6.98 ms: 1.02x faster                                                |
| 2to3                       | 280 ms                                                                 | 276 ms: 1.01x faster                                                 |
| async_tree_io_tg           | 978 ms                                                                 | 964 ms: 1.01x faster                                                 |
| sympy_integrate            | 23.6 ms                                                                | 23.2 ms: 1.01x faster                                                |
| coverage                   | 84.9 ms                                                                | 83.7 ms: 1.01x faster                                                |
| regex_compile              | 140 ms                                                                 | 138 ms: 1.01x faster                                                 |
| xml_etree_generate         | 79.6 ms                                                                | 78.6 ms: 1.01x faster                                                |
| sqlite_synth               | 2.80 us                                                                | 2.76 us: 1.01x faster                                                |
| scimark_monte_carlo        | 64.8 ms                                                                | 63.9 ms: 1.01x faster                                                |
| subparsers                 | 21.4 ms                                                                | 21.1 ms: 1.01x faster                                                |
| logging_silent             | 102 ns                                                                 | 101 ns: 1.01x faster                                                 |
| deltablue                  | 3.31 ms                                                                | 3.27 ms: 1.01x faster                                                |
| scimark_sparse_mat_mult    | 4.62 ms                                                                | 4.57 ms: 1.01x faster                                                |
| sympy_str                  | 305 ms                                                                 | 302 ms: 1.01x faster                                                 |
| telco                      | 7.67 ms                                                                | 7.61 ms: 1.01x faster                                                |
| html5lib                   | 67.0 ms                                                                | 66.4 ms: 1.01x faster                                                |
| sqlglot_parse              | 1.33 ms                                                                | 1.32 ms: 1.01x faster                                                |
| unpickle_pure_python       | 219 us                                                                 | 217 us: 1.01x faster                                                 |
| sqlglot_transpile          | 1.69 ms                                                                | 1.68 ms: 1.01x faster                                                |
| sqlalchemy_declarative     | 148 ms                                                                 | 147 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 561 ms: 1.01x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                                 | 99.9 ms: 1.01x faster                                                |
| scimark_sor                | 119 ms                                                                 | 118 ms: 1.00x faster                                                 |
| async_generators           | 456 ms                                                                 | 454 ms: 1.00x faster                                                 |
| regex_v8                   | 24.6 ms                                                                | 24.5 ms: 1.00x faster                                                |
| bench_thread_pool          | 889 us                                                                 | 886 us: 1.00x faster                                                 |
| python_startup_no_site     | 7.14 ms                                                                | 7.11 ms: 1.00x faster                                                |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                |
| create_gc_cycles           | 2.71 ms                                                                | 2.70 ms: 1.00x faster                                                |
| pidigits                   | 187 ms                                                                 | 187 ms: 1.00x slower                                                 |
| spectral_norm              | 115 ms                                                                 | 115 ms: 1.00x slower                                                 |
| dulwich_log                | 67.7 ms                                                                | 68.0 ms: 1.00x slower                                                |
| bench_mp_pool              | 84.8 ms                                                                | 85.2 ms: 1.01x slower                                                |
| mako                       | 10.3 ms                                                                | 10.3 ms: 1.01x slower                                                |
| regex_effbot               | 3.77 ms                                                                | 3.79 ms: 1.01x slower                                                |
| crypto_pyaes               | 68.5 ms                                                                | 68.9 ms: 1.01x slower                                                |
| thrift                     | 779 us                                                                 | 787 us: 1.01x slower                                                 |
| deepcopy                   | 267 us                                                                 | 271 us: 1.01x slower                                                 |
| logging_simple             | 5.56 us                                                                | 5.63 us: 1.01x slower                                                |
| nbody                      | 82.3 ms                                                                | 83.5 ms: 1.01x slower                                                |
| docutils                   | 2.95 sec                                                               | 3.00 sec: 1.02x slower                                               |
| scimark_fft                | 318 ms                                                                 | 326 ms: 1.03x slower                                                 |
| deepcopy_reduce            | 2.66 us                                                                | 2.74 us: 1.03x slower                                                |
| mdp                        | 2.62 sec                                                               | 2.73 sec: 1.04x slower                                               |
| genshi_text                | 25.1 ms                                                                | 26.3 ms: 1.05x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (27): scimark_lu, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_memoization_tg, pylint, async_tree_io, chaos, xml_etree_parse, async_tree_none, sphinx, float, sqlalchemy_imperative, genshi_xml, pycparser, json, pyflate, sympy_expand, pickle_pure_python, regex_dna, many_optionals, asyncio_websockets, pathlib, json_loads, logging_format, async_tree_none_tg, djangocms, nqueens

- Geometric mean (including insignificant results): 1.009x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x