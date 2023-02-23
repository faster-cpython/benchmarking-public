
# Results vs. base

- fork: iritkatriel
- ref: fetch_restore
- machine: linux-x86_64
- commit hash: 19b61a7
- commit date: 2023-02-23
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230223-linux-x86_64-python-c3a178398c199038f3a0-3.12.0a5+-c3a1783 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 251 ms: 1.00x slower                                                 |
| chameleon      | 6.32 ms                                                                | 6.48 ms: 1.03x slower                                                |
| docutils       | 2.54 sec                                                               | 2.55 sec: 1.00x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230223-linux-x86_64-python-c3a178398c199038f3a0-3.12.0a5+-c3a1783 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.3 ms                                                                | 93.6 ms: 1.04x faster                                                |
| float          | 72.5 ms                                                                | 73.5 ms: 1.01x slower                                                |
| pidigits       | 189 ms                                                                 | 193 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230223-linux-x86_64-python-c3a178398c199038f3a0-3.12.0a5+-c3a1783 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.79 ms                                                                | 3.27 ms: 1.16x faster                                                |
| regex_dna      | 214 ms                                                                 | 210 ms: 1.02x faster                                                 |
| regex_v8       | 22.3 ms                                                                | 22.1 ms: 1.01x faster                                                |
| regex_compile  | 132 ms                                                                 | 133 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230223-linux-x86_64-python-c3a178398c199038f3a0-3.12.0a5+-c3a1783 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                                 | 98.5 ms: 1.05x faster                                                |
| json_dumps           | 9.65 ms                                                                | 9.34 ms: 1.03x faster                                                |
| pickle_list          | 4.05 us                                                                | 3.92 us: 1.03x faster                                                |
| pickle               | 10.2 us                                                                | 9.95 us: 1.03x faster                                                |
| unpickle_list        | 5.02 us                                                                | 4.91 us: 1.02x faster                                                |
| xml_etree_parse      | 151 ms                                                                 | 148 ms: 1.02x faster                                                 |
| pickle_dict          | 30.6 us                                                                | 30.1 us: 1.02x faster                                                |
| xml_etree_process    | 55.1 ms                                                                | 55.8 ms: 1.01x slower                                                |
| xml_etree_generate   | 80.1 ms                                                                | 81.5 ms: 1.02x slower                                                |
| unpickle_pure_python | 197 us                                                                 | 203 us: 1.03x slower                                                 |
| pickle_pure_python   | 284 us                                                                 | 293 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (2): json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230223-linux-x86_64-python-c3a178398c199038f3a0-3.12.0a5+-c3a1783 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 8.98 ms                                                                | 8.97 ms: 1.00x faster                                                |
| python_startup_no_site | 6.51 ms                                                                | 6.51 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230223-linux-x86_64-python-c3a178398c199038f3a0-3.12.0a5+-c3a1783 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml     | 47.4 ms                                                                | 48.1 ms: 1.01x slower                                                |
| genshi_text    | 20.8 ms                                                                | 21.5 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark              | bm-20230223-linux-x86_64-python-c3a178398c199038f3a0-3.12.0a5+-c3a1783 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot           | 3.79 ms                                                                | 3.27 ms: 1.16x faster                                                |
| coroutines             | 23.6 ms                                                                | 22.3 ms: 1.06x faster                                                |
| unpack_sequence        | 44.0 ns                                                                | 41.9 ns: 1.05x faster                                                |
| xml_etree_iterparse    | 103 ms                                                                 | 98.5 ms: 1.05x faster                                                |
| nbody                  | 97.3 ms                                                                | 93.6 ms: 1.04x faster                                                |
| json_dumps             | 9.65 ms                                                                | 9.34 ms: 1.03x faster                                                |
| mdp                    | 2.61 sec                                                               | 2.53 sec: 1.03x faster                                               |
| pickle_list            | 4.05 us                                                                | 3.92 us: 1.03x faster                                                |
| pickle                 | 10.2 us                                                                | 9.95 us: 1.03x faster                                                |
| unpickle_list          | 5.02 us                                                                | 4.91 us: 1.02x faster                                                |
| pycparser              | 1.14 sec                                                               | 1.12 sec: 1.02x faster                                               |
| xml_etree_parse        | 151 ms                                                                 | 148 ms: 1.02x faster                                                 |
| pickle_dict            | 30.6 us                                                                | 30.1 us: 1.02x faster                                                |
| regex_dna              | 214 ms                                                                 | 210 ms: 1.02x faster                                                 |
| scimark_monte_carlo    | 67.1 ms                                                                | 66.2 ms: 1.01x faster                                                |
| logging_format         | 6.60 us                                                                | 6.51 us: 1.01x faster                                                |
| async_generators       | 416 ms                                                                 | 411 ms: 1.01x faster                                                 |
| pathlib                | 17.8 ms                                                                | 17.6 ms: 1.01x faster                                                |
| telco                  | 6.48 ms                                                                | 6.42 ms: 1.01x faster                                                |
| regex_v8               | 22.3 ms                                                                | 22.1 ms: 1.01x faster                                                |
| meteor_contest         | 104 ms                                                                 | 103 ms: 1.01x faster                                                 |
| dulwich_log            | 63.5 ms                                                                | 63.3 ms: 1.00x faster                                                |
| pyflate                | 412 ms                                                                 | 411 ms: 1.00x faster                                                 |
| python_startup         | 8.98 ms                                                                | 8.97 ms: 1.00x faster                                                |
| python_startup_no_site | 6.51 ms                                                                | 6.51 ms: 1.00x slower                                                |
| bench_thread_pool      | 792 us                                                                 | 794 us: 1.00x slower                                                 |
| docutils               | 2.54 sec                                                               | 2.55 sec: 1.00x slower                                               |
| aiohttp                | 1.01 ms                                                                | 1.01 ms: 1.00x slower                                                |
| 2to3                   | 250 ms                                                                 | 251 ms: 1.00x slower                                                 |
| mypy2                  | 332 ms                                                                 | 334 ms: 1.00x slower                                                 |
| sqlglot_optimize       | 50.9 ms                                                                | 51.2 ms: 1.01x slower                                                |
| crypto_pyaes           | 73.3 ms                                                                | 73.8 ms: 1.01x slower                                                |
| chaos                  | 68.0 ms                                                                | 68.5 ms: 1.01x slower                                                |
| regex_compile          | 132 ms                                                                 | 133 ms: 1.01x slower                                                 |
| sympy_integrate        | 20.6 ms                                                                | 20.7 ms: 1.01x slower                                                |
| sympy_sum              | 166 ms                                                                 | 168 ms: 1.01x slower                                                 |
| fannkuch               | 364 ms                                                                 | 367 ms: 1.01x slower                                                 |
| xml_etree_process      | 55.1 ms                                                                | 55.8 ms: 1.01x slower                                                |
| sqlglot_parse          | 1.43 ms                                                                | 1.44 ms: 1.01x slower                                                |
| dask                   | 503 ms                                                                 | 509 ms: 1.01x slower                                                 |
| go                     | 135 ms                                                                 | 136 ms: 1.01x slower                                                 |
| sympy_str              | 283 ms                                                                 | 287 ms: 1.01x slower                                                 |
| float                  | 72.5 ms                                                                | 73.5 ms: 1.01x slower                                                |
| genshi_xml             | 47.4 ms                                                                | 48.1 ms: 1.01x slower                                                |
| pidigits               | 189 ms                                                                 | 193 ms: 1.02x slower                                                 |
| sqlglot_transpile      | 1.71 ms                                                                | 1.74 ms: 1.02x slower                                                |
| deltablue              | 3.18 ms                                                                | 3.24 ms: 1.02x slower                                                |
| xml_etree_generate     | 80.1 ms                                                                | 81.5 ms: 1.02x slower                                                |
| scimark_lu             | 108 ms                                                                 | 110 ms: 1.02x slower                                                 |
| sympy_expand           | 457 ms                                                                 | 465 ms: 1.02x slower                                                 |
| hexiom                 | 6.10 ms                                                                | 6.22 ms: 1.02x slower                                                |
| thrift                 | 763 us                                                                 | 779 us: 1.02x slower                                                 |
| deepcopy               | 333 us                                                                 | 341 us: 1.02x slower                                                 |
| spectral_norm          | 93.7 ms                                                                | 95.9 ms: 1.02x slower                                                |
| deepcopy_memo          | 34.7 us                                                                | 35.6 us: 1.02x slower                                                |
| chameleon              | 6.32 ms                                                                | 6.48 ms: 1.03x slower                                                |
| generators             | 29.7 ms                                                                | 30.5 ms: 1.03x slower                                                |
| deepcopy_reduce        | 3.00 us                                                                | 3.08 us: 1.03x slower                                                |
| unpickle_pure_python   | 197 us                                                                 | 203 us: 1.03x slower                                                 |
| raytrace               | 281 ms                                                                 | 289 ms: 1.03x slower                                                 |
| logging_silent         | 92.5 ns                                                                | 95.4 ns: 1.03x slower                                                |
| nqueens                | 79.2 ms                                                                | 81.6 ms: 1.03x slower                                                |
| pickle_pure_python     | 284 us                                                                 | 293 us: 1.03x slower                                                 |
| scimark_sor            | 105 ms                                                                 | 109 ms: 1.03x slower                                                 |
| genshi_text            | 20.8 ms                                                                | 21.5 ms: 1.03x slower                                                |
| richards               | 41.4 ms                                                                | 43.4 ms: 1.05x slower                                                |
| gc_traversal           | 3.66 ms                                                                | 4.07 ms: 1.11x slower                                                |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (26): djangocms, async_tree_cpu_io_mixed, logging_simple, async_tree_io, create_gc_cycles, scimark_fft, mako, async_tree_none, tornado_http, bench_mp_pool, scimark_sparse_mat_mult, sqlglot_normalize, json_loads, asyncio_tcp, pprint_pformat, sqlite_synth, pprint_safe_repr, gunicorn, sqlalchemy_declarative, django_template, coverage, sqlalchemy_imperative, json, html5lib, async_tree_memoization, unpickle
