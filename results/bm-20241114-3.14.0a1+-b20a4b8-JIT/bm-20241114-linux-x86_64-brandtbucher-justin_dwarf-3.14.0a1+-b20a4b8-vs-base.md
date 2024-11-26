# Results vs. base

- fork: brandtbucher
- ref: justin_dwarf
- machine: linux-x86_64
- commit hash: b20a4b8
- commit date: 2024-11-14
- overall geometric mean: 1.132x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 1.29 sec: 4.60x slower                                               |
| docutils       | 2.95 sec                                                               | 6.96 sec: 2.36x slower                                               |
| html5lib       | 67.0 ms                                                                | 69.5 ms: 1.04x slower                                                |
| sphinx         | 1.18 sec                                                               | 3.03 sec: 2.57x slower                                               |
| Geometric mean | (ref)                                                                  | 2.32x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| coroutines       | 23.2 ms                                                                | 23.1 ms: 1.01x faster                                                |
| async_generators | 456 ms                                                                 | 464 ms: 1.02x slower                                                 |
| async_tree_none  | 332 ms                                                                 | 339 ms: 1.02x slower                                                 |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x slower                                                 |
| float          | 76.7 ms                                                                | 80.1 ms: 1.04x slower                                                |
| nbody          | 82.3 ms                                                                | 89.5 ms: 1.09x slower                                                |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                                | 3.66 ms: 1.03x faster                                                |
| regex_dna      | 216 ms                                                                 | 214 ms: 1.01x faster                                                 |
| regex_compile  | 140 ms                                                                 | 229 ms: 1.63x slower                                                 |
| regex_v8       | 24.6 ms                                                                | 48.4 ms: 1.97x slower                                                |
| Geometric mean | (ref)                                                                  | 1.33x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.00 sec                                                               | 2.05 sec: 1.02x slower                                               |
| xml_etree_generate   | 79.6 ms                                                                | 83.1 ms: 1.04x slower                                                |
| unpickle_pure_python | 219 us                                                                 | 231 us: 1.05x slower                                                 |
| xml_etree_iterparse  | 101 ms                                                                 | 106 ms: 1.06x slower                                                 |
| xml_etree_process    | 56.0 ms                                                                | 60.4 ms: 1.08x slower                                                |
| json_dumps           | 11.1 ms                                                                | 13.7 ms: 1.23x slower                                                |
| json_loads           | 26.8 us                                                                | 34.2 us: 1.27x slower                                                |
| pickle_pure_python   | 321 us                                                                 | 628 us: 1.96x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.17x slower                                                         |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                                | 7.16 ms: 1.00x slower                                                |
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text    | 25.1 ms                                                                | 26.2 ms: 1.04x slower                                                |
| mako           | 10.3 ms                                                                | 10.7 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                         |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| gc_traversal             | 4.74 ms                                                                | 4.49 ms: 1.05x faster                                                |
| regex_effbot             | 3.77 ms                                                                | 3.66 ms: 1.03x faster                                                |
| coverage                 | 84.9 ms                                                                | 83.2 ms: 1.02x faster                                                |
| create_gc_cycles         | 2.71 ms                                                                | 2.69 ms: 1.01x faster                                                |
| regex_dna                | 216 ms                                                                 | 214 ms: 1.01x faster                                                 |
| coroutines               | 23.2 ms                                                                | 23.1 ms: 1.01x faster                                                |
| pidigits                 | 187 ms                                                                 | 187 ms: 1.00x slower                                                 |
| python_startup_no_site   | 7.14 ms                                                                | 7.16 ms: 1.00x slower                                                |
| python_startup           | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                |
| pathlib                  | 16.1 ms                                                                | 16.2 ms: 1.01x slower                                                |
| raytrace                 | 283 ms                                                                 | 286 ms: 1.01x slower                                                 |
| typing_runtime_protocols | 170 us                                                                 | 172 us: 1.01x slower                                                 |
| richards_super           | 47.1 ms                                                                | 47.7 ms: 1.01x slower                                                |
| mdp                      | 2.62 sec                                                               | 2.65 sec: 1.01x slower                                               |
| bench_thread_pool        | 889 us                                                                 | 906 us: 1.02x slower                                                 |
| async_generators         | 456 ms                                                                 | 464 ms: 1.02x slower                                                 |
| async_tree_none          | 332 ms                                                                 | 339 ms: 1.02x slower                                                 |
| logging_format           | 6.17 us                                                                | 6.31 us: 1.02x slower                                                |
| sqlglot_transpile        | 1.69 ms                                                                | 1.73 ms: 1.02x slower                                                |
| sqlglot_parse            | 1.33 ms                                                                | 1.36 ms: 1.02x slower                                                |
| tomli_loads              | 2.00 sec                                                               | 2.05 sec: 1.02x slower                                               |
| scimark_lu               | 113 ms                                                                 | 117 ms: 1.03x slower                                                 |
| meteor_contest           | 109 ms                                                                 | 112 ms: 1.03x slower                                                 |
| bpe_tokeniser            | 4.53 sec                                                               | 4.66 sec: 1.03x slower                                               |
| shortest_path            | 482 ms                                                                 | 498 ms: 1.03x slower                                                 |
| nqueens                  | 87.9 ms                                                                | 91.1 ms: 1.04x slower                                                |
| html5lib                 | 67.0 ms                                                                | 69.5 ms: 1.04x slower                                                |
| logging_simple           | 5.56 us                                                                | 5.78 us: 1.04x slower                                                |
| xml_etree_generate       | 79.6 ms                                                                | 83.1 ms: 1.04x slower                                                |
| connected_components     | 437 ms                                                                 | 456 ms: 1.04x slower                                                 |
| pprint_pformat           | 1.51 sec                                                               | 1.58 sec: 1.04x slower                                               |
| genshi_text              | 25.1 ms                                                                | 26.2 ms: 1.04x slower                                                |
| float                    | 76.7 ms                                                                | 80.1 ms: 1.04x slower                                                |
| mako                     | 10.3 ms                                                                | 10.7 ms: 1.05x slower                                                |
| fannkuch                 | 389 ms                                                                 | 407 ms: 1.05x slower                                                 |
| scimark_monte_carlo      | 64.8 ms                                                                | 67.9 ms: 1.05x slower                                                |
| crypto_pyaes             | 68.5 ms                                                                | 71.9 ms: 1.05x slower                                                |
| unpickle_pure_python     | 219 us                                                                 | 231 us: 1.05x slower                                                 |
| pprint_safe_repr         | 724 ms                                                                 | 763 ms: 1.05x slower                                                 |
| richards                 | 40.7 ms                                                                | 42.9 ms: 1.05x slower                                                |
| xml_etree_iterparse      | 101 ms                                                                 | 106 ms: 1.06x slower                                                 |
| chaos                    | 59.1 ms                                                                | 62.6 ms: 1.06x slower                                                |
| go                       | 133 ms                                                                 | 141 ms: 1.06x slower                                                 |
| scimark_sor              | 119 ms                                                                 | 126 ms: 1.06x slower                                                 |
| deepcopy                 | 267 us                                                                 | 284 us: 1.06x slower                                                 |
| scimark_fft              | 318 ms                                                                 | 338 ms: 1.06x slower                                                 |
| deepcopy_reduce          | 2.66 us                                                                | 2.83 us: 1.07x slower                                                |
| scimark_sparse_mat_mult  | 4.62 ms                                                                | 4.94 ms: 1.07x slower                                                |
| spectral_norm            | 115 ms                                                                 | 123 ms: 1.07x slower                                                 |
| comprehensions           | 17.5 us                                                                | 18.8 us: 1.07x slower                                                |
| deepcopy_memo            | 29.6 us                                                                | 31.9 us: 1.08x slower                                                |
| hexiom                   | 7.08 ms                                                                | 7.65 ms: 1.08x slower                                                |
| xml_etree_process        | 56.0 ms                                                                | 60.4 ms: 1.08x slower                                                |
| generators               | 36.6 ms                                                                | 39.7 ms: 1.08x slower                                                |
| deltablue                | 3.31 ms                                                                | 3.59 ms: 1.08x slower                                                |
| nbody                    | 82.3 ms                                                                | 89.5 ms: 1.09x slower                                                |
| logging_silent           | 102 ns                                                                 | 111 ns: 1.09x slower                                                 |
| pycparser                | 1.16 sec                                                               | 1.28 sec: 1.10x slower                                               |
| sympy_integrate          | 23.6 ms                                                                | 26.5 ms: 1.12x slower                                                |
| sympy_expand             | 509 ms                                                                 | 601 ms: 1.18x slower                                                 |
| sqlite_synth             | 2.80 us                                                                | 3.35 us: 1.20x slower                                                |
| pyflate                  | 449 ms                                                                 | 543 ms: 1.21x slower                                                 |
| json_dumps               | 11.1 ms                                                                | 13.7 ms: 1.23x slower                                                |
| json                     | 4.98 ms                                                                | 6.27 ms: 1.26x slower                                                |
| bench_mp_pool            | 84.8 ms                                                                | 108 ms: 1.27x slower                                                 |
| json_loads               | 26.8 us                                                                | 34.2 us: 1.27x slower                                                |
| telco                    | 7.67 ms                                                                | 10.5 ms: 1.37x slower                                                |
| thrift                   | 779 us                                                                 | 1.09 ms: 1.40x slower                                                |
| dulwich_log              | 67.7 ms                                                                | 97.0 ms: 1.43x slower                                                |
| sympy_str                | 305 ms                                                                 | 457 ms: 1.50x slower                                                 |
| regex_compile            | 140 ms                                                                 | 229 ms: 1.63x slower                                                 |
| sqlglot_normalize        | 114 ms                                                                 | 197 ms: 1.72x slower                                                 |
| sympy_sum                | 176 ms                                                                 | 317 ms: 1.80x slower                                                 |
| sqlalchemy_declarative   | 148 ms                                                                 | 283 ms: 1.92x slower                                                 |
| pickle_pure_python       | 321 us                                                                 | 628 us: 1.96x slower                                                 |
| regex_v8                 | 24.6 ms                                                                | 48.4 ms: 1.97x slower                                                |
| sqlglot_optimize         | 60.3 ms                                                                | 142 ms: 2.35x slower                                                 |
| docutils                 | 2.95 sec                                                               | 6.96 sec: 2.36x slower                                               |
| sphinx                   | 1.18 sec                                                               | 3.03 sec: 2.57x slower                                               |
| 2to3                     | 280 ms                                                                 | 1.29 sec: 4.60x slower                                               |
| pylint                   | 380 ms                                                                 | 2.05 sec: 5.41x slower                                               |
| Geometric mean           | (ref)                                                                  | 1.17x slower                                                         |

Benchmark hidden because not significant (14): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io_tg, django_template, async_tree_none_tg, async_tree_memoization_tg, sqlalchemy_imperative, async_tree_memoization, async_tree_io, k_core, xml_etree_parse, genshi_xml, djangocms
Ignored benchmarks (2) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: many_optionals, subparsers

- Geometric mean (including insignificant results): 1.132x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.04x