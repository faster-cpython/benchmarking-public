
# Results vs. base

- fork: brandtbucher
- ref: remove_old_branch
- machine: linux-x86_64
- commit hash: b1845b6
- commit date: 2023-01-18
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 251 ms: 1.00x faster                                                      |
| docutils       | 2.58 sec                                                               | 2.51 sec: 1.03x faster                                                    |
| html5lib       | 60.5 ms                                                                | 59.6 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 93.9 ms                                                                | 92.8 ms: 1.01x faster                                                     |
| float          | 72.1 ms                                                                | 72.5 ms: 1.01x slower                                                     |
| pidigits       | 189 ms                                                                 | 192 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 127 ms: 1.01x faster                                                      |
| regex_dna      | 211 ms                                                                 | 210 ms: 1.00x faster                                                      |
| regex_effbot   | 3.57 ms                                                                | 3.64 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_list      | 5.18 us                                                                | 5.01 us: 1.03x faster                                                     |
| pickle_pure_python | 283 us                                                                 | 285 us: 1.01x slower                                                      |
| json_loads         | 23.7 us                                                                | 23.9 us: 1.01x slower                                                     |
| xml_etree_process  | 53.7 ms                                                                | 54.1 ms: 1.01x slower                                                     |
| json_dumps         | 9.30 ms                                                                | 9.42 ms: 1.01x slower                                                     |
| pickle             | 10.1 us                                                                | 10.2 us: 1.01x slower                                                     |
| xml_etree_parse    | 148 ms                                                                 | 151 ms: 1.03x slower                                                      |
| unpickle           | 13.0 us                                                                | 13.4 us: 1.04x slower                                                     |
| pickle_dict        | 30.0 us                                                                | 31.9 us: 1.06x slower                                                     |
| pickle_list        | 4.00 us                                                                | 4.27 us: 1.07x slower                                                     |
| Geometric mean     | (ref)                                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.93 ms                                                                | 8.96 ms: 1.00x slower                                                     |
| python_startup_no_site | 6.45 ms                                                                | 6.48 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 32.7 ms                                                                | 32.4 ms: 1.01x faster                                                     |
| genshi_xml      | 47.4 ms                                                                | 47.0 ms: 1.01x faster                                                     |
| genshi_text     | 20.8 ms                                                                | 20.6 ms: 1.01x faster                                                     |
| mako            | 9.64 ms                                                                | 9.70 ms: 1.01x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                              |

All benchmarks:
===============

| Benchmark              | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4+-b1845b6 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pyflate                | 416 ms                                                                 | 397 ms: 1.05x faster                                                      |
| coroutines             | 25.9 ms                                                                | 24.8 ms: 1.04x faster                                                     |
| go                     | 138 ms                                                                 | 133 ms: 1.04x faster                                                      |
| unpickle_list          | 5.18 us                                                                | 5.01 us: 1.03x faster                                                     |
| docutils               | 2.58 sec                                                               | 2.51 sec: 1.03x faster                                                    |
| html5lib               | 60.5 ms                                                                | 59.6 ms: 1.02x faster                                                     |
| logging_format         | 6.45 us                                                                | 6.36 us: 1.01x faster                                                     |
| deepcopy               | 330 us                                                                 | 326 us: 1.01x faster                                                      |
| pprint_safe_repr       | 684 ms                                                                 | 676 ms: 1.01x faster                                                      |
| asyncio_tcp            | 495 ms                                                                 | 489 ms: 1.01x faster                                                      |
| nbody                  | 93.9 ms                                                                | 92.8 ms: 1.01x faster                                                     |
| raytrace               | 286 ms                                                                 | 283 ms: 1.01x faster                                                      |
| meteor_contest         | 105 ms                                                                 | 104 ms: 1.01x faster                                                      |
| scimark_monte_carlo    | 65.8 ms                                                                | 65.1 ms: 1.01x faster                                                     |
| regex_compile          | 129 ms                                                                 | 127 ms: 1.01x faster                                                      |
| json                   | 4.63 ms                                                                | 4.59 ms: 1.01x faster                                                     |
| deepcopy_memo          | 34.2 us                                                                | 33.9 us: 1.01x faster                                                     |
| django_template        | 32.7 ms                                                                | 32.4 ms: 1.01x faster                                                     |
| genshi_xml             | 47.4 ms                                                                | 47.0 ms: 1.01x faster                                                     |
| deepcopy_reduce        | 2.93 us                                                                | 2.91 us: 1.01x faster                                                     |
| logging_simple         | 5.80 us                                                                | 5.76 us: 1.01x faster                                                     |
| thrift                 | 743 us                                                                 | 738 us: 1.01x faster                                                      |
| genshi_text            | 20.8 ms                                                                | 20.6 ms: 1.01x faster                                                     |
| scimark_fft            | 305 ms                                                                 | 303 ms: 1.01x faster                                                      |
| sqlglot_optimize       | 51.2 ms                                                                | 50.9 ms: 1.01x faster                                                     |
| bench_thread_pool      | 778 us                                                                 | 774 us: 1.00x faster                                                      |
| sympy_sum              | 155 ms                                                                 | 155 ms: 1.00x faster                                                      |
| regex_dna              | 211 ms                                                                 | 210 ms: 1.00x faster                                                      |
| sympy_integrate        | 19.7 ms                                                                | 19.6 ms: 1.00x faster                                                     |
| dulwich_log            | 62.2 ms                                                                | 62.0 ms: 1.00x faster                                                     |
| 2to3                   | 252 ms                                                                 | 251 ms: 1.00x faster                                                      |
| python_startup         | 8.93 ms                                                                | 8.96 ms: 1.00x slower                                                     |
| python_startup_no_site | 6.45 ms                                                                | 6.48 ms: 1.00x slower                                                     |
| float                  | 72.1 ms                                                                | 72.5 ms: 1.01x slower                                                     |
| scimark_sor            | 105 ms                                                                 | 106 ms: 1.01x slower                                                      |
| async_generators       | 353 ms                                                                 | 355 ms: 1.01x slower                                                      |
| nqueens                | 76.2 ms                                                                | 76.7 ms: 1.01x slower                                                     |
| pickle_pure_python     | 283 us                                                                 | 285 us: 1.01x slower                                                      |
| mako                   | 9.64 ms                                                                | 9.70 ms: 1.01x slower                                                     |
| chaos                  | 63.9 ms                                                                | 64.3 ms: 1.01x slower                                                     |
| sqlglot_normalize      | 105 ms                                                                 | 105 ms: 1.01x slower                                                      |
| json_loads             | 23.7 us                                                                | 23.9 us: 1.01x slower                                                     |
| coverage               | 96.3 ms                                                                | 97.0 ms: 1.01x slower                                                     |
| xml_etree_process      | 53.7 ms                                                                | 54.1 ms: 1.01x slower                                                     |
| logging_silent         | 90.8 ns                                                                | 91.6 ns: 1.01x slower                                                     |
| unpack_sequence        | 41.3 ns                                                                | 41.7 ns: 1.01x slower                                                     |
| deltablue              | 3.19 ms                                                                | 3.22 ms: 1.01x slower                                                     |
| hexiom                 | 5.96 ms                                                                | 6.02 ms: 1.01x slower                                                     |
| json_dumps             | 9.30 ms                                                                | 9.42 ms: 1.01x slower                                                     |
| sqlite_synth           | 2.58 us                                                                | 2.61 us: 1.01x slower                                                     |
| mdp                    | 2.66 sec                                                               | 2.69 sec: 1.01x slower                                                    |
| pickle                 | 10.1 us                                                                | 10.2 us: 1.01x slower                                                     |
| spectral_norm          | 96.2 ms                                                                | 97.6 ms: 1.01x slower                                                     |
| pidigits               | 189 ms                                                                 | 192 ms: 1.02x slower                                                      |
| crypto_pyaes           | 71.4 ms                                                                | 72.6 ms: 1.02x slower                                                     |
| regex_effbot           | 3.57 ms                                                                | 3.64 ms: 1.02x slower                                                     |
| fannkuch               | 355 ms                                                                 | 362 ms: 1.02x slower                                                      |
| generators             | 75.2 ms                                                                | 76.9 ms: 1.02x slower                                                     |
| xml_etree_parse        | 148 ms                                                                 | 151 ms: 1.03x slower                                                      |
| pathlib                | 17.6 ms                                                                | 18.1 ms: 1.03x slower                                                     |
| create_gc_cycles       | 1.44 ms                                                                | 1.48 ms: 1.03x slower                                                     |
| unpickle               | 13.0 us                                                                | 13.4 us: 1.04x slower                                                     |
| pickle_dict            | 30.0 us                                                                | 31.9 us: 1.06x slower                                                     |
| pickle_list            | 4.00 us                                                                | 4.27 us: 1.07x slower                                                     |
| gc_traversal           | 3.82 ms                                                                | 4.30 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (26): async_tree_memoization, scimark_lu, xml_etree_iterparse, tornado_http, scimark_sparse_mat_mult, richards, telco, pycparser, gunicorn, regex_v8, sympy_str, mypy, dask, sympy_expand, bench_mp_pool, aiohttp, async_tree_io, sqlglot_transpile, async_tree_none, async_tree_cpu_io_mixed, xml_etree_generate, pprint_pformat, unpickle_pure_python, sqlglot_parse, chameleon, djangocms
