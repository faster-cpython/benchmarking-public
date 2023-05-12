
# Results vs. base

- fork: brandtbucher
- ref: always_inline
- machine: linux-x86_64
- commit hash: 2cb76fa
- commit date: 2023-05-11
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230512-linux-x86_64-python-434db68ee31514ddc4aa-3.12.0a7+-434db68 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 270 ms                                                                 | 269 ms: 1.00x faster                                                  |
| docutils       | 2.70 sec                                                               | 2.72 sec: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230512-linux-x86_64-python-434db68ee31514ddc4aa-3.12.0a7+-434db68 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 89.3 ms                                                                | 88.8 ms: 1.01x faster                                                 |
| float          | 80.6 ms                                                                | 82.0 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230512-linux-x86_64-python-434db68ee31514ddc4aa-3.12.0a7+-434db68 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 206 ms                                                                 | 203 ms: 1.02x faster                                                  |
| regex_effbot   | 3.57 ms                                                                | 3.52 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230512-linux-x86_64-python-434db68ee31514ddc4aa-3.12.0a7+-434db68 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_list        | 5.03 us                                                                | 4.86 us: 1.04x faster                                                 |
| unpickle             | 15.0 us                                                                | 14.6 us: 1.03x faster                                                 |
| tomli_loads          | 2.24 sec                                                               | 2.19 sec: 1.02x faster                                                |
| xml_etree_process    | 60.1 ms                                                                | 59.2 ms: 1.01x faster                                                 |
| json_dumps           | 9.90 ms                                                                | 9.79 ms: 1.01x faster                                                 |
| unpickle_pure_python | 221 us                                                                 | 219 us: 1.01x faster                                                  |
| json_loads           | 25.2 us                                                                | 25.0 us: 1.01x faster                                                 |
| pickle_pure_python   | 317 us                                                                 | 314 us: 1.01x faster                                                  |
| xml_etree_parse      | 153 ms                                                                 | 154 ms: 1.01x slower                                                  |
| pickle               | 10.6 us                                                                | 10.8 us: 1.02x slower                                                 |
| pickle_list          | 4.51 us                                                                | 4.64 us: 1.03x slower                                                 |
| pickle_dict          | 31.0 us                                                                | 32.8 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230512-linux-x86_64-python-434db68ee31514ddc4aa-3.12.0a7+-434db68 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.67 ms                                                                | 6.71 ms: 1.01x slower                                                 |
| python_startup         | 9.13 ms                                                                | 9.20 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230512-linux-x86_64-python-434db68ee31514ddc4aa-3.12.0a7+-434db68 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|-----------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 11.0 ms                                                                | 10.8 ms: 1.01x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20230512-linux-x86_64-python-434db68ee31514ddc4aa-3.12.0a7+-434db68 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|--------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| scimark_sor              | 135 ms                                                                 | 123 ms: 1.09x faster                                                  |
| spectral_norm            | 109 ms                                                                 | 104 ms: 1.05x faster                                                  |
| generators               | 32.6 ms                                                                | 31.2 ms: 1.04x faster                                                 |
| unpickle_list            | 5.03 us                                                                | 4.86 us: 1.04x faster                                                 |
| unpickle                 | 15.0 us                                                                | 14.6 us: 1.03x faster                                                 |
| tomli_loads              | 2.24 sec                                                               | 2.19 sec: 1.02x faster                                                |
| crypto_pyaes             | 79.7 ms                                                                | 78.1 ms: 1.02x faster                                                 |
| regex_dna                | 206 ms                                                                 | 203 ms: 1.02x faster                                                  |
| xml_etree_process        | 60.1 ms                                                                | 59.2 ms: 1.01x faster                                                 |
| regex_effbot             | 3.57 ms                                                                | 3.52 ms: 1.01x faster                                                 |
| pyflate                  | 450 ms                                                                 | 444 ms: 1.01x faster                                                  |
| mako                     | 11.0 ms                                                                | 10.8 ms: 1.01x faster                                                 |
| json_dumps               | 9.90 ms                                                                | 9.79 ms: 1.01x faster                                                 |
| unpickle_pure_python     | 221 us                                                                 | 219 us: 1.01x faster                                                  |
| meteor_contest           | 106 ms                                                                 | 105 ms: 1.01x faster                                                  |
| async_tree_none          | 476 ms                                                                 | 471 ms: 1.01x faster                                                  |
| json_loads               | 25.2 us                                                                | 25.0 us: 1.01x faster                                                 |
| async_tree_memoization   | 578 ms                                                                 | 573 ms: 1.01x faster                                                  |
| hexiom                   | 6.26 ms                                                                | 6.21 ms: 1.01x faster                                                 |
| telco                    | 6.84 ms                                                                | 6.78 ms: 1.01x faster                                                 |
| pickle_pure_python       | 317 us                                                                 | 314 us: 1.01x faster                                                  |
| nbody                    | 89.3 ms                                                                | 88.8 ms: 1.01x faster                                                 |
| pprint_safe_repr         | 741 ms                                                                 | 736 ms: 1.01x faster                                                  |
| unpack_sequence          | 47.4 ns                                                                | 47.1 ns: 1.01x faster                                                 |
| async_tree_io            | 1.17 sec                                                               | 1.16 sec: 1.00x faster                                                |
| comprehensions           | 21.0 us                                                                | 20.9 us: 1.00x faster                                                 |
| 2to3                     | 270 ms                                                                 | 269 ms: 1.00x faster                                                  |
| asyncio_tcp              | 517 ms                                                                 | 516 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl          | 1.80 sec                                                               | 1.80 sec: 1.00x faster                                                |
| chaos                    | 65.4 ms                                                                | 65.6 ms: 1.00x slower                                                 |
| sqlglot_normalize        | 109 ms                                                                 | 109 ms: 1.00x slower                                                  |
| docutils                 | 2.70 sec                                                               | 2.72 sec: 1.01x slower                                                |
| xml_etree_parse          | 153 ms                                                                 | 154 ms: 1.01x slower                                                  |
| python_startup_no_site   | 6.67 ms                                                                | 6.71 ms: 1.01x slower                                                 |
| python_startup           | 9.13 ms                                                                | 9.20 ms: 1.01x slower                                                 |
| sqlglot_parse            | 1.34 ms                                                                | 1.35 ms: 1.01x slower                                                 |
| coverage                 | 95.6 ms                                                                | 96.5 ms: 1.01x slower                                                 |
| async_generators         | 455 ms                                                                 | 459 ms: 1.01x slower                                                  |
| raytrace                 | 299 ms                                                                 | 302 ms: 1.01x slower                                                  |
| nqueens                  | 81.0 ms                                                                | 82.0 ms: 1.01x slower                                                 |
| pickle                   | 10.6 us                                                                | 10.8 us: 1.02x slower                                                 |
| logging_silent           | 101 ns                                                                 | 103 ns: 1.02x slower                                                  |
| float                    | 80.6 ms                                                                | 82.0 ms: 1.02x slower                                                 |
| scimark_fft              | 353 ms                                                                 | 359 ms: 1.02x slower                                                  |
| create_gc_cycles         | 1.47 ms                                                                | 1.50 ms: 1.02x slower                                                 |
| scimark_lu               | 115 ms                                                                 | 118 ms: 1.02x slower                                                  |
| typing_runtime_protocols | 144 us                                                                 | 148 us: 1.03x slower                                                  |
| pickle_list              | 4.51 us                                                                | 4.64 us: 1.03x slower                                                 |
| coroutines               | 21.8 ms                                                                | 23.0 ms: 1.05x slower                                                 |
| pickle_dict              | 31.0 us                                                                | 32.8 us: 1.06x slower                                                 |
| gc_traversal             | 3.52 ms                                                                | 3.83 ms: 1.09x slower                                                 |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (34): regex_compile, async_tree_cpu_io_mixed, richards, json, sqlalchemy_declarative, deepcopy_reduce, mypy2, xml_etree_generate, dulwich_log, pathlib, pprint_pformat, sqlalchemy_imperative, deepcopy, bench_thread_pool, bench_mp_pool, dask, sqlglot_optimize, regex_v8, xml_etree_iterparse, pidigits, deltablue, go, richards_super, sqlglot_transpile, fannkuch, tornado_http, scimark_sparse_mat_mult, mdp, scimark_monte_carlo, logging_simple, logging_format, deepcopy_memo, sqlite_synth, pycparser
