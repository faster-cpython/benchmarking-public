# Results vs. base

- fork: brandtbucher
- ref: no_underflow
- machine: linux-x86_64
- commit hash: c781896
- commit date: 2025-02-07
- overall geometric mean: 1.007x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 260 ms                                                                 | 259 ms: 1.00x faster                                                 |
| docutils       | 2.69 sec                                                               | 2.65 sec: 1.02x faster                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|---------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| coroutines                | 22.8 ms                                                                | 22.5 ms: 1.01x faster                                                |
| async_tree_memoization    | 327 ms                                                                 | 325 ms: 1.01x faster                                                 |
| asyncio_websockets        | 553 ms                                                                 | 551 ms: 1.00x faster                                                 |
| async_generators          | 408 ms                                                                 | 409 ms: 1.00x slower                                                 |
| async_tree_memoization_tg | 317 ms                                                                 | 319 ms: 1.01x slower                                                 |
| Geometric mean            | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (6): async_tree_none, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 70.9 ms                                                                | 69.5 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.17 ms                                                                | 3.05 ms: 1.04x faster                                                |
| regex_dna      | 208 ms                                                                 | 204 ms: 1.02x faster                                                 |
| regex_compile  | 126 ms                                                                 | 125 ms: 1.00x faster                                                 |
| regex_v8       | 23.7 ms                                                                | 24.2 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps           | 11.9 ms                                                                | 11.7 ms: 1.02x faster                                                |
| json_loads           | 28.8 us                                                                | 28.6 us: 1.01x faster                                                |
| xml_etree_parse      | 138 ms                                                                 | 137 ms: 1.01x faster                                                 |
| unpickle_pure_python | 199 us                                                                 | 198 us: 1.00x faster                                                 |
| xml_etree_iterparse  | 95.5 ms                                                                | 96.4 ms: 1.01x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (4): xml_etree_generate, pickle_pure_python, tomli_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                |
| python_startup_no_site | 7.07 ms                                                                | 7.06 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 10.1 ms                                                                | 9.91 ms: 1.02x faster                                                |
| django_template | 32.6 ms                                                                | 32.0 ms: 1.02x faster                                                |
| genshi_text     | 21.8 ms                                                                | 21.4 ms: 1.02x faster                                                |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|---------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nqueens                   | 88.3 ms                                                                | 82.6 ms: 1.07x faster                                                |
| spectral_norm             | 96.1 ms                                                                | 92.0 ms: 1.04x faster                                                |
| hexiom                    | 6.62 ms                                                                | 6.35 ms: 1.04x faster                                                |
| regex_effbot              | 3.17 ms                                                                | 3.05 ms: 1.04x faster                                                |
| pprint_safe_repr          | 753 ms                                                                 | 723 ms: 1.04x faster                                                 |
| pprint_pformat            | 1.53 sec                                                               | 1.47 sec: 1.04x faster                                               |
| richards_super            | 51.4 ms                                                                | 49.7 ms: 1.04x faster                                                |
| richards                  | 45.0 ms                                                                | 43.5 ms: 1.03x faster                                                |
| go                        | 122 ms                                                                 | 118 ms: 1.03x faster                                                 |
| mdp                       | 2.56 sec                                                               | 2.49 sec: 1.03x faster                                               |
| logging_silent            | 109 ns                                                                 | 106 ns: 1.03x faster                                                 |
| regex_dna                 | 208 ms                                                                 | 204 ms: 1.02x faster                                                 |
| thrift                    | 775 us                                                                 | 759 us: 1.02x faster                                                 |
| bench_thread_pool         | 889 us                                                                 | 871 us: 1.02x faster                                                 |
| json_dumps                | 11.9 ms                                                                | 11.7 ms: 1.02x faster                                                |
| mako                      | 10.1 ms                                                                | 9.91 ms: 1.02x faster                                                |
| pyflate                   | 436 ms                                                                 | 428 ms: 1.02x faster                                                 |
| float                     | 70.9 ms                                                                | 69.5 ms: 1.02x faster                                                |
| django_template           | 32.6 ms                                                                | 32.0 ms: 1.02x faster                                                |
| fannkuch                  | 398 ms                                                                 | 390 ms: 1.02x faster                                                 |
| genshi_text               | 21.8 ms                                                                | 21.4 ms: 1.02x faster                                                |
| deltablue                 | 3.28 ms                                                                | 3.22 ms: 1.02x faster                                                |
| meteor_contest            | 108 ms                                                                 | 106 ms: 1.02x faster                                                 |
| deepcopy                  | 262 us                                                                 | 258 us: 1.02x faster                                                 |
| subparsers                | 20.6 ms                                                                | 20.3 ms: 1.02x faster                                                |
| docutils                  | 2.69 sec                                                               | 2.65 sec: 1.02x faster                                               |
| coroutines                | 22.8 ms                                                                | 22.5 ms: 1.01x faster                                                |
| typing_runtime_protocols  | 162 us                                                                 | 160 us: 1.01x faster                                                 |
| sympy_str                 | 276 ms                                                                 | 273 ms: 1.01x faster                                                 |
| generators                | 28.1 ms                                                                | 27.8 ms: 1.01x faster                                                |
| sqlalchemy_imperative     | 17.0 ms                                                                | 16.9 ms: 1.01x faster                                                |
| json                      | 5.19 ms                                                                | 5.13 ms: 1.01x faster                                                |
| sqlite_synth              | 2.75 us                                                                | 2.72 us: 1.01x faster                                                |
| raytrace                  | 274 ms                                                                 | 271 ms: 1.01x faster                                                 |
| dulwich_log               | 66.4 ms                                                                | 65.7 ms: 1.01x faster                                                |
| sqlglot_parse             | 1.28 ms                                                                | 1.27 ms: 1.01x faster                                                |
| sympy_expand              | 472 ms                                                                 | 468 ms: 1.01x faster                                                 |
| many_optionals            | 956 us                                                                 | 948 us: 1.01x faster                                                 |
| json_loads                | 28.8 us                                                                | 28.6 us: 1.01x faster                                                |
| logging_simple            | 5.63 us                                                                | 5.59 us: 1.01x faster                                                |
| sympy_sum                 | 151 ms                                                                 | 150 ms: 1.01x faster                                                 |
| sqlglot_normalize         | 107 ms                                                                 | 106 ms: 1.01x faster                                                 |
| sympy_integrate           | 20.2 ms                                                                | 20.0 ms: 1.01x faster                                                |
| async_tree_memoization    | 327 ms                                                                 | 325 ms: 1.01x faster                                                 |
| sqlalchemy_declarative    | 132 ms                                                                 | 131 ms: 1.01x faster                                                 |
| xml_etree_parse           | 138 ms                                                                 | 137 ms: 1.01x faster                                                 |
| sqlglot_transpile         | 1.59 ms                                                                | 1.58 ms: 1.01x faster                                                |
| 2to3                      | 260 ms                                                                 | 259 ms: 1.00x faster                                                 |
| regex_compile             | 126 ms                                                                 | 125 ms: 1.00x faster                                                 |
| bench_mp_pool             | 81.1 ms                                                                | 80.8 ms: 1.00x faster                                                |
| unpickle_pure_python      | 199 us                                                                 | 198 us: 1.00x faster                                                 |
| asyncio_websockets        | 553 ms                                                                 | 551 ms: 1.00x faster                                                 |
| sqlglot_optimize          | 53.7 ms                                                                | 53.6 ms: 1.00x faster                                                |
| python_startup            | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                |
| python_startup_no_site    | 7.07 ms                                                                | 7.06 ms: 1.00x faster                                                |
| async_generators          | 408 ms                                                                 | 409 ms: 1.00x slower                                                 |
| create_gc_cycles          | 2.46 ms                                                                | 2.46 ms: 1.00x slower                                                |
| bpe_tokeniser             | 4.35 sec                                                               | 4.36 sec: 1.00x slower                                               |
| connected_components      | 439 ms                                                                 | 441 ms: 1.00x slower                                                 |
| async_tree_memoization_tg | 317 ms                                                                 | 319 ms: 1.01x slower                                                 |
| xml_etree_iterparse       | 95.5 ms                                                                | 96.4 ms: 1.01x slower                                                |
| telco                     | 7.60 ms                                                                | 7.68 ms: 1.01x slower                                                |
| deepcopy_reduce           | 2.66 us                                                                | 2.69 us: 1.01x slower                                                |
| scimark_lu                | 114 ms                                                                 | 115 ms: 1.01x slower                                                 |
| scimark_monte_carlo       | 65.5 ms                                                                | 66.2 ms: 1.01x slower                                                |
| scimark_fft               | 310 ms                                                                 | 314 ms: 1.01x slower                                                 |
| regex_v8                  | 23.7 ms                                                                | 24.2 ms: 1.02x slower                                                |
| scimark_sparse_mat_mult   | 4.47 ms                                                                | 4.61 ms: 1.03x slower                                                |
| pycparser                 | 1.11 sec                                                               | 1.16 sec: 1.05x slower                                               |
| gc_traversal              | 4.58 ms                                                                | 4.94 ms: 1.08x slower                                                |
| Geometric mean            | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (26): html5lib, pylint, logging_format, genshi_xml, xml_etree_generate, scimark_sor, async_tree_none, comprehensions, deepcopy_memo, sphinx, shortest_path, pickle_pure_python, tomli_loads, pidigits, async_tree_io, async_tree_cpu_io_mixed_tg, chaos, k_core, coverage, nbody, pathlib, xml_etree_process, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io_tg, crypto_pyaes

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 99.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x