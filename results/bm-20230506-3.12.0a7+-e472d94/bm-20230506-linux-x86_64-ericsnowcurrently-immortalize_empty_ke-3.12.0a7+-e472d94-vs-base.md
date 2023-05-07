
# Results vs. base

- fork: ericsnowcurrently
- ref: immortalize_empty_ke
- machine: linux-x86_64
- commit hash: e472d94
- commit date: 2023-05-06
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 270 ms                                                                 | 270 ms: 1.00x slower                                                              |
| docutils       | 2.73 sec                                                               | 2.72 sec: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 81.2 ms                                                                | 82.0 ms: 1.01x slower                                                             |
| nbody          | 90.6 ms                                                                | 93.1 ms: 1.03x slower                                                             |
| pidigits       | 189 ms                                                                 | 197 ms: 1.05x slower                                                              |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 207 ms                                                                 | 211 ms: 1.02x slower                                                              |
| regex_v8       | 22.0 ms                                                                | 22.8 ms: 1.04x slower                                                             |
| regex_effbot   | 3.60 ms                                                                | 3.74 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                      |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 220 us                                                                 | 218 us: 1.01x faster                                                              |
| unpickle_list        | 4.99 us                                                                | 4.95 us: 1.01x faster                                                             |
| pickle_dict          | 31.6 us                                                                | 31.4 us: 1.01x faster                                                             |
| xml_etree_iterparse  | 104 ms                                                                 | 104 ms: 1.01x faster                                                              |
| pickle_pure_python   | 316 us                                                                 | 318 us: 1.00x slower                                                              |
| json_loads           | 25.3 us                                                                | 25.5 us: 1.01x slower                                                             |
| pickle_list          | 4.54 us                                                                | 4.58 us: 1.01x slower                                                             |
| xml_etree_generate   | 84.9 ms                                                                | 85.9 ms: 1.01x slower                                                             |
| xml_etree_process    | 59.3 ms                                                                | 59.9 ms: 1.01x slower                                                             |
| json_dumps           | 9.87 ms                                                                | 9.99 ms: 1.01x slower                                                             |
| pickle               | 10.5 us                                                                | 10.7 us: 1.02x slower                                                             |
| unpickle             | 15.0 us                                                                | 15.7 us: 1.05x slower                                                             |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 6.69 ms                                                                | 6.70 ms: 1.00x slower                                                             |
| python_startup         | 9.15 ms                                                                | 9.19 ms: 1.00x slower                                                             |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|-----------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako      | 10.7 ms                                                                | 10.6 ms: 1.01x faster                                                             |

All benchmarks:
===============

| Benchmark              | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff | bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7+-e472d94 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpack_sequence        | 58.6 ns                                                                | 47.9 ns: 1.22x faster                                                             |
| gc_traversal           | 4.37 ms                                                                | 3.97 ms: 1.10x faster                                                             |
| spectral_norm          | 107 ms                                                                 | 101 ms: 1.05x faster                                                              |
| mdp                    | 2.68 sec                                                               | 2.56 sec: 1.05x faster                                                            |
| sqlalchemy_imperative  | 19.4 ms                                                                | 18.9 ms: 1.02x faster                                                             |
| fannkuch               | 377 ms                                                                 | 372 ms: 1.01x faster                                                              |
| mako                   | 10.7 ms                                                                | 10.6 ms: 1.01x faster                                                             |
| coroutines             | 22.7 ms                                                                | 22.4 ms: 1.01x faster                                                             |
| deepcopy_reduce        | 3.21 us                                                                | 3.17 us: 1.01x faster                                                             |
| unpickle_pure_python   | 220 us                                                                 | 218 us: 1.01x faster                                                              |
| unpickle_list          | 4.99 us                                                                | 4.95 us: 1.01x faster                                                             |
| scimark_fft            | 358 ms                                                                 | 355 ms: 1.01x faster                                                              |
| coverage               | 102 ms                                                                 | 102 ms: 1.01x faster                                                              |
| pickle_dict            | 31.6 us                                                                | 31.4 us: 1.01x faster                                                             |
| xml_etree_iterparse    | 104 ms                                                                 | 104 ms: 1.01x faster                                                              |
| meteor_contest         | 105 ms                                                                 | 105 ms: 1.01x faster                                                              |
| docutils               | 2.73 sec                                                               | 2.72 sec: 1.00x faster                                                            |
| 2to3                   | 270 ms                                                                 | 270 ms: 1.00x slower                                                              |
| python_startup_no_site | 6.69 ms                                                                | 6.70 ms: 1.00x slower                                                             |
| python_startup         | 9.15 ms                                                                | 9.19 ms: 1.00x slower                                                             |
| deltablue              | 3.57 ms                                                                | 3.58 ms: 1.00x slower                                                             |
| dulwich_log            | 68.1 ms                                                                | 68.4 ms: 1.00x slower                                                             |
| bench_thread_pool      | 831 us                                                                 | 834 us: 1.00x slower                                                              |
| pickle_pure_python     | 316 us                                                                 | 318 us: 1.00x slower                                                              |
| generators             | 30.9 ms                                                                | 31.1 ms: 1.01x slower                                                             |
| chaos                  | 68.2 ms                                                                | 68.6 ms: 1.01x slower                                                             |
| json_loads             | 25.3 us                                                                | 25.5 us: 1.01x slower                                                             |
| go                     | 136 ms                                                                 | 137 ms: 1.01x slower                                                              |
| nqueens                | 79.5 ms                                                                | 80.1 ms: 1.01x slower                                                             |
| pickle_list            | 4.54 us                                                                | 4.58 us: 1.01x slower                                                             |
| float                  | 81.2 ms                                                                | 82.0 ms: 1.01x slower                                                             |
| asyncio_tcp            | 507 ms                                                                 | 513 ms: 1.01x slower                                                              |
| xml_etree_generate     | 84.9 ms                                                                | 85.9 ms: 1.01x slower                                                             |
| xml_etree_process      | 59.3 ms                                                                | 59.9 ms: 1.01x slower                                                             |
| json_dumps             | 9.87 ms                                                                | 9.99 ms: 1.01x slower                                                             |
| pprint_safe_repr       | 734 ms                                                                 | 744 ms: 1.01x slower                                                              |
| scimark_lu             | 113 ms                                                                 | 115 ms: 1.01x slower                                                              |
| hexiom                 | 6.11 ms                                                                | 6.21 ms: 1.01x slower                                                             |
| sqlite_synth           | 2.74 us                                                                | 2.78 us: 1.02x slower                                                             |
| pprint_pformat         | 1.50 sec                                                               | 1.53 sec: 1.02x slower                                                            |
| regex_dna              | 207 ms                                                                 | 211 ms: 1.02x slower                                                              |
| pickle                 | 10.5 us                                                                | 10.7 us: 1.02x slower                                                             |
| crypto_pyaes           | 77.8 ms                                                                | 79.6 ms: 1.02x slower                                                             |
| pathlib                | 18.8 ms                                                                | 19.3 ms: 1.02x slower                                                             |
| nbody                  | 90.6 ms                                                                | 93.1 ms: 1.03x slower                                                             |
| telco                  | 6.77 ms                                                                | 7.00 ms: 1.03x slower                                                             |
| logging_silent         | 102 ns                                                                 | 106 ns: 1.04x slower                                                              |
| regex_v8               | 22.0 ms                                                                | 22.8 ms: 1.04x slower                                                             |
| logging_format         | 7.05 us                                                                | 7.31 us: 1.04x slower                                                             |
| regex_effbot           | 3.60 ms                                                                | 3.74 ms: 1.04x slower                                                             |
| logging_simple         | 6.35 us                                                                | 6.61 us: 1.04x slower                                                             |
| pidigits               | 189 ms                                                                 | 197 ms: 1.05x slower                                                              |
| unpickle               | 15.0 us                                                                | 15.7 us: 1.05x slower                                                             |
| pycparser              | 1.16 sec                                                               | 1.21 sec: 1.05x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (27): richards, async_tree_cpu_io_mixed, scimark_sparse_mat_mult, deepcopy, async_tree_none, create_gc_cycles, comprehensions, dask, sqlglot_optimize, bench_mp_pool, deepcopy_memo, xml_etree_parse, sqlglot_transpile, sqlglot_normalize, scimark_sor, raytrace, scimark_monte_carlo, sqlglot_parse, sqlalchemy_declarative, pyflate, async_tree_memoization, mypy2, tornado_http, async_generators, async_tree_io, regex_compile, json
