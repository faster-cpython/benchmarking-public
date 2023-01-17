
# Results vs. base

- fork: iritkatriel
- ref: const_regs
- machine: linux-x86_64
- commit hash: 80ea135
- commit date: 2023-01-16
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 259 ms: 1.02x slower                                              |
| docutils       | 2.50 sec                                                               | 2.62 sec: 1.05x slower                                            |
| html5lib       | 59.5 ms                                                                | 61.5 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                      |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 72.1 ms                                                                | 74.1 ms: 1.03x slower                                             |
| nbody          | 95.0 ms                                                                | 96.2 ms: 1.01x slower                                             |
| pidigits       | 192 ms                                                                 | 198 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 134 ms: 1.04x slower                                              |
| regex_dna      | 211 ms                                                                 | 217 ms: 1.03x slower                                              |
| regex_effbot   | 3.60 ms                                                                | 3.63 ms: 1.01x slower                                             |
| regex_v8       | 22.0 ms                                                                | 22.2 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 9.37 ms                                                                | 9.44 ms: 1.01x slower                                             |
| json_loads           | 23.8 us                                                                | 24.1 us: 1.01x slower                                             |
| pickle               | 10.1 us                                                                | 10.2 us: 1.01x slower                                             |
| pickle_dict          | 30.4 us                                                                | 31.1 us: 1.02x slower                                             |
| pickle_pure_python   | 281 us                                                                 | 297 us: 1.06x slower                                              |
| unpickle             | 12.9 us                                                                | 13.2 us: 1.02x slower                                             |
| unpickle_list        | 4.98 us                                                                | 5.00 us: 1.00x slower                                             |
| unpickle_pure_python | 200 us                                                                 | 203 us: 1.02x slower                                              |
| xml_etree_iterparse  | 109 ms                                                                 | 103 ms: 1.06x faster                                              |
| xml_etree_generate   | 76.8 ms                                                                | 78.4 ms: 1.02x slower                                             |
| xml_etree_process    | 53.8 ms                                                                | 54.5 ms: 1.01x slower                                             |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                      |

Benchmark hidden because not significant (2): pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.50 ms                                                                | 8.57 ms: 1.01x slower                                             |
| python_startup_no_site | 6.06 ms                                                                | 6.11 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 32.3 ms                                                                | 34.3 ms: 1.06x slower                                             |
| genshi_text     | 20.2 ms                                                                | 21.2 ms: 1.05x slower                                             |
| genshi_xml      | 46.5 ms                                                                | 47.6 ms: 1.03x slower                                             |
| mako            | 9.78 ms                                                                | 9.60 ms: 1.02x faster                                             |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                      |

All benchmarks:
===============

| Benchmark               | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3                    | 253 ms                                                                 | 259 ms: 1.02x slower                                              |
| async_generators        | 357 ms                                                                 | 359 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed | 753 ms                                                                 | 760 ms: 1.01x slower                                              |
| async_tree_io           | 1.31 sec                                                               | 1.33 sec: 1.02x slower                                            |
| async_tree_memoization  | 622 ms                                                                 | 668 ms: 1.07x slower                                              |
| chaos                   | 66.7 ms                                                                | 69.0 ms: 1.03x slower                                             |
| bench_thread_pool       | 782 us                                                                 | 794 us: 1.01x slower                                              |
| coroutines              | 24.7 ms                                                                | 25.8 ms: 1.04x slower                                             |
| coverage                | 98.4 ms                                                                | 97.7 ms: 1.01x faster                                             |
| crypto_pyaes            | 75.1 ms                                                                | 76.8 ms: 1.02x slower                                             |
| dask                    | 491 ms                                                                 | 518 ms: 1.05x slower                                              |
| deepcopy                | 331 us                                                                 | 343 us: 1.04x slower                                              |
| deepcopy_reduce         | 2.88 us                                                                | 3.05 us: 1.06x slower                                             |
| deepcopy_memo           | 34.0 us                                                                | 35.6 us: 1.05x slower                                             |
| deltablue               | 3.24 ms                                                                | 3.39 ms: 1.05x slower                                             |
| django_template         | 32.3 ms                                                                | 34.3 ms: 1.06x slower                                             |
| docutils                | 2.50 sec                                                               | 2.62 sec: 1.05x slower                                            |
| dulwich_log             | 62.0 ms                                                                | 63.5 ms: 1.02x slower                                             |
| float                   | 72.1 ms                                                                | 74.1 ms: 1.03x slower                                             |
| create_gc_cycles        | 1.45 ms                                                                | 1.46 ms: 1.01x slower                                             |
| gc_traversal            | 3.57 ms                                                                | 3.80 ms: 1.06x slower                                             |
| generators              | 79.3 ms                                                                | 76.1 ms: 1.04x faster                                             |
| genshi_text             | 20.2 ms                                                                | 21.2 ms: 1.05x slower                                             |
| genshi_xml              | 46.5 ms                                                                | 47.6 ms: 1.03x slower                                             |
| go                      | 136 ms                                                                 | 141 ms: 1.04x slower                                              |
| hexiom                  | 6.07 ms                                                                | 6.31 ms: 1.04x slower                                             |
| html5lib                | 59.5 ms                                                                | 61.5 ms: 1.03x slower                                             |
| json_dumps              | 9.37 ms                                                                | 9.44 ms: 1.01x slower                                             |
| json_loads              | 23.8 us                                                                | 24.1 us: 1.01x slower                                             |
| logging_format          | 6.28 us                                                                | 6.51 us: 1.04x slower                                             |
| logging_silent          | 93.9 ns                                                                | 99.3 ns: 1.06x slower                                             |
| logging_simple          | 5.75 us                                                                | 5.89 us: 1.02x slower                                             |
| mako                    | 9.78 ms                                                                | 9.60 ms: 1.02x faster                                             |
| mdp                     | 2.44 sec                                                               | 2.59 sec: 1.06x slower                                            |
| nbody                   | 95.0 ms                                                                | 96.2 ms: 1.01x slower                                             |
| nqueens                 | 79.6 ms                                                                | 79.3 ms: 1.00x faster                                             |
| pickle                  | 10.1 us                                                                | 10.2 us: 1.01x slower                                             |
| pickle_dict             | 30.4 us                                                                | 31.1 us: 1.02x slower                                             |
| pickle_pure_python      | 281 us                                                                 | 297 us: 1.06x slower                                              |
| pidigits                | 192 ms                                                                 | 198 ms: 1.03x slower                                              |
| pprint_safe_repr        | 666 ms                                                                 | 689 ms: 1.03x slower                                              |
| pprint_pformat          | 1.38 sec                                                               | 1.40 sec: 1.02x slower                                            |
| pycparser               | 1.14 sec                                                               | 1.16 sec: 1.02x slower                                            |
| pyflate                 | 393 ms                                                                 | 402 ms: 1.02x slower                                              |
| python_startup          | 8.50 ms                                                                | 8.57 ms: 1.01x slower                                             |
| python_startup_no_site  | 6.06 ms                                                                | 6.11 ms: 1.01x slower                                             |
| raytrace                | 282 ms                                                                 | 298 ms: 1.06x slower                                              |
| regex_compile           | 129 ms                                                                 | 134 ms: 1.04x slower                                              |
| regex_dna               | 211 ms                                                                 | 217 ms: 1.03x slower                                              |
| regex_effbot            | 3.60 ms                                                                | 3.63 ms: 1.01x slower                                             |
| regex_v8                | 22.0 ms                                                                | 22.2 ms: 1.01x slower                                             |
| richards                | 41.9 ms                                                                | 44.3 ms: 1.06x slower                                             |
| scimark_fft             | 312 ms                                                                 | 311 ms: 1.01x faster                                              |
| scimark_lu              | 107 ms                                                                 | 111 ms: 1.03x slower                                              |
| scimark_monte_carlo     | 64.2 ms                                                                | 65.1 ms: 1.01x slower                                             |
| scimark_sor             | 106 ms                                                                 | 110 ms: 1.04x slower                                              |
| scimark_sparse_mat_mult | 4.03 ms                                                                | 4.15 ms: 1.03x slower                                             |
| spectral_norm           | 96.4 ms                                                                | 98.1 ms: 1.02x slower                                             |
| sqlglot_parse           | 1.41 ms                                                                | 1.47 ms: 1.04x slower                                             |
| sqlglot_transpile       | 1.71 ms                                                                | 1.77 ms: 1.04x slower                                             |
| sqlglot_optimize        | 51.0 ms                                                                | 52.7 ms: 1.03x slower                                             |
| sqlglot_normalize       | 105 ms                                                                 | 109 ms: 1.03x slower                                              |
| sympy_expand            | 453 ms                                                                 | 473 ms: 1.04x slower                                              |
| sympy_integrate         | 20.2 ms                                                                | 22.1 ms: 1.10x slower                                             |
| sympy_sum               | 162 ms                                                                 | 168 ms: 1.04x slower                                              |
| sympy_str               | 280 ms                                                                 | 291 ms: 1.04x slower                                              |
| telco                   | 6.37 ms                                                                | 6.28 ms: 1.01x faster                                             |
| thrift                  | 751 us                                                                 | 745 us: 1.01x faster                                              |
| unpack_sequence         | 43.8 ns                                                                | 44.5 ns: 1.02x slower                                             |
| unpickle                | 12.9 us                                                                | 13.2 us: 1.02x slower                                             |
| unpickle_list           | 4.98 us                                                                | 5.00 us: 1.00x slower                                             |
| unpickle_pure_python    | 200 us                                                                 | 203 us: 1.02x slower                                              |
| xml_etree_iterparse     | 109 ms                                                                 | 103 ms: 1.06x faster                                              |
| xml_etree_generate      | 76.8 ms                                                                | 78.4 ms: 1.02x slower                                             |
| xml_etree_process       | 53.8 ms                                                                | 54.5 ms: 1.01x slower                                             |
| Geometric mean          | (ref)                                                                  | 1.02x slower                                                      |

Benchmark hidden because not significant (13): async_tree_none, asyncio_tcp, chameleon, bench_mp_pool, djangocms, fannkuch, json, meteor_contest, mypy, pathlib, pickle_list, sqlite_synth, xml_etree_parse
