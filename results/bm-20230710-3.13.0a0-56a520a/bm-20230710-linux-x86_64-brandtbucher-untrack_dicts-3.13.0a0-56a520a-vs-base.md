
# Results vs. base

- fork: brandtbucher
- ref: untrack_dicts
- machine: linux-x86_64
- commit hash: 56a520a
- commit date: 2023-07-10
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230710-linux-x86_64-python-a840806d338805fe74a9-3.13.0a0-a840806 | bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 197 ms                                                                | 197 ms: 1.00x slower                                                 |
| nbody          | 88.2 ms                                                               | 94.1 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230710-linux-x86_64-python-a840806d338805fe74a9-3.13.0a0-a840806 | bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.49 ms                                                               | 3.52 ms: 1.01x slower                                                |
| regex_dna      | 208 ms                                                                | 213 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                         |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230710-linux-x86_64-python-a840806d338805fe74a9-3.13.0a0-a840806 | bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle             | 10.6 us                                                               | 10.4 us: 1.02x faster                                                |
| json_dumps         | 9.85 ms                                                               | 9.64 ms: 1.02x faster                                                |
| pickle_list        | 4.48 us                                                               | 4.39 us: 1.02x faster                                                |
| pickle_pure_python | 294 us                                                                | 291 us: 1.01x faster                                                 |
| pickle_dict        | 31.9 us                                                               | 31.7 us: 1.01x faster                                                |
| unpickle           | 14.8 us                                                               | 15.0 us: 1.01x slower                                                |
| xml_etree_process  | 57.7 ms                                                               | 58.5 ms: 1.01x slower                                                |
| xml_etree_parse    | 151 ms                                                                | 154 ms: 1.02x slower                                                 |
| xml_etree_generate | 83.9 ms                                                               | 85.7 ms: 1.02x slower                                                |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (5): unpickle_list, unpickle_pure_python, tomli_loads, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230710-linux-x86_64-python-a840806d338805fe74a9-3.13.0a0-a840806 | bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 9.23 ms                                                               | 9.21 ms: 1.00x faster                                                |
| python_startup_no_site | 6.72 ms                                                               | 6.71 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230710-linux-x86_64-python-a840806d338805fe74a9-3.13.0a0-a840806 | bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a |
|-----------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako      | 10.8 ms                                                               | 10.9 ms: 1.01x slower                                                |

All benchmarks:
===============

| Benchmark                | bm-20230710-linux-x86_64-python-a840806d338805fe74a9-3.13.0a0-a840806 | bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| gc_traversal             | 4.21 ms                                                               | 3.91 ms: 1.08x faster                                                |
| mdp                      | 2.71 sec                                                              | 2.55 sec: 1.06x faster                                               |
| scimark_lu               | 112 ms                                                                | 109 ms: 1.03x faster                                                 |
| logging_silent           | 103 ns                                                                | 100 ns: 1.02x faster                                                 |
| pickle                   | 10.6 us                                                               | 10.4 us: 1.02x faster                                                |
| json_dumps               | 9.85 ms                                                               | 9.64 ms: 1.02x faster                                                |
| async_tree_io            | 1.19 sec                                                              | 1.17 sec: 1.02x faster                                               |
| pickle_list              | 4.48 us                                                               | 4.39 us: 1.02x faster                                                |
| coverage                 | 93.5 ms                                                               | 92.0 ms: 1.02x faster                                                |
| pprint_safe_repr         | 734 ms                                                                | 722 ms: 1.02x faster                                                 |
| pyflate                  | 450 ms                                                                | 443 ms: 1.02x faster                                                 |
| pprint_pformat           | 1.50 sec                                                              | 1.48 sec: 1.01x faster                                               |
| generators               | 28.8 ms                                                               | 28.4 ms: 1.01x faster                                                |
| logging_format           | 6.60 us                                                               | 6.51 us: 1.01x faster                                                |
| async_tree_memoization   | 589 ms                                                                | 581 ms: 1.01x faster                                                 |
| deepcopy_memo            | 38.0 us                                                               | 37.6 us: 1.01x faster                                                |
| async_tree_none          | 483 ms                                                                | 478 ms: 1.01x faster                                                 |
| pickle_pure_python       | 294 us                                                                | 291 us: 1.01x faster                                                 |
| json                     | 4.89 ms                                                               | 4.84 ms: 1.01x faster                                                |
| logging_simple           | 5.93 us                                                               | 5.88 us: 1.01x faster                                                |
| meteor_contest           | 105 ms                                                                | 104 ms: 1.01x faster                                                 |
| pickle_dict              | 31.9 us                                                               | 31.7 us: 1.01x faster                                                |
| spectral_norm            | 108 ms                                                                | 107 ms: 1.01x faster                                                 |
| deepcopy_reduce          | 3.17 us                                                               | 3.15 us: 1.01x faster                                                |
| asyncio_tcp              | 510 ms                                                                | 508 ms: 1.00x faster                                                 |
| mypy2                    | 336 ms                                                                | 335 ms: 1.00x faster                                                 |
| scimark_fft              | 353 ms                                                                | 352 ms: 1.00x faster                                                 |
| python_startup           | 9.23 ms                                                               | 9.21 ms: 1.00x faster                                                |
| asyncio_tcp_ssl          | 1.78 sec                                                              | 1.78 sec: 1.00x faster                                               |
| python_startup_no_site   | 6.72 ms                                                               | 6.71 ms: 1.00x faster                                                |
| pidigits                 | 197 ms                                                                | 197 ms: 1.00x slower                                                 |
| coroutines               | 22.1 ms                                                               | 22.1 ms: 1.00x slower                                                |
| go                       | 137 ms                                                                | 137 ms: 1.00x slower                                                 |
| chaos                    | 58.9 ms                                                               | 59.2 ms: 1.00x slower                                                |
| scimark_sor              | 120 ms                                                                | 121 ms: 1.01x slower                                                 |
| hexiom                   | 5.95 ms                                                               | 6.01 ms: 1.01x slower                                                |
| pathlib                  | 18.8 ms                                                               | 18.9 ms: 1.01x slower                                                |
| regex_effbot             | 3.49 ms                                                               | 3.52 ms: 1.01x slower                                                |
| mako                     | 10.8 ms                                                               | 10.9 ms: 1.01x slower                                                |
| create_gc_cycles         | 1.51 ms                                                               | 1.52 ms: 1.01x slower                                                |
| unpickle                 | 14.8 us                                                               | 15.0 us: 1.01x slower                                                |
| deltablue                | 3.26 ms                                                               | 3.31 ms: 1.01x slower                                                |
| richards                 | 46.3 ms                                                               | 46.9 ms: 1.01x slower                                                |
| xml_etree_process        | 57.7 ms                                                               | 58.5 ms: 1.01x slower                                                |
| comprehensions           | 20.2 us                                                               | 20.5 us: 1.01x slower                                                |
| fannkuch                 | 387 ms                                                                | 393 ms: 1.02x slower                                                 |
| richards_super           | 52.4 ms                                                               | 53.4 ms: 1.02x slower                                                |
| xml_etree_parse          | 151 ms                                                                | 154 ms: 1.02x slower                                                 |
| regex_dna                | 208 ms                                                                | 213 ms: 1.02x slower                                                 |
| typing_runtime_protocols | 147 us                                                                | 150 us: 1.02x slower                                                 |
| xml_etree_generate       | 83.9 ms                                                               | 85.7 ms: 1.02x slower                                                |
| unpack_sequence          | 43.8 ns                                                               | 44.7 ns: 1.02x slower                                                |
| nqueens                  | 79.3 ms                                                               | 81.7 ms: 1.03x slower                                                |
| nbody                    | 88.2 ms                                                               | 94.1 ms: 1.07x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (28): async_tree_cpu_io_mixed, raytrace, sqlite_synth, pycparser, async_generators, scimark_monte_carlo, unpickle_list, unpickle_pure_python, dulwich_log, deepcopy, tornado_http, crypto_pyaes, tomli_loads, dask, bench_thread_pool, float, scimark_sparse_mat_mult, bench_mp_pool, regex_compile, docutils, sqlglot_parse, json_loads, sqlglot_normalize, xml_etree_iterparse, regex_v8, sqlglot_optimize, sqlglot_transpile, telco
