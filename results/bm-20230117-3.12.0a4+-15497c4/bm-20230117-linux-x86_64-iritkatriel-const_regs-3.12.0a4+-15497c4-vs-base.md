
# Results vs. base

- fork: iritkatriel
- ref: const_regs
- machine: linux-x86_64
- commit hash: 15497c4
- commit date: 2023-01-17
- overall geometric mean: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 258 ms: 1.02x slower                                              |
| chameleon      | 6.31 ms                                                                | 6.50 ms: 1.03x slower                                             |
| docutils       | 2.50 sec                                                               | 2.61 sec: 1.04x slower                                            |
| html5lib       | 59.5 ms                                                                | 61.5 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 72.1 ms                                                                | 73.3 ms: 1.02x slower                                             |
| nbody          | 95.0 ms                                                                | 95.9 ms: 1.01x slower                                             |
| pidigits       | 192 ms                                                                 | 198 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 134 ms: 1.04x slower                                              |
| regex_effbot   | 3.60 ms                                                                | 3.53 ms: 1.02x faster                                             |
| regex_v8       | 22.0 ms                                                                | 22.5 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 9.37 ms                                                                | 9.45 ms: 1.01x slower                                             |
| json_loads           | 23.8 us                                                                | 24.0 us: 1.01x slower                                             |
| pickle               | 10.1 us                                                                | 10.4 us: 1.04x slower                                             |
| pickle_dict          | 30.4 us                                                                | 32.4 us: 1.07x slower                                             |
| pickle_list          | 4.07 us                                                                | 4.37 us: 1.07x slower                                             |
| pickle_pure_python   | 281 us                                                                 | 295 us: 1.05x slower                                              |
| unpickle             | 12.9 us                                                                | 13.1 us: 1.02x slower                                             |
| unpickle_pure_python | 200 us                                                                 | 203 us: 1.02x slower                                              |
| xml_etree_iterparse  | 109 ms                                                                 | 104 ms: 1.04x faster                                              |
| xml_etree_generate   | 76.8 ms                                                                | 77.5 ms: 1.01x slower                                             |
| xml_etree_process    | 53.8 ms                                                                | 54.1 ms: 1.01x slower                                             |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                      |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.50 ms                                                                | 8.58 ms: 1.01x slower                                             |
| python_startup_no_site | 6.06 ms                                                                | 6.11 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 32.3 ms                                                                | 34.0 ms: 1.05x slower                                             |
| genshi_text     | 20.2 ms                                                                | 21.1 ms: 1.04x slower                                             |
| genshi_xml      | 46.5 ms                                                                | 48.1 ms: 1.04x slower                                             |
| mako            | 9.78 ms                                                                | 9.85 ms: 1.01x slower                                             |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                      |

All benchmarks:
===============

| Benchmark              | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3                   | 253 ms                                                                 | 258 ms: 1.02x slower                                              |
| async_tree_memoization | 622 ms                                                                 | 659 ms: 1.06x slower                                              |
| chameleon              | 6.31 ms                                                                | 6.50 ms: 1.03x slower                                             |
| chaos                  | 66.7 ms                                                                | 68.9 ms: 1.03x slower                                             |
| bench_thread_pool      | 782 us                                                                 | 792 us: 1.01x slower                                              |
| coroutines             | 24.7 ms                                                                | 26.1 ms: 1.06x slower                                             |
| coverage               | 98.4 ms                                                                | 97.5 ms: 1.01x faster                                             |
| crypto_pyaes           | 75.1 ms                                                                | 76.8 ms: 1.02x slower                                             |
| dask                   | 491 ms                                                                 | 521 ms: 1.06x slower                                              |
| deepcopy               | 331 us                                                                 | 346 us: 1.05x slower                                              |
| deepcopy_reduce        | 2.88 us                                                                | 3.00 us: 1.04x slower                                             |
| deepcopy_memo          | 34.0 us                                                                | 35.8 us: 1.05x slower                                             |
| deltablue              | 3.24 ms                                                                | 3.39 ms: 1.05x slower                                             |
| django_template        | 32.3 ms                                                                | 34.0 ms: 1.05x slower                                             |
| docutils               | 2.50 sec                                                               | 2.61 sec: 1.04x slower                                            |
| dulwich_log            | 62.0 ms                                                                | 63.6 ms: 1.02x slower                                             |
| fannkuch               | 365 ms                                                                 | 379 ms: 1.04x slower                                              |
| float                  | 72.1 ms                                                                | 73.3 ms: 1.02x slower                                             |
| create_gc_cycles       | 1.45 ms                                                                | 1.43 ms: 1.01x faster                                             |
| gc_traversal           | 3.57 ms                                                                | 4.30 ms: 1.20x slower                                             |
| generators             | 79.3 ms                                                                | 76.3 ms: 1.04x faster                                             |
| genshi_text            | 20.2 ms                                                                | 21.1 ms: 1.04x slower                                             |
| genshi_xml             | 46.5 ms                                                                | 48.1 ms: 1.04x slower                                             |
| go                     | 136 ms                                                                 | 140 ms: 1.03x slower                                              |
| hexiom                 | 6.07 ms                                                                | 6.32 ms: 1.04x slower                                             |
| html5lib               | 59.5 ms                                                                | 61.5 ms: 1.04x slower                                             |
| json                   | 4.66 ms                                                                | 4.71 ms: 1.01x slower                                             |
| json_dumps             | 9.37 ms                                                                | 9.45 ms: 1.01x slower                                             |
| json_loads             | 23.8 us                                                                | 24.0 us: 1.01x slower                                             |
| logging_format         | 6.28 us                                                                | 6.51 us: 1.04x slower                                             |
| logging_silent         | 93.9 ns                                                                | 98.2 ns: 1.05x slower                                             |
| logging_simple         | 5.75 us                                                                | 5.90 us: 1.03x slower                                             |
| mako                   | 9.78 ms                                                                | 9.85 ms: 1.01x slower                                             |
| mdp                    | 2.44 sec                                                               | 2.57 sec: 1.05x slower                                            |
| nbody                  | 95.0 ms                                                                | 95.9 ms: 1.01x slower                                             |
| nqueens                | 79.6 ms                                                                | 83.5 ms: 1.05x slower                                             |
| pathlib                | 17.8 ms                                                                | 18.0 ms: 1.01x slower                                             |
| pickle                 | 10.1 us                                                                | 10.4 us: 1.04x slower                                             |
| pickle_dict            | 30.4 us                                                                | 32.4 us: 1.07x slower                                             |
| pickle_list            | 4.07 us                                                                | 4.37 us: 1.07x slower                                             |
| pickle_pure_python     | 281 us                                                                 | 295 us: 1.05x slower                                              |
| pidigits               | 192 ms                                                                 | 198 ms: 1.03x slower                                              |
| pprint_safe_repr       | 666 ms                                                                 | 704 ms: 1.06x slower                                              |
| pprint_pformat         | 1.38 sec                                                               | 1.42 sec: 1.03x slower                                            |
| pycparser              | 1.14 sec                                                               | 1.16 sec: 1.02x slower                                            |
| pyflate                | 393 ms                                                                 | 408 ms: 1.04x slower                                              |
| python_startup         | 8.50 ms                                                                | 8.58 ms: 1.01x slower                                             |
| python_startup_no_site | 6.06 ms                                                                | 6.11 ms: 1.01x slower                                             |
| raytrace               | 282 ms                                                                 | 296 ms: 1.05x slower                                              |
| regex_compile          | 129 ms                                                                 | 134 ms: 1.04x slower                                              |
| regex_effbot           | 3.60 ms                                                                | 3.53 ms: 1.02x faster                                             |
| regex_v8               | 22.0 ms                                                                | 22.5 ms: 1.02x slower                                             |
| richards               | 41.9 ms                                                                | 43.8 ms: 1.05x slower                                             |
| scimark_fft            | 312 ms                                                                 | 315 ms: 1.01x slower                                              |
| scimark_lu             | 107 ms                                                                 | 112 ms: 1.04x slower                                              |
| scimark_monte_carlo    | 64.2 ms                                                                | 64.9 ms: 1.01x slower                                             |
| scimark_sor            | 106 ms                                                                 | 109 ms: 1.03x slower                                              |
| sqlglot_parse          | 1.41 ms                                                                | 1.45 ms: 1.02x slower                                             |
| sqlglot_transpile      | 1.71 ms                                                                | 1.76 ms: 1.03x slower                                             |
| sqlglot_optimize       | 51.0 ms                                                                | 52.6 ms: 1.03x slower                                             |
| sqlglot_normalize      | 105 ms                                                                 | 109 ms: 1.03x slower                                              |
| sqlite_synth           | 2.57 us                                                                | 2.60 us: 1.01x slower                                             |
| sympy_expand           | 453 ms                                                                 | 474 ms: 1.05x slower                                              |
| sympy_integrate        | 20.2 ms                                                                | 22.1 ms: 1.09x slower                                             |
| sympy_sum              | 162 ms                                                                 | 167 ms: 1.03x slower                                              |
| sympy_str              | 280 ms                                                                 | 291 ms: 1.04x slower                                              |
| thrift                 | 751 us                                                                 | 758 us: 1.01x slower                                              |
| unpack_sequence        | 43.8 ns                                                                | 42.1 ns: 1.04x faster                                             |
| unpickle               | 12.9 us                                                                | 13.1 us: 1.02x slower                                             |
| unpickle_pure_python   | 200 us                                                                 | 203 us: 1.02x slower                                              |
| xml_etree_iterparse    | 109 ms                                                                 | 104 ms: 1.04x faster                                              |
| xml_etree_generate     | 76.8 ms                                                                | 77.5 ms: 1.01x slower                                             |
| xml_etree_process      | 53.8 ms                                                                | 54.1 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                                  | 1.03x slower                                                      |

Benchmark hidden because not significant (15): async_generators, async_tree_none, async_tree_cpu_io_mixed, async_tree_io, asyncio_tcp, bench_mp_pool, djangocms, meteor_contest, mypy, regex_dna, scimark_sparse_mat_mult, spectral_norm, telco, unpickle_list, xml_etree_parse
